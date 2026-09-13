# Umbau auf den GSM-Produktionsstandard (Autosave + IServ) – Implementierungsplan

> **For agentic workers:** Dieser Plan wird in dieser Sitzung inline ausgeführt (superpowers:executing-plans). Schritte nutzen Checkboxen (`- [ ]`). Jeder Task endet mit grünen Tests und einem Commit.

**Goal:** Das bestehende interaktive Arbeitsblatt „Der Erste Weltkrieg (1914–1918)“ (Geschichte, Klasse 9, Klassenunterricht) erfüllt vollständig die Spezifikation `INTERAKTIVES_ARBEITSBLATT_MIT_AUTOSAVE_UND_ISERV.md` (Stand Sept. 2026) und schöpft iPad-Interaktivität aus (Pencil-Handschrift, objektbasiertes Zeichnen, Lesestrecke, Blitzfragen, Domino).

**Architecture:** Flask + Flask-SocketIO (threading, gthread-Worker) + SQLite-WAL. Backend wird in fokussierte Module zerlegt (`db.py`, `presence.py`, `ki.py`, `iserv_archiv.py`, `inhalte_server.py`, `app.py`). Frontend: ein JS-Modul je Verantwortung unter gemeinsamem Namensraum `window.WK`; ein einziger Zustandsvertrag (`collectBackup`/`applyBackupData`) speist IndexedDB-Autosave, Server-Autosave, JSON-Export, Snapshots und IServ-Archiv.

**Tech Stack:** Flask 3, Flask-SocketIO 5 (async_mode threading, simple-websocket), SQLite WAL, google-genai, cryptography (HKDF-SHA256 + AES-256-GCM), requests (WebDAV), Chart.js 4.4.1 (lokal), Fabric.js 5.3.0 (lokal), gunicorn gthread, Docker/Coolify.

---

## Verbindliche Verträge

### App-Kennung und Versionen

```python
APP_ID = "gsm-geschichte-erster-weltkrieg"   # stabil, nie mehr ändern
STATE_SCHEMA_VERSION = 2                       # Zustandsvertrag collectBackup()
DB_SCHEMA_VERSION = 2                          # Migrationen additiv
ARCHIV_FORMAT = "gsm-iabackup"
STATE_MAX_BYTES = 2 * 1024 * 1024
```

### Stationen (Aufgabennummern, pro Reiter)

| Reiter | Stationen |
|---|---|
| ursachen | `L1`, 1 MC, 2 Lücke, 3 Zuordnung, 4 Sortierung, 5 Diagramm, 6 Karte, 7 Freitext, 8 Notizen, **9 Zeichnen (Bündnissystem)** |
| ausloeser | `L2`, 10 Sortierung, 11 MC, 12 Lücke, 13 Zuordnung, 14 Diagramm, 15 Karte, 16 Freitext, 17 Notizen |
| verlauf | `L3`, 18 MC, 19 Lücke, 20 Zuordnung, 21 Sortierung, 22 Diagramm, 23 Karte, 24 Freitext, 25 Notizen, **26 Zeichnen (Schützengraben)** |
| kriegsende | `L4`, 27 MC, 28 Lücke, 29 Sortierung, 30 Zuordnung, 31 Diagramm, 32 Karte, 33 Freitext, 34 Notizen |
| folgen | `L5`, 35 MC, 36 Lücke, 37 Zuordnung, 38 Diagramm, 39 Sortierung, 40 Karte, 41 Freitext, 42 Notizen, **43 Zeichnen (Plakat/Karikatur Versailles)** |
| abschluss | 44 Zeitstrahl, 45 Quellenkritik-MC, **46 Blitzfragen**, **47 Domino**, 48 Quellenverzeichnis, `T` Transfer |

Gesamt: 5 Lesestrecken + 48 + T = **54 Stationen**. `L*`-Lösungen liegen nur auf dem Server.

### Zustandsvertrag (collectBackup)

```json
{
  "schema_version": 2,
  "app_id": "gsm-geschichte-erster-weltkrieg",
  "exported_at": "2026-09-13T12:00:00",
  "lernplatz": {"schueler_id": "…", "pseudonym": "…", "klasse": "…"},
  "active_tab": "ursachen",
  "completed": ["1", "L1", "T"],
  "niveaus": {"1": "B"},
  "texte": {"ft-7": "…", "nt-ursachen": "…", "nq-ursachen": "…", "ft-T": "…"},
  "quellen": [{"titel": "…", "ort": "…", "art": "…", "wert": "…", "grund": "…"}],
  "aufgaben": {"1": {"typ": "mc", "gewaehlt": [2], "fertig": true, "ok": true},
               "2": {"typ": "luecke", "werte": ["Imperialismus", ""]},
               "3": {"typ": "zuordnung", "paare": [0, 2]},
               "4": {"typ": "sortierung", "reihenfolge": [2, 0, 1], "geprueft": false},
               "6": {"typ": "karte", "besucht": ["berlin"], "gewaehlt": [], "fertig": false}},
  "lesestrecke": {"ursachen": {"phase": 2, "fertig": false, "retry_until": 1789000000000, "versuche": 1}},
  "blitz": {"aktuelle_id": "b07", "gesehen": ["b01", "b07"], "richtig": 1, "beantwortet": 1},
  "domino": {"kette": ["d01", "d05"], "fehler": 0, "fertig": false},
  "zeichnungen": {"buendnis": {"json": {"version": "5.1.0", "objects": []}, "objekte": 3}}
}
```

Kompakt (`{compact:true}`): ohne `preview` in `zeichnungen`. Vorschauen liegen separat in `zeichnungen`-Tabelle. Import/Restore prüft `schema_version`, `app_id`, Typen, Größe.

### Datenbank (additiv migriert, `schema_migrations(version)`)

```sql
CREATE TABLE IF NOT EXISTS schueler (id TEXT PRIMARY KEY, pseudonym TEXT NOT NULL, klasse TEXT NOT NULL,
  joined_at TEXT NOT NULL, last_active TEXT, socket_id TEXT, resume_token_hash TEXT);
CREATE TABLE IF NOT EXISTS fortschritt (id INTEGER PRIMARY KEY AUTOINCREMENT, schueler_id TEXT NOT NULL,
  aufgabe_nr TEXT NOT NULL, niveau TEXT NOT NULL DEFAULT 'A', erledigt_at TEXT NOT NULL, UNIQUE(schueler_id, aufgabe_nr, niveau));
CREATE TABLE IF NOT EXISTS antworten (id INTEGER PRIMARY KEY AUTOINCREMENT, schueler_id TEXT NOT NULL, aufgabe_nr TEXT NOT NULL,
  niveau TEXT NOT NULL, antwort_typ TEXT NOT NULL, frage TEXT, antwort_text TEXT, korrekt INTEGER, versuch_nr INTEGER NOT NULL DEFAULT 1, erstellt_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS notizen (id INTEGER PRIMARY KEY AUTOINCREMENT, schueler_id TEXT NOT NULL, abschnitt TEXT NOT NULL,
  stichpunkte TEXT NOT NULL DEFAULT '', quellen TEXT NOT NULL DEFAULT '', updated_at TEXT NOT NULL, UNIQUE(schueler_id, abschnitt));
CREATE TABLE IF NOT EXISTS ki_anfragen (id INTEGER PRIMARY KEY AUTOINCREMENT, schueler_id TEXT NOT NULL, typ TEXT NOT NULL, kontext TEXT,
  status TEXT NOT NULL DEFAULT 'wartend', token_count INTEGER NOT NULL DEFAULT 0, erstellt_at TEXT NOT NULL, bearbeitet_at TEXT);
CREATE TABLE IF NOT EXISTS chat_messages (id INTEGER PRIMARY KEY AUTOINCREMENT, schueler_id TEXT NOT NULL, typ TEXT NOT NULL,
  frage TEXT NOT NULL, antwort TEXT NOT NULL, tokens INTEGER NOT NULL DEFAULT 0, erstellt_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS token_budget (datum TEXT PRIMARY KEY, tokens_used INTEGER NOT NULL DEFAULT 0);
CREATE TABLE IF NOT EXISTS ki_sperren (schueler_id TEXT PRIMARY KEY, gesperrt_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS zeichnungen (id INTEGER PRIMARY KEY AUTOINCREMENT, schueler_id TEXT NOT NULL, geraet TEXT NOT NULL,
  canvas_json TEXT NOT NULL, preview_data TEXT NOT NULL, updated_at TEXT NOT NULL, UNIQUE(schueler_id, geraet));
CREATE TABLE IF NOT EXISTS arbeitsstaende (schueler_id TEXT PRIMARY KEY, state_json TEXT NOT NULL, revision INTEGER NOT NULL DEFAULT 0, updated_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS gespeicherte_sitzungen (id TEXT PRIMARY KEY, name TEXT NOT NULL, snapshot_json TEXT NOT NULL, created_at TEXT NOT NULL, updated_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS fortsetzungsstatus (id INTEGER PRIMARY KEY CHECK (id = 1), active INTEGER NOT NULL DEFAULT 0, source_name TEXT, started_at TEXT);
CREATE TABLE IF NOT EXISTS fortsetzungsziele (student_id TEXT PRIMARY KEY, status TEXT NOT NULL DEFAULT 'verfuegbar');
CREATE TABLE IF NOT EXISTS fortsetzungsanfragen (id TEXT PRIMARY KEY, new_student_id TEXT NOT NULL, pseudonym TEXT NOT NULL, klasse TEXT NOT NULL,
  resume_token_hash TEXT NOT NULL, target_student_id TEXT, status TEXT NOT NULL DEFAULT 'wartend', created_at TEXT NOT NULL, decided_at TEXT);
CREATE TABLE IF NOT EXISTS ki_gruppenfreigabe (id INTEGER PRIMARY KEY CHECK (id = 1), active INTEGER NOT NULL DEFAULT 0, locked INTEGER NOT NULL DEFAULT 0,
  klasse TEXT NOT NULL DEFAULT '', allowed_types TEXT NOT NULL DEFAULT '[]', starts_at TEXT, expires_at TEXT,
  token_limit INTEGER NOT NULL DEFAULT 0, tokens_used INTEGER NOT NULL DEFAULT 0, per_student_limit INTEGER NOT NULL DEFAULT 0);
CREATE TABLE IF NOT EXISTS ki_gruppen_nutzung (schueler_id TEXT PRIMARY KEY, tokens INTEGER NOT NULL DEFAULT 0);
CREATE TABLE IF NOT EXISTS lehrer_tokens (token_hash TEXT PRIMARY KEY, created_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS lesestrecke_status (schueler_id TEXT NOT NULL, abschnitt TEXT NOT NULL, phase INTEGER NOT NULL DEFAULT 0,
  fertig INTEGER NOT NULL DEFAULT 0, retry_until REAL NOT NULL DEFAULT 0, versuche INTEGER NOT NULL DEFAULT 0, UNIQUE(schueler_id, abschnitt));
```

Pragmas: `journal_mode=WAL`, `foreign_keys=ON`, `secure_delete=ON`. Kein Löschen beim Start; beim Prozessstart nur `UPDATE schueler SET socket_id=NULL`.

Snapshot (`db.build_snapshot()`): `schueler`, `fortschritt`, `antworten`, `notizen`, `ki_anfragen`, `chat_messages`, `token_budget`, `ki_sperren`, `zeichnungen`, `arbeitsstaende`, `ki_gruppenfreigabe`, `ki_gruppen_nutzung`, `lesestrecke_status`. Nicht: `gespeicherte_sitzungen`, `lehrer_tokens`, Fortsetzungstabellen.

### HTTP-API (Lernende)

| Route | Zweck |
|---|---|
| `POST /login` | Pseudonym+Klasse+Häkchen → neuer Lernplatz + Resume-Token; bei aktivem Fortsetzungsmodus → Anfrage + `/warten` |
| `POST /logout` | Browser-Token und Server-Hash löschen |
| `POST /api/resume` `{schueler_id, token}` | Session wiederherstellen (compare_digest) |
| `GET /api/status` | Fortschritt, Notizen, KI-Status, Gruppenfreigabe, letzter Autosave |
| `GET/POST /api/autosave` | Arbeitsstand lesen/UPSERT mit monotoner Revision |
| `POST /api/fortschritt`, `POST /api/antwort` | Stationen/Versuche (Antwort mit `frage`) |
| `GET /api/lesestrecke/<abschnitt>` · `POST …/antwort` | Abschnitte ohne Lösung; Prüfung + `retry_until` serverseitig |
| `POST /api/zeichnung` · `GET /api/zeichnungen` | Objekt-JSON + Vorschau je Gerät |
| `POST /api/ki-anfrage`, `/api/chat`, `/api/check-answer`, `/api/zeichnung-analyse`, `/api/handschrift` | KI-Wege, alle mit `ki_pruefen()` |
| `GET /warten` · `GET /api/fortsetzung/status` | Warteseite mit Polling |

### HTTP-API (Lehrkraft, `X-Lehrer-Token`-Header oder Session)

`/api/lehrer/state`, `/api/ki-entscheidung`, `/api/lehrer/ki-sperren`, `/api/lehrer/daten-loeschen`, `/api/lehrer/sitzung-zuruecksetzen`, `/api/lehrer/gruppenfreigabe`, `/api/lehrer/snapshots` (GET/POST) + `/<id>/laden` + `DELETE /<id>`, `/api/lehrer/iserv/status|test|abschluss|archive|vorschau|wiederherstellen|loeschen`, `/api/lehrer/fortsetzung/auto|zuordnen|beenden`.

### Socket.IO-Räume (genau ein Raum je Ereignis)

- `lehrer_room`: `neuer_schueler`, `schueler_online`, `schueler_offline`, `fortschritt_update`, `antwort_zaehler`, `neue_anfrage`, `anfrage_erledigt`, `ki_sperr_status`, `token_update`, `autosave_update`, `schueler_geloescht`, `sitzung_zurueckgesetzt`, `gruppenfreigabe_update`, `fortsetzung_update`
- `schueler_{sid}`: `ki_entscheidung`, `ki_gesperrt`, `gruppenfreigabe`, `sitzung_beendet`, `autosave_flush`, `fortsetzung_zugeordnet`
- `watch_{sid}`: `antwort_live`, `chat_live`, `notizen_live`, `zeichnung_live`
- Client → Server: `schueler_join`, `lehrer_join {token}`, `watch_schueler {schueler_id}`, `autosave_ack {revision}`

### IServ-Archiv

- Datei: `MAGIC(8)=b"GSMIAB01" | salt(16) | nonce(12) | AES-256-GCM(ciphertext+tag)`, AAD = MAGIC+salt, Dateischlüssel = HKDF-SHA256(master, salt, info=b"gsm-iabackup-v1").
- Umschlag: `{"format":"gsm-iabackup","schema_version":2,"app_id":APP_ID,"name":…,"created_at_utc":…,"snapshot":{…}}`, kanonisch: `json.dumps(sort_keys=True, separators=(",",":"), ensure_ascii=False)`.
- Dateiname: `^[0-9a-f]{12}_\d{8}-\d{6}_[A-Za-z0-9_-]{1,40}\.iabackup$`, Marker = `sha256(APP_ID)[:12]`.
- WebDAV über `requests` mit austauschbarem Transport (Tests injizieren Fake).
- Abschluss = 11-Schritt-Transaktion (Flush → Snapshot → Validieren → Digest → Verschlüsseln → PUT `If-None-Match: *` → GET → Entschlüsseln → Prüfen → Digest vergleichen → erst dann bereinigen).

---

## Dateistruktur

```
app.py               Routen, Socket-Handler, Wiring (schlank)
config.py            Umgebungsvariablen, Konstanten, APP_ID
db.py                Verbindung, Migrationen, Snapshot bauen/wiederherstellen/bereinigen, Notizen-Sync
presence.py          Socket-Präsenz (Mengen + Eigentümer), threadsicher
ki.py                Gemini-Client, Prompts, ki_pruefen(), Token-Buchung, Gruppenfreigabe
iserv_archiv.py      Konfiguration, Krypto, Dateiname, WebDAV-Client, Abschluss-Transaktion
inhalte_server.py    Lesestrecken (Text + Fragen + Lösungen), Abschnittsstruktur
gunicorn.conf.py     gthread, 1 Worker
static/js/inhalte.js     Aufgaben, Karten, Blitzfragen-Pool, Domino, Zeichenaufträge
static/js/kern.js        WK-Namensraum: Zustand, Helfer, Fortschritt, Tabs, Socket, Toast
static/js/autosave.js    IndexedDB + Server-Autosave, Revisionen, Flush/Ack, JSON-Export/-Import
static/js/aufgaben.js    Renderer + Serialisierung je Aufgabentyp
static/js/karte.js       SVG-Karte mit Küsten-Pfaden und Hotspots
static/js/lesestrecke.js Gegatete Lesestrecke (serverseitig geprüft)
static/js/zeichnen.js    Fabric.js-Zeichenaufträge + Handschrift-Pad
static/js/spiele.js      Blitzfragen (nicht wiederholend), Domino
static/js/ki.js          Freigabe-Modal, Tutor, Korrektur, Zeichenanalyse, Handschrift, Markdown-lite
static/js/reader.js      Fokus-Reader
static/js/app.js         Init: Aufbau, Restore (lokal ∥ Server), dann Socket + Autosave
static/js/dashboard.js, detail.js, warten.js
templates/…, tests/…
```

---

## Tasks

### Task 1: Backend-Zerlegung, Konfiguration, Migrationen ohne Startlöschung
Files: Create `config.py`, `db.py`, `presence.py`; Modify `app.py`; Test `tests/test_db.py`
- [ ] Test: Tabellen existieren nach `init_db()`; zweiter Aufruf auf alter DB (nur `schueler` ohne `resume_token_hash`) ergänzt Spalte, verwirft keine Zeilen; `socket_id` wird beim Start geleert; Daten überleben Import.
- [ ] Implementieren, Tests grün, Commit `refactor: Backend in Module zerlegen, additive Migrationen`.

### Task 2: Resume-Token, Lehrkraft-Aktionstoken, Präsenz
Files: Modify `app.py`, `presence.py`, `templates/*.html`; Test `tests/test_identity.py`, `tests/test_presence.py`
- [ ] Tests: Login liefert Token; `/api/resume` mit gültigem Token verbindet, mit falschem 403; Logout löscht Hash; Lehrer-Header ohne Session autorisiert; Schüler-Login löscht Lehrer-Flag nicht; zwei Sockets → online bis letzter Disconnect; Lehrer-Socket im selben Profil ändert nichts.
- [ ] Implementieren, Commit `feat: Resume-Token, Lehrer-Aktionstoken, exakte Präsenz`.

### Task 3: Server-Autosave mit Revisionen, Notizen-Sync, Flush-Protokoll
Files: Modify `app.py`, `db.py`; Test `tests/test_autosave.py`
- [ ] Tests: höhere Revision gewinnt, niedrigere abgelehnt (`accepted:false`); falsche `app_id`/Schema/Typ/Größe → 400; Notizen-Tabelle spiegelt `texte.nt-*`/`nq-*`; `request_flush()` protokolliert `online/confirmed/missing`.
- [ ] Implementieren, Commit `feat: Server-Autosave mit monotonen Revisionen`.

### Task 4: KI-Modul mit Gruppenfreigabe, persistenter Sperre, Chat-Speicherung
Files: Create `ki.py`; Modify `app.py`; Test `tests/test_ki.py`
- [ ] Tests: Prüfreihenfolge (Sperre → Tagesbudget → Gruppe → Einzel), Gruppe Zeit/Typ/Klasse/Budget, Sperre überlebt Neuimport, Einzelanfrage ohne Freigabe blockiert ohne Protokoll-Duplikat, Chat wird in `chat_messages` gespeichert, Zeichnung/Handschrift-Routen ohne Key liefern Hinweis.
- [ ] Implementieren, Commit `feat: KI-Freigaben (Einzel + Gruppe), persistente Sperre, Chatverlauf`.

### Task 5: Lesestrecke serverseitig
Files: Create `inhalte_server.py`; Modify `app.py`; Test `tests/test_lesestrecke.py`
- [ ] Tests: GET liefert keine Lösungen; richtige Antwort → nächste Phase; falsche → `retry_until` 60/75/90 s eskalierend; Antwort vor Ablauf → 429; letzte Phase → Station `L1` erledigt.
- [ ] Implementieren (5 Abschnitte × 4 Absätze mit je einer eindeutigen Frage), Commit `feat: gegatete Lesestrecke`.

### Task 6: Snapshots (temporär) und Zeichnungen-API
Files: Modify `db.py`, `app.py`; Test `tests/test_snapshots.py`
- [ ] Tests: Snapshot speichern/laden/löschen; Zeichnungen überleben; Laden ersetzt Live-Tabellen und invalidiert Sockets; Reset räumt Präsenz.
- [ ] Commit `feat: temporäre Lehrkraft-Snapshots, Zeichnungen`.

### Task 7: IServ-Archiv (Krypto, WebDAV, Abschluss, Wiederherstellung)
Files: Create `iserv_archiv.py`; Modify `app.py`; Test `tests/test_iserv.py`
- [ ] Tests: Konfig-Validierung (https, Zugangsdaten in URL, Pfad `..`, Timeout-Bereich, 32-Byte-Key); Roundtrip; Manipulation/falscher Key → Fehler; Dateiname; Fake-WebDAV: Listing filtert Marker + App-ID, PUT mit `If-None-Match`, Abschluss löscht nur bei Digest-Gleichheit, fehlgeschlagener Download/Digest lässt alles stehen; Ansicht entfernt Hashes, Fortsetzung behält sie; Remote-Löschen validiert Eigentum.
- [ ] Commit `feat: verschlüsseltes IServ-WebDAV-Archiv mit Verifizieren-vor-Löschen`.

### Task 8: Fortsetzungsmodus
Files: Modify `app.py`, `db.py`; Create `templates/warten.html`, `static/js/warten.js`; Test `tests/test_fortsetzung.py`
- [ ] Tests: Token-Rejoin; Login ohne Token → Anfrage + Warteseite; eindeutige Sammelzuordnung; Mehrdeutigkeit bleibt manuell; ein Ziel nur einmal; Ablehnen/Neustart; Beenden löscht keine Lernplätze.
- [ ] Commit `feat: Fortsetzungsstunde`.

### Task 9: Inhalte (Neunummerierung, Zeichenaufträge, Blitzfragen, Domino), Strukturtests
Files: Modify `static/js/inhalte.js`, `config.py`; Test `tests/test_inhalte.py`
- [ ] Commit `feat: neue Stationen und Nummerierung`.

### Task 10: Frontend-Kern, Autosave-Client, Aufgaben-Renderer mit Serialisierung
Files: Create `kern.js`, `autosave.js`, `aufgaben.js`, `ki.js`, `reader.js`, `app.js`; Modify `index.html`, `app.css`
- [ ] Browserprobe: Reload stellt alles wieder her; Interaktion während Laden bleibt; JSON-Export/-Import; Textfallback.
- [ ] Commit `feat: Zustandsvertrag, IndexedDB- und Server-Autosave im Browser`.

### Task 11: Karte, Lesestrecke, Zeichnen, Handschrift, Spiele
Files: Create `karte.js`, `lesestrecke.js`, `zeichnen.js`, `spiele.js`
- [ ] Browserprobe je Modul, Touch-Ziele ≥ 44 px, kein Overflow bei 375/768/1024.
- [ ] Commit je Modul.

### Task 12: Dashboard und Detail (Snapshots, IServ, Fortsetzung, Gruppenfreigabe, Autosave-Zeit, Zeichnungen, Chatverlauf)
- [ ] Commit `feat: Dashboard-Verwaltung`.

### Task 13: Deployment, README, .env.example, Push
Files: `Dockerfile`, `gunicorn.conf.py`, `requirements.txt`, `.dockerignore`, `.env.example`, `.gitattributes`, `README.md`
- [ ] Secret-Check, Push auf `https://github.com/WIlski54/Einstieg_WKI.git`.
