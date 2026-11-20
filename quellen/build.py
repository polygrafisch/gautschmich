"""Baut die Startseite index.html aus template.html, lehrplan.json und materialien.json.

Aufruf (im Repository-Ordner):  python3 quellen/build.py
Benötigt: Python 3 mit Pillow und numpy (pip install pillow numpy)
"""
import base64, json, math, pathlib
import numpy as np
from PIL import Image

QUELLEN = pathlib.Path(__file__).parent
REPO = QUELLEN.parent

html = (QUELLEN / "template.html").read_text(encoding="utf-8")

def b64(datei):
    return base64.b64encode((QUELLEN / "fonts" / datei).read_bytes()).decode()

# Pixel-Brille, 26 x 5 Raster
karte = [
    "##########################",
    "  ##ww######  ##ww######  ",
    "  #ww#######  #ww#######  ",
    "   ########    ########   ",
    "    ######      ######    ",
]
rects = []
for y, zeile in enumerate(karte):
    for x, c in enumerate(zeile):
        if c in "#w":
            farbe = "#0b0710" if c == "#" else "#ffffff"
            rects.append(f'<rect x="{x}" y="{y}" width="1.02" height="1.02" fill="{farbe}"/>')

# Tonwerte des Gutenberg-Porträts vorberechnen (0 = Papier, 255 = volle Farbe).
# So muss der Browser keine Canvas-Pixel auslesen (Fingerprint-Schutz).
GW = 256
bild = Image.open(QUELLEN / "gutenberg.jpg").convert("L")
GH = round(GW * bild.height / bild.width)
l = np.asarray(bild.resize((GW, GH), Image.BOX), dtype=float) / 255
schwarz, weiss = np.quantile(l, 0.04), np.quantile(l, 0.88)
dunkel = np.clip((weiss - l) / max(0.05, weiss - schwarz), 0, 1)
ton = (dunkel * 255).round().astype(np.uint8).tobytes()

def json_einbetten(pfad):
    return pfad.read_text(encoding="utf-8").replace("</", "<\\/")

html = (html.replace("__HEROS_REGULAR__", b64("heros-regular.woff2"))
            .replace("__HEROS_BOLD__", b64("heros-bold.woff2"))
            .replace("__HEROS_ITALIC__", b64("heros-italic.woff2"))
            .replace("__BRILLE__", "".join(rects))
            .replace("__GW__", str(GW)).replace("__GH__", str(GH))
            .replace("__TONWERTE__", base64.b64encode(ton).decode())
            .replace("__LEHRPLAN__", json_einbetten(QUELLEN / "lehrplan.json"))
            .replace("__MATERIALIEN__", json_einbetten(REPO / "materialien.json")))

ziel = REPO / "index.html"
ziel.write_text(html, encoding="utf-8")
print(ziel, len(html) // 1024, "KB")
