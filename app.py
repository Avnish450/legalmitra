# -*- coding: utf-8 -*-
"""
app.py
======
The Flask web server for LegalMitra.

This is the file you run:

    python app.py

and then open http://127.0.0.1:5000 in a browser.

Flask's job here is small and easy to follow. Each function below is tied to
one web address (a "route"). When the browser asks for that address, the
function runs, picks the right data out of the knowledge base, and hands it to
an HTML template which Flask fills in and sends back.

    URL                        WHAT IT SHOWS
    /                          home page
    /categories                all 20 branches of law
    /category/<id>             topics and templates in one branch
    /topic/<id>                one full legal topic
    /documents                 the document template library
    /document/<id>             one fill-in-the-blank template
    /document/<id>/download    the same template as a .txt file
    /chat                      the talking chatbot
    /api/chat                  the JSON endpoint the chatbot page calls
    /search                    search results
    /glossary                  A-to-Z dictionary of legal words
    /emergency                 quick-help cards
    /emergency/<id>            one quick-help card
    /helplines                 national helpline numbers
    /about                     how the project was built
    /contact                   contact form
    /stats                     usage analytics
"""

import uuid

from flask import (
    Flask,
    Response,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

import chatbot
import database
import legal_data
from legal_data import (
    CATEGORIES,
    DOCUMENTS,
    EMERGENCY,
    GLOSSARY,
    HELPLINES,
    TOPICS,
    documents_in_category,
    get_category,
    get_document,
    get_emergency,
    get_topic,
    topics_in_category,
)

app = Flask(__name__)

# Needed by Flask to sign the session cookie. In a real deployment this would
# be read from an environment variable and never committed to the repository.
app.secret_key = "legalmitra-college-project-secret-key"

# Create the database tables the first time the app starts.
database.init_db()


# ---------------------------------------------------------------------------
# THINGS EVERY PAGE NEEDS
# ---------------------------------------------------------------------------

@app.context_processor
def inject_globals():
    """Variables made available to every template automatically."""
    return {
        "site_name": "LegalMitra",
        "tagline": "Every law, explained simply.",
        "all_categories": CATEGORIES,
        "helplines": HELPLINES,
        "kb_stats": legal_data.stats(),
    }


def current_session_id():
    """Give each browser a random id so conversations can be kept apart."""
    if "sid" not in session:
        session["sid"] = uuid.uuid4().hex
    return session["sid"]


# ---------------------------------------------------------------------------
# MAIN PAGES
# ---------------------------------------------------------------------------

@app.route("/")
def home():
    featured = [
        get_topic("fundamental-rights"),
        get_topic("fir-filing"),
        get_topic("rent-and-tenancy"),
        get_topic("consumer-complaint"),
        get_topic("employee-rights"),
        get_topic("cybercrime-reporting"),
    ]
    popular_docs = [
        get_document("rental-agreement"),
        get_document("nda"),
        get_document("legal-notice"),
        get_document("will-testament"),
        get_document("offer-letter"),
        get_document("rti-application"),
    ]
    return render_template(
        "index.html",
        featured=[t for t in featured if t],
        popular_docs=[d for d in popular_docs if d],
        emergency=EMERGENCY[:6],
    )


@app.route("/categories")
def categories():
    rows = []
    for category in CATEGORIES:
        rows.append({
            "category": category,
            "topics": topics_in_category(category["id"]),
            "documents": documents_in_category(category["id"]),
        })
    return render_template("categories.html", rows=rows)


@app.route("/category/<category_id>")
def category_page(category_id):
    category = get_category(category_id)
    if not category:
        return render_template("404.html", thing="category"), 404
    return render_template(
        "category.html",
        category=category,
        topics=topics_in_category(category_id),
        documents=documents_in_category(category_id),
    )


@app.route("/topic/<topic_id>")
def topic_page(topic_id):
    topic = get_topic(topic_id)
    if not topic:
        return render_template("404.html", thing="topic"), 404

    related = [
        t for t in topics_in_category(topic["category"])
        if t["id"] != topic_id
    ][:3]
    related_docs = documents_in_category(topic["category"])[:3]

    return render_template(
        "topic.html",
        topic=topic,
        category=get_category(topic["category"]),
        related=related,
        related_docs=related_docs,
    )


# ---------------------------------------------------------------------------
# DOCUMENT TEMPLATES
# ---------------------------------------------------------------------------

@app.route("/documents")
def documents():
    selected = request.args.get("category", "").strip()
    if selected:
        shown = documents_in_category(selected)
    else:
        shown = DOCUMENTS
    used_categories = [
        c for c in CATEGORIES if documents_in_category(c["id"])
    ]
    return render_template(
        "documents.html",
        documents=shown,
        used_categories=used_categories,
        selected=selected,
    )


@app.route("/document/<document_id>")
def document_page(document_id):
    document = get_document(document_id)
    if not document:
        return render_template("404.html", thing="document"), 404
    related = [
        d for d in documents_in_category(document["category"])
        if d["id"] != document_id
    ][:3]
    return render_template(
        "document.html",
        document=document,
        category=get_category(document["category"]),
        related=related,
    )


@app.route("/document/<document_id>/download")
def document_download(document_id):
    """Send the template to the browser as a plain .txt file."""
    document = get_document(document_id)
    if not document:
        return render_template("404.html", thing="document"), 404

    header = (
        "=" * 74 + "\n"
        + document["title"].upper().center(74) + "\n"
        + "=" * 74 + "\n\n"
        + "PURPOSE      : " + document["purpose"] + "\n"
        + "WHEN TO USE  : " + document["when_to_use"] + "\n\n"
        + "STAMP DUTY / REGISTRATION\n"
        + document["stamp"] + "\n\n"
        + "BEFORE YOU START, KEEP READY\n"
        + "\n".join("  - " + item for item in document["checklist"]) + "\n\n"
        + "-" * 74 + "\n"
        + "Replace every [SQUARE BRACKET] with your own details.\n"
        + "-" * 74 + "\n\n"
    )

    footer = (
        "\n\n" + "-" * 74 + "\n"
        + "Generated by LegalMitra - an academic project.\n"
        + "This is a sample draft for learning, NOT legal advice. Stamp duty and\n"
        + "registration rules differ from state to state. Have a qualified\n"
        + "advocate review any document before you sign it.\n"
        + "-" * 74 + "\n"
    )

    content = header + document["body"] + footer
    filename = document_id + ".txt"

    return Response(
        content,
        mimetype="text/plain; charset=utf-8",
        headers={"Content-Disposition": "attachment; filename=" + filename},
    )


# ---------------------------------------------------------------------------
# CHATBOT
# ---------------------------------------------------------------------------

@app.route("/chat")
def chat_page():
    current_session_id()
    return render_template(
        "chat.html",
        ai_on=chatbot.ai_available(),
        starters=[
            "What are my rights if I am arrested?",
            "My landlord is not returning my security deposit",
            "How do I register a trademark?",
            "Give me a rent agreement format",
            "Builder has delayed possession of my flat",
            "My employer has not paid my salary",
            "A cheque given to me has bounced",
            "How do I file an RTI application?",
        ],
    )


@app.route("/api/chat", methods=["POST"])
def api_chat():
    """
    The chat page sends the visitor's message here as JSON and gets the
    reply back as JSON. This is the only part of the site that the browser
    talks to in the background.
    """
    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()
    session_id = current_session_id()

    if not message:
        return jsonify({"error": "Please type a question."}), 400

    history = database.session_history(session_id, limit=3)
    reply = chatbot.answer(message, history=history)

    top_source = reply["sources"][0]["title"] if reply["sources"] else ""
    database.save_chat(
        session_id=session_id,
        question=message,
        answer=reply["answer"],
        intent=reply["intent"],
        engine=reply["engine"],
        confidence=reply["confidence"],
        top_source=top_source,
    )

    return jsonify(reply)


@app.route("/api/clear", methods=["POST"])
def api_clear():
    """Start a fresh conversation by issuing a new session id."""
    session["sid"] = uuid.uuid4().hex
    return jsonify({"ok": True})


# ---------------------------------------------------------------------------
# SEARCH, GLOSSARY, EMERGENCY
# ---------------------------------------------------------------------------

@app.route("/search")
def search():
    query = request.args.get("q", "").strip()
    results = []
    if query:
        found = chatbot.ENGINE.search(query, limit=20)
        for item in found:
            entry = item["entry"]
            obj = entry["object"]
            results.append({
                "kind": entry["kind"],
                "title": entry["title"],
                "url": entry["url"],
                "category": legal_data.category_name(entry["category"]),
                "score": item["score"],
                "snippet": obj.get("summary") or obj.get("purpose", ""),
            })
        database.save_search(query, len(results))

    glossary_hits = []
    if query:
        lowered = query.lower()
        glossary_hits = [
            g for g in GLOSSARY
            if lowered in g["term"].lower() or lowered in g["meaning"].lower()
        ][:5]

    return render_template(
        "search.html",
        query=query,
        results=results,
        glossary_hits=glossary_hits,
    )


@app.route("/glossary")
def glossary():
    letter = request.args.get("letter", "").upper()
    terms = sorted(GLOSSARY, key=lambda item: item["term"].lower())
    if letter:
        terms = [t for t in terms if t["term"].upper().startswith(letter)]
    available = sorted({t["term"][0].upper() for t in GLOSSARY})
    return render_template(
        "glossary.html",
        terms=terms,
        letters=available,
        selected=letter,
    )


@app.route("/emergency")
def emergency():
    return render_template("emergency.html", cards=EMERGENCY)


@app.route("/emergency/<card_id>")
def emergency_card(card_id):
    card = get_emergency(card_id)
    if not card:
        return render_template("404.html", thing="quick-help card"), 404
    return render_template(
        "emergency_card.html",
        card=card,
        topic=get_topic(card["topic"]),
    )


@app.route("/helplines")
def helplines_page():
    return render_template("helplines.html")


# ---------------------------------------------------------------------------
# ABOUT, CONTACT, ANALYTICS
# ---------------------------------------------------------------------------

@app.route("/about")
def about():
    return render_template("about.html", ai_on=chatbot.ai_available())


@app.route("/contact", methods=["GET", "POST"])
def contact():
    sent = False
    error = ""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        subject = request.form.get("subject", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            error = "Name, email and message are required."
        elif "@" not in email or "." not in email:
            error = "Please enter a valid email address."
        else:
            database.save_contact(name, email, subject, message)
            sent = True

    return render_template("contact.html", sent=sent, error=error)


@app.route("/stats")
def stats_page():
    return render_template(
        "stats.html",
        totals=database.counts(),
        popular=database.popular_questions(10),
        topics_hit=database.popular_topics(10),
        recent=database.recent_chats(10),
        kb=legal_data.stats(),
        indexed=len(chatbot.ENGINE.entries),
        ai_on=chatbot.ai_available(),
    )


# ---------------------------------------------------------------------------
# ERROR PAGES
# ---------------------------------------------------------------------------

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html", thing="page"), 404


@app.errorhandler(500)
def server_error(error):
    return render_template("404.html", thing="page (server error)"), 500


# ---------------------------------------------------------------------------
# START THE SERVER
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 62)
    print(" LegalMitra - Legal Information Portal with AI Chatbot")
    print("=" * 62)
    summary = legal_data.stats()
    print(" Categories        :", summary["categories"])
    print(" Legal topics      :", summary["topics"])
    print(" Document templates:", summary["documents"])
    print(" Glossary terms    :", summary["glossary"])
    print(" Indexed entries   :", len(chatbot.ENGINE.entries))
    print(" AI mode           :", "ON" if chatbot.ai_available() else "OFF (offline engine)")
    print("-" * 62)
    print(" Open your browser at:  http://127.0.0.1:5000")
    print(" Press CTRL+C to stop the server")
    print("=" * 62)
    app.run(debug=True, host="0.0.0.0", port=5000)
