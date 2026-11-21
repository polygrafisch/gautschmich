# gautschmi.ch – Anleitung für Claude

gautschmi.ch ist Marco Knobels Website mit selbst gemachtem Lernmaterial für Polygrafinnen und Polygrafen EFZ an der Schule für Gestaltung Zürich. Zielpublikum sind die Lernenden.

## Sprache
- Deutsch mit Schweizer Rechtschreibung: ss statt ß, Anführungszeichen «…» und ‹…›.
- Lernende direkt und freundlich ansprechen, kurz und klar.
- Dezimalkomma (7,5), Tausendertrennung mit Apostroph (1'200).

## Gestaltung
- Schrift: TeX Gyre Heros, als WOFF2-Subset in die HTML-Datei eingebettet. Gewichte: 400, 700, 400 kursiv.
- Keine Kästen und Container. Linien statt Boxen, Abgrenzung über Schriftstärke und Weissraum.
- Kein Orange. Keine Versal-Spitztitel (kleine gesperrte Grossbuchstaben). Keine Mittelpunkte (·) als Trennzeichen.
- Zurückhaltend. Pop-Elemente gibt es nur auf der Startseite (Rasterporträt von Gutenberg, Pixelbrille).

### Farben
| Rolle | Wert |
|---|---|
| Pink (Riso Fluorescent Pink, Startseite) | #ff48b0 |
| Schwarz | #111111 |
| Weiss | #ffffff |

Handlungskompetenzbereiche (Linie / Text / Hintergrundton / heller Ton):
| Bereich | Kurzname | Linie | Text | Ton 13 % | Ton 7 % |
|---|---|---|---|---|---|
| a | Marketing | #d9ad0b | #9c7c00 | #faf4df | #fcf9ee |
| b | Mediengestaltung | #c4453d | #b03a33 | #f7e7e6 | #fbf2f1 |
| c | Typografische Konzepte | #3f8a5a | #357a4e | #e6f0ea | #f2f7f3 |
| d | Bild und Grafik | #3a6aa8 | #2f5c96 | #e5ecf4 | #f1f5f9 |
| e | Deutsch | #8a5c3e | #7a5034 | #f0eae6 | #f7f4f1 |
| f | Medienproduktion | #7c52a3 | #6d4692 | #eee9f3 | #f6f3f9 |

Material zu einem Bereich darf dessen Farbe dezent als Akzent verwenden: Linie, Kennbuchstabe oder heller Hintergrundton eines Titels.

### Typografie
- Grosse Titel: 700, enge Laufweite (−0,01 bis −0,03 em), Zeilenabstand um 1,0.
- Fliesstext: 400, 1 bis 1,2 rem, Zeilenabstand 1,4 bis 1,5, Zeilen höchstens etwa 46 em breit.
- Hilfstexte: kleiner, Deckkraft 0,55 bis 0,7.
- Trennlinien: 1,5 px Schwarz für Hauptgliederung, 1 px mit 10 bis 20 % Schwarz für Unterteilungen.

## Technik
- Jedes Material ist eine einzelne, in sich geschlossene HTML-Datei: Schrift, Bilder und Daten eingebettet, keine externen Abhängigkeiten. Sie läuft lokal per Doppelklick und auf dem Server. Einzige Ausnahme ist der Besuchszähler GoatCounter im Fusszeilen-Baustein. Er zählt nur online und ist für die Funktion nicht nötig.
- Keine Canvas-Pixel auslesen (getImageData). LibreWolf und Firefox mit Fingerprint-Schutz blockieren das. Daten lieber beim Erstellen vorberechnen.
- Mobil tauglich (ab 360 px Breite), Tastatur bedienbar, prefers-reduced-motion respektieren.
- Browser-Speicher (localStorage) nur für Kleinigkeiten wie Spielstand, immer mit try/catch.
- Favicon: Jedes Material übernimmt im `<head>` direkt nach `<title>` die Zeile `<link rel="icon" …>` aus `quellen/template.html` (pinkes Quadrat mit schwarzem Punkt, als Data-URI). Sonst zeigt der Browser ein altes, zwischengespeichertes Icon der Domain. Im Stamm liegt zusätzlich `favicon.ico` als Rückfall.
- Kopfzeile: Oben rechts im Kopf jedes Materials steht der Link «zurück zu gautschmi.ch» (`https://gautschmi.ch/`), fett, in der Textfarbe des Bereichs, mit dem Ton 13 % hinterlegt; beim Überfahren Bereichslinie als Hintergrund und weisse Schrift. Links daneben der Kennbuchstabe und das Leistungsziel. Auf den Materialseiten steht sichtbar «gautschmich» ohne Punkt, also «zurück zu gautschmich». Die Startseite nimmt den Punkt nur zurück (`.gm-pkt`).
- Fusszeile: Jedes Lernmaterial endet mit dem Baustein `quellen/fusszeile.html`, unverändert übernommen (HTML, CSS und Skript). Er enthält «**gautschmich** Alle Angaben ohne Gewähr. Es gelten die jeweiligen Schullehrpläne.», «Inhalte beitragen», «Fehler melden» und «zurück zu gautschmich». Die Mailadresse wird erst beim Klick per JavaScript zusammengesetzt und darf nie im Quelltext stehen. Der Betreff enthält automatisch den Seitentitel (`<title>`), darum jedem Material einen treffenden Titel geben.

## Aufbau des Repositorys
```
index.html            Startseite, wird gebaut, nie von Hand bearbeiten
materialien.json      Liste aller Lernmaterialien
material/<kurzname>/  ein Lernmaterial pro Ordner, darin index.html (in sich geschlossen)
quellen/              Bauteile der Startseite: template.html, build.py, lehrplan.json,
                      gutenberg.jpg, fonts/ (TeX Gyre Heros als WOFF2-Subset)
CNAME                 Domain gautschmi.ch für GitHub Pages
.nojekyll             GitHub Pages liefert die Dateien unverändert aus
```

## Neues Lernmaterial einhängen
1. Material als `material/<kurzname>/index.html` ablegen. Kurzname klein, ohne Umlaute, mit Bindestrichen, z. B. `satzspiegel-quiz`.
2. Eintrag in `materialien.json` ergänzen:
   ```json
   { "titel": "Satzspiegel-Quiz", "pfad": "material/satzspiegel-quiz/", "art": "Lernspiel",
     "leistungsziele": ["c2.1"], "lehrjahre": [2] }
   ```
   Externe Materialien (z. B. Gimkit, Kahoot) bekommen als `pfad` die volle URL (`https://…`). Die Startseite öffnet sie dann in einem neuen Tab und zeigt ↗ an.
   `leistungsziele` gemäss `quellen/lehrplan.json`. `lehrjahre` darf leer sein, dann erscheint das Material in allen Lehrjahren des Leistungsziels.
3. Startseite neu bauen: `python3 quellen/build.py` (braucht Pillow und numpy).
4. Im Browser prüfen: Das Material erscheint beim aufgeklappten Leistungsziel unter «Material».
5. Commit mit kurzer deutscher Nachricht, dann push auf `main`. GitHub Pages veröffentlicht automatisch.

Ans Ende jedes Materials gehört der Baustein `quellen/fusszeile.html` (siehe Technik).

## Grundlage
Schullehrplan Polygrafin/Polygraf EFZ der SfG Zürich, Version 4.1.2026, ohne Blocktage. Die Daten in `quellen/lehrplan.json` wurden aus dem PDF ausgelesen und von Hand bereinigt.
