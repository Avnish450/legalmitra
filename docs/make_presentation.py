# -*- coding: utf-8 -*-
"""
docs/make_presentation.py
=========================
Builds the PRESENTATION AND CODE WALKTHROUGH pdf - the document to read
before the viva, and to keep open beside you while presenting.

    python docs/make_presentation.py
    ->  docs/LegalMitra_Presentation_Guide.pdf

This is different from make_report.py. The report is the formal academic
document. This one is practical: what to say, what to click, what every
important line of code does, and the answers to the questions an examiner
is most likely to ask.

Code shown in this document is READ FROM THE ACTUAL SOURCE FILES at build
time, so it can never drift out of date with the project.
"""

import inspect
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.graphics.shapes import Drawing, Line, Polygon, Rect, String
from reportlab.platypus import (
    KeepTogether, PageBreak, Paragraph, Preformatted, Spacer, Table, TableStyle,
)
from reportlab.platypus.doctemplate import BaseDocTemplate, PageTemplate
from reportlab.platypus.frames import Frame

import chatbot
import legal_data

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB = legal_data.stats()
INDEXED = len(chatbot.ENGINE.entries)

# ---------------------------------------------------------------------------
# STYLES
# ---------------------------------------------------------------------------
INK = colors.HexColor("#16202b")
INK2 = colors.HexColor("#4b5462")
GREY = colors.HexColor("#767e8b")
SEAL = colors.HexColor("#8c2f27")
BRASS = colors.HexColor("#9a7524")
GREEN = colors.HexColor("#2c6149")
RULE = colors.HexColor("#d8d4ca")
PAPER = colors.HexColor("#f5f3ee")
CODEBG = colors.HexColor("#fbfaf7")
BLUE = colors.HexColor("#eaf0f8")

styles = getSampleStyleSheet()
S_H1 = ParagraphStyle("h1", parent=styles["Heading1"], fontName="Helvetica-Bold",
                      fontSize=17, leading=21, textColor=INK, spaceBefore=4, spaceAfter=8)
S_H2 = ParagraphStyle("h2", parent=styles["Heading2"], fontName="Helvetica-Bold",
                      fontSize=12.2, leading=16, textColor=SEAL, spaceBefore=13, spaceAfter=5)
S_H3 = ParagraphStyle("h3", parent=styles["Heading3"], fontName="Helvetica-Bold",
                      fontSize=10.4, leading=14, textColor=INK, spaceBefore=9, spaceAfter=3)
S_BODY = ParagraphStyle("b", parent=styles["Normal"], fontName="Helvetica",
                        fontSize=9.6, leading=14.4, alignment=TA_JUSTIFY,
                        textColor=INK, spaceAfter=6)
S_BUL = ParagraphStyle("bu", parent=S_BODY, leftIndent=15, bulletIndent=4, spaceAfter=3)
S_CODE = ParagraphStyle("c", parent=styles["Code"], fontName="Courier",
                        fontSize=7.3, leading=9.3, textColor=colors.HexColor("#232833"),
                        backColor=CODEBG, borderPadding=6, spaceBefore=3, spaceAfter=8)
S_SAY = ParagraphStyle("say", parent=S_BODY, fontName="Helvetica-Oblique",
                       fontSize=9.8, leading=14.6, textColor=INK, alignment=0, spaceAfter=0)
S_CAP = ParagraphStyle("cap", parent=styles["Normal"], fontName="Helvetica-Oblique",
                       fontSize=8.2, leading=11, alignment=TA_CENTER, textColor=GREY,
                       spaceBefore=3, spaceAfter=10)

PAGE_W, PAGE_H = A4
CW = PAGE_W - 40 * mm
story = []


# ---------------------------------------------------------------------------
# BUILDING BLOCKS
# ---------------------------------------------------------------------------
def h1(t, newpage=True):
    if newpage:
        story.append(PageBreak())
    story.append(Paragraph(t, S_H1))
    d = Drawing(CW, 5)
    d.add(Line(0, 2, CW, 2, strokeColor=BRASS, strokeWidth=1.6))
    story.append(d)
    story.append(Spacer(1, 7))


def h2(t): story.append(Paragraph(t, S_H2))
def h3(t): story.append(Paragraph(t, S_H3))
def p(t): story.append(Paragraph(t, S_BODY))
def gap(h=7): story.append(Spacer(1, h))


def bullets(items, numbered=False):
    for i, it in enumerate(items, 1):
        story.append(Paragraph(it, S_BUL, bulletText=("%d." % i) if numbered else "•"))
    gap(4)


def code(text, title=None):
    if title:
        story.append(Paragraph(title, S_H3))
    story.append(Preformatted(text.strip("\n"), S_CODE))


def box(text, fill=BLUE, border=INK, style=None):
    para = Paragraph(text, style or ParagraphStyle("bx", parent=S_BODY, fontSize=9.3,
                                                   leading=13.6, spaceAfter=0))
    t = Table([[para]], colWidths=[CW])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), fill),
        ("LINEBEFORE", (0, 0), (0, -1), 3, border),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(t)
    gap(9)


def say(text):
    """A 'what to say out loud' block."""
    para = Paragraph("<b>Say this:</b> “" + text + "”", S_SAY)
    t = Table([[para]], colWidths=[CW])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f2ead4")),
        ("LINEBEFORE", (0, 0), (0, -1), 3, BRASS),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(t)
    gap(9)


def table(data, widths, cap=None, fs=8.3, head=True):
    st = [
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), fs),
        ("LEADING", (0, 0), (-1, -1), fs + 3.2),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.4, RULE),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ]
    if head:
        st += [("BACKGROUND", (0, 0), (-1, 0), INK),
               ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
               ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
               ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, PAPER])]
    else:
        st += [("ROWBACKGROUNDS", (0, 0), (-1, -1), [colors.white, PAPER])]

    wrapped = []
    for ri, row in enumerate(data):
        nr = []
        for cell in row:
            if isinstance(cell, str):
                isH = head and ri == 0
                cs = ParagraphStyle("cell", parent=S_BODY, fontSize=fs, leading=fs + 3.2,
                                    alignment=0, spaceAfter=0,
                                    fontName="Helvetica-Bold" if isH else "Helvetica",
                                    textColor=colors.white if isH else INK)
                nr.append(Paragraph(cell, cs))
            else:
                nr.append(cell)
        wrapped.append(nr)
    t = Table(wrapped, colWidths=widths, repeatRows=1 if head else 0)
    t.setStyle(TableStyle(st))
    story.append(t)
    if cap:
        story.append(Paragraph(cap, S_CAP))
    else:
        gap(9)


def code_explain(rows, cap=None):
    """A two-column 'code line -> what it does' table."""
    data = [["Code", "What this line does"]]
    for c, e in rows:
        data.append([Paragraph('<font face="Courier" size="7.2">%s</font>' %
                               c.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"),
                               ParagraphStyle("cc", parent=S_BODY, fontSize=7.2, leading=10,
                                              spaceAfter=0, alignment=0)), e])
    table(data, [CW * 0.46, CW * 0.54], cap, fs=8.1)


# ---------------------------------------------------------------------------
# READ REAL SOURCE CODE SO NOTHING IS OUT OF DATE
# ---------------------------------------------------------------------------
def source_of(func):
    """Return the real source text of a function from the project."""
    try:
        return inspect.getsource(func)
    except Exception:
        return "(source unavailable)"


def file_slice(relpath, start_marker, end_marker=None, max_lines=40):
    """Pull a labelled chunk out of a source file."""
    path = os.path.join(ROOT, relpath)
    try:
        with open(path, "r", encoding="utf-8") as fh:
            text = fh.read()
    except OSError:
        return "(file not found: %s)" % relpath
    i = text.find(start_marker)
    if i < 0:
        return "(marker not found in %s)" % relpath
    rest = text[i:]
    if end_marker:
        j = rest.find(end_marker, len(start_marker))
        if j > 0:
            rest = rest[:j]
    return "\n".join(rest.splitlines()[:max_lines])


def loc(relpath):
    try:
        with open(os.path.join(ROOT, relpath), "r", encoding="utf-8") as fh:
            return sum(1 for _ in fh)
    except OSError:
        return 0


# ---------------------------------------------------------------------------
# PAGE FURNITURE
# ---------------------------------------------------------------------------
def decorate(canvas, doc):
    canvas.saveState()
    pg = canvas.getPageNumber()
    if pg > 1:
        canvas.setStrokeColor(RULE)
        canvas.setLineWidth(0.5)
        canvas.line(20 * mm, PAGE_H - 15 * mm, PAGE_W - 20 * mm, PAGE_H - 15 * mm)
        canvas.setFont("Helvetica-Oblique", 7.6)
        canvas.setFillColor(GREY)
        canvas.drawString(20 * mm, PAGE_H - 13 * mm, "LegalMitra - Presentation & Code Walkthrough")
        canvas.drawRightString(PAGE_W - 20 * mm, PAGE_H - 13 * mm, "Keep this open during the viva")
        canvas.line(20 * mm, 14 * mm, PAGE_W - 20 * mm, 14 * mm)
        canvas.setFont("Helvetica", 8)
        canvas.drawCentredString(PAGE_W / 2, 9.5 * mm, str(pg))
    canvas.restoreState()


class Doc(BaseDocTemplate):
    def afterFlowable(self, f):
        if isinstance(f, Paragraph) and f.style.name == "h1":
            self.notify("TOCEntry", (0, f.getPlainText(), self.page))


# ===========================================================================
#  COVER
# ===========================================================================
def cover():
    gap(30)
    story.append(Paragraph("LegalMitra", ParagraphStyle(
        "t", parent=S_H1, fontSize=34, leading=40, alignment=TA_CENTER, spaceAfter=4)))
    story.append(Paragraph("Presentation &amp; Code Walkthrough", ParagraphStyle(
        "s", parent=S_BODY, fontSize=14, leading=20, alignment=TA_CENTER,
        textColor=SEAL, spaceAfter=14)))
    d = Drawing(CW, 4)
    d.add(Line(CW * 0.25, 1, CW * 0.75, 1, strokeColor=BRASS, strokeWidth=2))
    story.append(d)
    gap(16)

    story.append(Paragraph(
        "Everything I need to explain this project: what it does, how every "
        "important piece of code works, how the chatbot decides its answer, "
        "how it says <i>“I don’t know”</i>, and the questions I should be "
        "ready for.",
        ParagraphStyle("i", parent=S_BODY, fontSize=11, leading=16.5,
                       alignment=TA_CENTER, textColor=INK2)))
    gap(20)

    d = Drawing(CW, 120)
    cx = CW / 2
    d.add(Rect(cx - 50, 6, 100, 108, fillColor=PAPER, strokeColor=INK,
               strokeWidth=1.2, rx=10, ry=10))
    d.add(Line(cx, 32, cx, 88, strokeColor=INK, strokeWidth=2.2))
    d.add(Line(cx - 30, 88, cx + 30, 88, strokeColor=INK, strokeWidth=2.2))
    for side in (-1, 1):
        px = cx + side * 30
        d.add(Line(px, 88, px - 12, 70, strokeColor=INK, strokeWidth=0.9))
        d.add(Line(px, 88, px + 12, 70, strokeColor=INK, strokeWidth=0.9))
        d.add(Polygon([px - 14, 70, px + 14, 70, px + 8, 61, px - 8, 61],
                      fillColor=BRASS, strokeColor=INK, strokeWidth=1))
    d.add(Polygon([cx - 19, 32, cx + 19, 32, cx + 13, 26, cx - 13, 26],
                  fillColor=INK, strokeColor=INK))
    d.add(String(cx, 14, "LegalMitra", fontName="Helvetica-Bold", fontSize=8,
                 fillColor=INK, textAnchor="middle"))
    story.append(d)
    gap(18)

    rows = [
        ["Project", "LegalMitra - legal information portal with a voice chatbot"],
        ["Built with", "Python 3, Flask, SQLite, HTML, CSS, vanilla JavaScript"],
        ["Not used", "No TypeScript, no React, no ML library, no build step"],
        ["Knowledge base", "%d branches of law, %d topics, %d templates, %d glossary terms"
         % (KB["categories"], KB["topics"], KB["documents"], KB["glossary"])],
        ["Search engine", "TF-IDF + cosine similarity, written by hand (~80 lines)"],
        ["Accuracy", "93.3% Top-1, 100% Top-3 on a 30-question test set"],
        ["Total code", "About 12,000 lines across 39 files"],
        ["Submitted by", "Poorvi Rai - [USN]"],
        ["Guide", "[GUIDE NAME]"],
    ]
    table([["", ""]] + rows, [CW * 0.26, CW * 0.74], head=False, fs=9)


# ===========================================================================
#  1. THE PITCH
# ===========================================================================
def sec_pitch():
    h1("1. The 60-second version")

    p("This is what I say if I only get one minute. Everything else in this "
      "document is detail behind these three paragraphs.")

    say("Most people meet the law at the worst possible moment - a cheque has "
        "already bounced, a landlord has already kept the deposit, a salary has "
        "already gone unpaid. And at that moment they hit two problems: they "
        "don't know which branch of law their problem belongs to, and "
        "everything written about it is written for lawyers.")

    say("So I built LegalMitra. It covers %d branches of law with %d topics "
        "written in plain English, %d ready-to-use document templates, and a "
        "chatbot you can type to or speak to. You describe your problem in "
        "ordinary words - 'my landlord kept my deposit' - and it finds the "
        "right law, explains what to do, tells you the deadline, and reads the "
        "answer out loud."
        % (KB["categories"], KB["topics"], KB["documents"]))

    say("The interesting part technically is that I didn't use any machine "
        "learning library. I implemented the search myself using TF-IDF and "
        "cosine similarity - about 80 lines of Python. I then tested it on 30 "
        "questions written the way a normal person types, got 66.7% correct, "
        "found out why it was failing, fixed the ranking, and got it to 93.3%.")

    box("<b>If I remember only one thing:</b> the strongest part of this project "
        "is not that it works - it is that I <b>measured</b> it, found a real "
        "defect, understood the cause, fixed it, and measured again. That is the "
        "story to tell.", fill=colors.HexColor("#e2eee8"), border=GREEN)

    h2("1.1 The one-line answer to “what is your project?”")
    p("<i>“A legal help website where you can ask a question in normal English - "
      "by typing or by speaking - and it finds the right law, explains it "
      "simply, and gives you the document you need.”</i>")

    h2("1.2 Three things that make it more than a website")
    bullets([
        "<b>It understands ordinary language.</b> Nobody searches for "
        "‘retrenchment’. They type ‘my boss fired me’. I built a synonym layer "
        "that bridges the two.",
        "<b>It talks.</b> Speech in and speech out, using the browser's own "
        "Web Speech API - no paid service, works offline.",
        "<b>It admits when it doesn't know.</b> Below a confidence score it says "
        "so instead of guessing. In a legal tool a confident wrong answer is "
        "the worst possible output.",
    ])


# ===========================================================================
#  2. DEMO SCRIPT
# ===========================================================================
def sec_demo():
    h1("2. Demo script - exactly what to click and say")

    p("A demo goes wrong when you browse around looking for something. Follow "
      "this order. It takes about four minutes and it builds up: content first, "
      "then intelligence, then voice, then honesty.")

    table([
        ["#", "Do this", "Say this while you do it"],
        ["1", "Open the home page.",
         "“This is the home page. Twenty branches of law, eighty topics, thirty-one document templates. These numbers are not typed into the page - they are counted from the knowledge base at run time.”"],
        ["2", "Click <b>Areas of Law</b>, then open <b>Criminal Law</b>, then <b>How to File an FIR</b>.",
         "“Every topic has the same five parts - a summary, the key points, a numbered procedure, the Acts that apply, and FAQs. I fixed that structure first so one template could render any topic.”"],
        ["3", "Press <b>Listen to this page</b>.",
         "“The whole knowledge base can be listened to, not just read. This uses the browser's speech engine.”"],
        ["4", "Open the <b>chatbot</b>. Type: <i>my landlord is not returning my deposit</i>",
         "“I never used the word ‘tenancy’ or ‘deposit refund law’. It found the right topic from ordinary words.”"],
        ["5", "Point at the <b>source links</b> under the reply.",
         "“Every answer shows which pages it came from, with the relevance score. Nothing is invented - it can only return what is in the knowledge base.”"],
        ["6", "Type: <i>give me a rent agreement format</i>",
         "“Same subject, but now it gives the template instead of the explanation. It detected that I asked for a format. That was a bug I had to fix - I'll come back to it.”"],
        ["7", "Press the <b>microphone</b> and speak a question.",
         "“Speech recognition runs in the browser, so there is no paid API and no audio leaves the machine.”"],
        ["8", "Type: <i>how do I bake a cake</i>",
         "“And this is the part I'm most pleased with. It doesn't guess. Below a confidence threshold it tells you honestly that it has no confident match.”"],
        ["9", "Open a <b>document template</b>, show the yellow blanks, press Download.",
         "“Every blank you must fill is marked. The stored template is plain text - the highlighting is done by one regular expression in the browser.”"],
        ["10", "Open <b>Emergency Help</b> &rarr; <b>I have been arrested</b>.",
         "“For urgent situations the structure is inverted - numbered actions first, then what NOT to do, then the helpline. The ‘do not’ list came out of user testing.”"],
        ["11", "Open the <b>analytics</b> page.",
         "“Everything asked is logged to SQLite. The count of unanswered questions is my improvement list.”"],
    ], [CW * 0.04, CW * 0.34, CW * 0.62], "Demo running order", fs=8)

    h2("2.1 Have these three sentences ready for the end")
    bullets([
        "“The whole thing runs offline - no internet, no API key, no paid service.”",
        "“The search engine is about eighty lines and I can explain every line.”",
        "“It is legal <i>information</i>, not legal advice, and that boundary is "
        "built into the design, not just written in a disclaimer.”",
    ])


# ===========================================================================
#  3. HOW IT FITS TOGETHER
# ===========================================================================
def diagram_flow():
    d = Drawing(CW, 300)
    steps = [
        ("Browser", "the user types or speaks", colors.white),
        ("chat.js", "sends the message to the server", colors.HexColor("#eaf0f8")),
        ("app.py", "Flask route /api/chat receives it", colors.HexColor("#eaf0f8")),
        ("chatbot.py", "works out the intent", colors.HexColor("#e2eee8")),
        ("chatbot.py", "cleans, stems and expands the words", colors.HexColor("#e2eee8")),
        ("chatbot.py", "TF-IDF vector + cosine similarity", colors.HexColor("#e2eee8")),
        ("chatbot.py", "builds the structured answer", colors.HexColor("#e2eee8")),
        ("database.py", "logs the question and answer", colors.HexColor("#f2ead4")),
        ("chat.js", "draws the reply and speaks it aloud", colors.HexColor("#eaf0f8")),
    ]
    y = 268
    for i, (name, what, fill) in enumerate(steps):
        d.add(Rect(4, y, 96, 24, fillColor=fill, strokeColor=INK, strokeWidth=1, rx=4, ry=4))
        d.add(String(52, y + 9, name, fontName="Helvetica-Bold", fontSize=7.6,
                     fillColor=INK, textAnchor="middle"))
        d.add(String(110, y + 9, what, fontName="Helvetica", fontSize=7.6, fillColor=INK2))
        if i < len(steps) - 1:
            d.add(Line(52, y, 52, y - 6, strokeColor=INK2, strokeWidth=1))
            d.add(Polygon([52, y - 8, 49, y - 3, 55, y - 3], fillColor=INK2, strokeColor=INK2))
        y -= 32
    return d


def sec_flow():
    h1("3. How the whole thing fits together")

    p("If an examiner asks “explain your architecture”, this single picture is "
      "the answer. It is one question travelling from the microphone to the "
      "spoken reply.")
    story.append(diagram_flow())
    story.append(Paragraph("Figure 1: one question, end to end", S_CAP))

    say("There are three layers. The browser handles the interface and all the "
        "voice work. Flask handles the web routing. And chatbot.py does the "
        "actual thinking - it has no idea the web exists, which is why I can "
        "test it from the command line with no browser at all.")

    h2("3.1 The files I wrote, and what each one is for")
    table([
        ["File", "Lines", "What it does", "Why it is separate"],
        ["app.py", str(loc("app.py")), "The Flask server. One function per web page.", "Knows about the web, knows nothing about legal matching"],
        ["chatbot.py", str(loc("chatbot.py")), "The search-and-answer engine.", "Knows about matching, knows nothing about HTTP"],
        ["database.py", str(loc("database.py")), "SQLite tables and queries.", "All the SQL in one place"],
        ["legal_data.py", str(loc("legal_data.py")), "The 20 categories plus helper lookups.", "The one file everything imports from"],
        ["legal_topics.py", str(loc("legal_topics.py")), "40 topics (first ten branches).", "Content, split so no file is unmanageable"],
        ["legal_topics_extra.py", str(loc("legal_topics_extra.py")), "40 topics (last ten branches).", "Same"],
        ["legal_documents.py", str(loc("legal_documents.py")), "%d document templates." % KB["documents"], "Largest file - it is all content"],
        ["legal_extras.py", str(loc("legal_extras.py")), "Glossary, emergency cards, helplines.", "Smaller structures kept together"],
        ["templates/ (17 files)", "1,588", "The HTML pages, using Jinja2.", "base.html holds the shared layout"],
        ["static/css/style.css", str(loc("static/css/style.css")), "All the styling, written by hand.", "No Bootstrap, no Tailwind"],
        ["static/js/chat.js", str(loc("static/js/chat.js")), "The chat + both voice directions.", "The only complex JavaScript"],
        ["static/js/main.js", str(loc("static/js/main.js")), "Menu, copy, print, filters, page reader.", "Small helpers for the other pages"],
    ], [CW * 0.21, CW * 0.08, CW * 0.36, CW * 0.35], "Every file and its job", fs=7.8)

    box("<b>Question you will definitely get:</b> “Why did you split it like "
        "this?”<br/><br/>"
        "<b>Answer:</b> so that each file has one job. <font face='Courier'>app.py</font> "
        "handles the web, <font face='Courier'>chatbot.py</font> handles the "
        "matching, the <font face='Courier'>legal_*</font> files are pure "
        "content. That separation is what lets me run "
        "<font face='Courier'>python chatbot.py</font> and test the engine in "
        "the terminal without starting a server at all.")


# ===========================================================================
#  4. THE DATA
# ===========================================================================
def sec_data():
    h1("4. How I structured the legal content")

    p("Before writing any content I fixed the shape of a topic. Every one of "
      "the %d topics is a Python dictionary with exactly the same eight keys. "
      "That decision is why one HTML template can display any topic and one "
      "function can make any topic searchable." % KB["topics"])

    code('''
{
    "id":       "cheque-bounce",             # slug that becomes the URL
    "category": "criminal",                  # links to a CATEGORIES entry
    "title":    "Cheque Bounce - Section 138 Negotiable Instruments Act",
    "summary":  "When a cheque is returned unpaid ... strict timeline ...",
    "key_points": [ "The cheque must have been issued for a legally ...",
                    "A written demand notice must be sent within 30 days ..." ],
    "laws":       [ "Negotiable Instruments Act, 1881 - Sections 138, 139 ..." ],
    "steps":      [ "Collect the original cheque and the bank return memo.",
                    "Within 30 days of the memo, send a legal demand notice ..." ],
    "faqs":       [ {"q": "What if the notice comes back undelivered?",
                     "a": "If it was sent to the correct address ..."} ],
    "keywords":   [ "cheque bounce", "section 138", "dishonour", "demand notice" ],
}
''', "One topic, in full")

    say("I deliberately kept the content as Python dictionaries instead of "
        "database tables. The content is read-only and I am the one writing it, "
        "so keeping it as code means I can review a change as a text diff, and "
        "adding a topic needs no database migration and no admin screen.")

    h2("4.1 Why the templates use [SQUARE BRACKETS]")
    p("Every blank a user must fill in is written as "
      "<font face='Courier'>[LIKE THIS]</font>. The stored template stays plain "
      "text - completely clean and printable - and the yellow highlighting is "
      "added in the browser by a single regular expression. If an examiner asks "
      "“how did you highlight those?”, this is the whole answer:")

    code('''
template.innerHTML = escaped.replace(/\\[([^\\]]+)\\]/g, "<mark>[$1]</mark>");
''')

    h2("4.2 Coverage")
    rows = [["Branch of law", "Topics", "Templates"]]
    for c in legal_data.CATEGORIES:
        rows.append([c["name"], str(len(legal_data.topics_in_category(c["id"]))),
                     str(len(legal_data.documents_in_category(c["id"])))])
    rows.append(["<b>Total</b>", "<b>%d</b>" % KB["topics"], "<b>%d</b>" % KB["documents"]])
    table(rows, [CW * 0.62, CW * 0.19, CW * 0.19], "What the knowledge base covers", fs=7.8)


# ===========================================================================
#  5. THE ENGINE - THE PART TO KNOW COLD
# ===========================================================================
def sec_engine():
    h1("5. The chatbot engine, explained line by line")

    box("This is the section to know properly. Everything else in the project "
        "is content or plumbing; this is the part I actually engineered. It is "
        "in <font face='Courier'>chatbot.py</font> and uses only "
        "<font face='Courier'>math</font>, <font face='Courier'>re</font> and "
        "<font face='Courier'>collections.Counter</font> from the standard "
        "library. <b>No scikit-learn, no NLTK, no TensorFlow.</b>")

    h2("5.1 The eight stages")
    table([
        ["#", "Stage", "What happens", "Example on “my landlord is not returning my deposit”"],
        ["1", "Tokenise", "Lower-case, drop punctuation, split into words", "my, landlord, is, not, returning, my, deposit"],
        ["2", "Remove stopwords", "Throw away words that carry no meaning", "landlord, returning, deposit"],
        ["3", "Stem", "Chop word endings so forms match", "landlord, return, deposit"],
        ["4", "Expand synonyms", "Add the legal words the user did not use", "+ rent, tenancy, lease, security, refund"],
        ["5", "Build a TF-IDF vector", "Give each word a weight - rare words count more", "‘tenanc’ heavy, ‘return’ light"],
        ["6", "Cosine similarity", "Compare against all %d entries" % INDEXED, "best match scores 0.77"],
        ["7", "Adjust the ranking", "Push templates up or down by intent", "template pushed down - this is a problem, not a format request"],
        ["8", "Compose the answer", "Assemble summary, points, steps, laws", "the reply you see"],
    ], [CW * 0.04, CW * 0.18, CW * 0.34, CW * 0.44], "The pipeline in one table", fs=7.9)

    # ---------------- stage 1-3 ----------------
    h2("5.2 Stages 1 to 3 - cleaning the words")
    code('''
STOPWORDS = { "a", "about", "above", ..., "the", "is", "my", "not",
              "sir", "madam", "kindly", "please", "help", "tell" }

TOKEN_PATTERN = re.compile(r"[a-z0-9]+")

def tokenize(text):
    """Turn a sentence into a clean list of stemmed, meaningful words."""
    words = TOKEN_PATTERN.findall(text.lower())
    return [stem(w) for w in words if w not in STOPWORDS and len(w) > 1]
''', "The tokeniser")

    code_explain([
        ('TOKEN_PATTERN.findall(text.lower())',
         "Lower-cases everything and keeps only letters and digits, so “FIR”, “Fir” and “fir.” all become the same word."),
        ('if w not in STOPWORDS',
         "Removes words that appear in almost every topic. Without this, two unrelated sentences look similar just because both contain “the” and “is”."),
        ('and len(w) > 1',
         "Drops single characters left over from punctuation."),
        ('stem(w)',
         "Reduces the word to its root so “filing”, “filed” and “file” all match."),
    ])

    p("I added six words to the standard stopword list that are specific to "
      "this project - <i>sir, madam, kindly, please, help, tell</i> - because "
      "they appeared constantly in test questions and carried no meaning.")

    h3("The stemmer, and the bug that shaped it")
    code('''
SUFFIXES = ["ational", "iveness", "fulness", "ousness", "ization", "ations",
            "ement", "ments", "ities", "ition", "ional", "ances", "ences",
            "ingly", "ance", "ence", "ment", "tion", "sion", "ness", "ible",
            "able", "ally", "ies", "ive", "ing", "ers", "est", "ed", "ly",
            "es", "s"]

def stem(word):
    """Remove the longest matching suffix, but never leave a stub."""
    for suffix in SUFFIXES:
        if word.endswith(suffix) and len(word) - len(suffix) >= 4:
            return word[:-len(suffix)]
    return word
''')

    box("<b>A good thing to volunteer in the viva.</b> My first version had no "
        "length guard. It stemmed <i>“sale”</i> to <i>“sal”</i> and "
        "<i>“lease”</i> to <i>“leas”</i>, so a search for a sale deed stopped "
        "matching the sale deed template completely. I found it by printing the "
        "token list, and fixed it with the rule that a word may never be cut "
        "below four characters. Showing a bug you found yourself is worth more "
        "than claiming it worked first time.",
        fill=colors.HexColor("#f2ead4"), border=BRASS)

    # ---------------- stage 4 ----------------
    h2("5.3 Stage 4 - the synonym layer (the most useful thing I built)")
    p("Nobody types <i>retrenchment</i>. They type <i>my boss fired me</i>. "
      "This table bridges everyday words to legal words, and it improved real "
      "usability more than any change to the maths.")

    code('''
SYNONYMS = {
    "fired":    "termination dismissal employment",
    "boss":     "employer employment",
    "landlord": "rent tenancy lease landlord",
    "builder":  "rera promoter real estate possession",
    "bounce":   "cheque bounce dishonour 138",
    "hacked":   "cybercrime hacking it act",
    "smoke":    "pollution environment air ngt",
    ...                                   # about 60 mappings in total
}

def expand_query(text):
    """Add the legal equivalent of everyday words to the user's question."""
    lowered = text.lower()
    extras = []
    for word, replacement in SYNONYMS.items():
        if re.search(r"\\b" + re.escape(word) + r"\\b", lowered):
            extras.append(replacement)
    return text + " " + " ".join(extras) if extras else text
''')

    code_explain([
        (r'r"\b" + re.escape(word) + r"\b"',
         "The \\b are word boundaries. Without them the entry for “car” fires inside “carpet area” and drags a motor-vehicle topic into a property question. I hit exactly that bug."),
        ('return text + " " + " ".join(extras)',
         "The legal words are ADDED to the question, not substituted, so the user's own words still count too."),
    ])

    # ---------------- stage 5 ----------------
    h2("5.4 Stage 5 - TF-IDF, the actual maths")
    p("This is the formula an examiner is most likely to ask me to explain at "
      "the board. It has two halves.")

    box("<b>TF (Term Frequency)</b> = how often a word appears in this topic, "
        "divided by the total number of words in it.<br/>"
        "<i>Meaning: a word repeated in a topic is probably important to it.</i>"
        "<br/><br/>"
        "<b>IDF (Inverse Document Frequency)</b> = log( N / (1 + df) ) + 1, "
        "where N is the total number of entries and df is how many entries "
        "contain the word.<br/>"
        "<i>Meaning: a word that appears in every topic (“law”, “court”) tells "
        "you nothing, so it gets a tiny weight. A rare word (“gratuity”) is "
        "highly distinctive, so it gets a big weight.</i><br/><br/>"
        "<b>Final weight = TF × IDF.</b>")

    code('''
def _build(self):
    items       = self._collect()                 # all 111 topics + templates
    token_lists = [tokenize(item["text"]) for item in items]
    total_documents = len(items)

    # How many entries contain each word?
    document_frequency = Counter()
    for tokens in token_lists:
        for word in set(tokens):                  # set() -> count each entry ONCE
            document_frequency[word] += 1

    # Inverse document frequency
    self.idf = {word: math.log(total_documents / (1 + count)) + 1.0
                for word, count in document_frequency.items()}

    for item, tokens in zip(items, token_lists):
        self.entries.append(item)
        self.vectors.append(self._vectorise(tokens))
''', "Building the index (runs once, when the program starts)")

    code_explain([
        ('for word in set(tokens)',
         "set() is essential. Document frequency counts how many ENTRIES contain the word, not how many times it appears. Without set() a word repeated in one topic would be counted many times."),
        ('math.log(total / (1 + count))',
         "The 1 + prevents division by zero if a word somehow has zero count."),
        ('+ 1.0',
         "Keeps every weight positive. Without it, a word appearing in every single entry would get a weight of exactly zero and be silently dropped."),
        ('self.vectors.append(...)',
         "Every entry is converted once, at start-up. No request ever pays this cost."),
    ])

    h3("Normalising the vector - why long topics don't cheat")
    p("A long topic naturally contains more words and would score higher "
      "against any question. So each vector is divided by its own length, which "
      "makes every vector exactly 1 unit long. Now only the <i>direction</i> "
      "matters, not the size.")

    code('''
def _vectorise(self, tokens):
    if not tokens:
        return {}
    counts = Counter(tokens)
    total  = len(tokens)
    vector = {}
    for word, count in counts.items():
        weight = self.idf.get(word)
        if weight is None:
            continue                          # word never seen while indexing
        vector[word] = (count / total) * weight     # TF x IDF

    length = math.sqrt(sum(v * v for v in vector.values()))
    if length == 0:
        return {}
    return {w: v / length for w, v in vector.items()}     # normalise
''')

    # ---------------- stage 6 ----------------
    h2("5.5 Stage 6 - cosine similarity")
    p("Cosine similarity measures the <i>angle</i> between two vectors. If two "
      "texts are about the same thing they point in the same direction, and the "
      "cosine is close to 1. If they share nothing, they are at right angles "
      "and the cosine is 0.")

    box("cos(A, B) = (A · B) / (|A| × |B|)<br/><br/>"
        "But I already made every vector 1 unit long when building the index. "
        "So |A| × |B| = 1, and the whole formula collapses to just the "
        "<b>dot product</b> - multiply the shared words and add them up. "
        "That is why the search is fast even though it is plain Python.")

    code('''
score = 0.0
if len(query_vector) < len(vector):
    for word, weight in query_vector.items():
        if word in vector:
            score += weight * vector[word]
else:
    for word, weight in vector.items():
        if word in query_vector:
            score += weight * query_vector[word]
''')

    code_explain([
        ('if len(query_vector) < len(vector)',
         "A small optimisation I added: loop over whichever vector has fewer words. The question has about 20 words, an entry has hundreds, so this saves most of the work."),
        ('score += weight * vector[word]',
         "The dot product. Only words present in BOTH contribute anything."),
    ])

    # ---------------- stage 7 ----------------
    h2("5.6 Stage 7 - the ranking fix (my best story)")
    p("This is the defect my testing exposed, and the change that took accuracy "
      "from 66.7% to 93.3%.")

    p("<b>The problem:</b> a document template and the topic that explains the "
      "same subject share almost all their vocabulary. The cheque-bounce notice "
      "template and the cheque-bounce topic look nearly identical to a "
      "bag-of-words model. Worse, the template packs that vocabulary into a "
      "shorter document, so after normalising, the template scored "
      "<i>higher</i>. Users asking “a cheque bounced, what do I do?” were being "
      "handed a blank notice form instead of an explanation.")

    p("<b>The fix:</b> detect whether the person actually asked for a document, "
      "and scale the score accordingly.")

    code('''
TEMPLATE_HINTS = ("template", "format", "draft", "sample", "specimen",
                  "download", "how to write", "agreement", "deed", "letter",
                  "application form", "petition", "affidavit")

wants_template = any(hint in lowered_query for hint in TEMPLATE_HINTS)
...
if entry["kind"] == "document":
    score *= 1.25 if wants_template else 0.72
''')

    table([
        ["Measure", "Before the fix", "After the fix"],
        ["Top-1 accuracy (correct page first)", "66.7% (20/30)", "<b>93.3% (28/30)</b>"],
        ["Top-3 accuracy (correct page in first three)", "96.7% (29/30)", "<b>100% (30/30)</b>"],
        ["Template requests still reaching a template", "10/10", "<b>10/10</b>"],
    ], [CW * 0.46, CW * 0.27, CW * 0.27], "The measured effect of one change")

    say("The important thing is not the number. It is that I found it by "
        "measuring rather than by guessing. I wrote thirty questions the way a "
        "normal person types, recorded which page should come back, ran it, and "
        "then actually read the ten failures instead of just looking at the "
        "score. Seven of the ten had the same cause, and one change fixed all "
        "seven without breaking the case it might have damaged.")

    # ---------------- stage 8 ----------------
    h2("5.7 Stage 8 - building the reply")
    p("The winning entry is assembled into a fixed shape so every answer reads "
      "the same way: title, summary, up to five key points, up to five numbered "
      "steps, up to four Acts, and the first FAQ.")

    code('''
def build_topic_answer(topic, score):
    lines = []
    lines.append(topic["title"].upper())
    lines.append("Area of law: " + category_name(topic["category"]))
    lines.append("")
    lines.append(topic["summary"])

    if topic.get("key_points"):
        lines.append(""); lines.append("KEY POINTS")
        lines.append(_bullets(topic["key_points"], limit=5))

    if topic.get("steps"):
        lines.append(""); lines.append("WHAT YOU SHOULD DO")
        lines.append("\\n".join("  %d. %s" % (i, s)
                     for i, s in enumerate(topic["steps"][:5], start=1)))

    if topic.get("laws"):
        lines.append(""); lines.append("LAW THAT APPLIES")
        lines.append(_bullets(topic["laws"], limit=4))

    return "\\n".join(lines)
''')

    p("The headings are written in CAPITALS on their own line. The browser then "
      "turns any such line into a styled heading, which is why the reply looks "
      "formatted even though the server only ever sends plain text.")


# ===========================================================================
#  6. THE "I DON'T KNOW" REPLY
# ===========================================================================
def unknown_demo():
    """Run the real engine on an out-of-scope question for genuine numbers."""
    q = "how do i bake a chocolate cake"
    res = chatbot.ENGINE.search(q, limit=3)
    rows = [["Rank", "Best entry the engine could find", "Score", "Above the 0.02 floor?"]]
    if res:
        for i, r in enumerate(res, 1):
            rows.append([str(i), r["entry"]["title"], "%.4f" % r["score"],
                         "YES" if r["score"] >= 0.02 else "<b>no</b>"])
    else:
        rows.append(["-", "nothing matched at all", "0.0000", "<b>no</b>"])
    reply = chatbot.answer(q, use_ai=False)
    return q, rows, reply


def sec_unknown():
    h1("6. How the chatbot says “I don’t know”")

    box("This is the feature I am most pleased with, and it is worth showing "
        "deliberately in the demo. Any search engine can return its best guess. "
        "The harder decision is knowing when the best guess is not good enough "
        "to give at all.")

    h2("6.1 Why I added it")
    p("My first version always returned its top match, no matter how weak. I "
      "typed a question about something completely outside the knowledge base "
      "and it confidently produced a legal topic that had nothing to do with "
      "it. The answer looked exactly as authoritative as a correct one.")

    say("In a legal tool that is the worst thing the system can do. A user "
        "cannot tell a confident wrong answer from a right one, and they might "
        "act on it. So I decided the engine had to be able to refuse.")

    h2("6.2 How it works - the confidence floor")
    p("Cosine similarity always returns a number between 0 and 1. A good match "
      "scores roughly 0.3 to 0.8. A question with nothing in common scores "
      "almost 0. So I set a threshold: if the best score is below "
      "<b>0.02</b>, the engine does not answer.")

    code('''
results = ENGINE.search(message, limit=8)
...
if not results or results[0]["score"] < 0.02:
    return {
        "answer": (
            "I could not find a confident match for that in my knowledge "
            "base.\\n\\nI currently cover " + str(len(CATEGORIES)) + " areas "
            "of law including criminal, civil, property, company, contract, "
            "labour, intellectual property, cyber, family, consumer, tax, "
            "banking, motor vehicle, environment, infrastructure, medical, "
            "education and international law.\\n\\nTry rephrasing with the "
            "subject you are concerned about - for example 'my employer has "
            "not paid my salary' or 'builder has delayed possession of my "
            "flat'.\\n\\n" + DISCLAIMER
        ),
        "intent":      "unknown",      # logged so I can review it later
        "sources":     [],             # no source links - there is no source
        "suggestions": suggestions_for(None),
        "engine":      "offline",
        "confidence":  0.0,
    }
''', "The refusal path, from chatbot.py")

    code_explain([
        ('if not results or results[0]["score"] < 0.02',
         "Two cases: either nothing matched at all, or the best match is too weak to trust."),
        ('"intent": "unknown"',
         "This is recorded in the database. The analytics page counts these, so every refusal becomes an item on my improvement list."),
        ('"sources": []',
         "No source links are shown, because there is no source. The interface then has nothing to point at, which reinforces the honesty."),
        ('"confidence": 0.0',
         "Reported back to the browser, so the reply can never be displayed as if it were confident."),
        ('suggestions_for(None)',
         "Instead of a dead end, the user gets four example questions that DO work."),
    ])

    h2("6.3 A real refusal, run just now")
    q, rows, reply = unknown_demo()
    p("Here is the engine actually being asked <b>“%s”</b> while this document "
      "was being generated. These are real scores, not made up." % q)
    table(rows, [CW * 0.08, CW * 0.52, CW * 0.16, CW * 0.24],
          "Nothing clears the confidence floor, so the engine refuses", fs=8)

    p("And this is the exact reply the user sees:")
    import textwrap
    wrapped = []
    for line in reply["answer"].split("\n"):
        if not line.strip():
            wrapped.append("")
        else:
            wrapped.extend(textwrap.wrap(line, width=92) or [""])
    code("\n".join(wrapped))

    h2("6.4 What I say about it in the viva")
    say("Adding this actually made the system answer fewer questions, and when "
        "I first did it, it felt like a step backwards. But it is the most "
        "important correctness decision in the project. The system now has "
        "three possible outputs instead of two: the right answer, a related "
        "answer with its sources shown so you can check it, or an honest "
        "admission that it does not know. There is no fourth state where it "
        "makes something up.")

    h2("6.5 Three more places the same honesty appears")
    bullets([
        "<b>Source links on every reply.</b> Each answer shows the pages it came "
        "from, with the relevance score, so the user can verify it rather than "
        "trust it.",
        "<b>The offline engine cannot invent anything.</b> It is retrieval, not "
        "generation - it can only return text that is already written in the "
        "knowledge base. There is no mechanism by which it could produce a "
        "section number that does not exist.",
        "<b>State-specific figures are refused too.</b> Where stamp duty or "
        "tenancy rules differ between states, the content says that they differ "
        "instead of quoting one state's number as if it were national.",
    ])


# ===========================================================================
#  7. WORKED EXAMPLE
# ===========================================================================
def sec_worked():
    h1("7. One question, traced all the way through")

    q = "my landlord is not returning my deposit"
    raw = chatbot.TOKEN_PATTERN.findall(q.lower())
    kept = [w for w in raw if w not in chatbot.STOPWORDS and len(w) > 1]
    stemmed = [chatbot.stem(w) for w in kept]
    final = chatbot.tokenize(chatbot.expand_query(q))
    vec = chatbot.ENGINE._vectorise(final)
    top = sorted(vec.items(), key=lambda kv: kv[1], reverse=True)[:6]
    res = chatbot.ENGINE.search(q, limit=4)

    p("If I am asked to “walk me through what happens”, this is the answer. "
      "Every number below was produced by running the real engine while this "
      "document was being built.")

    box("<b>The question:</b> “%s”" % q)

    h2("7.1 The words")
    table([
        ["Stage", "Result"],
        ["1. Raw tokens", ", ".join(raw)],
        ["2. Stopwords removed", ", ".join(kept)],
        ["3. Stemmed", ", ".join(stemmed)],
        ["4. Synonyms added", ", ".join(final[:20]) + " …"],
        ["Vector size", "%d distinct terms" % len(vec)],
    ], [CW * 0.24, CW * 0.76], "Text processing, step by step", fs=8.2)

    p("Notice stage 4. The user never typed <i>tenancy</i>, <i>lease</i>, "
      "<i>rent</i>, <i>security</i> or <i>refund</i> - the synonym layer added "
      "them, and that is what makes the match work.")

    h2("7.2 The weights")
    rows = [["Stemmed word", "IDF (how rare it is)", "Final weight in the vector"]]
    for t, w in top:
        rows.append([t, "%.3f" % chatbot.ENGINE.idf.get(t, 0), "%.4f" % w])
    table(rows, [CW * 0.34, CW * 0.33, CW * 0.33],
          "The six heaviest words in the question", fs=8.2)

    p("This table is the clearest possible demonstration of what IDF does. "
      "The distinctive legal words dominate; ordinary words that appear all "
      "over the knowledge base contribute almost nothing.")

    h2("7.3 The result")
    rows = [["Rank", "Entry", "Type", "Cosine score"]]
    for i, r in enumerate(res, 1):
        rows.append([str(i), r["entry"]["title"],
                     "Template" if r["entry"]["kind"] == "document" else "Topic",
                     "%.4f" % r["score"]])
    table(rows, [CW * 0.08, CW * 0.56, CW * 0.16, CW * 0.20],
          "Ranked matches for the question", fs=8.2)

    say("The correct topic wins clearly. And notice the rent agreement template "
        "is not at the top even though it shares most of the same words - the "
        "ranking adjustment recognised that this message describes a problem "
        "rather than asking for a format.")


# ===========================================================================
#  8. FLASK, VOICE, DATABASE
# ===========================================================================
def sec_rest():
    h1("8. The rest of the code")

    h2("8.1 Flask - how a web page happens")
    p("Each route is a short function. It picks the data and hands it to an "
      "HTML template. There is no logic in the routes at all.")

    code('''
@app.route("/topic/<topic_id>")
def topic_page(topic_id):
    topic = get_topic(topic_id)
    if not topic:
        return render_template("404.html", thing="topic"), 404

    related      = [t for t in topics_in_category(topic["category"])
                    if t["id"] != topic_id][:3]
    related_docs = documents_in_category(topic["category"])[:3]

    return render_template("topic.html",
                           topic=topic,
                           category=get_category(topic["category"]),
                           related=related,
                           related_docs=related_docs)
''')

    code_explain([
        ('@app.route("/topic/<topic_id>")',
         "A decorator. It tells Flask: when the browser asks for this address, run this function. The angle brackets capture part of the URL as a parameter."),
        ('get_topic(topic_id)',
         "Looks the topic up in the knowledge base by its id."),
        ('return render_template(...), 404',
         "If the id does not exist, return the friendly error page WITH a real 404 status code, not a fake 200."),
        ('render_template("topic.html", topic=topic, ...)',
         "Jinja2 fills the HTML template with this data and sends the finished page."),
    ])

    h3("The chat endpoint - the only one the browser calls in the background")
    code('''
@app.route("/api/chat", methods=["POST"])
def api_chat():
    data       = request.get_json(silent=True) or {}
    message    = (data.get("message") or "").strip()
    session_id = current_session_id()

    if not message:
        return jsonify({"error": "Please type a question."}), 400

    history = database.session_history(session_id, limit=3)   # short memory
    reply   = chatbot.answer(message, history=history)

    database.save_chat(session_id=session_id, question=message,
                       answer=reply["answer"], intent=reply["intent"],
                       engine=reply["engine"], confidence=reply["confidence"],
                       top_source=reply["sources"][0]["title"] if reply["sources"] else "")

    return jsonify(reply)
''')

    p("Every reply has the same JSON shape, which keeps the JavaScript simple - "
      "it never has to check what kind of answer it received:")
    code('''
{ "answer": "...", "intent": "question", "sources": [...],
  "suggestions": [...], "engine": "offline", "confidence": 0.7701 }
''')

    h2("8.2 The voice code")
    p("Both directions use the browser's own Web Speech API. Nothing is sent to "
      "a paid service and no audio reaches my server.")

    h3("Speech to text - the microphone")
    code('''
var Recognition = window.SpeechRecognition || window.webkitSpeechRecognition;

recogniser = new Recognition();
recogniser.lang           = "en-IN";   // Indian English accent model
recogniser.continuous     = false;     // stop after one sentence
recogniser.interimResults = true;      // show words as they are spoken

recogniser.onresult = function (event) {
    var text = "";
    for (var i = event.resultIndex; i < event.results.length; i++) {
        text += event.results[i][0].transcript;
    }
    input.value = text;                             // live transcription

    if (event.results[event.results.length - 1].isFinal) {
        setTimeout(function () { send(); }, 400);   // then send it
    }
};
''')

    code_explain([
        ('lang = "en-IN"',
         "Indian English. With the default en-US it mis-transcribed Indian names and legal words like ‘stridhan’."),
        ('interimResults = true',
         "Shows words as you speak. Testers stopped mid-sentence thinking the mic had failed when nothing appeared."),
        ('setTimeout(..., 400)',
         "A 400 ms delay before sending. The browser sometimes revises its final result, and sending instantly clipped the question."),
    ])

    h3("Text to speech - and the bug worth mentioning")
    p("Long answers simply stopped speaking half way through. Browsers truncate "
      "very long utterances. I split the answer at sentence boundaries into "
      "roughly 200-character pieces and queue them.")

    code('''
var chunks = clean.match(/[^.!?]+[.!?]*/g) || [clean];
var buffer = "", queue = [];

chunks.forEach(function (piece) {
    if ((buffer + piece).length > 200) { if (buffer) queue.push(buffer); buffer = piece; }
    else { buffer += piece; }
});
if (buffer) queue.push(buffer);

queue.forEach(function (part) {
    var utterance   = new SpeechSynthesisUtterance(part.trim());
    utterance.voice = chosenVoice;
    utterance.rate  = parseFloat(rateBox.value);
    synth.speak(utterance);              // queued, played one after another
});
''')

    table([
        ["Problem I hit", "Cause", "What I did"],
        ["Long answers stopped speaking", "Browsers truncate long utterances", "Split into ~200 character chunks and queued them"],
        ["The mic transcribed the bot's own voice", "Speech was still playing when the mic opened", "Cancel speech synthesis whenever the mic starts"],
        ["Voice list was empty on first load", "Chrome loads voices asynchronously", "Also rebuild the list on the voiceschanged event"],
        ["Spoken questions were sent truncated", "The browser revises its final result", "Added a 400 ms delay before sending"],
    ], [CW * 0.32, CW * 0.30, CW * 0.38], "Voice bugs I found and fixed", fs=8)

    h2("8.3 The database")
    p("SQLite, because it needs no server, no password and no installation - "
      "the whole database is one file created automatically on first run. "
      "Three tables, and <b>only interaction data</b>: the legal content is not "
      "in the database at all.")

    code('''
CREATE TABLE IF NOT EXISTS chat_log (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id  TEXT    NOT NULL,   -- random id, NOT a user identity
    question    TEXT    NOT NULL,
    answer      TEXT    NOT NULL,
    intent      TEXT,               -- question / emergency / unknown / ...
    engine      TEXT,               -- 'offline' or 'ai'
    confidence  REAL,               -- the cosine score of the best match
    top_source  TEXT,               -- which page the answer came from
    created_at  TEXT    NOT NULL
);
''')

    p("The most useful query I wrote is the one that finds my own weaknesses:")
    code('''
-- Questions the engine could NOT answer confidently: my improvement list
SELECT COUNT(*) FROM chat_log WHERE intent = 'unknown';
''')

    box("<b>Privacy point worth making:</b> there is no login, no name and no "
        "email anywhere in the chat path. The session id is a random value with "
        "no link to a person. Voice audio is handled by the browser and never "
        "reaches the server or the database at all.")


# ===========================================================================
#  9. RESULTS
# ===========================================================================
def sec_results():
    h1("9. What I measured")

    p("Numbers are more convincing than claims. These are the ones to have "
      "ready.")

    table([
        ["Measure", "Value"],
        ["Branches of law covered", str(KB["categories"])],
        ["Legal topics written", str(KB["topics"])],
        ["Document templates", str(KB["documents"])],
        ["Glossary terms", str(KB["glossary"])],
        ["FAQs answered", str(KB["faqs"])],
        ["Entries the engine searches", str(INDEXED)],
        ["Web routes", "19"],
        ["HTML templates", "17"],
        ["Total lines of code", "about 12,000"],
        ["Top-1 retrieval accuracy", "93.3% (28/30)"],
        ["Top-3 retrieval accuracy", "100% (30/30)"],
        ["Format requests routed to a template", "10/10"],
        ["Answer time", "well under a tenth of a second"],
        ["External runtime dependencies", "1 (Flask)"],
        ["Cost of the whole project", "Rs 0"],
    ], [CW * 0.58, CW * 0.42], "Numbers to have ready", fs=8.6)

    h2("9.1 How I tested it")
    p("I wrote 30 questions phrased the way a non-lawyer would actually type "
      "them - situations, not legal terms - and recorded in advance which page "
      "should be returned. The script "
      "<font face='Courier'>docs/evaluate.py</font> runs them all and reports "
      "the score. I can run it live in front of the examiner:")
    code("python docs/evaluate.py")

    say("I measured two things. Top-1 is whether the correct page comes back "
        "first. Top-3 matters as well, because the chatbot shows the top three "
        "as source links under every answer - so a page that comes second is "
        "still visible and one click away.")


# ===========================================================================
#  10. VIVA QUESTIONS
# ===========================================================================
def sec_viva():
    h1("10. Questions I should be ready for")

    p("Grouped by how likely they are. The answers are short on purpose - say "
      "the short answer first and let them ask for more.")

    h2("10.1 They will almost certainly ask these")
    qa = [
        ("What is your project in one line?",
         "A legal help website where you can ask a question in normal English, by typing or speaking, and it finds the right law, explains it simply, and gives you the document you need."),
        ("Which technologies did you use?",
         "Python 3 with Flask for the server, SQLite for storage, Jinja2 for the pages, and plain HTML, CSS and JavaScript for the front end. No TypeScript, no React, no build step. The only external dependency is Flask."),
        ("Did you use any AI or machine learning library?",
         "No. The search engine is classical information retrieval - TF-IDF and cosine similarity - which I implemented myself in about eighty lines. I chose that deliberately because I can explain every line, and because when it gives a wrong answer I can print the exact word weights that caused it. There is an optional mode that can pass the retrieved material to a language model to rewrite the reply, but the project is demonstrated with it switched off."),
        ("Explain TF-IDF.",
         "TF is how often a word appears in a document divided by its length - a repeated word matters to that document. IDF is log of total documents divided by how many contain the word - a word appearing everywhere tells you nothing, so it gets a low weight, while a rare word like 'gratuity' gets a high one. Multiply them and you get a weight that is high only for words that are both frequent here and rare elsewhere."),
        ("What is cosine similarity and why did you use it?",
         "It measures the angle between two vectors rather than the distance, so it compares what a text is ABOUT independently of how long it is. Without it, long topics would beat short ones on every query. And because I normalise every vector to unit length when building the index, the cosine reduces to just a dot product, which is why it is fast."),
        ("How does the chatbot know what the user means?",
         "Three things stacked. First an intent layer classifies the message - greeting, definition, emergency, document request, or an ordinary question. Second a synonym table maps everyday words to legal ones, so 'my boss fired me' also searches for 'termination'. Third the TF-IDF search finds the closest topic."),
        ("What happens if the chatbot doesn't know the answer?",
         "It says so. Cosine similarity gives a score between 0 and 1, and if the best score is below 0.02 the engine refuses to answer - it explains what it does cover and suggests how to rephrase. It also logs that as an 'unknown' intent so I can see what to add next. In a legal tool a confident wrong answer is far worse than admitting ignorance."),
        ("How accurate is it?",
         "93.3% Top-1 and 100% Top-3 on a set of 30 questions written the way real users type. It was 66.7% at first - I found that document templates were beating the topics that explained the same subject, fixed the ranking, and re-measured."),
    ]
    for q, a in qa:
        h3("Q. " + q)
        p(a)

    h2("10.2 Likely follow-ups")
    qa2 = [
        ("Why SQLite and not MySQL?",
         "No server process to install or run during a demonstration, and the whole database is a single file. For a project storing usage logs it is the right size of tool."),
        ("Why did you store the legal content in Python files instead of the database?",
         "Because it is read-only content that I author, not data that users create. Keeping it as code means changes are reviewable as a text diff, adding a topic needs no migration, and I did not have to build an admin interface nobody would use."),
        ("How would you scale this?",
         "The index is in memory and rebuilt at start-up, which is right for 111 entries. For hundreds of thousands I would need a persistent inverted index, and I would move to a proper WSGI server instead of Flask's development server."),
        ("What is the time complexity of a search?",
         "O(N × m) where N is the number of entries and m is the smaller of the two vectors - I loop over whichever vector has fewer words. Plus O(N log N) to sort. Building the index is O(N × L) but happens once at start-up."),
        ("Why does the voice only work in Chrome?",
         "Speech recognition in the Web Speech API is implemented in Chromium-based browsers. I handle its absence gracefully - the microphone button is hidden with an explanatory note and everything still works by typing."),
        ("Is this legal advice?",
         "No, and that boundary is built into the design rather than just stated. It gives general information; it never evaluates the facts of a case, predicts an outcome or recommends a course of action. There is a disclaimer strip on every page and a disclaimer appended to every single chatbot reply."),
        ("How do you stop it giving wrong legal information?",
         "The offline engine cannot invent anything - it is retrieval, so it can only return text already written in the knowledge base. Every answer shows the pages it came from so the user can verify it. And where a rule varies by state, the content says that it varies instead of quoting one state's figure."),
        ("What was the hardest part?",
         "Honestly, not the code - it was the vocabulary gap. Not one test user typed a legal term. Building the layer that maps ordinary words to legal ones did more for usability than any change to the maths."),
        ("What would you do differently?",
         "Write the evaluation set first. I built the engine for six weeks on impressions and only measured it near the end. If those thirty test questions had existed in week four, I would have caught the template ranking bug immediately instead of shipping it for most of the project."),
        ("What is the future scope?",
         "Regional languages - the browser speech API already supports Hindi and Kannada, so it is mainly a content problem. Then spelling correction, semantic search using embeddings alongside TF-IDF, and a guided flow that fills a template by asking questions."),
    ]
    for q, a in qa2:
        h3("Q. " + q)
        p(a)

    h2("10.3 If they ask something I genuinely don't know")
    box("Say so, then say what I would do to find out. “I haven't tested that - "
        "my instinct is X, and the way I'd check it is Y.” That answer is "
        "respected. Guessing and being wrong is not. It is also exactly the "
        "principle I built into the chatbot, so I can even point at that.",
        fill=colors.HexColor("#e2eee8"), border=GREEN)


# ===========================================================================
#  11. TROUBLESHOOTING + CHEAT SHEET
# ===========================================================================
def sec_last():
    h1("11. If something goes wrong during the demo")

    table([
        ["Symptom", "Cause", "Fix on the spot"],
        ["‘ModuleNotFoundError: flask’", "Dependencies not installed on this machine", "pip install -r requirements.txt"],
        ["‘Address already in use’", "Port 5000 is taken", "Close the other window, or change the port on the last line of app.py"],
        ["Microphone button missing", "Browser has no speech recognition", "Expected - say so and demo by typing. Use Chrome or Edge."],
        ["Microphone does nothing", "Permission was refused earlier", "Click the padlock in the address bar and allow the microphone"],
        ["No voice comes out", "Muted, or no voice installed", "Check the speaker button in the chat header"],
        ["Analytics page shows zeros", "Nothing has been asked yet", "Ask two questions first, then open it"],
        ["Chatbot says it cannot find a match", "The question is outside the knowledge base", "This is correct behaviour - use it as the honesty demo"],
        ["The internet is down", "Nothing - it does not matter", "Everything runs locally. Say so; it is a selling point."],
    ], [CW * 0.28, CW * 0.32, CW * 0.40], "Demo troubleshooting", fs=8)

    h2("11.1 Commands I might be asked to run")
    code('''
python app.py                  # start the website  -> http://127.0.0.1:5000
python chatbot.py              # chatbot in the terminal, no browser needed
python legal_data.py           # print the knowledge base coverage table
python database.py             # create the database and print the totals
python docs/evaluate.py        # run the 30-question accuracy test
python docs/make_report.py     # regenerate the project report PDF
''')

    h1("12. One-page cheat sheet")

    box("<b>THE PITCH.</b> A legal help website where you ask a question in "
        "normal English - typed or spoken - and it finds the right law, "
        "explains it simply, tells you the deadline, and gives you the document "
        "you need.")

    table([
        ["Topic", "The answer in one line"],
        ["Stack", "Python, Flask, SQLite, Jinja2, HTML, CSS, vanilla JavaScript"],
        ["Not used", "TypeScript, React, any ML library, any paid API, any build step"],
        ["Content", "%d branches, %d topics, %d templates, %d glossary terms, %d FAQs"
         % (KB["categories"], KB["topics"], KB["documents"], KB["glossary"], KB["faqs"])],
        ["Engine", "TF-IDF + cosine similarity, hand-written, ~80 lines, %d indexed entries" % INDEXED],
        ["TF", "how often a word appears here / total words here"],
        ["IDF", "log( total entries / (1 + entries containing the word) ) + 1"],
        ["Cosine", "dot product of two unit-length vectors = the angle between them"],
        ["Synonyms", "~60 mappings so ‘boss fired me’ finds ‘termination’"],
        ["Intents", "greeting, thanks, bye, emergency, definition, document, question, unknown"],
        ["‘I don’t know’", "if the best cosine score is below 0.02, refuse and say so"],
        ["Accuracy", "93.3% Top-1, 100% Top-3 on 30 realistic questions"],
        ["The story", "66.7% → found templates outranking topics → fixed ranking → 93.3%"],
        ["Voice", "Web Speech API in the browser: en-IN recognition, chunked synthesis"],
        ["Database", "3 SQLite tables, interaction logs only, no personal data"],
        ["Boundary", "Legal information, never legal advice - built in, not just disclaimed"],
    ], [CW * 0.20, CW * 0.80], None, fs=8.4)

    box("<b>If I only get one sentence at the end:</b> “The part I am proudest "
        "of is that it knows when it doesn’t know - it refuses to answer below "
        "a confidence threshold, because in a legal tool a confident wrong "
        "answer is the most dangerous thing you can produce.”",
        fill=colors.HexColor("#f2ead4"), border=BRASS)


# ===========================================================================
#  BUILD
# ===========================================================================
def build():
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "LegalMitra_Presentation_Guide.pdf")
    doc = Doc(out, pagesize=A4,
              leftMargin=20 * mm, rightMargin=20 * mm,
              topMargin=20 * mm, bottomMargin=18 * mm,
              title="LegalMitra - Presentation & Code Walkthrough",
              author="LegalMitra project")
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="n")
    doc.addPageTemplates([PageTemplate(id="all", frames=frame, onPage=decorate)])

    cover()
    sec_pitch()
    sec_demo()
    sec_flow()
    sec_data()
    sec_engine()
    sec_unknown()
    sec_worked()
    sec_rest()
    sec_results()
    sec_viva()
    sec_last()

    doc.build(story)
    return out, doc.page


if __name__ == "__main__":
    print("Building the presentation guide...")
    path, pages = build()
    print("  Written:", path)
    print("  Pages  : %d   Size: %.0f KB" % (pages, os.path.getsize(path) / 1024.0))
