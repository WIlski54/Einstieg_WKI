"""Glossar: antippbare Fachbegriffe mit kurzer Erklärung und Schaubild.

Die fett markierten Begriffe der Lesestrecken werden im Browser zu Links. Ein Tipp öffnet
die Erklärung als Einblendung – ohne die App zu verlassen. Sprache: Sek I, kurze Sätze.
"""

import re

BILD = "/static/img/lese/{}.svg"


def normalisieren(text: str) -> str:
    text = re.sub(r"[„“\"'’‚‘]", "", str(text or "")).lower().strip()
    text = re.sub(r"[.,;:!?]+$", "", text).strip()
    return re.sub(r"\s+", " ", text)


GLOSSAR = {
    "marokkokrise": {
        "titel": "Marokkokrisen 1905 und 1911", "bild": "glossar-marokkokrise",
        "text": "Frankreich wollte Marokko in Nordafrika kontrollieren. Deutschland mischte sich ein, um Frankreich zu schwächen. Zweimal stand Europa kurz vor einem Krieg. Am Ende ging Deutschland leer aus und fühlte sich ausgegrenzt.",
        "aliase": ["Marokkokrisen 1905 und 1911", "Marokkokrise", "Marokkokrisen"],
    },
    "elsass-lothringen": {
        "titel": "Elsass-Lothringen", "bild": "ursachen-2",
        "text": "Ein Gebiet an der Grenze zwischen Frankreich und Deutschland. 1871, nach dem Deutsch-Französischen Krieg, kam es zu Deutschland. Frankreich wollte es unbedingt zurück. 1919 fiel es an Frankreich.",
        "aliase": ["Elsass-Lothringen", "Elsaß-Lothringen"],
    },
    "flottenwettruesten": {
        "titel": "Flottenwettrüsten", "bild": "ursachen-3",
        "text": "Ab 1898 baute Deutschland eine große Kriegsflotte. Großbritannien sah das als Bedrohung und baute noch mehr Schiffe. Beide Länder gaben riesige Summen aus. Das Vertrauen zwischen ihnen verschwand.",
        "aliase": ["Flottenwettrüsten", "Wettrüsten"],
    },
    "schlieffen-plan": {
        "titel": "Der Schlieffen-Plan", "bild": "glossar-schlieffen",
        "text": "Der deutsche Kriegsplan, benannt nach General Alfred von Schlieffen (1905). Die Idee: Frankreich in sechs Wochen durch Belgien besiegen, dann alle Truppen gegen Russland schicken. 1914 scheiterte der Plan an der Marne.",
        "aliase": ["Schlieffen-Plan", "Schlieffenplan"],
    },
    "dreibund": {
        "titel": "Der Dreibund", "bild": "ursachen-4",
        "text": "Bündnis von 1882: Deutschland, Österreich-Ungarn und Italien. Es war nur zur Verteidigung gedacht. Italien blieb 1914 deshalb neutral und kämpfte ab 1915 sogar gegen Österreich-Ungarn.",
        "aliase": ["Dreibund", "Zweibund"],
    },
    "triple-entente": {
        "titel": "Die Triple Entente", "bild": "ursachen-4",
        "text": "Bündnis aus Frankreich, Russland und Großbritannien. Es entstand in Schritten zwischen 1894 und 1907. „Entente“ ist Französisch und heißt „Verständigung“. Zusammen mit Serbien nennt man diese Seite auch „Alliierte“.",
        "aliase": ["Triple Entente", "Entente"],
    },
    "balkan": {
        "titel": "Der Balkan – das „Pulverfass Europas“", "bild": "ursachen-4",
        "text": "Der Balkan ist eine Halbinsel in Südosteuropa. Das Osmanische Reich verlor dort immer mehr Gebiete. Serbien, Österreich-Ungarn und Russland stritten um Einfluss. Zwei Balkankriege (1912/13) hatten die Lage weiter verschärft.",
        "aliase": ["Balkan", "Pulverfass Balkan"],
    },
    "gavrilo-princip": {
        "titel": "Gavrilo Princip", "bild": "ausloeser-1",
        "text": "Ein 19-jähriger bosnischer Serbe. Er gehörte zu einer Gruppe junger Nationalisten, die von der serbischen Geheimorganisation „Schwarze Hand“ Waffen bekam. Am 28. Juni 1914 erschoss er das Thronfolgerpaar. Er starb 1918 im Gefängnis.",
        "aliase": ["Gavrilo Princip", "Princip"],
    },
    "franz-ferdinand": {
        "titel": "Franz Ferdinand", "bild": "ausloeser-1",
        "text": "Der Thronfolger von Österreich-Ungarn und Neffe des alten Kaisers Franz Joseph. Am 28. Juni 1914 besuchte er Sarajevo. Dort wurde er zusammen mit seiner Frau Sophie ermordet.",
        "aliase": ["Franz Ferdinand"],
    },
    "blankoscheck": {
        "titel": "Der „Blankoscheck“", "bild": "ausloeser-2",
        "text": "Am 5./6. Juli 1914 versprach Kaiser Wilhelm II. Österreich-Ungarn volle Unterstützung – egal, was es gegen Serbien tut. Wie ein unterschriebener Scheck ohne Betrag. Das machte Wien mutig und den Krieg wahrscheinlicher.",
        "aliase": ["Blankoscheck"],
    },
    "ultimatum": {
        "titel": "Das Ultimatum", "bild": "ausloeser-2",
        "text": "Ein Ultimatum ist eine Forderung mit Frist. Wenn sie nicht erfüllt wird, folgen Konsequenzen. Wien stellte Serbien am 23. Juli 1914 zehn harte Forderungen mit 48 Stunden Frist. Serbien nahm fast alle an – trotzdem kam der Krieg.",
        "aliase": ["Ultimatum"],
    },
    "belgien": {
        "titel": "Belgien – der neutrale Nachbar", "bild": "glossar-schlieffen",
        "text": "Belgien war seit 1839 neutral. Die Großmächte, auch Großbritannien, hatten das garantiert. Der Schlieffen-Plan führte trotzdem durch Belgien. Als deutsche Truppen am 4. August 1914 einmarschierten, erklärte Großbritannien den Krieg.",
        "aliase": ["Belgien", "Neutralität Belgiens"],
    },
    "julikrise": {
        "titel": "Die Julikrise", "bild": "ausloeser-3",
        "text": "So heißen die fünf Wochen zwischen dem Attentat (28. Juni 1914) und dem Kriegsbeginn (4. August 1914). Jede Entscheidung löste die nächste aus – wie Dominosteine. Historiker streiten bis heute, wer die größte Schuld trug.",
        "aliase": ["Julikrise"],
    },
    "ausloeser": {
        "titel": "Auslöser", "bild": "ausloeser-4",
        "text": "Ein Auslöser ist das Ereignis, das etwas in Gang setzt – wie ein Funke. Der Auslöser des Ersten Weltkriegs war das Attentat von Sarajevo. Ohne die tieferen Ursachen hätte der Funke aber nichts entzündet.",
        "aliase": ["Auslöser"],
    },
    "ursachen": {
        "titel": "Ursachen", "bild": "ausloeser-4",
        "text": "Ursachen sind die tiefen Gründe, die lange vorher bestehen – wie das Pulver im Fass. Beim Ersten Weltkrieg: Imperialismus, Nationalismus, Militarismus und das Bündnissystem.",
        "aliase": ["Ursachen", "Ursache"],
    },
    "marneschlacht": {
        "titel": "Die Marneschlacht", "bild": "verlauf-1",
        "text": "September 1914 am Fluss Marne, kurz vor Paris. Französische und britische Truppen stoppten den deutschen Vormarsch. Der Schlieffen-Plan war gescheitert. Danach begann der Stellungskrieg.",
        "aliase": ["Marneschlacht", "Marne"],
    },
    "stellungskrieg": {
        "titel": "Stellungskrieg", "bild": "verlauf-1",
        "text": "Die Front bewegt sich kaum. Die Soldaten leben monatelang in Schützengräben. Wer angreift, läuft ins Feuer von Maschinengewehren und Kanonen. Zwischen den Gräben liegt das „Niemandsland“.",
        "aliase": ["Stellungskrieg"],
    },
    "tannenberg": {
        "titel": "Schlacht bei Tannenberg", "bild": None,
        "text": "Ende August 1914 in Ostpreußen. Deutsche Truppen unter Hindenburg und Ludendorff besiegten eine russische Armee. Die beiden Generäle wurden dadurch in Deutschland zu Helden.",
        "aliase": ["Tannenberg"],
    },
    "ypern": {
        "titel": "Ypern – der erste Giftgasangriff", "bild": "verlauf-2",
        "text": "Ypern ist eine Stadt in Belgien. Im April 1915 setzte Deutschland dort zum ersten Mal Chlorgas ein. Danach benutzten beide Seiten Giftgas. Gasmasken wurden zur normalen Ausrüstung.",
        "aliase": ["Ypern"],
    },
    "materialschlacht": {
        "titel": "Materialschlacht", "bild": "verlauf-2",
        "text": "Eine Schlacht, in der riesige Mengen an Granaten, Maschinengewehren und Munition eingesetzt werden. Ziel: den Gegner „ausbluten“ lassen. Hunderttausende sterben, die Front bewegt sich kaum. Beispiele: Verdun und Somme 1916.",
        "aliase": ["Materialschlachten", "Materialschlacht"],
    },
    "verdun": {
        "titel": "Die Schlacht um Verdun", "bild": "verlauf-2",
        "text": "Februar bis Dezember 1916. Deutsche Truppen griffen die französische Festung Verdun an. Rund 700.000 Soldaten wurden getötet oder verwundet. Verdun steht bis heute für sinnloses Sterben.",
        "aliase": ["Verdun"],
    },
    "somme": {
        "titel": "Die Schlacht an der Somme", "bild": "verlauf-2",
        "text": "Juli bis November 1916. Briten und Franzosen griffen am Fluss Somme an. Allein am ersten Tag verloren die Briten 57.000 Mann. Hier fuhren die ersten Panzer. Insgesamt über eine Million Verluste.",
        "aliase": ["Somme"],
    },
    "u-boot-krieg": {
        "titel": "Der uneingeschränkte U-Boot-Krieg", "bild": "verlauf-3",
        "text": "Ab Februar 1917 versenkten deutsche U-Boote alle Schiffe um Großbritannien ohne Warnung – auch neutrale und Passagierschiffe. So sollte Großbritannien ausgehungert werden. Stattdessen traten die USA in den Krieg ein.",
        "aliase": ["uneingeschränkte U-Boot-Krieg", "U-Boot-Krieg", "uneingeschränkter U-Boot-Krieg"],
    },
    "usa": {
        "titel": "Die USA im Ersten Weltkrieg", "bild": "verlauf-3",
        "text": "Die Vereinigten Staaten waren bis 1917 neutral, lieferten aber Waren an die Entente. Wegen des U-Boot-Kriegs erklärten sie im April 1917 den Krieg. Bis November 1918 kamen rund zwei Millionen US-Soldaten nach Frankreich.",
        "aliase": ["USA"],
    },
    "brest-litowsk": {
        "titel": "Der Frieden von Brest-Litowsk", "bild": "verlauf-3",
        "text": "3. März 1918: Friedensvertrag zwischen Sowjetrussland und den Mittelmächten. Russland verlor riesige Gebiete, zum Beispiel Polen, das Baltikum und die Ukraine. Der Krieg im Osten war beendet.",
        "aliase": ["Brest-Litowsk"],
    },
    "steckruebenwinter": {
        "titel": "Der Steckrübenwinter", "bild": "glossar-steckruebe",
        "text": "Winter 1916/17. Die Kartoffelernte war schlecht, die britische Seeblockade ließ kaum Lebensmittel ins Land. Die Menschen aßen vor allem Steckrüben. Hunderttausende starben an Hunger und Krankheiten.",
        "aliase": ["Steckrübenwinter"],
    },
    "oberste-heeresleitung": {
        "titel": "Die Oberste Heeresleitung", "bild": "glossar-ohl",
        "text": "Die Führung des deutschen Heeres. Ab 1916 waren das Paul von Hindenburg und Erich Ludendorff. Sie bestimmten fast die ganze Politik. Am 29. September 1918 verlangten sie selbst einen sofortigen Waffenstillstand.",
        "aliase": ["Oberste Heeresleitung", "Heeresleitung"],
    },
    "14-punkte": {
        "titel": "Die 14 Punkte", "bild": "glossar-14punkte",
        "text": "Ein Friedensplan von US-Präsident Wilson vom Januar 1918. Darin: keine Geheimverträge, Abrüstung, Völker bestimmen selbst über sich, ein Völkerbund. Deutschland hoffte auf einen milden Frieden – Versailles wurde härter.",
        "aliase": ["14 Punkte", "14 Punkte Wilsons"],
    },
    "wilson": {
        "titel": "Woodrow Wilson", "bild": "glossar-14punkte",
        "text": "US-Präsident von 1913 bis 1921. Er wollte einen gerechten Frieden und gründete den Völkerbund. Der amerikanische Senat lehnte den Beitritt zum Völkerbund aber ab.",
        "aliase": ["Wilson"],
    },
    "oktoberreformen": {
        "titel": "Die Oktoberreformen", "bild": "kriegsende-2",
        "text": "Im Oktober 1918 wurde die Verfassung geändert. Der Reichskanzler brauchte nun die Mehrheit des Reichstags. Der Kaiser verlor Macht. Das Kaiserreich wurde eine parlamentarische Monarchie – für wenige Wochen.",
        "aliase": ["Oktoberreformen"],
    },
    "max-von-baden": {
        "titel": "Prinz Max von Baden", "bild": None,
        "text": "Der letzte Reichskanzler des Kaiserreichs (Oktober bis November 1918). Er bat die USA um Waffenstillstand. Am 9. November 1918 verkündete er die Abdankung des Kaisers und übergab die Regierung an Friedrich Ebert.",
        "aliase": ["Max von Baden"],
    },
    "matrosenaufstand": {
        "titel": "Der Matrosenaufstand in Kiel", "bild": "kriegsende-3",
        "text": "Ende Oktober 1918 sollte die Flotte zu einer letzten Schlacht auslaufen. Die Matrosen weigerten sich. Am 3./4. November übernahmen Arbeiter- und Soldatenräte die Stadt Kiel. Von dort breitete sich die Revolution aus.",
        "aliase": ["Matrosenaufstand in Kiel", "Matrosenaufstand"],
    },
    "novemberrevolution": {
        "titel": "Die Novemberrevolution", "bild": "kriegsende-3",
        "text": "Im November 1918 stürzten Matrosen, Soldaten und Arbeiter die Monarchie. In vielen Städten bildeten sich Räte. Am 9. November 1918 wurde in Berlin die Republik ausgerufen. Der Kaiser floh in die Niederlande.",
        "aliase": ["Novemberrevolution"],
    },
    "scheidemann": {
        "titel": "Philipp Scheidemann", "bild": "glossar-republik",
        "text": "SPD-Politiker. Am 9. November 1918 rief er von einem Fenster des Reichstags die Republik aus. 1919 wurde er der erste Ministerpräsident der Weimarer Republik.",
        "aliase": ["Philipp Scheidemann", "Scheidemann"],
    },
    "ebert": {
        "titel": "Friedrich Ebert", "bild": "glossar-republik",
        "text": "Vorsitzender der SPD. Ab dem 9. November 1918 führte er die Regierung. 1919 wurde er der erste Reichspräsident der Weimarer Republik.",
        "aliase": ["Friedrich Ebert", "Ebert"],
    },
    "compiegne": {
        "titel": "Der Waffenstillstand von Compiègne", "bild": "kriegsende-4",
        "text": "Am 11. November 1918 um 11 Uhr traten die Waffen still. Unterschrieben wurde in einem Eisenbahnwagen im Wald von Compiègne bei Paris. Für Deutschland unterschrieb der Politiker Matthias Erzberger.",
        "aliase": ["Compiègne", "Compiegne", "Waffenstillstand von Compiègne"],
    },
    "dolchstosslegende": {
        "titel": "Die Dolchstoßlegende", "bild": "kriegsende-4",
        "text": "Eine Lüge: Das Heer sei unbesiegt gewesen und von der Heimat „von hinten erdolcht“ worden. In Wahrheit hatten die Generäle selbst den Waffenstillstand verlangt. Rechte Gruppen nutzten die Lüge gegen die Republik.",
        "aliase": ["Dolchstoßlegende", "Dolchstosslegende"],
    },
    "spanische-grippe": {
        "titel": "Die Spanische Grippe", "bild": "glossar-grippe",
        "text": "Eine weltweite Grippewelle von 1918 bis 1920. Soldaten trugen das Virus um die ganze Welt. Sie forderte viele Millionen Tote – mehr als der Krieg selbst.",
        "aliase": ["Spanische Grippe"],
    },
    "artikel-231": {
        "titel": "Artikel 231 – der Kriegsschuldartikel", "bild": "folgen-2",
        "text": "Der Artikel im Versailler Vertrag, in dem Deutschland und seine Verbündeten die Schuld am Krieg anerkennen mussten. Er war die Grundlage für die Reparationen. Viele Deutsche empfanden ihn als Beleidigung.",
        "aliase": ["Artikel 231"],
    },
    "reparationen": {
        "titel": "Reparationen", "bild": "folgen-2",
        "text": "Zahlungen für die Kriegsschäden an die Sieger. 1921 wurde die Summe auf 132 Milliarden Goldmark festgelegt. Bezahlt wurde in Geld und Waren, zum Beispiel Kohle. Der Streit darüber führte 1923 zur Besetzung des Ruhrgebiets.",
        "aliase": ["Reparationen"],
    },
    "gebietsverluste": {
        "titel": "Die Gebietsverluste Deutschlands", "bild": "folgen-3",
        "text": "Rund 13 Prozent des Gebiets: Elsass-Lothringen an Frankreich, Posen und Westpreußen an Polen, Nordschleswig an Dänemark, Eupen-Malmedy an Belgien. Danzig, das Memelland und das Saargebiet kamen unter fremde Verwaltung. Alle Kolonien gingen verloren.",
        "aliase": ["13 Prozent seines Gebiets", "Gebietsverluste"],
    },
    "heer-100000": {
        "titel": "Das Heer von 100.000 Mann", "bild": "folgen-2",
        "text": "Deutschland durfte nur noch 100.000 Berufssoldaten haben. Verboten waren Wehrpflicht, Panzer, Luftwaffe und U-Boote. So sollte Deutschland keinen neuen Krieg beginnen können.",
        "aliase": ["100.000 Mann"],
    },
    "weimarer-republik": {
        "titel": "Die Weimarer Republik", "bild": "glossar-weimar",
        "text": "Die erste Demokratie in Deutschland, von 1919 bis 1933. Die Verfassung wurde in der Stadt Weimar beschlossen. Alle Männer und Frauen ab 20 durften wählen. Versailles, Krisen und ihre Gegner machten ihr das Leben schwer.",
        "aliase": ["Weimarer Republik"],
    },
    "neue-staaten": {
        "titel": "Neue Staaten nach 1918", "bild": "folgen-3",
        "text": "Aus den zerfallenen Reichen entstanden neue Staaten: Polen, die Tschechoslowakei, Jugoslawien, Estland, Lettland, Litauen und Finnland. In vielen lebten große Minderheiten – ein Grund für neue Konflikte.",
        "aliase": ["Polen, die Tschechoslowakei, Jugoslawien", "neue Staaten"],
    },
    "voelkerbund": {
        "titel": "Der Völkerbund", "bild": "folgen-3",
        "text": "Gegründet 1920 in Genf. Ziel: Streit zwischen Staaten friedlich lösen. Die USA traten nicht bei, Deutschland erst 1926. Der Völkerbund konnte den Zweiten Weltkrieg nicht verhindern.",
        "aliase": ["Völkerbund"],
    },
    "frauenwahlrecht": {
        "titel": "Das Frauenwahlrecht", "bild": "folgen-4",
        "text": "Am 12. November 1918 beschloss die neue Regierung das Wahlrecht für Frauen. Am 19. Januar 1919 durften Frauen zum ersten Mal wählen und gewählt werden. 37 Frauen zogen in die Nationalversammlung ein.",
        "aliase": ["Wahlrecht", "Frauenwahlrecht"],
    },
    "urkatastrophe": {
        "titel": "„Urkatastrophe des 20. Jahrhunderts“", "bild": "folgen-4",
        "text": "So nannte der amerikanische Historiker George F. Kennan den Ersten Weltkrieg (1979). Gemeint ist: Aus diesem Krieg wuchsen die großen Katastrophen des Jahrhunderts – Faschismus, Nationalsozialismus, Zweiter Weltkrieg.",
        "aliase": ["Urkatastrophe des 20. Jahrhunderts", "Urkatastrophe"],
    },
}

ALIASE = {normalisieren(alias): key for key, eintrag in GLOSSAR.items() for alias in eintrag["aliase"] + [eintrag["titel"]]}


def glossar_fuer_client() -> dict:
    return {
        "eintraege": {
            key: {"titel": e["titel"], "text": e["text"], "bild": BILD.format(e["bild"]) if e.get("bild") else None}
            for key, e in GLOSSAR.items()
        },
        "aliase": ALIASE,
    }


def eintrag_fuer(begriff: str):
    key = ALIASE.get(normalisieren(begriff))
    return GLOSSAR.get(key) if key else None
