"""Serverseitige Inhalte: gegatete Lesestrecken mit Verständnisfragen.

Die Lösungen liegen ausschließlich hier. Der Client erhält Text, Frage und Optionen,
aber nie die richtige Position. Jede Frage lässt sich aus ihrem Abschnitt allein beantworten.
"""

import random

LESESTRECKEN = {
    "ursachen": {
        "station": "L1", "eyebrow": "Lesestrecke M1",
        "titel": "Langfristige Ursachen: Warum war Europa 1914 ein „Pulverfass“?",
        "abschnitte": [
            {
                "ueberschrift": "Imperialismus",
                "text": "Die europäischen Großmächte wetteiferten um Kolonien, Rohstoffe und Absatzmärkte. Deutschland, erst 1871 gegründet, kam zu spät und forderte einen „Platz an der Sonne“. In den <strong>Marokkokrisen 1905 und 1911</strong> standen Deutschland und Frankreich kurz vor einem Krieg.",
                "frage": "Worum wetteiferten die Großmächte im Imperialismus?",
                "optionen": ["Um Kolonien, Rohstoffe und Absatzmärkte", "Um die meisten Eisenbahnlinien in Europa", "Um den Sitz des Völkerbunds"],
                "loesung": 0,
                "erklaerung": "Genau: Kolonien versprachen Rohstoffe, Märkte und Ansehen – darum ging der Wettlauf.",
            },
            {
                "ueberschrift": "Nationalismus",
                "text": "Viele Menschen hielten das eigene Volk für überlegen. Frankreich wollte das 1871 verlorene <strong>Elsass-Lothringen</strong> zurück. Serbische Nationalisten wollten alle Südslawen in einem Staat vereinen – eine Bedrohung für den Vielvölkerstaat Österreich-Ungarn.",
                "frage": "Welches Gebiet wollte Frankreich zurückgewinnen?",
                "optionen": ["Elsass-Lothringen", "Bosnien", "Belgien"],
                "loesung": 0,
                "erklaerung": "Richtig: Elsass-Lothringen hatte Frankreich 1871 an das Deutsche Reich verloren.",
            },
            {
                "ueberschrift": "Militarismus und Wettrüsten",
                "text": "Das Militär genoss hohes Ansehen, Krieg galt als normales Mittel der Politik. Deutschland und Großbritannien lieferten sich ein <strong>Flottenwettrüsten</strong>, alle Großmächte vergrößerten ihre Heere. Die Generalstäbe hatten fertige Kriegspläne – Deutschland den <strong>Schlieffen-Plan</strong>: erst Frankreich schnell besiegen, dann gegen Russland kämpfen.",
                "frage": "Was sah der Schlieffen-Plan vor?",
                "optionen": ["Erst Frankreich schnell besiegen, dann gegen Russland kämpfen", "Erst Russland angreifen, dann Frankreich", "Nur die Flotte gegen Großbritannien einsetzen"],
                "loesung": 0,
                "erklaerung": "Genau: Der Plan setzte auf einen schnellen Sieg im Westen, bevor Russland mobil war.",
            },
            {
                "ueberschrift": "Bündnissystem",
                "text": "Europa war in zwei Blöcke geteilt: der <strong>Dreibund</strong> (Deutschland, Österreich-Ungarn, Italien; 1882) und die <strong>Triple Entente</strong> (Frankreich, Russland, Großbritannien; 1907). Ein Streit zwischen zwei Staaten konnte so alle Großmächte in den Krieg ziehen. Besonders gefährlich war der <strong>Balkan</strong>, wo das Osmanische Reich Gebiete verlor und Österreich-Ungarn und Russland um Einfluss kämpften.",
                "frage": "Welche Staaten bildeten die Triple Entente?",
                "optionen": ["Frankreich, Russland und Großbritannien", "Deutschland, Österreich-Ungarn und Italien", "Serbien, Belgien und das Osmanische Reich"],
                "loesung": 0,
                "erklaerung": "Richtig: Frankreich, Russland und Großbritannien standen dem Dreibund gegenüber.",
            },
        ],
    },
    "ausloeser": {
        "station": "L2", "eyebrow": "Lesestrecke M2",
        "titel": "Der Auslöser: Das Attentat von Sarajevo und die Julikrise",
        "abschnitte": [
            {
                "ueberschrift": "Das Attentat",
                "text": "Am <strong>28. Juni 1914</strong> erschoss der bosnisch-serbische Nationalist <strong>Gavrilo Princip</strong> in Sarajevo den österreichisch-ungarischen Thronfolger <strong>Franz Ferdinand</strong> und seine Frau Sophie. Princip gehörte zu einer Gruppe, die von der serbischen Geheimorganisation „Schwarze Hand“ unterstützt wurde. Österreich-Ungarn machte Serbien verantwortlich.",
                "frage": "Wer wurde am 28. Juni 1914 in Sarajevo erschossen?",
                "optionen": ["Der Thronfolger Franz Ferdinand und seine Frau Sophie", "Kaiser Wilhelm II.", "Der serbische König"],
                "loesung": 0,
                "erklaerung": "Genau: Das Attentat galt dem österreichisch-ungarischen Thronfolger.",
            },
            {
                "ueberschrift": "Blankoscheck und Ultimatum",
                "text": "Am <strong>5./6. Juli</strong> sicherte Deutschland seinem Verbündeten uneingeschränkte Unterstützung zu – den <strong>„Blankoscheck“</strong>. Am <strong>23. Juli</strong> stellte Wien Serbien ein <strong>Ultimatum</strong> mit fast unerfüllbaren Forderungen. Serbien nahm fast alle Punkte an, doch am <strong>28. Juli</strong> erklärte Österreich-Ungarn Serbien den Krieg.",
                "frage": "Was bedeutet der „Blankoscheck“?",
                "optionen": ["Deutschland sicherte Österreich-Ungarn uneingeschränkte Unterstützung zu", "Serbien zahlte eine Entschädigung an Österreich-Ungarn", "Großbritannien versprach Serbien Hilfe"],
                "loesung": 0,
                "erklaerung": "Richtig: Wie ein unterschriebener, aber nicht ausgefüllter Scheck – Wien konnte den Betrag selbst bestimmen.",
            },
            {
                "ueberschrift": "Die Kettenreaktion",
                "text": "Jetzt griff das Bündnissystem: Russland machte am <strong>30. Juli</strong> als Schutzmacht Serbiens mobil. Deutschland erklärte am <strong>1. August</strong> Russland und am <strong>3. August</strong> Frankreich den Krieg. Am <strong>4. August</strong> marschierten deutsche Truppen in das neutrale <strong>Belgien</strong> ein – daraufhin erklärte Großbritannien Deutschland den Krieg.",
                "frage": "Warum erklärte Großbritannien Deutschland den Krieg?",
                "optionen": ["Weil deutsche Truppen in das neutrale Belgien einmarschierten", "Weil Deutschland Serbien angegriffen hatte", "Weil Russland es darum bat"],
                "loesung": 0,
                "erklaerung": "Genau: Der Bruch der belgischen Neutralität war für London der Kriegsgrund.",
            },
            {
                "ueberschrift": "Auslöser und Ursache",
                "text": "Diese fünf Wochen nennt man <strong>Julikrise</strong>. Das Attentat war nur der <strong>Auslöser</strong> (der „Funke“), die eigentlichen <strong>Ursachen</strong> (das „Pulverfass“) lagen tiefer. Viele Menschen jubelten im August 1914 – das sogenannte „Augusterlebnis“ –, doch die Begeisterung war längst nicht überall so groß, wie die Propaganda behauptete.",
                "frage": "Welches Bild beschreibt das Attentat im Text?",
                "optionen": ["Der Funke, der das Pulverfass entzündet", "Das Pulverfass selbst", "Der Regen, der den Brand löscht"],
                "loesung": 0,
                "erklaerung": "Richtig: Der Auslöser ist der Funke – die Ursachen sind das Pulverfass.",
            },
        ],
    },
    "verlauf": {
        "station": "L3", "eyebrow": "Lesestrecke M3",
        "titel": "Der Verlauf: Vom Bewegungskrieg zur Materialschlacht",
        "abschnitte": [
            {
                "ueberschrift": "1914: Der Plan scheitert",
                "text": "Der Schlieffen-Plan scheiterte im September in der <strong>Marneschlacht</strong> – die Deutschen wurden vor Paris gestoppt. Die Westfront erstarrte zum <strong>Stellungskrieg</strong>: Schützengräben von der Nordsee bis zur Schweiz. Im Osten besiegte Deutschland die Russen bei <strong>Tannenberg</strong>; die Ostfront blieb beweglicher.",
                "frage": "Wo wurde der deutsche Vormarsch 1914 gestoppt?",
                "optionen": ["In der Marneschlacht vor Paris", "Bei Tannenberg in Ostpreußen", "An der Somme"],
                "loesung": 0,
                "erklaerung": "Genau: An der Marne endete der Bewegungskrieg im Westen.",
            },
            {
                "ueberschrift": "1915/1916: Materialschlachten",
                "text": "Bei <strong>Ypern</strong> setzte Deutschland 1915 erstmals Giftgas ein. Italien trat auf Seiten der Entente ein. 1916 tobten die <strong>Materialschlachten</strong> um <strong>Verdun</strong> (rund 700.000 Tote und Verwundete) und an der <strong>Somme</strong> (über eine Million Verluste, erste Panzer) – ohne dass sich die Front wesentlich verschob. Maschinengewehre und Artillerie machten jeden Angriff zum Massensterben.",
                "frage": "Was kennzeichnet eine Materialschlacht laut Text?",
                "optionen": ["Riesige Verluste, ohne dass sich die Front wesentlich verschiebt", "Ein schneller Durchbruch mit Kavallerie", "Kämpfe, die nur auf See stattfinden"],
                "loesung": 0,
                "erklaerung": "Richtig: Verdun und Somme kosteten Hunderttausende – und brachten kaum Gelände.",
            },
            {
                "ueberschrift": "1917: Die Wende",
                "text": "Der <strong>uneingeschränkte U-Boot-Krieg</strong> führte im April zum <strong>Kriegseintritt der USA</strong>. In Russland stürzten die Revolutionen den Zaren; die Bolschewiki schlossen im März 1918 den Frieden von <strong>Brest-Litowsk</strong>.",
                "frage": "Was führte zum Kriegseintritt der USA?",
                "optionen": ["Der uneingeschränkte U-Boot-Krieg", "Die Marneschlacht", "Der Frieden von Brest-Litowsk"],
                "loesung": 0,
                "erklaerung": "Genau: Die Versenkung auch neutraler Schiffe brachte die USA im April 1917 in den Krieg.",
            },
            {
                "ueberschrift": "Totaler Krieg und 1918",
                "text": "Der Krieg erfasste die ganze Gesellschaft: Frauen arbeiteten in Rüstungsfabriken, die britische Seeblockade führte zum <strong>„Steckrübenwinter“</strong> 1916/17 mit Hunger in Deutschland, Propaganda lenkte die Stimmung. <strong>1918:</strong> Die deutsche Frühjahrsoffensive scheiterte; ab dem <strong>8. August</strong>, dem „schwarzen Tag des deutschen Heeres“, drängten die Alliierten mit Panzern und frischen US-Truppen die Deutschen zurück.",
                "frage": "Was war die Ursache des „Steckrübenwinters“?",
                "optionen": ["Die britische Seeblockade", "Ein Vulkanausbruch", "Der Frieden von Brest-Litowsk"],
                "loesung": 0,
                "erklaerung": "Richtig: Die Blockade schnitt Deutschland von Lebensmittelimporten ab.",
            },
        ],
    },
    "kriegsende": {
        "station": "L4", "eyebrow": "Lesestrecke M4",
        "titel": "Das Kriegsende: Niederlage, Revolution, Waffenstillstand",
        "abschnitte": [
            {
                "ueberschrift": "Militärisch verloren",
                "text": "Im Sommer 1918 war der Krieg für Deutschland militärisch verloren: Die Frühjahrsoffensive war gescheitert, täglich trafen rund 10.000 frische US-Soldaten in Frankreich ein, die Heimat hungerte. Am <strong>29. September 1918</strong> verlangte die <strong>Oberste Heeresleitung</strong> (Hindenburg und Ludendorff) einen sofortigen Waffenstillstand. Grundlage sollten die <strong>14 Punkte</strong> des US-Präsidenten <strong>Wilson</strong> sein.",
                "frage": "Wer verlangte am 29. September 1918 einen sofortigen Waffenstillstand?",
                "optionen": ["Die Oberste Heeresleitung um Hindenburg und Ludendorff", "Die Matrosen in Kiel", "Der US-Präsident Wilson"],
                "loesung": 0,
                "erklaerung": "Genau: Die Militärführung selbst forderte den Waffenstillstand – wichtig für die spätere Dolchstoßlegende.",
            },
            {
                "ueberschrift": "Oktoberreformen und Bündnispartner",
                "text": "Mit den <strong>Oktoberreformen</strong> wurde das Kaiserreich parlamentarisiert: Prinz <strong>Max von Baden</strong> wurde Reichskanzler und war nun vom Reichstag abhängig. Gleichzeitig brachen die Verbündeten weg: Bulgarien (29. September), das Osmanische Reich (30. Oktober) und Österreich-Ungarn (3. November) schlossen Waffenstillstände.",
                "frage": "Was änderten die Oktoberreformen?",
                "optionen": ["Der Reichskanzler wurde vom Reichstag abhängig", "Der Kaiser erhielt mehr Macht", "Deutschland trat dem Völkerbund bei"],
                "loesung": 0,
                "erklaerung": "Richtig: Das Reich wurde parlamentarisiert – die Regierung brauchte nun die Mehrheit des Reichstags.",
            },
            {
                "ueberschrift": "Matrosenaufstand und Revolution",
                "text": "Als die Marineführung die Flotte zu einer letzten, aussichtslosen Schlacht auslaufen lassen wollte, verweigerten die Matrosen den Befehl. Der <strong>Matrosenaufstand in Kiel</strong> (3./4. November) wurde zur <strong>Novemberrevolution</strong>: Überall bildeten sich Arbeiter- und Soldatenräte. Am <strong>9. November 1918</strong> wurde die Abdankung Kaiser Wilhelms II. verkündet; <strong>Philipp Scheidemann</strong> rief die Republik aus, <strong>Friedrich Ebert</strong> (SPD) übernahm die Regierung.",
                "frage": "Wo begann die Novemberrevolution?",
                "optionen": ["Beim Matrosenaufstand in Kiel", "Im Reichstag in Berlin", "Im Wald von Compiègne"],
                "loesung": 0,
                "erklaerung": "Genau: Die Matrosen in Kiel verweigerten das sinnlose Auslaufen – der Aufstand breitete sich aus.",
            },
            {
                "ueberschrift": "Waffenstillstand und Dolchstoßlegende",
                "text": "Am <strong>11. November 1918</strong> unterzeichnete Matthias Erzberger im Wald von <strong>Compiègne</strong> den Waffenstillstand. Ludendorff und andere verbreiteten später die <strong>Dolchstoßlegende</strong>: Das „im Felde unbesiegte“ Heer sei von der Heimat verraten worden. Das war falsch – die Militärführung selbst hatte den Waffenstillstand gefordert. Die Lüge belastete die junge Republik schwer.",
                "frage": "Warum war die Dolchstoßlegende falsch?",
                "optionen": ["Weil die Militärführung selbst den Waffenstillstand gefordert hatte", "Weil der Krieg erst 1919 endete", "Weil es keine Revolution gegeben hatte"],
                "loesung": 0,
                "erklaerung": "Richtig: Nicht die Heimat, sondern die Oberste Heeresleitung hatte um Waffenstillstand gebeten.",
            },
        ],
    },
    "folgen": {
        "station": "L5", "eyebrow": "Lesestrecke M5",
        "titel": "Die Folgen: Ein neues Europa und die „Urkatastrophe“",
        "abschnitte": [
            {
                "ueberschrift": "Menschliche Verluste",
                "text": "Rund 9 bis 10 Millionen Soldaten und etwa 6 bis 7 Millionen Zivilisten starben, dazu kamen Millionen Verwundete und Kriegsversehrte. Die <strong>Spanische Grippe</strong> 1918–1920 forderte weltweit weitere Millionen Opfer. Eine ganze Generation war traumatisiert.",
                "frage": "Wie viele Soldaten starben laut Text ungefähr?",
                "optionen": ["Rund 9 bis 10 Millionen", "Rund 900.000", "Rund 90 Millionen"],
                "loesung": 0,
                "erklaerung": "Genau: 9 bis 10 Millionen Soldaten – dazu Millionen Zivilisten.",
            },
            {
                "ueberschrift": "Der Versailler Vertrag",
                "text": "<strong>28. Juni 1919:</strong> Deutschland durfte nicht mitverhandeln. Es musste den <strong>Kriegsschuldartikel 231</strong> anerkennen, <strong>Reparationen</strong> zahlen (1921 auf 132 Milliarden Goldmark festgelegt), rund <strong>13 Prozent seines Gebiets</strong> abtreten (Elsass-Lothringen an Frankreich, Posen und Westpreußen an Polen, alle Kolonien) und sein Heer auf <strong>100.000 Mann</strong> verkleinern. Viele Deutsche nannten ihn „Schandfrieden“ oder „Diktat“ – eine schwere Hypothek für die <strong>Weimarer Republik</strong>.",
                "frage": "Was legte Artikel 231 fest?",
                "optionen": ["Die Kriegsschuld Deutschlands und seiner Verbündeten", "Die Größe der deutschen Flotte", "Den Beitritt Deutschlands zum Völkerbund"],
                "loesung": 0,
                "erklaerung": "Richtig: Artikel 231 ist der Kriegsschuldartikel – die Grundlage für die Reparationen.",
            },
            {
                "ueberschrift": "Eine neue Landkarte",
                "text": "Vier Reiche zerfielen – das deutsche Kaiserreich, Österreich-Ungarn, das Russische Reich und das Osmanische Reich. Neue Staaten entstanden: <strong>Polen, die Tschechoslowakei, Jugoslawien</strong>, die baltischen Staaten, Finnland. In Russland herrschten nach der Revolution die Bolschewiki. Der <strong>Völkerbund</strong> (1920) sollte künftige Kriege verhindern – die USA traten ihm allerdings nicht bei.",
                "frage": "Wozu wurde der Völkerbund gegründet?",
                "optionen": ["Um künftige Kriege zu verhindern", "Um Deutschland neue Kolonien zu geben", "Um die Spanische Grippe zu bekämpfen"],
                "loesung": 0,
                "erklaerung": "Genau: Der Völkerbund sollte Konflikte friedlich lösen – ohne die USA blieb er aber schwach.",
            },
            {
                "ueberschrift": "Langfristige Folgen",
                "text": "Frauen hatten in Fabriken Männer ersetzt und erhielten in Deutschland 1918/19 das <strong>Wahlrecht</strong>. Schulden, Inflation (1923 Hyperinflation) und Revanchismus vergifteten die Politik. Weil der Erste Weltkrieg den Boden für Faschismus, Nationalsozialismus und den Zweiten Weltkrieg bereitete, nannte ihn der Historiker George F. Kennan die <strong>„Urkatastrophe des 20. Jahrhunderts“</strong>.",
                "frage": "Warum nannte Kennan den Ersten Weltkrieg die „Urkatastrophe“?",
                "optionen": ["Weil er den Boden für Nationalsozialismus und Zweiten Weltkrieg bereitete", "Weil er der längste Krieg der Geschichte war", "Weil er die Spanische Grippe auslöste"],
                "loesung": 0,
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
        eintrag = {"ueberschrift": a["ueberschrift"], "text": a["text"], "frage": a["frage"], "optionen": list(a["optionen"])}
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
