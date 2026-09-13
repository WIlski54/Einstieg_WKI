"""KI-Anbindung: Gemini-Client, Prompts, Freigabeprüfung, Sperren und Token-Buchung.

Prüfreihenfolge jeder KI-Route (Standard §18.2):
1. persistente Einzel- oder Gruppensperre
2. globales Tagesbudget
3. aktive Zeitspanne der Gruppenfreigabe
4. erlaubter Funktionstyp
5. Klassenzuordnung
6. Gruppenbudget
7. persönliches Budget
8. andernfalls gültige Einzelanfrage
"""

import datetime as dt
import json
import re

from config import AI_MODEL, AI_REQUEST_TYPES, APP_TITEL, DAILY_TOKEN_LIMIT, GEMINI_API_KEY
from db import get_db, now_iso

try:
    from google import genai
    from google.genai import types as genai_types
except ImportError:  # Die App bleibt ohne KI-Abhängigkeit nutzbar.
    genai = None
    genai_types = None

AI_CLIENT = genai.Client(api_key=GEMINI_API_KEY) if genai and GEMINI_API_KEY else None


def konfiguriert() -> bool:
    return AI_CLIENT is not None


# ── Prompts ──────────────────────────────────────────────────────────────────
SYSTEM_PROMPT = f"""Du bist ein freundlicher Geschichts-Tutor für Schülerinnen und Schüler der Klasse 9
(Klassenunterricht, heterogene Lerngruppe) an der Gesamtschule Meiderich in Duisburg.
Thema der Stunde: {APP_TITEL} – Ursachen, Auslöser, Verlauf, Kriegsende und Folgen.
Wichtige Fachbegriffe: Imperialismus, Nationalismus, Militarismus, Wettrüsten, Bündnissystem
(Dreibund, Triple Entente), Pulverfass Balkan, Attentat von Sarajevo, Julikrise, Blankoscheck,
Ultimatum, Mobilmachung, Schlieffen-Plan, Zweifrontenkrieg, Marneschlacht, Stellungskrieg,
Materialschlacht (Verdun, Somme), Giftgas, U-Boot-Krieg, Kriegseintritt der USA, totaler Krieg,
Heimatfront, Russische Revolution, Brest-Litowsk, Frühjahrsoffensive, Oberste Heeresleitung,
Matrosenaufstand, Novemberrevolution, Waffenstillstand von Compiègne, Dolchstoßlegende,
14 Punkte Wilsons, Versailler Vertrag, Artikel 231, Reparationen, Völkerbund, Urkatastrophe.
Regeln:
- Erkläre auf dem Niveau einer 9. Klasse (Gesamtschule), anschaulich und mit Beispielen.
- Gib KEINE fertigen Lösungen für Aufgaben – stelle Rückfragen und gib Denkanstöße.
- Unterstütze bei der Recherche: nenne verlässliche Quellen (Schulbuch, bpb.de, LeMO des
  Deutschen Historischen Museums, Planet Wissen) und erkläre, woran man verlässliche Quellen erkennt.
- Achte auf die zeitliche Ordnung der Ereignisse und korrigiere falsche Jahreszahlen behutsam.
- Antworte auf Deutsch, in maximal 3–4 Sätzen, ermutigend und respektvoll. Du darfst **fett** für
  Fachbegriffe verwenden, sonst kein Markdown.
- Transparenz: Du bist eine KI, das ist den Lernenden bekannt."""

KORREKTUR_PROMPT = f"""Du bist eine einfühlsame Geschichtslehrkraft (Klasse 9, Gesamtschule Meiderich Duisburg).
Thema: {APP_TITEL}. Bewerte die Schülerantwort pädagogisch:
1. Lobe konkret, was RICHTIG ist – nenne richtige Begriffe, Daten und Zusammenhänge beim Namen.
2. Weise sanft auf sachliche Fehler, falsche Jahreszahlen oder Lücken hin – nie abwertend.
3. Bei unvollständigen Antworten: gib einen Hinweis, der weiterhilft, NICHT die komplette Lösung.
4. Bei Recherche-Stichpunkten: prüfe auch die zeitliche Ordnung und ob Quellen genannt sind.
5. Antworte auf Deutsch, ermutigend, maximal 3–4 Sätze.
6. Antworte NUR als JSON ohne Markdown: {{"correct": true|false|null, "feedback": "dein Text", "hint": "optionaler Tipp"}}
   correct=true, wenn die Antwort im Kern richtig und ausreichend ist; false bei sachlichen Fehlern;
   null, wenn es sich um eine Meinung/Beurteilung handelt, die man nicht als richtig/falsch bewerten kann."""

ZEICHNUNG_PROMPT = f"""Du bist eine Geschichtslehrkraft (Klasse 9, Gesamtschule). Thema: {APP_TITEL}.
Du siehst die Skizze einer Schülerin oder eines Schülers zu einem Zeichenauftrag. Bewerte pädagogisch:
1. Beschreibe kurz, was du erkennst (Formen, Beschriftungen, Pfeile).
2. Nenne, welche geforderten Elemente vorhanden sind und welche fehlen.
3. Gib genau einen konkreten Verbesserungstipp – keine fertige Lösung.
4. Antworte NUR als JSON ohne Markdown: {{"sterne": 0-3, "erkannt": ["…"], "fehlt": ["…"], "feedback": "2–4 Sätze in direkter Anrede"}}"""

HANDSCHRIFT_PROMPT = """Du bist ein Transkriptionswerkzeug. Das Bild zeigt handschriftliche Stichpunkte
einer Schülerin oder eines Schülers (Deutsch, Thema Erster Weltkrieg). Gib AUSSCHLIESSLICH den erkannten
Text zurück, Zeile für Zeile, ohne Kommentar, ohne Anführungszeichen, ohne Markdown. Unleserliche Stellen
als [?] markieren. Erfinde nichts dazu."""


# ── Gemini-Aufrufe ──────────────────────────────────────────────────────────
def generate(contents: str, system_instruction: str):
    return AI_CLIENT.models.generate_content(
        model=AI_MODEL,
        contents=contents,
        config=genai_types.GenerateContentConfig(system_instruction=system_instruction),
    )


def generate_mit_bild(prompt: str, png_bytes: bytes, system_instruction: str):
    bild = genai_types.Part.from_bytes(data=png_bytes, mime_type="image/png")
    return AI_CLIENT.models.generate_content(
        model=AI_MODEL,
        contents=[prompt, bild],
        config=genai_types.GenerateContentConfig(system_instruction=system_instruction),
    )


def estimate_tokens(text: str) -> int:
    return max(1, len(text) // 4)


def response_token_count(response, fallback_text: str) -> int:
    """Provider-Metadaten bevorzugen, nur ohne sie schätzen."""
    usage = getattr(response, "usage_metadata", None)
    total = getattr(usage, "total_token_count", None) if usage else None
    return int(total) if total else estimate_tokens(fallback_text)


def parse_json_response(text: str) -> dict:
    cleaned = re.sub(r"^```(?:json)?|```$", "", text.strip(), flags=re.I | re.M).strip()
    try:
        result = json.loads(cleaned)
        if not isinstance(result, dict):
            raise ValueError
    except (json.JSONDecodeError, ValueError):
        return {"correct": None, "feedback": cleaned[:900], "hint": ""}
    return {
        "correct": result.get("correct") if isinstance(result.get("correct"), bool) else None,
        "feedback": str(result.get("feedback", ""))[:900],
        "hint": str(result.get("hint", ""))[:400],
    }


def parse_zeichnung_response(text: str) -> dict:
    cleaned = re.sub(r"^```(?:json)?|```$", "", text.strip(), flags=re.I | re.M).strip()
    try:
        result = json.loads(cleaned)
        if not isinstance(result, dict):
            raise ValueError
    except (json.JSONDecodeError, ValueError):
        return {"sterne": None, "erkannt": [], "fehlt": [], "feedback": cleaned[:900]}
    sterne = result.get("sterne")
    return {
        "sterne": int(sterne) if isinstance(sterne, (int, float)) and 0 <= sterne <= 3 else None,
        "erkannt": [str(x)[:120] for x in (result.get("erkannt") or []) if x][:8],
        "fehlt": [str(x)[:120] for x in (result.get("fehlt") or []) if x][:8],
        "feedback": str(result.get("feedback", ""))[:900],
    }


# ── Tagesbudget ─────────────────────────────────────────────────────────────
def get_today_tokens() -> int:
    today = dt.date.today().isoformat()
    with get_db() as db:
        row = db.execute("SELECT tokens_used FROM token_budget WHERE datum=?", (today,)).fetchone()
    return int(row["tokens_used"]) if row else 0


def add_tokens(count: int) -> None:
    today = dt.date.today().isoformat()
    with get_db() as db:
        db.execute(
            "INSERT INTO token_budget (datum, tokens_used) VALUES (?, ?) "
            "ON CONFLICT(datum) DO UPDATE SET tokens_used = tokens_used + ?",
            (today, count, count),
        )
        db.commit()


def budget_ok() -> bool:
    return get_today_tokens() < DAILY_TOKEN_LIMIT


def budget_payload() -> dict:
    return {"today": get_today_tokens(), "limit": DAILY_TOKEN_LIMIT}


# ── Einzelsperren (persistent) ──────────────────────────────────────────────
def ist_gesperrt(sid: str) -> bool:
    with get_db() as db:
        return db.execute("SELECT 1 FROM ki_sperren WHERE schueler_id=?", (sid,)).fetchone() is not None


def sperren(sid: str) -> None:
    with get_db() as db:
        db.execute("INSERT OR IGNORE INTO ki_sperren (schueler_id, gesperrt_at) VALUES (?, ?)", (sid, now_iso()))
        db.execute(
            "UPDATE ki_anfragen SET status='abgelehnt', bearbeitet_at=? WHERE schueler_id=? AND status='wartend'",
            (now_iso(), sid),
        )
        db.commit()


def entsperren(sid: str) -> None:
    with get_db() as db:
        db.execute("DELETE FROM ki_sperren WHERE schueler_id=?", (sid,))
        db.commit()


def gesperrte_ids() -> list[str]:
    with get_db() as db:
        return sorted(r["schueler_id"] for r in db.execute("SELECT schueler_id FROM ki_sperren").fetchall())


# ── Gruppenfreigabe ─────────────────────────────────────────────────────────
GRUPPE_DEFAULT = {
    "active": 0, "locked": 0, "klasse": "", "allowed_types": "[]", "starts_at": None,
    "expires_at": None, "token_limit": 0, "tokens_used": 0, "per_student_limit": 0,
}


def gruppenfreigabe_lesen() -> dict:
    with get_db() as db:
        row = db.execute("SELECT * FROM ki_gruppenfreigabe WHERE id=1").fetchone()
    data = dict(GRUPPE_DEFAULT, **dict(row)) if row else dict(GRUPPE_DEFAULT)
    data.pop("id", None)
    try:
        typen = json.loads(data.get("allowed_types") or "[]")
    except json.JSONDecodeError:
        typen = []
    data["typen"] = [t for t in typen if t in AI_REQUEST_TYPES]
    data["active"] = bool(data["active"])
    data["locked"] = bool(data["locked"])
    if data["active"] and data["expires_at"] and data["expires_at"] < now_iso():
        data["active"] = False
        data["abgelaufen"] = True
    if data["active"] and data["token_limit"] and data["tokens_used"] >= data["token_limit"]:
        data["active"] = False
        data["budget_erschoepft"] = True
    return data


def gruppenfreigabe_setzen(typen, klasse: str, minuten: int, token_limit: int, per_student_limit: int) -> dict:
    typen = [t for t in (typen or []) if t in AI_REQUEST_TYPES]
    minuten = max(1, min(int(minuten or 45), 24 * 60))
    start = dt.datetime.now()
    ende = start + dt.timedelta(minutes=minuten)
    with get_db() as db:
        db.execute(
            "INSERT OR REPLACE INTO ki_gruppenfreigabe (id, active, locked, klasse, allowed_types, starts_at, expires_at, "
            "token_limit, tokens_used, per_student_limit) VALUES (1, 1, 0, ?, ?, ?, ?, ?, 0, ?)",
            (
                str(klasse or "").strip()[:20], json.dumps(typen), start.isoformat(timespec="seconds"),
                ende.isoformat(timespec="seconds"), max(0, int(token_limit or 0)), max(0, int(per_student_limit or 0)),
            ),
        )
        db.execute("DELETE FROM ki_gruppen_nutzung")
        db.commit()
    return gruppenfreigabe_lesen()


def gruppenfreigabe_beenden() -> dict:
    with get_db() as db:
        db.execute("UPDATE ki_gruppenfreigabe SET active=0 WHERE id=1")
        db.commit()
    return gruppenfreigabe_lesen()


def gruppe_sperren() -> dict:
    """Sofort wirksam, persistent; lehnt wartende Einzelanfragen ab (Standard §18.2)."""
    with get_db() as db:
        db.execute(
            "INSERT INTO ki_gruppenfreigabe (id, active, locked) VALUES (1, 0, 1) "
            "ON CONFLICT(id) DO UPDATE SET active=0, locked=1"
        )
        db.execute("UPDATE ki_anfragen SET status='abgelehnt', bearbeitet_at=? WHERE status='wartend'", (now_iso(),))
        db.commit()
    return gruppenfreigabe_lesen()


def gruppe_entsperren() -> dict:
    with get_db() as db:
        db.execute("UPDATE ki_gruppenfreigabe SET locked=0 WHERE id=1")
        db.commit()
    return gruppenfreigabe_lesen()


def gruppen_nutzung(sid: str) -> int:
    with get_db() as db:
        row = db.execute("SELECT tokens FROM ki_gruppen_nutzung WHERE schueler_id=?", (sid,)).fetchone()
    return int(row["tokens"]) if row else 0


# ── Freigabeprüfung ─────────────────────────────────────────────────────────
def ensure_ai_request(request_id, typ: str, sid: str):
    """Liefert die freigegebene Einzelanfrage oder None."""
    try:
        request_id = int(request_id)
    except (TypeError, ValueError):
        return None
    with get_db() as db:
        row = db.execute("SELECT * FROM ki_anfragen WHERE id=?", (request_id,)).fetchone()
    if not row or row["schueler_id"] != sid or row["typ"] != typ or row["status"] != "freigegeben":
        return None
    return row


def ki_pruefen(sid: str, klasse: str, typ: str, anfrage_id=None) -> dict:
    """Serverseitige Prüfung in verbindlicher Reihenfolge. Liefert {ok, quelle, grund, anfrage}."""
    gruppe = gruppenfreigabe_lesen()
    if gruppe["locked"]:
        return {"ok": False, "quelle": None, "grund": "Die Lehrkraft hat die KI für die Gruppe gesperrt.", "anfrage": None}
    if ist_gesperrt(sid):
        return {"ok": False, "quelle": None, "grund": "Der KI-Zugang ist für diesen Lernplatz gesperrt.", "anfrage": None}
    if not budget_ok():
        return {"ok": False, "quelle": None, "grund": "Das Token-Budget für heute ist erschöpft.", "anfrage": None}
    if gruppe["active"]:
        jetzt = now_iso()
        zeit_ok = (gruppe["starts_at"] or "") <= jetzt <= (gruppe["expires_at"] or "9999")
        typ_ok = typ in gruppe["typen"]
        klasse_ok = not gruppe["klasse"] or gruppe["klasse"].strip().lower() == str(klasse or "").strip().lower()
        gruppen_budget_ok = not gruppe["token_limit"] or gruppe["tokens_used"] < gruppe["token_limit"]
        persoenlich_ok = not gruppe["per_student_limit"] or gruppen_nutzung(sid) < gruppe["per_student_limit"]
        if zeit_ok and typ_ok and klasse_ok and gruppen_budget_ok and persoenlich_ok:
            return {"ok": True, "quelle": "gruppe", "grund": "", "anfrage": None}
    anfrage = ensure_ai_request(anfrage_id, typ, sid)
    if anfrage:
        return {"ok": True, "quelle": "einzel", "grund": "", "anfrage": anfrage}
    return {"ok": False, "quelle": None, "grund": "Noch nicht freigegeben.", "anfrage": None}


def tokens_buchen(sid: str, tokens: int, quelle: str, anfrage_id=None) -> None:
    add_tokens(tokens)
    with get_db() as db:
        if quelle == "gruppe":
            db.execute("UPDATE ki_gruppenfreigabe SET tokens_used=tokens_used+? WHERE id=1", (tokens,))
            db.execute(
                "INSERT INTO ki_gruppen_nutzung (schueler_id, tokens) VALUES (?, ?) "
                "ON CONFLICT(schueler_id) DO UPDATE SET tokens=tokens+?",
                (sid, tokens, tokens),
            )
        elif anfrage_id is not None:
            db.execute("UPDATE ki_anfragen SET token_count=token_count+? WHERE id=?", (tokens, anfrage_id))
        db.commit()


def chat_speichern(sid: str, typ: str, frage: str, antwort: str, tokens: int) -> str:
    zeit = now_iso()
    with get_db() as db:
        db.execute(
            "INSERT INTO chat_messages (schueler_id, typ, frage, antwort, tokens, erstellt_at) VALUES (?,?,?,?,?,?)",
            (sid, typ, frage[:1500], antwort[:3000], int(tokens or 0), zeit),
        )
        db.commit()
    return zeit


def chat_verlauf(sid: str, limit: int = 100) -> list[dict]:
    with get_db() as db:
        rows = db.execute(
            "SELECT typ, frage, antwort, tokens, erstellt_at FROM chat_messages WHERE schueler_id=? ORDER BY id DESC LIMIT ?",
            (sid, limit),
        ).fetchall()
    return [dict(r) for r in reversed(rows)]
