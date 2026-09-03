# -*- coding: utf-8 -*-
"""
database.py
===========
All the SQLite work for LegalMitra, kept in one small file.

We use SQLite because it needs no server, no password and no installation -
Python already ships with it. The whole database is a single file called
legalmitra.db which is created automatically the first time the site runs.

THREE TABLES
------------
chat_log      every question asked and the answer given, so we can show
              analytics and so a conversation can be reviewed later
search_log    every search made from the search box
contact_msg   messages sent through the Contact page

Nothing personal is stored - there is no login and no name unless the visitor
types one into the contact form.
"""

import os
import sqlite3
from datetime import datetime

def _db_path():
    """Where the database file lives.

    Normally it sits next to the code. But on a serverless host such as
    Vercel the application folder is READ ONLY and the only writable place
    is /tmp, so the database goes there instead. Data in /tmp is temporary
    and disappears when the instance is recycled, which is acceptable
    because we only store usage logs, never anything a user needs back.
    """
    serverless = os.environ.get("VERCEL") or os.environ.get("AWS_LAMBDA_FUNCTION_NAME")
    if serverless:
        return os.path.join("/tmp", "legalmitra.db")
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "legalmitra.db")


DB_FILE = _db_path()


def get_connection():
    """Open a connection that returns rows we can access by column name."""
    connection = sqlite3.connect(DB_FILE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    """Create the tables if they do not already exist. Safe to call every run."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_log (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id  TEXT    NOT NULL,
            question    TEXT    NOT NULL,
            answer      TEXT    NOT NULL,
            intent      TEXT,
            engine      TEXT,
            confidence  REAL,
            top_source  TEXT,
            created_at  TEXT    NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS search_log (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            query       TEXT    NOT NULL,
            results     INTEGER NOT NULL,
            created_at  TEXT    NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contact_msg (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            name        TEXT    NOT NULL,
            email       TEXT    NOT NULL,
            subject     TEXT,
            message     TEXT    NOT NULL,
            created_at  TEXT    NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def _now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ---------------------------------------------------------------------------
# WRITING
# ---------------------------------------------------------------------------

def save_chat(session_id, question, answer, intent, engine, confidence, top_source):
    """Store one question-and-answer pair."""
    connection = get_connection()
    connection.execute(
        """INSERT INTO chat_log
           (session_id, question, answer, intent, engine, confidence,
            top_source, created_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (session_id, question, answer, intent, engine, confidence,
         top_source, _now()),
    )
    connection.commit()
    connection.close()


def save_search(query, result_count):
    """Store one search-box query."""
    connection = get_connection()
    connection.execute(
        "INSERT INTO search_log (query, results, created_at) VALUES (?, ?, ?)",
        (query, result_count, _now()),
    )
    connection.commit()
    connection.close()


def save_contact(name, email, subject, message):
    """Store one message from the Contact page."""
    connection = get_connection()
    connection.execute(
        """INSERT INTO contact_msg (name, email, subject, message, created_at)
           VALUES (?, ?, ?, ?, ?)""",
        (name, email, subject, message, _now()),
    )
    connection.commit()
    connection.close()


# ---------------------------------------------------------------------------
# READING
# ---------------------------------------------------------------------------

def recent_chats(limit=20):
    """The most recent conversations, newest first."""
    connection = get_connection()
    rows = connection.execute(
        "SELECT * FROM chat_log ORDER BY id DESC LIMIT ?", (limit,)
    ).fetchall()
    connection.close()
    return [dict(row) for row in rows]


def session_history(session_id, limit=10):
    """The last few turns of one visitor's conversation, oldest first.

    This is what gives the chatbot a short memory, so a follow-up question
    like "and what if he refuses?" still makes sense.
    """
    connection = get_connection()
    rows = connection.execute(
        """SELECT question, answer FROM chat_log
           WHERE session_id = ? ORDER BY id DESC LIMIT ?""",
        (session_id, limit),
    ).fetchall()
    connection.close()

    history = []
    for row in reversed(rows):
        history.append({"role": "user", "content": row["question"]})
        history.append({"role": "assistant", "content": row["answer"]})
    return history


def popular_questions(limit=10):
    """The questions asked most often - used on the analytics page."""
    connection = get_connection()
    rows = connection.execute(
        """SELECT question, COUNT(*) AS times
           FROM chat_log
           GROUP BY LOWER(question)
           ORDER BY times DESC, question ASC
           LIMIT ?""",
        (limit,),
    ).fetchall()
    connection.close()
    return [dict(row) for row in rows]


def popular_topics(limit=10):
    """Which knowledge-base pages the chatbot answered from most often."""
    connection = get_connection()
    rows = connection.execute(
        """SELECT top_source, COUNT(*) AS times
           FROM chat_log
           WHERE top_source IS NOT NULL AND top_source <> ''
           GROUP BY top_source
           ORDER BY times DESC
           LIMIT ?""",
        (limit,),
    ).fetchall()
    connection.close()
    return [dict(row) for row in rows]


def counts():
    """Simple totals for the analytics page."""
    connection = get_connection()
    chats = connection.execute("SELECT COUNT(*) FROM chat_log").fetchone()[0]
    searches = connection.execute("SELECT COUNT(*) FROM search_log").fetchone()[0]
    messages = connection.execute("SELECT COUNT(*) FROM contact_msg").fetchone()[0]
    sessions = connection.execute(
        "SELECT COUNT(DISTINCT session_id) FROM chat_log"
    ).fetchone()[0]
    unanswered = connection.execute(
        "SELECT COUNT(*) FROM chat_log WHERE intent = 'unknown'"
    ).fetchone()[0]
    connection.close()
    return {
        "chats": chats,
        "searches": searches,
        "messages": messages,
        "sessions": sessions,
        "unanswered": unanswered,
    }


if __name__ == "__main__":
    init_db()
    print("Database ready at:", DB_FILE)
    print("Totals:", counts())
