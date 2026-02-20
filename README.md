# Wikipedia-Wissensnavigator

Ein interaktives Python-Projekt, das mithilfe der OpenAI API automatisch Quizfragen aus Wikipedia-Artikeln generiert.

Ziel des Projekts ist es, Wissen intelligent aufzubereiten, automatisch Fragen zu erstellen und Inhalte verständlich zusammenzufassen – „Know it all at a glance“.

# Features

🔎 Automatische Wikipedia-Artikelsuche

Unscharfe oder mehrdeutige Suchbegriffe werden intelligent verarbeitet

Vorschläge bei nicht eindeutigen Treffern

🧾 KI-generierte Zusammenfassungen

Lange Artikel werden kompakt und verständlich dargestellt

❓ Automatische Quiz-Generierung

Multiple-Choice-Fragen (A, B, C, D)

Strukturierte JSON-Ausgabe für zuverlässige Weiterverarbeitung

🎯 Verschiedene Schwierigkeitslevel

Anpassbare Quiz-Komplexität

📊 Saubere Struktur durch Structured Outputs

KI-Antworten werden im JSON-Format verarbeitet

Klare Trennung zwischen Logik und Text

🛠️ Verwendete Technologien

Python 3.x

OpenAI API

Wikipedia API (wikipedia Python Package)

JSON für strukturierte Datenverarbeitung

Colorama (für farbige Konsolenausgabe)


# ⚙️ Installation

Repository klonen:

git clone <repository-url>
cd <repository-name>


Virtuelle Umgebung erstellen (optional, empfohlen):

python -m venv venv
venv\Scripts\activate


Abhängigkeiten installieren:

pip install openai wikipedia colorama


OpenAI API-Key als Umgebungsvariable setzen:

Windows:

setx OPENAI_API_KEY "dein_api_key"


Mac/Linux:

export OPENAI_API_KEY="dein_api_key"

# ▶️ Projekt starten
python main.py

Suchbegriff eingeben → Zusammenfassung lesen → Quiz starten → Punkte erhalten 🎉
