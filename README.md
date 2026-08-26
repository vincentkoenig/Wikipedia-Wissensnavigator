# Wikipedia Wissensnavigator 🧠

Ein KI-gestütztes Kommandozeilen-Tool, das Wikipedia-Artikel durchsucht, mithilfe der OpenAI API prägnante Zusammenfassungen erstellt und interaktive Multiple-Choice-Quizze generiert — alles direkt im Terminal.

> *"Wissen auf einen Blick."*

## Demo

```
================================ Welcome ================================
Please choose an option:
1. Search article
2. Exit
Enter a topic: Python (programming language)
Fetching Wikipedia article...
========================= SUMMARY =========================
Python is a high-level, general-purpose programming language known for
its clear syntax and readability...
===========================================================
Would you like a short quiz? (y/n): y
Question 1: What is Python primarily known for?
A) Low-level memory management
B) Clear syntax and readability
C) Browser-based execution
D) Compiled performance
Your answer (A/B/C/D): B
✅ Correct!
RESULT: 3/3 correct (100%)
```

## Features

- 🔎 **Intelligente Wikipedia-Suche** — verarbeitet unscharfe und mehrdeutige Suchbegriffe und schlägt Alternativen vor, wenn kein exakter Treffer gefunden wird
- 🤖 **KI-gestützte Zusammenfassungen** — lange Artikel werden über die OpenAI API zu klaren, gut lesbaren Übersichten verdichtet
- ❓ **Automatisch generierte Quizze** — Multiple-Choice-Fragen (A/B/C/D) mit einstellbarem Schwierigkeitsgrad, als JSON strukturiert für zuverlässige Verarbeitung
- 🎨 **Übersichtliche Terminal-UI** — farblich gestaltete Ausgabe mit Colorama für ein poliertes Kommandozeilen-Erlebnis
- 📊 **Strukturierte Ausgaben** — KI-Antworten werden als JSON geparst, für konsistente und zuverlässige Ergebnisse

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI_API-412991?style=flat&logo=openai&logoColor=white)
![Wikipedia](https://img.shields.io/badge/Wikipedia_API-000000?style=flat&logo=wikipedia&logoColor=white)

- **Python 3.x**
- **OpenAI API** — GPT-basierte Zusammenfassung und Quiz-Generierung
- **wikipedia** — Python-Paket zum Abrufen von Wikipedia-Artikeln
- **Colorama** — plattformübergreifende farbige Terminal-Ausgabe
- **JSON** — strukturierte Datenverarbeitung für KI-Antworten

## Projektstruktur

```
Wikipedia-Wissensnavigator/
├── main.py            # CLI-Loop, Menü, Quiz-Ablauf
├── wiki_functions.py  # Abruf von Wikipedia-Artikeln & URLs
├── openai_api.py      # OpenAI-Zusammenfassung & Quiz-Generierung
└── README.md
```

## Erste Schritte

**1. Repository klonen**
```bash
git clone https://github.com/vincentkoenig/Wikipedia-Wissensnavigator.git
cd Wikipedia-Wissensnavigator
```

**2. Virtuelle Umgebung erstellen (empfohlen)**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

**3. Abhängigkeiten installieren**
```bash
pip install openai wikipedia colorama
```

**4. OpenAI API-Key setzen**
```bash
# Windows
setx OPENAI_API_KEY "dein-api-key"
# Mac/Linux
export OPENAI_API_KEY="dein-api-key"
```

**5. App starten**
```bash
python main.py
```

## Funktionsweise

1. Ein beliebiges Thema eingeben → die App durchsucht Wikipedia und ruft den vollständigen Artikeltext ab
2. Der Artikel wird an die OpenAI API gesendet, die eine prägnante Zusammenfassung zurückgibt
3. Optional generiert die KI 3 Multiple-Choice-Quizfragen auf Basis der Zusammenfassung
4. Die Antworten werden ausgewertet und ein Ergebnis angezeigt

## Was ich gelernt habe

- Integration von Drittanbieter-APIs (OpenAI, Wikipedia) in Python
- Parsen und Verarbeiten strukturierter JSON-Antworten von KI-Modellen
- Trennung von Zuständigkeiten über mehrere Module hinweg (`main.py`, `wiki_functions.py`, `openai_api.py`)
- Entwicklung interaktiver CLI-Anwendungen inkl. Nutzereingaben und Fehlerbehandlung
- Einsatz von Colorama für plattformübergreifendes Terminal-Styling
