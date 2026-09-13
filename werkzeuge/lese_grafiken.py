"""Erzeugt die schematischen SVG-Grafiken für Lesestrecken und Glossar.

Aufruf:  python werkzeuge/lese_grafiken.py
Ausgabe: static/img/lese/*.svg  (400 × 240, GSM-Farben, ohne externe Schriften/Bilder)

Die Grafiken sind bewusst einfache Schaubilder: Kästen, Pfeile, Symbole, kurze Beschriftungen.
Sie sollen den Text bildlich stützen, nicht dekorieren. Jede Datei lässt sich später durch
eine echte Abbildung gleichen Namens ersetzen.
"""

import os
from html import escape

ZIEL = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "static", "img", "lese")
BLAU, DUNKEL, ORANGE, MAGENTA, ROT, GRUEN, GRAU, HELL, TEXT = "#006AB3", "#004b80", "#F7B800", "#AD007C", "#dc2626", "#16a34a", "#6b7280", "#eef5fb", "#1e293b"
FONT = "font-family='Lato, Arial, sans-serif'"


def svg(titel, *teile):
    body = "\n".join(teile)
    return (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 400 240' role='img' aria-label='{escape(titel)}' {FONT}>\n"
            f"<title>{escape(titel)}</title>\n<rect width='400' height='240' rx='14' fill='{HELL}'/>\n{body}\n</svg>\n")


def t(x, y, text, size=13, weight=400, fill=TEXT, anchor="middle"):
    return f"<text x='{x}' y='{y}' font-size='{size}' font-weight='{weight}' fill='{fill}' text-anchor='{anchor}'>{escape(text)}</text>"


def box(x, y, w, h, text="", fill="#fff", stroke=BLAU, size=13, weight=700, tfill=TEXT, rx=10, sw=2):
    lines = text.split("\n") if text else []
    out = f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='{rx}' fill='{fill}' stroke='{stroke}' stroke-width='{sw}'/>"
    if lines:
        start = y + h / 2 - (len(lines) - 1) * (size + 3) / 2 + size / 3
        for i, line in enumerate(lines):
            out += t(x + w / 2, start + i * (size + 3), line, size, weight, tfill)
    return out


def arrow(x1, y1, x2, y2, color=DUNKEL, w=3, dash=""):
    d = f" stroke-dasharray='{dash}'" if dash else ""
    return (f"<defs><marker id='m{color[1:]}' markerWidth='8' markerHeight='8' refX='6' refY='4' orient='auto'><path d='M0,0 L8,4 L0,8 z' fill='{color}'/></marker></defs>"
            f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{color}' stroke-width='{w}' marker-end='url(#m{color[1:]})'{d}/>")


def curve(d, color=DUNKEL, w=3, dash=""):
    dd = f" stroke-dasharray='{dash}'" if dash else ""
    return (f"<defs><marker id='c{color[1:]}' markerWidth='8' markerHeight='8' refX='6' refY='4' orient='auto'><path d='M0,0 L8,4 L0,8 z' fill='{color}'/></marker></defs>"
            f"<path d='{d}' fill='none' stroke='{color}' stroke-width='{w}' marker-end='url(#c{color[1:]})'{dd}/>")


def person(x, y, color=DUNKEL, s=1.0):
    return (f"<circle cx='{x}' cy='{y}' r='{6 * s}' fill='{color}'/>"
            f"<path d='M{x - 8 * s},{y + 24 * s} v-{10 * s} a{8 * s},{8 * s} 0 0 1 {16 * s},0 v{10 * s} z' fill='{color}'/>")


def ship(x, y, color=DUNKEL, w=40):
    return (f"<path d='M{x},{y} h{w} l-6,10 h-{w - 12} z' fill='{color}'/>"
            f"<rect x='{x + w * 0.35}' y='{y - 9}' width='{w * 0.3}' height='9' fill='{color}'/>"
            f"<rect x='{x + w * 0.47}' y='{y - 16}' width='4' height='8' fill='{color}'/>")


def flag(x, y, color, label="", w=34, h=22):
    out = f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='3' fill='{color}' stroke='#fff' stroke-width='1.5'/>"
    if label:
        out += t(x + w / 2, y + h / 2 + 5, label, 12, 900, "#fff")
    return out


def barrel(x, y, w=70, h=80, label="Pulverfass"):
    return (f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='12' fill='#8b5e3c' stroke='#5b3b22' stroke-width='3'/>"
            f"<line x1='{x}' y1='{y + h * 0.3}' x2='{x + w}' y2='{y + h * 0.3}' stroke='#5b3b22' stroke-width='3'/>"
            f"<line x1='{x}' y1='{y + h * 0.7}' x2='{x + w}' y2='{y + h * 0.7}' stroke='#5b3b22' stroke-width='3'/>"
            + t(x + w / 2, y + h + 16, label, 12, 700))


def spark(x, y):
    return (f"<path d='M{x},{y - 18} l4,12 l12,-6 l-8,10 l12,6 l-13,1 l2,13 l-9,-10 l-9,10 l2,-13 l-13,-1 l12,-6 l-8,-10 l12,6 z' fill='{ORANGE}' stroke='{ROT}' stroke-width='2'/>")


def kreuz(x, y, s=16, color=ROT):
    return f"<path d='M{x - s},{y - s} L{x + s},{y + s} M{x + s},{y - s} L{x - s},{y + s}' stroke='{color}' stroke-width='5' stroke-linecap='round'/>"


def krone(x, y, color=ORANGE):
    return f"<path d='M{x - 16},{y + 10} l4,-20 l8,10 l4,-16 l4,16 l8,-10 l4,20 z' fill='{color}' stroke='{DUNKEL}' stroke-width='2'/>"


# ─── Lesestrecke Ursachen ─────────────────────────────────────────────────
def ursachen_1():
    return svg("Wettlauf um Kolonien",
        box(16, 60, 120, 90, "Großmächte\nEuropas", "#fff", BLAU),
        flag(28, 152, BLAU, "GB", 28, 18), flag(62, 152, ROT, "F", 28, 18), flag(96, 152, DUNKEL, "D", 28, 18),
        arrow(140, 90, 232, 60), arrow(140, 110, 232, 150),
        t(186, 70, "Wettlauf", 12, 700, MAGENTA), t(186, 140, "Wettlauf", 12, 700, MAGENTA),
        box(240, 30, 140, 64, "Afrika", "#f1ead9", GRAU), box(240, 120, 140, 64, "Asien", "#f1ead9", GRAU),
        f"<rect x='250' y='62' width='26' height='20' fill='#8b5e3c' stroke='#5b3b22'/>", t(304, 77, "Rohstoffe", 11, 700),
        f"<circle cx='262' cy='160' r='9' fill='{ORANGE}' stroke='#b8860b'/><circle cx='276' cy='166' r='9' fill='{ORANGE}' stroke='#b8860b'/>", t(318, 170, "Märkte", 11, 700),
        f"<circle cx='40' cy='210' r='14' fill='#fff' stroke='{DUNKEL}' stroke-width='2'/><line x1='40' y1='210' x2='40' y2='200' stroke='{DUNKEL}' stroke-width='2'/><line x1='40' y1='210' x2='48' y2='214' stroke='{DUNKEL}' stroke-width='2'/>",
        t(64, 214, "Deutschland: erst seit 1871 – kommt zu spät", 12, 700, ROT, "start"))


def ursachen_2():
    return svg("Nationalismus: Elsass-Lothringen und Serbien",
        f"<path d='M20,58 h120 v40 h-80 l-12,14 l-2,-14 h-26 z' fill='#fff' stroke='{MAGENTA}' stroke-width='2'/>",
        t(80, 82, "„Wir sind die Besten!“", 12, 700, MAGENTA),
        t(80, 130, "Nationalismus", 12, 900, TEXT),
        box(160, 40, 70, 60, "Frank-\nreich", "#dbe9f7", BLAU, 12), box(232, 40, 56, 60, "Elsass-\nLothr.", "#fde7f3", MAGENTA, 11), box(290, 40, 90, 60, "Deutsches\nReich", "#e5e7eb", GRAU, 12),
        arrow(258, 118, 258, 104, ROT), t(258, 134, "„zurück!“ (verloren 1871)", 11, 700, ROT),
        box(160, 150, 90, 56, "Serbien", "#dbe9f7", BLAU, 12), box(290, 140, 96, 76, "Österreich-\nUngarn\n(viele Völker)", "#e5e7eb", GRAU, 11),
        arrow(252, 178, 286, 178, ROT),
        t(220, 230, "Serbien will alle Südslawen in einem Staat vereinen", 10, 700, ROT))


def ursachen_3():
    ships_d = "".join(ship(20 + i * 48, 86, DUNKEL, 38) for i in range(3))
    ships_gb = "".join(ship(20 + i * 48, 136, BLAU, 38) for i in range(4))
    return svg("Wettrüsten und Schlieffen-Plan",
        t(100, 40, "Flottenwettrüsten", 13, 900), ships_d, t(178, 92, "D", 12, 900, DUNKEL, "start"), ships_gb, t(226, 142, "GB", 12, 900, BLAU, "start"),
        t(100, 176, "Beide bauen immer mehr Schiffe", 11, 400, GRAU),
        t(300, 40, "Schlieffen-Plan", 13, 900),
        box(232, 60, 56, 50, "Frank-\nreich", "#dbe9f7", BLAU, 11), box(290, 60, 40, 50, "Bel-\ngien", "#f1ead9", GRAU, 10), box(332, 60, 56, 50, "Deutsch-\nland", "#e5e7eb", GRAU, 10),
        box(332, 150, 56, 50, "Russ-\nland", "#dbe9f7", BLAU, 11),
        curve("M360,112 C360,140 310,150 262,112", ROT, 3), t(300, 150, "1. schnell", 11, 900, ROT),
        arrow(360, 116, 360, 146, DUNKEL, 3, "5 4"), t(352, 134, "2. danach", 10, 700, DUNKEL, "end"),
        t(310, 222, "Krieg an zwei Fronten vermeiden", 11, 400, GRAU))


def ursachen_4():
    return svg("Zwei Blöcke und das Pulverfass Balkan",
        box(14, 30, 160, 92, "", "#fde7f3", MAGENTA), t(94, 50, "Dreibund (1882)", 13, 900, MAGENTA),
        flag(26, 62, DUNKEL, "D"), flag(70, 62, "#7c2d12", "Ö-U"), flag(114, 62, GRUEN, "I"), t(94, 108, "Deutschland · Österreich-Ungarn · Italien", 9, 400, GRAU),
        box(226, 30, 160, 92, "", "#dbe9f7", BLAU), t(306, 50, "Triple Entente (1907)", 13, 900, BLAU),
        flag(238, 62, ROT, "F"), flag(282, 62, "#0f766e", "R"), flag(326, 62, BLAU, "GB"), t(306, 108, "Frankreich · Russland · Großbritannien", 9, 400, GRAU),
        f"<path d='M186,60 l14,20 l-10,4 l16,22' fill='none' stroke='{ROT}' stroke-width='4' stroke-linecap='round'/>",
        t(200, 140, "Ein Streit zwischen zwei Staaten zieht alle hinein.", 11, 700),
        barrel(40, 150, 60, 70, "Balkan = Pulverfass"), spark(70, 140),
        box(130, 156, 250, 70, "Osmanisches Reich verliert Gebiete.\nÖsterreich-Ungarn und Russland\nstreiten um Einfluss.", "#fff", GRAU, 11, 400))


# ─── Lesestrecke Auslöser ─────────────────────────────────────────────────
def ausloeser_1():
    return svg("Das Attentat von Sarajevo",
        t(200, 30, "Sarajevo, 28. Juni 1914", 15, 900, DUNKEL),
        f"<rect x='150' y='110' width='150' height='44' rx='10' fill='{DUNKEL}'/><rect x='180' y='90' width='80' height='26' rx='8' fill='{DUNKEL}'/>",
        f"<circle cx='180' cy='158' r='12' fill='#111'/><circle cx='270' cy='158' r='12' fill='#111'/>",
        person(205, 96, "#fff", .8), person(238, 96, "#fff", .8),
        t(225, 184, "Franz Ferdinand + Sophie", 12, 700), t(225, 200, "im offenen Auto", 11, 400, GRAU),
        person(60, 110, ROT, 1.1), t(60, 158, "Gavrilo Princip", 12, 700, ROT), t(60, 172, "serbischer Nationalist", 10, 400, GRAU),
        arrow(80, 118, 146, 124, ROT, 3, "6 4"),
        box(300, 60, 90, 44, "Schuld?\nSerbien!", "#fde7f3", MAGENTA, 12), arrow(300, 96, 270, 106, MAGENTA, 2, "4 3"),
        t(200, 226, "Der Funke für die Julikrise", 11, 400, GRAU))


def ausloeser_2():
    return svg("Blankoscheck und Ultimatum",
        f"<rect x='16' y='40' width='180' height='96' rx='8' fill='#fff' stroke='{DUNKEL}' stroke-width='2'/>",
        t(106, 62, "SCHECK", 12, 900, GRAU), t(30, 86, "Betrag: __________", 12, 700, TEXT, "start"), t(30, 108, "Von: Berlin   An: Wien", 12, 400, TEXT, "start"), t(30, 126, "Unterschrift: Wilhelm II.", 11, 400, GRAU, "start"),
        t(106, 156, "„Blankoscheck“ (5./6. Juli)", 12, 900, MAGENTA), t(106, 172, "= volle Unterstützung, egal was Wien tut", 10, 400, GRAU),
        f"<rect x='232' y='44' width='150' height='70' rx='8' fill='#fff' stroke='{ROT}' stroke-width='2'/><path d='M232,44 l75,40 l75,-40' fill='none' stroke='{ROT}' stroke-width='2'/>",
        t(307, 100, "Ultimatum an Serbien", 11, 900, ROT),
        f"<circle cx='262' cy='160' r='22' fill='#fff' stroke='{DUNKEL}' stroke-width='3'/><line x1='262' y1='160' x2='262' y2='144' stroke='{DUNKEL}' stroke-width='3'/><line x1='262' y1='160' x2='274' y2='166' stroke='{DUNKEL}' stroke-width='3'/>",
        t(262, 200, "48 Stunden", 12, 900), t(340, 150, "23. Juli", 12, 700, TEXT), t(340, 168, "Serbien sagt\nfast alles zu", 10, 400, GRAU).replace("\n", "</text><text x='340' y='182' font-size='10' fill='#6b7280' text-anchor='middle'>"),
        t(340, 214, "28. Juli: Krieg!", 13, 900, ROT))


def ausloeser_3():
    steine = [("Ö-U", "28.7."), ("Russland", "30.7."), ("Deutschl.", "1.8."), ("Frankr.", "3.8."), ("Belgien", "4.8."), ("GB", "4.8.")]
    out = []
    for i, (name, datum) in enumerate(steine):
        x = 30 + i * 60
        kipp = min(i * 9, 40)
        out.append(f"<g transform='rotate({-kipp} {x + 18} 170)'><rect x='{x}' y='60' width='36' height='110' rx='6' fill='{'#fde7f3' if i == 0 else '#fff'}' stroke='{DUNKEL}' stroke-width='2'/>"
                   f"<text x='{x + 18}' y='120' font-size='10' font-weight='700' text-anchor='middle' transform='rotate(-90 {x + 18} 120)'>{escape(name)}</text></g>")
        out.append(t(x + 18, 200, datum, 11, 700, ROT))
    return svg("Die Julikrise als Kettenreaktion", t(200, 32, "Jeder Schritt löst den nächsten aus", 14, 900, DUNKEL), *out,
               arrow(12, 96, 40, 100, MAGENTA), t(200, 228, "Attentat → Kriegserklärung → Mobilmachung → Krieg in ganz Europa", 10, 400, GRAU))


def ausloeser_4():
    return svg("Funke und Pulverfass",
        barrel(60, 60, 110, 120, ""), t(115, 200, "PULVERFASS = Ursachen", 12, 900, DUNKEL),
        t(115, 94, "Imperialismus", 10, 700, "#fff"), t(115, 112, "Nationalismus", 10, 700, "#fff"), t(115, 130, "Militarismus", 10, 700, "#fff"), t(115, 148, "Bündnisse", 10, 700, "#fff"),
        spark(230, 80), arrow(232, 96, 180, 120, ROT, 3, "6 4"),
        t(300, 60, "FUNKE = Auslöser", 13, 900, ROT), t(300, 80, "Attentat von Sarajevo", 12, 700), t(300, 96, "28. Juni 1914", 11, 400, GRAU),
        box(210, 130, 176, 80, "Ohne Pulverfass\nhätte der Funke\nnichts entzündet.", "#fff", GRAU, 12, 400))


# ─── Lesestrecke Verlauf ──────────────────────────────────────────────────
def verlauf_1():
    return svg("Marneschlacht und Stellungskrieg",
        box(300, 30, 84, 50, "Deutsches\nReich", "#e5e7eb", GRAU, 11), box(200, 30, 56, 50, "Belgien", "#f1ead9", GRAU, 10), box(30, 30, 110, 50, "Frankreich", "#dbe9f7", BLAU, 12),
        f"<circle cx='70' cy='70' r='5' fill='{ROT}'/>", t(70, 92, "Paris", 11, 700),
        curve("M300,56 C240,40 180,50 130,66", ROT, 4), kreuz(122, 66, 10),
        t(150, 106, "gestoppt: Marne, Sept. 1914", 11, 900, ROT),
        t(200, 128, "Danach: Stellungskrieg", 14, 900, DUNKEL),
        f"<path d='M20,170 l20,-14 l20,14 l20,-14 l20,14 l20,-14 l20,14 l20,-14 l20,14 l20,-14 l20,14 l20,-14 l20,14 l20,-14 l20,14 l20,-14 l20,14 l20,-14 l20,14' fill='none' stroke='#8b5e3c' stroke-width='4'/>",
        f"<path d='M20,196 l20,-14 l20,14 l20,-14 l20,14 l20,-14 l20,14 l20,-14 l20,14 l20,-14 l20,14 l20,-14 l20,14 l20,-14 l20,14 l20,-14 l20,14 l20,-14 l20,14' fill='none' stroke='#8b5e3c' stroke-width='4'/>",
        t(20, 220, "Nordsee", 11, 700, GRAU, "start"), t(380, 220, "Schweiz", 11, 700, GRAU, "end"), t(200, 187, "Niemandsland", 10, 700, ROT))


def verlauf_2():
    return svg("Materialschlacht 1916",
        f"<rect x='0' y='150' width='400' height='90' fill='#8b5e3c'/>",
        f"<rect x='40' y='150' width='60' height='40' fill='#5b3b22'/><rect x='300' y='150' width='60' height='40' fill='#5b3b22'/>",
        person(70, 160, "#fff", .7), person(330, 160, "#fff", .7),
        t(70, 214, "Graben", 11, 700, "#fff"), t(330, 214, "Graben", 11, 700, "#fff"), t(200, 214, "Niemandsland", 11, 700, "#fff"),
        curve("M100,150 C160,60 240,60 296,148", ROT, 3, "6 4"), curve("M300,150 C240,80 160,80 104,148", ROT, 3, "6 4"),
        f"<path d='M150,120 h8 v10 h-8 z M190,105 h8 v10 h-8 z M240,120 h8 v10 h-8 z' fill='{DUNKEL}'/>",
        f"<path d='M120,150 l30,-8 l0,8 z' fill='{DUNKEL}'/><path d='M280,150 l-30,-8 l0,8 z' fill='{DUNKEL}'/>",
        t(200, 30, "Granaten, Maschinengewehre, Stacheldraht", 13, 900, DUNKEL),
        box(20, 44, 160, 48, "Verdun 1916\n≈ 700.000 Tote + Verwundete", "#fff", ROT, 11), box(220, 44, 160, 48, "Somme 1916\n> 1 Million Verluste", "#fff", ROT, 11),
        t(200, 112, "Die Front bewegt sich fast nicht.", 12, 700, ROT))


def verlauf_3():
    return svg("1917: die Wende",
        f"<rect x='0' y='120' width='250' height='120' fill='#cfe3f2'/>",
        ship(40, 120, DUNKEL, 60), f"<path d='M110,120 l30,-12 v12 z' fill='{ROT}'/>",
        f"<path d='M60,170 h70 a10,10 0 0 1 0,20 h-70 a10,10 0 0 1 0,-20 z' fill='#374151'/><rect x='88' y='160' width='14' height='10' fill='#374151'/>",
        t(96, 210, "U-Boot versenkt Schiffe", 11, 700, DUNKEL), t(96, 224, "ab Februar 1917 ohne Warnung", 10, 400, DUNKEL),
        flag(280, 130, BLAU, "USA", 60, 36), arrow(280, 148, 236, 148, BLAU, 4), t(310, 186, "April 1917:", 12, 900, BLAU), t(310, 202, "USA treten ein", 12, 700),
        box(20, 20, 150, 70, "Russland 1917:\nRevolution", "#fff", MAGENTA, 12),
        arrow(174, 55, 220, 55, MAGENTA, 3), box(224, 26, 160, 58, "März 1918:\nFrieden von Brest-Litowsk", "#fde7f3", MAGENTA, 11),
        t(200, 106, "Russland steigt aus – die USA kommen dazu", 11, 700, GRAU))


def verlauf_4():
    return svg("Totaler Krieg: die Heimatfront",
        f"<rect x='20' y='90' width='90' height='60' fill='#9ca3af'/><rect x='30' y='60' width='14' height='30' fill='#6b7280'/><rect x='50' y='70' width='14' height='20' fill='#6b7280'/>",
        person(65, 118, "#fff", .8), t(65, 170, "Frauen arbeiten", 11, 700), t(65, 184, "in Waffenfabriken", 10, 400, GRAU),
        f"<ellipse cx='200' cy='120' rx='40' ry='16' fill='#fff' stroke='{GRAU}' stroke-width='3'/><ellipse cx='200' cy='118' rx='8' ry='6' fill='#e0b04a'/>",
        t(200, 158, "Steckrübenwinter", 11, 900, ROT), t(200, 172, "1916/17: Hunger", 10, 400, GRAU),
        ship(300, 60, BLAU, 36), ship(342, 60, BLAU, 36), t(340, 84, "Seeblockade", 11, 700, BLAU), t(340, 98, "kaum Waren nach Deutschland", 9, 400, GRAU),
        f"<rect x='300' y='120' width='80' height='56' rx='6' fill='{ORANGE}' stroke='{DUNKEL}' stroke-width='2'/>", t(340, 144, "PROPA-", 11, 900, DUNKEL), t(340, 160, "GANDA", 11, 900, DUNKEL),
        t(200, 30, "Der Krieg betrifft alle – auch zu Hause", 13, 900, DUNKEL),
        t(200, 222, "1918: Offensive scheitert, Alliierte drängen zurück", 11, 700, ROT))


# ─── Lesestrecke Kriegsende ───────────────────────────────────────────────
def kriegsende_1():
    return svg("Sommer 1918: militärisch verloren",
        f"<rect x='190' y='60' width='20' height='120' fill='{DUNKEL}'/><rect x='150' y='180' width='100' height='12' rx='4' fill='{DUNKEL}'/>",
        f"<line x1='60' y1='52' x2='340' y2='96' stroke='{DUNKEL}' stroke-width='8' stroke-linecap='round'/>",
        f"<line x1='70' y1='54' x2='70' y2='84' stroke='{GRAU}' stroke-width='2'/><line x1='330' y1='94' x2='330' y2='140' stroke='{GRAU}' stroke-width='2'/>",
        box(14, 84, 112, 44, "Deutschland:\nerschöpft, Hunger", "#fde7f3", MAGENTA, 10, 700, MAGENTA),
        box(268, 140, 124, 54, "Alliierte + USA:\n10.000 neue Soldaten\njeden Tag", "#dbe9f7", BLAU, 10, 700, DUNKEL),
        f"<rect x='90' y='200' width='220' height='34' rx='6' fill='#fff' stroke='{ROT}' stroke-width='2'/>",
        t(200, 214, "29. Sept. 1918: Die Generäle", 10, 700, ROT), t(200, 227, "verlangen einen Waffenstillstand", 10, 700, ROT),
        t(200, 30, "Die Waage kippt", 14, 900, DUNKEL))


def kriegsende_2():
    return svg("Oktoberreformen und die Verbündeten geben auf",
        f"<rect x='30' y='110' width='140' height='70' fill='#fff' stroke='{DUNKEL}' stroke-width='2'/><path d='M60,110 a40,32 0 0 1 80,0 z' fill='#fff' stroke='{DUNKEL}' stroke-width='2'/>"
        f"<rect x='45' y='130' width='12' height='50' fill='{DUNKEL}'/><rect x='75' y='130' width='12' height='50' fill='{DUNKEL}'/><rect x='105' y='130' width='12' height='50' fill='{DUNKEL}'/><rect x='135' y='130' width='12' height='50' fill='{DUNKEL}'/>",
        t(100, 200, "Reichstag bekommt Macht", 11, 900, DUNKEL), t(100, 214, "Oktober 1918: Reformen", 10, 400, GRAU),
        t(300, 40, "Verbündete geben auf:", 13, 900, ROT),
        f"<g transform='rotate(20 240 100)'>{flag(222, 84, GRUEN, 'BG')}</g>", t(240, 130, "Bulgarien", 10, 700), t(240, 142, "29. Sept.", 10, 400, GRAU),
        f"<g transform='rotate(35 310 100)'>{flag(292, 84, ROT, 'OSM')}</g>", t(310, 130, "Osman. Reich", 10, 700), t(310, 142, "30. Okt.", 10, 400, GRAU),
        f"<g transform='rotate(50 375 100)'>{flag(357, 84, '#7c2d12', 'Ö-U')}</g>", t(375, 130, "Österr.-Ung.", 10, 700), t(375, 142, "3. Nov.", 10, 400, GRAU),
        t(300, 190, "Deutschland steht allein", 12, 700, TEXT),
        t(200, 24, "Herbst 1918", 12, 400, GRAU))


def kriegsende_3():
    return svg("Matrosenaufstand und Novemberrevolution",
        f"<rect x='0' y='150' width='180' height='90' fill='#cfe3f2'/>", ship(20, 150, DUNKEL, 56), ship(90, 150, DUNKEL, 56),
        person(60, 190, "#fff", .8), person(90, 190, "#fff", .8), person(120, 190, "#fff", .8),
        f"<path d='M30,40 h70 v36 h-40 l-10,12 l-2,-12 h-18 z' fill='#fff' stroke='{ROT}' stroke-width='2'/>", t(65, 64, "„Nein!“", 13, 900, ROT),
        t(90, 110, "Kiel, 3./4. Nov. 1918", 11, 900, DUNKEL), t(90, 123, "Matrosen weigern sich", 10, 400, GRAU),
        f"<rect x='200' y='60' width='6' height='120' fill='{DUNKEL}'/><path d='M206,64 h60 l-10,14 l10,14 h-60 z' fill='{ROT}'/>",
        arrow(210, 214, 296, 214, ROT, 4), t(253, 232, "Revolution breitet sich aus", 10, 700, ROT),
        box(300, 116, 90, 50, "Berlin\n9. Nov. 1918", "#fff", DUNKEL, 11),
        t(345, 184, "Kaiser dankt ab", 10, 700), t(345, 198, "Republik ausgerufen", 10, 900, ROT),
        t(300, 40, "Arbeiter- und Soldatenräte", 12, 700, TEXT), t(300, 56, "übernehmen die Städte", 11, 400, GRAU))


def kriegsende_4():
    return svg("Waffenstillstand und Dolchstoßlegende",
        f"<rect x='20' y='70' width='150' height='60' rx='8' fill='#5b3b22' stroke='{DUNKEL}' stroke-width='2'/><rect x='30' y='80' width='30' height='24' fill='#fff'/><rect x='70' y='80' width='30' height='24' fill='#fff'/><rect x='110' y='80' width='30' height='24' fill='#fff'/>"
        f"<circle cx='50' cy='138' r='9' fill='#111'/><circle cx='140' cy='138' r='9' fill='#111'/><rect x='0' y='146' width='190' height='4' fill='{GRAU}'/>",
        t(95, 40, "Eisenbahnwagen bei Compiègne", 11, 900, DUNKEL), t(95, 56, "11. Nov. 1918, 11 Uhr: Waffenstillstand", 10, 400, TEXT),
        t(95, 176, "Die Waffen schweigen.", 11, 700, GRUEN),
        person(275, 78, DUNKEL, 1.2), f"<path d='M312,84 l-22,9' stroke='{ROT}' stroke-width='5' stroke-linecap='round'/><path d='M312,84 l8,-4 l-2,8 z' fill='{ROT}'/>",
        t(300, 148, "„Dolchstoßlegende“:", 11, 900, MAGENTA), t(300, 162, "Heimat hat das Heer verraten?", 10, 400, TEXT),
        kreuz(290, 96, 28, ROT),
        box(210, 176, 180, 54, "FALSCH! Die Generäle selbst\nhatten den Waffenstillstand\nverlangt (29. Sept.).", "#fff", ROT, 10, 700, ROT))


# ─── Lesestrecke Folgen ───────────────────────────────────────────────────
def folgen_1():
    soldaten = "".join(person(30 + i * 34, 70, DUNKEL, .9) for i in range(10))
    zivil = "".join(person(30 + i * 34, 140, GRAU, .9) for i in range(7))
    return svg("Die Toten des Krieges",
        t(200, 30, "Eine Figur = 1 Million Menschen", 12, 700, GRAU),
        soldaten, t(200, 118, "≈ 9–10 Millionen Soldaten", 13, 900, DUNKEL),
        zivil, t(200, 188, "≈ 6–7 Millionen Zivilisten", 13, 900, GRAU),
        f"<circle cx='350' cy='138' r='14' fill='{MAGENTA}'/><circle cx='350' cy='138' r='6' fill='#fff'/>", t(350, 164, "Spanische Grippe", 10, 700, MAGENTA), t(350, 176, "1918–20: Millionen Tote", 9, 400, GRAU),
        t(200, 222, "Dazu Millionen Verletzte und Traumatisierte", 11, 400, TEXT))


def folgen_2():
    return svg("Der Versailler Vertrag 1919",
        f"<rect x='30' y='30' width='200' height='190' rx='6' fill='#fff' stroke='{DUNKEL}' stroke-width='2'/>",
        t(130, 56, "VERTRAG VON VERSAILLES", 11, 900, DUNKEL), t(130, 72, "28. Juni 1919", 10, 400, GRAU),
        t(44, 100, "Art. 231: Deutschland ist schuld", 11, 700, ROT, "start"),
        t(44, 124, "Reparationen: Geld für Schäden", 11, 700, TEXT, "start"),
        t(44, 148, "−13 % Gebiet, alle Kolonien", 11, 700, TEXT, "start"),
        t(44, 172, "Heer: nur noch 100.000 Mann", 11, 700, TEXT, "start"),
        f"<circle cx='196' cy='196' r='14' fill='{ROT}'/><text x='196' y='201' font-size='10' font-weight='900' fill='#fff' text-anchor='middle'>SIEGEL</text>",
        f"<rect x='270' y='120' width='60' height='10' fill='{DUNKEL}'/><rect x='274' y='130' width='6' height='36' fill='{DUNKEL}'/><rect x='320' y='130' width='6' height='36' fill='{DUNKEL}'/><rect x='274' y='86' width='6' height='34' fill='{DUNKEL}'/>",
        kreuz(300, 110, 18),
        t(300, 190, "Deutschland darf", 11, 700), t(300, 204, "nicht mitverhandeln", 11, 700), t(300, 222, "→ „Diktat“", 12, 900, ROT))


def folgen_3():
    kronen = "".join(krone(50 + i * 60, 60) + kreuz(50 + i * 60, 56, 20, ROT) for i in range(4))
    return svg("Eine neue Landkarte",
        t(140, 24, "Vier Reiche zerfallen", 13, 900, DUNKEL), kronen,
        t(50, 96, "Deutsches Reich", 8, 700), t(110, 96, "Österr.-Ung.", 8, 700), t(170, 96, "Russland", 8, 700), t(230, 96, "Osman. Reich", 8, 700),
        arrow(140, 106, 140, 122, DUNKEL),
        box(16, 130, 74, 34, "Polen", "#dcfce7", GRUEN, 11), box(96, 130, 100, 34, "Tschechoslow.", "#dcfce7", GRUEN, 10), box(202, 130, 84, 34, "Jugoslawien", "#dcfce7", GRUEN, 10),
        box(16, 170, 120, 34, "Baltische Staaten", "#dcfce7", GRUEN, 10), box(142, 170, 70, 34, "Finnland", "#dcfce7", GRUEN, 10),
        t(142, 224, "Neue Staaten entstehen", 11, 700, GRUEN),
        f"<circle cx='340' cy='150' r='44' fill='#fff' stroke='{BLAU}' stroke-width='3'/>", t(340, 146, "Völker-", 12, 900, BLAU), t(340, 162, "bund", 12, 900, BLAU), t(340, 210, "1920 · USA nicht dabei", 9, 700, GRAU))


def folgen_4():
    stationen = [("Krieg", "1914–18"), ("Versailles", "1919"), ("Krise", "1923"), ("NS-Zeit", "ab 1933"), ("2. Welt-", "krieg 1939")]
    out = []
    for i, (a, b) in enumerate(stationen):
        x = 14 + i * 76
        out.append(box(x, 50, 66, 50, f"{a}\n{b}", "#fff" if i < 4 else "#fee2e2", DUNKEL if i < 4 else ROT, 10))
        if i < 4:
            out.append(arrow(x + 66, 75, x + 76, 75, ROT, 3))
    return svg("Langfristige Folgen",
        t(200, 30, "Die „Urkatastrophe“ – eine Kette von Folgen", 12, 900, DUNKEL), *out,
        person(60, 150, MAGENTA, 1.2), f"<rect x='84' y='150' width='40' height='28' fill='#fff' stroke='{DUNKEL}' stroke-width='2'/><path d='M92,164 l8,8 l16,-14' fill='none' stroke='{GRUEN}' stroke-width='3'/>",
        t(96, 208, "Frauenwahlrecht 1918/19", 11, 900, MAGENTA), t(96, 222, "Frauen dürfen wählen", 10, 400, GRAU),
        box(190, 130, 196, 80, "Schulden, Inflation und\nRachegedanken vergiften\ndie junge Republik.", "#fff", GRAU, 11, 400))


# ─── Glossar (zusätzliche Bilder) ────────────────────────────────────────
def glossar_marokkokrise():
    return svg("Marokkokrisen 1905 und 1911",
        f"<path d='M120,60 q60,-30 140,0 q40,60 20,120 q-80,40 -160,0 q-30,-60 0,-120 z' fill='#f1ead9' stroke='{GRAU}' stroke-width='2'/>",
        t(200, 130, "Marokko", 16, 900, DUNKEL), t(200, 150, "(Nordafrika)", 11, 400, GRAU),
        flag(40, 40, ROT, "F"), arrow(80, 52, 130, 90, ROT, 3), t(58, 80, "will Marokko", 10, 700, ROT),
        flag(320, 40, DUNKEL, "D"), arrow(320, 52, 268, 90, DUNKEL, 3), t(340, 80, "mischt sich ein", 10, 700, DUNKEL),
        f"<path d='M186,88 l10,16 l-8,3 l12,18' fill='none' stroke='{ROT}' stroke-width='4' stroke-linecap='round'/>",
        t(200, 205, "1905 und 1911: fast Krieg zwischen Frankreich und Deutschland", 10, 700, TEXT),
        t(200, 222, "Deutschland geht leer aus – und fühlt sich ausgegrenzt", 10, 400, GRAU))


def glossar_schlieffen():
    return svg("Der Schlieffen-Plan",
        box(40, 60, 90, 70, "Frankreich", "#dbe9f7", BLAU, 12), box(140, 60, 60, 70, "Belgien\n(neutral)", "#f1ead9", GRAU, 10), box(210, 60, 90, 70, "Deutsches\nReich", "#e5e7eb", GRAU, 11), box(310, 60, 80, 70, "Russland", "#dbe9f7", BLAU, 12),
        f"<circle cx='70' cy='110' r='5' fill='{ROT}'/>", t(70, 124, "Paris", 9, 700, "#fff"),
        curve("M255,50 C230,10 150,10 90,52", ROT, 4), t(170, 14, "1. Durch Belgien nach Paris – in 6 Wochen", 10, 900, ROT),
        arrow(300, 100, 306, 100, DUNKEL, 4, "6 4"), t(300, 148, "2. Dann alle Truppen nach Osten", 10, 900, DUNKEL), t(300, 161, "gegen Russland", 10, 900, DUNKEL),
        box(40, 170, 350, 54, "Idee: Russland braucht lange, um mobil zu machen.\nWirklichkeit: Der Plan scheitert im September 1914 an der Marne.", "#fff", GRAU, 10, 400))


def glossar_steckruebe():
    return svg("Steckrübenwinter 1916/17",
        f"<ellipse cx='200' cy='130' rx='90' ry='34' fill='#fff' stroke='{GRAU}' stroke-width='4'/>",
        f"<path d='M180,126 q20,-40 44,0 q-10,14 -44,0 z' fill='#e0b04a' stroke='#8b5e3c' stroke-width='2'/><path d='M202,100 l4,-16 l6,4' fill='none' stroke='{GRUEN}' stroke-width='3'/>",
        t(200, 190, "Nur Steckrüben – kein Brot, keine Kartoffeln", 12, 900, DUNKEL),
        t(200, 210, "Die britische Seeblockade lässt kaum Lebensmittel nach Deutschland.", 10, 400, TEXT),
        t(200, 226, "Hunderttausende sterben an Hunger und Krankheit.", 10, 400, GRAU),
        t(200, 40, "Winter 1916/17", 14, 900, ROT))


def glossar_grippe():
    return svg("Spanische Grippe 1918–1920",
        f"<circle cx='120' cy='120' r='40' fill='{MAGENTA}'/>" + "".join(f"<line x1='120' y1='120' x2='{120 + 56 * dx}' y2='{120 + 56 * dy}' stroke='{MAGENTA}' stroke-width='6' stroke-linecap='round'/>" for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (.7, .7), (-.7, .7), (.7, -.7), (-.7, -.7)]) + f"<circle cx='120' cy='120' r='16' fill='#fff'/>",
        t(280, 80, "Weltweite Grippewelle", 13, 900, MAGENTA), t(280, 100, "1918 bis 1920", 12, 700),
        t(280, 130, "Viele Millionen Tote –", 11, 400, TEXT), t(280, 146, "mehr als im Krieg selbst.", 11, 400, TEXT),
        t(280, 176, "Soldaten trugen das Virus", 10, 400, GRAU), t(280, 190, "um die ganze Welt.", 10, 400, GRAU))


def glossar_weimar():
    return svg("Die Weimarer Republik",
        f"<rect x='40' y='50' width='150' height='34' fill='#111'/><rect x='40' y='84' width='150' height='34' fill='{ROT}'/><rect x='40' y='118' width='150' height='34' fill='{ORANGE}'/>",
        t(115, 176, "Schwarz-Rot-Gold", 11, 700), t(115, 190, "Flagge der Republik", 10, 400, GRAU),
        box(220, 50, 160, 40, "1919–1933", "#fff", DUNKEL, 13),
        t(300, 118, "Erste Demokratie", 12, 900, DUNKEL), t(300, 134, "in Deutschland", 12, 900, DUNKEL),
        t(300, 160, "Alle Männer und Frauen", 10, 400, TEXT), t(300, 174, "ab 20 dürfen wählen.", 10, 400, TEXT),
        t(300, 200, "Belastet durch Versailles,", 10, 400, GRAU), t(300, 214, "Krisen und alte Eliten.", 10, 400, GRAU))


def glossar_ohl():
    return svg("Die Oberste Heeresleitung",
        person(120, 80, DUNKEL, 1.6), person(200, 80, DUNKEL, 1.6), t(120, 140, "Hindenburg", 12, 900), t(200, 140, "Ludendorff", 12, 900),
        t(160, 160, "Die beiden Generäle führen das Heer", 11, 400, TEXT), t(160, 176, "und bestimmen ab 1916 fast die ganze Politik.", 10, 400, GRAU),
        box(250, 50, 136, 110, "29. Sept. 1918:\nSie verlangen sofort\neinen Waffenstillstand.\nDer Krieg ist verloren.", "#fff", ROT, 10, 700, ROT),
        t(200, 214, "Später leugnen sie das – die „Dolchstoßlegende“ entsteht.", 10, 700, MAGENTA))


def glossar_14punkte():
    return svg("Die 14 Punkte von US-Präsident Wilson",
        f"<rect x='40' y='30' width='170' height='190' rx='6' fill='#fff' stroke='{DUNKEL}' stroke-width='2'/>",
        t(125, 56, "14 PUNKTE (Jan. 1918)", 11, 900, DUNKEL),
        t(52, 84, "• keine Geheimverträge", 10, 400, TEXT, "start"), t(52, 104, "• freie Meere", 10, 400, TEXT, "start"),
        t(52, 124, "• Abrüstung", 10, 400, TEXT, "start"), t(52, 144, "• Völker bestimmen selbst", 10, 400, TEXT, "start"),
        t(52, 164, "• Elsass-Lothringen an Frankreich", 10, 400, TEXT, "start"), t(52, 184, "• ein Völkerbund", 10, 400, TEXT, "start"),
        t(52, 204, "• …", 10, 400, GRAU, "start"),
        flag(250, 40, BLAU, "USA", 60, 36), t(310, 100, "Woodrow Wilson", 12, 900), t(310, 116, "US-Präsident", 10, 400, GRAU),
        box(230, 140, 160, 70, "Deutschland hoffte auf\neinen milden Frieden.\nVersailles wurde härter.", "#fff", GRAU, 10, 400))


def glossar_reichstag_republik():
    return svg("Ausrufung der Republik am 9. November 1918",
        f"<rect x='40' y='120' width='140' height='70' fill='#fff' stroke='{DUNKEL}' stroke-width='2'/><path d='M70,120 a40,32 0 0 1 80,0 z' fill='#fff' stroke='{DUNKEL}' stroke-width='2'/>",
        f"<rect x='90' y='100' width='40' height='20' fill='{DUNKEL}'/>", person(110, 92, ROT, .9),
        t(110, 210, "Philipp Scheidemann (SPD)", 11, 900), t(110, 224, "ruft vom Reichstag die Republik aus", 9, 400, GRAU),
        box(220, 60, 160, 50, "Kaiser Wilhelm II.\ndankt ab", "#fff", ROT, 12),
        arrow(300, 112, 300, 132, DUNKEL, 3),
        box(220, 136, 160, 50, "Friedrich Ebert (SPD)\nführt die Regierung", "#dcfce7", GRUEN, 11),
        t(200, 34, "Berlin, 9. November 1918", 14, 900, DUNKEL))


GRAFIKEN = {
    "ursachen-1": ursachen_1, "ursachen-2": ursachen_2, "ursachen-3": ursachen_3, "ursachen-4": ursachen_4,
    "ausloeser-1": ausloeser_1, "ausloeser-2": ausloeser_2, "ausloeser-3": ausloeser_3, "ausloeser-4": ausloeser_4,
    "verlauf-1": verlauf_1, "verlauf-2": verlauf_2, "verlauf-3": verlauf_3, "verlauf-4": verlauf_4,
    "kriegsende-1": kriegsende_1, "kriegsende-2": kriegsende_2, "kriegsende-3": kriegsende_3, "kriegsende-4": kriegsende_4,
    "folgen-1": folgen_1, "folgen-2": folgen_2, "folgen-3": folgen_3, "folgen-4": folgen_4,
    "glossar-marokkokrise": glossar_marokkokrise, "glossar-schlieffen": glossar_schlieffen, "glossar-steckruebe": glossar_steckruebe,
    "glossar-grippe": glossar_grippe, "glossar-weimar": glossar_weimar, "glossar-ohl": glossar_ohl,
    "glossar-14punkte": glossar_14punkte, "glossar-republik": glossar_reichstag_republik,
}


def main():
    os.makedirs(ZIEL, exist_ok=True)
    for name, fn in GRAFIKEN.items():
        with open(os.path.join(ZIEL, name + ".svg"), "w", encoding="utf-8", newline="\n") as f:
            f.write(fn())
    print(f"{len(GRAFIKEN)} Grafiken nach {ZIEL} geschrieben")


if __name__ == "__main__":
    main()
