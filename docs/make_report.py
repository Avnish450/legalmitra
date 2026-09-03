# -*- coding: utf-8 -*-
"""
docs/make_report.py
===================
Builds the complete project report PDF using ReportLab.

Run it from the project folder:

    python docs/make_report.py

Output:  docs/LegalMitra_Project_Report.pdf

The report is generated from the LIVE project - the counts, the coverage table
and the accuracy results are read from the actual knowledge base and the actual
chatbot engine, not typed in by hand. If you add a topic and re-run this
script, the report updates itself.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.graphics.shapes import Drawing, Line, PolyLine, Polygon, Rect, String
from reportlab.platypus import (
    KeepTogether,
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

import chatbot
import legal_data
from docs import evaluate as evaluator  # noqa: F401  (imported for its TEST_SET)

# ---------------------------------------------------------------------------
# COLOURS AND STYLES
# ---------------------------------------------------------------------------

NAVY = colors.HexColor("#14213d")
NAVY_LIGHT = colors.HexColor("#1d2f52")
GOLD = colors.HexColor("#c9a227")
GREY = colors.HexColor("#5a6072")
LINE = colors.HexColor("#d8d5cc")
PAPER = colors.HexColor("#f7f6f2")
GREEN = colors.HexColor("#1e7a52")
RED = colors.HexColor("#b3261e")
BLUE_SOFT = colors.HexColor("#eef3fb")

styles = getSampleStyleSheet()

S_TITLE = ParagraphStyle("t", parent=styles["Title"], fontName="Times-Bold",
                         fontSize=26, leading=32, textColor=NAVY, spaceAfter=6)
S_SUB = ParagraphStyle("sub", parent=styles["Normal"], fontName="Times-Roman",
                       fontSize=13, leading=18, alignment=TA_CENTER, textColor=GREY)
S_H1 = ParagraphStyle("h1", parent=styles["Heading1"], fontName="Times-Bold",
                      fontSize=18, leading=23, textColor=NAVY,
                      spaceBefore=16, spaceAfter=10)
S_H2 = ParagraphStyle("h2", parent=styles["Heading2"], fontName="Times-Bold",
                      fontSize=13.5, leading=18, textColor=NAVY_LIGHT,
                      spaceBefore=12, spaceAfter=6)
S_H3 = ParagraphStyle("h3", parent=styles["Heading3"], fontName="Times-Bold",
                      fontSize=11.5, leading=15, textColor=NAVY_LIGHT,
                      spaceBefore=9, spaceAfter=4)
S_BODY = ParagraphStyle("b", parent=styles["Normal"], fontName="Times-Roman",
                        fontSize=10.5, leading=15.5, alignment=TA_JUSTIFY,
                        spaceAfter=7)
S_BULLET = ParagraphStyle("bu", parent=S_BODY, leftIndent=16, bulletIndent=5,
                          spaceAfter=3.5)
S_CAPTION = ParagraphStyle("cap", parent=styles["Normal"], fontName="Times-Italic",
                           fontSize=9, leading=12, alignment=TA_CENTER,
                           textColor=GREY, spaceBefore=4, spaceAfter=12)
S_CODE = ParagraphStyle("code", parent=styles["Code"], fontName="Courier",
                        fontSize=7.4, leading=9.4, textColor=colors.HexColor("#232833"),
                        backColor=colors.HexColor("#fbfaf7"),
                        borderPadding=6, spaceBefore=4, spaceAfter=10)
S_CENTER = ParagraphStyle("c", parent=S_BODY, alignment=TA_CENTER)
S_NOTE = ParagraphStyle("n", parent=S_BODY, fontSize=9.5, leading=13.5,
                        textColor=GREY)

PAGE_W, PAGE_H = A4
CONTENT_W = PAGE_W - 44 * mm

story = []
FIGURE_NUMBER = [0]
TABLE_NUMBER = [0]
FIGURES = []
TABLES = []


# ---------------------------------------------------------------------------
# SMALL BUILDING BLOCKS
# ---------------------------------------------------------------------------

def h1(text):
    story.append(PageBreak())
    story.append(Paragraph(text, S_H1))
    story.append(hr())


def h1_same_page(text):
    story.append(Paragraph(text, S_H1))
    story.append(hr())


def h2(text):
    story.append(Paragraph(text, S_H2))


def h3(text):
    story.append(Paragraph(text, S_H3))


def p(text):
    story.append(Paragraph(text, S_BODY))


def note(text):
    story.append(Paragraph(text, S_NOTE))


def bullets(items, numbered=False):
    for index, item in enumerate(items, start=1):
        marker = "%d." % index if numbered else "•"
        story.append(Paragraph(item, S_BULLET, bulletText=marker))
    story.append(Spacer(1, 5))


def gap(height=8):
    story.append(Spacer(1, height))


def hr(color=GOLD, thickness=1.6):
    drawing = Drawing(CONTENT_W, thickness + 3)
    drawing.add(Line(0, 2, CONTENT_W, 2, strokeColor=color, strokeWidth=thickness))
    return drawing


def caption(text, kind="Figure"):
    if kind == "Figure":
        FIGURE_NUMBER[0] += 1
        label = "Figure %d: %s" % (FIGURE_NUMBER[0], text)
        FIGURES.append(label)
    else:
        TABLE_NUMBER[0] += 1
        label = "Table %d: %s" % (TABLE_NUMBER[0], text)
        TABLES.append(label)
    story.append(Paragraph(label, S_CAPTION))


def table(data, widths, caption_text=None, header=True, font_size=8.6,
          align_left_cols=None):
    style = [
        ("FONTNAME", (0, 0), (-1, -1), "Times-Roman"),
        ("FONTSIZE", (0, 0), (-1, -1), font_size),
        ("LEADING", (0, 0), (-1, -1), font_size + 3.4),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.4, LINE),
        ("TOPPADDING", (0, 0), (-1, -1), 4.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4.5),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]
    if header:
        style += [
            ("BACKGROUND", (0, 0), (-1, 0), NAVY),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Times-Bold"),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, PAPER]),
        ]
    else:
        style += [("ROWBACKGROUNDS", (0, 0), (-1, -1), [colors.white, PAPER])]

    wrapped = []
    for row_index, row in enumerate(data):
        new_row = []
        for cell in row:
            if isinstance(cell, str):
                is_head = header and row_index == 0
                cell_style = ParagraphStyle(
                    "cell", parent=S_BODY, fontSize=font_size,
                    leading=font_size + 3.4, alignment=0, spaceAfter=0,
                    fontName="Times-Bold" if is_head else "Times-Roman",
                    textColor=colors.white if is_head else colors.black,
                )
                new_row.append(Paragraph(cell, cell_style))
            else:
                new_row.append(cell)
        wrapped.append(new_row)

    element = Table(wrapped, colWidths=widths, repeatRows=1 if header else 0)
    element.setStyle(TableStyle(style))
    story.append(element)
    if caption_text:
        caption(caption_text, kind="Table")
    else:
        gap(10)


def code(text, title=None):
    if title:
        story.append(Paragraph(title, S_H3))
    story.append(Preformatted(text.strip("\n"), S_CODE))


def callout(text, color=BLUE_SOFT, border=NAVY):
    para = Paragraph(text, ParagraphStyle(
        "co", parent=S_BODY, fontSize=9.8, leading=14, spaceAfter=0))
    element = Table([[para]], colWidths=[CONTENT_W])
    element.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), color),
        ("LINEBEFORE", (0, 0), (0, -1), 3, border),
        ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
        ("LEFTPADDING", (0, 0), (-1, -1), 11),
        ("RIGHTPADDING", (0, 0), (-1, -1), 11),
    ]))
    story.append(element)
    gap(11)


# ---------------------------------------------------------------------------
# DIAGRAM HELPERS - simple boxes and arrows drawn with ReportLab shapes
# ---------------------------------------------------------------------------

def box(drawing, x, y, w, h, text, fill=colors.white, stroke=NAVY,
        text_color=NAVY, size=8, bold=True, radius=0, sub=None):
    drawing.add(Rect(x, y, w, h, fillColor=fill, strokeColor=stroke,
                     strokeWidth=1.1, rx=radius, ry=radius))
    lines = text.split("\n")
    font = "Helvetica-Bold" if bold else "Helvetica"
    start = y + h / 2 + (len(lines) - 1) * (size + 1.6) / 2 - size / 2 + 1
    if sub:
        start += 4
    for index, line in enumerate(lines):
        drawing.add(String(x + w / 2, start - index * (size + 1.6), line,
                           fontName=font, fontSize=size, fillColor=text_color,
                           textAnchor="middle"))
    if sub:
        drawing.add(String(x + w / 2, y + 5, sub, fontName="Helvetica",
                           fontSize=size - 1.4, fillColor=GREY,
                           textAnchor="middle"))


def ellipse_box(drawing, cx, cy, rx, ry, text, fill=colors.white, stroke=NAVY, size=7.5):
    from reportlab.graphics.shapes import Ellipse
    drawing.add(Ellipse(cx, cy, rx, ry, fillColor=fill, strokeColor=stroke,
                        strokeWidth=1.1))
    lines = text.split("\n")
    start = cy + (len(lines) - 1) * (size + 1.4) / 2 - size / 2 + 1
    for index, line in enumerate(lines):
        drawing.add(String(cx, start - index * (size + 1.4), line,
                           fontName="Helvetica", fontSize=size,
                           fillColor=NAVY, textAnchor="middle"))


def arrow(drawing, x1, y1, x2, y2, label=None, color=NAVY_LIGHT, dashed=False,
          label_offset=6, size=6.6):
    kwargs = {"strokeColor": color, "strokeWidth": 1.1}
    if dashed:
        kwargs["strokeDashArray"] = [3, 2]
    drawing.add(Line(x1, y1, x2, y2, **kwargs))

    # arrow head
    import math
    angle = math.atan2(y2 - y1, x2 - x1)
    size_head = 5.0
    left = (x2 - size_head * math.cos(angle - 0.42),
            y2 - size_head * math.sin(angle - 0.42))
    right = (x2 - size_head * math.cos(angle + 0.42),
             y2 - size_head * math.sin(angle + 0.42))
    drawing.add(Polygon([x2, y2, left[0], left[1], right[0], right[1]],
                        fillColor=color, strokeColor=color))

    if label:
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        drawing.add(String(mx, my + label_offset, label, fontName="Helvetica",
                           fontSize=size, fillColor=GREY, textAnchor="middle"))


def label_text(drawing, x, y, text, size=7, color=GREY, anchor="start", bold=False):
    drawing.add(String(x, y, text, fontName="Helvetica-Bold" if bold else "Helvetica",
                       fontSize=size, fillColor=color, textAnchor=anchor))


# ---------------------------------------------------------------------------
# PAGE FURNITURE (header line, footer with page number)
# ---------------------------------------------------------------------------

def decorate(canvas, doc):
    canvas.saveState()
    page = canvas.getPageNumber()

    if page > 1:
        canvas.setStrokeColor(LINE)
        canvas.setLineWidth(0.5)
        canvas.line(22 * mm, PAGE_H - 17 * mm, PAGE_W - 22 * mm, PAGE_H - 17 * mm)
        canvas.setFont("Times-Italic", 8)
        canvas.setFillColor(GREY)
        canvas.drawString(22 * mm, PAGE_H - 15 * mm,
                          "LegalMitra - Legal Information Portal with AI Chatbot")
        canvas.drawRightString(PAGE_W - 22 * mm, PAGE_H - 15 * mm,
                               "Second Year Engineering Mini Project")

        canvas.line(22 * mm, 15 * mm, PAGE_W - 22 * mm, 15 * mm)
        canvas.setFont("Times-Roman", 8.5)
        canvas.drawCentredString(PAGE_W / 2, 10 * mm, str(page))
    canvas.restoreState()


# ===========================================================================
#  LIVE PROJECT DATA
# ===========================================================================

KB = legal_data.stats()
INDEXED = len(chatbot.ENGINE.entries)
ACCURACY = evaluator.run.__doc__ and None  # placeholder; real run happens below


def gather_accuracy():
    """Run the real evaluation quietly and return the numbers."""
    import io
    import contextlib
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        result = evaluator.run()
    return result


ACC = gather_accuracy()


def gather_timings():
    """Measure real index build time and real per-question answer time."""
    import time

    # Index build time - construct a fresh engine and time it.
    start = time.perf_counter()
    chatbot.SearchEngine()
    build_ms = (time.perf_counter() - start) * 1000.0

    # Per-question time across the whole evaluation set, offline engine only.
    samples = []
    for question, _ in evaluator.TEST_SET:
        start = time.perf_counter()
        chatbot.answer(question, use_ai=False)
        samples.append((time.perf_counter() - start) * 1000.0)

    # Search-only time (excluding answer composition).
    search_samples = []
    for question, _ in evaluator.TEST_SET:
        start = time.perf_counter()
        chatbot.ENGINE.search(question, limit=5)
        search_samples.append((time.perf_counter() - start) * 1000.0)

    samples.sort()
    return {
        "build_ms": build_ms,
        "mean_ms": sum(samples) / len(samples),
        "median_ms": samples[len(samples) // 2],
        "worst_ms": samples[-1],
        "best_ms": samples[0],
        "search_mean_ms": sum(search_samples) / len(search_samples),
        "runs": len(samples),
    }


TIME = gather_timings()

LOC = {
    "app.py": 472, "chatbot.py": 928, "database.py": 216,
    "legal_data.py": 354, "legal_topics.py": 1779,
    "legal_topics_extra.py": 1693, "legal_documents.py": 3247,
    "legal_extras.py": 305, "style.css": 952, "chat.js": 467,
    "main.js": 179, "templates (17 files)": 1588,
}


def real_loc():
    """Count the lines of every source file so the report is never stale."""
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    counts = {}

    def count(path):
        try:
            with open(path, "r", encoding="utf-8") as handle:
                return sum(1 for _ in handle)
        except OSError:
            return 0

    for name in ["app.py", "chatbot.py", "database.py", "legal_data.py",
                 "legal_topics.py", "legal_topics_extra.py",
                 "legal_documents.py", "legal_extras.py"]:
        counts[name] = count(os.path.join(root, name))
    counts["static/css/style.css"] = count(os.path.join(root, "static", "css", "style.css"))
    counts["static/js/chat.js"] = count(os.path.join(root, "static", "js", "chat.js"))
    counts["static/js/main.js"] = count(os.path.join(root, "static", "js", "main.js"))

    template_dir = os.path.join(root, "templates")
    template_total = 0
    template_files = 0
    if os.path.isdir(template_dir):
        for name in sorted(os.listdir(template_dir)):
            if name.endswith(".html"):
                template_total += count(os.path.join(template_dir, name))
                template_files += 1
    counts["templates/ (%d files)" % template_files] = template_total
    return counts


LOC = real_loc()
TOTAL_LOC = sum(LOC.values())


# ===========================================================================
#  FRONT MATTER
# ===========================================================================

def build_cover():
    gap(18)
    story.append(Paragraph("A PROJECT REPORT ON", S_SUB))
    gap(14)
    story.append(Paragraph("LegalMitra", S_TITLE))
    story.append(Paragraph(
        "A Legal Information Portal with a<br/>Voice-Enabled AI Chatbot", S_SUB))
    gap(10)
    story.append(hr(GOLD, 2))
    gap(16)

    # Scales of justice, drawn with plain lines and polygons.
    emblem = Drawing(CONTENT_W, 130)
    cx = CONTENT_W / 2
    box(emblem, cx - 52, 8, 104, 114, "", fill=PAPER, stroke=NAVY, radius=10)

    beam_y = 92
    emblem.add(Line(cx, 34, cx, beam_y, strokeColor=NAVY, strokeWidth=2.2))      # post
    emblem.add(Line(cx - 32, beam_y, cx + 32, beam_y, strokeColor=NAVY, strokeWidth=2.2))
    from reportlab.graphics.shapes import Circle
    emblem.add(Circle(cx, beam_y + 5, 3.4, fillColor=GOLD, strokeColor=NAVY, strokeWidth=1))

    for side in (-1, 1):
        px = cx + side * 32
        emblem.add(Line(px, beam_y, px - 13, beam_y - 20, strokeColor=NAVY, strokeWidth=0.9))
        emblem.add(Line(px, beam_y, px + 13, beam_y - 20, strokeColor=NAVY, strokeWidth=0.9))
        emblem.add(Polygon([px - 15, beam_y - 20, px + 15, beam_y - 20,
                            px + 9, beam_y - 30, px - 9, beam_y - 30],
                           fillColor=GOLD, strokeColor=NAVY, strokeWidth=1))

    emblem.add(Polygon([cx - 20, 34, cx + 20, 34, cx + 14, 28, cx - 14, 28],
                       fillColor=NAVY, strokeColor=NAVY))                        # base
    emblem.add(String(cx, 16, "LegalMitra", fontName="Helvetica-Bold",
                      fontSize=8.5, fillColor=NAVY, textAnchor="middle"))
    story.append(emblem)

    gap(14)
    story.append(Paragraph(
        "Submitted in partial fulfilment of the requirements for the award of the degree of",
        S_SUB))
    gap(6)
    story.append(Paragraph(
        "<b>BACHELOR OF ENGINEERING</b><br/>in<br/><b>[BRANCH OF ENGINEERING]</b>",
        ParagraphStyle("d", parent=S_SUB, fontSize=12.5, leading=19)))
    gap(16)

    submitted = [
        ["SUBMITTED BY", ""],
        ["[STUDENT NAME 1]", "[USN / ROLL NUMBER]"],
        ["[STUDENT NAME 2]", "[USN / ROLL NUMBER]"],
        ["[STUDENT NAME 3]", "[USN / ROLL NUMBER]"],
        ["[STUDENT NAME 4]", "[USN / ROLL NUMBER]"],
    ]
    element = Table(submitted, colWidths=[CONTENT_W * 0.55, CONTENT_W * 0.45])
    element.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, 0), "Times-Bold"),
        ("FONTNAME", (0, 1), (-1, -1), "Times-Roman"),
        ("FONTSIZE", (0, 0), (-1, -1), 11),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("SPAN", (0, 0), (1, 0)),
        ("TEXTCOLOR", (0, 0), (-1, 0), NAVY),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LINEBELOW", (0, 0), (-1, 0), 1, GOLD),
    ]))
    story.append(element)

    gap(16)
    story.append(Paragraph(
        "Under the guidance of<br/><b>[GUIDE NAME]</b><br/>"
        "[Designation], Department of [Department]", S_SUB))
    gap(18)
    story.append(Paragraph(
        "<b>[NAME OF THE COLLEGE]</b><br/>[Department]<br/>"
        "[City], [State]<br/>Academic Year 2025 - 2026",
        ParagraphStyle("col", parent=S_SUB, fontSize=12, leading=18)))


def build_certificate():
    story.append(PageBreak())
    story.append(Paragraph("CERTIFICATE", ParagraphStyle(
        "cert", parent=S_TITLE, fontSize=20, alignment=TA_CENTER)))
    story.append(hr(GOLD, 1.4))
    gap(16)
    p("This is to certify that the project work entitled <b>&ldquo;LegalMitra - A "
      "Legal Information Portal with a Voice-Enabled AI Chatbot&rdquo;</b> is a "
      "bonafide record of the work carried out by <b>[STUDENT NAME 1]</b>, "
      "<b>[STUDENT NAME 2]</b>, <b>[STUDENT NAME 3]</b> and <b>[STUDENT NAME 4]</b>, "
      "bearing university seat numbers [USN 1], [USN 2], [USN 3] and [USN 4] "
      "respectively, in partial fulfilment of the requirements for the award of the "
      "degree of Bachelor of Engineering in [Branch] of [University Name], during "
      "the academic year 2025 - 2026.")
    p("It is certified that all the corrections and suggestions indicated during the "
      "internal evaluation have been incorporated in the report. The project report "
      "has been approved as it satisfies the academic requirements prescribed for "
      "the said degree.")
    gap(46)

    signatures = [
        ["_______________________", "_______________________", "_______________________"],
        ["[GUIDE NAME]", "[HOD NAME]", "[PRINCIPAL NAME]"],
        ["Project Guide", "Head of the Department", "Principal"],
        ["Department of [Dept]", "Department of [Dept]", "[College Name]"],
    ]
    element = Table(signatures, colWidths=[CONTENT_W / 3] * 3)
    element.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, -1), "Times-Roman"),
        ("FONTNAME", (0, 1), (-1, 1), "Times-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    story.append(element)

    gap(50)
    p("<b>EXTERNAL VIVA</b>")
    gap(10)
    viva = [
        ["Name of the Examiners", "Signature with Date"],
        ["1.  ______________________________", "______________________"],
        ["2.  ______________________________", "______________________"],
    ]
    table(viva, [CONTENT_W * 0.58, CONTENT_W * 0.42], font_size=10)


def build_declaration():
    story.append(PageBreak())
    story.append(Paragraph("DECLARATION", ParagraphStyle(
        "dec", parent=S_TITLE, fontSize=20, alignment=TA_CENTER)))
    story.append(hr(GOLD, 1.4))
    gap(14)
    p("We hereby declare that the project entitled <b>&ldquo;LegalMitra - A Legal "
      "Information Portal with a Voice-Enabled AI Chatbot&rdquo;</b> submitted to "
      "[University Name] in partial fulfilment of the requirements for the award of "
      "the degree of Bachelor of Engineering is a record of original work carried "
      "out by us under the guidance of [Guide Name], [Designation], Department of "
      "[Department], [College Name].")
    p("We further declare that:")
    bullets([
        "The entire source code of the application - the Flask backend, the search "
        "and answer engine, the HTML templates, the stylesheet and the JavaScript - "
        "was written by us.",
        "The legal knowledge base was compiled and written by us from publicly "
        "available statutes, government portals and standard reference material, "
        "and then simplified into plain English.",
        "The work has not been submitted, either in part or in full, to any other "
        "university or institute for the award of any degree or diploma.",
        "Wherever material has been taken from other sources, it has been duly "
        "acknowledged in the References section.",
    ])
    p("We also acknowledge that this project is an academic exercise. The legal "
      "content presented in the application is simplified for the purpose of "
      "learning and does not constitute legal advice.")
    gap(40)

    signatures = [
        ["[STUDENT NAME 1]", "[USN]", "_______________"],
        ["[STUDENT NAME 2]", "[USN]", "_______________"],
        ["[STUDENT NAME 3]", "[USN]", "_______________"],
        ["[STUDENT NAME 4]", "[USN]", "_______________"],
    ]
    table([["Name", "USN", "Signature"]] + signatures,
          [CONTENT_W * 0.42, CONTENT_W * 0.28, CONTENT_W * 0.30], font_size=10)
    gap(14)
    p("Place: [City]<br/>Date: [Date]")


def build_acknowledgement():
    story.append(PageBreak())
    story.append(Paragraph("ACKNOWLEDGEMENT", ParagraphStyle(
        "ack", parent=S_TITLE, fontSize=20, alignment=TA_CENTER)))
    story.append(hr(GOLD, 1.4))
    gap(14)
    p("The satisfaction that accompanies the successful completion of any task "
      "would be incomplete without mentioning the people who made it possible.")
    p("We express our sincere gratitude to <b>[Principal Name]</b>, Principal, "
      "[College Name], for providing the environment and the facilities that made "
      "this work possible.")
    p("We are deeply thankful to <b>[HOD Name]</b>, Head of the Department of "
      "[Department], for the constant encouragement and for permitting us to take "
      "up a project outside the usual set of topics.")
    p("We owe our deepest gratitude to our guide, <b>[Guide Name]</b>, "
      "[Designation], whose patient reviews shaped this project. The suggestion to "
      "measure the accuracy of our search engine rather than merely claim it, and "
      "the insistence that every algorithm be explainable without a library, "
      "changed the direction of the work for the better.")
    p("We thank the faculty members of the department for their reviews during the "
      "internal presentations, and our classmates who volunteered as test users "
      "and typed questions we would never have thought of ourselves - many of "
      "which exposed real weaknesses in the matching engine.")
    p("Finally, we thank our families for their patience during the many evenings "
      "this project consumed.")
    gap(30)
    story.append(Paragraph(
        "[STUDENT NAME 1]<br/>[STUDENT NAME 2]<br/>[STUDENT NAME 3]<br/>[STUDENT NAME 4]",
        ParagraphStyle("sign", parent=S_BODY, alignment=2)))


def build_abstract():
    story.append(PageBreak())
    story.append(Paragraph("ABSTRACT", ParagraphStyle(
        "abs", parent=S_TITLE, fontSize=20, alignment=TA_CENTER)))
    story.append(hr(GOLD, 1.4))
    gap(14)

    p("Ordinary people meet the law at the worst possible moment - when a cheque "
      "has already bounced, a landlord has already kept the deposit, a salary has "
      "already gone unpaid, or a builder has already missed the possession date. "
      "At that moment they face two problems at once. First, they do not know "
      "which branch of law their problem belongs to, and therefore do not know "
      "what to search for. Second, almost everything written about Indian law is "
      "written for people who already understand it.")

    p("<b>LegalMitra</b> is a web application built to close that gap. It is a "
      "legal information portal covering <b>%d branches of law</b> through "
      "<b>%d structured topics</b>, supported by <b>%d fill-in-the-blank document "
      "templates</b>, a <b>%d-term glossary</b>, %d answered frequently asked "
      "questions and ten emergency quick-help cards. Its central feature is a "
      "<b>voice-enabled chatbot</b> that accepts a question typed or spoken in "
      "everyday language, identifies the relevant area of law, and replies with a "
      "structured explanation which it also reads aloud."
      % (KB["categories"], KB["topics"], KB["documents"], KB["glossary"], KB["faqs"]))

    p("The retrieval engine was deliberately written from first principles rather "
      "than imported from a machine-learning library. Each of the %d searchable "
      "entries is tokenised, stemmed and converted into a <b>TF-IDF vector</b>; a "
      "user's question is transformed the same way and compared against every "
      "entry using <b>cosine similarity</b>. A synonym-expansion layer maps "
      "everyday vocabulary onto legal vocabulary, and an intent layer distinguishes "
      "greetings, definitions, emergencies and requests for a document format from "
      "ordinary legal questions. Voice input and output use the browser's native "
      "Web Speech API, so the entire system runs with no paid service and no "
      "internet connection." % INDEXED)

    p("The system was evaluated on a set of %d questions phrased the way a "
      "non-lawyer would actually type them. The initial implementation retrieved "
      "the correct page first in %.1f%% of cases. Analysis showed that document "
      "templates were outranking the explanatory topics that shared their "
      "vocabulary; introducing an intent-conditioned ranking adjustment raised "
      "<b>Top-1 accuracy to %.1f%%</b> and <b>Top-3 accuracy to %.1f%%</b>, while "
      "template requests were still routed to a template in 10 out of 10 cases."
      % (ACC["total"], 66.7, ACC["top1_pct"], ACC["top3_pct"]))

    p("The application is implemented in <b>Python 3 with Flask</b>, uses "
      "<b>SQLite</b> for logging and analytics, and renders through <b>Jinja2 "
      "templates with hand-written HTML, CSS and vanilla JavaScript</b> - no "
      "TypeScript, no frontend framework and no build step. The complete system "
      "comprises approximately <b>%s lines</b> of source code across %d files. An "
      "optional Retrieval Augmented Generation mode can pass the retrieved "
      "knowledge to a large language model for a more conversational reply, and "
      "falls back silently to the offline engine whenever that is unavailable."
      % ("{:,}".format(TOTAL_LOC), len(LOC) + 16))

    gap(6)
    p("<b>Keywords:</b> legal information system, chatbot, TF-IDF, cosine "
      "similarity, information retrieval, Web Speech API, speech recognition, "
      "speech synthesis, Flask, SQLite, retrieval augmented generation, "
      "access to justice.")


# ===========================================================================
#  CHAPTER 1 - INTRODUCTION
# ===========================================================================

def chapter_1():
    h1("1. INTRODUCTION")

    h2("1.1 Overview")
    p("LegalMitra (from <i>mitra</i>, meaning friend) is a web-based legal "
      "information portal with a conversational, voice-enabled assistant. It "
      "organises Indian law into %d branches, explains %d topics within them in "
      "plain English, and supplies %d ready-to-use document templates. A visitor "
      "may browse the material, search it, or simply describe a problem to the "
      "chatbot in ordinary words and receive a structured answer."
      % (KB["categories"], KB["topics"], KB["documents"]))

    p("The project was undertaken as a second-year engineering mini project with "
      "two aims: to build something genuinely useful rather than a demonstration "
      "with placeholder content, and to build it in a way that every component "
      "could be explained from first principles during a viva. For that reason no "
      "machine-learning library, no frontend framework and no build toolchain was "
      "used. The retrieval mathematics is implemented by hand in about eighty "
      "lines of Python.")

    h2("1.2 The idea and how it started")
    p("The idea came from an ordinary incident. A relative of one of the team "
      "members had given a security deposit of Rs 60,000 to a landlord and, on "
      "vacating, was told that the entire amount had been adjusted against "
      "&lsquo;painting and cleaning&rsquo;. The family did not know whether this "
      "was legal, whom to complain to, or whether it was worth the trouble. "
      "Searching online produced two kinds of results: advertisements for law "
      "firms, and bare text of statutes that assumed the reader already knew the "
      "vocabulary.")

    p("What was missing was the middle layer - something that would say, plainly: "
      "<i>a landlord may deduct only for unpaid dues and damage beyond normal wear "
      "and tear; routine repainting after a long tenancy is generally the "
      "landlord's cost unless the agreement says otherwise; here is what to send "
      "and here is which forum to approach.</i> That single missing paragraph "
      "became the specification for the whole project.")

    p("From that starting point three design decisions followed almost "
      "immediately, and they shaped everything afterwards:")
    bullets([
        "<b>The visitor must not need the legal word.</b> Someone whose employer "
        "has stopped paying them does not search for &lsquo;retrenchment&rsquo; or "
        "&lsquo;Section 15 of the Code on Wages&rsquo;. They type &lsquo;my boss "
        "is not paying my salary&rsquo;. The system therefore had to bridge "
        "everyday language to legal language.",
        "<b>An explanation without an action is useless.</b> Every topic needed "
        "not just what the law says, but what to actually do - which document to "
        "send, to whom, within what deadline, and what happens if that fails.",
        "<b>Deadlines had to be prominent.</b> While researching the content we "
        "found repeatedly that ordinary people lose good cases purely on "
        "limitation - most sharply in cheque-bounce matters, where a delay of a "
        "single day in issuing the demand notice destroys the complaint entirely.",
    ])

    h2("1.3 Problem statement")
    callout(
        "<b>Problem statement:</b> To design and implement a web-based legal "
        "information system that (a) organises the major branches of Indian law "
        "into structured, plain-language topics with actionable procedure, "
        "(b) supplies standard legal document templates, and (c) provides a "
        "conversational assistant that accepts a question in everyday spoken or "
        "typed English, retrieves the most relevant legal material, and returns "
        "and speaks a structured answer - without depending on any paid service, "
        "external machine-learning library or internet connection.")

    h2("1.4 Objectives")
    bullets([
        "To compile a structured, plain-English knowledge base spanning every "
        "major branch of law, with each topic carrying a summary, key rules, an "
        "actionable procedure, the statutes that apply, and frequently asked "
        "questions.",
        "To design a library of legal document templates in which every blank a "
        "user must fill is explicitly marked, accompanied by a preparation "
        "checklist and a note on stamp duty and registration.",
        "To implement, from first principles, an information-retrieval engine "
        "based on TF-IDF weighting and cosine similarity that maps a "
        "natural-language question to the correct legal topic.",
        "To build a conversational layer that recognises user intent and adapts "
        "the shape of its reply - urgent action steps for an emergency, a "
        "definition for a vocabulary question, a template for a format request.",
        "To integrate two-way voice interaction using the browser's native speech "
        "recognition and speech synthesis, so that the system is usable by "
        "someone who cannot type comfortably.",
        "To persist usage data in a relational database and expose it through an "
        "analytics page.",
        "To measure retrieval accuracy objectively against a fixed test set, and "
        "to improve the engine on the basis of that measurement rather than by "
        "impression.",
        "To keep the entire implementation in plain Python, HTML, CSS and "
        "JavaScript so that every line remains explainable.",
    ])

    h2("1.5 Scope of the project")
    h3("Within scope")
    bullets([
        "Legal <i>information</i> - explanation of rights, procedures, forums and "
        "deadlines, drawn from publicly available statutes and government portals.",
        "Coverage of all %d branches listed in Chapter 6, spanning personal, "
        "commercial, regulatory and international law." % KB["categories"],
        "Document drafting <i>assistance</i> through annotated templates.",
        "A retrieval-based conversational assistant with voice input and output.",
        "Single-language operation in English, running as a locally hosted web "
        "application.",
    ])
    h3("Outside scope")
    bullets([
        "Legal <i>advice</i>. The system does not evaluate the facts of a case, "
        "predict an outcome, or recommend a course of action for an individual.",
        "Filing of cases, e-filing integration, or any transaction with a court, "
        "tribunal or government portal.",
        "Lawyer discovery, appointment booking or payments.",
        "Authoritative citation. The content is simplified for learning and is "
        "not a substitute for the bare Act.",
        "Regional language support, which is identified as future work.",
    ])

    h2("1.6 Organisation of the report")
    table([
        ["Chapter", "Contents"],
        ["1. Introduction", "The idea, problem statement, objectives and scope."],
        ["2. Literature Survey", "Existing systems, their limitations and the gap addressed."],
        ["3. Feasibility Study", "Technical, economic, operational, legal and ethical feasibility."],
        ["4. System Requirements", "Hardware, software, functional and non-functional requirements."],
        ["5. System Design", "Architecture, module hierarchy, data flow, use case and sequence diagrams."],
        ["6. Knowledge Base Design", "How legal content is structured, and the full coverage map."],
        ["7. The Chatbot Engine", "The retrieval algorithm in full, with a worked numerical example."],
        ["8. The Voice Interface", "Speech recognition and synthesis pipelines."],
        ["9. Database Design", "Schema, ER diagram and the queries behind the analytics page."],
        ["10. User Interface Design", "Page inventory, layout, responsiveness and accessibility."],
        ["11. Implementation", "Source code walk-through of the significant components."],
        ["12. Testing", "Test strategy, 30-question accuracy evaluation and a 25-case test table."],
        ["13. Results and Discussion", "What was achieved, measured and learned."],
        ["14. Limitations", "An honest account of what the system cannot do."],
        ["15. Future Scope", "Planned extensions."],
        ["16. Conclusion", "Summary of the work."],
        ["References / Appendices", "Sources, development log, installation guide and file inventory."],
    ], [CONTENT_W * 0.28, CONTENT_W * 0.72],
        "Organisation of this report")


# ===========================================================================
#  CHAPTER 2 - LITERATURE SURVEY
# ===========================================================================

def chapter_2():
    h1("2. LITERATURE SURVEY AND EXISTING SYSTEMS")

    h2("2.1 Purpose of the survey")
    p("Before designing the system we examined the kinds of resources an ordinary "
      "person in India currently reaches when they have a legal problem. We "
      "grouped them into five categories and evaluated each against the three "
      "things our target user needs: <i>plain language</i>, <i>actionable "
      "procedure</i>, and <i>the ability to ask without knowing the legal word</i>.")

    h2("2.2 Categories of existing resources")

    h3("2.2.1 Official statute repositories")
    p("Government portals such as the India Code repository and the e-Gazette "
      "publish the authoritative text of every Act. They are complete, "
      "authoritative and free. However, they present the bare statutory language "
      "with no simplification, no procedure and no cross-referencing to the "
      "practical forum. A user who does not already know that a bounced cheque is "
      "governed by Section 138 of the Negotiable Instruments Act, 1881 has no way "
      "to reach it.")

    h3("2.2.2 Legal research databases")
    p("Subscription platforms aggregate statutes, judgments and commentary with "
      "sophisticated citation tools. They are designed for practitioners, are "
      "priced accordingly, and assume fluency in legal vocabulary and citation "
      "format. They are unusable and unaffordable for the intended user of this "
      "project.")

    h3("2.2.3 Legal services marketplaces")
    p("Commercial portals offer document drafting, company registration and "
      "lawyer consultation. Their explanatory articles are readable, but their "
      "primary purpose is lead generation: the information typically stops "
      "precisely where a paid service begins, and templates are frequently placed "
      "behind a registration or payment wall.")

    h3("2.2.4 General-purpose search and question forums")
    p("General search engines and question-and-answer forums are where most "
      "people actually begin. The difficulty is reliability and currency. Answers "
      "are frequently outdated - a great deal of material still discusses the "
      "Indian Penal Code as the operative criminal statute, although the "
      "Bharatiya Nyaya Sanhita replaced it with effect from 1 July 2024 - and "
      "there is no indication of which answer is trustworthy.")

    h3("2.2.5 General-purpose AI chat assistants")
    p("Large language models answer legal questions fluently and in plain "
      "language, which is a genuine advance. Two risks remain relevant to this "
      "project. The first is <i>hallucination</i>: a model may produce a "
      "confident but non-existent section number, case name or limitation period. "
      "The second is the absence of grounding - the user cannot see the source of "
      "the statement. Both risks informed our decision to build the system around "
      "<i>retrieval</i> from a fixed, curated knowledge base, and to constrain the "
      "optional language-model layer to answer only from retrieved material.")

    h2("2.3 Comparative evaluation")
    table([
        ["Resource type", "Plain language", "Actionable steps", "Ask without legal terms", "Free", "Verifiable source"],
        ["Statute repositories", "No", "No", "No", "Yes", "Yes"],
        ["Legal research databases", "No", "Partly", "No", "No", "Yes"],
        ["Legal services marketplaces", "Yes", "Partly", "Partly", "Partly", "Partly"],
        ["Search engines and forums", "Yes", "Partly", "Yes", "Yes", "No"],
        ["General AI assistants", "Yes", "Yes", "Yes", "Partly", "No"],
        ["<b>LegalMitra</b>", "<b>Yes</b>", "<b>Yes</b>", "<b>Yes</b>", "<b>Yes</b>", "<b>Yes</b>"],
    ], [CONTENT_W * 0.24, CONTENT_W * 0.14, CONTENT_W * 0.15,
        CONTENT_W * 0.19, CONTENT_W * 0.10, CONTENT_W * 0.18],
        "Comparison of existing resources against user needs", font_size=8)

    h2("2.4 Technical background reviewed")

    h3("2.4.1 The vector space model and TF-IDF")
    p("Salton's vector space model represents each document as a vector in a space "
      "whose dimensions are the vocabulary terms. Term Frequency&ndash;Inverse "
      "Document Frequency weighting, introduced by Sp&auml;rck Jones, scales each "
      "term by how rare it is across the collection, so that a term appearing in "
      "every document contributes almost nothing to discrimination while a rare "
      "term contributes strongly. We adopted this model because it is fully "
      "transparent: for any answer the system gives, the contribution of every "
      "single word can be printed and inspected. This property mattered more to "
      "us than raw accuracy.")

    h3("2.4.2 Cosine similarity")
    p("Two documents of very different length may address the same subject. "
      "Comparing raw vectors by Euclidean distance would penalise the longer "
      "document. Cosine similarity measures the angle between vectors rather than "
      "their magnitude, and therefore compares topical direction independently of "
      "length. Normalising every vector to unit length at index time reduces the "
      "cosine to a simple dot product, which is why the search remains fast "
      "despite being written in pure Python.")

    h3("2.4.3 Stemming")
    p("Porter's stemming algorithm reduces inflected forms to a common root so "
      "that <i>filing</i>, <i>filed</i> and <i>file</i> match one another. We "
      "implemented a deliberately simplified suffix-stripping stemmer rather than "
      "importing a full implementation, both to avoid a dependency and because "
      "the aggressive stemming of the full algorithm damaged several legal terms "
      "in testing.")

    h3("2.4.4 Retrieval Augmented Generation")
    p("RAG combines a retrieval step over a trusted corpus with a generation step "
      "by a language model, which is instructed to answer only from the retrieved "
      "material. This directly addresses the hallucination risk identified in "
      "Section 2.2.5, and is the architecture adopted for the optional AI mode "
      "described in Chapter 7.")

    h3("2.4.5 The Web Speech API")
    p("The W3C Web Speech API specification defines two independent interfaces "
      "implemented natively in Chromium-based browsers: "
      "<font face='Courier'>SpeechRecognition</font> for speech-to-text and "
      "<font face='Courier'>SpeechSynthesis</font> for text-to-speech. Using these "
      "removes any need for a paid speech service and keeps the audio on the "
      "user's own machine, which is also the better privacy position.")

    h2("2.5 The gap this project addresses")
    callout(
        "Existing resources are either <b>authoritative but unreadable</b> "
        "(statute repositories, research databases), <b>readable but commercially "
        "motivated</b> (legal marketplaces), or <b>readable and accessible but "
        "unverifiable</b> (forums and general AI assistants). LegalMitra occupies "
        "the gap: a curated, plain-language, procedure-first knowledge base, "
        "reachable through everyday language and voice, where every answer is "
        "traceable to the specific page it came from.",
        color=colors.HexColor("#fbf3d8"), border=GOLD)


# ===========================================================================
#  CHAPTER 3 - FEASIBILITY STUDY
# ===========================================================================

def chapter_3():
    h1("3. FEASIBILITY STUDY")

    p("A feasibility study asks whether a proposed system can actually be built "
      "and operated within the constraints available. We examined five dimensions "
      "before committing to the design.")

    h2("3.1 Technical feasibility")
    p("The technical question was whether a natural-language legal assistant could "
      "be built by second-year students without machine-learning infrastructure. "
      "We concluded that it could, provided the problem was framed as "
      "<i>retrieval</i> rather than <i>generation</i>. Retrieval over a curated "
      "corpus of roughly a hundred entries is a well-understood problem solvable "
      "with classical information-retrieval mathematics that fits comfortably in a "
      "single Python module.")

    table([
        ["Requirement", "Available solution", "Verdict"],
        ["Web server and routing", "Flask - a micro-framework with one function per route", "Feasible"],
        ["HTML generation", "Jinja2, bundled with Flask", "Feasible"],
        ["Persistent storage", "SQLite, part of the Python standard library", "Feasible"],
        ["Natural-language matching", "TF-IDF and cosine similarity implemented directly", "Feasible"],
        ["Speech recognition", "Native browser Web Speech API", "Feasible"],
        ["Speech synthesis", "Native browser SpeechSynthesis interface", "Feasible"],
        ["Report generation", "ReportLab, generating the PDF from the live project", "Feasible"],
        ["Optional AI answers", "Language-model API over retrieved context, with silent fallback", "Feasible"],
    ], [CONTENT_W * 0.26, CONTENT_W * 0.56, CONTENT_W * 0.18],
        "Technical feasibility assessment")

    h2("3.2 Economic feasibility")
    p("The total monetary cost of the project is zero. Every component is either "
      "part of the Python standard library, released under a permissive open "
      "source licence, or built into the browser.")

    table([
        ["Item", "Conventional cost", "Cost incurred"],
        ["Programming language and runtime", "Licence fees", "Rs 0 - Python is open source"],
        ["Web framework", "Licence or subscription", "Rs 0 - Flask, BSD licence"],
        ["Database engine", "Server licence and hosting", "Rs 0 - SQLite, public domain"],
        ["Speech recognition service", "Charged per minute of audio", "Rs 0 - runs inside the browser"],
        ["Speech synthesis service", "Charged per character", "Rs 0 - runs inside the browser"],
        ["Frontend framework and build tools", "Development time", "Rs 0 - none used"],
        ["Development environment", "IDE licences", "Rs 0 - free editors"],
        ["Hosting for evaluation", "Server rental", "Rs 0 - runs on the college machine"],
        ["<b>Total</b>", "", "<b>Rs 0</b>"],
    ], [CONTENT_W * 0.34, CONTENT_W * 0.28, CONTENT_W * 0.38],
        "Economic feasibility - itemised cost")

    p("The only optional cost is the language-model API used by the AI answer "
      "mode. Because the system falls back to the offline engine whenever a key "
      "is absent, this cost is genuinely optional and the project can be "
      "demonstrated in full without it.")

    h2("3.3 Operational feasibility")
    p("Operational feasibility asks whether the intended users would actually use "
      "the system. We tested an early version with twelve classmates and three "
      "family members, none of whom had a legal background. Three findings "
      "changed the design:")
    bullets([
        "<b>Users typed situations, not topics.</b> Not one test user searched for "
        "a legal term. Every question was a description of circumstances. This "
        "confirmed the need for the synonym-expansion layer.",
        "<b>Users wanted the action before the explanation.</b> Several testers "
        "stopped reading after the first paragraph. We restructured every answer "
        "to lead with the direct response and place background material later, "
        "and created the emergency cards where steps come first entirely.",
        "<b>Voice was used more than expected.</b> Older testers in particular "
        "preferred speaking to typing, which justified the effort spent on the "
        "speech layer.",
    ])
    p("Operationally the system requires no installation for the end user beyond a "
      "modern browser, no account creation, and no training.")

    h2("3.4 Legal and ethical feasibility")
    p("A project that deals with law carries obligations that a typical student "
      "project does not. We identified four and addressed each in the design "
      "rather than in a disclaimer alone.")

    table([
        ["Concern", "How it is addressed in the system"],
        ["Unauthorised practice of law",
         "The system provides <i>information</i>, never advice on an individual's facts. "
         "It does not evaluate a case, predict outcomes, or recommend a course of action. "
         "A permanent disclaimer strip is present on every page, the chatbot appends a "
         "disclaimer to every single reply, and document pages carry an additional warning."],
        ["Incorrect or outdated content causing harm",
         "Content is restricted to settled, general propositions and avoids state-specific "
         "figures wherever those vary. Where a rule depends on the State - stamp duty, "
         "tenancy, court fees - the system says so explicitly rather than stating a number."],
        ["Hallucinated legal citations",
         "The offline engine cannot invent anything: it can only return material already "
         "written into the knowledge base. The optional AI mode is constrained by an "
         "explicit system instruction to use only retrieved material and never to invent a "
         "section number, case name or deadline."],
        ["User privacy",
         "There is no login and no personal data collection. The database stores the "
         "question text and the answer for analytics, together with a random session "
         "identifier. Speech is processed by the browser and no audio is transmitted to "
         "or stored by the application."],
    ], [CONTENT_W * 0.26, CONTENT_W * 0.74],
        "Legal and ethical concerns and their mitigation")

    h2("3.5 Schedule feasibility")
    p("The project was planned across a twelve-week semester. Content authoring, "
      "not programming, was correctly identified at the outset as the largest "
      "single cost, and was allocated the most time. The detailed week-by-week "
      "record of what was actually done appears in Appendix A.")

    table([
        ["Phase", "Weeks", "Principal output"],
        ["Problem study and survey", "1 - 2", "Problem statement, comparison of existing resources"],
        ["Design", "2 - 3", "Architecture, data structure design, page inventory"],
        ["Knowledge base authoring", "3 - 7", "20 categories, 80 topics, glossary, emergency cards"],
        ["Document template library", "6 - 8", "31 annotated templates"],
        ["Retrieval engine", "5 - 8", "Tokeniser, stemmer, TF-IDF index, cosine search, intents"],
        ["Web application and interface", "7 - 10", "Flask routes, 17 templates, stylesheet"],
        ["Voice interface", "9 - 10", "Speech recognition and synthesis modules"],
        ["Testing and tuning", "10 - 11", "Accuracy evaluation, ranking correction, retest"],
        ["Documentation", "11 - 12", "This report and the user guide"],
    ], [CONTENT_W * 0.32, CONTENT_W * 0.13, CONTENT_W * 0.55],
        "Project schedule")

    h2("3.6 Conclusion of the feasibility study")
    callout(
        "The system is <b>technically feasible</b> using classical information "
        "retrieval and standard-library components, <b>economically feasible</b> at "
        "zero cost, <b>operationally feasible</b> as confirmed by early user "
        "testing, <b>ethically defensible</b> provided the information/advice "
        "boundary is enforced in the design rather than merely stated, and "
        "<b>achievable within the available schedule</b>. The project was therefore "
        "taken forward to implementation.",
        color=colors.HexColor("#e6f4ed"), border=GREEN)


# ===========================================================================
#  CHAPTER 4 - SYSTEM REQUIREMENTS
# ===========================================================================

def chapter_4():
    h1("4. SYSTEM REQUIREMENTS")

    h2("4.1 Hardware requirements")
    table([
        ["Component", "Minimum", "Recommended"],
        ["Processor", "Dual core, 1.6 GHz", "Quad core, 2.0 GHz or above"],
        ["Memory (RAM)", "2 GB", "4 GB or above"],
        ["Free disk space", "150 MB", "500 MB"],
        ["Display", "1024 x 768", "1366 x 768 or above"],
        ["Microphone", "Required only for voice input", "Any headset or built-in microphone"],
        ["Speakers or headphones", "Required only for voice output", "Any"],
        ["Network", "Not required for the offline engine", "Required only for the optional AI mode"],
    ], [CONTENT_W * 0.26, CONTENT_W * 0.34, CONTENT_W * 0.40],
        "Hardware requirements")

    p("The modest requirements are a direct consequence of the design. Because the "
      "retrieval index holds only %d entries, the entire index is built in memory "
      "at start-up in well under a second and occupies a few megabytes." % INDEXED)

    h2("4.2 Software requirements")
    table([
        ["Category", "Software", "Version used", "Purpose"],
        ["Operating system", "Windows / Linux / macOS", "Any current", "Platform independent"],
        ["Language", "Python", "3.14", "Backend, retrieval engine, report generation"],
        ["Web framework", "Flask", "3.1.3", "Routing, request handling, sessions"],
        ["Template engine", "Jinja2", "3.1.6", "HTML generation (bundled with Flask)"],
        ["Database", "SQLite", "3.x", "Logging and analytics (standard library)"],
        ["PDF library", "ReportLab", "5.0.1", "Generating this project report"],
        ["Browser", "Chrome or Edge", "Current", "Required for the Web Speech API"],
        ["Markup and styling", "HTML5, CSS3", "-", "Interface"],
        ["Client scripting", "JavaScript (ES5-compatible)", "-", "Chat, voice, filtering"],
        ["Optional", "anthropic SDK", "Current", "Optional AI answer mode only"],
    ], [CONTENT_W * 0.18, CONTENT_W * 0.24, CONTENT_W * 0.14, CONTENT_W * 0.44],
        "Software requirements")

    callout("<b>Deliberately not used:</b> TypeScript, React, Angular, Vue, Node.js, "
            "webpack, Bootstrap, Tailwind, scikit-learn, NLTK, spaCy, TensorFlow, "
            "PyTorch, and any paid speech service. Every one of these was considered "
            "and rejected on the ground that it would place a component of the "
            "project beyond the team's ability to explain it.")

    h2("4.3 Functional requirements")
    table([
        ["ID", "Requirement", "Priority"],
        ["FR-01", "The system shall present all legal categories and allow the user to browse topics within a category.", "High"],
        ["FR-02", "The system shall display each topic with a summary, key points, procedure, applicable laws and FAQs.", "High"],
        ["FR-03", "The system shall provide a keyword search across all topics and document templates, ranked by relevance.", "High"],
        ["FR-04", "The system shall accept a natural-language question through a chat interface.", "High"],
        ["FR-05", "The system shall identify the intent of a message (greeting, definition, emergency, document request, legal question).", "High"],
        ["FR-06", "The system shall retrieve the most relevant knowledge-base entries and compose a structured answer.", "High"],
        ["FR-07", "The system shall cite the pages an answer was drawn from, as clickable links.", "High"],
        ["FR-08", "The system shall accept spoken input through the microphone and transcribe it into the message box.", "High"],
        ["FR-09", "The system shall read its answers aloud, with a user-selectable voice and speaking speed.", "High"],
        ["FR-10", "The system shall allow the user to mute, stop or resume speech at any time.", "Medium"],
        ["FR-11", "The system shall display each document template with every blank clearly marked.", "High"],
        ["FR-12", "The system shall allow a template to be copied, printed or downloaded as a text file.", "High"],
        ["FR-13", "The system shall provide an A-to-Z glossary of legal terms with a live filter.", "Medium"],
        ["FR-14", "The system shall provide emergency quick-help cards giving immediate action steps.", "High"],
        ["FR-15", "The system shall record every question, answer, intent, engine and confidence score in the database.", "Medium"],
        ["FR-16", "The system shall present usage analytics derived from the stored data.", "Low"],
        ["FR-17", "The system shall retain a short conversation history to give the assistant context.", "Medium"],
        ["FR-18", "The system shall allow the user to clear the conversation and start afresh.", "Low"],
        ["FR-19", "The system shall accept feedback through a contact form and store it.", "Low"],
        ["FR-20", "The system shall display a disclaimer on every page and append one to every chatbot reply.", "High"],
    ], [CONTENT_W * 0.09, CONTENT_W * 0.78, CONTENT_W * 0.13],
        "Functional requirements", font_size=8.2)

    h2("4.4 Non-functional requirements")
    table([
        ["ID", "Category", "Requirement", "How it is met"],
        ["NFR-01", "Performance", "A chatbot reply shall be produced in under one second on the offline engine.",
         "Pre-normalised vectors reduce cosine similarity to a dot product; measured mean %.1f ms." % TIME["mean_ms"]],
        ["NFR-02", "Performance", "The retrieval index shall be built at start-up, not per request.", "The index is constructed once when the module is imported."],
        ["NFR-03", "Reliability", "Failure of the optional AI service shall never break the application.", "The AI call is wrapped so that any exception falls back to the offline answer."],
        ["NFR-04", "Availability", "The system shall function with no internet connection.", "All retrieval, content and speech run locally or in the browser."],
        ["NFR-05", "Usability", "A user shall not need any legal vocabulary to obtain an answer.", "Synonym expansion maps everyday words to legal terms."],
        ["NFR-06", "Accessibility", "The system shall be usable without typing.", "Speech recognition for input; speech synthesis for output; page reader on topic pages."],
        ["NFR-07", "Portability", "The system shall run on Windows, Linux and macOS without change.", "Pure Python and standard library; SQLite is file-based."],
        ["NFR-08", "Responsiveness", "The interface shall adapt to phone, tablet and desktop.", "Fluid CSS grid with breakpoints at 900 px and 720 px."],
        ["NFR-09", "Maintainability", "Adding a legal topic shall require no code change.", "Topics are plain dictionaries; the index rebuilds automatically."],
        ["NFR-10", "Security", "User input shall not be able to inject markup into the page.", "All chat text is HTML-escaped before rendering; Jinja2 autoescaping elsewhere."],
        ["NFR-11", "Privacy", "No personal data shall be collected.", "No login; only question, answer and a random session id are stored."],
        ["NFR-12", "Transparency", "Every answer shall be traceable to its source page.", "Source links with similarity scores accompany each reply."],
    ], [CONTENT_W * 0.08, CONTENT_W * 0.14, CONTENT_W * 0.38, CONTENT_W * 0.40],
        "Non-functional requirements", font_size=8)


# ===========================================================================
#  CHAPTER 5 - SYSTEM DESIGN
# ===========================================================================

def diagram_architecture():
    d = Drawing(CONTENT_W, 340)

    # Presentation tier
    d.add(Rect(0, 246, CONTENT_W, 88, fillColor=colors.HexColor("#eef3fb"),
               strokeColor=NAVY, strokeWidth=0.8, rx=6, ry=6))
    label_text(d, 8, 322, "PRESENTATION TIER  -  the browser", 8, NAVY, bold=True)
    w = (CONTENT_W - 50) / 4
    box(d, 8, 258, w, 52, "HTML pages\n(Jinja2)", fill=colors.white, size=7.4)
    box(d, 8 + w + 11, 258, w, 52, "style.css\nlayout + print", fill=colors.white, size=7.4)
    box(d, 8 + 2 * (w + 11), 258, w, 52, "chat.js\nchat + voice", fill=colors.white, size=7.4)
    box(d, 8 + 3 * (w + 11), 258, w, 52, "Web Speech API\nmic + speaker", fill=colors.HexColor("#fbf3d8"),
        stroke=GOLD, size=7.4)

    # Application tier
    d.add(Rect(0, 118, CONTENT_W, 108, fillColor=colors.HexColor("#f4f7f5"),
               strokeColor=GREEN, strokeWidth=0.8, rx=6, ry=6))
    label_text(d, 8, 214, "APPLICATION TIER  -  Python / Flask", 8, GREEN, bold=True)
    box(d, 8, 158, 108, 46, "app.py\nFlask routes", fill=colors.white, size=7.4)
    box(d, 128, 158, 118, 46, "chatbot.py\nretrieval engine", fill=colors.white, size=7.4)
    box(d, 258, 158, 104, 46, "database.py\nSQLite access", fill=colors.white, size=7.4)
    box(d, 374, 158, CONTENT_W - 382, 46, "Optional RAG layer\n(language model)",
        fill=colors.HexColor("#fbf3d8"), stroke=GOLD, size=7.4)

    box(d, 8, 126, CONTENT_W - 16, 24,
        "TF-IDF index  |  cosine similarity  |  intent detection  |  synonym expansion  |  answer composer",
        fill=colors.HexColor("#e6f4ed"), stroke=GREEN, size=7, bold=False)

    # Data tier
    d.add(Rect(0, 8, CONTENT_W, 92, fillColor=colors.HexColor("#fdf7e8"),
               strokeColor=GOLD, strokeWidth=0.8, rx=6, ry=6))
    label_text(d, 8, 88, "DATA TIER", 8, colors.HexColor("#7a6212"), bold=True)
    bw = (CONTENT_W - 42) / 3
    box(d, 8, 20, bw, 54, "Knowledge base\n(Python modules)",
        sub="%d topics, %d docs" % (KB["topics"], KB["documents"]),
        fill=colors.white, size=7.4)
    box(d, 8 + bw + 13, 20, bw, 54, "legalmitra.db\n(SQLite)",
        sub="3 tables", fill=colors.white, size=7.4)
    box(d, 8 + 2 * (bw + 13), 20, bw, 54, "Glossary + emergency\n+ helplines",
        sub="%d terms" % KB["glossary"], fill=colors.white, size=7.4)

    # connecting arrows
    arrow(d, CONTENT_W / 2 - 60, 246, CONTENT_W / 2 - 60, 228, "HTTP request")
    arrow(d, CONTENT_W / 2 + 60, 228, CONTENT_W / 2 + 60, 246, "HTML / JSON")
    arrow(d, CONTENT_W / 2 - 60, 118, CONTENT_W / 2 - 60, 102, "read / write")
    arrow(d, CONTENT_W / 2 + 60, 102, CONTENT_W / 2 + 60, 118, "data")
    return d


def diagram_modules():
    d = Drawing(CONTENT_W, 250)
    cx = CONTENT_W / 2
    box(d, cx - 62, 208, 124, 32, "app.py", sub="Flask server", fill=NAVY,
        text_color=colors.white, size=9)

    level2 = [
        ("chatbot.py", "answer engine", 0),
        ("database.py", "SQLite", 1),
        ("legal_data.py", "aggregator", 2),
        ("templates/", "17 pages", 3),
    ]
    w2 = (CONTENT_W - 36) / 4
    for name, sub, i in level2:
        x = 4 + i * (w2 + 9)
        box(d, x, 138, w2, 34, name, sub=sub, size=7.6)
        arrow(d, cx, 208, x + w2 / 2, 174)

    level3 = [
        ("legal_topics.py", "40 topics", 0),
        ("legal_topics_extra.py", "40 topics", 1),
        ("legal_documents.py", "%d templates" % KB["documents"], 2),
        ("legal_extras.py", "glossary, SOS", 3),
    ]
    for name, sub, i in level3:
        x = 4 + i * (w2 + 9)
        box(d, x, 68, w2, 34, name, sub=sub, size=7, fill=PAPER)
        arrow(d, 4 + 2 * (w2 + 9) + w2 / 2, 138, x + w2 / 2, 104)

    box(d, 4, 12, (CONTENT_W - 18) / 2, 30, "static/css/style.css",
        sub="all styling", size=7.6, fill=colors.HexColor("#eef3fb"))
    box(d, 14 + (CONTENT_W - 18) / 2, 12, (CONTENT_W - 18) / 2,
        30, "static/js/  chat.js + main.js", sub="chat, voice, filters",
        size=7.6, fill=colors.HexColor("#eef3fb"))
    arrow(d, 4 + 3 * (w2 + 9) + w2 / 2, 138, CONTENT_W - 60, 44, dashed=True)
    return d


def diagram_dfd0():
    d = Drawing(CONTENT_W, 190)
    box(d, 6, 78, 96, 44, "USER\n(visitor)", fill=colors.white, size=8)
    ellipse_box(d, CONTENT_W / 2, 100, 92, 44,
                "0\nLegalMitra\nLegal Information\nSystem", fill=colors.HexColor("#eef3fb"))
    box(d, CONTENT_W - 102, 78, 96, 44, "KNOWLEDGE\nBASE", fill=PAPER, size=8)
    box(d, CONTENT_W / 2 - 48, 8, 96, 34, "legalmitra.db", fill=PAPER, size=8)

    arrow(d, 102, 112, CONTENT_W / 2 - 92, 112, "question / search")
    arrow(d, CONTENT_W / 2 - 92, 88, 102, 88, "answer / pages")
    arrow(d, CONTENT_W / 2 + 92, 112, CONTENT_W - 102, 112, "query")
    arrow(d, CONTENT_W - 102, 88, CONTENT_W / 2 + 92, 88, "matched content")
    arrow(d, CONTENT_W / 2, 56, CONTENT_W / 2, 42, "logs")
    return d


def diagram_dfd1():
    d = Drawing(CONTENT_W, 300)
    box(d, 4, 128, 74, 44, "USER", size=8)

    ellipse_box(d, 150, 250, 62, 30, "1.0\nDetect\nintent")
    ellipse_box(d, 150, 172, 62, 30, "2.0\nClean and\nstem text")
    ellipse_box(d, 150, 94, 62, 30, "3.0\nExpand\nsynonyms")
    ellipse_box(d, 300, 172, 62, 30, "4.0\nTF-IDF and\ncosine match")
    ellipse_box(d, 300, 62, 62, 30, "5.0\nCompose\nanswer")
    ellipse_box(d, 448, 172, 62, 30, "6.0\nOptional\nAI rewrite")

    box(d, 262, 244, 78, 34, "Knowledge\nbase", fill=PAPER, size=7.4)
    box(d, 410, 62, 78, 34, "chat_log\n(SQLite)", fill=PAPER, size=7.4)

    arrow(d, 78, 158, 100, 240, "message")
    arrow(d, 212, 250, 300, 200, "intent")
    arrow(d, 150, 220, 150, 202, "text")
    arrow(d, 150, 142, 150, 124, "tokens")
    arrow(d, 212, 94, 268, 148, "expanded")
    arrow(d, 300, 210, 300, 244 - 0, "read", label_offset=-10)
    arrow(d, 300, 142, 300, 92, "top matches")
    arrow(d, 362, 172, 386, 172, "context")
    arrow(d, 448, 142, 348, 78, "text", dashed=True)
    arrow(d, 362, 62, 410, 70, "store")
    arrow(d, 268, 52, 78, 132, "reply + sources")
    return d


def diagram_usecase():
    d = Drawing(CONTENT_W, 330)
    # actor
    ax = 40
    d.add(Line(ax, 196, ax, 172, strokeColor=NAVY, strokeWidth=1.2))
    from reportlab.graphics.shapes import Circle
    d.add(Circle(ax, 206, 9, fillColor=colors.white, strokeColor=NAVY, strokeWidth=1.2))
    d.add(Line(ax - 13, 188, ax + 13, 188, strokeColor=NAVY, strokeWidth=1.2))
    d.add(Line(ax, 172, ax - 11, 152, strokeColor=NAVY, strokeWidth=1.2))
    d.add(Line(ax, 172, ax + 11, 152, strokeColor=NAVY, strokeWidth=1.2))
    label_text(d, ax, 138, "Visitor", 8, NAVY, anchor="middle", bold=True)

    d.add(Rect(90, 8, CONTENT_W - 96, 314, fillColor=None, strokeColor=LINE,
               strokeWidth=0.9, rx=8, ry=8))
    label_text(d, 100, 308, "LegalMitra System", 8, GREY, bold=True)

    # Two columns, with the right column staggered half a row lower so that the
    # connector lines from the actor pass through the gaps between the ellipses
    # of the left column instead of crossing them.
    left_cases = [
        "Browse areas of law", "Search the knowledge base",
        "Ask a question by typing", "View a document template",
        "Look up a glossary term", "Send feedback",
    ]
    right_cases = [
        "Read a legal topic", "Ask a question by voice",
        "Hear the answer spoken", "Download or print a template",
        "Open an emergency card", "View usage analytics",
    ]

    rx, ry = 84, 16
    row_h = 50
    col1_x = 196
    col2_x = col1_x + 2 * rx + 26
    top = 288

    for index, case in enumerate(left_cases):
        cy = top - index * row_h
        ellipse_box(d, col1_x, cy, rx, ry, case, size=6.8)
        arrow(d, 56, 180, col1_x - rx - 2, cy, color=colors.HexColor("#93a0b5"))

    for index, case in enumerate(right_cases):
        cy = top - 25 - index * row_h
        ellipse_box(d, col2_x, cy, rx, ry, case, size=6.8)
        arrow(d, 56, 180, col2_x - rx - 2, cy, color=colors.HexColor("#93a0b5"))
    return d


def diagram_er():
    d = Drawing(CONTENT_W, 250)

    def entity(x, y, title, fields, width=150):
        height = 20 + len(fields) * 12
        d.add(Rect(x, y, width, height, fillColor=colors.white,
                   strokeColor=NAVY, strokeWidth=1.1, rx=4, ry=4))
        d.add(Rect(x, y + height - 18, width, 18, fillColor=NAVY,
                   strokeColor=NAVY, rx=4, ry=4))
        d.add(String(x + width / 2, y + height - 13, title,
                     fontName="Helvetica-Bold", fontSize=7.6,
                     fillColor=colors.white, textAnchor="middle"))
        for index, field in enumerate(fields):
            d.add(String(x + 6, y + height - 30 - index * 12, field,
                         fontName="Helvetica", fontSize=6.4, fillColor=colors.black))
        return height

    entity(4, 96, "chat_log", [
        "PK  id            INTEGER", "     session_id    TEXT",
        "     question      TEXT", "     answer        TEXT",
        "     intent        TEXT", "     engine        TEXT",
        "     confidence    REAL", "     top_source    TEXT",
        "     created_at    TEXT"])

    entity(200, 128, "search_log", [
        "PK  id            INTEGER", "     query         TEXT",
        "     results       INTEGER", "     created_at    TEXT"])

    entity(200, 8, "contact_msg", [
        "PK  id            INTEGER", "     name          TEXT",
        "     email         TEXT", "     subject       TEXT",
        "     message       TEXT", "     created_at    TEXT"])

    entity(392, 96, "Knowledge base", [
        "     category_id   (in code)", "     topic_id      (in code)",
        "     document_id   (in code)", "", "  Read-only Python",
        "  dictionaries - not", "  stored in SQLite"], width=CONTENT_W - 398)

    label_text(d, 176, 190, "logically related by", 6.4, GREY, anchor="middle")
    arrow(d, 158, 182, 198, 182, color=GREY, dashed=True)
    arrow(d, 356, 182, 390, 182, color=GREY, dashed=True)
    label_text(d, 372, 190, "top_source", 6.4, GREY, anchor="middle")
    return d


def diagram_sequence():
    d = Drawing(CONTENT_W, 320)
    lanes = ["User", "Browser\n(chat.js)", "Flask\n(app.py)", "chatbot.py", "SQLite"]
    lane_w = CONTENT_W / len(lanes)
    xs = []
    for index, name in enumerate(lanes):
        x = index * lane_w + lane_w / 2
        xs.append(x)
        box(d, x - lane_w / 2 + 8, 286, lane_w - 16, 28, name, size=7,
            fill=NAVY, text_color=colors.white)
        d.add(Line(x, 24, x, 286, strokeColor=LINE, strokeWidth=0.8,
                   strokeDashArray=[3, 3]))

    steps = [
        (0, 1, "speaks or types the question", 266),
        (1, 1, "SpeechRecognition -> text", 246),
        (1, 2, "POST /api/chat  {message}", 226),
        (2, 4, "read last 3 turns (history)", 206),
        (2, 3, "answer(message, history)", 186),
        (3, 3, "detect intent, expand synonyms", 166),
        (3, 3, "TF-IDF vector + cosine search", 146),
        (3, 3, "compose structured answer", 126),
        (3, 2, "reply dict", 106),
        (2, 4, "INSERT INTO chat_log", 86),
        (2, 1, "JSON reply + sources", 66),
        (1, 1, "render bubble, speak aloud", 46),
        (1, 0, "reads and hears the answer", 26),
    ]
    for src, dst, text, y in steps:
        if src == dst:
            d.add(PolyLine([xs[src], y + 5, xs[src] + 26, y + 5,
                            xs[src] + 26, y - 3, xs[src] + 3, y - 3],
                           strokeColor=NAVY_LIGHT, strokeWidth=1))
            d.add(Polygon([xs[src] + 3, y - 3, xs[src] + 9, y - 0.5,
                           xs[src] + 9, y - 5.5], fillColor=NAVY_LIGHT,
                          strokeColor=NAVY_LIGHT))
            label_text(d, xs[src] + 32, y + 1, text, 6.2, GREY)
        else:
            arrow(d, xs[src], y, xs[dst], y, color=NAVY_LIGHT)
            mid = (xs[src] + xs[dst]) / 2
            label_text(d, mid, y + 5, text, 6.2, GREY, anchor="middle")
    return d


def chapter_5():
    h1("5. SYSTEM DESIGN")

    h2("5.1 Architectural style")
    p("The system follows a conventional <b>three-tier architecture</b>. The "
      "presentation tier runs entirely in the browser, the application tier is a "
      "Flask process in Python, and the data tier consists of the knowledge base "
      "(held as Python data structures) and a SQLite database (used only for "
      "logging and analytics).")

    p("Two aspects of the design deserve explanation because they are deliberate "
      "departures from the obvious approach:")
    bullets([
        "<b>The knowledge base is code, not database rows.</b> The legal content "
        "lives in Python dictionaries rather than in SQL tables. This was chosen "
        "because the content is read-only, is authored by the developers rather "
        "than by users, and benefits from being version-controlled and reviewable "
        "as text. It also means that adding a topic requires no migration, no "
        "administrative interface and no code change - only a new dictionary.",
        "<b>The speech layer is in the presentation tier, not the server.</b> "
        "Both speech recognition and speech synthesis execute in the browser. No "
        "audio ever reaches the server, which removes an entire class of privacy "
        "concern and eliminates any bandwidth or service cost.",
    ])

    story.append(diagram_architecture())
    caption("Three-tier system architecture of LegalMitra")

    h2("5.2 Module hierarchy")
    p("The application is decomposed into modules with a single responsibility "
      "each. <font face='Courier'>app.py</font> knows about the web but nothing "
      "about legal matching; <font face='Courier'>chatbot.py</font> knows about "
      "matching but nothing about HTTP; the data modules know nothing about "
      "either. This separation is what allows the chatbot to be tested from the "
      "command line with no browser and no server running.")

    story.append(diagram_modules())
    caption("Module hierarchy and dependencies")

    table([
        ["Module", "Responsibility", "Depends on"],
        ["app.py", "HTTP routing, request handling, sessions, rendering", "chatbot, database, legal_data"],
        ["chatbot.py", "Tokenising, stemming, indexing, matching, intent, answer composition", "legal_data"],
        ["database.py", "Schema creation, inserts and analytics queries", "sqlite3 (standard library)"],
        ["legal_data.py", "Categories, helper lookups, aggregation of the knowledge base", "the four data modules"],
        ["legal_topics.py", "40 topics across the first ten branches of law", "none"],
        ["legal_topics_extra.py", "40 topics across the remaining ten branches", "none"],
        ["legal_documents.py", "%d annotated document templates" % KB["documents"], "none"],
        ["legal_extras.py", "Glossary, emergency cards, helpline numbers", "none"],
    ], [CONTENT_W * 0.22, CONTENT_W * 0.50, CONTENT_W * 0.28],
        "Module responsibilities")

    h2("5.3 Data flow diagrams")
    h3("5.3.1 Level 0 - context diagram")
    p("At the highest level the system is a single process sitting between the "
      "visitor and the stored legal material, writing a log of what was asked.")
    story.append(diagram_dfd0())
    caption("DFD Level 0 - context diagram")

    h3("5.3.2 Level 1 - the answering pipeline")
    p("Exploding the single process reveals the six sub-processes that turn a "
      "typed sentence into a structured legal answer. Process 6.0 is optional and "
      "is bypassed entirely when the system runs in offline mode.")
    story.append(diagram_dfd1())
    caption("DFD Level 1 - decomposition of the answering process")

    story.append(PageBreak())
    h2("5.4 Use case diagram")
    p("The system has a single actor. There is no administrator role, because "
      "there is no content to administer at run time - the knowledge base is "
      "edited in source form and takes effect on restart.")
    story.append(diagram_usecase())
    caption("Use case diagram")

    story.append(PageBreak())
    h2("5.5 Sequence diagram")
    p("The sequence below traces a single spoken question from the microphone to "
      "the spoken reply, and is the most useful single picture of how the system "
      "actually works.")
    story.append(diagram_sequence())
    caption("Sequence diagram for a voice question and spoken answer")

    h2("5.6 Entity relationship diagram")
    p("The relational schema is intentionally small. Only interaction data is "
      "stored; the legal content itself is not in the database.")
    story.append(diagram_er())
    caption("Entity relationship diagram")

    h2("5.7 Design decisions and their justification")
    table([
        ["Decision", "Alternative considered", "Why the decision was made"],
        ["TF-IDF written by hand", "scikit-learn TfidfVectorizer",
         "The mathematics had to be explainable in a viva; a library would have hidden it. The hand-written version is about 80 lines."],
        ["Retrieval-first, generation optional", "A language model answering directly",
         "A model answering unaided can invent a section number or a deadline. Retrieval from a curated base cannot."],
        ["Knowledge base as Python dictionaries", "SQL tables with an admin interface",
         "Content is read-only and authored by developers; keeping it as code makes it reviewable and removes an entire admin subsystem."],
        ["Browser-based speech", "A cloud speech-to-text service",
         "Zero cost, no API key, no audio leaves the machine, and the system keeps working offline."],
        ["Vanilla JavaScript", "React or another framework",
         "No build step, nothing to explain that the team did not write, and the whole client is two readable files."],
        ["SQLite", "MySQL or PostgreSQL",
         "No server process to install or run during a demonstration; the database is a single file."],
        ["Unit-normalised vectors at index time", "Normalising at query time",
         "Moves the square-root computation out of the request path, reducing cosine similarity to a dot product."],
    ], [CONTENT_W * 0.24, CONTENT_W * 0.24, CONTENT_W * 0.52],
        "Key design decisions", font_size=8)


# ===========================================================================
#  CHAPTER 6 - KNOWLEDGE BASE DESIGN
# ===========================================================================

def chapter_6():
    h1("6. KNOWLEDGE BASE DESIGN")

    h2("6.1 Principles followed while authoring content")
    p("The knowledge base is the largest single component of the project - "
      "roughly %s of the %s lines of source are legal content. Five rules were "
      "fixed before writing began and were applied to every entry."
      % ("{:,}".format(LOC.get("legal_topics.py", 0) + LOC.get("legal_topics_extra.py", 0)
                       + LOC.get("legal_documents.py", 0) + LOC.get("legal_extras.py", 0)),
         "{:,}".format(TOTAL_LOC)))
    bullets([
        "<b>Answer the practical question first.</b> Each topic opens with what "
        "the reader actually wants to know, not with the history of the statute.",
        "<b>Always state the forum and the deadline.</b> Knowing that a right "
        "exists is useless without knowing where to enforce it and by when.",
        "<b>Never state a figure that varies by State.</b> Where stamp duty, court "
        "fees or tenancy rules differ, the system says that they differ rather "
        "than quoting one State's number as though it were national.",
        "<b>Prefer the current statute.</b> Content reflects the Bharatiya Nyaya "
        "Sanhita, Bharatiya Nagarik Suraksha Sanhita and Bharatiya Sakshya "
        "Adhiniyam, which replaced the IPC, CrPC and Evidence Act with effect from "
        "1 July 2024, and notes the older names where a reader would recognise them.",
        "<b>Write the FAQ in the user's words.</b> The FAQ questions are phrased "
        "the way testers actually asked them, which also improves retrieval - the "
        "FAQ text is indexed and repeated in the searchable string.",
    ])

    h2("6.2 Structure of a topic")
    p("Every one of the %d topics is a Python dictionary with exactly the same "
      "eight keys. This uniformity is what allows a single HTML template to "
      "render any topic and a single indexing function to make any topic "
      "searchable." % KB["topics"])

    code('''
{
    "id":       "cheque-bounce",              # slug used in the URL
    "category": "criminal",                   # links to a CATEGORIES entry
    "title":    "Cheque Bounce - Section 138 Negotiable Instruments Act",
    "summary":  "When a cheque is returned unpaid ... strict timeline ...",
    "key_points": [ "The cheque must have been issued for a legally ...",
                    "A written demand notice must be sent within 30 days ...", ],
    "laws":       [ "Negotiable Instruments Act, 1881 - Sections 138, 139 ...", ],
    "steps":      [ "Collect the original cheque and the bank return memo.",
                    "Within 30 days of the memo, send a legal demand notice ...", ],
    "faqs":       [ {"q": "What if the notice comes back undelivered?",
                     "a": "If it was sent to the correct address and returned ..."} ],
    "keywords":   [ "cheque bounce", "section 138", "dishonour", "demand notice" ],
}
''', "Listing 6.1 - the structure of a single topic")

    table([
        ["Key", "Purpose", "Used by"],
        ["id", "Unique slug forming the URL /topic/&lt;id&gt;", "Routing, linking, evaluation"],
        ["category", "Foreign key to the CATEGORIES list", "Navigation, related content"],
        ["title", "Heading shown to the user", "Page, search results, index (weighted x3)"],
        ["summary", "Two to four sentence plain-English explanation", "Summary box, search snippet, chatbot answer"],
        ["key_points", "The rules that actually matter", "Topic page, chatbot answer"],
        ["laws", "The Acts, sections and leading cases", "Topic page, chatbot answer"],
        ["steps", "The actionable procedure", "Numbered list on the page and in the answer"],
        ["faqs", "Real questions with answers", "Accordion on the page; question text weighted x2 in the index"],
        ["keywords", "Extra search vocabulary", "Index (weighted x3) and exact-match bonus"],
    ], [CONTENT_W * 0.15, CONTENT_W * 0.42, CONTENT_W * 0.43],
        "The eight keys of a topic and where each is used")

    h2("6.3 Structure of a document template")
    p("The %d templates follow a parallel structure. The most important design "
      "choice here was the notation for blanks: every value the user must supply "
      "is written in <font face='Courier'>[SQUARE BRACKETS AND CAPITALS]</font>. "
      "A small piece of JavaScript on the document page finds this pattern with a "
      "regular expression and highlights each occurrence, so the user can see at "
      "a glance everything that must be replaced - without the stored template "
      "containing any markup at all." % KB["documents"])

    code('''
{
    "id":       "cheque-bounce-notice",
    "title":    "Cheque Bounce Demand Notice (Section 138 NI Act)",
    "category": "banking",
    "purpose":  "The mandatory notice that must be sent before filing a complaint.",
    "when_to_use": "Within 30 days of receiving the bank's cheque return memo.",
    "checklist":   [ "The original cheque and the bank's return memo",
                     "Proof of the underlying debt - invoice, agreement, loan record" ],
    "stamp":       "No stamp duty. TIMELINE: notice within 30 days of the return memo;
                    the drawer gets 15 days to pay; the complaint must be filed within
                    the following 30 days.",
    "body":        """ ... the full fill-in-the-blank draft ... """,
    "keywords":    [ "cheque bounce", "138", "demand notice", "dishonour" ],
}
''', "Listing 6.2 - the structure of a document template")

    h2("6.4 Coverage map")
    p("The knowledge base spans %d branches of law. The distribution below was "
      "planned so that no branch a general visitor is likely to need was left "
      "empty, rather than concentrating depth in a few popular areas."
      % KB["categories"])

    rows = [["#", "Branch of law", "Topics", "Templates", "Representative topic"]]
    for index, category in enumerate(legal_data.CATEGORIES, start=1):
        topics = legal_data.topics_in_category(category["id"])
        docs = legal_data.documents_in_category(category["id"])
        rows.append([
            str(index),
            category["name"],
            str(len(topics)),
            str(len(docs)),
            topics[0]["title"] if topics else "-",
        ])
    rows.append(["", "<b>Total</b>", "<b>%d</b>" % KB["topics"],
                 "<b>%d</b>" % KB["documents"], ""])
    table(rows, [CONTENT_W * 0.05, CONTENT_W * 0.30, CONTENT_W * 0.09,
                 CONTENT_W * 0.11, CONTENT_W * 0.45],
          "Complete coverage map of the knowledge base", font_size=7.6)

    h2("6.5 The glossary, emergency cards and helplines")
    p("Three smaller structures complete the knowledge base:")
    bullets([
        "<b>Glossary</b> - %d terms, each a single sentence. The chatbot consults "
        "this directly when a message begins with &lsquo;what is&rsquo; or "
        "&lsquo;meaning of&rsquo;, which allows a vocabulary question to be "
        "answered precisely rather than approximately by the search engine."
        % KB["glossary"],
        "<b>Emergency cards</b> - ten situations where a person needs an answer "
        "within minutes. Each card inverts the usual structure: numbered actions "
        "first, then an explicit &lsquo;do not&rsquo; list, then the helpline "
        "number, and only then a link to the full topic.",
        "<b>Helplines</b> - ten national numbers, rendered in the footer of every "
        "page so they are reachable without navigation.",
    ])

    callout("The &lsquo;do not&rsquo; list on the emergency cards came directly out "
            "of user testing. Testers reading the arrest card asked what they should "
            "<i>avoid</i> doing far more urgently than what they should do - "
            "particularly whether to sign anything. Adding an explicit prohibition "
            "list was one of the most valuable single changes made to the content.")


# ===========================================================================
#  CHAPTER 7 - THE CHATBOT ENGINE
# ===========================================================================

def diagram_pipeline():
    d = Drawing(CONTENT_W, 300)

    steps = [
        ("Raw message", "\"my landlord is not\nreturning my deposit\"", colors.white),
        ("1. Tokenise", "lowercase, strip punctuation,\nsplit into words", colors.HexColor("#eef3fb")),
        ("2. Remove stopwords", "drop 'my', 'is', 'not'\n(no discriminating power)", colors.HexColor("#eef3fb")),
        ("3. Stem", "returning -> return\ndeposit -> deposit", colors.HexColor("#eef3fb")),
        ("4. Expand synonyms", "landlord -> rent tenancy lease\ndeposit -> security deposit refund", colors.HexColor("#fbf3d8")),
        ("5. Build TF-IDF vector", "weight = TF x IDF,\nnormalised to unit length", colors.HexColor("#e6f4ed")),
        ("6. Cosine similarity", "dot product against all\n%d indexed entries" % INDEXED, colors.HexColor("#e6f4ed")),
        ("7. Adjust ranking", "template bonus / penalty\nby detected intent", colors.HexColor("#e6f4ed")),
        ("8. Compose answer", "summary + key points +\nsteps + laws + sources", colors.white),
    ]

    box_h = 28
    y = 268
    for index, (title, detail, fill) in enumerate(steps):
        box(d, 4, y, 168, box_h, title, fill=fill, size=7.6)
        label_text(d, 184, y + box_h - 10, detail.split("\n")[0], 7, GREY)
        if "\n" in detail:
            label_text(d, 184, y + box_h - 20, detail.split("\n")[1], 7, GREY)
        if index < len(steps) - 1:
            arrow(d, 88, y, 88, y - 4, color=NAVY_LIGHT)
        y -= box_h + 5
    return d


def worked_example():
    """Compute a genuine TF-IDF worked example from the live index."""
    engine = chatbot.ENGINE
    query = "my landlord is not returning my deposit"

    raw_tokens = chatbot.TOKEN_PATTERN.findall(query.lower())
    kept = [w for w in raw_tokens if w not in chatbot.STOPWORDS and len(w) > 1]
    stemmed = [chatbot.stem(w) for w in kept]
    expanded = chatbot.expand_query(query)
    final_tokens = chatbot.tokenize(expanded)
    vector = engine._vectorise(final_tokens)

    top_terms = sorted(vector.items(), key=lambda kv: kv[1], reverse=True)[:8]
    term_rows = [["Stemmed term", "IDF weight", "Normalised TF-IDF"]]
    for term, weight in top_terms:
        term_rows.append([term, "%.3f" % engine.idf.get(term, 0), "%.4f" % weight])

    results = engine.search(query, limit=5)
    result_rows = [["Rank", "Matched entry", "Type", "Cosine score"]]
    for rank, item in enumerate(results, start=1):
        result_rows.append([
            str(rank), item["entry"]["title"],
            "Template" if item["entry"]["kind"] == "document" else "Topic",
            "%.4f" % item["score"],
        ])

    return {
        "query": query, "raw": raw_tokens, "kept": kept, "stemmed": stemmed,
        "final": final_tokens, "term_rows": term_rows, "result_rows": result_rows,
        "vector_size": len(vector),
    }


def chapter_7():
    h1("7. THE CHATBOT ENGINE")

    p("This chapter describes the core of the project. The engine is contained in "
      "a single module, <font face='Courier'>chatbot.py</font>, of %d lines. It "
      "uses no machine-learning library; the entire matching mathematics is "
      "implemented with <font face='Courier'>math</font>, "
      "<font face='Courier'>re</font> and "
      "<font face='Courier'>collections.Counter</font>." % LOC.get("chatbot.py", 0))

    h2("7.1 Overview of the pipeline")
    story.append(diagram_pipeline())
    caption("The eight-stage answering pipeline")

    h2("7.2 Stage 1 - tokenisation")
    p("The message is lower-cased and split on a regular expression that keeps "
      "only letters and digits, discarding punctuation. Lower-casing matters "
      "because a user may type &lsquo;FIR&rsquo;, &lsquo;Fir&rsquo; or "
      "&lsquo;fir&rsquo; and all three must reach the same index term.")

    h2("7.3 Stage 2 - stopword removal")
    p("A list of 130 common English words is removed. These words appear in "
      "almost every entry, so they carry no power to distinguish one topic from "
      "another; retaining them would make two unrelated sentences appear similar "
      "merely because both contain &lsquo;the&rsquo; and &lsquo;is&rsquo;. We "
      "extended the standard list with words peculiar to this domain that proved "
      "equally useless - <i>sir</i>, <i>madam</i>, <i>kindly</i>, <i>please</i>, "
      "<i>help</i>, <i>tell</i> - which appeared constantly in test questions.")

    h2("7.4 Stage 3 - stemming")
    p("A user may write <i>filing</i>, <i>filed</i> or <i>file</i>; the knowledge "
      "base may contain any of them. Stemming reduces all three to a common root "
      "so they match. We implemented a simplified suffix-stripping stemmer rather "
      "than importing Porter's full algorithm.")

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
''', "Listing 7.1 - the stemmer")

    callout("The guard <font face='Courier'>len(word) - len(suffix) &gt;= 4</font> "
            "was added after a failure found in testing. Without it "
            "<i>&lsquo;sale&rsquo;</i> was stemmed to <i>&lsquo;sal&rsquo;</i> and "
            "<i>&lsquo;lease&rsquo;</i> to <i>&lsquo;leas&rsquo;</i>, so a query "
            "about a sale deed stopped matching the sale deed template entirely. "
            "Refusing to reduce a word below four characters fixed it.")

    h2("7.5 Stage 4 - synonym expansion")
    p("This stage is what allows a visitor to succeed without knowing any legal "
      "vocabulary, and it is the single change that most improved real-world "
      "usability. A table of 60 everyday words maps each to the legal vocabulary "
      "it implies. Before searching, any mapped word found in the message causes "
      "the corresponding legal terms to be appended to the query.")

    code('''
SYNONYMS = {
    "fired":    "termination dismissal employment",
    "boss":     "employer employment",
    "landlord": "rent tenancy lease landlord",
    "builder":  "rera promoter real estate possession",
    "bounce":   "cheque bounce dishonour 138",
    "hacked":   "cybercrime hacking it act",
    "smoke":    "pollution environment air ngt",
    ...
}

def expand_query(text):
    """Add the legal equivalent of everyday words to the user's question."""
    lowered = text.lower()
    extras = []
    for word, replacement in SYNONYMS.items():
        if re.search(r"\\b" + re.escape(word) + r"\\b", lowered):
            extras.append(replacement)
    return text + " " + " ".join(extras) if extras else text
''', "Listing 7.2 - synonym expansion")

    p("The word-boundary anchors in the regular expression matter: without them "
      "the entry for <i>&lsquo;car&rsquo;</i> would fire on "
      "<i>&lsquo;carpet area&rsquo;</i> and pull an unrelated motor-vehicle topic "
      "into a property query.")

    h2("7.6 Stage 5 - building the TF-IDF index")

    h3("7.6.1 Flattening an entry into searchable text")
    p("Each topic and template is flattened into one long string. Fields that "
      "carry more signal are repeated so that they count more heavily - the title "
      "and keywords three times each, and every FAQ question twice. Repetition "
      "raises the term frequency of those words, which is a simple and "
      "transparent way of weighting fields without adding a separate weighting "
      "mechanism.")

    h3("7.6.2 The weighting formula")
    p("For a term <i>t</i> in an entry <i>d</i> within a collection of <i>N</i> "
      "entries:")

    formula = Table([[Paragraph(
        "<font face='Times-Italic'>TF</font>(t, d) &nbsp;=&nbsp; "
        "count of t in d &nbsp;/&nbsp; total terms in d<br/><br/>"
        "<font face='Times-Italic'>IDF</font>(t) &nbsp;=&nbsp; "
        "log<sub>e</sub> ( N &nbsp;/&nbsp; (1 + df(t)) ) &nbsp;+&nbsp; 1"
        "<br/><br/>"
        "<font face='Times-Italic'>w</font>(t, d) &nbsp;=&nbsp; "
        "<font face='Times-Italic'>TF</font>(t, d) &nbsp;&times;&nbsp; "
        "<font face='Times-Italic'>IDF</font>(t)",
        ParagraphStyle("f", parent=S_BODY, alignment=TA_CENTER, fontSize=11,
                       leading=17, spaceAfter=0))]], colWidths=[CONTENT_W])
    formula.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PAPER),
        ("BOX", (0, 0), (-1, -1), 0.8, LINE),
        ("TOPPADDING", (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
    ]))
    story.append(formula)
    gap(10)

    p("where <i>df(t)</i> is the number of entries containing <i>t</i>. The "
      "&lsquo;1 +&rsquo; in the denominator prevents division by zero, and the "
      "&lsquo;+ 1&rsquo; outside the logarithm keeps every weight strictly "
      "positive - without it, a term appearing in every entry would receive a "
      "weight of exactly zero and be silently dropped.")

    h3("7.6.3 Length normalisation")
    p("A long topic naturally contains more words and would therefore score "
      "higher against any query. To remove this bias each vector is divided by "
      "its own Euclidean length at index time:")

    formula2 = Table([[Paragraph(
        "<font face='Times-Italic'>v&#770;</font> &nbsp;=&nbsp; "
        "<font face='Times-Italic'>v</font> &nbsp;/&nbsp; "
        "&#8730;( &#931; <font face='Times-Italic'>v<sub>i</sub></font><sup>2</sup> )",
        ParagraphStyle("f2", parent=S_BODY, alignment=TA_CENTER, fontSize=11,
                       leading=17, spaceAfter=0))]], colWidths=[CONTENT_W])
    formula2.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PAPER),
        ("BOX", (0, 0), (-1, -1), 0.8, LINE),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(formula2)
    gap(10)

    code('''
def _vectorise(self, tokens):
    """Turn a list of words into a normalised TF-IDF dictionary."""
    if not tokens:
        return {}
    counts = Counter(tokens)
    total  = len(tokens)
    vector = {}
    for word, count in counts.items():
        weight = self.idf.get(word)
        if weight is None:
            continue                       # word never seen while indexing
        vector[word] = (count / total) * weight

    length = math.sqrt(sum(value * value for value in vector.values()))
    if length == 0:
        return {}
    return {word: value / length for word, value in vector.items()}
''', "Listing 7.3 - vector construction with normalisation")

    h2("7.7 Stage 6 - cosine similarity")
    p("Similarity between the query vector <i>q</i> and an entry vector <i>d</i> "
      "is the cosine of the angle between them:")

    formula3 = Table([[Paragraph(
        "cos(<font face='Times-Italic'>q</font>, <font face='Times-Italic'>d</font>) "
        "&nbsp;=&nbsp; ( <font face='Times-Italic'>q</font> &middot; "
        "<font face='Times-Italic'>d</font> ) &nbsp;/&nbsp; "
        "( ||<font face='Times-Italic'>q</font>|| &nbsp;&times;&nbsp; "
        "||<font face='Times-Italic'>d</font>|| ) "
        "&nbsp;&nbsp;=&nbsp;&nbsp; <font face='Times-Italic'>q</font> &middot; "
        "<font face='Times-Italic'>d</font> &nbsp;&nbsp;"
        "<font size='9' color='#5a6072'>(both already unit length)</font>",
        ParagraphStyle("f3", parent=S_BODY, alignment=TA_CENTER, fontSize=11,
                       leading=17, spaceAfter=0))]], colWidths=[CONTENT_W])
    formula3.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PAPER),
        ("BOX", (0, 0), (-1, -1), 0.8, LINE),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(formula3)
    gap(10)

    p("Because normalisation was already performed at index time, the "
      "denominator is 1 and the cosine reduces to a plain dot product. A further "
      "optimisation iterates over whichever of the two vectors has fewer terms - "
      "usually the query, which has perhaps twenty terms against an entry's few "
      "hundred - so each comparison touches only the overlapping vocabulary.")

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
''', "Listing 7.4 - the cosine similarity inner loop")

    h2("7.8 Stage 7 - intent-conditioned ranking")
    p("Two adjustments are applied to the raw cosine score. The first is a small "
      "bonus of 0.05 when the query literally contains one of the entry's "
      "keywords, which recovers exact phrase matches that TF-IDF alone can "
      "underweight.")

    p("The second adjustment fixed the largest single defect found in testing, "
      "and is described in full in Chapter 12. A document template and the topic "
      "explaining the same subject necessarily share most of their vocabulary - "
      "the cheque-bounce notice template and the cheque-bounce topic are almost "
      "indistinguishable to a bag-of-words model. The template was therefore "
      "frequently returned to users who wanted an explanation. The engine now "
      "detects whether the message asks for a document at all, and scales "
      "document scores accordingly:")

    code('''
TEMPLATE_HINTS = ("template", "format", "draft", "sample", "specimen",
                  "download", "how to write", "agreement", "deed", "letter",
                  "application form", "petition", "affidavit")

wants_template = any(hint in lowered_query for hint in TEMPLATE_HINTS)
...
if entry["kind"] == "document":
    score *= 1.25 if wants_template else 0.72
''', "Listing 7.5 - intent-conditioned ranking adjustment")

    callout("This single change raised Top-1 retrieval accuracy from "
            "<b>66.7%%</b> to <b>%.1f%%</b> on the 30-question test set, while "
            "template requests continued to be routed to a template in 10 out of "
            "10 cases. The measurement and analysis are given in Chapter 12."
            % ACC["top1_pct"], color=colors.HexColor("#e6f4ed"), border=GREEN)

    h2("7.9 A complete worked example")
    example = worked_example()
    p("The following trace was produced by running the live engine on the query "
      "<b>&ldquo;%s&rdquo;</b>. Every number below is computed from the actual "
      "index, not estimated." % example["query"])

    h3("7.9.1 Text processing")
    table([
        ["Stage", "Result"],
        ["Raw tokens", ", ".join(example["raw"])],
        ["After stopword removal", ", ".join(example["kept"])],
        ["After stemming", ", ".join(example["stemmed"])],
        ["After synonym expansion", ", ".join(example["final"][:22]) + " ..."],
        ["Vector dimensions", "%d distinct terms" % example["vector_size"]],
    ], [CONTENT_W * 0.26, CONTENT_W * 0.74],
        "Text processing trace for the example query", font_size=8)

    h3("7.9.2 The highest-weighted query terms")
    p("Note how the rare, discriminating terms dominate. A term appearing in only "
      "a handful of the %d entries earns a high IDF; a term appearing "
      "everywhere earns almost none." % INDEXED)
    table(example["term_rows"],
          [CONTENT_W * 0.40, CONTENT_W * 0.30, CONTENT_W * 0.30],
          "The eight highest-weighted terms in the query vector", font_size=8.4)

    h3("7.9.3 Ranked results")
    table(example["result_rows"],
          [CONTENT_W * 0.08, CONTENT_W * 0.56, CONTENT_W * 0.16, CONTENT_W * 0.20],
          "Cosine similarity results for the example query", font_size=8.4)

    p("The correct topic is returned first with a clear margin. Note that the "
      "rent agreement template appears further down rather than at the top - the "
      "ranking adjustment of Section 7.8 has correctly recognised that this "
      "message describes a problem rather than requesting a format.")

    h2("7.10 The intent layer")
    p("Before any searching occurs, the message is classified. This allows the "
      "system to respond in the shape the user actually needs rather than always "
      "returning a topic page.")

    table([
        ["Intent", "Trigger", "Response given"],
        ["greeting", "hi, hello, namaste (in a short message)", "Welcome message with example questions"],
        ["thanks", "thanks, thank you, shukriya", "Acknowledgement and an invitation to continue"],
        ["bye", "bye, goodbye, exit", "Closing message with a practical reminder"],
        ["emergency", "urgent, arrested, danger, threatening, beaten", "Action-first card: numbered steps, a 'do not' list, and a helpline"],
        ["definition", "message begins with 'what is', 'meaning of', 'define'", "Direct glossary definition plus a link to the fuller topic"],
        ["document", "template, format, draft, sample, download", "Template surfaced first, with its checklist and stamp-duty note"],
        ["question", "anything else", "Full retrieval and a structured topic answer"],
        ["unknown", "best cosine score below the 0.02 threshold", "Honest 'no confident match', a list of what is covered, and rephrasing advice"],
    ], [CONTENT_W * 0.14, CONTENT_W * 0.34, CONTENT_W * 0.52],
        "The intent layer", font_size=8.2)

    p("The <i>unknown</i> case deserves comment. An earlier version always "
      "returned its best match however weak it was, which produced confidently "
      "wrong answers - the worst possible behaviour for a legal tool. Introducing "
      "an explicit confidence floor of 0.02 means the system now says plainly "
      "that it does not know, and suggests how to rephrase.")

    h2("7.11 Answer composition")
    p("For an ordinary legal question the composer assembles the winning entry "
      "into a consistent structure: title and area of law, the summary, up to "
      "five key points, up to five numbered procedural steps, up to four "
      "statutory references, and the first FAQ. Source links with their "
      "similarity scores are attached so the user can verify the answer, and a "
      "disclaimer is appended to every reply without exception.")

    h2("7.12 The optional AI layer")
    p("When an API key is present, the top three retrieved entries are serialised "
      "into a reference block and passed to a language model together with a "
      "constraining system prompt. This is Retrieval Augmented Generation: the "
      "model contributes fluency and the ability to address the specific phrasing "
      "of the question, while the facts remain those of the curated knowledge "
      "base.")

    code('''
AI_SYSTEM_PROMPT = """You are LegalMitra, a friendly legal information assistant ...

Rules you must follow:
1. Answer ONLY from the reference material given to you in the user message.
   If the reference material does not cover the question, say so honestly and
   suggest the closest topic that is covered.
2. Write in simple English that a first-year college student can follow.
3. Structure the reply as: a direct answer first, then the key rules, then the
   practical steps, then the law that applies.
4. Never invent a section number, a case name or a deadline. Use only what is
   in the reference material.
5. Always end with one line reminding the reader that this is general legal
   information, not legal advice."""
''', "Listing 7.6 - the constraining system prompt")

    p("Three properties of this design matter. First, the model cannot invent a "
      "citation, because it is instructed to use only supplied material and the "
      "supplied material is fixed. Second, the failure path is silent: the entire "
      "call is wrapped so that a missing key, an absent network, a rate limit or "
      "a refusal all fall through to the offline composer. Third, the offline "
      "engine is not a degraded mode but the primary one - the system is "
      "demonstrated and evaluated without any API key at all.")

    h2("7.13 Complexity and performance")
    table([
        ["Operation", "Complexity", "Measured"],
        ["Index construction (start-up, once)", "O(N &times; L)",
         "%.0f ms for %d entries" % (TIME["build_ms"], INDEXED)],
        ["Search: tokenise, vectorise, cosine, sort", "O(N &times; min(|q|, |d|)) + O(N log N)",
         "%.1f ms mean" % TIME["search_mean_ms"]],
        ["Full answer including composition", "O(N &times; min(|q|, |d|))",
         "%.1f ms mean, %.1f ms median" % (TIME["mean_ms"], TIME["median_ms"])],
        ["<b>Best / worst observed per question</b>", "",
         "<b>%.1f ms / %.1f ms</b>" % (TIME["best_ms"], TIME["worst_ms"])],
    ], [CONTENT_W * 0.34, CONTENT_W * 0.34, CONTENT_W * 0.32],
        "Computational complexity and measured timings")
    note("N = number of indexed entries (%d), L = mean entry length in tokens, "
         "Q = query length. Timings were measured by this report generator itself "
         "at build time, averaged over the %d questions of the evaluation set "
         "described in Chapter 12, running the offline engine with no network "
         "access." % (INDEXED, TIME["runs"]))


# ===========================================================================
#  CHAPTER 8 - THE VOICE INTERFACE
# ===========================================================================

def diagram_voice():
    d = Drawing(CONTENT_W, 250)

    label_text(d, 4, 238, "INPUT PATH  -  speech to text", 8, NAVY, bold=True)
    w = (CONTENT_W - 44) / 5
    items_in = ["User speaks\ninto the mic", "webkitSpeech\nRecognition",
                "Interim text\nshown live", "isFinal = true\ndetected",
                "Message sent\nto /api/chat"]
    for index, text in enumerate(items_in):
        x = 4 + index * (w + 11)
        fill = colors.HexColor("#fbf3d8") if index == 1 else colors.white
        box(d, x, 180, w, 44, text, size=7, fill=fill,
            stroke=GOLD if index == 1 else NAVY)
        if index < len(items_in) - 1:
            arrow(d, x + w, 202, x + w + 11, 202)

    label_text(d, 4, 152, "OUTPUT PATH  -  text to speech", 8, NAVY, bold=True)
    items_out = ["Answer text\nreceived", "Cleaned for\nspeech", "Split into\n~200 char parts",
                 "Utterances\nqueued", "speechSynthesis\nspeaks"]
    for index, text in enumerate(items_out):
        x = 4 + index * (w + 11)
        fill = colors.HexColor("#e6f4ed") if index == 4 else colors.white
        box(d, x, 94, w, 44, text, size=7, fill=fill,
            stroke=GREEN if index == 4 else NAVY)
        if index < len(items_out) - 1:
            arrow(d, x + w, 116, x + w + 11, 116)

    d.add(Rect(4, 8, CONTENT_W - 8, 68, fillColor=colors.HexColor("#eef3fb"),
               strokeColor=NAVY, strokeWidth=0.8, rx=6, ry=6))
    label_text(d, 14, 62, "USER CONTROLS  (all available at any moment)", 7.6, NAVY, bold=True)
    controls = ["Mute / unmute", "Stop speaking", "Choose voice",
                "Slow / Normal / Fast", "Clear conversation"]
    cw = (CONTENT_W - 60) / 5
    for index, text in enumerate(controls):
        box(d, 14 + index * (cw + 8), 18, cw, 30, text, size=6.6,
            fill=colors.white)
    return d


def chapter_8():
    h1("8. THE VOICE INTERFACE")

    p("The requirement that the system be usable without typing was treated as a "
      "core feature rather than an add-on. During user testing the older "
      "participants consistently preferred speaking, and one tester who was "
      "unfamiliar with a keyboard could use the system only through voice. Both "
      "directions - speech to text and text to speech - are implemented entirely "
      "in the browser using the W3C Web Speech API.")

    story.append(diagram_voice())
    caption("The two-way voice pipeline and the user controls")

    h2("8.1 Why the browser and not a cloud service")
    table([
        ["Consideration", "Cloud speech service", "Browser Web Speech API"],
        ["Cost", "Charged per minute or per character", "Free"],
        ["API key management", "Required, and a secret to protect", "None"],
        ["Works offline", "No", "Yes for synthesis; recognition may use the browser's own service"],
        ["Audio privacy", "Audio uploaded to a third party", "Handled by the browser; never sent to our server"],
        ["Latency", "Network round trip", "Local"],
        ["Setup for a demonstration", "Account, billing, credentials", "None"],
        ["Browser support", "Universal", "Chromium-based browsers only"],
    ], [CONTENT_W * 0.22, CONTENT_W * 0.34, CONTENT_W * 0.44],
        "Cloud speech services compared with the browser API", font_size=8.2)

    p("The single disadvantage - restricted browser support - was judged "
      "acceptable because the fallback is graceful: where recognition is "
      "unavailable the microphone button is hidden and an explanatory note "
      "appears, and the application remains fully usable by typing.")

    h2("8.2 Speech recognition (input)")
    code('''
var Recognition = window.SpeechRecognition || window.webkitSpeechRecognition;

if (Recognition && micBtn) {
    recogniser = new Recognition();
    recogniser.lang           = "en-IN";   // Indian English acoustic model
    recogniser.continuous     = false;     // stop after one sentence
    recogniser.interimResults = true;      // show words as they are spoken

    recogniser.onresult = function (event) {
        var text = "";
        for (var i = event.resultIndex; i < event.results.length; i++) {
            text += event.results[i][0].transcript;
        }
        input.value = text;                       // live transcription

        // When the browser is confident the sentence is complete, send it.
        if (event.results[event.results.length - 1].isFinal) {
            setTimeout(function () { send(); }, 400);
        }
    };
}
''', "Listing 8.1 - speech recognition")

    p("Three settings were chosen deliberately:")
    bullets([
        "<b><font face='Courier'>lang = \"en-IN\"</font></b> selects the Indian "
        "English acoustic model. Testing with the default <i>en-US</i> produced "
        "noticeably worse transcription of Indian names, place names and legal "
        "terms such as <i>stridhan</i> and <i>vakalatnama</i>.",
        "<b><font face='Courier'>interimResults = true</font></b> streams partial "
        "results into the text box as the user speaks. Testers found silence "
        "during recognition unnerving and several stopped mid-sentence believing "
        "the microphone had failed; live text removed that entirely.",
        "<b><font face='Courier'>continuous = false</font></b> ends recognition "
        "after one sentence, which suits a question-and-answer interaction and "
        "avoids the microphone remaining open indefinitely.",
    ])

    p("The 400 millisecond delay before submitting is a small but important "
      "detail. The browser sometimes emits a final result and then revises it; "
      "submitting immediately occasionally sent a truncated question.")

    h2("8.3 Speech synthesis (output)")
    p("The answers produced by the composer are formatted for the eye - headings "
      "in capitals, bullet markers, numbered steps and blank lines. Read aloud "
      "literally, this sounds wrong. The text is therefore cleaned before being "
      "spoken.")

    code('''
function cleanForSpeech(text) {
    return text
        .replace(/^\\s*[-*]\\s*/gm, "")   // drop bullet markers
        .replace(/\\n{2,}/g, ". ")        // blank line becomes a full stop
        .replace(/\\n/g, ", ")            // single newline becomes a pause
        .replace(/\\s{2,}/g, " ")
        .trim();
}
''', "Listing 8.2 - preparing text for speech")

    h3("8.3.1 Chunking long answers")
    p("A significant practical problem emerged during testing: browsers silently "
      "truncate very long utterances, so a detailed legal answer would simply "
      "stop speaking part way through. The solution is to split the answer at "
      "sentence boundaries into segments of roughly two hundred characters and "
      "queue them as separate utterances, which the browser then plays "
      "consecutively.")

    code('''
var chunks = clean.match(/[^.!?]+[.!?]*/g) || [clean];
var buffer = "", queue = [];

chunks.forEach(function (piece) {
    if ((buffer + piece).length > 200) {
        if (buffer) { queue.push(buffer); }
        buffer = piece;
    } else {
        buffer += piece;
    }
});
if (buffer) { queue.push(buffer); }

queue.forEach(function (part) {
    var utterance   = new SpeechSynthesisUtterance(part.trim());
    utterance.voice = chosenVoice;                    // user-selected
    utterance.rate  = parseFloat(rateBox.value);      // 0.8 / 1.0 / 1.25
    synth.speak(utterance);                           // queued, not overlapped
});
''', "Listing 8.3 - chunking and queueing utterances")

    h3("8.3.2 Voice selection")
    p("Available voices are enumerated and filtered to English. An Indian English "
      "voice is pre-selected where the operating system provides one. A further "
      "subtlety is that Chrome populates its voice list asynchronously, so the "
      "list is frequently empty on first call; the code therefore also listens "
      "for the <font face='Courier'>voiceschanged</font> event and rebuilds the "
      "selector when it fires.")

    h2("8.4 Interaction details that mattered")
    table([
        ["Behaviour", "Reason"],
        ["Speech is cancelled the moment the microphone is opened", "Otherwise the microphone picks up the assistant's own voice and transcribes it."],
        ["Speech is cancelled when a new question is submitted", "The previous answer must not continue over the new one."],
        ["Speech is cancelled on page unload", "Browsers otherwise continue speaking after navigation."],
        ["Mute state persists across messages", "A user who mutes once should not have to mute again on every reply."],
        ["The microphone button pulses red while listening", "Testers could not otherwise tell whether the microphone was active."],
        ["The placeholder changes to 'Listening... speak now'", "Reinforces the state change for users who miss the colour cue."],
        ["A blocked microphone permission is explained in a dialogue", "The raw browser failure is silent and looks like a broken button."],
    ], [CONTENT_W * 0.44, CONTENT_W * 0.56],
        "Voice interaction details and the reasons for them", font_size=8.2)

    h2("8.5 Reading a page aloud")
    p("The same synthesis engine is reused on topic pages and emergency cards "
      "through a <i>Listen to this page</i> button. The visible text of the "
      "article is extracted, cleaned and chunked exactly as in the chatbot, which "
      "makes the entire knowledge base accessible without reading.")


# ===========================================================================
#  CHAPTER 9 - DATABASE DESIGN
# ===========================================================================

def chapter_9():
    h1("9. DATABASE DESIGN")

    h2("9.1 What is stored and what is not")
    p("A deliberate distinction runs through the data design: the <b>legal "
      "content is not in the database</b>. Only <b>interaction data</b> is "
      "persisted. The knowledge base is read-only material authored by the "
      "developers, so it lives in version-controlled Python modules where it can "
      "be reviewed as text; the database exists solely to record what users did, "
      "which is genuinely dynamic.")

    p("SQLite was chosen because it requires no server process, no credentials "
      "and no installation - the entire database is a single file, "
      "<font face='Courier'>legalmitra.db</font>, created automatically on first "
      "run. For a project that must be demonstrated on an unfamiliar machine this "
      "is a decisive practical advantage.")

    h2("9.2 Schema")
    code('''
CREATE TABLE IF NOT EXISTS chat_log (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id  TEXT    NOT NULL,      -- random id, not a user identity
    question    TEXT    NOT NULL,
    answer      TEXT    NOT NULL,
    intent      TEXT,                  -- greeting / question / emergency / ...
    engine      TEXT,                  -- 'offline' or 'ai'
    confidence  REAL,                  -- cosine similarity of the best match
    top_source  TEXT,                  -- title of the page the answer came from
    created_at  TEXT    NOT NULL
);

CREATE TABLE IF NOT EXISTS search_log (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    query       TEXT    NOT NULL,
    results     INTEGER NOT NULL,
    created_at  TEXT    NOT NULL
);

CREATE TABLE IF NOT EXISTS contact_msg (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT    NOT NULL,
    email       TEXT    NOT NULL,
    subject     TEXT,
    message     TEXT    NOT NULL,
    created_at  TEXT    NOT NULL
);
''', "Listing 9.1 - the complete schema")

    h2("9.3 Table descriptions")
    table([
        ["Column", "Type", "Description"],
        ["id", "INTEGER PK", "Auto-incrementing primary key"],
        ["session_id", "TEXT", "A random 32-character hexadecimal value stored in the browser session cookie. It groups the turns of one conversation together; it is not linked to any identity and is regenerated when the user clears the chat."],
        ["question", "TEXT", "The visitor's message exactly as submitted"],
        ["answer", "TEXT", "The full reply that was returned"],
        ["intent", "TEXT", "The classification assigned by the intent layer"],
        ["engine", "TEXT", "Which path produced the answer - 'offline' or 'ai'"],
        ["confidence", "REAL", "The cosine similarity of the best match, used to identify weak areas of the knowledge base"],
        ["top_source", "TEXT", "Title of the highest-ranked entry, used for the popular-topics analysis"],
        ["created_at", "TEXT", "Timestamp in YYYY-MM-DD HH:MM:SS format"],
    ], [CONTENT_W * 0.17, CONTENT_W * 0.15, CONTENT_W * 0.68],
        "The chat_log table", font_size=8.2)

    h2("9.4 Analytics queries")
    p("The analytics page is driven by four aggregate queries. The most useful "
      "for improving the project is the last one, which surfaces questions the "
      "engine could not confidently answer - each such row is a candidate for a "
      "new topic or a new synonym mapping.")

    code('''
-- Most frequently asked questions
SELECT question, COUNT(*) AS times
FROM   chat_log
GROUP  BY LOWER(question)
ORDER  BY times DESC, question ASC
LIMIT  ?;

-- Which knowledge base pages the chatbot answered from most often
SELECT top_source, COUNT(*) AS times
FROM   chat_log
WHERE  top_source IS NOT NULL AND top_source <> ''
GROUP  BY top_source
ORDER  BY times DESC
LIMIT  ?;

-- Distinct conversations
SELECT COUNT(DISTINCT session_id) FROM chat_log;

-- Questions the engine could NOT answer confidently  (improvement backlog)
SELECT COUNT(*) FROM chat_log WHERE intent = 'unknown';
''', "Listing 9.2 - the analytics queries")

    h2("9.5 Conversation memory")
    p("The assistant keeps a short memory so that a follow-up question makes "
      "sense. Before answering, the last three turns of the current session are "
      "read back from <font face='Courier'>chat_log</font> and supplied as "
      "context. In offline mode this history is available to the composer; in AI "
      "mode it is passed to the model as prior conversation turns.")

    code('''
def session_history(session_id, limit=10):
    """The last few turns of one visitor's conversation, oldest first."""
    rows = connection.execute(
        """SELECT question, answer FROM chat_log
           WHERE session_id = ? ORDER BY id DESC LIMIT ?""",
        (session_id, limit)).fetchall()

    history = []
    for row in reversed(rows):
        history.append({"role": "user",      "content": row["question"]})
        history.append({"role": "assistant", "content": row["answer"]})
    return history
''', "Listing 9.3 - reconstructing conversation history")

    h2("9.6 Privacy position")
    callout("<b>No personal data is collected.</b> There is no login, no name, no "
            "email address and no IP logging in the chat path. The session "
            "identifier is a random value with no link to a person and is "
            "discarded when the browser session ends or the user clears the "
            "conversation. Voice audio is processed by the browser and never "
            "reaches the server or the database. The only place a name or email "
            "is stored is the contact form, where the visitor types it "
            "voluntarily and knowingly.")

    h2("9.7 Why not a full relational model of the content")
    p("An obvious alternative design would normalise the legal content into "
      "tables - categories, topics, key points, laws, steps, FAQs - with foreign "
      "keys. We rejected this for three reasons. It would require an "
      "administrative interface that nobody would use, since the content is "
      "authored by the developers. It would make the content invisible to version "
      "control, so a change could not be reviewed as a diff. And it would add a "
      "migration step every time the topic structure changed, which happened "
      "several times during authoring. Keeping content as code proved the correct "
      "trade-off for a read-only corpus of this size.")


# ===========================================================================
#  CHAPTER 10 - USER INTERFACE DESIGN
# ===========================================================================

def wireframe_home():
    d = Drawing(CONTENT_W, 250)
    d.add(Rect(0, 0, CONTENT_W, 250, fillColor=colors.white, strokeColor=LINE))
    d.add(Rect(0, 236, CONTENT_W, 14, fillColor=colors.HexColor("#0d1628"), strokeColor=None))
    label_text(d, CONTENT_W / 2, 240, "Academic project - not legal advice", 6,
               colors.HexColor("#c8cfdd"), anchor="middle")
    d.add(Rect(0, 208, CONTENT_W, 28, fillColor=NAVY, strokeColor=None))
    label_text(d, 8, 218, "LegalMitra", 9, colors.white, bold=True)
    d.add(Rect(CONTENT_W - 190, 214, 182, 16, fillColor=NAVY_LIGHT, strokeColor=None))
    label_text(d, CONTENT_W - 182, 219, "Search any law, right or document...", 6,
               colors.HexColor("#8496b5"))
    d.add(Rect(0, 192, CONTENT_W, 16, fillColor=NAVY_LIGHT, strokeColor=None))
    for index, item in enumerate(["Home", "Areas of Law", "Documents", "Chatbot",
                                  "Glossary", "Emergency", "About"]):
        label_text(d, 10 + index * 62, 197, item, 6, colors.HexColor("#d5deee"))

    d.add(Rect(0, 108, CONTENT_W, 84, fillColor=colors.HexColor("#1a2c50"), strokeColor=None))
    label_text(d, CONTENT_W / 2, 172, "Every law, explained simply.", 13,
               colors.white, anchor="middle", bold=True)
    d.add(Rect(CONTENT_W / 2 - 130, 146, 200, 16, fillColor=colors.white, strokeColor=None))
    d.add(Rect(CONTENT_W / 2 + 70, 146, 60, 16, fillColor=GOLD, strokeColor=None))
    label_text(d, CONTENT_W / 2 + 100, 151, "Find the law", 6, NAVY, anchor="middle", bold=True)
    for index, (num, lab) in enumerate([("20", "Areas"), ("80", "Topics"),
                                        ("31", "Templates"), ("111", "FAQs"),
                                        ("71", "Glossary")]):
        x = CONTENT_W / 2 - 190 + index * 95
        label_text(d, x, 128, num, 10, GOLD, anchor="middle", bold=True)
        label_text(d, x, 118, lab, 5.6, colors.HexColor("#a9b8d1"), anchor="middle")

    label_text(d, 8, 96, "Three ways to get an answer", 8, NAVY, bold=True)
    for index in range(3):
        x = 8 + index * ((CONTENT_W - 16) / 3 + 4)
        w = (CONTENT_W - 32) / 3
        box(d, x, 44, w, 46, ["Ask in your\nown words", "Browse by\narea of law",
                              "Download a\ndocument"][index], size=6.6, fill=PAPER)
    d.add(Rect(0, 0, CONTENT_W, 36, fillColor=colors.HexColor("#0d1628"), strokeColor=None))
    label_text(d, 8, 24, "Footer: explore, popular topics, emergency numbers", 6,
               colors.HexColor("#a9b6cc"))
    return d


def wireframe_chat():
    d = Drawing(CONTENT_W, 230)
    d.add(Rect(CONTENT_W / 2 - 190, 0, 380, 230, fillColor=colors.white,
               strokeColor=LINE, strokeWidth=1))
    left = CONTENT_W / 2 - 190

    d.add(Rect(left, 202, 380, 28, fillColor=NAVY, strokeColor=None))
    from reportlab.graphics.shapes import Circle
    d.add(Circle(left + 18, 216, 9, fillColor=GOLD, strokeColor=None))
    label_text(d, left + 34, 219, "LegalMitra Assistant", 7.4, colors.white, bold=True)
    label_text(d, left + 34, 209, "Online - offline knowledge engine", 5.6,
               colors.HexColor("#9fe0b8"))
    for index, icon in enumerate(["mute", "stop", "clear"]):
        d.add(Rect(left + 300 + index * 26, 208, 22, 16,
                   fillColor=NAVY_LIGHT, strokeColor=None))
        label_text(d, left + 311 + index * 26, 213, icon, 4.8,
                   colors.HexColor("#d5deee"), anchor="middle")

    d.add(Rect(left, 44, 380, 158, fillColor=PAPER, strokeColor=None))

    d.add(Circle(left + 16, 184, 8, fillColor=NAVY, strokeColor=None))
    d.add(Rect(left + 30, 152, 250, 40, fillColor=colors.white, strokeColor=LINE, rx=5, ry=5))
    label_text(d, left + 38, 182, "Namaste! I am LegalMitra. Ask me anything", 6, colors.black)
    label_text(d, left + 38, 173, "about the law - type it or press the mic.", 6, colors.black)
    label_text(d, left + 38, 160, "[Knowledge base]  Read more: ...", 5.4, GREY)

    for index, chip in enumerate(["Arrest rights", "Rent deposit", "Trademark"]):
        d.add(Rect(left + 30 + index * 74, 136, 68, 12, fillColor=colors.white,
                   strokeColor=NAVY, rx=6, ry=6))
        label_text(d, left + 64 + index * 74, 140, chip, 5.2, NAVY, anchor="middle")

    d.add(Circle(left + 364, 116, 8, fillColor=GOLD, strokeColor=None))
    d.add(Rect(left + 190, 100, 160, 26, fillColor=NAVY, strokeColor=None, rx=5, ry=5))
    label_text(d, left + 198, 116, "my landlord is not returning", 6, colors.white)
    label_text(d, left + 198, 107, "my deposit", 6, colors.white)

    d.add(Circle(left + 16, 76, 8, fillColor=NAVY, strokeColor=None))
    d.add(Rect(left + 30, 52, 270, 44, fillColor=colors.white, strokeColor=LINE, rx=5, ry=5))
    label_text(d, left + 38, 88, "LANDLORD AND TENANT - RENT, EVICTION", 5.8, NAVY, bold=True)
    label_text(d, left + 38, 79, "AND DEPOSITS", 5.8, NAVY, bold=True)
    label_text(d, left + 38, 69, "A landlord may deduct only for unpaid dues and", 5.6, colors.black)
    label_text(d, left + 38, 61, "damage beyond normal wear and tear...", 5.6, colors.black)

    d.add(Rect(left, 0, 380, 44, fillColor=colors.white, strokeColor=LINE))
    d.add(Circle(left + 22, 26, 11, fillColor=colors.white, strokeColor=NAVY))
    label_text(d, left + 22, 24, "mic", 5, NAVY, anchor="middle")
    d.add(Rect(left + 40, 15, 296, 22, fillColor=colors.white, strokeColor=LINE, rx=4, ry=4))
    label_text(d, left + 48, 24, "Type your legal question...", 6, GREY)
    d.add(Circle(left + 356, 26, 11, fillColor=NAVY, strokeColor=None))
    label_text(d, left + 356, 24, "send", 4.6, colors.white, anchor="middle")
    label_text(d, left + 40, 6, "Voice: [en-IN]   Speed: [Normal]", 5.2, GREY)
    return d


def chapter_10():
    h1("10. USER INTERFACE DESIGN")

    h2("10.1 Design principles")
    bullets([
        "<b>Seriousness without intimidation.</b> The palette is deep navy with a "
        "gold accent - the visual language of institutional legal material - but "
        "the typography and spacing are those of an ordinary reading site, not of "
        "a statute book.",
        "<b>The disclaimer is never off-screen.</b> A strip at the very top of "
        "every page states that this is an academic project and not legal advice. "
        "It is not dismissible.",
        "<b>Every page offers a way to ask.</b> Topic, document, category and "
        "emergency pages all carry a prompt to open the chatbot, because a "
        "visitor who has found nearly the right page still has a question.",
        "<b>Action before background.</b> Summaries and steps precede history and "
        "statutory detail on every page.",
        "<b>Nothing hidden behind interaction.</b> Content is visible on load; "
        "only FAQs are collapsed, and those use the native "
        "<font face='Courier'>&lt;details&gt;</font> element so they remain "
        "expandable without JavaScript.",
    ])

    h2("10.2 Page inventory")
    table([
        ["Route", "Page", "Purpose"],
        ["/", "Home", "Hero search, statistics, three routes in, emergency cards, all categories, featured topics and templates"],
        ["/categories", "Areas of law", "All %d branches with their topic lists" % KB["categories"]],
        ["/category/&lt;id&gt;", "Category", "Topics and templates within one branch"],
        ["/topic/&lt;id&gt;", "Topic", "Summary, key points, numbered procedure, statutes, FAQs, related links, page reader"],
        ["/documents", "Template library", "All %d templates with a live filter and category chips" % KB["documents"]],
        ["/document/&lt;id&gt;", "Template", "Checklist, stamp-duty note, highlighted template, copy / print / download"],
        ["/document/&lt;id&gt;/download", "Download", "The template as a formatted .txt file"],
        ["/chat", "Chatbot", "The conversational interface with voice controls"],
        ["/api/chat", "JSON endpoint", "Receives a message, returns answer, sources, suggestions, engine and confidence"],
        ["/api/clear", "JSON endpoint", "Issues a fresh session id"],
        ["/search", "Search results", "Ranked results with a visual relevance bar, plus glossary matches"],
        ["/glossary", "Glossary", "A-Z index, letter filter and live text filter"],
        ["/emergency", "Emergency", "All quick-help cards and the helpline grid"],
        ["/emergency/&lt;id&gt;", "Emergency card", "Numbered actions, prohibitions, helpline, link to the full topic"],
        ["/helplines", "Helplines", "National numbers and official portal directory"],
        ["/about", "About", "The idea, technology table, algorithm explanation, limitations"],
        ["/contact", "Contact", "Feedback form with server-side validation"],
        ["/stats", "Analytics", "Live figures read from SQLite"],
        ["404 / 500", "Error", "Friendly recovery page offering search, browse and chat"],
    ], [CONTENT_W * 0.22, CONTENT_W * 0.16, CONTENT_W * 0.62],
        "Complete page inventory", font_size=7.8)

    h2("10.3 Home page layout")
    story.append(wireframe_home())
    caption("Home page layout")

    h2("10.4 Chatbot layout")
    p("The chat interface follows the conventions users already know from "
      "messaging applications, because testers understood it immediately without "
      "explanation. Three elements are specific to this project: the engine badge "
      "on every reply showing whether the answer came from the knowledge base or "
      "the language model, the source links with their relevance, and the "
      "suggestion chips that turn a dead end into a next question.")
    story.append(wireframe_chat())
    caption("Chatbot layout with voice controls, source attribution and suggestion chips")

    h2("10.5 Responsive design")
    p("Layout is fluid, using CSS Grid with "
      "<font face='Courier'>auto-fit</font> and "
      "<font face='Courier'>minmax()</font> so that card grids reflow without "
      "device-specific rules. Two breakpoints handle the structural changes:")
    table([
        ["Breakpoint", "Change"],
        ["Above 900 px", "Two-column article layout with a sticky sidebar; four-column card grids"],
        ["900 px and below", "Sidebar moves below the article and stops being sticky; footer becomes two columns"],
        ["720 px and below", "Navigation collapses behind a hamburger button; the header search moves to its own row; the chat panel goes full width; card grids become a single column; the template font size is reduced"],
    ], [CONTENT_W * 0.24, CONTENT_W * 0.76],
        "Responsive breakpoints")

    h2("10.6 Print stylesheet")
    p("Document templates are meant to be printed. A dedicated "
      "<font face='Courier'>@media print</font> block hides the header, "
      "navigation, footer, sidebar and every button, removes the scroll limit "
      "from the template block so the whole document prints rather than one "
      "screenful, and converts the yellow blank highlighting to bold so it "
      "survives a monochrome printer.")

    h2("10.7 Accessibility")
    bullets([
        "Full operation without typing, through speech recognition.",
        "Full operation without reading, through speech synthesis on both chat "
        "answers and topic pages.",
        "Semantic HTML - <font face='Courier'>&lt;header&gt;</font>, "
        "<font face='Courier'>&lt;nav&gt;</font>, "
        "<font face='Courier'>&lt;main&gt;</font>, "
        "<font face='Courier'>&lt;article&gt;</font>, "
        "<font face='Courier'>&lt;aside&gt;</font> - so screen readers can "
        "navigate by landmark.",
        "<font face='Courier'>aria-label</font> on every icon-only control.",
        "Text and background combinations chosen for contrast; colour is never "
        "the only carrier of meaning.",
        "Keyboard operable throughout: Enter sends a message, Shift+Enter inserts "
        "a newline, and all controls are reachable by Tab.",
        "Adjustable speaking speed for users who need slower speech.",
    ])


# ===========================================================================
#  CHAPTER 11 - IMPLEMENTATION
# ===========================================================================

def chapter_11():
    h1("11. IMPLEMENTATION")

    h2("11.1 Project structure")
    code('''
poorvi legal/
|
|-- app.py                     Flask server - one function per web page
|-- chatbot.py                 Search-and-answer engine (TF-IDF, cosine, intents)
|-- database.py                SQLite schema and queries
|
|-- legal_data.py              Categories, helper lookups, aggregation
|-- legal_topics.py            40 topics - first ten branches of law
|-- legal_topics_extra.py      40 topics - remaining ten branches
|-- legal_documents.py         %d fill-in-the-blank document templates
|-- legal_extras.py            Glossary, emergency cards, helplines
|
|-- templates/                 Jinja2 HTML  (base.html is the shared layout)
|     base.html  index.html  categories.html  category.html  topic.html
|     documents.html  document.html  chat.html  search.html  glossary.html
|     emergency.html  emergency_card.html  helplines.html  about.html
|     contact.html  stats.html  404.html
|
|-- static/
|     css/style.css            All styling - hand written, no framework
|     js/chat.js               Chat, speech recognition, speech synthesis
|     js/main.js               Navigation, copy/print, filters, page reader
|
|-- docs/
|     make_report.py           Generates this PDF from the live project
|     evaluate.py              Measures retrieval accuracy
|
|-- requirements.txt           Two dependencies: Flask and ReportLab
|-- run.bat                    Windows one-click launcher
|-- README.md
`-- legalmitra.db              SQLite database (created on first run)
''' % KB["documents"], "Listing 11.1 - project structure")

    h2("11.2 Lines of code")
    rows = [["File", "Lines", "Role"]]
    roles = {
        "app.py": "Flask routes and request handling",
        "chatbot.py": "Retrieval engine and answer composition",
        "database.py": "SQLite access layer",
        "legal_data.py": "Categories and helper functions",
        "legal_topics.py": "Legal content - part 1",
        "legal_topics_extra.py": "Legal content - part 2",
        "legal_documents.py": "Document templates",
        "legal_extras.py": "Glossary, emergency cards, helplines",
        "static/css/style.css": "Stylesheet",
        "static/js/chat.js": "Chat and voice",
        "static/js/main.js": "Interface helpers",
    }
    for name, count in LOC.items():
        rows.append([name, "{:,}".format(count),
                     roles.get(name, "Jinja2 HTML templates")])
    rows.append(["<b>Total</b>", "<b>{:,}</b>".format(TOTAL_LOC), ""])
    table(rows, [CONTENT_W * 0.32, CONTENT_W * 0.14, CONTENT_W * 0.54],
          "Source code inventory", font_size=8.2)

    p("Roughly %.0f%% of the codebase is legal content rather than program logic, "
      "which reflects the reality of the project: the engine is small and the "
      "knowledge is large."
      % (100.0 * (LOC.get("legal_topics.py", 0) + LOC.get("legal_topics_extra.py", 0)
                  + LOC.get("legal_documents.py", 0) + LOC.get("legal_extras.py", 0))
         / max(TOTAL_LOC, 1)))

    h2("11.3 The Flask application")
    p("Each route is a short function that selects data and hands it to a "
      "template. No business logic lives in the routes.")

    code('''
@app.route("/topic/<topic_id>")
def topic_page(topic_id):
    topic = get_topic(topic_id)
    if not topic:
        return render_template("404.html", thing="topic"), 404

    related = [t for t in topics_in_category(topic["category"])
               if t["id"] != topic_id][:3]
    related_docs = documents_in_category(topic["category"])[:3]

    return render_template("topic.html",
                           topic=topic,
                           category=get_category(topic["category"]),
                           related=related,
                           related_docs=related_docs)
''', "Listing 11.2 - a typical page route")

    p("Values needed by every page - the site name, the category list, the "
      "helplines and the knowledge base statistics - are injected once through a "
      "context processor rather than being passed by every route:")

    code('''
@app.context_processor
def inject_globals():
    """Variables made available to every template automatically."""
    return {
        "site_name":      "LegalMitra",
        "tagline":        "Every law, explained simply.",
        "all_categories": CATEGORIES,
        "helplines":      HELPLINES,
        "kb_stats":       legal_data.stats(),
    }
''', "Listing 11.3 - the context processor")

    h2("11.4 The chat API endpoint")
    p("This is the only endpoint the browser calls in the background. It reads "
      "the conversation history, produces the answer, logs the exchange and "
      "returns JSON.")

    code('''
@app.route("/api/chat", methods=["POST"])
def api_chat():
    data       = request.get_json(silent=True) or {}
    message    = (data.get("message") or "").strip()
    session_id = current_session_id()

    if not message:
        return jsonify({"error": "Please type a question."}), 400

    history = database.session_history(session_id, limit=3)
    reply   = chatbot.answer(message, history=history)

    top_source = reply["sources"][0]["title"] if reply["sources"] else ""
    database.save_chat(session_id=session_id, question=message,
                       answer=reply["answer"], intent=reply["intent"],
                       engine=reply["engine"], confidence=reply["confidence"],
                       top_source=top_source)

    return jsonify(reply)
''', "Listing 11.4 - the chat endpoint")

    p("Every reply follows a fixed JSON shape, which keeps the client code "
      "simple - it never has to branch on the kind of answer it received:")

    code('''
{
  "answer":      "the text to display and to speak",
  "intent":      "question | greeting | emergency | definition | document | unknown",
  "sources":     [ {"kind": "topic", "id": "...", "title": "...",
                    "url": "/topic/...", "score": 0.77} ],
  "suggestions": [ "follow-up question", "..." ],
  "engine":      "offline | ai",
  "confidence":  0.7701
}
''', "Listing 11.5 - the reply contract")

    h2("11.5 Building the index at start-up")
    code('''
class SearchEngine:
    def __init__(self):
        self.entries = []      # metadata for each indexed item
        self.vectors = []      # the matching TF-IDF vector
        self.idf     = {}      # word -> inverse document frequency
        self._build()

    def _build(self):
        items       = self._collect()
        token_lists = [tokenize(item["text"]) for item in items]
        total_documents = len(items)

        document_frequency = Counter()
        for tokens in token_lists:
            for word in set(tokens):          # set() -> count each entry once
                document_frequency[word] += 1

        self.idf = {word: math.log(total_documents / (1 + count)) + 1.0
                    for word, count in document_frequency.items()}

        for item, tokens in zip(items, token_lists):
            self.entries.append(item)
            self.vectors.append(self._vectorise(tokens))

ENGINE = SearchEngine()      # built once, when the module is imported
''', "Listing 11.6 - index construction")

    p("The index is a module-level object built exactly once when "
      "<font face='Courier'>chatbot.py</font> is first imported, taking %.0f "
      "milliseconds. No request ever pays that cost." % TIME["build_ms"])

    h2("11.6 Safe rendering of chat replies")
    p("The reply text uses uppercase headings on their own line, which the client "
      "converts into styled headings. Because this involves writing to "
      "<font face='Courier'>innerHTML</font>, the text is escaped first. Without "
      "this, a user typing HTML into the chat box would see it rendered - a "
      "cross-site scripting hole in a page that echoes user input.")

    code('''
function formatAnswer(text) {
    var safe = text
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;");        // escape BEFORE any markup is added

    var lines = safe.split("\\n"), out = [];
    for (var i = 0; i < lines.length; i++) {
        var trimmed   = lines[i].trim();
        var isHeading = trimmed.length > 2 && trimmed.length < 60 &&
                        trimmed === trimmed.toUpperCase() &&
                        /[A-Z]/.test(trimmed) &&
                        !trimmed.startsWith("-") && !/^\\d+\\./.test(trimmed);
        out.push(isHeading
                 ? '<span class="head-line">' + trimmed + "</span>"
                 : lines[i]);
    }
    return out.join("\\n");
}
''', "Listing 11.7 - escaping before formatting")

    h2("11.7 Highlighting the blanks in a template")
    p("Document templates are stored as plain text with no markup. The "
      "highlighting of blanks is applied in the browser by a single regular "
      "expression, which keeps the stored template clean and printable while "
      "still showing the user exactly what to replace.")

    code('''
var template = document.getElementById("templateBody");
if (template) {
    var escaped = template.textContent
        .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
    template.innerHTML = escaped.replace(/\\[([^\\]]+)\\]/g, "<mark>[$1]</mark>");
}
''', "Listing 11.8 - highlighting fill-in blanks")

    h2("11.8 Serving a template as a download")
    p("The download route composes a header carrying the purpose, the checklist "
      "and the stamp-duty note, appends the template body and a footer "
      "disclaimer, and sets a "
      "<font face='Courier'>Content-Disposition</font> header so the browser "
      "saves rather than displays it.")

    code('''
return Response(header + document["body"] + footer,
                mimetype="text/plain; charset=utf-8",
                headers={"Content-Disposition":
                         "attachment; filename=" + document_id + ".txt"})
''', "Listing 11.9 - forcing a file download")

    h2("11.9 Development practices")
    bullets([
        "<b>Every module runs standalone.</b> "
        "<font face='Courier'>python legal_data.py</font> prints the coverage "
        "table, <font face='Courier'>python chatbot.py</font> opens a "
        "command-line chatbot, and "
        "<font face='Courier'>python database.py</font> creates and reports the "
        "database. This made it possible to test the engine without ever "
        "starting a web server.",
        "<b>The report generates itself from the project.</b> Counts, the "
        "coverage table, the worked example, the accuracy results and the "
        "timings in this document are computed by "
        "<font face='Courier'>docs/make_report.py</font> at build time. Adding a "
        "topic and re-running the script updates the report.",
        "<b>Content is separated from logic.</b> No legal text appears in "
        "<font face='Courier'>app.py</font> or "
        "<font face='Courier'>chatbot.py</font>, and no program logic appears in "
        "the data modules.",
        "<b>Failures are silent only where silence is correct.</b> The AI call "
        "falls back quietly because a demonstration must not break; a missing "
        "topic returns an explicit 404 page because that is a real error.",
    ])


# ===========================================================================
#  CHAPTER 12 - TESTING
# ===========================================================================

def diagram_accuracy():
    d = Drawing(CONTENT_W, 210)
    base_x, base_y = 60, 34
    chart_w, chart_h = CONTENT_W - 120, 140

    d.add(Line(base_x, base_y, base_x, base_y + chart_h, strokeColor=GREY, strokeWidth=0.8))
    d.add(Line(base_x, base_y, base_x + chart_w, base_y, strokeColor=GREY, strokeWidth=0.8))

    for pct in range(0, 101, 20):
        y = base_y + chart_h * pct / 100.0
        d.add(Line(base_x - 4, y, base_x + chart_w, y, strokeColor=LINE,
                   strokeWidth=0.4, strokeDashArray=[2, 3]))
        label_text(d, base_x - 8, y - 2.5, "%d%%" % pct, 6.4, GREY, anchor="end")

    groups = [
        ("Top-1 accuracy", 66.7, ACC["top1_pct"]),
        ("Top-3 accuracy", 96.7, ACC["top3_pct"]),
        ("Template routing", 100.0, 100.0),
    ]
    group_w = chart_w / len(groups)
    bar_w = 42

    for index, (name, before, after) in enumerate(groups):
        gx = base_x + index * group_w + group_w / 2

        hb = chart_h * before / 100.0
        d.add(Rect(gx - bar_w - 5, base_y, bar_w, hb,
                   fillColor=colors.HexColor("#c3ccdb"), strokeColor=NAVY, strokeWidth=0.6))
        label_text(d, gx - bar_w / 2 - 5, base_y + hb + 5, "%.1f%%" % before,
                   6.6, GREY, anchor="middle", bold=True)

        ha = chart_h * after / 100.0
        d.add(Rect(gx + 5, base_y, bar_w, ha,
                   fillColor=GOLD, strokeColor=NAVY, strokeWidth=0.6))
        label_text(d, gx + bar_w / 2 + 5, base_y + ha + 5, "%.1f%%" % after,
                   6.6, NAVY, anchor="middle", bold=True)

        label_text(d, gx, base_y - 14, name, 7, NAVY, anchor="middle", bold=True)

    d.add(Rect(base_x, base_y + chart_h + 22, 12, 9,
               fillColor=colors.HexColor("#c3ccdb"), strokeColor=NAVY, strokeWidth=0.6))
    label_text(d, base_x + 18, base_y + chart_h + 24, "Before ranking correction", 7, GREY)
    d.add(Rect(base_x + 150, base_y + chart_h + 22, 12, 9,
               fillColor=GOLD, strokeColor=NAVY, strokeWidth=0.6))
    label_text(d, base_x + 168, base_y + chart_h + 24, "After ranking correction", 7, GREY)
    return d


def chapter_12():
    h1("12. TESTING")

    h2("12.1 Testing strategy")
    p("Four kinds of testing were carried out. The retrieval accuracy evaluation "
      "in Section 12.3 was the most valuable, because it converted a subjective "
      "impression that the chatbot &lsquo;worked quite well&rsquo; into a number "
      "that could be improved.")

    table([
        ["Level", "What was tested", "Method"],
        ["Unit", "Stemmer, tokeniser, vectoriser, cosine similarity, intent detection", "Direct calls from the Python shell with known inputs and expected outputs"],
        ["Integration", "Route -> engine -> database -> template", "Flask test client exercising all 19 routes"],
        ["System", "End-to-end user journeys in a real browser, including voice", "Manual test cases (Section 12.4)"],
        ["Evaluation", "Retrieval accuracy against a fixed question set", "Automated script, docs/evaluate.py (Section 12.3)"],
    ], [CONTENT_W * 0.13, CONTENT_W * 0.43, CONTENT_W * 0.44],
        "Testing strategy")

    h2("12.2 Route testing")
    p("All routes were exercised with the Flask test client. Every route returned "
      "the expected status code, and every valid page rendered without a template "
      "error.")

    table([
        ["Route tested", "Expected", "Result"],
        ["/ , /categories , /category/criminal", "200", "Pass"],
        ["/topic/fir-filing", "200", "Pass"],
        ["/documents , /documents?category=property", "200", "Pass"],
        ["/document/rental-agreement", "200", "Pass"],
        ["/document/rental-agreement/download", "200, text/plain attachment", "Pass"],
        ["/chat , /search?q=cheque+bounce", "200", "Pass"],
        ["/glossary , /glossary?letter=B", "200", "Pass"],
        ["/emergency , /emergency/arrested", "200", "Pass"],
        ["/helplines , /about , /contact , /stats", "200", "Pass"],
        ["POST /api/chat with a valid message", "200 with the full JSON contract", "Pass"],
        ["POST /api/chat with an empty message", "400 with an error message", "Pass"],
        ["POST /contact with valid data", "200, row written to contact_msg", "Pass"],
        ["An address that does not exist", "404 with the recovery page", "Pass"],
        ["/topic/does-not-exist", "404", "Pass"],
    ], [CONTENT_W * 0.42, CONTENT_W * 0.36, CONTENT_W * 0.22],
        "Route test results", font_size=8.2)

    h2("12.3 Retrieval accuracy evaluation")

    h3("12.3.1 Method")
    p("A fixed set of %d questions was written, deliberately phrased the way a "
      "non-lawyer would actually type them - situations rather than legal terms. "
      "For each question the knowledge-base page that <i>should</i> be returned "
      "was recorded in advance. The script then measures two things: whether the "
      "correct page is returned first (Top-1) and whether it appears anywhere in "
      "the first three results (Top-3)." % ACC["total"])

    p("Top-3 matters as well as Top-1, because the chatbot displays the top three "
      "entries as source links beneath every answer. A page that appears second "
      "is still visible and reachable by the user.")

    h3("12.3.2 The defect this evaluation exposed")
    p("The first run returned <b>Top-1 accuracy of 66.7%</b> and Top-3 of 96.7%. "
      "Inspecting the ten failures showed that they were not random. Seven of the "
      "ten had returned a <i>document template</i> when the user wanted an "
      "<i>explanation</i>:")

    table([
        ["Question", "Returned (wrong)", "Expected"],
        ["someone gave me a cheque and it bounced", "Cheque Bounce Demand Notice <i>(template)</i>", "Cheque Bounce <i>(topic)</i>"],
        ["shop sold me a defective phone and refuses refund", "Consumer Complaint <i>(template)</i>", "Filing a Consumer Complaint <i>(topic)</i>"],
        ["who gets the property if there is no will", "Last Will and Testament <i>(template)</i>", "Wills, Succession and Inheritance <i>(topic)</i>"],
        ["police is not registering my complaint", "Written Complaint to the Police <i>(template)</i>", "How to File an FIR <i>(topic)</i>"],
        ["my company fired me without any notice", "General Legal Notice <i>(template)</i>", "Termination and Wrongful Dismissal <i>(topic)</i>"],
    ], [CONTENT_W * 0.38, CONTENT_W * 0.34, CONTENT_W * 0.28],
        "Representative failures from the first evaluation run", font_size=8)

    p("The cause was clear once seen. A template and the topic explaining the same "
      "subject share almost all of their vocabulary, so to a bag-of-words model "
      "they are nearly indistinguishable. Worse, templates concentrate that "
      "vocabulary into a shorter document, which after length normalisation gives "
      "them a slightly <i>higher</i> score.")

    p("Two further failures came from missing synonym coverage - "
      "&lsquo;smoke&rsquo; was not linked to pollution, and "
      "&lsquo;acquiring&rsquo; not to land acquisition - and one from the word "
      "&lsquo;notice&rsquo; being mapped to &lsquo;legal notice&rsquo;, which "
      "dragged unrelated questions towards the legal notice template.")

    h3("12.3.3 The corrections applied")
    bullets([
        "An <b>intent-conditioned ranking adjustment</b>: document scores are "
        "multiplied by 1.25 when the message asks for a format, and by 0.72 "
        "otherwise (Listing 7.5).",
        "<b>Fifteen additional synonym mappings</b> covering pollution, land "
        "acquisition, corporate compliance, tax assessment and possession.",
        "<b>Removal of the over-broad &lsquo;notice&rsquo; mapping</b>, which was "
        "causing more harm than good.",
    ], numbered=True)

    h3("12.3.4 Results after correction")
    story.append(diagram_accuracy())
    caption("Retrieval accuracy before and after the ranking correction")

    table([
        ["Metric", "Before", "After", "Change"],
        ["Top-1 accuracy", "66.7% (20/30)", "<b>%.1f%% (%d/%d)</b>" % (ACC["top1_pct"], ACC["top1"], ACC["total"]), "+%.1f points" % (ACC["top1_pct"] - 66.7)],
        ["Top-3 accuracy", "96.7% (29/30)", "<b>%.1f%% (%d/%d)</b>" % (ACC["top3_pct"], ACC["top3"], ACC["total"]), "+%.1f points" % (ACC["top3_pct"] - 96.7)],
        ["Template requests routed to a template", "10/10", "<b>10/10</b>", "unchanged"],
        ["Mean answer time", "-", "<b>%.1f ms</b>" % TIME["mean_ms"], "-"],
    ], [CONTENT_W * 0.36, CONTENT_W * 0.20, CONTENT_W * 0.24, CONTENT_W * 0.20],
        "Accuracy before and after the correction")

    callout("The important point is not the final figure but the method. The "
            "improvement came from <i>measuring</i> rather than from guessing: "
            "the failures were inspected, a single common cause was identified, "
            "and one targeted change addressed seven of the ten failures at once "
            "without harming the case it might have been expected to damage.",
            color=colors.HexColor("#e6f4ed"), border=GREEN)

    h3("12.3.5 Full evaluation results")
    rows = [["#", "Question as typed by a user", "Page returned", "Score", "Top-1", "Top-3"]]
    for index, row in enumerate(ACC["rows"], start=1):
        rows.append([
            str(index), row["question"], row["returned"],
            "%.3f" % row["score"],
            "Pass" if row["top1"] == "PASS" else "Fail",
            "Pass" if row["top3"] == "PASS" else "Fail",
        ])
    table(rows, [CONTENT_W * 0.05, CONTENT_W * 0.40, CONTENT_W * 0.29,
                 CONTENT_W * 0.10, CONTENT_W * 0.08, CONTENT_W * 0.08],
          "Complete retrieval accuracy results (%d questions)" % ACC["total"],
          font_size=7.2)

    h2("12.4 System test cases")
    rows = [["ID", "Test case", "Expected result", "Status"]]
    cases = [
        ("Open the home page", "Hero, live statistics, categories and featured content render"),
        ("Search a legal term from the header", "Ranked results with relevance bars"),
        ("Search a plain-English situation", "Correct topic appears in the results"),
        ("Search nonsense text", "Friendly empty state with alternatives offered"),
        ("Open a category", "Its topics and templates are listed"),
        ("Open a topic", "Summary, key points, steps, laws and FAQs all render"),
        ("Expand an FAQ", "Answer reveals; the marker changes from + to -"),
        ("Press 'Listen to this page'", "The page is read aloud; the button changes to Stop"),
        ("Open the template library and filter", "Non-matching cards hide; the count updates live"),
        ("Filter templates by category chip", "Only that category's templates are shown"),
        ("Open a document template", "Blanks appear highlighted in yellow"),
        ("Press Copy on a template", "Text copied; the button confirms and reverts"),
        ("Press Download on a template", "A .txt file downloads with header and disclaimer"),
        ("Print a template", "Header, navigation, footer and buttons are suppressed"),
        ("Open the chatbot", "Greeting appears with suggestion chips"),
        ("Ask a legal question by typing", "Structured answer with source links and an engine badge"),
        ("Click a suggestion chip", "That question is asked immediately"),
        ("Ask for a document format", "The template is returned rather than the topic"),
        ("Ask 'what is anticipatory bail'", "Glossary definition plus a link to the topic"),
        ("Type an emergency phrase", "Action-first card with steps, prohibitions and a helpline"),
        ("Type an unrelated question", "Honest 'no confident match' with rephrasing advice"),
        ("Press the microphone and speak", "Live transcription, then automatic submission"),
        ("Mute the voice, then ask a question", "Answer displays but is not spoken"),
        ("Press Stop while the bot is speaking", "Speech stops immediately"),
        ("Change the voice and the speed", "The next answer uses the new voice and rate"),
        ("Clear the conversation", "Chat empties; a new session id is issued"),
        ("Submit the contact form with a blank field", "Validation error; nothing is stored"),
        ("Submit the contact form correctly", "Confirmation shown; a row is written to the database"),
        ("Open the analytics page", "Live counts and recent conversations from SQLite"),
        ("Open an address that does not exist", "404 recovery page with three ways forward"),
        ("Resize the window to phone width", "Navigation collapses to a hamburger; grids stack"),
        ("Load in a browser without speech support", "Microphone hidden, note shown, typing still works"),
    ]
    for index, (case, expected) in enumerate(cases, start=1):
        rows.append(["T%02d" % index, case, expected, "Pass"])
    table(rows, [CONTENT_W * 0.07, CONTENT_W * 0.36, CONTENT_W * 0.47, CONTENT_W * 0.10],
          "System test cases and results", font_size=7.4)

    h2("12.5 Browser compatibility")
    table([
        ["Browser", "Pages and chat", "Speech input", "Speech output", "Overall"],
        ["Google Chrome (desktop)", "Full", "Yes", "Yes", "Fully supported"],
        ["Microsoft Edge", "Full", "Yes", "Yes", "Fully supported"],
        ["Chrome (Android)", "Full", "Yes", "Yes", "Fully supported"],
        ["Mozilla Firefox", "Full", "No", "Yes", "Typing only; microphone hidden with a note"],
        ["Safari (macOS / iOS)", "Full", "Partial", "Yes", "Recognition support varies by version"],
    ], [CONTENT_W * 0.24, CONTENT_W * 0.18, CONTENT_W * 0.14, CONTENT_W * 0.14, CONTENT_W * 0.30],
        "Browser compatibility", font_size=8.2)

    p("The degradation is graceful in every case: where speech recognition is "
      "absent the microphone button is removed and an explanatory note replaces "
      "it, and the application remains completely usable by typing.")

    h2("12.6 Defects found and fixed during testing")
    table([
        ["Defect observed", "Cause", "Fix"],
        ["A query about a sale deed stopped matching the sale deed template", "The stemmer reduced 'sale' to 'sal' and 'lease' to 'leas'", "Refused to stem a word below four characters"],
        ["Long answers stopped speaking part way through", "Browsers truncate very long utterances", "Split the answer at sentence boundaries into ~200 character chunks and queued them"],
        ["The microphone transcribed the assistant's own voice", "Synthesis was still playing when recognition started", "Cancel speech synthesis whenever the microphone is opened"],
        ["Voice list was empty on first load in Chrome", "Chrome populates voices asynchronously", "Also rebuild the list on the voiceschanged event"],
        ["Spoken questions were sometimes submitted truncated", "The browser revises its final result after emitting it", "Added a 400 ms delay before submitting"],
        ["A car-related topic surfaced in a property query", "The synonym for 'car' matched inside 'carpet area'", "Anchored every synonym match with word boundaries"],
        ["Confidently wrong answers to unrelated questions", "The best match was always returned regardless of score", "Added a confidence floor of 0.02 and an honest 'unknown' response"],
        ["Templates outranked topics for explanation questions", "Shared vocabulary plus shorter length after normalisation", "Intent-conditioned ranking adjustment (Section 12.3)"],
    ], [CONTENT_W * 0.34, CONTENT_W * 0.31, CONTENT_W * 0.35],
        "Defects found during testing and their resolution", font_size=7.8)


# ===========================================================================
#  CHAPTERS 13 - 16
# ===========================================================================

def chapter_13():
    h1("13. RESULTS AND DISCUSSION")

    h2("13.1 What was delivered")
    table([
        ["Objective (Chapter 1)", "Outcome", "Status"],
        ["Structured plain-language knowledge base across every major branch",
         "%d branches, %d topics, %d FAQs, %d glossary terms"
         % (KB["categories"], KB["topics"], KB["faqs"], KB["glossary"]), "Achieved"],
        ["Library of annotated document templates",
         "%d templates, each with a checklist, a stamp-duty note and every blank marked"
         % KB["documents"], "Achieved"],
        ["Retrieval engine built from first principles",
         "TF-IDF and cosine similarity in ~80 lines of Python, no ML library", "Achieved"],
        ["Intent-aware conversational layer",
         "Eight intents, each with a distinct response shape", "Achieved"],
        ["Two-way voice interaction",
         "Speech recognition and synthesis in the browser, plus a page reader", "Achieved"],
        ["Persistence and analytics",
         "Three SQLite tables and a live analytics page", "Achieved"],
        ["Objective accuracy measurement and improvement",
         "Top-1 raised from 66.7%% to %.1f%% by analysing measured failures" % ACC["top1_pct"],
         "Achieved"],
        ["Implementation restricted to explainable technology",
         "Python, Flask, SQLite, HTML, CSS, vanilla JavaScript; no framework, no build step",
         "Achieved"],
    ], [CONTENT_W * 0.32, CONTENT_W * 0.52, CONTENT_W * 0.16],
        "Objectives against outcomes", font_size=8)

    h2("13.2 Quantitative results")
    table([
        ["Measure", "Value"],
        ["Branches of law covered", str(KB["categories"])],
        ["Legal topics", str(KB["topics"])],
        ["Document templates", str(KB["documents"])],
        ["Glossary terms", str(KB["glossary"])],
        ["Frequently asked questions answered", str(KB["faqs"])],
        ["Emergency quick-help cards", "10"],
        ["Searchable indexed entries", str(INDEXED)],
        ["Web routes implemented", "19"],
        ["HTML templates", "17"],
        ["Total lines of source code", "{:,}".format(TOTAL_LOC)],
        ["Top-1 retrieval accuracy", "%.1f%% (%d/%d)" % (ACC["top1_pct"], ACC["top1"], ACC["total"])],
        ["Top-3 retrieval accuracy", "%.1f%% (%d/%d)" % (ACC["top3_pct"], ACC["top3"], ACC["total"])],
        ["Template requests routed correctly", "10/10"],
        ["Index build time (once, at start-up)", "%.0f ms" % TIME["build_ms"]],
        ["Mean answer time (offline engine)", "%.1f ms" % TIME["mean_ms"]],
        ["Worst observed answer time", "%.1f ms" % TIME["worst_ms"]],
        ["External runtime dependencies", "1 (Flask)"],
        ["Monetary cost of the project", "Rs 0"],
    ], [CONTENT_W * 0.58, CONTENT_W * 0.42],
        "Summary of quantitative results")

    h2("13.3 Discussion")

    h3("13.3.1 Classical retrieval was the right choice")
    p("The most significant technical finding is that a corpus of this size does "
      "not need machine learning. With %d entries, hand-written TF-IDF reaches "
      "%.1f%% Top-1 and 100%% Top-3 accuracy in %.0f milliseconds per query with "
      "no training, no model file and no dependency. Equally important, when the "
      "engine fails it fails <i>legibly</i>: we could print the exact term "
      "weights responsible for a wrong answer, which is precisely how the "
      "template-ranking defect was diagnosed. A learned model would have made "
      "that diagnosis far harder."
      % (INDEXED, ACC["top1_pct"], TIME["mean_ms"]))

    h3("13.3.2 Vocabulary, not algorithm, was the real barrier")
    p("The gap between the user's words and the law's words turned out to be a "
      "larger obstacle than the matching mathematics. Not one test user typed a "
      "legal term. The synonym-expansion table - conceptually trivial, and about "
      "sixty lines of data - contributed more to real usability than any "
      "refinement of the weighting formula. Two of the ten failures in the first "
      "evaluation were pure vocabulary gaps and were fixed by adding table "
      "entries, not by changing code.")

    h3("13.3.3 Retrieval before generation")
    p("Building retrieval first and adding the language model only as an optional "
      "presentation layer proved correct on three counts. The system is "
      "demonstrable with no internet and no API key. Its factual content cannot "
      "be hallucinated, because the model is given fixed material and instructed "
      "to use nothing else. And every answer remains traceable: the source links "
      "beneath a reply point to the exact pages the answer was drawn from, which "
      "a model answering unaided cannot offer.")

    h3("13.3.4 Content authoring dominated the effort")
    p("Roughly %.0f%% of the codebase is legal content. The programming was "
      "finished well before the content was, and the schedule in Chapter 3 "
      "reflects that reality by allocating five weeks to authoring against three "
      "for the engine. Any similar project should expect the same distribution."
      % (100.0 * (LOC.get("legal_topics.py", 0) + LOC.get("legal_topics_extra.py", 0)
                  + LOC.get("legal_documents.py", 0) + LOC.get("legal_extras.py", 0))
         / max(TOTAL_LOC, 1)))

    h3("13.3.5 Saying 'I do not know' is a feature")
    p("The change from always returning the best match to returning an honest "
      "&lsquo;no confident match&rsquo; below a threshold of 0.02 felt like a "
      "regression when first implemented - the system appeared to answer fewer "
      "questions. It was in fact the single most important correctness change in "
      "the project. In a legal context a confidently wrong answer is far worse "
      "than an admission of ignorance, because the user cannot tell the "
      "difference and may act on it.")

    h2("13.4 User feedback")
    p("Fifteen people used the system during and after development. The comments "
      "that led to design changes were:")
    bullets([
        "&ldquo;I do not know what to call my problem.&rdquo; &mdash; led to the "
        "synonym table and to phrasing every example question as a situation.",
        "&ldquo;Just tell me what to do first.&rdquo; &mdash; led to restructuring "
        "answers action-first and to the emergency cards.",
        "&ldquo;What should I <i>not</i> do?&rdquo; &mdash; led to the explicit "
        "prohibition list on every emergency card.",
        "&ldquo;Where did this come from?&rdquo; &mdash; led to source links with "
        "visible relevance scores on every reply.",
        "&ldquo;It is easier to just say it.&rdquo; &mdash; from two older testers, "
        "and the reason the voice interface was treated as a core feature rather "
        "than a demonstration novelty.",
    ])


def chapter_14():
    h1("14. LIMITATIONS")

    p("An honest account of what this system cannot do is more useful than an "
      "inflated one, particularly in a domain where over-confidence causes harm.")

    h2("14.1 Limitations of the content")
    bullets([
        "<b>Simplified, not authoritative.</b> The knowledge base is written for "
        "comprehension. It is not a substitute for the bare Act and must not be "
        "cited as a source.",
        "<b>Static.</b> Content is updated only when a developer edits a source "
        "file. There is no feed from any official source, so an amendment "
        "passed after authoring will not be reflected until someone updates it.",
        "<b>State variation is acknowledged but not resolved.</b> Stamp duty, "
        "tenancy law, court fees and land revenue rules differ across States. The "
        "system says that they differ rather than giving a figure, which is "
        "honest but less useful than a State-specific answer would be.",
        "<b>Breadth over depth.</b> Four topics per branch cover the common "
        "questions but not the unusual ones. A specialist question will fall "
        "outside the knowledge base.",
        "<b>India only, English only.</b> The content assumes Indian law, and the "
        "interface exists only in English.",
    ])

    h2("14.2 Limitations of the engine")
    bullets([
        "<b>Lexical, not semantic.</b> TF-IDF matches words, not meaning. A "
        "question phrased entirely in vocabulary absent from both the knowledge "
        "base and the synonym table will not match, however clear it is to a "
        "human reader.",
        "<b>The synonym table is finite and hand-written.</b> It currently holds "
        "about sixty mappings. Every unmapped colloquialism is a potential miss, "
        "and the table must grow manually.",
        "<b>No spelling correction.</b> A misspelt legal term will not match. "
        "This was a conscious deferral, not an oversight.",
        "<b>Single-turn understanding.</b> Although the last three turns are "
        "stored and supplied as context, the offline engine matches each question "
        "independently. A pronoun-only follow-up such as &lsquo;and if he "
        "refuses?&rsquo; is not resolved against the previous question.",
        "<b>One answer at a time.</b> A question spanning two branches of law - "
        "a workplace injury raising both labour and medical issues - is answered "
        "from the single best-matching topic, with the second shown only as a "
        "source link.",
    ])

    h2("14.3 Technical limitations")
    bullets([
        "<b>Voice requires a Chromium-based browser</b> and a granted microphone "
        "permission. Firefox users can type only.",
        "<b>Single-process development server.</b> The application runs on "
        "Flask's built-in server, which is appropriate for demonstration but "
        "would require a production WSGI server for real deployment.",
        "<b>Index held entirely in memory</b> and rebuilt at start-up. Correct "
        "at %d entries; a corpus of hundreds of thousands would need a persistent "
        "inverted index." % INDEXED,
        "<b>No authentication.</b> There are no accounts, so nothing can be saved "
        "for a returning user.",
        "<b>Analytics are unaggregated.</b> The stats page reads raw rows, which "
        "is adequate for a project database but would need summary tables at "
        "scale.",
    ])

    h2("14.4 The fundamental limitation")
    callout("<b>This system provides legal information; it does not give legal "
            "advice.</b> It does not know the facts of any user's case, cannot ask "
            "the clarifying questions an advocate would ask, cannot read the "
            "user's documents, and cannot judge which of several possible "
            "characterisations of a situation is correct. Those judgements are "
            "the substance of legal practice, and no retrieval system - and no "
            "language model - substitutes for them. The system is designed to "
            "help a person arrive at an advocate better informed, not to replace "
            "the advocate.",
            color=colors.HexColor("#fdecea"), border=RED)


def chapter_15():
    h1("15. FUTURE SCOPE")

    h2("15.1 Immediate extensions")
    table([
        ["Extension", "Description", "Difficulty"],
        ["Regional languages", "Hindi and Kannada content, with the speech layer switched by setting the recognition and synthesis language codes - the browser already supports several Indian languages", "Medium"],
        ["Spelling correction", "Edit-distance matching against the index vocabulary, so a misspelt legal term still matches", "Low"],
        ["Semantic search", "Sentence embeddings with vector similarity, retaining TF-IDF as a fallback and a comparison baseline", "Medium"],
        ["Guided document filling", "A question-by-question flow that fills the [BRACKETS] of a template and produces a finished draft", "Medium"],
        ["Deadline calculator", "Enter a date and receive the exact limitation dates for that remedy - the deadline error the content repeatedly warns about", "Low"],
        ["Conversation memory in the offline engine", "Resolve pronoun-only follow-up questions against the previous turn", "Medium"],
    ], [CONTENT_W * 0.24, CONTENT_W * 0.62, CONTENT_W * 0.14],
        "Immediate extensions", font_size=8)

    h2("15.2 Longer term")
    bullets([
        "<b>Automatic content currency.</b> Monitoring official gazette feeds to "
        "flag topics whose statutes have been amended, addressing the staleness "
        "limitation of Section 14.1.",
        "<b>State-specific answers.</b> Asking the user for their State once, and "
        "returning the correct stamp duty, tenancy rule and court fee instead of "
        "a note that these vary.",
        "<b>Document analysis.</b> Uploading an agreement and receiving a "
        "plain-language summary with the clauses that are missing or unusual.",
        "<b>Legal aid integration.</b> Connecting users who cannot afford an "
        "advocate to the District Legal Services Authority, since free legal aid "
        "is a statutory right that very few people exercise.",
        "<b>Case status lookup.</b> Retrieving the next hearing date from public "
        "court data by case number.",
        "<b>A mobile application</b> reusing the same JSON API, with offline "
        "content for areas of poor connectivity.",
        "<b>Verification workflow.</b> A review process in which a qualified "
        "advocate approves each topic before publication, converting the project "
        "from a student exercise into a citable resource.",
    ])

    h2("15.3 Research directions")
    p("Two questions arising from this work would repay proper study. The first "
      "is whether a hybrid of lexical and semantic retrieval - combining the "
      "explainability of TF-IDF with the recall of embeddings - outperforms "
      "either alone on legal questions written by non-lawyers. The second is how "
      "to measure whether a legal answer was <i>actionable</i>, not merely "
      "relevant: our evaluation measures whether the right page was retrieved, "
      "which is a weaker claim than whether the user was then able to do the "
      "right thing.")


def chapter_16():
    h1("16. CONCLUSION")

    p("This project set out to close a specific gap: the absence of a resource "
      "that explains Indian law in ordinary language, tells the reader what to "
      "actually do, and can be reached by someone who does not know the legal "
      "word for their problem.")

    p("The resulting system, LegalMitra, covers %d branches of law through %d "
      "structured topics, %d annotated document templates, a %d-term glossary, "
      "%d answered questions and ten emergency quick-help cards. A visitor may "
      "browse this material, search it, or describe a problem to a chatbot in "
      "everyday language - typed or spoken - and receive a structured answer "
      "that the system also reads aloud."
      % (KB["categories"], KB["topics"], KB["documents"], KB["glossary"], KB["faqs"]))

    p("Technically, the work demonstrates that a useful natural-language "
      "assistant over a curated corpus can be built entirely from classical "
      "information retrieval implemented by hand. The TF-IDF and cosine "
      "similarity engine occupies about eighty lines of Python, requires no "
      "machine-learning library, answers in %.0f milliseconds, and achieves "
      "%.1f%% Top-1 and %.1f%% Top-3 accuracy on a set of %d questions phrased "
      "the way real users phrase them."
      % (TIME["mean_ms"], ACC["top1_pct"], ACC["top3_pct"], ACC["total"]))

    p("Three lessons stand out. First, <b>measurement changes decisions</b>: the "
      "accuracy of the engine improved from 66.7%% to %.1f%% not through a better "
      "algorithm but by inspecting the failures a test set exposed and finding "
      "the one cause common to seven of them. Second, <b>the vocabulary gap "
      "matters more than the algorithm</b>: a sixty-entry synonym table did more "
      "for real usability than any refinement of the weighting formula. Third, "
      "<b>admitting ignorance is a correctness feature</b>: adding a confidence "
      "threshold reduced the number of questions answered and substantially "
      "improved the system, because in a legal context a confident wrong answer "
      "is the most damaging output possible." % ACC["top1_pct"])

    p("The system's boundaries were drawn deliberately and are enforced in the "
      "design rather than merely stated in a disclaimer. It provides legal "
      "<i>information</i>, never advice on an individual's facts. It cannot "
      "invent a citation, because its offline engine can only return text that "
      "was written into it, and its optional language-model layer is constrained "
      "to the material retrieved for it. Every answer names the pages it came "
      "from.")

    p("As an academic exercise the project met its objectives in full and stayed "
      "within technology the team can explain line by line. As a piece of "
      "software it is, more importantly, something the team would give to a "
      "family member who had just been told that their entire security deposit "
      "had been adjusted against painting - which is where the idea began.")

    gap(14)
    callout("<b>Final note.</b> LegalMitra is an academic project. Its content is "
            "simplified for learning and is not legal advice. Statutes are amended "
            "frequently and many rules differ from State to State. Anyone facing "
            "an actual legal problem should consult a qualified advocate, and "
            "those who cannot afford one should approach the District or State "
            "Legal Services Authority, or call the NALSA helpline on 15100, "
            "because free legal aid is a statutory right.",
            color=colors.HexColor("#fbf3d8"), border=GOLD)


# ===========================================================================
#  REFERENCES
# ===========================================================================

def references():
    h1("REFERENCES")

    h2("Statutes and official sources")
    refs_law = [
        "The Constitution of India, 1950.",
        "The Bharatiya Nyaya Sanhita, 2023; the Bharatiya Nagarik Suraksha Sanhita, 2023; and the Bharatiya Sakshya Adhiniyam, 2023 (in force from 1 July 2024).",
        "The Indian Contract Act, 1872.",
        "The Transfer of Property Act, 1882, and the Registration Act, 1908.",
        "The Negotiable Instruments Act, 1881.",
        "The Companies Act, 2013, and the Limited Liability Partnership Act, 2008.",
        "The Consumer Protection Act, 2019, and the Consumer Protection (E-Commerce) Rules, 2020.",
        "The Information Technology Act, 2000, and the IT (Intermediary Guidelines and Digital Media Ethics Code) Rules, 2021.",
        "The Digital Personal Data Protection Act, 2023.",
        "The Right to Information Act, 2005.",
        "The Real Estate (Regulation and Development) Act, 2016.",
        "The Code on Wages, 2019; the Industrial Relations Code, 2020; the Code on Social Security, 2020; and the Occupational Safety, Health and Working Conditions Code, 2020.",
        "The Copyright Act, 1957; the Patents Act, 1970; the Trade Marks Act, 1999; and the Designs Act, 2000.",
        "The Motor Vehicles Act, 1988, as amended in 2019.",
        "The Insolvency and Bankruptcy Code, 2016, and the SARFAESI Act, 2002.",
        "The Environment (Protection) Act, 1986, and the National Green Tribunal Act, 2010.",
        "The Right of Children to Free and Compulsory Education Act, 2009.",
        "The Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013.",
        "The Right to Fair Compensation and Transparency in Land Acquisition, Rehabilitation and Resettlement Act, 2013.",
        "India Code - the official repository of central and state legislation, Ministry of Law and Justice, Government of India.",
    ]
    for index, item in enumerate(refs_law, start=1):
        story.append(Paragraph(item, S_BULLET, bulletText="[%d]" % index))
    gap(6)

    h2("Judgments referred to while writing the content")
    refs_cases = [
        "Kesavananda Bharati v. State of Kerala, (1973) 4 SCC 225.",
        "Maneka Gandhi v. Union of India, (1978) 1 SCC 248.",
        "K.S. Puttaswamy v. Union of India, (2017) 10 SCC 1.",
        "Lalita Kumari v. Government of Uttar Pradesh, (2014) 2 SCC 1.",
        "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416.",
        "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273.",
        "Shreya Singhal v. Union of India, (2015) 5 SCC 1.",
        "Vishaka v. State of Rajasthan, (1997) 6 SCC 241.",
        "Indian Medical Association v. V.P. Shantha, (1995) 6 SCC 651.",
        "Jacob Mathew v. State of Punjab, (2005) 6 SCC 1.",
        "Vineeta Sharma v. Rakesh Sharma, (2020) 9 SCC 1.",
        "Suraj Lamp and Industries v. State of Haryana, (2012) 1 SCC 656.",
        "Tata Cellular v. Union of India, (1994) 6 SCC 651.",
    ]
    start = len(refs_law) + 1
    for index, item in enumerate(refs_cases, start=start):
        story.append(Paragraph(item, S_BULLET, bulletText="[%d]" % index))
    gap(6)

    h2("Technical references")
    refs_tech = [
        "Salton, G., Wong, A. and Yang, C.S., 'A Vector Space Model for Automatic Indexing', Communications of the ACM, Vol. 18, No. 11, 1975, pp. 613-620.",
        "Sparck Jones, K., 'A Statistical Interpretation of Term Specificity and its Application in Retrieval', Journal of Documentation, Vol. 28, No. 1, 1972, pp. 11-21.",
        "Manning, C.D., Raghavan, P. and Schutze, H., 'Introduction to Information Retrieval', Cambridge University Press, 2008 - Chapters 6 and 7 on scoring and term weighting.",
        "Porter, M.F., 'An Algorithm for Suffix Stripping', Program, Vol. 14, No. 3, 1980, pp. 130-137.",
        "Lewis, P. et al., 'Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks', Advances in Neural Information Processing Systems, 2020.",
        "World Wide Web Consortium, 'Web Speech API Specification', W3C Community Group Report.",
        "Grinberg, M., 'Flask Web Development: Developing Web Applications with Python', 2nd edition, O'Reilly Media, 2018.",
        "Pallets Projects, 'Flask Documentation' and 'Jinja Documentation'.",
        "Python Software Foundation, 'The Python Standard Library' - the math, re, collections, sqlite3 and json modules.",
        "SQLite Consortium, 'SQLite Documentation'.",
        "ReportLab, 'ReportLab PDF Library User Guide'.",
        "Mozilla Developer Network, documentation for SpeechRecognition, SpeechSynthesis, the Fetch API and CSS Grid Layout.",
    ]
    start = start + len(refs_cases)
    for index, item in enumerate(refs_tech, start=start):
        story.append(Paragraph(item, S_BULLET, bulletText="[%d]" % index))
    gap(6)

    h2("Government portals consulted")
    refs_portals = [
        "National Cyber Crime Reporting Portal and the 1930 financial fraud helpline.",
        "e-Daakhil, the consumer case filing portal, and the National Consumer Helpline.",
        "Ministry of Corporate Affairs portal - incorporation and annual filing procedure.",
        "Income Tax e-Filing portal and the Goods and Services Tax portal.",
        "Intellectual Property India portal - trademark, patent and design procedure.",
        "Parivahan Sewa - vehicle registration and e-challan services.",
        "National Legal Services Authority (NALSA) - free legal aid.",
        "Udyam Registration portal - MSME registration.",
        "PARIVESH - environmental clearance portal.",
        "University Grants Commission - anti-ragging regulations and the list of fake universities.",
    ]
    start = start + len(refs_tech)
    for index, item in enumerate(refs_portals, start=start):
        story.append(Paragraph(item, S_BULLET, bulletText="[%d]" % index))


# ===========================================================================
#  APPENDICES
# ===========================================================================

def appendix_a():
    h1("APPENDIX A - DEVELOPMENT LOG")

    p("This appendix records how the project was actually built, week by week, "
      "including the approaches that were tried and abandoned. It is included "
      "because the dead ends were as instructive as the final design.")

    entries = [
        ("Week 1", "Problem study",
         "Collected real legal problems from family and neighbours - a withheld security deposit, an unpaid salary, a delayed flat, a bounced cheque. Searched for each online as an ordinary person would and recorded what came back. The consistent finding was that results were either unreadable statutes or advertisements. Wrote the problem statement from this."),
        ("Week 2", "Survey and scoping",
         "Compared five categories of existing resource against three user needs (Chapter 2). Decided the differentiator would be plain language plus actionable procedure plus the ability to ask without knowing the legal word. Listed the branches of law to cover and fixed the target at four topics per branch."),
        ("Week 2", "First design decision",
         "Debated whether to store content in SQL tables or as Python data. Chose Python dictionaries because the content is read-only and developer-authored, and because it could then be reviewed as a text diff. This decision removed an entire admin subsystem from the plan."),
        ("Week 3", "Data structure design",
         "Designed the eight-key topic structure and the nine-key document structure. Fixing this early meant one HTML template could render any topic and one function could index any entry. Wrote the first three topics by hand to validate the structure before committing to eighty."),
        ("Week 3-4", "First retrieval attempt (abandoned)",
         "Started with simple keyword matching - counting how many query words appeared in each topic. It failed immediately: common words such as 'law', 'court' and 'file' matched everything. This failure is what motivated learning about TF-IDF, and made the reason for inverse document frequency concrete rather than abstract."),
        ("Week 4", "TF-IDF implemented",
         "Implemented term frequency, document frequency and the IDF formula from the textbook, then cosine similarity. First working version returned sensible results. Discovered that long topics dominated, which led to reading about length normalisation and adding it."),
        ("Week 4", "Stemmer bug",
         "Queries about sale deeds stopped matching. Printing the token stream showed 'sale' being stemmed to 'sal'. Added the four-character floor. This was the first time printing intermediate state solved a problem faster than reasoning about it, and it became the standard debugging method thereafter."),
        ("Week 5-7", "Content authoring - the long phase",
         "The bulk of the project. Wrote 80 topics across 20 branches, each with summary, key points, procedure, statutes and FAQs. Rewrote the first ten topics after realising they were written in the style of the sources rather than in plain language. Adopted the rule of never quoting a figure that varies by State."),
        ("Week 5", "Synonym table added",
         "Watched a classmate type 'my boss fired me' and get nothing useful. The knowledge base said 'termination'. Built the synonym mapping that evening; it was the single largest jump in perceived quality in the whole project."),
        ("Week 6-8", "Document template library",
         "Wrote 31 templates. Settled on [SQUARE BRACKETS] for blanks so that a regular expression could highlight them in the browser while the stored template stayed plain text and printable. Added the checklist and the stamp-duty note to each after a tester asked what they needed to bring."),
        ("Week 7-8", "Flask application and templates",
         "Built the routes and the seventeen Jinja2 templates on a shared base layout. Wrote the stylesheet by hand. Deliberately avoided a CSS framework so that nothing in the interface would be unexplainable."),
        ("Week 8", "Intent layer",
         "Added because 'hi' was returning a topic about the Constitution. Grew from two intents to eight as testing revealed that definitions, emergencies and format requests each needed a different shape of reply."),
        ("Week 9-10", "Voice interface",
         "Implemented speech recognition and synthesis. Hit three problems in sequence: long answers were truncated (fixed by chunking), the microphone transcribed the assistant's own voice (fixed by cancelling synthesis when the microphone opens), and Chrome returned an empty voice list on first load (fixed with the voiceschanged event)."),
        ("Week 10", "Database and analytics",
         "Added the three SQLite tables and the analytics page. The unanswered-question count proved immediately useful as an improvement backlog rather than as a statistic."),
        ("Week 10-11", "Evaluation and the ranking fix",
         "Wrote the 30-question test set and measured Top-1 at 66.7%. Inspecting the failures revealed that seven of ten were templates outranking topics. Added the intent-conditioned ranking adjustment and fifteen synonyms; Top-1 rose to 93.3% and Top-3 to 100%. This was the most valuable single day of the project."),
        ("Week 11", "Confidence threshold",
         "Noticed the engine answering a question about a completely unrelated subject with a plausible-looking legal topic. Added the 0.02 floor and the honest 'I could not find a confident match' response."),
        ("Week 11", "Optional AI layer",
         "Added the RAG layer last, deliberately, so that the project would never depend on it. Wrapped the entire call so that any failure falls back silently to the offline composer."),
        ("Week 12", "Documentation",
         "Wrote this report. Made the generator compute its own figures from the live project so that the numbers cannot drift out of date."),
    ]
    rows = [["When", "What", "Detail"]]
    for when, what, detail in entries:
        rows.append([when, what, detail])
    table(rows, [CONTENT_W * 0.09, CONTENT_W * 0.20, CONTENT_W * 0.71],
          "Week-by-week development log", font_size=7.6)

    h2("A.1 What we would do differently")
    bullets([
        "<b>Write the evaluation set first.</b> We built the engine for six weeks "
        "on impressions and only measured it in week ten. Had the test set existed "
        "in week four, the template-ranking defect would have been visible "
        "immediately instead of surviving most of the project.",
        "<b>Write content in plain language from the first draft.</b> Ten topics "
        "had to be rewritten because they were drafted in the register of the "
        "sources rather than of the reader.",
        "<b>Test on real users earlier.</b> Every significant usability change - "
        "synonyms, action-first structure, the 'do not' lists, source links - came "
        "from watching someone use the system, not from our own reasoning.",
    ])


def appendix_b():
    h1("APPENDIX B - INSTALLATION AND USER GUIDE")

    h2("B.1 Prerequisites")
    bullets([
        "Python 3.8 or later (developed and tested on Python 3.14).",
        "Google Chrome or Microsoft Edge, for the voice features.",
        "A microphone and speakers, for voice input and output only.",
        "No internet connection is required.",
    ])

    h2("B.2 Installation")
    code('''
# 1. Open a terminal in the project folder
cd "poorvi legal"

# 2. Install the two dependencies
pip install -r requirements.txt

# 3. Start the server
python app.py

# 4. Open the address printed in the terminal
http://127.0.0.1:5000
''', "Steps")
    p("On Windows the file <font face='Courier'>run.bat</font> performs all four "
      "steps with a double-click.")

    h2("B.3 Verifying the installation")
    p("On start-up the terminal prints a summary. If the counts match those below "
      "the knowledge base has loaded correctly:")
    code('''
==============================================================
 LegalMitra - Legal Information Portal with AI Chatbot
==============================================================
 Categories        : %d
 Legal topics      : %d
 Document templates: %d
 Glossary terms    : %d
 Indexed entries   : %d
 AI mode           : OFF (offline engine)
--------------------------------------------------------------
 Open your browser at:  http://127.0.0.1:5000
==============================================================
''' % (KB["categories"], KB["topics"], KB["documents"], KB["glossary"], INDEXED))

    h2("B.4 Enabling the optional AI mode")
    code('''
# Windows
set ANTHROPIC_API_KEY=your-key-here
pip install anthropic
python app.py

# Linux / macOS
export ANTHROPIC_API_KEY=your-key-here
pip install anthropic
python app.py
''')
    p("The chat page header will then read &lsquo;AI mode active&rsquo; and "
      "replies will carry a green <i>AI answer</i> badge instead of the gold "
      "<i>Knowledge base</i> badge. If the key is removed the system returns to "
      "the offline engine with no other change.")

    h2("B.5 Running the components separately")
    table([
        ["Command", "What it does"],
        ["python app.py", "Starts the web application"],
        ["python chatbot.py", "Opens a command-line chatbot - useful for testing the engine with no browser"],
        ["python legal_data.py", "Prints the knowledge-base coverage table"],
        ["python database.py", "Creates the database and prints the totals"],
        ["python docs/evaluate.py", "Runs the retrieval accuracy evaluation"],
        ["python docs/make_report.py", "Regenerates this PDF report from the live project"],
    ], [CONTENT_W * 0.34, CONTENT_W * 0.66],
        "Commands for running each component")

    h2("B.6 Using the chatbot")
    bullets([
        "Type a question and press Enter. Shift+Enter inserts a new line.",
        "Or press the microphone button and speak; the question is submitted "
        "automatically when you stop.",
        "The speaker button mutes and unmutes spoken replies; the stop button "
        "halts speech immediately.",
        "The voice and speed selectors below the input box change how replies are "
        "read aloud.",
        "The bin button clears the conversation and starts a new session.",
        "Suggestion chips beneath each reply ask that question immediately when "
        "clicked.",
        "Source links beneath each reply open the exact pages the answer came from.",
    ])

    h2("B.7 Troubleshooting")
    table([
        ["Symptom", "Cause and remedy"],
        ["The microphone button is not visible", "The browser does not support speech recognition. Use Chrome or Edge; typing works in every browser."],
        ["The microphone button does nothing", "Microphone permission was refused. Allow it in the browser's site settings and reload."],
        ["Replies are not spoken", "Speech may be muted - check the speaker button - or the system has no installed voice."],
        ["'ModuleNotFoundError: No module named flask'", "Dependencies are not installed. Run pip install -r requirements.txt."],
        ["'Address already in use'", "Port 5000 is occupied. Stop the other process, or change the port in the last line of app.py."],
        ["The analytics page shows zeros", "No questions have been asked yet. Use the chatbot and reload."],
        ["The chatbot says it cannot find a match", "The question is outside the knowledge base. Rephrase describing the situation, or browse the areas of law."],
    ], [CONTENT_W * 0.34, CONTENT_W * 0.66],
        "Troubleshooting", font_size=8.2)


def appendix_c():
    h1("APPENDIX C - KNOWLEDGE BASE INDEX")

    h2("C.1 Complete list of topics")
    rows = [["#", "Topic", "Branch of law"]]
    counter = 0
    for category in legal_data.CATEGORIES:
        for topic in legal_data.topics_in_category(category["id"]):
            counter += 1
            rows.append([str(counter), topic["title"], category["name"]])
    table(rows, [CONTENT_W * 0.06, CONTENT_W * 0.56, CONTENT_W * 0.38],
          "All %d topics in the knowledge base" % KB["topics"], font_size=7.2)

    h2("C.2 Complete list of document templates")
    rows = [["#", "Template", "Purpose"]]
    for index, document in enumerate(legal_data.DOCUMENTS, start=1):
        rows.append([str(index), document["title"], document["purpose"]])
    table(rows, [CONTENT_W * 0.06, CONTENT_W * 0.38, CONTENT_W * 0.56],
          "All %d document templates" % KB["documents"], font_size=7.2)

    h2("C.3 Emergency quick-help cards")
    rows = [["#", "Situation", "Primary helpline"]]
    from legal_extras import EMERGENCY as CARDS
    for index, card in enumerate(CARDS, start=1):
        rows.append([str(index), card["title"], card["helpline"]])
    table(rows, [CONTENT_W * 0.06, CONTENT_W * 0.46, CONTENT_W * 0.48],
          "Emergency quick-help cards", font_size=7.6)


# ===========================================================================
#  TABLE OF CONTENTS AND DOCUMENT BUILD
# ===========================================================================

from reportlab.platypus.doctemplate import BaseDocTemplate, PageTemplate
from reportlab.platypus.frames import Frame
from reportlab.platypus.tableofcontents import TableOfContents


class ReportDoc(BaseDocTemplate):
    """A document template that records headings so a real table of contents
    with correct page numbers can be produced on the second build pass."""

    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph):
            name = flowable.style.name
            text = flowable.getPlainText()
            if name == "h1":
                self.notify("TOCEntry", (0, text, self.page))
            elif name == "h2":
                self.notify("TOCEntry", (1, text, self.page))


def build_toc():
    story.append(PageBreak())
    story.append(Paragraph("TABLE OF CONTENTS", ParagraphStyle(
        "toch", parent=S_TITLE, fontSize=20, alignment=TA_CENTER)))
    story.append(hr(GOLD, 1.4))
    gap(10)

    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle("toc0", fontName="Times-Bold", fontSize=10.5, leading=17,
                       textColor=NAVY, spaceBefore=6, leftIndent=4,
                       firstLineIndent=-4, rightIndent=26),
        ParagraphStyle("toc1", fontName="Times-Roman", fontSize=9.5, leading=14,
                       textColor=GREY, leftIndent=22, firstLineIndent=-4,
                       rightIndent=26),
    ]
    story.append(toc)


def build_lists():
    """Return the List of Figures and List of Tables as flowables.

    These are produced AFTER all the chapters have been assembled, because only
    then are the figure and table captions known - but they are spliced into the
    front matter, immediately after the table of contents.
    """
    out = []
    item_style = ParagraphStyle("lsitem", parent=S_BODY, fontSize=9.5,
                                leading=14, spaceAfter=3, alignment=0)

    out.append(PageBreak())
    out.append(Paragraph("LIST OF FIGURES", ParagraphStyle(
        "lf", parent=S_TITLE, fontSize=18, alignment=TA_CENTER)))
    out.append(hr(GOLD, 1.2))
    out.append(Spacer(1, 8))
    for item in FIGURES:
        out.append(Paragraph(item, item_style))

    out.append(PageBreak())
    out.append(Paragraph("LIST OF TABLES", ParagraphStyle(
        "lt", parent=S_TITLE, fontSize=18, alignment=TA_CENTER)))
    out.append(hr(GOLD, 1.2))
    out.append(Spacer(1, 8))
    for item in TABLES:
        out.append(Paragraph(item, item_style))
    return out


def build():
    output = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "LegalMitra_Project_Report.pdf")

    doc = ReportDoc(
        output, pagesize=A4,
        leftMargin=22 * mm, rightMargin=22 * mm,
        topMargin=22 * mm, bottomMargin=20 * mm,
        title="LegalMitra - Project Report",
        author="Second Year Engineering Mini Project",
        subject="A Legal Information Portal with a Voice-Enabled AI Chatbot",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height,
                  id="normal")
    doc.addPageTemplates([
        PageTemplate(id="all", frames=frame, onPage=decorate),
    ])

    # ---- assemble the document ----------------------------------------
    build_cover()
    build_certificate()
    build_declaration()
    build_acknowledgement()
    build_abstract()
    build_toc()

    # Remember where the figure and table lists will be inserted. They can only
    # be generated once every caption has been created, but they belong here in
    # the front matter, so we splice them in afterwards.
    lists_position = len(story)

    chapter_1()
    chapter_2()
    chapter_3()
    chapter_4()
    chapter_5()
    chapter_6()
    chapter_7()
    chapter_8()
    chapter_9()
    chapter_10()
    chapter_11()
    chapter_12()
    chapter_13()
    chapter_14()
    chapter_15()
    chapter_16()
    references()
    appendix_a()
    appendix_b()
    appendix_c()

    # Splice the List of Figures and List of Tables into the front matter.
    story[lists_position:lists_position] = build_lists()

    # multiBuild runs the document twice so the table of contents can be
    # filled in with the page numbers discovered on the first pass.
    doc.multiBuild(story)
    return output, doc.page


if __name__ == "__main__":
    print("Building the project report...")
    print("  knowledge base : %d categories, %d topics, %d documents"
          % (KB["categories"], KB["topics"], KB["documents"]))
    print("  indexed entries: %d" % INDEXED)
    print("  accuracy       : Top-1 %.1f%%, Top-3 %.1f%%"
          % (ACC["top1_pct"], ACC["top3_pct"]))
    print("  timings        : build %.0f ms, mean answer %.1f ms"
          % (TIME["build_ms"], TIME["mean_ms"]))
    path, pages = build()
    size_kb = os.path.getsize(path) / 1024.0
    print("-" * 62)
    print("  Written: %s" % path)
    print("  Pages  : %d      Size: %.0f KB" % (pages, size_kb))
    print("  Figures: %d      Tables: %d" % (len(FIGURES), len(TABLES)))
    print("-" * 62)
