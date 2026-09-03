# -*- coding: utf-8 -*-
"""
chatbot.py
==========
The brain of LegalMitra.

This file contains a small SEARCH-AND-ANSWER ENGINE written completely from
scratch in plain Python. It uses NO machine-learning library - no scikit-learn,
no NLTK, no TensorFlow. Everything below is built with the standard library
only (math, re, collections), so every line can be explained in a viva.

HOW IT WORKS - the five steps
-----------------------------
1. CLEAN     : the text is lower-cased, punctuation is removed and it is split
               into words (tokens).
2. STEM      : word endings are chopped off so that "filing", "filed" and
               "file" all become "file".
3. INDEX     : every topic and document in the knowledge base is converted into
               a bag of stemmed words, and we count how often each word appears
               (Term Frequency) and in how many documents it appears
               (Document Frequency).
4. WEIGH     : each word gets a TF-IDF weight.
                   TF   = count of the word in this document / total words
                   IDF  = log(total documents / (1 + documents containing word))
                   weight = TF * IDF
               A word that appears everywhere (like "law") gets a low weight; a
               rare, meaningful word (like "gratuity") gets a high weight.
5. MATCH     : the user's question is converted into the same kind of vector and
               compared with every stored vector using COSINE SIMILARITY:

                   cos(A, B) = (A . B) / (|A| * |B|)

               Because we normalise every vector to unit length while building
               the index, the cosine is simply the dot product, which is fast.

On top of the maths there is a small INTENT LAYER that recognises greetings,
thanks, emergencies and requests for a document, so the bot behaves like a
conversation rather than a search box.

OPTIONAL AI UPGRADE
-------------------
If the `anthropic` package is installed and an ANTHROPIC_API_KEY is present in
the environment, the retrieved knowledge-base entries are passed to a Claude
model which writes the final reply (this is called RAG - Retrieval Augmented
Generation). If the key is missing, the site still works perfectly using the
offline engine below. The project is fully functional without any internet
connection or paid API.
"""

import math
import os
import re
from collections import Counter

from legal_data import (
    CATEGORIES,
    DOCUMENTS,
    EMERGENCY,
    GLOSSARY,
    HELPLINES,
    TOPICS,
    category_name,
)

# ---------------------------------------------------------------------------
# 1. TEXT CLEANING
# ---------------------------------------------------------------------------

# Words that carry no meaning for searching. Removing them stops the engine
# from matching two sentences merely because both contain "the" and "is".
STOPWORDS = {
    "a", "about", "above", "after", "again", "all", "am", "an", "and", "any",
    "are", "as", "at", "be", "because", "been", "before", "being", "below",
    "between", "both", "but", "by", "can", "cannot", "could", "did", "do",
    "does", "doing", "done", "down", "during", "each", "few", "for", "from",
    "further", "get", "got", "had", "has", "have", "having", "he", "her",
    "here", "hers", "him", "his", "how", "i", "if", "in", "into", "is", "it",
    "its", "just", "may", "me", "might", "more", "most", "must", "my", "no",
    "nor", "not", "now", "of", "off", "on", "once", "only", "or", "other",
    "our", "ours", "out", "over", "own", "please", "same", "shall", "she",
    "should", "so", "some", "such", "than", "that", "the", "their", "them",
    "then", "there", "these", "they", "this", "those", "through", "to", "too",
    "under", "until", "up", "very", "was", "we", "were", "what", "when",
    "where", "which", "while", "who", "whom", "why", "will", "with", "would",
    "you", "your", "yours", "sir", "madam", "hello", "hi", "tell", "know",
    "want", "need", "help", "give", "kindly", "regarding", "also", "am",
}

# Suffixes removed by our small stemmer, longest first so that "ations" is
# handled before "s".
SUFFIXES = [
    "ational", "iveness", "fulness", "ousness", "ization", "ations", "ement",
    "ments", "ities", "ition", "ional", "ances", "ences", "ingly", "ance",
    "ence", "ment", "tion", "sion", "ness", "ible", "able", "ally", "ies",
    "ive", "ing", "ies", "ers", "est", "ed", "ly", "es", "s",
]

TOKEN_PATTERN = re.compile(r"[a-z0-9]+")


def stem(word):
    """
    A very small suffix-stripping stemmer.

    We deliberately do not use a library. The rule is simple: remove the
    longest matching suffix, but never make the word shorter than 4 letters,
    otherwise "sale" would become "sal" and stop matching anything useful.
    """
    for suffix in SUFFIXES:
        if word.endswith(suffix) and len(word) - len(suffix) >= 4:
            return word[: -len(suffix)]
    return word


def tokenize(text):
    """Turn a sentence into a clean list of stemmed, meaningful words."""
    words = TOKEN_PATTERN.findall(text.lower())
    return [stem(w) for w in words if w not in STOPWORDS and len(w) > 1]


# ---------------------------------------------------------------------------
# 2. SYNONYMS - so everyday words find the legal words
# ---------------------------------------------------------------------------
# A visitor types "my boss fired me". The knowledge base says "termination".
# This table bridges that gap by adding the legal word to the query before it
# is searched.

SYNONYMS = {
    "fired": "termination dismissal employment",
    "sacked": "termination dismissal employment",
    "boss": "employer employment",
    "job": "employment employee",
    "salary": "wages employment payment",
    "money": "payment recovery amount",
    "cheated": "fraud cheating consumer",
    "scam": "fraud cybercrime cheating",
    "hacked": "cybercrime hacking it act",
    "stolen": "theft criminal fir",
    "theft": "theft criminal fir police",
    "beaten": "assault hurt criminal fir",
    "wife": "marriage divorce maintenance family",
    "husband": "marriage divorce maintenance family",
    "kid": "child custody minor",
    "kids": "child custody minor",
    "child": "child custody minor guardianship",
    "flat": "property apartment real estate",
    "house": "property house real estate",
    "builder": "rera promoter real estate possession",
    "landlord": "rent tenancy lease landlord",
    "tenant": "rent tenancy lease tenant",
    "shop": "business commercial establishment",
    "company": "company corporate incorporation",
    "startup": "startup company incorporation funding",
    "brand": "trademark brand logo",
    "logo": "trademark brand design",
    "copy": "copyright infringement plagiarism",
    "copied": "copyright infringement plagiarism",
    "invention": "patent invention novelty",
    "tax": "taxation income tax gst",
    "gst": "gst indirect tax registration",
    "bank": "banking loan account",
    "loan": "loan banking recovery default",
    "emi": "loan repayment default",
    "cheque": "cheque bounce 138 negotiable",
    "bounce": "cheque bounce dishonour 138",
    "accident": "accident motor compensation mact",
    "bike": "motor vehicle registration",
    "car": "motor vehicle registration insurance",
    "challan": "traffic challan penalty",
    "insurance": "insurance claim policy",
    "doctor": "medical negligence hospital",
    "hospital": "medical negligence hospital patient",
    "college": "education university student",
    "school": "education rte school admission",
    "ragging": "ragging ugc campus student",
    "pollution": "pollution environment ngt",
    "garbage": "waste management pollution",
    "tender": "tender procurement government contract",
    "contractor": "construction contract epc work",
    "arrest": "arrest bail police custody",
    "bail": "bail arrest custody",
    "fir": "fir police complaint cognizable",
    "police": "police fir complaint",
    "court": "court civil suit procedure",
    "case": "suit case litigation procedure",
    "notice": "legal notice demand",
    "will": "will succession inheritance testament",
    "property": "property real estate transfer",
    "land": "land property revenue records",
    "rent": "rent tenancy lease agreement",
    "divorce": "divorce marriage family maintenance",
    "marriage": "marriage registration family",
    "harassment": "harassment posh workplace women",
    "privacy": "privacy data protection dpdp",
    "data": "data protection privacy dpdp",
    "online": "cyber internet online it act",
    "refund": "refund consumer deficiency",
    "delivery": "consumer ecommerce goods",
    "amazon": "ecommerce consumer online marketplace",
    "flipkart": "ecommerce consumer online marketplace",
    "refugee": "refugee asylum migration",
    "rights": "fundamental rights constitution",
    "smoke": "pollution environment air ngt",
    "smell": "pollution nuisance environment",
    "noise": "pollution noise nuisance environment",
    "dumping": "waste management pollution environment",
    "factory": "pollution industry environment consent",
    "acquiring": "land acquisition compensation solatium",
    "acquisition": "land acquisition compensation rehabilitation",
    "highway": "land acquisition infrastructure road",
    "compliance": "compliance annual filing roc corporate",
    "scrutiny": "tax notice assessment appeal",
    "department": "authority government notice",
    "fraud": "fraud cheating cybercrime",
    "possession": "possession property rera delivery",
    "deposit": "security deposit tenancy refund",
}

# Words that show the visitor wants a ready-made DOCUMENT rather than an
# explanation of the law. Used both by the intent layer and by the ranking.
TEMPLATE_HINTS = (
    "template", "format", "draft", "sample", "specimen", "download",
    "how to write", "how do i write", "agreement", "deed", "letter",
    "application form", "petition", "affidavit",
)


def expand_query(text):
    """Add the legal equivalent of everyday words to the user's question."""
    lowered = text.lower()
    extras = []
    for word, replacement in SYNONYMS.items():
        if re.search(r"\b" + re.escape(word) + r"\b", lowered):
            extras.append(replacement)
    if extras:
        return text + " " + " ".join(extras)
    return text


# ---------------------------------------------------------------------------
# 3. BUILDING THE SEARCHABLE INDEX
# ---------------------------------------------------------------------------

def _topic_text(topic):
    """Flatten a topic dictionary into one long searchable string.

    The title and the keywords are repeated three times on purpose. Repeating
    a word increases its Term Frequency, which is a simple way of telling the
    engine 'these words matter more than the words buried in the body text'.
    """
    parts = [
        topic["title"], topic["title"], topic["title"],
        " ".join(topic.get("keywords", [])),
        " ".join(topic.get("keywords", [])),
        " ".join(topic.get("keywords", [])),
        category_name(topic["category"]),
        topic.get("summary", ""),
        " ".join(topic.get("key_points", [])),
        " ".join(topic.get("laws", [])),
        " ".join(topic.get("steps", [])),
    ]
    for faq in topic.get("faqs", []):
        parts.append(faq["q"])
        parts.append(faq["q"])
        parts.append(faq["a"])
    return " ".join(parts)


def _document_text(document):
    """Flatten a document template into one searchable string."""
    parts = [
        document["title"], document["title"], document["title"],
        " ".join(document.get("keywords", [])),
        " ".join(document.get("keywords", [])),
        " ".join(document.get("keywords", [])),
        "document template format draft sample agreement",
        category_name(document["category"]),
        document.get("purpose", ""),
        document.get("when_to_use", ""),
        " ".join(document.get("checklist", [])),
    ]
    return " ".join(parts)


class SearchEngine:
    """A tiny TF-IDF search engine over the legal knowledge base."""

    def __init__(self):
        self.entries = []        # metadata for each indexed item
        self.vectors = []        # the matching TF-IDF vector for each item
        self.idf = {}            # word -> inverse document frequency
        self._build()

    # -- step 1: collect every searchable item ---------------------------
    def _collect(self):
        items = []
        for topic in TOPICS:
            items.append({
                "kind": "topic",
                "id": topic["id"],
                "title": topic["title"],
                "category": topic["category"],
                "url": "/topic/" + topic["id"],
                "text": _topic_text(topic),
                "object": topic,
            })
        for document in DOCUMENTS:
            items.append({
                "kind": "document",
                "id": document["id"],
                "title": document["title"],
                "category": document["category"],
                "url": "/document/" + document["id"],
                "text": _document_text(document),
                "object": document,
            })
        return items

    # -- step 2: build the index ----------------------------------------
    def _build(self):
        items = self._collect()
        token_lists = [tokenize(item["text"]) for item in items]
        total_documents = len(items)

        # Document Frequency: in how many entries does each word appear?
        document_frequency = Counter()
        for tokens in token_lists:
            for word in set(tokens):
                document_frequency[word] += 1

        # Inverse Document Frequency. The +1 avoids a division by zero and the
        # +1 outside the log keeps every weight positive.
        self.idf = {
            word: math.log(total_documents / (1 + count)) + 1.0
            for word, count in document_frequency.items()
        }

        # TF-IDF vector for every entry, normalised to unit length.
        for item, tokens in zip(items, token_lists):
            self.entries.append(item)
            self.vectors.append(self._vectorise(tokens))

    def _vectorise(self, tokens):
        """Turn a list of words into a normalised TF-IDF dictionary."""
        if not tokens:
            return {}
        counts = Counter(tokens)
        total = len(tokens)
        vector = {}
        for word, count in counts.items():
            weight = self.idf.get(word)
            if weight is None:
                continue                      # word never seen while indexing
            vector[word] = (count / total) * weight

        # L2 normalisation: divide by the length of the vector so that a long
        # topic does not automatically beat a short one.
        length = math.sqrt(sum(value * value for value in vector.values()))
        if length == 0:
            return {}
        return {word: value / length for word, value in vector.items()}

    # -- step 3: search --------------------------------------------------
    def search(self, query, limit=5):
        """Return the best matching entries with their similarity score."""
        tokens = tokenize(expand_query(query))
        if not tokens:
            return []
        query_vector = self._vectorise(tokens)
        if not query_vector:
            return []

        # Does the visitor want a document, or an explanation of the law?
        # "give me a rent agreement format" wants the template.
        # "my landlord kept my deposit" wants the explanation.
        lowered_query = query.lower()
        wants_template = any(hint in lowered_query for hint in TEMPLATE_HINTS)

        results = []
        for entry, vector in zip(self.entries, self.vectors):
            # Cosine similarity. Both vectors are already unit length, so the
            # cosine is just the dot product of the words they share.
            score = 0.0
            if len(query_vector) < len(vector):
                for word, weight in query_vector.items():
                    if word in vector:
                        score += weight * vector[word]
            else:
                for word, weight in vector.items():
                    if word in query_vector:
                        score += weight * query_vector[word]

            # Small bonus when the question literally contains a keyword of the
            # entry. Pure TF-IDF sometimes misses an exact phrase match.
            for keyword in entry["object"].get("keywords", []):
                if keyword in lowered_query:
                    score += 0.05

            # Templates share a lot of vocabulary with the topic that explains
            # the same subject, so without this the template often wins even
            # when the visitor only wanted to understand the law. We nudge
            # documents down for explanation questions and up for format
            # requests.
            if entry["kind"] == "document":
                score *= 1.25 if wants_template else 0.72

            if score > 0:
                results.append((score, entry))

        results.sort(key=lambda pair: pair[0], reverse=True)
        return [
            {"score": round(score, 4), "entry": entry}
            for score, entry in results[:limit]
        ]


# One shared engine, built once when the server starts.
ENGINE = SearchEngine()


# ---------------------------------------------------------------------------
# 4. INTENT DETECTION
# ---------------------------------------------------------------------------

GREETING_WORDS = {"hi", "hello", "hey", "namaste", "hii", "hlo", "greetings", "yo", "hola"}
THANKS_WORDS = {"thanks", "thank", "thankyou", "thx", "shukriya", "dhanyavad"}
BYE_WORDS = {"bye", "goodbye", "exit", "quit", "see"}
EMERGENCY_WORDS = {
    "urgent", "emergency", "immediately", "right now", "arrested", "arrest",
    "help me", "danger", "threatening", "beaten", "kidnap", "suicide",
}
DOCUMENT_WORDS = {
    "template", "format", "draft", "sample", "specimen", "download",
    "how to write", "how do i write", "make a", "prepare a",
}


def detect_intent(message):
    """Work out what kind of message this is before searching for an answer."""
    text = message.lower().strip()
    words = set(TOKEN_PATTERN.findall(text))

    if not text:
        return "empty"
    if words & GREETING_WORDS and len(words) <= 3:
        return "greeting"
    if words & THANKS_WORDS:
        return "thanks"
    if words & BYE_WORDS and len(words) <= 3:
        return "bye"
    if any(phrase in text for phrase in EMERGENCY_WORDS):
        return "emergency"
    if any(phrase in text for phrase in DOCUMENT_WORDS):
        return "document"
    if text.startswith(("what is", "what are", "meaning of", "define")):
        return "definition"
    return "question"


def find_glossary_term(message):
    """If the user asked 'what is X' and X is in our glossary, return it."""
    text = message.lower()
    best = None
    for item in GLOSSARY:
        term = item["term"].lower()
        if re.search(r"\b" + re.escape(term) + r"\b", text):
            if best is None or len(term) > len(best["term"]):
                best = item
    return best


def find_emergency_card(message):
    """Match the message against the emergency quick-help cards."""
    text = message.lower()
    scores = []
    for card in EMERGENCY:
        score = 0
        for word in tokenize(card["title"]):
            if word in tokenize(text):
                score += 1
        if score:
            scores.append((score, card))
    if not scores:
        return None
    scores.sort(key=lambda pair: pair[0], reverse=True)
    return scores[0][1]


# ---------------------------------------------------------------------------
# 5. BUILDING THE ANSWER
# ---------------------------------------------------------------------------

DISCLAIMER = (
    "This is general legal information for learning, not legal advice. "
    "For your own matter please consult a qualified advocate."
)

WELCOME = (
    "Namaste! I am LegalMitra, your legal information assistant.\n\n"
    "I can explain any area of law - from criminal and property to company, "
    "cyber, consumer, labour, tax and international law - and I can give you "
    "ready-to-use document templates.\n\n"
    "Try asking me something like:\n"
    "  - What are my rights if I am arrested?\n"
    "  - My landlord is not returning my deposit\n"
    "  - How do I register a trademark?\n"
    "  - Give me a rent agreement format\n"
    "  - What is anticipatory bail?"
)


def _bullets(items, limit=None, marker="  - "):
    """Format a list of strings as plain-text bullet points."""
    chosen = items[:limit] if limit else items
    return "\n".join(marker + str(item) for item in chosen)


def build_topic_answer(topic, score):
    """Compose a readable answer out of one topic dictionary."""
    lines = []
    lines.append(topic["title"].upper())
    lines.append("Area of law: " + category_name(topic["category"]))
    lines.append("")
    lines.append(topic["summary"])

    if topic.get("key_points"):
        lines.append("")
        lines.append("KEY POINTS")
        lines.append(_bullets(topic["key_points"], limit=5))

    if topic.get("steps"):
        lines.append("")
        lines.append("WHAT YOU SHOULD DO")
        numbered = [
            "  {}. {}".format(index, step)
            for index, step in enumerate(topic["steps"][:5], start=1)
        ]
        lines.append("\n".join(numbered))

    if topic.get("laws"):
        lines.append("")
        lines.append("LAW THAT APPLIES")
        lines.append(_bullets(topic["laws"], limit=4))

    if topic.get("faqs"):
        faq = topic["faqs"][0]
        lines.append("")
        lines.append("COMMONLY ASKED")
        lines.append("  Q. " + faq["q"])
        lines.append("  A. " + faq["a"])

    return "\n".join(lines)


def build_document_answer(document):
    """Compose an answer that points the user to a document template."""
    lines = []
    lines.append(document["title"].upper())
    lines.append("Area of law: " + category_name(document["category"]))
    lines.append("")
    lines.append(document["purpose"])
    lines.append("")
    lines.append("WHEN TO USE IT")
    lines.append("  " + document["when_to_use"])
    lines.append("")
    lines.append("KEEP THIS READY BEFORE DRAFTING")
    lines.append(_bullets(document["checklist"], limit=5))
    lines.append("")
    lines.append("STAMP DUTY / REGISTRATION")
    lines.append("  " + document["stamp"])
    lines.append("")
    lines.append(
        "The full fill-in-the-blank template is on the document page, where you "
        "can also copy, print or download it."
    )
    return "\n".join(lines)


def build_emergency_answer(card):
    """Compose an urgent, action-first answer."""
    lines = []
    lines.append("URGENT: " + card["title"].upper())
    lines.append("")
    lines.append("DO THIS NOW")
    numbered = [
        "  {}. {}".format(index, step)
        for index, step in enumerate(card["immediate"], start=1)
    ]
    lines.append("\n".join(numbered))
    lines.append("")
    lines.append("DO NOT")
    lines.append(_bullets(card["do_not"]))
    lines.append("")
    lines.append("HELPLINE: " + card["helpline"])
    return "\n".join(lines)


def suggestions_for(entry):
    """Follow-up questions shown as clickable chips under the reply."""
    if entry is None:
        return [
            "What are my fundamental rights?",
            "How do I file an FIR?",
            "Give me a rent agreement format",
            "What is a cheque bounce case?",
        ]

    obj = entry["object"]
    ideas = []
    if entry["kind"] == "topic":
        for faq in obj.get("faqs", [])[:2]:
            ideas.append(faq["q"])
        same_area = [
            t for t in TOPICS
            if t["category"] == obj["category"] and t["id"] != obj["id"]
        ]
        for topic in same_area[:2]:
            ideas.append(topic["title"])
    else:
        ideas.append("What law applies to " + obj["title"] + "?")
        same_area = [
            d for d in DOCUMENTS
            if d["category"] == obj["category"] and d["id"] != obj["id"]
        ]
        for document in same_area[:2]:
            ideas.append(document["title"] + " format")
    return ideas[:4]


# ---------------------------------------------------------------------------
# 6. THE OPTIONAL AI (LLM) LAYER
# ---------------------------------------------------------------------------

# Set the environment variable ANTHROPIC_API_KEY to switch this on. Without it
# the whole website still works using the offline engine above.
AI_MODEL = "claude-opus-5"

AI_SYSTEM_PROMPT = """You are LegalMitra, a friendly legal information assistant on an educational
website about Indian law, built as a college project.

Rules you must follow:
1. Answer ONLY from the reference material given to you in the user message.
   If the reference material does not cover the question, say so honestly and
   suggest the closest topic that is covered.
2. Write in simple English that a first-year college student can follow. Short
   paragraphs and bullet points. No long legal sentences.
3. Structure the reply as: a direct answer first, then the key rules, then the
   practical steps, then the law that applies.
4. Never invent a section number, a case name or a deadline. Use only what is
   in the reference material.
5. Always end with one line reminding the reader that this is general legal
   information, not legal advice.
6. Keep the whole reply under 300 words."""


def ai_available():
    """True only if the SDK is installed AND an API key is configured."""
    if not os.environ.get("ANTHROPIC_API_KEY"):
        return False
    try:
        import anthropic  # noqa: F401
    except ImportError:
        return False
    return True


def build_context(results):
    """Turn the search results into reference text for the model to read."""
    blocks = []
    for result in results:
        entry = result["entry"]
        obj = entry["object"]
        if entry["kind"] == "topic":
            block = [
                "### TOPIC: " + obj["title"],
                "Area: " + category_name(obj["category"]),
                "Summary: " + obj["summary"],
                "Key points: " + " | ".join(obj.get("key_points", [])),
                "Steps: " + " | ".join(obj.get("steps", [])),
                "Laws: " + " | ".join(obj.get("laws", [])),
            ]
            for faq in obj.get("faqs", []):
                block.append("FAQ: " + faq["q"] + " -> " + faq["a"])
        else:
            block = [
                "### DOCUMENT TEMPLATE: " + obj["title"],
                "Purpose: " + obj["purpose"],
                "When to use: " + obj["when_to_use"],
                "Checklist: " + " | ".join(obj.get("checklist", [])),
                "Stamp duty note: " + obj["stamp"],
            ]
        blocks.append("\n".join(block))
    return "\n\n".join(blocks)


def ask_ai(question, results, history=None):
    """
    Send the retrieved knowledge to Claude and return its reply.

    Returns None if anything goes wrong, so that the caller can quietly fall
    back to the offline answer. A college demo must never crash because the
    internet is down.
    """
    try:
        import anthropic

        client = anthropic.Anthropic()

        messages = []
        for turn in (history or [])[-4:]:
            messages.append({"role": turn["role"], "content": turn["content"]})

        messages.append({
            "role": "user",
            "content": (
                "REFERENCE MATERIAL FROM THE WEBSITE'S KNOWLEDGE BASE:\n\n"
                + build_context(results)
                + "\n\n---\n\nVISITOR'S QUESTION: "
                + question
            ),
        })

        response = client.messages.create(
            model=AI_MODEL,
            max_tokens=1200,
            system=AI_SYSTEM_PROMPT,
            messages=messages,
        )

        # The model can decline a request; check before reading the text.
        if getattr(response, "stop_reason", None) == "refusal":
            return None

        parts = [
            block.text for block in response.content
            if getattr(block, "type", "") == "text"
        ]
        text = "\n".join(parts).strip()
        return text or None

    except Exception:
        # Missing key, no internet, rate limit - fall back silently.
        return None


# ---------------------------------------------------------------------------
# 7. THE MAIN ENTRY POINT USED BY app.py
# ---------------------------------------------------------------------------

def answer(message, history=None, use_ai=True):
    """
    Take the visitor's message and return a dictionary the website can render.

    The returned dictionary always has the same shape:
        {
          "answer"      : the text to display and to speak,
          "intent"      : what kind of message this was,
          "sources"     : list of pages the answer came from,
          "suggestions" : follow-up questions to show as chips,
          "engine"      : "offline" or "ai", shown as a small badge,
          "confidence"  : the similarity score of the best match
        }
    """
    message = (message or "").strip()
    intent = detect_intent(message)

    # --- conversational intents, answered without searching --------------
    if intent == "empty":
        return {
            "answer": "Please type a question and I will do my best to help.",
            "intent": intent, "sources": [], "suggestions": suggestions_for(None),
            "engine": "offline", "confidence": 0.0,
        }

    if intent == "greeting":
        return {
            "answer": WELCOME, "intent": intent, "sources": [],
            "suggestions": suggestions_for(None), "engine": "offline",
            "confidence": 1.0,
        }

    if intent == "thanks":
        return {
            "answer": (
                "You are welcome. Ask me anything else about the law - I am "
                "here to help.\n\n" + DISCLAIMER
            ),
            "intent": intent, "sources": [], "suggestions": suggestions_for(None),
            "engine": "offline", "confidence": 1.0,
        }

    if intent == "bye":
        return {
            "answer": (
                "Goodbye, and all the best. Remember: keep your documents safe, "
                "put agreements in writing, and never miss a legal deadline."
            ),
            "intent": intent, "sources": [], "suggestions": [],
            "engine": "offline", "confidence": 1.0,
        }

    # --- emergency gets an action-first answer ---------------------------
    if intent == "emergency":
        card = find_emergency_card(message)
        if card:
            related = None
            for topic in TOPICS:
                if topic["id"] == card["topic"]:
                    related = topic
                    break
            sources = []
            if related:
                sources.append({
                    "kind": "topic", "id": related["id"],
                    "title": related["title"], "url": "/topic/" + related["id"],
                })
            return {
                "answer": build_emergency_answer(card) + "\n\n" + DISCLAIMER,
                "intent": intent, "sources": sources,
                "suggestions": ["Explain " + (related["title"] if related else "my rights"),
                                "What are the national helpline numbers?"],
                "engine": "offline", "confidence": 1.0,
            }

    # --- a plain dictionary question -------------------------------------
    if intent == "definition":
        term = find_glossary_term(message)
        if term:
            results = ENGINE.search(term["term"], limit=3)
            sources = [
                {"kind": r["entry"]["kind"], "id": r["entry"]["id"],
                 "title": r["entry"]["title"], "url": r["entry"]["url"]}
                for r in results[:2]
            ]
            body = (
                term["term"].upper() + "\n\n" + term["meaning"]
            )
            if results:
                body += (
                    "\n\nYou can read more on the page: "
                    + results[0]["entry"]["title"]
                )
            return {
                "answer": body + "\n\n" + DISCLAIMER,
                "intent": intent, "sources": sources,
                "suggestions": suggestions_for(results[0]["entry"] if results else None),
                "engine": "offline",
                "confidence": 1.0,
            }

    # --- everything else goes through the search engine -------------------
    results = ENGINE.search(message, limit=8)

    # If the visitor clearly asked for a template ("format", "draft", "sample"),
    # push the document templates above the explanatory articles.
    if intent == "document":
        templates = [r for r in results if r["entry"]["kind"] == "document"]
        articles = [r for r in results if r["entry"]["kind"] != "document"]
        if templates:
            results = templates + articles
    results = results[:5]

    if not results or results[0]["score"] < 0.02:
        return {
            "answer": (
                "I could not find a confident match for that in my knowledge "
                "base.\n\nI currently cover "
                + str(len(CATEGORIES)) + " areas of law including criminal, "
                "civil, property, company, contract, labour, intellectual "
                "property, cyber, family, consumer, tax, banking, motor "
                "vehicle, environment, infrastructure, medical, education and "
                "international law.\n\nTry rephrasing with the subject you are "
                "concerned about - for example 'my employer has not paid my "
                "salary' or 'builder has delayed possession of my flat'.\n\n"
                + DISCLAIMER
            ),
            "intent": "unknown", "sources": [],
            "suggestions": suggestions_for(None),
            "engine": "offline", "confidence": 0.0,
        }

    best = results[0]["entry"]
    sources = [
        {"kind": r["entry"]["kind"], "id": r["entry"]["id"],
         "title": r["entry"]["title"], "url": r["entry"]["url"],
         "score": r["score"]}
        for r in results[:3]
    ]

    # Try the AI writer first; fall back to the offline composer.
    engine_used = "offline"
    text = None
    if use_ai and ai_available():
        text = ask_ai(message, results[:3], history=history)
        if text:
            engine_used = "ai"

    if not text:
        if best["kind"] == "topic":
            text = build_topic_answer(best["object"], results[0]["score"])
        else:
            text = build_document_answer(best["object"])

        # Mention the runner-up so the visitor knows there is more to read.
        if len(results) > 1:
            text += "\n\nRELATED PAGES\n" + _bullets(
                [r["entry"]["title"] for r in results[1:3]]
            )

    return {
        "answer": text + "\n\n" + DISCLAIMER,
        "intent": intent,
        "sources": sources,
        "suggestions": suggestions_for(best),
        "engine": engine_used,
        "confidence": results[0]["score"],
    }


# ---------------------------------------------------------------------------
# 8. COMMAND LINE TEST MODE
# ---------------------------------------------------------------------------
# Running "python chatbot.py" lets you test the engine without the website.

if __name__ == "__main__":
    print("LegalMitra offline chatbot test. Type 'quit' to exit.")
    print("AI mode:", "ON" if ai_available() else "OFF (offline engine)")
    print("Knowledge base:", len(ENGINE.entries), "searchable entries")
    print("-" * 60)
    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if user_input.lower() in {"quit", "exit"}:
            break
        reply = answer(user_input)
        print("\nLegalMitra [{}, score {}]:".format(
            reply["engine"], reply["confidence"]))
        print(reply["answer"])
