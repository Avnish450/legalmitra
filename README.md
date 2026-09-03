# LegalMitra — Legal Information Portal with a Voice-Enabled AI Chatbot

A second-year engineering mini project.
Python + Flask + SQLite + plain HTML/CSS/JavaScript. **No TypeScript, no React, no build step.**

---

## What it does

| Feature | Description |
|---|---|
| **20 areas of law** | Constitutional, criminal, civil, corporate, contract, labour, IPR, cyber, family, property, infrastructure, environment, consumer, taxation, banking, motor vehicles, human rights & international, startup, medical, education |
| **80 legal topics** | Each with a summary, key points, step-by-step procedure, the Acts that apply, and FAQs |
| **31 document templates** | Rent agreement, sale deed, NDA, will, legal notice, affidavit, POA, consumer complaint, RTI, and more — every blank marked in `[SQUARE BRACKETS]` |
| **71-term glossary** | A-to-Z dictionary of legal words |
| **10 emergency cards** | "What to do right now" for arrest, online fraud, domestic violence, accidents, etc. |
| **Talking chatbot** | Ask by **voice or text**; it searches, explains, and **speaks the answer aloud** |
| **Search engine** | TF-IDF + cosine similarity, written from scratch — no ML library |
| **Analytics page** | Live counts read from the SQLite database |

---

## Quick start

```bash
# 1. Install the two dependencies
pip install -r requirements.txt

# 2. Run the server
python app.py

# 3. Open in a browser
http://127.0.0.1:5000
```

On Windows you can simply double-click **`run.bat`**.

> Use **Chrome or Edge** for the chatbot — the microphone and the speaking voice
> use the browser's built-in Web Speech API, which Firefox does not fully support.

---

## Project structure

```
poorvi legal/
├── app.py                  Flask server — one function per web page
├── chatbot.py              The search-and-answer engine (TF-IDF, cosine similarity, intents)
├── database.py             SQLite tables and queries
│
├── legal_data.py           Categories + helper functions; joins the knowledge base
├── legal_topics.py         Topics part 1 (10 branches of law)
├── legal_topics_extra.py   Topics part 2 (10 branches of law)
├── legal_documents.py      31 fill-in-the-blank document templates
├── legal_extras.py         Glossary, emergency cards, helpline numbers
│
├── templates/              16 Jinja2 HTML pages (base.html is the common layout)
├── static/css/style.css    All styling, hand-written, no framework
├── static/js/chat.js       Chatbot + speech recognition + speech synthesis
├── static/js/main.js       Navigation, copy/print, filters, page reader
│
├── docs/make_report.py     Builds the project report PDF with ReportLab
├── docs/LegalMitra_Project_Report.pdf
│
├── requirements.txt
├── run.bat                 Windows one-click launcher
└── legalmitra.db           SQLite database (created automatically on first run)
```

---

## How the chatbot works

No pre-trained model is used in the default mode. Six steps:

1. **Clean** — lowercase, strip punctuation, split into words
2. **Stem** — chop word endings so *filing / filed / file* all match
3. **Expand** — map everyday words to legal ones (*"boss fired me"* → *termination*)
4. **Weigh** — TF-IDF: `TF × IDF`, where `IDF = log(N / (1 + df)) + 1`
5. **Match** — cosine similarity against all 111 indexed entries; vectors are
   pre-normalised, so the cosine is just a dot product
6. **Compose** — build a structured answer: explanation → key points → steps → law

An **intent layer** on top handles greetings, thanks, emergencies, definitions
and requests for a document format differently from an ordinary question.

### Optional AI mode

Set an API key and the retrieved entries are passed to a Claude model that
writes the reply in natural language (Retrieval Augmented Generation):

```bash
# Windows
set ANTHROPIC_API_KEY=your-key-here
pip install anthropic
python app.py
```

The model is instructed to use **only** the supplied knowledge base, so it
cannot invent a section number. If the key is missing, the internet is down, or
the API errors, the site silently falls back to the offline engine — **it never
crashes during a demo.**

---

## Voice features

| Direction | Technology | Where |
|---|---|---|
| Speech → text | `webkitSpeechRecognition` (`en-IN`) | Microphone button on the chat page |
| Text → speech | `window.speechSynthesis` | Answers are read aloud; voice and speed are selectable |
| Page reader | `speechSynthesis` | "Listen to this page" button on topic pages |

Both run **inside the browser**. No paid speech service, no API key, no internet.

---

## Database

SQLite, created automatically as `legalmitra.db`:

| Table | Purpose |
|---|---|
| `chat_log` | Every question and answer, with intent, engine used and confidence score |
| `search_log` | Every search-box query and how many results it returned |
| `contact_msg` | Messages sent from the Contact page |

No login, no personal data — nothing is stored unless the visitor types it.

---

## Regenerating the project report PDF

```bash
python docs/make_report.py
```

This rebuilds `docs/LegalMitra_Project_Report.pdf` — cover page, abstract, system
architecture diagrams, DFDs, ER diagram, module descriptions, the chatbot
algorithm with worked calculations, code listings, a 25-case test table, results,
limitations, future scope and the week-by-week development log.

---

## Testing

```bash
python legal_data.py    # prints the knowledge-base coverage table
python chatbot.py       # command-line chatbot, no browser needed
python database.py      # creates the database and prints the totals
```

---

## Disclaimer

This is an **academic project**. The content is simplified for learning and is
**not legal advice**. Statutes are amended often and many rules — especially
stamp duty, tenancy and court fees — differ from State to State. Always consult a
qualified advocate before acting on anything here.
