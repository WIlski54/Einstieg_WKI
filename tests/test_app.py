import json
import os
import re

import app as appmodule
import db as dbmod
from config import ABSCHNITTE, ALLE_AUFGABEN
from conftest import anmelden, session_werte

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["ok"] is True and data["ki"] is False


def test_login_requires_privacy_and_pseudonym(client):
    resp = client.post("/login", data={"pseudonym": "A", "klasse": "9", "privacy_ok": "on"})
    assert "mindestens 2 Zeichen" in resp.get_data(as_text=True)
    resp = client.post("/login", data={"pseudonym": "Fuchs", "klasse": "9"})
    assert "Datenschutz" in resp.get_data(as_text=True)
    assert client.get("/arbeitsblatt").status_code == 302
    assert client.get("/api/status").status_code == 401


def test_student_page_and_status(student):
    page = student.get("/arbeitsblatt")
    assert page.status_code == 200
    html = page.get_data(as_text=True)
    assert "Der Erste Weltkrieg" in html
    assert "inhalte.js" in html and "app.js" in html
    assert session_werte(student)["resume_token"] in html  # Token wandert in den Browser-Storage
    status = student.get("/api/status").get_json()
    assert status["ok"] and status["erledigt"] == [] and status["aufgaben_gesamt"] == len(ALLE_AUFGABEN) == 54
    assert status["ki_konfiguriert"] is False and status["autosave"] is None


def test_fortschritt_and_abschnitte(student):
    assert student.post("/api/fortschritt", json={"aufgabe": 1, "niveau": "B"}).get_json()["ok"]
    assert student.post("/api/fortschritt", json={"aufgabe": "T"}).get_json()["ok"]
    assert student.post("/api/fortschritt", json={"aufgabe": "l1", "niveau": "A"}).get_json()["ok"]
    assert student.post("/api/fortschritt", json={"aufgabe": 1, "niveau": "B"}).get_json()["erledigt"] == 3
    assert student.post("/api/fortschritt", json={"aufgabe": 99, "niveau": "A"}).status_code == 400
    assert student.post("/api/fortschritt", json={"aufgabe": 2, "niveau": "X"}).status_code == 400
    status = student.get("/api/status").get_json()
    assert {e["nr"] for e in status["erledigt"]} == {"1", "T", "L1"}
    sid = session_werte(student)["schueler_id"]
    info = appmodule.get_schueler_info(sid)
    assert info["aufgaben_erledigt"] == 3
    assert info["abschnitte"]["ursachen"]["erledigt"] == 2
    assert info["abschnitte"]["abschluss"]["erledigt"] == 1
    assert info["abschnitte"]["abschluss"]["gesamt"] == 6


def test_antwort_protokoll_mit_frage(student):
    r1 = student.post("/api/antwort", json={"aufgabe": 3, "niveau": "A", "typ": "zuordnung", "frage": "Welches Beispiel passt?", "antwort": "✅ Imperialismus → Kolonien", "korrekt": True}).get_json()
    r2 = student.post("/api/antwort", json={"aufgabe": 3, "niveau": "A", "typ": "zuordnung", "antwort": "❌ falsch", "korrekt": False}).get_json()
    assert r1["versuch"] == 1 and r2["versuch"] == 2 and r2["gesamt"] == 2
    assert student.post("/api/antwort", json={"aufgabe": 3, "niveau": "A", "typ": "unbekannt", "antwort": "x"}).status_code == 400
    rows = dbmod.get_db().execute("SELECT korrekt, versuch_nr, frage FROM antworten ORDER BY id").fetchall()
    assert [(r["korrekt"], r["versuch_nr"]) for r in rows] == [(1, 1), (0, 2)]
    assert rows[0]["frage"] == "Welches Beispiel passt?"


def test_teacher_pages_and_auth(student, teacher, client):
    assert client.get("/api/lehrer/state").status_code == 401
    assert client.get("/lehrer").status_code == 302
    with appmodule.app.test_client() as anon:
        assert "Falsches Passwort" in anon.post("/lehrer/login", data={"passwort": "nope"}).get_data(as_text=True)
    student.post("/api/fortschritt", json={"aufgabe": 10, "niveau": "C"})
    dash = teacher.get("/lehrer").get_data(as_text=True)
    assert "student-table" in dash
    sid = session_werte(student)["schueler_id"]
    detail = teacher.get(f"/lehrer/schueler/{sid}").get_data(as_text=True)
    assert "Silberfuchs" in detail and 'id="tile-10"' in detail and "niv-C" in detail
    assert teacher.get("/lehrer/schueler/unbekannt").status_code == 302
    state = teacher.get("/api/lehrer/state").get_json()
    assert state["ok"] and {k for k in state} >= {"schueler", "anfragen", "budget", "gesperrt", "gruppenfreigabe", "snapshots", "fortsetzung", "iserv"}


def test_daten_loeschen_und_reset(student, teacher):
    sid = session_werte(student)["schueler_id"]
    student.post("/api/fortschritt", json={"aufgabe": 1, "niveau": "A"})
    assert teacher.post("/api/lehrer/daten-loeschen", json={"schueler_id": sid}).get_json()["ok"]
    db = dbmod.get_db()
    for table in ("schueler", "fortschritt"):
        assert db.execute(f"SELECT COUNT(*) AS n FROM {table}").fetchone()["n"] == 0
    assert student.get("/api/status").status_code == 401
    anmelden(appmodule.app.test_client(), "Zweiter", "9b")
    assert teacher.post("/api/lehrer/sitzung-zuruecksetzen").get_json()["geloescht"] == 1


def test_kein_loeschen_beim_start(student):
    """Ein Neustart (init_db) darf die laufende Sitzung nicht löschen (Standard §6)."""
    student.post("/api/fortschritt", json={"aufgabe": 1, "niveau": "A"})
    dbmod.init_db()
    assert dbmod.get_db().execute("SELECT COUNT(*) AS n FROM schueler").fetchone()["n"] == 1
    assert dbmod.get_db().execute("SELECT COUNT(*) AS n FROM fortschritt").fetchone()["n"] == 1


def test_lehrer_login_ohne_passwortkonfiguration(monkeypatch, client):
    monkeypatch.setattr(appmodule, "LEHRER_PASSWORD", "")
    resp = client.post("/lehrer/login", data={"passwort": "irgendwas"})
    assert "nicht gesetzt" in resp.get_data(as_text=True)


def _ids(html: str) -> list[str]:
    return re.findall(r'\sid="([^"]+)"', html)


def test_keine_doppelten_html_ids(student, teacher):
    """Standard §23.1: keine doppelten HTML-IDs in gerenderten Seiten."""
    sid = session_werte(student)["schueler_id"]
    seiten = {
        "login": appmodule.app.test_client().get("/login"),
        "arbeitsblatt": student.get("/arbeitsblatt"),
        "warten": student.get("/warten"),
        "lehrer_login": appmodule.app.test_client().get("/lehrer/login"),
        "dashboard": teacher.get("/lehrer"),
        "detail": teacher.get(f"/lehrer/schueler/{sid}"),
    }
    for name, resp in seiten.items():
        assert resp.status_code == 200, name
        ids = _ids(resp.get_data(as_text=True))
        doppelt = {i for i in ids if ids.count(i) > 1}
        assert not doppelt, f"{name}: doppelte IDs {doppelt}"


def test_inhalte_js_passt_zur_serverstruktur():
    """Die Aufgabennummern in inhalte.js müssen zu ABSCHNITTE in config.py passen."""
    src = open(os.path.join(ROOT, "static", "js", "inhalte.js"), encoding="utf-8").read()
    tabs_src = src.split("tabs: [", 1)[1]
    blocks = re.split(r'\n\s*key: "', tabs_src)[1:]
    gefunden = {}
    for block in blocks:
        key = block.split('"', 1)[0]
        nrs = re.findall(r'\bnr: (\d+|"T")', block)
        gefunden[key] = {int(n) if n.isdigit() else "T" for n in nrs}
    erwartet = {a["key"]: {n for n in a["aufgaben"] if not str(n).startswith("L")} for a in ABSCHNITTE}
    assert set(gefunden) == set(erwartet)
    for key in erwartet:
        assert gefunden[key] == erwartet[key], key
    for block in blocks:
        key = block.split('"', 1)[0]
        typen = set(re.findall(r'typ: "([a-z]+)"', block))
        if key == "abschluss":
            assert {"sortierung", "mc", "blitz", "domino", "quellen", "transfer"} <= typen
        else:
            assert {"mc", "luecke", "zuordnung", "sortierung", "diagramm", "karte", "freitext", "notizen"} <= typen, key


def test_inhalte_niveaus_complete():
    src = open(os.path.join(ROOT, "static", "js", "inhalte.js"), encoding="utf-8").read()
    differenziert = re.findall(r'typ: "(mc|luecke|zuordnung|sortierung|diagramm|karte|freitext|zeichnen)"', src)
    assert len(differenziert) == 40
    assert src.count("niveaus: {") == len(differenziert)
    for niveau in ("A: {", "B: {", "C: {"):
        assert src.count(niveau) >= len(differenziert)
    for block in re.findall(r'\{ (?:multi: 2, )?frage: "[^"]+", optionen: \[(.*?)\] \}', src, flags=re.S):
        oks = block.count("ok: true")
        assert oks in (1, 2)
    # Blitzfragen: stabile, eindeutige IDs
    ids = re.findall(r'\{ id: "(b\d+)"', src)
    assert len(ids) >= 20 and len(ids) == len(set(ids))
    dom = re.findall(r'\{ id: "(d\d+)"', src)
    assert len(dom) >= 10 and len(dom) == len(set(dom))
