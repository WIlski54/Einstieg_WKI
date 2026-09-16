"""Erzeugt die schematischen SVG-Grafiken für Lesestrecken und Glossar.

Aufruf:  python werkzeuge/lese_grafiken.py
Ausgabe: static/img/lese/*.svg  (400 × 240, GSM-Farben, ohne externe Schriften/Bilder)

Die Grafiken sind bewusst einfache Schaubilder: Kästen, Pfeile, Symbole, kurze Beschriftungen.
Sie sollen den Text bildlich stützen, nicht dekorieren. Jede Datei lässt sich später durch
eine echte Abbildung gleichen Namens ersetzen.
"""

import math
import os
from html import escape

ZIEL = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "static", "img", "lese")
BLAU, DUNKEL, ORANGE, MAGENTA, ROT, GRUEN, GRAU, HELL, TEXT = "#006AB3", "#004b80", "#F7B800", "#AD007C", "#dc2626", "#16a34a", "#6b7280", "#eef5fb", "#1e293b"
FONT = "font-family='Lato, Arial, sans-serif'"


def svg(titel, *teile, w=400, h=240):
    body = "\n".join(teile)
    return (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {w} {h}' role='img' aria-label='{escape(titel)}' {FONT}>\n"
            f"<title>{escape(titel)}</title>\n<rect width='{w}' height='{h}' rx='14' fill='{HELL}'/>\n{body}\n</svg>\n")


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


# ─── Gegenständliche Helfer (plastische Szenen, 480 × 288) ───────────────
# Regeln: Objekte mit Volumen (Verläufe, Schatten), echte Landschaft statt Kästen,
# Beschriftung von Pfeilen immer ÜBER oder UNTER dem Pfeil – nie auf der Linie.
SZENE_DEFS = ("<defs>"
    "<linearGradient id='gHimmel' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='#b9dcf5'/><stop offset='1' stop-color='#eef7ff'/></linearGradient>"
    "<linearGradient id='gMeer' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='#6ab6ec'/><stop offset='1' stop-color='#1b5a95'/></linearGradient>"
    "<linearGradient id='gLand' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='#bcdc8f'/><stop offset='1' stop-color='#7aa348'/></linearGradient>"
    "<linearGradient id='gSand' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='#f5e4ad'/><stop offset='1' stop-color='#d3b268'/></linearGradient>"
    "<linearGradient id='gRumpf' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='#55606f'/><stop offset='1' stop-color='#0f172a'/></linearGradient>"
    "<linearGradient id='gHolz' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='#b5804a'/><stop offset='1' stop-color='#7a4b22'/></linearGradient>"
    "<linearGradient id='gStein' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='#f8fafc'/><stop offset='1' stop-color='#c7d2df'/></linearGradient>"
    "<radialGradient id='gMuenze' cx='.35' cy='.35' r='.75'><stop offset='0' stop-color='#fff3b0'/><stop offset='1' stop-color='#c98a00'/></radialGradient>"
    "<radialGradient id='gSonne' cx='.5' cy='.5' r='.5'><stop offset='0' stop-color='#fff7c2'/><stop offset='.55' stop-color='#F7B800'/><stop offset='1' stop-color='#F7B800' stop-opacity='0'/></radialGradient>"
    "<filter id='fSchatten' x='-20%' y='-20%' width='140%' height='150%'><feDropShadow dx='0' dy='2' stdDeviation='1.6' flood-color='#000' flood-opacity='.28'/></filter>"
    "</defs>")


def tl(x, y, text, size=13, weight=700, fill=TEXT, anchor="middle"):
    """Text mit weißem Halo – lesbar auf Meer, Land und Himmel."""
    return (f"<text x='{x}' y='{y}' font-size='{size}' font-weight='{weight}' fill='{fill}' text-anchor='{anchor}' "
            f"paint-order='stroke' stroke='#fff' stroke-width='4' stroke-linejoin='round'>{escape(text)}</text>")


def flagge(x, y, art, w=18, h=12):
    rahmen = f"<rect x='{x}' y='{y}' width='{w}' height='{h}' fill='none' stroke='#0f172a' stroke-width='.6'/>"
    if art == "GB":
        return (f"<rect x='{x}' y='{y}' width='{w}' height='{h}' fill='#1d3f8f'/>"
                f"<path d='M{x},{y} L{x + w},{y + h} M{x + w},{y} L{x},{y + h}' stroke='#fff' stroke-width='{h * 0.22}'/>"
                f"<path d='M{x},{y} L{x + w},{y + h} M{x + w},{y} L{x},{y + h}' stroke='#c8102e' stroke-width='{h * 0.08}'/>"
                f"<path d='M{x + w / 2},{y} V{y + h} M{x},{y + h / 2} H{x + w}' stroke='#fff' stroke-width='{h * 0.3}'/>"
                f"<path d='M{x + w / 2},{y} V{y + h} M{x},{y + h / 2} H{x + w}' stroke='#c8102e' stroke-width='{h * 0.16}'/>" + rahmen)
    if art == "F":
        return (f"<rect x='{x}' y='{y}' width='{w / 3}' height='{h}' fill='#0055a4'/><rect x='{x + w / 3}' y='{y}' width='{w / 3}' height='{h}' fill='#fff'/>"
                f"<rect x='{x + 2 * w / 3}' y='{y}' width='{w / 3}' height='{h}' fill='#ef4135'/>" + rahmen)
    return (f"<rect x='{x}' y='{y}' width='{w}' height='{h / 3}' fill='#111'/><rect x='{x}' y='{y + h / 3}' width='{w}' height='{h / 3}' fill='#fff'/>"
            f"<rect x='{x}' y='{y + 2 * h / 3}' width='{w}' height='{h / 3}' fill='#dd0000'/>" + rahmen)


def fahnenmast(x, y, art, hoehe=24, w=18, h=12):
    return (f"<line x1='{x}' y1='{y}' x2='{x}' y2='{y - hoehe}' stroke='#374151' stroke-width='1.6'/>"
            f"<circle cx='{x}' cy='{y - hoehe}' r='1.6' fill='#374151'/>" + flagge(x + 1, y - hoehe + 1, art, w, h))


def dampfer(x, y, s=1.0, art="D"):
    """Dampfschiff, Fahrt nach rechts. x = Heck, y = Wasserlinie."""
    L = 72 * s
    rumpf = (f"<path d='M{x},{y - 13 * s} H{x + L} L{x + L + 9 * s},{y - 6 * s} L{x + L - 2 * s},{y} H{x + 7 * s} Z' fill='url(#gRumpf)' filter='url(#fSchatten)'/>"
             f"<path d='M{x + 2 * s},{y - 4 * s} H{x + L + 6 * s} L{x + L - 2 * s},{y} H{x + 7 * s} Z' fill='#b91c1c'/>"
             f"<line x1='{x}' y1='{y - 13 * s}' x2='{x + L}' y2='{y - 13 * s}' stroke='#e5e7eb' stroke-width='{1.2 * s}'/>")
    deck = (f"<rect x='{x + 16 * s}' y='{y - 25 * s}' width='{34 * s}' height='{12 * s}' rx='{2 * s}' fill='#f8fafc' stroke='#94a3b8' stroke-width='{.8 * s}'/>"
            + "".join(f"<circle cx='{x + (22 + i * 7) * s}' cy='{y - 19 * s}' r='{1.8 * s}' fill='#1e3a5f'/>" for i in range(4)))
    schlot = (f"<rect x='{x + 30 * s}' y='{y - 40 * s}' width='{10 * s}' height='{16 * s}' fill='{ORANGE}' stroke='#7c4a00' stroke-width='{.8 * s}'/>"
              f"<rect x='{x + 30 * s}' y='{y - 40 * s}' width='{10 * s}' height='{4 * s}' fill='#111827'/>")
    rauch = "".join(f"<circle cx='{x + (33 - i * 7) * s}' cy='{y - (45 + i * 8) * s}' r='{(3.5 + i * 1.8) * s}' fill='#cbd5e1' opacity='{.85 - i * .2}'/>" for i in range(3))
    mast = (f"<line x1='{x + 9 * s}' y1='{y - 13 * s}' x2='{x + 9 * s}' y2='{y - 42 * s}' stroke='#374151' stroke-width='{1.4 * s}'/>"
            + flagge(x + 10 * s, y - 42 * s, art, 16 * s, 10 * s))
    bug = f"<line x1='{x + L - 2 * s}' y1='{y - 13 * s}' x2='{x + L + 14 * s}' y2='{y - 22 * s}' stroke='#374151' stroke-width='{1.2 * s}'/>"
    return rumpf + deck + schlot + rauch + mast + bug


def dschunke(x, y, s=1.0):
    L = 30 * s
    m = x + L * 0.55
    return (f"<path d='M{x},{y - 8 * s} Q{x + L / 2},{y - 2 * s} {x + L},{y - 9 * s} L{x + L - 3 * s},{y} H{x + 3 * s} Z' fill='url(#gHolz)' stroke='#5b3b22' stroke-width='{1 * s}' filter='url(#fSchatten)'/>"
            f"<line x1='{m}' y1='{y - 6 * s}' x2='{m}' y2='{y - 34 * s}' stroke='#5b3b22' stroke-width='{1.4 * s}'/>"
            f"<path d='M{m},{y - 34 * s} L{m + 13 * s},{y - 30 * s} L{m + 9 * s},{y - 8 * s} L{m - 8 * s},{y - 10 * s} Z' fill='#e0c48a' stroke='#8b6a3e' stroke-width='{.9 * s}'/>"
            + "".join(f"<line x1='{m - 6 * s}' y1='{y - (12 + i * 6) * s}' x2='{m + 11 * s}' y2='{y - (11 + i * 6) * s}' stroke='#8b6a3e' stroke-width='{.7 * s}'/>" for i in range(3)))


def palme(x, y, s=1.0):
    tx, ty = x + 8 * s, y - 34 * s
    wedel = "".join(f"<path d='M{tx},{ty} q{dx * s},{dy * s} {ex * s},{ey * s}' stroke='#2f855a' stroke-width='{4 * s}' stroke-linecap='round' fill='none'/>"
                    for dx, dy, ex, ey in [(-10, -12, -24, -2), (-6, -14, -6, -22), (6, -14, 10, -22), (10, -10, 26, -4), (-12, -2, -22, 10), (12, -2, 24, 10)])
    return (f"<path d='M{x},{y} q{4 * s},{-18 * s} {8 * s},{-34 * s}' stroke='#8b5a2b' stroke-width='{4 * s}' stroke-linecap='round' fill='none'/>" + wedel
            + f"<circle cx='{tx - 3 * s}' cy='{ty + 2 * s}' r='{2.2 * s}' fill='#7a4b22'/><circle cx='{tx + 3 * s}' cy='{ty + 3 * s}' r='{2.2 * s}' fill='#7a4b22'/>")


def elefant(x, y, s=1.0, color="#8a8f98"):
    return (f"<g fill='{color}'><ellipse cx='{x}' cy='{y - 14 * s}' rx='{20 * s}' ry='{13 * s}'/>"
            + "".join(f"<rect x='{x + dx * s}' y='{y - 10 * s}' width='{6 * s}' height='{10 * s}' rx='{2 * s}'/>" for dx in (-16, -7, 3, 12))
            + f"<circle cx='{x + 22 * s}' cy='{y - 20 * s}' r='{9 * s}'/>"
            f"<ellipse cx='{x + 17 * s}' cy='{y - 19 * s}' rx='{5 * s}' ry='{7 * s}' fill='#6b7280'/>"
            f"<path d='M{x + 29 * s},{y - 16 * s} q{6 * s},{8 * s} {0},{14 * s}' stroke='{color}' stroke-width='{4 * s}' stroke-linecap='round' fill='none'/>"
            f"<path d='M{x + 27 * s},{y - 13 * s} q{5 * s},{2 * s} {7 * s},{7 * s}' stroke='#fff' stroke-width='{1.8 * s}' stroke-linecap='round' fill='none'/>"
            f"<circle cx='{x + 25 * s}' cy='{y - 22 * s}' r='{1.2 * s}' fill='#111'/></g>")


def kiste(x, y, w=26, h=20, label=""):
    out = (f"<rect x='{x}' y='{y}' width='{w}' height='{h}' fill='url(#gHolz)' stroke='#5b3b22' stroke-width='1.2' filter='url(#fSchatten)'/>"
           f"<path d='M{x},{y} L{x + w},{y + h} M{x + w},{y} L{x},{y + h}' stroke='#5b3b22' stroke-width='1.2'/>"
           f"<rect x='{x + 1}' y='{y + 1}' width='{w - 2}' height='{h - 2}' fill='none' stroke='#d9a86c' stroke-width='.8' opacity='.7'/>")
    if label:
        out += tl(x + w / 2, y + h / 2 + 3, label, 8, 800, "#3b2414")
    return out


def sack(x, y, w=16, h=20, fill="#d9b382"):
    return (f"<path d='M{x},{y} C{x - 2},{y - h * 0.5} {x + w * 0.3},{y - h * 0.7} {x + w * 0.35},{y - h} h{w * 0.3} "
            f"C{x + w * 0.7},{y - h * 0.7} {x + w + 2},{y - h * 0.5} {x + w},{y} Z' fill='{fill}' stroke='#8b6a3e' stroke-width='1' filter='url(#fSchatten)'/>"
            f"<line x1='{x + w * 0.32}' y1='{y - h * 0.9}' x2='{x + w * 0.68}' y2='{y - h * 0.9}' stroke='#8b6a3e' stroke-width='1.6'/>")


def muenzstapel(x, y, n=3, r=6):
    out = ""
    for k in range(n):
        cy = y - k * 3.2
        out += f"<rect x='{x - r}' y='{cy - 1.6}' width='{2 * r}' height='3.2' fill='#c98a00'/>"
        out += f"<ellipse cx='{x}' cy='{cy - 1.6}' rx='{r}' ry='{r * 0.42}' fill='url(#gMuenze)' stroke='#b8860b' stroke-width='.7'/>"
    return out


def pagode(x, y, s=1.0):
    """x = Mitte, y = Boden."""
    def dach(yb, halb, hoehe):
        return (f"<path d='M{x - halb * s},{yb - 5 * s} Q{x},{yb + 4 * s} {x + halb * s},{yb - 5 * s} L{x + halb * 0.4 * s},{yb - hoehe * s} "
                f"L{x - halb * 0.4 * s},{yb - hoehe * s} Z' fill='#9f1239' stroke='#4c0519' stroke-width='{1 * s}' filter='url(#fSchatten)'/>")
    def wand(yt, yb, halb):
        return (f"<rect x='{x - halb * s}' y='{yt}' width='{2 * halb * s}' height='{yb - yt}' fill='#fde68a' stroke='#92400e' stroke-width='{.8 * s}'/>"
                f"<rect x='{x - 3 * s}' y='{yt + 3 * s}' width='{6 * s}' height='{yb - yt - 5 * s}' fill='#7c2d12'/>")
    return (wand(y - 14 * s, y, 11) + dach(y - 14 * s, 30, 12)
            + wand(y - 38 * s, y - 26 * s, 9) + dach(y - 38 * s, 24, 11)
            + wand(y - 59 * s, y - 49 * s, 7) + dach(y - 59 * s, 18, 10)
            + f"<line x1='{x}' y1='{y - 69 * s}' x2='{x}' y2='{y - 80 * s}' stroke='#4c0519' stroke-width='{1.5 * s}'/><circle cx='{x}' cy='{y - 81 * s}' r='{2 * s}' fill='{ORANGE}'/>")


def marktstand(x, y, s=1.0):
    """x = links, y = Boden, Breite 56·s."""
    w = 56 * s
    out = (f"<rect x='{x + 4 * s}' y='{y - 16 * s}' width='{w - 8 * s}' height='{16 * s}' fill='url(#gHolz)' stroke='#5b3b22' stroke-width='{1 * s}'/>"
           f"<line x1='{x + 2 * s}' y1='{y}' x2='{x + 2 * s}' y2='{y - 40 * s}' stroke='#5b3b22' stroke-width='{2 * s}'/>"
           f"<line x1='{x + w - 2 * s}' y1='{y}' x2='{x + w - 2 * s}' y2='{y - 40 * s}' stroke='#5b3b22' stroke-width='{2 * s}'/>")
    streifen = "".join(f"<rect x='{x + i * w / 7}' y='{y - 46 * s}' width='{w / 7}' height='{8 * s}' fill='{ORANGE if i % 2 == 0 else '#fff'}'/>" for i in range(7))
    bogen = "".join(f"<path d='M{x + i * w / 7},{y - 38 * s} a{w / 14},{4 * s} 0 0 0 {w / 7},0 z' fill='{ORANGE if i % 2 == 0 else '#fff'}'/>" for i in range(7))
    out += f"<g filter='url(#fSchatten)'>{streifen}{bogen}<rect x='{x}' y='{y - 46 * s}' width='{w}' height='{8 * s}' fill='none' stroke='#7c4a00' stroke-width='{.8 * s}'/></g>"
    return out


def fabrik(x, y, s=1.0):
    w, h = 54 * s, 26 * s
    out = f"<rect x='{x}' y='{y - h}' width='{w}' height='{h}' fill='#b45309' stroke='#78350f' stroke-width='{1 * s}' filter='url(#fSchatten)'/>"
    out += "".join(f"<path d='M{x + i * w / 3},{y - h} L{x + i * w / 3},{y - h - 10 * s} L{x + (i + 1) * w / 3},{y - h} Z' fill='#7c2d12'/>" for i in range(3))
    out += "".join(f"<rect x='{x + (6 + i * 12) * s}' y='{y - h + 8 * s}' width='{7 * s}' height='{9 * s}' fill='#fde68a' stroke='#78350f' stroke-width='{.6 * s}'/>" for i in range(4))
    for cx in (x + 10 * s, x + 26 * s):
        out += f"<rect x='{cx}' y='{y - h - 26 * s}' width='{6 * s}' height='{18 * s}' fill='#57534e' stroke='#292524' stroke-width='{.8 * s}'/>"
        out += "".join(f"<circle cx='{cx + 3 * s - i * 5 * s}' cy='{y - h - (30 + i * 7) * s}' r='{(3 + i * 1.5) * s}' fill='#9ca3af' opacity='{.8 - i * .2}'/>" for i in range(3))
    return out


def palast(x, y, s=1.0):
    """Regierungsgebäude mit Kuppel. x = links, y = Boden, Breite 90·s."""
    w, h = 90 * s, 30 * s
    out = f"<rect x='{x}' y='{y - h}' width='{w}' height='{h}' fill='url(#gStein)' stroke='#64748b' stroke-width='{1 * s}' filter='url(#fSchatten)'/>"
    out += "".join(f"<rect x='{x + (6 + i * 14) * s}' y='{y - h + 5 * s}' width='{5 * s}' height='{h - 5 * s}' fill='#fff' stroke='#94a3b8' stroke-width='{.7 * s}'/>" for i in range(6))
    out += f"<path d='M{x + w / 2 - 16 * s},{y - h - 4 * s} a{16 * s},{16 * s} 0 0 1 {32 * s},0 z' fill='#2e7d5b' stroke='#1f5c42' stroke-width='{.8 * s}'/>"
    out += f"<rect x='{x - 2 * s}' y='{y - h - 4 * s}' width='{w + 4 * s}' height='{5 * s}' fill='#cbd5e1' stroke='#64748b' stroke-width='{.8 * s}'/>"
    return out


def uhr(x, y, r=11):
    out = f"<circle cx='{x}' cy='{y}' r='{r}' fill='#fff' stroke='{DUNKEL}' stroke-width='2.2' filter='url(#fSchatten)'/>"
    for i in range(12):
        a = i * math.pi / 6
        out += (f"<line x1='{x + (r - 2.5) * math.cos(a):.1f}' y1='{y + (r - 2.5) * math.sin(a):.1f}' x2='{x + (r - 1) * math.cos(a):.1f}' "
                f"y2='{y + (r - 1) * math.sin(a):.1f}' stroke='{DUNKEL}' stroke-width='1.2'/>")
    out += (f"<line x1='{x}' y1='{y}' x2='{x}' y2='{y - r * 0.62}' stroke='{DUNKEL}' stroke-width='2.2' stroke-linecap='round'/>"
            f"<line x1='{x}' y1='{y}' x2='{x + r * 0.5}' y2='{y + r * 0.28}' stroke='{ROT}' stroke-width='2' stroke-linecap='round'/>"
            f"<circle cx='{x}' cy='{y}' r='1.6' fill='{DUNKEL}'/>")
    return out



FLAGGEN_STREIFEN = {
    "OE": ("h", ["#111", "#f5c400"]),                 # Österreich-Ungarn (schwarz-gelb)
    "I": ("v", ["#009246", "#fff", "#ce2b37"]),        # Italien
    "R": ("h", ["#fff", "#0039a6", "#d52b1e"]),        # Russland
    "SRB": ("h", ["#c6363c", "#0c4076", "#fff"]),      # Serbien
    "B": ("v", ["#111", "#f5c400", "#ef3340"]),        # Belgien
}


def flagge2(x, y, art, w=18, h=12):
    """Flagge für weitere Staaten; GB/F/D über flagge()."""
    if art not in FLAGGEN_STREIFEN:
        return flagge(x, y, art, w, h)
    richtung, farben = FLAGGEN_STREIFEN[art]
    n = len(farben)
    out = ""
    for i, c in enumerate(farben):
        if richtung == "h":
            out += f"<rect x='{x}' y='{y + i * h / n}' width='{w}' height='{h / n}' fill='{c}'/>"
        else:
            out += f"<rect x='{x + i * w / n}' y='{y}' width='{w / n}' height='{h}' fill='{c}'/>"
    return out + f"<rect x='{x}' y='{y}' width='{w}' height='{h}' fill='none' stroke='#0f172a' stroke-width='.6'/>"


def mensch(x, y, s=1.0, farbe="#1e3a5f", haut="#f1c9a5", art=None, hut=False):
    """Stehende Figur, x = Mitte, y = Boden. Optional Fahne in der rechten Hand."""
    out = (f"<g filter='url(#fSchatten)'>"
           f"<rect x='{x - 7 * s}' y='{y - 22 * s}' width='{5.5 * s}' height='{22 * s}' rx='{2 * s}' fill='#2b2b2b'/>"
           f"<rect x='{x + 1.5 * s}' y='{y - 22 * s}' width='{5.5 * s}' height='{22 * s}' rx='{2 * s}' fill='#2b2b2b'/>"
           f"<path d='M{x - 9 * s},{y - 22 * s} v-{20 * s} a{9 * s},{9 * s} 0 0 1 {18 * s},0 v{20 * s} z' fill='{farbe}'/>"
           f"<circle cx='{x}' cy='{y - 50 * s}' r='{7 * s}' fill='{haut}'/>"
           f"<path d='M{x - 7 * s},{y - 52 * s} a{7 * s},{7 * s} 0 0 1 {14 * s},0 z' fill='#3b2a1a'/>")
    if hut:
        out += f"<rect x='{x - 8 * s}' y='{y - 58 * s}' width='{16 * s}' height='{3 * s}' fill='#1f2937'/><rect x='{x - 5 * s}' y='{y - 66 * s}' width='{10 * s}' height='{8 * s}' fill='#1f2937'/>"
    if art:
        out += (f"<line x1='{x + 12 * s}' y1='{y - 38 * s}' x2='{x + 12 * s}' y2='{y - 78 * s}' stroke='#5b3b22' stroke-width='{1.8 * s}'/>"
                f"<line x1='{x + 9 * s}' y1='{y - 36 * s}' x2='{x + 12 * s}' y2='{y - 44 * s}' stroke='{farbe}' stroke-width='{4 * s}' stroke-linecap='round'/>"
                + flagge2(x + 13 * s, y - 78 * s, art, 20 * s, 13 * s))
    return out + "</g>"


def sprechblase(x, y, w, h, zeilen, zx, zy, farbe=MAGENTA, size=11):
    """Rechteckige Sprechblase mit Zipfel Richtung (zx, zy)."""
    out = (f"<path d='M{x + 8},{y} H{x + w - 8} Q{x + w},{y} {x + w},{y + 8} V{y + h - 8} Q{x + w},{y + h} {x + w - 8},{y + h} "
           f"H{x + 8} Q{x},{y + h} {x},{y + h - 8} V{y + 8} Q{x},{y} {x + 8},{y} Z' fill='#fff' stroke='{farbe}' stroke-width='2' filter='url(#fSchatten)'/>")
    # Zipfel: vom unteren Rand zur Zielposition
    bx = min(max(zx, x + 14), x + w - 14)
    out += f"<path d='M{bx - 6},{y + h - 1} L{zx},{zy} L{bx + 6},{y + h - 1} Z' fill='#fff' stroke='{farbe}' stroke-width='2' stroke-linejoin='round'/>"
    out += f"<line x1='{bx - 6}' y1='{y + h - 1}' x2='{bx + 6}' y2='{y + h - 1}' stroke='#fff' stroke-width='3'/>"
    start = y + h / 2 - (len(zeilen) - 1) * (size + 3) / 2 + size / 3
    for i, z in enumerate(zeilen):
        out += t(x + w / 2, start + i * (size + 3), z, size, 800, farbe)
    return out


def zaun(x1, y, x2, h=14, farbe="#7a4b22"):
    out = "".join(f"<rect x='{x - 1.5}' y='{y - h}' width='3' height='{h}' fill='{farbe}'/>" for x in range(int(x1), int(x2) + 1, 12))
    out += f"<rect x='{x1 - 1.5}' y='{y - h * 0.75}' width='{x2 - x1 + 3}' height='2.2' fill='{farbe}'/><rect x='{x1 - 1.5}' y='{y - h * 0.35}' width='{x2 - x1 + 3}' height='2.2' fill='{farbe}'/>"
    return out


def grenzpfahl(x, y, s=1.0):
    """Schwarz-weiß-roter Grenzpfahl (Deutsches Reich)."""
    out = ""
    for i, c in enumerate(["#111", "#fff", "#dd0000"] * 3):
        out += f"<rect x='{x - 3 * s}' y='{y - (9 - i) * 5 * s}' width='{6 * s}' height='{5 * s}' fill='{c}' stroke='#111' stroke-width='.4'/>"
    return out + f"<circle cx='{x}' cy='{y - 46 * s}' r='{3 * s}' fill='#111'/>"


def wegweiser(x, y, text, s=1.0, farbe="#7a4b22"):
    w = len(text) * 5.6 * s + 14 * s
    return (f"<rect x='{x - 1.5 * s}' y='{y - 44 * s}' width='{3 * s}' height='{44 * s}' fill='{farbe}'/>"
            f"<path d='M{x - w / 2},{y - 42 * s} H{x + w / 2 - 6 * s} L{x + w / 2},{y - 35 * s} L{x + w / 2 - 6 * s},{y - 28 * s} H{x - w / 2} Z' fill='#fde68a' stroke='{farbe}' stroke-width='{1.2 * s}' filter='url(#fSchatten)'/>"
            + t(x - 3 * s, y - 31.5 * s, text, 9 * s, 800, "#3b2414"))


def kriegsschiff(x, y, s=1.0, art="D"):
    """Schlachtschiff (Dreadnought), Fahrt nach rechts. x = Heck, y = Wasserlinie."""
    L = 80 * s
    out = (f"<path d='M{x},{y - 11 * s} H{x + L} L{x + L + 10 * s},{y - 5 * s} L{x + L - 2 * s},{y} H{x + 6 * s} Z' fill='#6b7280' stroke='#374151' stroke-width='{.8 * s}' filter='url(#fSchatten)'/>"
           f"<path d='M{x + 2 * s},{y - 3 * s} H{x + L + 7 * s} L{x + L - 2 * s},{y} H{x + 6 * s} Z' fill='#7f1d1d'/>"
           f"<rect x='{x + 28 * s}' y='{y - 24 * s}' width='{26 * s}' height='{13 * s}' fill='#9ca3af' stroke='#4b5563' stroke-width='{.8 * s}'/>"
           f"<rect x='{x + 36 * s}' y='{y - 36 * s}' width='{7 * s}' height='{12 * s}' fill='#4b5563'/>"
           f"<rect x='{x + 46 * s}' y='{y - 34 * s}' width='{7 * s}' height='{10 * s}' fill='#4b5563'/>")
    for tx in (x + 12 * s, x + 62 * s):   # Geschütztürme mit Doppelrohr
        out += (f"<rect x='{tx}' y='{y - 18 * s}' width='{12 * s}' height='{7 * s}' rx='{2 * s}' fill='#4b5563'/>"
                f"<line x1='{tx + 6 * s}' y1='{y - 15 * s}' x2='{tx + 22 * s}' y2='{y - 17 * s}' stroke='#1f2937' stroke-width='{1.6 * s}'/>"
                f"<line x1='{tx + 6 * s}' y1='{y - 12.5 * s}' x2='{tx + 22 * s}' y2='{y - 14.5 * s}' stroke='#1f2937' stroke-width='{1.6 * s}'/>")
    out += "".join(f"<circle cx='{x + (39 - i * 6) * s}' cy='{y - (40 + i * 7) * s}' r='{(3 + i * 1.6) * s}' fill='#9ca3af' opacity='{.8 - i * .2}'/>" for i in range(3))
    out += (f"<line x1='{x + 20 * s}' y1='{y - 11 * s}' x2='{x + 20 * s}' y2='{y - 44 * s}' stroke='#374151' stroke-width='{1.2 * s}'/>"
            + flagge2(x + 21 * s, y - 44 * s, art, 14 * s, 9 * s))
    return out


def burg_vielvoelker(x, y, s=1.0):
    """Habsburger Vielvölkerreich als Flickenburg: x = links, y = Boden, Breite 120·s."""
    farben = ["#93c5fd", "#fca5a5", "#fde68a", "#bbf7d0", "#ddd6fe", "#fdba74", "#a5f3fc", "#f9a8d4", "#d9f99d", "#e5e7eb"]
    w, h = 120 * s, 54 * s
    out = f"<rect x='{x}' y='{y - h}' width='{w}' height='{h}' fill='#cbd5e1' stroke='#475569' stroke-width='{1.2 * s}' filter='url(#fSchatten)'/>"
    k = 0
    for reihe in range(3):
        for spalte in range(5):
            bx = x + spalte * w / 5 + (reihe % 2) * w / 10
            if bx + w / 5 > x + w:
                continue
            out += f"<rect x='{bx + 1}' y='{y - h + reihe * h / 3 + 1}' width='{w / 5 - 2}' height='{h / 3 - 2}' fill='{farben[k % len(farben)]}' stroke='#64748b' stroke-width='.6'/>"
            k += 1
    # Türme mit Zinnen
    for tx in (x - 8 * s, x + w - 14 * s):
        out += f"<rect x='{tx}' y='{y - h - 16 * s}' width='{22 * s}' height='{h + 16 * s}' fill='#94a3b8' stroke='#475569' stroke-width='{1 * s}'/>"
        out += "".join(f"<rect x='{tx + i * 7 * s}' y='{y - h - 22 * s}' width='{5 * s}' height='{6 * s}' fill='#94a3b8' stroke='#475569' stroke-width='{.8 * s}'/>" for i in range(3))
    out += f"<path d='M{x + 30 * s},{y - h} L{x + w - 30 * s},{y - h} L{x + w / 2},{y - h - 26 * s} Z' fill='#7f1d1d' stroke='#450a0a' stroke-width='{1 * s}'/>"
    out += krone(x + w / 2, y - h - 32 * s)
    # Risse
    out += f"<path d='M{x + 40 * s},{y - h + 4 * s} l4,8 l-5,6 l6,9 l-3,8 M{x + 84 * s},{y - h + 2 * s} l-4,9 l5,7 l-6,8' fill='none' stroke='#1f2937' stroke-width='{1.6 * s}' stroke-linecap='round'/>"
    # Tor
    out += f"<path d='M{x + w / 2 - 9 * s},{y} v-{14 * s} a{9 * s},{9 * s} 0 0 1 {18 * s},0 v{14 * s} z' fill='#3b2414'/>"
    return out


def himmel_und_boden(W, H, horizont, boden="url(#gLand)"):
    return (f"<rect width='{W}' height='{H}' fill='url(#gHimmel)'/>"
            f"<path d='M0,{horizont + 14} Q{W * 0.25},{horizont - 10} {W * 0.5},{horizont + 6} T{W},{horizont} V{H} H0 Z' fill='{boden}' stroke='#5b8a3a' stroke-width='1.5'/>")


def fussleiste(W, H, zeilen, hoehe=36, farbe=TEXT, size=12):
    sizes = size if isinstance(size, (list, tuple)) else [size] * len(zeilen)
    out = f"<rect x='0' y='{H - hoehe}' width='{W}' height='{hoehe}' fill='#fff' opacity='.94'/><line x1='0' y1='{H - hoehe}' x2='{W}' y2='{H - hoehe}' stroke='#cbd5e1'/>"
    if len(zeilen) == 1:
        return out + t(W / 2, H - hoehe / 2 + sizes[0] / 3, zeilen[0], sizes[0], 800, farbe)
    y = H - hoehe + 4
    for i, (z, s) in enumerate(zip(zeilen, sizes)):
        y += s + 1
        out += t(W / 2, y, z, s, 800 if i == 0 else 600, farbe if i == 0 else GRAU)
    return out


# ─── Lesestrecke Ursachen ─────────────────────────────────────────────────
def ursachen_1():
    W, H = 480, 288
    wellen = "".join(f"<path d='M{x},{y} q5,-3 10,0 t10,0 t10,0' stroke='#dbeafe' stroke-width='1.3' fill='none' opacity='.7'/>"
                     for x, y in [(160, 122), (205, 128), (262, 118), (215, 178), (176, 224), (300, 152), (255, 228), (338, 134), (405, 140), (455, 138)])
    return svg("Wettlauf um Kolonien: Großmächte Europas greifen nach Afrika und Asien",
        SZENE_DEFS,
        f"<clipPath id='cpSzene'><rect width='{W}' height='{H}' rx='14'/></clipPath>",
        "<g clip-path='url(#cpSzene)'>",
        f"<rect width='{W}' height='{H}' fill='url(#gHimmel)'/>",
        "<circle cx='262' cy='24' r='20' fill='url(#gSonne)'/><circle cx='262' cy='24' r='8' fill='#ffe66b' stroke='#e0a800' stroke-width='1'/>",
        "<path d='M196,40 q4,-4 8,0 q4,-4 8,0 M214,30 q3,-3 6,0 q3,-3 6,0' stroke='#475569' stroke-width='1.2' fill='none'/>",
        f"<rect x='0' y='108' width='{W}' height='{H - 108}' fill='url(#gMeer)'/>",
        wellen,
        # Landmassen
        "<path d='M0,0 H120 C150,30 125,70 140,100 C160,130 122,165 138,200 C150,230 118,262 128,288 H0 Z' fill='url(#gLand)' stroke='#5b8a3a' stroke-width='2'/>",
        "<path d='M300,0 H480 V118 C450,135 425,108 400,120 C370,132 345,105 322,92 C300,80 296,40 300,0 Z' fill='url(#gSand)' stroke='#b8965a' stroke-width='2'/>",
        "<ellipse cx='350' cy='70' rx='24' ry='8' fill='#a3c46f' opacity='.6'/><ellipse cx='420' cy='62' rx='16' ry='6' fill='#a3c46f' opacity='.5'/>",
        "<path d='M330,150 C355,140 385,158 410,150 C440,142 462,158 480,150 V288 H330 C318,250 316,200 330,150 Z' fill='url(#gLand)' stroke='#5b8a3a' stroke-width='2'/>",
        # Europa: Regierung, Fabrik, Hafen
        tl(62, 22, "Großmächte", 14, 800, DUNKEL), tl(62, 38, "Europas", 13, 700, DUNKEL),
        palast(14, 112, 0.95),
        fahnenmast(25.4, 79.7, "GB", 20), fahnenmast(56.75, 64.5, "F", 20), fahnenmast(88.1, 79.7, "D", 20),
        fabrik(18, 204, 0.95),
        "<rect x='104' y='223' width='3' height='9' fill='#5b3b22'/><rect x='124' y='223' width='3' height='9' fill='#5b3b22'/><rect x='144' y='223' width='3' height='9' fill='#5b3b22'/>",
        "<rect x='98' y='216' width='56' height='7' rx='2' fill='url(#gHolz)' stroke='#5b3b22' stroke-width='1'/>",
        kiste(104, 202, 14, 14),
        # Schiffe: GB und F voraus, D noch im Hafen
        dampfer(176, 142, 0.8, "GB"), dampfer(242, 158, 0.8, "F"), dampfer(158, 242, 0.7, "D"),
        dschunke(272, 246, 1.0),
        # Pfeile mit Beschriftung darüber bzw. darunter
        curve("M150,95 C200,62 260,58 314,84", MAGENTA, 3.5), tl(232, 56, "Wettlauf", 13, 800, MAGENTA),
        curve("M140,170 C190,180 250,186 310,198", MAGENTA, 3.5), tl(228, 210, "Wettlauf", 13, 800, MAGENTA),
        # Afrika: Rohstoffe
        tl(400, 22, "Afrika", 15, 800, DUNKEL), tl(400, 38, "Rohstoffe", 12, 800, MAGENTA),
        "<path d='M418,94 L452,42 L480,78 V94 Z' fill='#9aa3ae' stroke='#6b7280' stroke-width='1.2'/><path d='M443,56 L452,42 L461,55 Q452,60 443,56 Z' fill='#fff'/>",
        palme(322, 86, 0.85), palme(340, 94, 1.0),
        fahnenmast(388, 70, "GB", 24),
        elefant(384, 102, 0.85),
        sack(420, 104, 14, 18), kiste(444, 100, 26, 20), kiste(447, 81, 22, 18),
        # Asien: Märkte
        tl(400, 170, "Asien", 15, 800, DUNKEL), tl(400, 186, "Märkte", 12, 800, MAGENTA),
        pagode(452, 246, 0.85),
        fahnenmast(333, 200, "F", 24),
        marktstand(343, 246, 0.9),
        sack(349, 231, 12, 16), kiste(363, 217, 18, 14, "Tee"), muenzstapel(384, 230, 3, 5),
        # Fußzeile: Deutschland kommt zu spät
        "<rect x='0' y='252' width='480' height='36' fill='#fff' opacity='.93'/><line x1='0' y1='252' x2='480' y2='252' stroke='#cbd5e1'/>",
        uhr(24, 270, 11), flagge(44, 264, "D", 18, 12),
        t(70, 274.5, "Deutschland: erst seit 1871 – kommt zu spät", 13, 800, ROT, "start"),
        "</g>",
        w=W, h=H)


def ursachen_2():
    W, H = 480, 288
    return svg("Nationalismus: Frankreich will Elsass-Lothringen zurück, Serbien will alle Südslawen vereinen",
        SZENE_DEFS, f"<clipPath id='cpSzene'><rect width='{W}' height='{H}' rx='14'/></clipPath>", "<g clip-path='url(#cpSzene)'>",
        himmel_und_boden(W, H, 150),
        tl(240, 22, "Nationalismus: „Unser Volk ist das beste!“", 14, 800, DUNKEL),
        # ── links: Frankreich / Elsass-Lothringen / Deutsches Reich ──
        "<path d='M112,150 C130,170 110,200 128,226 C140,244 120,252 128,262 L232,262 C226,236 240,206 228,180 C222,166 236,154 226,150 Z' fill='#fde68a' opacity='.55' stroke='#b45309' stroke-width='1.2'/>",
        zaun(118, 236, 128, 12), zaun(120, 262, 130, 0),
        "<path d='M118,150 C136,170 116,200 134,226 C146,244 126,252 134,262' fill='none' stroke='#7a4b22' stroke-width='3'/>",
        grenzpfahl(140, 232, 0.9),
        tl(176, 196, "Elsass-", 11, 800, "#7c2d12"), tl(176, 210, "Lothringen", 11, 800, "#7c2d12"),
        wegweiser(200, 262, "seit 1871 deutsch", 0.9),
        fahnenmast(214, 178, "D", 26, 18, 12),
        mensch(40, 262, 0.75, "#1d4ed8", art="F"), mensch(64, 258, 0.7, "#1e40af"), mensch(86, 262, 0.75, "#1d4ed8"),
        sprechblase(14, 62, 166, 44, ["Gebt uns", "Elsass-Lothringen zurück!"], 60, 200, ROT, 11),
        tl(60, 280, "Frankreich", 12, 800, DUNKEL), tl(342, 176, "Deutsches Reich", 11, 800, "#111"),
        # ── rechts: Serbien / Österreich-Ungarn ──
        mensch(272, 258, 0.72, "#7f1d1d", art="SRB"), mensch(292, 262, 0.72, "#991b1b"),
        sprechblase(292, 60, 150, 44, ["Alle Südslawen", "in einen Staat!"], 272, 196, ROT, 11),
        burg_vielvoelker(352, 262, 0.95),
        tl(409, 274, "Österreich-Ungarn", 10, 800, DUNKEL), tl(409, 285, "viele Völker", 9, 700, "#7f1d1d"),
        tl(280, 280, "Serbien", 12, 800, DUNKEL),
        curve("M306,236 C322,226 336,224 348,228", ROT, 3.5), tl(326, 216, "bedroht", 11, 800, ROT),
        "</g>", w=W, h=H)


def ursachen_3():
    W, H = 480, 288
    wellen = "".join(f"<path d='M{x},{y} q5,-3 10,0 t10,0 t10,0' stroke='#dbeafe' stroke-width='1.3' fill='none' opacity='.7'/>"
                     for x, y in [(20, 100), (70, 126), (120, 96), (40, 168), (150, 172), (90, 200), (30, 228), (170, 232)])
    return svg("Militarismus: Flottenwettrüsten und Schlieffen-Plan",
        SZENE_DEFS, f"<clipPath id='cpSzene'><rect width='{W}' height='{H}' rx='14'/></clipPath>", "<g clip-path='url(#cpSzene)'>",
        f"<rect width='{W}' height='{H}' fill='url(#gHimmel)'/>",
        # ── links: Nordsee mit Schlachtschiffen ──
        f"<rect x='0' y='60' width='218' height='{H - 60}' fill='url(#gMeer)'/>", wellen,
        tl(108, 24, "Flottenwettrüsten", 14, 800, DUNKEL), tl(108, 40, "Beide bauen immer mehr Schiffe", 10, 700, GRAU),
        kriegsschiff(14, 108, 0.62, "D"), kriegsschiff(84, 118, 0.62, "D"), kriegsschiff(154, 108, 0.55, "D"),
        kriegsschiff(6, 186, 0.62, "GB"), kriegsschiff(70, 196, 0.62, "GB"), kriegsschiff(134, 186, 0.62, "GB"), kriegsschiff(150, 236, 0.5, "GB"),
        tl(20, 150, "Deutschland: 3", 11, 800, "#111", "start"), tl(20, 226, "Großbritannien: 4", 11, 800, "#1d3f8f", "start"),
        "<line x1='218' y1='0' x2='218' y2='288' stroke='#94a3b8' stroke-width='1.5' stroke-dasharray='5 4'/>",
        # ── rechts: Karte mit Schlieffen-Plan ──
        tl(350, 24, "Schlieffen-Plan", 14, 800, DUNKEL), tl(350, 40, "Krieg an zwei Fronten vermeiden", 10, 700, GRAU),
        "<rect x='226' y='52' width='254' height='236' fill='#e6f0f8'/>",
        "<path d='M226,110 C250,96 270,120 300,104 L312,150 C300,188 262,196 232,184 Z' fill='#bfdbfe' stroke='#1d4ed8' stroke-width='1.5'/>",   # Frankreich
        "<path d='M300,104 C316,84 336,92 342,108 L338,128 L312,150 Z' fill='#fde68a' stroke='#b45309' stroke-width='1.5'/>",                    # Belgien
        "<path d='M342,108 C360,80 400,86 412,112 L416,178 C392,198 350,196 338,178 L312,150 L338,128 Z' fill='#e5e7eb' stroke='#374151' stroke-width='1.5'/>",  # Deutschland
        "<path d='M412,112 C440,96 480,100 480,110 V240 C450,236 430,222 416,178 Z' fill='#d1fae5' stroke='#047857' stroke-width='1.5'/>",        # Russland
        tl(262, 148, "Frankreich", 11, 800, "#1e3a8a"), tl(322, 118, "Belgien", 9, 800, "#7c2d12"), tl(376, 150, "Deutschland", 11, 800, "#111"), tl(452, 176, "Russland", 11, 800, "#065f46"),
        flagge2(252, 154, "F", 14, 9), flagge2(314, 122, "B", 12, 8), flagge2(368, 154, "D", 14, 9), flagge2(444, 180, "R", 14, 9),
        # Pfeil 1: schnell über Belgien nach Frankreich – Beschriftung ÜBER dem Pfeil, frei vom Pfeil
        "<path d='M370,126 C346,96 300,84 268,118' fill='none' stroke='#fff' stroke-width='9' stroke-linecap='round'/>",
        curve("M370,126 C346,96 300,84 268,118", ROT, 5),
        "<rect x='282' y='62' width='84' height='18' rx='9' fill='#fff' stroke='#dc2626' stroke-width='1.5'/>", t(324, 75, "1. schnell", 12, 900, ROT),
        # Pfeil 2: danach nach Russland – Beschriftung UNTER dem Pfeil
        "<path d='M396,170 C410,196 428,206 448,210' fill='none' stroke='#fff' stroke-width='9' stroke-linecap='round'/>",
        curve("M396,170 C410,196 428,206 448,210", DUNKEL, 5, "9 5"),
        "<rect x='384' y='224' width='80' height='18' rx='9' fill='#fff' stroke='#004b80' stroke-width='1.5'/>", t(424, 237, "2. danach", 12, 900, DUNKEL),
        # Pickelhaube als Symbol des Militarismus
        "<path d='M246,254 a20,14 0 0 1 40,0 z' fill='#374151' stroke='#111' stroke-width='1.2' filter='url(#fSchatten)'/><rect x='240' y='252' width='52' height='6' rx='3' fill='#111'/><rect x='264' y='234' width='4' height='10' fill='#F7B800'/><path d='M262,236 l4,-8 l4,8 z' fill='#F7B800'/>",
        tl(304, 266, "Militär hat hohes Ansehen", 10, 700, GRAU, "start"),
        "</g>", w=W, h=H)


def ursachen_4():
    W, H = 480, 288
    seil = lambda x1, x2, y: f"<path d='M{x1},{y} Q{(x1 + x2) / 2},{y + 10} {x2},{y}' fill='none' stroke='#7a4b22' stroke-width='3' stroke-linecap='round'/>"
    return svg("Bündnissystem: Dreibund gegen Triple Entente, dazwischen das Pulverfass Balkan",
        SZENE_DEFS, f"<clipPath id='cpSzene'><rect width='{W}' height='{H}' rx='14'/></clipPath>", "<g clip-path='url(#cpSzene)'>",
        himmel_und_boden(W, H, 150),
        # ── Dreibund links ──
        "<rect x='8' y='10' width='176' height='26' rx='13' fill='#fde7f3' stroke='#AD007C' stroke-width='1.5'/>", t(96, 28, "Dreibund (1882)", 13, 900, MAGENTA),
        seil(32, 96, 196), seil(96, 160, 196),
        mensch(32, 226, 0.8, "#1f2937", art="D", hut=True), mensch(96, 226, 0.8, "#b45309", art="OE"), mensch(160, 226, 0.8, "#166534", art="I"),
        tl(32, 238, "Deutschland", 9, 800, DUNKEL), tl(96, 238, "Österreich-", 9, 800, DUNKEL), tl(96, 248, "Ungarn", 9, 800, DUNKEL), tl(160, 238, "Italien", 9, 800, DUNKEL),
        # ── Triple Entente rechts ──
        "<rect x='292' y='10' width='180' height='26' rx='13' fill='#dbe9f7' stroke='#006AB3' stroke-width='1.5'/>", t(382, 28, "Triple Entente (1907)", 13, 900, BLAU),
        seil(324, 384, 196), seil(384, 444, 196),
        mensch(324, 226, 0.8, "#1d4ed8", art="F"), mensch(384, 226, 0.8, "#7f1d1d", art="R"), mensch(444, 226, 0.8, "#1d3f8f", art="GB", hut=True),
        tl(324, 238, "Frankreich", 9, 800, DUNKEL), tl(384, 238, "Russland", 9, 800, DUNKEL), tl(444, 238, "Groß-", 9, 800, DUNKEL), tl(444, 248, "britannien", 9, 800, DUNKEL),
        # ── Streit-Blitze oben in der Mitte ──
        f"<path d='M222,44 l14,22 l-10,6 l16,26' fill='none' stroke='{ROT}' stroke-width='5' stroke-linecap='round' stroke-linejoin='round'/>",
        f"<path d='M258,44 l-14,22 l10,6 l-16,26' fill='none' stroke='{ROT}' stroke-width='5' stroke-linecap='round' stroke-linejoin='round'/>",
        tl(240, 112, "Streit", 12, 900, ROT),
        # ── Pulverfass Balkan: Lunte brennt, Funke berührt keinen Text ──
        "<rect x='212' y='168' width='56' height='64' rx='11' fill='url(#gHolz)' stroke='#5b3b22' stroke-width='3' filter='url(#fSchatten)'/>",
        "<line x1='212' y1='188' x2='268' y2='188' stroke='#5b3b22' stroke-width='3'/><line x1='212' y1='214' x2='268' y2='214' stroke='#5b3b22' stroke-width='3'/>",
        "<ellipse cx='240' cy='168' rx='28' ry='6' fill='#8b5e3c' stroke='#5b3b22' stroke-width='2'/>",
        "<path d='M240,166 q-14,-8 -6,-24' fill='none' stroke='#374151' stroke-width='2.5' stroke-linecap='round'/>",
        spark(234, 140),
        tl(240, 246, "Balkan = Pulverfass", 11, 900, "#3b2414"),
        # ── Fußleiste ──
        fussleiste(W, H, ["Ein Streit zwischen zwei Staaten zieht alle hinein.", "Osmanisches Reich verliert Gebiete – Ö-U und Russland streiten um Einfluss."], 34, TEXT, [11, 9.5]),
        "</g>", w=W, h=H)


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
        # Der Stoß kommt von links: der erste Stein ist am weitesten gekippt, der letzte steht noch.
        # Drehung im Uhrzeigersinn um die rechte untere Kante = Kopf fällt nach rechts auf den nächsten Stein.
        kipp = [38, 36, 32, 24, 12, 0][i]
        out.append(f"<g transform='rotate({kipp} {x + 36} 170)'><rect x='{x}' y='60' width='36' height='110' rx='6' fill='{'#fde7f3' if i == 0 else '#fff'}' stroke='{DUNKEL}' stroke-width='2'/>"
                   f"<text x='{x + 18}' y='120' font-size='10' font-weight='700' text-anchor='middle' transform='rotate(-90 {x + 18} 120)'>{escape(name)}</text></g>")
        out.append(t(x + 18, 200, datum, 11, 700, ROT))
    return svg("Die Julikrise als Kettenreaktion", t(200, 32, "Jeder Schritt löst den nächsten aus", 14, 900, DUNKEL), *out,
               arrow(10, 96, 70, 100, MAGENTA, 4), t(200, 228, "Attentat → Kriegserklärung → Mobilmachung → Krieg in ganz Europa", 10, 400, GRAU))


def ausloeser_4():
    return svg("Funke und Pulverfass",
        barrel(60, 60, 110, 120, ""), t(115, 200, "PULVERFASS = Ursachen", 12, 900, DUNKEL),
        t(115, 94, "Imperialismus", 10, 700, "#fff"), t(115, 112, "Nationalismus", 10, 700, "#fff"), t(115, 130, "Militarismus", 10, 700, "#fff"), t(115, 148, "Bündnisse", 10, 700, "#fff"),
        spark(230, 80), arrow(232, 96, 180, 120, ROT, 3, "6 4"),
        t(326, 60, "FUNKE = Auslöser", 13, 900, ROT), t(326, 80, "Attentat von Sarajevo", 12, 700), t(326, 96, "28. Juni 1914", 11, 400, GRAU),
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
