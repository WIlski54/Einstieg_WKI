import app as appmodule
import db as dbmod
from config import APP_ID, STATE_SCHEMA_VERSION
from conftest import anmelden, session_werte


def _state(sid, tab):
    return {"schema_version": STATE_SCHEMA_VERSION, "app_id": APP_ID, "lernplatz": {"schueler_id": sid}, "active_tab": tab}


def _vorbereiten(teacher):
    """Zwei Lernplätze A und B mit Arbeitsständen, Snapshot, dann Sitzung geleert und im Fortsetzungsmodus geladen."""
    a = anmelden(appmodule.app.test_client(), "Anna", "9a")
    b = anmelden(appmodule.app.test_client(), "Ben", "9a")
    sa, sb = session_werte(a), session_werte(b)
    a.post("/api/autosave", json={"revision": 5, "state": _state(sa["schueler_id"], "verlauf")})
    b.post("/api/autosave", json={"revision": 2, "state": _state(sb["schueler_id"], "folgen")})
    snap = teacher.post("/api/lehrer/snapshots", json={"name": "Stunde 1"}).get_json()["snapshot"]
    teacher.post("/api/lehrer/sitzung-zuruecksetzen")
    assert teacher.post(f"/api/lehrer/snapshots/{snap['id']}/laden").get_json()["lernende"] == 2
    return sa, sb


def test_token_rejoin_und_tokenlose_sammelzuordnung(client, teacher):
    sa, sb = _vorbereiten(teacher)
    assert appmodule.fortsetzung_status()["active"] is True
    # Anna hat ihr Token noch im Browser
    anna = appmodule.app.test_client()
    r = anna.post("/api/resume", json={"schueler_id": sa["schueler_id"], "token": sa["resume_token"]}).get_json()
    assert r["ok"] and r["wartend"] is False
    assert anna.get("/api/autosave").get_json()["state"]["active_tab"] == "verlauf"
    ziel = dbmod.get_db().execute("SELECT status FROM fortsetzungsziele WHERE student_id=?", (sa["schueler_id"],)).fetchone()
    assert ziel["status"] == "vergeben"
    # Ben meldet sich ohne Token neu an → Warteseite
    ben = appmodule.app.test_client()
    resp = ben.post("/login", data={"pseudonym": "ben", "klasse": "9A", "privacy_ok": "on"})
    assert resp.status_code == 302 and resp.headers["Location"].endswith("/warten")
    assert ben.get("/arbeitsblatt").status_code == 302
    assert ben.get("/warten").status_code == 200
    assert ben.get("/api/fortsetzung/status").get_json()["status"] == "wartend"
    payload = appmodule.fortsetzung_payload()
    assert len(payload["anfragen"]) == 1 and payload["anfragen"][0]["kandidaten"] == [sb["schueler_id"]]
    assert "resume_token_hash" not in payload["anfragen"][0]
    # Sammelzuordnung
    r = teacher.post("/api/lehrer/fortsetzung/auto").get_json()
    assert r == {"ok": True, "zugeordnet": 1, "mehrdeutig": 0, "ohne_treffer": 0}
    st = ben.get("/api/fortsetzung/status").get_json()
    assert st["status"] == "zugeordnet" and st["schueler_id"] == sb["schueler_id"] and st["redirect"].endswith("/arbeitsblatt")
    assert session_werte(ben)["schueler_id"] == sb["schueler_id"]
    assert ben.get("/arbeitsblatt").status_code == 200
    assert ben.get("/api/autosave").get_json()["state"]["active_tab"] == "folgen"
    assert dbmod.get_db().execute("SELECT COUNT(*) AS n FROM schueler").fetchone()["n"] == 2  # Platzhalter entfernt


def test_mehrdeutigkeit_manuell_und_nur_einmal_vergeben(client, teacher):
    # Zwei alte Lernplätze mit gleichem Pseudonym und gleicher Klasse
    c1 = anmelden(appmodule.app.test_client(), "Chris", "9a")
    c2 = anmelden(appmodule.app.test_client(), "Chris", "9a")
    id1, id2 = session_werte(c1)["schueler_id"], session_werte(c2)["schueler_id"]
    snap = teacher.post("/api/lehrer/snapshots", json={"name": "S"}).get_json()["snapshot"]
    teacher.post("/api/lehrer/sitzung-zuruecksetzen")
    teacher.post(f"/api/lehrer/snapshots/{snap['id']}/laden")
    neu = anmelden(appmodule.app.test_client(), "Chris", "9a")
    neu2 = anmelden(appmodule.app.test_client(), "Chris", "9a")
    assert teacher.post("/api/lehrer/fortsetzung/auto").get_json()["mehrdeutig"] == 2
    anfragen = appmodule.fortsetzung_payload()["anfragen"]
    assert all(set(a["kandidaten"]) == {id1, id2} for a in anfragen)
    a1, a2 = anfragen[0]["id"], anfragen[1]["id"]
    assert teacher.post("/api/lehrer/fortsetzung/zuordnen", json={"anfrage_id": a1, "aktion": "zuordnen", "target_student_id": id1}).get_json()["status"] == "zugeordnet"
    # derselbe Lernplatz darf nicht zweimal vergeben werden
    assert teacher.post("/api/lehrer/fortsetzung/zuordnen", json={"anfrage_id": a2, "aktion": "zuordnen", "target_student_id": id1}).status_code == 409
    assert teacher.post("/api/lehrer/fortsetzung/zuordnen", json={"anfrage_id": a2, "aktion": "ablehnen"}).get_json()["status"] == "abgelehnt"
    assert neu2.get("/api/fortsetzung/status").get_json()["status"] == "abgelehnt"
    assert teacher.post("/api/lehrer/fortsetzung/zuordnen", json={"anfrage_id": a2, "aktion": "zuordnen", "target_student_id": id2}).status_code == 404
    assert neu.get("/api/fortsetzung/status").get_json()["status"] == "zugeordnet"


def test_neustart_und_beenden(client, teacher):
    _vorbereiten(teacher)
    neu = anmelden(appmodule.app.test_client(), "Dana", "9a")
    anfrage = appmodule.fortsetzung_payload()["anfragen"][0]
    assert anfrage["kandidaten"] == []
    assert teacher.post("/api/lehrer/fortsetzung/zuordnen", json={"anfrage_id": anfrage["id"], "aktion": "neustart"}).get_json()["status"] == "neustart"
    st = neu.get("/api/fortsetzung/status").get_json()
    assert st["status"] == "neustart" and neu.get("/arbeitsblatt").status_code == 200
    wartend = anmelden(appmodule.app.test_client(), "Emil", "9a")
    r = teacher.post("/api/lehrer/fortsetzung/beenden").get_json()
    assert r["ok"] and r["neustarts"] == 1
    assert appmodule.fortsetzung_status()["active"] is False
    assert wartend.get("/api/fortsetzung/status").get_json()["status"] == "neustart"
    assert wartend.get("/arbeitsblatt").status_code == 200
    # Beenden löscht keine Lernplätze
    assert dbmod.get_db().execute("SELECT COUNT(*) AS n FROM schueler").fetchone()["n"] == 4


def test_warten_vor_der_lehrkraft(client, teacher):
    a = anmelden(appmodule.app.test_client(), "Anna", "9a")
    sa = session_werte(a)
    snap = teacher.post("/api/lehrer/snapshots", json={"name": "S"}).get_json()["snapshot"]
    dbmod.clear_live_data()  # wie nach einem IServ-Abschluss
    browser = appmodule.app.test_client()
    r = browser.post("/api/resume", json={"schueler_id": sa["schueler_id"], "token": sa["resume_token"]})
    assert r.status_code == 404 and r.get_json()["fortsetzung_aktiv"] is False
    st = browser.get(f"/api/fortsetzung/status?schueler_id={sa['schueler_id']}&token={sa['resume_token']}").get_json()
    assert st["status"] == "inaktiv"
    teacher.post(f"/api/lehrer/snapshots/{snap['id']}/laden")
    st = browser.get(f"/api/fortsetzung/status?schueler_id={sa['schueler_id']}&token={sa['resume_token']}").get_json()
    assert st["status"] == "verbunden" and st["redirect"].endswith("/arbeitsblatt")
    assert browser.get("/api/status").status_code == 200
