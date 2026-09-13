import time

import db as dbmod
import inhalte_server as inh
from conftest import session_werte


def test_inhalte_vollstaendig_und_eindeutig():
    assert set(inh.LESESTRECKEN) == {"ursachen", "ausloeser", "verlauf", "kriegsende", "folgen"}
    for key, strecke in inh.LESESTRECKEN.items():
        assert 4 <= len(strecke["abschnitte"]) <= 7, key
        for a in strecke["abschnitte"]:
            assert len(a["optionen"]) == 3 and 0 <= a["loesung"] < 3
            assert len(set(a["optionen"])) == 3
            assert a["erklaerung"] and a["text"] and a["frage"]


def test_client_daten_enthalten_keine_loesung(student):
    r = student.get("/api/lesestrecke/ursachen").get_json()
    assert r["ok"] and r["anzahl"] == 4 and r["status"]["phase"] == 0
    for a in r["abschnitte"]:
        assert "loesung" not in a and "erklaerung" not in a
        assert len(a["optionen"]) == 3
    assert student.get("/api/lesestrecke/unbekannt").status_code == 404


def test_richtig_falsch_sperre_und_abschluss(student, monkeypatch):
    sid = session_werte(student)["schueler_id"]
    loesung = inh.LESESTRECKEN["ursachen"]["abschnitte"][0]["loesung"]
    falsch = (loesung + 1) % 3
    # falsche Antwort → protokolliert, Sperre 60 s, Phase bleibt 0
    r = student.post("/api/lesestrecke/ursachen/antwort", json={"phase": 0, "wahl": falsch}).get_json()
    assert r["korrekt"] is False and r["status"]["phase"] == 0 and r["status"]["versuche"] == 1
    assert 55 <= r["status"]["retry_until"] - time.time() <= 61
    # Antwort während der Sperre → 429 mit retry_until (Reload umgeht die Sperre nicht)
    r2 = student.post("/api/lesestrecke/ursachen/antwort", json={"phase": 0, "wahl": loesung})
    assert r2.status_code == 429 and r2.get_json()["status"]["retry_until"] == r["status"]["retry_until"]
    st = student.get("/api/lesestrecke/ursachen").get_json()["status"]
    assert st["retry_until"] == r["status"]["retry_until"]
    # Sperre abgelaufen (simuliert): zweiter Fehlversuch → 75 s, dritter → 90 s
    with dbmod.get_db() as db:
        db.execute("UPDATE lesestrecke_status SET retry_until=0 WHERE schueler_id=?", (sid,))
        db.commit()
    r = student.post("/api/lesestrecke/ursachen/antwort", json={"phase": 0, "wahl": falsch}).get_json()
    assert 70 <= r["status"]["retry_until"] - time.time() <= 76
    with dbmod.get_db() as db:
        db.execute("UPDATE lesestrecke_status SET retry_until=0 WHERE schueler_id=?", (sid,))
        db.commit()
    r = student.post("/api/lesestrecke/ursachen/antwort", json={"phase": 0, "wahl": falsch}).get_json()
    assert 85 <= r["status"]["retry_until"] - time.time() <= 91
    with dbmod.get_db() as db:
        db.execute("UPDATE lesestrecke_status SET retry_until=0 WHERE schueler_id=?", (sid,))
        db.commit()
    # falsche Phase → 409
    assert student.post("/api/lesestrecke/ursachen/antwort", json={"phase": 2, "wahl": 0}).status_code == 409
    # richtig → nächste Phase mit Erklärung
    r = student.post("/api/lesestrecke/ursachen/antwort", json={"phase": 0, "wahl": loesung}).get_json()
    assert r["korrekt"] is True and r["status"]["phase"] == 1 and r["erklaerung"]
    for phase in (1, 2, 3):
        l = inh.LESESTRECKEN["ursachen"]["abschnitte"][phase]["loesung"]
        r = student.post("/api/lesestrecke/ursachen/antwort", json={"phase": phase, "wahl": l}).get_json()
    assert r["status"]["fertig"] is True and r["station"] == "L1"
    status = student.get("/api/status").get_json()
    assert {e["nr"] for e in status["erledigt"]} == {"L1"}
    antworten = dbmod.get_db().execute("SELECT korrekt FROM antworten WHERE schueler_id=? AND antwort_typ='lesestrecke'", (sid,)).fetchall()
    assert [a["korrekt"] for a in antworten] == [0, 0, 0, 1, 1, 1, 1]
    # nach Abschluss keine weiteren Antworten
    assert student.post("/api/lesestrecke/ursachen/antwort", json={"phase": 3, "wahl": 0}).status_code == 409
    daten = student.get("/api/lesestrecke/ursachen").get_json()
    assert all("erklaerung" in a for a in daten["abschnitte"])
