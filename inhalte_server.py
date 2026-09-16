"""Serverseitige Inhalte: gegatete Lesestrecken mit Verständnisfragen.

Die Lösungen liegen ausschließlich hier. Der Client erhält Text, Frage und Optionen,
aber nie die richtige Position. Jede Frage lässt sich aus ihrem Abschnitt allein beantworten.
Sprache: Sek I, kurze Sätze, Fakten unverändert.
"""

from config import ASSET_VERSION
import random

LESESTRECKEN = {
    "ursachen": {
        "station": "L1", "eyebrow": "Lesestrecke M1",
        "titel": "Warum war Europa 1914 ein „Pulverfass“?",
        "abschnitte": [
            {
                "ueberschrift": "Imperialismus",
                "bild": "ursachen-1", "bild_alt": "Schaubild: Imperialismus",
                "text": "Die Großmächte Europas wollten Kolonien. Dort gab es Rohstoffe und neue Märkte. Deutschland gab es erst seit 1871 und kam zu spät. Es forderte einen „Platz an der Sonne“. In den <strong>Marokkokrisen 1905 und 1911</strong> standen Deutschland und Frankreich kurz vor einem Krieg.",
                "frage": "Worum stritten die Großmächte im Imperialismus?",
                "optionen": ["Um die meisten Eisenbahnen", "Um Kolonien, Rohstoffe und Märkte", "Um den Sitz des Völkerbunds"],
                "loesung": 1,
                "erklaerung": "Genau: Kolonien brachten Rohstoffe, Märkte und Ansehen. Darum ging der Wettlauf.",
            },
            {
                "ueberschrift": "Nationalismus",
                "bild": "ursachen-2", "bild_alt": "Schaubild: Nationalismus",
                "text": "Viele Menschen hielten ihr eigenes Volk für besser als andere. Frankreich wollte <strong>Elsass-Lothringen</strong> zurück. Das Gebiet hatte es 1871 an Deutschland verloren. Serbische Nationalisten wollten alle Südslawen in einem Staat vereinen. Das bedrohte Österreich-Ungarn, in dem viele Völker lebten.",
                "frage": "Welches Gebiet wollte Frankreich zurück?",
                "optionen": ["Elsass-Lothringen", "Bosnien", "Belgien"],
                "loesung": 0,
                "erklaerung": "Richtig: Elsass-Lothringen hatte Frankreich 1871 verloren.",
            },
            {
                "ueberschrift": "Militarismus und Wettrüsten",
                "bild": "ursachen-3", "bild_alt": "Schaubild: Militarismus und Wettrüsten",
                "text": "Das Militär hatte hohes Ansehen. Krieg galt als normales Mittel der Politik. Deutschland und Großbritannien bauten um die Wette Kriegsschiffe: das <strong>Flottenwettrüsten</strong>. Alle Großmächte vergrößerten ihre Armeen. Deutschland hatte schon einen Kriegsplan, den <strong>Schlieffen-Plan</strong>: erst Frankreich schnell besiegen, dann gegen Russland kämpfen.",
                "frage": "Was sah der Schlieffen-Plan vor?",
                "optionen": ["Erst Russland angreifen, dann Frankreich", "Nur mit der Flotte gegen Großbritannien kämpfen", "Erst Frankreich schnell besiegen, dann Russland"],
                "loesung": 2,
                "erklaerung": "Genau: Erst ein schneller Sieg im Westen, dann der Krieg im Osten.",
            },
            {
                "ueberschrift": "Bündnissystem",
                "bild": "ursachen-4", "bild_alt": "Schaubild: Bündnissystem",
                "text": "Europa war in zwei Blöcke geteilt. Auf der einen Seite der <strong>Dreibund</strong>: Deutschland, Österreich-Ungarn, Italien (1882). Auf der anderen Seite die <strong>Triple Entente</strong>: Frankreich, Russland, Großbritannien (1907). Ein Streit zwischen zwei Staaten konnte so alle in den Krieg ziehen. Besonders gefährlich war der <strong>Balkan</strong>. Dort verlor das Osmanische Reich Gebiete, und Österreich-Ungarn und Russland stritten um Einfluss.",
                "frage": "Welche Staaten bildeten die Triple Entente?",
                "optionen": ["Deutschland, Österreich-Ungarn und Italien", "Frankreich, Russland und Großbritannien", "Serbien, Belgien und das Osmanische Reich"],
                "loesung": 1,
                "erklaerung": "Richtig: Frankreich, Russland und Großbritannien standen dem Dreibund gegenüber.",
            },
        ],
    },
    "ausloeser": {
        "station": "L2", "eyebrow": "Lesestrecke M2",
        "titel": "Das Attentat von Sarajevo und die Julikrise",
        "abschnitte": [
            {
                "ueberschrift": "Das Attentat",
                "bild": "ausloeser-1", "bild_alt": "Schaubild: Das Attentat",
                "text": "Am <strong>28. Juni 1914</strong> erschoss <strong>Gavrilo Princip</strong> in Sarajevo den Thronfolger von Österreich-Ungarn, <strong>Franz Ferdinand</strong>, und seine Frau Sophie. Princip war ein serbischer Nationalist. Eine serbische Geheimgruppe, die „Schwarze Hand“, hatte ihm geholfen. Österreich-Ungarn gab Serbien die Schuld.",
                "frage": "Wer wurde am 28. Juni 1914 erschossen?",
                "optionen": ["Der Thronfolger Franz Ferdinand und seine Frau Sophie", "Kaiser Wilhelm II.", "Der König von Serbien"],
                "loesung": 0,
                "erklaerung": "Genau: Das Attentat galt dem Thronfolger von Österreich-Ungarn.",
            },
            {
                "ueberschrift": "Blankoscheck und Ultimatum",
                "bild": "ausloeser-2", "bild_alt": "Schaubild: Blankoscheck und Ultimatum",
                "text": "Am <strong>5./6. Juli</strong> versprach Deutschland Österreich-Ungarn volle Unterstützung. Das nennt man den <strong>„Blankoscheck“</strong>. Am <strong>23. Juli</strong> stellte Wien Serbien ein <strong>Ultimatum</strong>: Serbien sollte die Hetze gegen Österreich verbieten, die Hintermänner des Attentats bestrafen und österreichische Beamte im eigenen Land ermitteln lassen. Frist: 48 Stunden. Serbien nahm fast alles an, nur keine fremden Ermittler im Land. Trotzdem erklärte Österreich-Ungarn am <strong>28. Juli</strong> Serbien den Krieg.",
                "frage": "Was ist der „Blankoscheck“?",
                "optionen": ["Serbien zahlt Geld an Österreich-Ungarn", "Großbritannien verspricht Serbien Hilfe", "Deutschland verspricht Österreich-Ungarn volle Unterstützung"],
                "loesung": 2,
                "erklaerung": "Richtig: Wie ein unterschriebener Scheck ohne Betrag. Wien konnte selbst entscheiden, wie weit es geht.",
            },
            {
                "ueberschrift": "Die Kettenreaktion",
                "bild": "ausloeser-3", "bild_alt": "Schaubild: Die Kettenreaktion",
                "text": "Jetzt griffen die Bündnisse. Russland machte am <strong>30. Juli</strong> seine Armee mobil, um Serbien zu helfen. Deutschland erklärte am <strong>1. August</strong> Russland den Krieg und am <strong>3. August</strong> Frankreich. Am <strong>4. August</strong> marschierten deutsche Truppen in das neutrale <strong>Belgien</strong> ein. Darauf erklärte Großbritannien Deutschland den Krieg.",
                "frage": "Warum erklärte Großbritannien Deutschland den Krieg?",
                "optionen": ["Weil Deutschland Serbien angegriffen hatte", "Weil deutsche Truppen in das neutrale Belgien einmarschierten", "Weil Russland darum bat"],
                "loesung": 1,
                "erklaerung": "Genau: Der Einmarsch in Belgien war für London der Grund.",
            },
            {
                "ueberschrift": "Auslöser und Ursache",
                "bild": "ausloeser-4", "bild_alt": "Schaubild: Auslöser und Ursache",
                "text": "Diese fünf Wochen heißen <strong>Julikrise</strong>. Das Attentat war nur der <strong>Auslöser</strong> – der Funke. Die <strong>Ursachen</strong> lagen tiefer – das Pulverfass. Im August 1914 jubelten viele Menschen. Aber die Freude war nicht überall so groß, wie die Propaganda behauptete.",
                "frage": "Welches Bild passt zum Attentat?",
                "optionen": ["Der Funke, der das Pulverfass entzündet", "Das Pulverfass selbst", "Der Regen, der das Feuer löscht"],
                "loesung": 0,
                "erklaerung": "Richtig: Der Auslöser ist der Funke. Die Ursachen sind das Pulverfass.",
            },
        ],
    },
    "verlauf": {
        "station": "L3", "eyebrow": "Lesestrecke M3",
        "titel": "Vom Bewegungskrieg zum Stellungskrieg",
        "abschnitte": [
            {
                "ueberschrift": "1914: Der Plan scheitert",
                "bild": "verlauf-1", "bild_alt": "Schaubild: 1914: Der Plan scheitert",
                "text": "Der Schlieffen-Plan scheiterte im September in der <strong>Marneschlacht</strong>. Die Deutschen wurden vor Paris gestoppt. Danach bewegte sich die Westfront kaum noch: <strong>Stellungskrieg</strong>. Schützengräben zogen sich von der Nordsee bis zur Schweiz. Im Osten besiegte Deutschland die Russen bei <strong>Tannenberg</strong>. Dort blieb die Front beweglicher.",
                "frage": "Wo wurde der deutsche Angriff 1914 gestoppt?",
                "optionen": ["In der Marneschlacht vor Paris", "Bei Tannenberg", "An der Somme"],
                "loesung": 0,
                "erklaerung": "Genau: An der Marne endete der schnelle Krieg im Westen.",
            },
            {
                "ueberschrift": "1915/1916: Materialschlachten",
                "bild": "verlauf-2", "bild_alt": "Schaubild: 1915/1916: Materialschlachten",
                "text": "1915 setzte Deutschland bei <strong>Ypern</strong> zum ersten Mal Giftgas ein. Italien trat auf der Seite der Entente in den Krieg ein. 1916 kam es zu den <strong>Materialschlachten</strong> um <strong>Verdun</strong> und an der <strong>Somme</strong>. Hunderttausende starben. Die Front bewegte sich trotzdem kaum. Maschinengewehre und Kanonen machten jeden Angriff zum Massensterben.",
                "frage": "Was ist typisch für eine Materialschlacht?",
                "optionen": ["Riesige Verluste, aber die Front bewegt sich kaum", "Ein schneller Durchbruch mit Reitern", "Kämpfe nur auf See"],
                "loesung": 0,
                "erklaerung": "Richtig: Verdun und Somme kosteten Hunderttausende – und brachten fast kein Land.",
            },
            {
                "ueberschrift": "1917: Die Wende",
                "bild": "verlauf-3", "bild_alt": "Schaubild: 1917: Die Wende",
                "text": "Ab Februar 1917 versenkten deutsche U-Boote ohne Warnung auch neutrale Schiffe: der <strong>uneingeschränkte U-Boot-Krieg</strong>. Darum traten die <strong>USA</strong> im April 1917 in den Krieg ein. In Russland stürzten Revolutionen den Zaren. Die neue Regierung schloss im März 1918 den Frieden von <strong>Brest-Litowsk</strong>.",
                "frage": "Warum traten die USA in den Krieg ein?",
                "optionen": ["Wegen der Marneschlacht", "Wegen des Friedens von Brest-Litowsk", "Wegen des uneingeschränkten U-Boot-Kriegs"],
                "loesung": 2,
                "erklaerung": "Genau: Die U-Boote versenkten auch neutrale Schiffe. Das brachte die USA in den Krieg.",
            },
            {
                "ueberschrift": "Totaler Krieg und 1918",
                "bild": "verlauf-4", "bild_alt": "Schaubild: Totaler Krieg und 1918",
                "text": "Der Krieg betraf alle Menschen. Frauen arbeiteten in Waffenfabriken. Die britische Seeblockade ließ kaum Waren nach Deutschland. Im <strong>„Steckrübenwinter“</strong> 1916/17 hungerten die Menschen. Propaganda beeinflusste die Stimmung. <strong>1918</strong> scheiterte die letzte deutsche Offensive. Ab dem <strong>8. August</strong> drängten die Alliierten mit Panzern und US-Soldaten die Deutschen zurück.",
                "frage": "Was war der Grund für den „Steckrübenwinter“?",
                "optionen": ["Ein Vulkanausbruch", "Die britische Seeblockade", "Der Frieden von Brest-Litowsk"],
                "loesung": 1,
                "erklaerung": "Richtig: Die Blockade ließ kaum noch Lebensmittel nach Deutschland.",
            },
        ],
    },
    "kriegsende": {
        "station": "L4", "eyebrow": "Lesestrecke M4",
        "titel": "Niederlage, Revolution, Waffenstillstand",
        "abschnitte": [
            {
                "ueberschrift": "Militärisch verloren",
                "bild": "kriegsende-1", "bild_alt": "Schaubild: Militärisch verloren",
                "text": "Im Sommer 1918 war der Krieg für Deutschland verloren. Die Offensive war gescheitert. Jeden Tag kamen rund 10.000 neue US-Soldaten nach Frankreich. Zu Hause hungerten die Menschen. Am <strong>29. September 1918</strong> verlangte die <strong>Oberste Heeresleitung</strong> (Hindenburg und Ludendorff) einen Waffenstillstand. Grundlage sollten die <strong>14 Punkte</strong> von US-Präsident <strong>Wilson</strong> sein.",
                "frage": "Wer verlangte am 29. September 1918 einen Waffenstillstand?",
                "optionen": ["Die Matrosen in Kiel", "US-Präsident Wilson", "Die Oberste Heeresleitung um Hindenburg und Ludendorff"],
                "loesung": 2,
                "erklaerung": "Genau: Die Generäle selbst wollten den Waffenstillstand. Das ist wichtig für die Dolchstoßlegende.",
            },
            {
                "ueberschrift": "Reformen und Verbündete",
                "bild": "kriegsende-2", "bild_alt": "Schaubild: Reformen und Verbündete",
                "text": "Mit den <strong>Oktoberreformen</strong> bekam der Reichstag mehr Macht. Prinz <strong>Max von Baden</strong> wurde Reichskanzler. Er brauchte nun die Mehrheit im Reichstag. Gleichzeitig gaben die Verbündeten auf: Bulgarien (29. September), das Osmanische Reich (30. Oktober) und Österreich-Ungarn (3. November).",
                "frage": "Was änderten die Oktoberreformen?",
                "optionen": ["Der Reichskanzler brauchte nun den Reichstag", "Der Kaiser bekam mehr Macht", "Deutschland trat in den Völkerbund ein"],
                "loesung": 0,
                "erklaerung": "Richtig: Die Regierung brauchte jetzt die Mehrheit des Reichstags.",
            },
            {
                "ueberschrift": "Matrosenaufstand und Revolution",
                "bild": "kriegsende-3", "bild_alt": "Schaubild: Matrosenaufstand und Revolution",
                "text": "Die Marineführung wollte die Flotte zu einer letzten Schlacht schicken. Die Matrosen weigerten sich. Der <strong>Matrosenaufstand in Kiel</strong> (3./4. November) wurde zur <strong>Novemberrevolution</strong>. Überall bildeten sich Räte aus Arbeitern und Soldaten. Am <strong>9. November 1918</strong> dankte der Kaiser ab. <strong>Philipp Scheidemann</strong> rief die Republik aus. <strong>Friedrich Ebert</strong> (SPD) übernahm die Regierung.",
                "frage": "Wo begann die Novemberrevolution?",
                "optionen": ["Im Reichstag in Berlin", "Beim Matrosenaufstand in Kiel", "Im Wald von Compiègne"],
                "loesung": 1,
                "erklaerung": "Genau: Die Matrosen in Kiel weigerten sich. Der Aufstand breitete sich aus.",
            },
            {
                "ueberschrift": "Waffenstillstand und Dolchstoßlegende",
                "bild": "kriegsende-4", "bild_alt": "Schaubild: Waffenstillstand und Dolchstoßlegende",
                "text": "Am <strong>11. November 1918</strong> unterschrieb Matthias Erzberger bei <strong>Compiègne</strong> den Waffenstillstand. Später verbreitete Ludendorff die <strong>Dolchstoßlegende</strong>: Das Heer sei unbesiegt gewesen und von der Heimat verraten worden. Das war falsch. Die Generäle selbst hatten den Waffenstillstand verlangt. Die Lüge schadete der jungen Republik sehr.",
                "frage": "Warum war die Dolchstoßlegende falsch?",
                "optionen": ["Weil die Generäle selbst den Waffenstillstand verlangt hatten", "Weil der Krieg erst 1919 endete", "Weil es keine Revolution gab"],
                "loesung": 0,
                "erklaerung": "Richtig: Nicht die Heimat, sondern die Heeresleitung hatte um den Waffenstillstand gebeten.",
            },
        ],
    },
    "folgen": {
        "station": "L5", "eyebrow": "Lesestrecke M5",
        "titel": "Ein neues Europa und die „Urkatastrophe“",
        "abschnitte": [
            {
                "ueberschrift": "Die Toten",
                "bild": "folgen-1", "bild_alt": "Schaubild: Die Toten",
                "text": "Rund 9 bis 10 Millionen Soldaten starben. Dazu kamen etwa 6 bis 7 Millionen Zivilisten. Millionen Menschen wurden verletzt. Die <strong>Spanische Grippe</strong> 1918–1920 tötete weltweit weitere Millionen. Eine ganze Generation war traumatisiert.",
                "frage": "Wie viele Soldaten starben ungefähr?",
                "optionen": ["Rund 900.000", "Rund 9 bis 10 Millionen", "Rund 90 Millionen"],
                "loesung": 1,
                "erklaerung": "Genau: 9 bis 10 Millionen Soldaten – und dazu Millionen Zivilisten.",
            },
            {
                "ueberschrift": "Der Versailler Vertrag",
                "bild": "folgen-2", "bild_alt": "Schaubild: Der Versailler Vertrag",
                "text": "Am <strong>28. Juni 1919</strong> musste Deutschland den Vertrag unterschreiben. Es durfte nicht mitverhandeln. Es musste die Kriegsschuld anerkennen (<strong>Artikel 231</strong>) und <strong>Reparationen</strong> zahlen. Es verlor rund <strong>13 Prozent seines Gebiets</strong>: Elsass-Lothringen an Frankreich, Posen und Westpreußen an Polen, alle Kolonien. Das Heer durfte nur noch <strong>100.000 Mann</strong> haben. Viele Deutsche nannten den Vertrag „Diktat“. Das belastete die <strong>Weimarer Republik</strong>.",
                "frage": "Was stand in Artikel 231?",
                "optionen": ["Die Größe der deutschen Flotte", "Deutschland tritt in den Völkerbund ein", "Deutschland und seine Verbündeten sind schuld am Krieg"],
                "loesung": 2,
                "erklaerung": "Richtig: Artikel 231 ist der Kriegsschuldartikel. Er war die Grundlage für die Reparationen.",
            },
            {
                "ueberschrift": "Eine neue Landkarte",
                "bild": "folgen-3", "bild_alt": "Schaubild: Eine neue Landkarte",
                "text": "Vier Reiche zerfielen: das deutsche Kaiserreich, Österreich-Ungarn, das Russische Reich und das Osmanische Reich. Neue Staaten entstanden: <strong>Polen, die Tschechoslowakei, Jugoslawien</strong>, die baltischen Staaten und Finnland. In Russland regierten nach der Revolution die Bolschewiki. Der <strong>Völkerbund</strong> (1920) sollte neue Kriege verhindern. Die USA traten ihm aber nicht bei.",
                "frage": "Wozu wurde der Völkerbund gegründet?",
                "optionen": ["Um neue Kriege zu verhindern", "Um Deutschland neue Kolonien zu geben", "Um die Spanische Grippe zu bekämpfen"],
                "loesung": 0,
                "erklaerung": "Genau: Der Völkerbund sollte Streit friedlich lösen. Ohne die USA blieb er aber schwach.",
            },
            {
                "ueberschrift": "Langfristige Folgen",
                "bild": "folgen-4", "bild_alt": "Schaubild: Langfristige Folgen",
                "text": "Frauen hatten im Krieg die Arbeit der Männer gemacht. In Deutschland bekamen sie 1918/19 das <strong>Wahlrecht</strong>. Schulden, Inflation (1923 Hyperinflation) und Rachegedanken vergifteten die Politik. Der Erste Weltkrieg bereitete den Boden für Faschismus, Nationalsozialismus und den Zweiten Weltkrieg. Deshalb nannte ihn der Historiker George F. Kennan die <strong>„Urkatastrophe des 20. Jahrhunderts“</strong>.",
                "frage": "Warum nannte Kennan den Ersten Weltkrieg die „Urkatastrophe“?",
                "optionen": ["Weil er der längste Krieg der Geschichte war", "Weil er den Boden für Nationalsozialismus und Zweiten Weltkrieg bereitete", "Weil er die Spanische Grippe auslöste"],
                "loesung": 1,
                "erklaerung": "Richtig: Aus dem Ersten Weltkrieg wuchsen die Katastrophen des 20. Jahrhunderts.",
            },
        ],
    },
}

STATION_ZU_ABSCHNITT = {v["station"]: k for k, v in LESESTRECKEN.items()}


def lesestrecke_fuer_client(key: str, status: dict) -> dict:
    """Text, Fragen und Optionen ohne Lösungen. Erklärungen nur für bereits bestandene Abschnitte."""
    strecke = LESESTRECKEN[key]
    phase = int(status.get("phase", 0))
    abschnitte = []
    for i, a in enumerate(strecke["abschnitte"]):
        eintrag = {"ueberschrift": a["ueberschrift"], "text": a["text"], "frage": a["frage"], "optionen": list(a["optionen"]),
                   "bild": f"/static/img/lese/{a['bild']}.svg?v={ASSET_VERSION}" if a.get("bild") else None, "bild_alt": a.get("bild_alt", "")}
        if i < phase:
            eintrag["erklaerung"] = a["erklaerung"]
        abschnitte.append(eintrag)
    return {
        "key": key, "station": strecke["station"], "eyebrow": strecke["eyebrow"], "titel": strecke["titel"],
        "abschnitte": abschnitte, "anzahl": len(abschnitte),
        "status": {"phase": phase, "fertig": bool(status.get("fertig")), "retry_until": float(status.get("retry_until", 0) or 0), "versuche": int(status.get("versuche", 0))},
    }


def pruefen(key: str, phase: int, wahl: int) -> tuple[bool, str]:
    abschnitt = LESESTRECKEN[key]["abschnitte"][phase]
    korrekt = int(wahl) == abschnitt["loesung"]
    return korrekt, abschnitt["erklaerung"] if korrekt else ""


def gemischte_reihenfolge(anzahl: int) -> list[int]:
    reihenfolge = list(range(anzahl))
    random.shuffle(reihenfolge)
    return reihenfolge
