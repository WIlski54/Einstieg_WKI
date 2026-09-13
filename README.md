# Der Erste Weltkrieg (1914–1918) – Interaktives Arbeitsblatt

Digitale Vollversion des Recherche-Arbeitsblatts „Der Erste Weltkrieg (1914–1918)“ für
Geschichte, Klasse 9 (Klassenunterricht), Gesamtschule Meiderich. Umgesetzt nach dem
GSM-Produktionsstandard „Interaktives Arbeitsblatt mit Autosave und IServ-Archivierung“
(Stand September 2026): Flask + Socket.IO, SQLite-WAL, iPad-first.

## Was die App kann

**Lernende**

- pseudonymer Lernplatz mit sicherer Wiederaufnahme (Resume-Token, kein Fingerprinting)
- 54 Stationen in sechs Reitern: fünf Lesestrecken (L1–L5, Lösungen nur auf dem Server),
  Multiple Choice, Lückentext, Zuordnung, Sortierung, Diagramme, Karten mit echten Küstenlinien,
  Freitext, Recherche-Stichpunkte, drei Zeichenaufträge (Fabric.js), Blitzfragen ohne Wiederholung,
  Begriffs-Domino, Quellenverzeichnis, Transferaufgabe
- A/B/C-Differenzierung pro Aufgabe – der Niveauwechsel ändert nur die jeweilige Karte
- Schrittmodus: immer nur eine Station offen, erledigte klappen zusammen, spätere bleiben
  ausgeblendet; „Später machen“ überspringt, die Reiter werden nacheinander freigeschaltet
- Sprache auf Sek-I-Niveau: kurze Sätze, wenig Text, Fakten unverändert
- Handschrift mit Finger oder Pencil für Stichpunkte, Transkription durch die KI nach Freigabe
- automatische Sicherung: IndexedDB (48 h) und Server-Autosave mit monotonen Revisionen,
  Flush bei Tabwechsel und Schließen, JSON-Export/-Import mit Textfallback für das iPad
- KI-Tutor, KI-Textfeedback, KI-Zeichenbewertung – nur nach Freigabe der Lehrkraft
- Fokus-Reader für das Original-Arbeitsblatt (Rasterseiten, PDF-Ansicht, separater Link)

**Lehrkraft (`/lehrer`)**

- Live-Dashboard: Präsenz aus echten Sockets, Fortschritt, Antwortversuche, letzter Autosave,
  Zeichnungen, KI-Chats
- KI-Einzelfreigaben und zeitlich begrenzte Gruppenfreigaben mit Budgets, persistente Sperren
- Zwischenstände (unverschlüsselt, kurzfristig) speichern, laden, löschen
- IServ-Archiv über HTTPS-WebDAV: HKDF-SHA256 + AES-256-GCM, `.iabackup`, Verifizieren-vor-Löschen
- Wiederherstellung als „Ansicht“ (ohne Resume-Hashes) oder „Fortsetzungsstunde“ (mit Token-Rejoin
  und manueller bzw. automatischer Zuordnung)
- Ein Neustart, Redeploy oder späterer Lehrkraft-Login löscht keine laufende Sitzung.

## Projektstruktur

```text
app.py               Routen, Socket.IO-Handler, Wiring
config.py            Umgebungsvariablen, Konstanten, APP_ID, Stationen
db.py                SQLite, additive Migrationen, Snapshots, Bereinigung
presence.py          Online-Präsenz aus Socket-Mengen
ki.py                Gemini, Prompts, Freigabeprüfung, Budgets, Sperren
iserv_archiv.py      Konfiguration, Krypto, WebDAV, Abschluss-Transaktion
inhalte_server.py    Lesestrecken mit Lösungen (nur serverseitig)
static/js/inhalte.js Aufgaben, Karten, Blitzfragen, Domino, Zeichenaufträge
static/js/*.js       kern, autosave, aufgaben, karte, lesestrecke, zeichnen, spiele, ki, reader, app
templates/           login, index, warten, lehrer_login, dashboard, schueler_detail
tests/               pytest-Suite (Autosave, Identität, Präsenz, KI, Snapshots, IServ, Fortsetzung, …)
```

## Lokal starten

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1          # macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
Copy-Item .env.example .env           # macOS/Linux: cp .env.example .env
python app.py
```

Dann `http://127.0.0.1:5000` öffnen. In der `.env` müssen mindestens `SECRET_KEY` und
`LEHRER_PASSWORD` gesetzt sein; ohne Lehrerpasswort bleibt der Lehrerbereich gesperrt.
Ohne `GEMINI_API_KEY` bleiben alle Aufgaben nutzbar, die KI-Flächen zeigen einen Hinweis.

Tests:

```bash
pip install pytest
pytest tests
```

## Umgebungsvariablen

Siehe `.env.example`. Alle Secrets sind ausschließlich Runtime-Variablen.

| Variable | Bedeutung |
|---|---|
| `SECRET_KEY` | Flask-Session-Schlüssel (Pflicht im Betrieb) |
| `LEHRER_PASSWORD` | Passwort des Lehrerbereichs (Pflicht) |
| `SESSION_COOKIE_SECURE` | `1` hinter HTTPS |
| `GEMINI_API_KEY`, `GEMINI_MODEL`, `DAILY_TOKEN_LIMIT` | KI, optional |
| `ISERV_WEBDAV_URL`, `ISERV_WEBDAV_USERNAME`, `ISERV_WEBDAV_PASSWORD` | WebDAV-Zugang, nur HTTPS |
| `ISERV_BACKUP_PATH` | Zielordner (POSIX-Pfad, wird nicht angelegt) |
| `ISERV_BACKUP_ENCRYPTION_KEY` | 32 Byte URL-safe Base64 |
| `ISERV_TIMEOUT_SECONDS` | 2–60 |
| `ISERV_CA_BUNDLE` | optionale schulische CA (PEM) |

## Ablauf einer Stunde

1. Lernende melden sich mit Pseudonym und Klasse an; das Gerät merkt sich den Lernplatz.
2. Alles wird automatisch gesichert. „Antwort abgeben“, „Stichpunkte abgeben“ und
   „Zeichnung abgeben“ schreiben bewertbare Versuche ins Protokoll.
3. Am Stundenende: **Stunde abschließen & archivieren**. Die App fordert verbundene Geräte zum
   letzten Autosave auf, verschlüsselt den Snapshot, lädt ihn hoch, liest ihn zurück, entschlüsselt
   und vergleicht den Digest. Erst dann werden die Daten auf dem App-Server gelöscht.
4. Fortsetzung: Archiv im Modus „Fortsetzungsstunde“ laden. Geräte mit gespeichertem Lernplatz
   verbinden sich automatisch; andere melden sich an und werden im Dashboard zugeordnet.

## Deployment (Coolify)

- Build Pack **Dockerfile**, interner Port **5000**, Healthcheck `/health`
- persistentes Volume nach **`/app/data`** (SQLite mit WAL)
- Environment Variables aus `.env.example` setzen, `SESSION_COOKIE_SECURE=1`
- Secrets nur zur Runtime („Available at Buildtime“ aus)
- genau ein Gunicorn-Worker (`gunicorn.conf.py`, gthread + simple-websocket)

Vor dem ersten Push in ein öffentliches Repo:

```bash
git grep -I --cached -n "AIzaSy"
git check-ignore -v .env
```

## Datenschutz

- Nur Pseudonym und Klasse; Datenschutz- und KI-Hinweis vor dem Login, Pflichtcheckbox.
- Gespeichert: Fortschritt, Antwortversuche, Stichpunkte, Quellen, Zeichnungen (Objekt-JSON +
  Vorschau), automatischer Arbeitsstand, KI-Anfragen und KI-Chats der Sitzung.
- Nach erfolgreichem IServ-Archiv werden die Sitzungsdaten auf dem App-Server gelöscht
  (`secure_delete`, WAL-Truncate, VACUUM). Provider-Snapshots, Volume-Backups und Proxy-Logs
  sind davon nicht erfasst und müssen separat geregelt werden.

## Bewusste Abweichung vom Standard

MathJax ist nicht eingebunden – Geschichte braucht kein LaTeX. KI-Antworten werden escaped und
mit einfachem Markdown (fett, Zeilenumbrüche) dargestellt.
