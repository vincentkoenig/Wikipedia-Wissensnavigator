# Wikipedia Knowledge Navigator 🧠

An AI-powered command-line tool that searches Wikipedia articles, generates concise summaries using the OpenAI API, and creates interactive multiple-choice quizzes — all in your terminal.

> *"Know it all at a glance."*

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

- 🔎 **Smart Wikipedia search** — handles fuzzy and ambiguous search terms, suggests alternatives when no exact match is found
- 🤖 **AI-powered summaries** — long articles condensed into clear, readable overviews via OpenAI API
- ❓ **Auto-generated quizzes** — multiple-choice questions (A/B/C/D) with adjustable difficulty, structured as JSON for reliable processing
- 🎨 **Clean terminal UI** — color-coded output with Colorama for a polished command-line experience
- 📊 **Structured outputs** — AI responses parsed as JSON for consistent, reliable results

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI_API-412991?style=flat&logo=openai&logoColor=white)
![Wikipedia](https://img.shields.io/badge/Wikipedia_API-000000?style=flat&logo=wikipedia&logoColor=white)

- **Python 3.x**
- **OpenAI API** — GPT-based summarization and quiz generation
- **wikipedia** — Python package for Wikipedia article retrieval
- **Colorama** — cross-platform colored terminal output
- **JSON** — structured data processing for AI responses

## Project Structure

```
Wikipedia-Wissensnavigator/
├── main.py            # CLI loop, menu, quiz runner
├── wiki_functions.py  # Wikipedia article fetching & URL retrieval
├── openai_api.py      # OpenAI summarization & quiz generation
└── README.md
```

## Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/vincentkoenig/Wikipedia-Wissensnavigator.git
cd Wikipedia-Wissensnavigator
```

**2. Create a virtual environment (recommended)**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install openai wikipedia colorama
```

**4. Set your OpenAI API key**
```bash
# Windows
setx OPENAI_API_KEY "your-api-key"

# Mac/Linux
export OPENAI_API_KEY="your-api-key"
```

**5. Run the app**
```bash
python main.py
```

## How It Works

1. Enter any topic → the app searches Wikipedia and retrieves the full article text
2. The article is sent to the OpenAI API, which returns a concise summary
3. Optionally, the AI generates 3 multiple-choice quiz questions based on the summary
4. Your answers are evaluated and a score is displayed

## What I Learned

- Integrating third-party APIs (OpenAI, Wikipedia) in Python
- Parsing and working with structured JSON responses from AI models
- Separating concerns across multiple modules (`main.py`, `wiki_functions.py`, `openai_api.py`)
- Building interactive CLI applications with user input handling and error cases
- Using Colorama for cross-platform terminal styling
