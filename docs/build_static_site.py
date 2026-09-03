# -*- coding: utf-8 -*-
"""
docs/build_static_site.py
=========================
Builds a SINGLE self-contained HTML file of the whole LegalMitra site, so the
project can be hosted and shared as one page with no Python server running.

    python docs/build_static_site.py   ->   docs/legalmitra.html

Everything is embedded in that one file:
  * the complete knowledge base, exported from the Python modules as JSON
  * a JavaScript port of the TF-IDF + cosine similarity engine from chatbot.py
  * the same voice interface (Web Speech API)
  * all styling

The Flask application in app.py remains the real project. This file exists so
that the same content can be opened from a URL, on a phone, with nothing
installed - which is how the project is demonstrated outside the lab.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import chatbot
import legal_data
from legal_extras import EMERGENCY, GLOSSARY, HELPLINES


def export_data():
    """Collect the whole knowledge base into one JSON-serialisable dict."""
    return {
        "categories": legal_data.CATEGORIES,
        "topics": legal_data.TOPICS,
        "documents": legal_data.DOCUMENTS,
        "glossary": GLOSSARY,
        "emergency": EMERGENCY,
        "helplines": HELPLINES,
        "synonyms": chatbot.SYNONYMS,
        "stopwords": sorted(chatbot.STOPWORDS),
        "suffixes": chatbot.SUFFIXES,
        "templateHints": list(chatbot.TEMPLATE_HINTS),
        "stats": legal_data.stats(),
    }


HTML = r"""<title>LegalMitra</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,400;0,600;0,700;1,400&family=Public+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap">

<style>
/* ===================================================================
   LegalMitra - design tokens
   Palette grounded in Indian court stationery: slate ink, laid paper,
   the oxblood of a seal and red tape, and muted brass from the scales.
   =================================================================== */
:root {
  --paper:      #f4f2ed;
  --surface:    #fbfaf7;
  --surface-2:  #ecebe4;
  --ink:        #1a2029;
  --ink-2:      #4a5260;
  --ink-3:      #757d8b;
  --rule:       #d9d5cb;
  --rule-soft:  #e6e3da;
  --seal:       #8c2f27;
  --seal-soft:  #f3e3e0;
  --brass:      #9a7524;
  --brass-soft: #f2ead4;
  --verdict:    #2c6149;
  --verdict-soft:#e2eee8;
  --shadow:     0 1px 2px rgba(26,32,41,.06), 0 8px 24px rgba(26,32,41,.07);
  --shadow-lg:  0 2px 6px rgba(26,32,41,.08), 0 20px 48px rgba(26,32,41,.14);

  --display: "Spectral", Georgia, "Times New Roman", serif;
  --body:    "Public Sans", "Segoe UI", system-ui, -apple-system, sans-serif;
  --mono:    "IBM Plex Mono", "Consolas", "Courier New", monospace;

  --wrap: 1180px;
  --r: 8px;
  --r-lg: 14px;
}

@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --paper:      #12161c;
    --surface:    #191e26;
    --surface-2:  #222833;
    --ink:        #e8e6e0;
    --ink-2:      #b3b8c2;
    --ink-3:      #858c99;
    --rule:       #2e3540;
    --rule-soft:  #242b35;
    --seal:       #d98b80;
    --seal-soft:  #2e1f1d;
    --brass:      #d6b169;
    --brass-soft: #2b2519;
    --verdict:    #7fc0a3;
    --verdict-soft:#1a2b24;
    --shadow:     0 1px 2px rgba(0,0,0,.4), 0 8px 24px rgba(0,0,0,.36);
    --shadow-lg:  0 2px 6px rgba(0,0,0,.45), 0 20px 48px rgba(0,0,0,.5);
  }
}

:root[data-theme="dark"] {
  --paper:      #12161c;
  --surface:    #191e26;
  --surface-2:  #222833;
  --ink:        #e8e6e0;
  --ink-2:      #b3b8c2;
  --ink-3:      #858c99;
  --rule:       #2e3540;
  --rule-soft:  #242b35;
  --seal:       #d98b80;
  --seal-soft:  #2e1f1d;
  --brass:      #d6b169;
  --brass-soft: #2b2519;
  --verdict:    #7fc0a3;
  --verdict-soft:#1a2b24;
  --shadow:     0 1px 2px rgba(0,0,0,.4), 0 8px 24px rgba(0,0,0,.36);
  --shadow-lg:  0 2px 6px rgba(0,0,0,.45), 0 20px 48px rgba(0,0,0,.5);
}

* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--paper);
  color: var(--ink);
  font-family: var(--body);
  font-size: 16px;
  line-height: 1.62;
  -webkit-font-smoothing: antialiased;
}
h1, h2, h3, h4 { font-family: var(--display); line-height: 1.2; text-wrap: balance; margin: 0; font-weight: 600; }
p { margin: 0 0 .85rem; }
a { color: inherit; }
button { font-family: inherit; }
:focus-visible { outline: 2px solid var(--brass); outline-offset: 2px; border-radius: 3px; }

.wrap { max-width: var(--wrap); margin: 0 auto; padding: 0 22px; }
.mono { font-family: var(--mono); }
.muted { color: var(--ink-2); }
.tnum { font-variant-numeric: tabular-nums; }

/* ---------- disclaimer ribbon ---------- */
.ribbon {
  background: var(--seal);
  color: #fff;
  font-size: .74rem;
  letter-spacing: .06em;
  text-transform: uppercase;
  text-align: center;
  padding: 6px 14px;
  font-weight: 600;
}
:root[data-theme="dark"] .ribbon,
:root:not([data-theme="light"]) .ribbon { color: #12161c; }
@media (prefers-color-scheme: light) { :root:not([data-theme="dark"]) .ribbon { color: #fff; } }

/* ---------- header ---------- */
header.site {
  position: sticky; top: 0; z-index: 60;
  background: var(--surface);
  border-bottom: 1px solid var(--rule);
}
.bar { display: flex; align-items: center; gap: 18px; padding: 12px 0; }
.brand { display: flex; align-items: center; gap: 11px; text-decoration: none; cursor: pointer; }
.brand svg { width: 30px; height: 30px; flex: none; }
.brand b { font-family: var(--display); font-size: 1.24rem; letter-spacing: -.01em; display: block; line-height: 1; }
.brand span { font-size: .68rem; color: var(--ink-3); letter-spacing: .1em; text-transform: uppercase; }

.omni { flex: 1; max-width: 460px; margin-left: auto; position: relative; }
.omni input {
  width: 100%; padding: 9px 13px 9px 34px;
  border: 1px solid var(--rule); border-radius: var(--r);
  background: var(--paper); color: var(--ink);
  font: inherit; font-size: .9rem;
}
.omni input::placeholder { color: var(--ink-3); }
.omni svg { position: absolute; left: 10px; top: 50%; transform: translateY(-50%); width: 15px; height: 15px; color: var(--ink-3); }

.iconbtn {
  width: 36px; height: 36px; flex: none;
  border: 1px solid var(--rule); border-radius: var(--r);
  background: var(--paper); color: var(--ink-2);
  cursor: pointer; display: grid; place-items: center; padding: 0;
}
.iconbtn:hover { border-color: var(--brass); color: var(--ink); }
.iconbtn svg { width: 16px; height: 16px; }

nav.tabs { border-top: 1px solid var(--rule-soft); overflow-x: auto; }
nav.tabs ul { display: flex; list-style: none; margin: 0; padding: 0; gap: 2px; }
nav.tabs button {
  border: none; background: none; cursor: pointer;
  padding: 11px 14px; font-size: .86rem; font-weight: 500;
  color: var(--ink-2); border-bottom: 2px solid transparent; white-space: nowrap;
}
nav.tabs button:hover { color: var(--ink); }
nav.tabs button[aria-current="true"] { color: var(--ink); border-bottom-color: var(--seal); font-weight: 600; }

/* ---------- generic blocks ---------- */
main { min-height: 70vh; padding: 30px 0 60px; }
.eyebrow {
  font-family: var(--mono); font-size: .7rem; letter-spacing: .14em;
  text-transform: uppercase; color: var(--ink-3); margin-bottom: 7px;
}
.head { margin-bottom: 22px; }
.head h1 { font-size: clamp(1.7rem, 3.4vw, 2.35rem); margin-bottom: 6px; }
.head h2 { font-size: 1.42rem; margin-bottom: 6px; }
.head p { color: var(--ink-2); max-width: 68ch; margin: 0; }

.grid { display: grid; gap: 14px; }
.g2 { grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); }
.g3 { grid-template-columns: repeat(auto-fill, minmax(268px, 1fr)); }
.g4 { grid-template-columns: repeat(auto-fill, minmax(212px, 1fr)); }

.card {
  background: var(--surface); border: 1px solid var(--rule);
  border-radius: var(--r-lg); padding: 17px 18px;
  display: flex; flex-direction: column; gap: 7px;
  text-align: left; font: inherit; color: inherit;
  cursor: pointer; transition: border-color .15s, transform .15s, box-shadow .15s;
}
.card:hover { border-color: var(--brass); transform: translateY(-2px); box-shadow: var(--shadow); }
.card h3 { font-size: 1.02rem; }
.card p { font-size: .875rem; color: var(--ink-2); margin: 0; flex: 1; }
.card .foot { display: flex; gap: 8px; align-items: center; flex-wrap: wrap; padding-top: 9px; border-top: 1px solid var(--rule-soft); margin-top: 3px; }
.card.static { cursor: default; }
.card.static:hover { border-color: var(--rule); transform: none; box-shadow: none; }

.tag {
  font-family: var(--mono); font-size: .67rem; letter-spacing: .07em;
  text-transform: uppercase; padding: 3px 8px; border-radius: 999px;
  background: var(--surface-2); color: var(--ink-2); white-space: nowrap;
}
.tag.seal { background: var(--seal-soft); color: var(--seal); }
.tag.brass { background: var(--brass-soft); color: var(--brass); }
.tag.verdict { background: var(--verdict-soft); color: var(--verdict); }

.btn {
  display: inline-flex; align-items: center; gap: 7px; justify-content: center;
  padding: 10px 17px; border-radius: var(--r); cursor: pointer;
  border: 1px solid var(--ink); background: var(--ink); color: var(--paper);
  font: inherit; font-size: .88rem; font-weight: 600; text-decoration: none;
}
.btn:hover { opacity: .88; }
.btn.ghost { background: transparent; color: var(--ink); border-color: var(--rule); }
.btn.ghost:hover { border-color: var(--ink); opacity: 1; }
.btn.seal { background: var(--seal); border-color: var(--seal); color: #fff; }
.btn.sm { padding: 6px 12px; font-size: .8rem; }
.row { display: flex; gap: 10px; flex-wrap: wrap; }

/* ---------- home ---------- */
.hero { border-bottom: 1px solid var(--rule); padding-bottom: 26px; margin-bottom: 30px; }
.hero h1 { font-size: clamp(2rem, 5vw, 3.05rem); letter-spacing: -.015em; margin-bottom: 12px; }
.hero h1 em { font-style: italic; color: var(--seal); }
.hero .lede { font-size: 1.06rem; color: var(--ink-2); max-width: 60ch; margin-bottom: 20px; }
.askbox { display: flex; gap: 9px; max-width: 640px; margin-bottom: 14px; flex-wrap: wrap; }
.askbox input {
  flex: 1; min-width: 240px; padding: 13px 15px; font: inherit; font-size: .96rem;
  border: 1px solid var(--rule); border-radius: var(--r);
  background: var(--surface); color: var(--ink);
}
.figures { display: flex; flex-wrap: wrap; gap: 26px; margin-top: 24px; }
.figures div b { font-family: var(--display); font-size: 1.72rem; display: block; line-height: 1; }
.figures div span { font-family: var(--mono); font-size: .68rem; letter-spacing: .11em; text-transform: uppercase; color: var(--ink-3); }

/* ---------- article ---------- */
.layout { display: grid; grid-template-columns: minmax(0,1fr) 282px; gap: 30px; align-items: start; }
article {
  background: var(--surface); border: 1px solid var(--rule);
  border-radius: var(--r-lg); padding: 30px 32px;
}
article h2 {
  font-size: 1.22rem; margin: 28px 0 11px; padding-bottom: 6px;
  border-bottom: 2px solid var(--brass); display: inline-block;
}
article h2:first-child { margin-top: 0; }
article ul, article ol { padding-left: 1.2rem; margin: 0 0 14px; }
article li { margin-bottom: .45rem; }

.pull {
  background: var(--surface-2); border-left: 3px solid var(--ink);
  padding: 15px 18px; border-radius: 0 var(--r) var(--r) 0;
  margin-bottom: 22px; font-size: 1.02rem;
}
ol.steps { list-style: none; padding: 0; counter-reset: s; }
ol.steps li { counter-increment: s; position-relative; position: relative; padding-left: 40px; margin-bottom: 11px; }
ol.steps li::before {
  content: counter(s, decimal-leading-zero);
  position: absolute; left: 0; top: 1px;
  font-family: var(--mono); font-size: .74rem; font-weight: 500;
  color: var(--seal); background: var(--seal-soft);
  padding: 2px 6px; border-radius: 4px;
}
ul.laws { list-style: none; padding: 0; }
ul.laws li {
  border-left: 3px solid var(--brass); background: var(--brass-soft);
  padding: 9px 13px; border-radius: 0 var(--r) var(--r) 0;
  margin-bottom: 7px; font-size: .89rem;
}
details.faq { border: 1px solid var(--rule); border-radius: var(--r); margin-bottom: 8px; background: var(--paper); }
details.faq summary { padding: 12px 15px; cursor: pointer; font-weight: 600; font-size: .93rem; list-style: none; }
details.faq summary::-webkit-details-marker { display: none; }
details.faq summary::before { content: "+ "; color: var(--brass); font-family: var(--mono); }
details.faq[open] summary::before { content: "\2212 "; }
details.faq .body { padding: 0 15px 14px; color: var(--ink-2); font-size: .92rem; }

aside { position: sticky; top: 112px; display: grid; gap: 14px; }
.panel { background: var(--surface); border: 1px solid var(--rule); border-radius: var(--r-lg); padding: 16px 17px; }
.panel h4 {
  font-family: var(--mono); font-size: .68rem; letter-spacing: .12em;
  text-transform: uppercase; color: var(--ink-3); margin-bottom: 10px; font-weight: 500;
}
.panel ul { list-style: none; padding: 0; margin: 0; display: grid; gap: 8px; font-size: .88rem; }
.panel a { color: var(--ink); text-decoration: none; border-bottom: 1px solid var(--rule); }
.panel a:hover { border-color: var(--brass); color: var(--seal); }
.panel.dark { background: var(--ink); border-color: var(--ink); }
.panel.dark h4, .panel.dark p { color: rgba(255,255,255,.66); }
:root[data-theme="dark"] .panel.dark, :root:not([data-theme="light"]) .panel.dark { background: var(--surface-2); border-color: var(--rule); }
.panel.dark p { font-size: .87rem; margin-bottom: 12px; }
.panel.dark .btn { width: 100%; }

.note { padding: 13px 16px; border-radius: var(--r); font-size: .89rem; margin-bottom: 18px; border: 1px solid; }
.note.warn { background: var(--brass-soft); border-color: var(--brass); color: var(--ink); }
.note.info { background: var(--surface-2); border-color: var(--rule); color: var(--ink); }
.note.danger { background: var(--seal-soft); border-color: var(--seal); color: var(--ink); }

/* ---------- template viewer ---------- */
.toolbar {
  display: flex; gap: 8px; align-items: center; flex-wrap: wrap;
  background: var(--ink); padding: 10px 13px; border-radius: var(--r) var(--r) 0 0;
}
:root[data-theme="dark"] .toolbar, :root:not([data-theme="light"]) .toolbar { background: var(--surface-2); }
.toolbar .name { font-family: var(--mono); font-size: .7rem; letter-spacing: .1em; text-transform: uppercase; color: rgba(255,255,255,.6); margin-right: auto; }
:root[data-theme="dark"] .toolbar .name, :root:not([data-theme="light"]) .toolbar .name { color: var(--ink-3); }
pre.tpl {
  background: var(--paper); border: 1px solid var(--rule); border-top: none;
  border-radius: 0 0 var(--r) var(--r); padding: 22px;
  font-family: var(--mono); font-size: .77rem; line-height: 1.7;
  white-space: pre-wrap; word-wrap: break-word; overflow-x: auto;
  max-height: 640px; overflow-y: auto; margin: 0; color: var(--ink);
}
pre.tpl mark { background: var(--brass-soft); color: var(--brass); font-weight: 500; padding: 0 2px; border-radius: 3px; }

/* ---------- chat ---------- */
.chat {
  display: flex; flex-direction: column; height: min(72vh, 660px);
  background: var(--surface); border: 1px solid var(--rule);
  border-radius: var(--r-lg); overflow: hidden; box-shadow: var(--shadow);
}
.chat-top { display: flex; align-items: center; gap: 11px; padding: 12px 16px; border-bottom: 1px solid var(--rule); background: var(--surface-2); }
.chat-top .who b { display: block; font-family: var(--display); font-size: 1rem; }
.chat-top .who span { font-size: .74rem; color: var(--verdict); display: flex; align-items: center; gap: 5px; }
.dot { width: 6px; height: 6px; border-radius: 50%; background: var(--verdict); }
.chat-top .acts { margin-left: auto; display: flex; gap: 6px; }
.chat-log { flex: 1; overflow-y: auto; padding: 18px; display: flex; flex-direction: column; gap: 14px; }

.msg { display: flex; gap: 10px; align-items: flex-start; }
.msg .av { width: 28px; height: 28px; border-radius: 7px; flex: none; display: grid; place-items: center; font-size: .74rem; font-weight: 700; font-family: var(--mono); }
.msg.bot .av { background: var(--ink); color: var(--paper); }
:root[data-theme="dark"] .msg.bot .av, :root:not([data-theme="light"]) .msg.bot .av { background: var(--brass); color: #12161c; }
.msg.me { flex-direction: row-reverse; }
.msg.me .av { background: var(--seal); color: #fff; }
.bubble {
  max-width: 78%; padding: 12px 15px; border-radius: 11px;
  background: var(--paper); border: 1px solid var(--rule);
  font-size: .91rem; white-space: pre-wrap; word-wrap: break-word; line-height: 1.6;
}
.msg.me .bubble { background: var(--ink); color: var(--paper); border-color: var(--ink); }
:root[data-theme="dark"] .msg.me .bubble, :root:not([data-theme="light"]) .msg.me .bubble { background: var(--surface-2); color: var(--ink); border-color: var(--rule); }
.bubble .hl { display: block; font-family: var(--display); font-weight: 700; color: var(--seal); margin: 9px 0 3px; font-size: .95rem; }
.bubble .hl:first-child { margin-top: 0; }
.bubble .src { margin-top: 10px; padding-top: 8px; border-top: 1px dashed var(--rule); display: flex; gap: 6px; flex-wrap: wrap; align-items: center; font-size: .74rem; }
.bubble .src button { border: 1px solid var(--rule); background: var(--surface); color: var(--ink); border-radius: 999px; padding: 3px 9px; font-size: .74rem; cursor: pointer; }
.bubble .src button:hover { border-color: var(--brass); color: var(--seal); }
.chips { display: flex; gap: 7px; flex-wrap: wrap; padding-left: 38px; }
.chip { border: 1px solid var(--rule); background: var(--surface); color: var(--ink); border-radius: 999px; padding: 5px 12px; font-size: .8rem; cursor: pointer; }
.chip:hover { border-color: var(--seal); color: var(--seal); }
.typing { display: flex; gap: 4px; padding: 4px 2px; }
.typing i { width: 6px; height: 6px; border-radius: 50%; background: var(--ink-3); animation: bl 1.2s infinite; }
.typing i:nth-child(2) { animation-delay: .18s; }
.typing i:nth-child(3) { animation-delay: .36s; }
@keyframes bl { 0%,60%,100% { opacity: .25; } 30% { opacity: 1; } }

.chat-in { border-top: 1px solid var(--rule); padding: 12px 14px; background: var(--surface); }
.chat-in .line { display: flex; gap: 9px; align-items: flex-end; }
.chat-in textarea {
  flex: 1; resize: none; max-height: 120px; padding: 11px 13px;
  border: 1px solid var(--rule); border-radius: var(--r);
  background: var(--paper); color: var(--ink); font: inherit; font-size: .92rem; line-height: 1.5;
}
.round { width: 42px; height: 42px; border-radius: 50%; border: 1px solid var(--rule); background: var(--paper); color: var(--ink); cursor: pointer; display: grid; place-items: center; flex: none; padding: 0; }
.round svg { width: 17px; height: 17px; }
.round:hover { border-color: var(--ink); }
.round.send { background: var(--ink); color: var(--paper); border-color: var(--ink); }
:root[data-theme="dark"] .round.send, :root:not([data-theme="light"]) .round.send { background: var(--brass); color: #12161c; border-color: var(--brass); }
.round.live { background: var(--seal); border-color: var(--seal); color: #fff; animation: pulse 1.3s infinite; }
@keyframes pulse { 0% { box-shadow: 0 0 0 0 rgba(140,47,39,.5); } 70% { box-shadow: 0 0 0 12px rgba(140,47,39,0); } 100% { box-shadow: 0 0 0 0 rgba(140,47,39,0); } }
.voicebar { display: flex; gap: 14px; flex-wrap: wrap; align-items: center; margin-top: 8px; font-size: .74rem; color: var(--ink-3); }
.voicebar select { font: inherit; font-size: .74rem; padding: 2px 5px; border: 1px solid var(--rule); border-radius: 5px; background: var(--paper); color: var(--ink); max-width: 170px; }

/* ---------- glossary / emergency / tables ---------- */
.az { display: flex; flex-wrap: wrap; gap: 5px; margin-bottom: 18px; }
.az button { width: 32px; height: 32px; border: 1px solid var(--rule); background: var(--surface); color: var(--ink); border-radius: 6px; cursor: pointer; font-size: .8rem; font-weight: 600; padding: 0; }
.az button:hover, .az button[aria-pressed="true"] { background: var(--ink); color: var(--paper); border-color: var(--ink); }
.term { background: var(--surface); border: 1px solid var(--rule); border-radius: var(--r); padding: 13px 16px; margin-bottom: 8px; }
.term b { font-family: var(--display); font-size: 1.02rem; }
.term p { margin: 2px 0 0; color: var(--ink-2); font-size: .89rem; }

.sos { background: var(--surface); border: 1px solid var(--rule); border-top: 3px solid var(--seal); border-radius: var(--r-lg); padding: 19px; }
.sos h3 { font-size: 1.06rem; margin-bottom: 11px; }
ul.do, ul.dont { list-style: none; padding: 0; margin: 0 0 12px; }
ul.do li, ul.dont li { position: relative; padding-left: 22px; font-size: .88rem; margin-bottom: 6px; }
ul.do li::before { content: "\2713"; position: absolute; left: 0; color: var(--verdict); font-weight: 700; }
ul.dont li::before { content: "\2717"; position: absolute; left: 0; color: var(--seal); font-weight: 700; }
.hl-card { background: var(--surface); border: 1px solid var(--rule); border-radius: var(--r); padding: 15px; text-align: center; }
.hl-card b { font-family: var(--display); font-size: 1.45rem; color: var(--seal); display: block; }
.hl-card span { font-size: .8rem; color: var(--ink-2); }

.result { background: var(--surface); border: 1px solid var(--rule); border-radius: var(--r); padding: 15px 17px; margin-bottom: 9px; cursor: pointer; text-align: left; width: 100%; font: inherit; color: inherit; display: block; }
.result:hover { border-color: var(--brass); }
.result h3 { font-size: 1rem; margin-bottom: 3px; }
.result p { font-size: .86rem; color: var(--ink-2); margin: 0 0 7px; }
.meter { height: 4px; width: 76px; background: var(--rule); border-radius: 999px; overflow: hidden; display: inline-block; vertical-align: middle; }
.meter i { display: block; height: 100%; background: var(--brass); }

table.data { width: 100%; border-collapse: collapse; font-size: .86rem; background: var(--surface); border: 1px solid var(--rule); border-radius: var(--r); overflow: hidden; }
table.data th { background: var(--ink); color: var(--paper); text-align: left; padding: 10px 13px; font-size: .78rem; font-weight: 600; }
:root[data-theme="dark"] table.data th, :root:not([data-theme="light"]) table.data th { background: var(--surface-2); color: var(--ink); }
table.data td { padding: 9px 13px; border-top: 1px solid var(--rule-soft); }

.scroll-x { overflow-x: auto; }

footer.site { border-top: 1px solid var(--rule); background: var(--surface); padding: 28px 0; margin-top: 40px; font-size: .85rem; color: var(--ink-2); }
footer.site .cols { display: grid; grid-template-columns: 1.7fr 1fr 1.3fr; gap: 28px; }
footer.site h4 { font-family: var(--mono); font-size: .67rem; letter-spacing: .12em; text-transform: uppercase; color: var(--ink-3); margin-bottom: 9px; font-weight: 500; }
footer.site ul { list-style: none; padding: 0; margin: 0; display: grid; gap: 6px; }
footer.site button { background: none; border: none; padding: 0; color: var(--ink-2); cursor: pointer; font: inherit; text-align: left; }
footer.site button:hover { color: var(--seal); }
.hlrow { display: flex; justify-content: space-between; gap: 10px; }
.hlrow b { font-family: var(--mono); color: var(--seal); }

@media (max-width: 900px) {
  .layout { grid-template-columns: 1fr; }
  aside { position: static; }
  footer.site .cols { grid-template-columns: 1fr; }
}
@media (max-width: 640px) {
  .bar { flex-wrap: wrap; }
  .omni { order: 3; max-width: 100%; width: 100%; margin-left: 0; }
  article { padding: 20px; }
  .bubble { max-width: 88%; }
  .figures { gap: 18px; }
}
@media (prefers-reduced-motion: reduce) {
  * { animation: none !important; transition: none !important; }
}
</style>

<div class="ribbon">Academic project &mdash; legal information for learning, not legal advice</div>

<header class="site">
  <div class="wrap bar">
    <a class="brand" onclick="go('home')" tabindex="0" role="button">
      <svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round">
        <path d="M16 5v22M9 27h14M16 8l-8 2M16 8l8 2"/>
        <path d="M8 10l-4 8h8zM24 10l-4 8h8z" fill="none"/>
      </svg>
      <span><b>LegalMitra</b><span>Every law, explained</span></span>
    </a>
    <div class="omni">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>
      <input id="omni" type="search" placeholder="Search a law, a right, or your problem&hellip;" aria-label="Search">
    </div>
    <button class="iconbtn" id="themeBtn" title="Switch theme" aria-label="Switch theme">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="4.5"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M19.1 4.9l-1.4 1.4M6.3 17.7l-1.4 1.4"/></svg>
    </button>
  </div>
  <nav class="tabs"><div class="wrap"><ul id="tabs"></ul></div></nav>
</header>

<main><div class="wrap" id="view"></div></main>

<footer class="site"><div class="wrap cols">
  <div>
    <h4>LegalMitra</h4>
    <p>A student-built legal information portal covering <span id="fCat"></span> branches of law, with <span id="fTop"></span> explained topics, <span id="fDoc"></span> document templates and a talking assistant.</p>
    <p class="muted">Built with Python, Flask, SQLite, HTML, CSS and JavaScript as a second-year engineering mini project. This page is the self-contained version of that project.</p>
  </div>
  <div>
    <h4>Explore</h4>
    <ul>
      <li><button onclick="go('areas')">Areas of law</button></li>
      <li><button onclick="go('docs')">Document templates</button></li>
      <li><button onclick="go('chat')">Ask the assistant</button></li>
      <li><button onclick="go('glossary')">A&ndash;Z glossary</button></li>
      <li><button onclick="go('sos')">Emergency help</button></li>
      <li><button onclick="go('about')">About the project</button></li>
    </ul>
  </div>
  <div>
    <h4>Emergency numbers</h4>
    <ul id="fHelp"></ul>
  </div>
</div></footer>

<script>
/* =====================================================================
   LegalMitra - single page application
   A JavaScript port of the Python engine in chatbot.py, over the same
   knowledge base exported from the Python modules.
   ===================================================================== */
const DB = __DATA__;

/* ---------------------------------------------------------------
   1. SMALL HELPERS
   These are declared FIRST because the search engine below is built
   immediately at load time and calls catName().
   --------------------------------------------------------------- */
const esc = s => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
const catOf = id => DB.categories.find(c => c.id === id);
const catName = id => { const c = catOf(id); return c ? c.name : id; };
const topicOf = id => DB.topics.find(t => t.id === id);
const docOf = id => DB.documents.find(d => d.id === id);
const topicsIn = id => DB.topics.filter(t => t.category === id);
const docsIn = id => DB.documents.filter(d => d.category === id);
const view = () => document.getElementById("view");

/* ---------------------------------------------------------------
   2. THE SEARCH ENGINE  (port of chatbot.py)
   --------------------------------------------------------------- */
const STOP = new Set(DB.stopwords);
const SUFFIXES = DB.suffixes;
const TOKEN_RE = /[a-z0-9]+/g;

function stem(w) {
  for (const s of SUFFIXES) {
    if (w.endsWith(s) && w.length - s.length >= 4) return w.slice(0, -s.length);
  }
  return w;
}
function tokenize(text) {
  const out = [];
  const m = String(text).toLowerCase().match(TOKEN_RE) || [];
  for (const w of m) if (!STOP.has(w) && w.length > 1) out.push(stem(w));
  return out;
}
function expandQuery(text) {
  const low = text.toLowerCase(), extra = [];
  for (const [word, rep] of Object.entries(DB.synonyms)) {
    if (new RegExp("\\b" + word.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + "\\b").test(low)) extra.push(rep);
  }
  return extra.length ? text + " " + extra.join(" ") : text;
}

function topicText(t) {
  const parts = [t.title, t.title, t.title,
    (t.keywords || []).join(" "), (t.keywords || []).join(" "), (t.keywords || []).join(" "),
    catName(t.category), t.summary, (t.key_points || []).join(" "),
    (t.laws || []).join(" "), (t.steps || []).join(" ")];
  for (const f of (t.faqs || [])) { parts.push(f.q, f.q, f.a); }
  return parts.join(" ");
}
function docText(d) {
  return [d.title, d.title, d.title,
    (d.keywords || []).join(" "), (d.keywords || []).join(" "), (d.keywords || []).join(" "),
    "document template format draft sample agreement", catName(d.category),
    d.purpose, d.when_to_use, (d.checklist || []).join(" ")].join(" ");
}

const ENGINE = (function build() {
  const entries = [];
  DB.topics.forEach(t => entries.push({ kind: "topic", id: t.id, title: t.title, category: t.category, obj: t, text: topicText(t) }));
  DB.documents.forEach(d => entries.push({ kind: "document", id: d.id, title: d.title, category: d.category, obj: d, text: docText(d) }));

  const tokenLists = entries.map(e => tokenize(e.text));
  const N = entries.length;

  const df = new Map();
  tokenLists.forEach(toks => { for (const w of new Set(toks)) df.set(w, (df.get(w) || 0) + 1); });

  const idf = new Map();
  for (const [w, c] of df) idf.set(w, Math.log(N / (1 + c)) + 1);

  function vectorise(tokens) {
    if (!tokens.length) return null;
    const counts = new Map();
    for (const w of tokens) counts.set(w, (counts.get(w) || 0) + 1);
    const total = tokens.length, v = new Map();
    for (const [w, c] of counts) {
      const weight = idf.get(w);
      if (weight === undefined) continue;
      v.set(w, (c / total) * weight);
    }
    let len = 0; for (const x of v.values()) len += x * x;
    len = Math.sqrt(len);
    if (!len) return null;
    for (const [w, x] of v) v.set(w, x / len);
    return v;
  }

  const vectors = tokenLists.map(vectorise);

  function search(query, limit) {
    limit = limit || 5;
    const qv = vectorise(tokenize(expandQuery(query)));
    if (!qv) return [];
    const low = query.toLowerCase();
    const wantsTpl = DB.templateHints.some(h => low.includes(h));
    const out = [];
    for (let i = 0; i < entries.length; i++) {
      const v = vectors[i];
      if (!v) continue;
      let score = 0;
      const small = qv.size < v.size ? qv : v, big = qv.size < v.size ? v : qv;
      for (const [w, x] of small) { const y = big.get(w); if (y !== undefined) score += x * y; }
      for (const k of (entries[i].obj.keywords || [])) if (low.includes(k)) score += 0.05;
      if (entries[i].kind === "document") score *= wantsTpl ? 1.25 : 0.72;
      if (score > 0) out.push({ score: score, entry: entries[i] });
    }
    out.sort((a, b) => b.score - a.score);
    return out.slice(0, limit);
  }
  return { search: search, size: entries.length, idf: idf };
})();

/* ---------------------------------------------------------------
   3. INTENT AND ANSWER COMPOSITION
   --------------------------------------------------------------- */
const GREET = new Set(["hi","hello","hey","namaste","hii","hlo","greetings","yo","hola"]);
const THANKS = new Set(["thanks","thank","thankyou","thx","shukriya","dhanyavad"]);
const BYE = new Set(["bye","goodbye","exit","quit","see"]);
const SOS_WORDS = ["urgent","emergency","immediately","right now","arrested","arrest","help me","danger","threatening","beaten","kidnap"];
const DOC_WORDS = ["template","format","draft","sample","specimen","download","how to write","how do i write"];
const DISCLAIMER = "This is general legal information for learning, not legal advice. For your own matter please consult a qualified advocate.";

function detectIntent(msg) {
  const t = msg.toLowerCase().trim();
  const words = new Set(t.match(TOKEN_RE) || []);
  if (!t) return "empty";
  const inter = [...words].filter(w => GREET.has(w));
  if (inter.length && words.size <= 3) return "greeting";
  if ([...words].some(w => THANKS.has(w))) return "thanks";
  if ([...words].some(w => BYE.has(w)) && words.size <= 3) return "bye";
  if (SOS_WORDS.some(p => t.includes(p))) return "emergency";
  if (DOC_WORDS.some(p => t.includes(p))) return "document";
  if (/^(what is|what are|meaning of|define)/.test(t)) return "definition";
  return "question";
}
function findGlossary(msg) {
  const t = msg.toLowerCase(); let best = null;
  for (const g of DB.glossary) {
    const term = g.term.toLowerCase();
    if (new RegExp("\\b" + term.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + "\\b").test(t)) {
      if (!best || term.length > best.term.length) best = g;
    }
  }
  return best;
}
function findSos(msg) {
  const qt = new Set(tokenize(msg)); let best = null, bs = 0;
  for (const c of DB.emergency) {
    let s = 0; for (const w of tokenize(c.title)) if (qt.has(w)) s++;
    if (s > bs) { bs = s; best = c; }
  }
  return best;
}
const bul = (arr, n) => (n ? arr.slice(0, n) : arr).map(x => "  - " + x).join("\n");

function topicAnswer(t) {
  const L = [t.title.toUpperCase(), "Area of law: " + catName(t.category), "", t.summary];
  if (t.key_points && t.key_points.length) L.push("", "KEY POINTS", bul(t.key_points, 5));
  if (t.steps && t.steps.length) L.push("", "WHAT YOU SHOULD DO", t.steps.slice(0, 5).map((s, i) => "  " + (i + 1) + ". " + s).join("\n"));
  if (t.laws && t.laws.length) L.push("", "LAW THAT APPLIES", bul(t.laws, 4));
  if (t.faqs && t.faqs.length) L.push("", "COMMONLY ASKED", "  Q. " + t.faqs[0].q, "  A. " + t.faqs[0].a);
  return L.join("\n");
}
function docAnswer(d) {
  return [d.title.toUpperCase(), "Area of law: " + catName(d.category), "", d.purpose, "",
    "WHEN TO USE IT", "  " + d.when_to_use, "", "KEEP THIS READY BEFORE DRAFTING", bul(d.checklist, 5),
    "", "STAMP DUTY / REGISTRATION", "  " + d.stamp, "",
    "Open the template page to copy, print or download the full draft."].join("\n");
}
function sosAnswer(c) {
  return ["URGENT: " + c.title.toUpperCase(), "", "DO THIS NOW",
    c.immediate.map((s, i) => "  " + (i + 1) + ". " + s).join("\n"), "",
    "DO NOT", bul(c.do_not), "", "HELPLINE: " + c.helpline].join("\n");
}
function suggestFor(entry) {
  if (!entry) return ["What are my fundamental rights?", "How do I file an FIR?", "Give me a rent agreement format", "What is a cheque bounce case?"];
  const o = entry.obj, out = [];
  if (entry.kind === "topic") {
    (o.faqs || []).slice(0, 2).forEach(f => out.push(f.q));
    DB.topics.filter(t => t.category === o.category && t.id !== o.id).slice(0, 2).forEach(t => out.push(t.title));
  } else {
    out.push("What law applies to " + o.title + "?");
    DB.documents.filter(d => d.category === o.category && d.id !== o.id).slice(0, 2).forEach(d => out.push(d.title + " format"));
  }
  return out.slice(0, 4);
}

function answer(message) {
  const msg = (message || "").trim();
  const intent = detectIntent(msg);
  const base = { intent: intent, sources: [], suggestions: suggestFor(null), confidence: 0 };

  if (intent === "empty") return Object.assign(base, { answer: "Please type a question and I will do my best to help." });
  if (intent === "greeting") return Object.assign(base, { answer:
    "Namaste! I am LegalMitra, your legal information assistant.\n\nI can explain any area of law – from criminal and property to company, cyber, consumer, labour, tax and international law – and I can give you ready-to-use document formats.\n\nTry asking me:\n  - What are my rights if I am arrested?\n  - My landlord is not returning my deposit\n  - How do I register a trademark?\n  - Give me a rent agreement format", confidence: 1 });
  if (intent === "thanks") return Object.assign(base, { answer: "You are welcome. Ask me anything else about the law – I am here to help.\n\n" + DISCLAIMER, confidence: 1 });
  if (intent === "bye") return Object.assign(base, { answer: "Goodbye, and all the best. Remember: keep your documents safe, put agreements in writing, and never miss a legal deadline.", suggestions: [], confidence: 1 });

  if (intent === "emergency") {
    const card = findSos(msg);
    if (card) {
      const topic = DB.topics.find(t => t.id === card.topic);
      return { answer: sosAnswer(card) + "\n\n" + DISCLAIMER, intent: intent, confidence: 1,
        sources: topic ? [{ kind: "topic", id: topic.id, title: topic.title }] : [],
        suggestions: ["Explain " + (topic ? topic.title : "my rights"), "What are the national helpline numbers?"] };
    }
  }
  if (intent === "definition") {
    const term = findGlossary(msg);
    if (term) {
      const r = ENGINE.search(term.term, 3);
      let body = term.term.toUpperCase() + "\n\n" + term.meaning;
      if (r.length) body += "\n\nYou can read more on the page: " + r[0].entry.title;
      return { answer: body + "\n\n" + DISCLAIMER, intent: intent, confidence: 1,
        sources: r.slice(0, 2).map(x => ({ kind: x.entry.kind, id: x.entry.id, title: x.entry.title })),
        suggestions: suggestFor(r.length ? r[0].entry : null) };
    }
  }

  let res = ENGINE.search(msg, 8);
  if (intent === "document") {
    const tpl = res.filter(r => r.entry.kind === "document");
    if (tpl.length) res = tpl.concat(res.filter(r => r.entry.kind !== "document"));
  }
  res = res.slice(0, 5);

  if (!res.length || res[0].score < 0.02) {
    return Object.assign(base, { intent: "unknown", answer:
      "I could not find a confident match for that in my knowledge base.\n\nI currently cover " + DB.categories.length +
      " areas of law including criminal, civil, property, company, contract, labour, intellectual property, cyber, family, consumer, tax, banking, motor vehicle, environment, infrastructure, medical, education and international law.\n\nTry rephrasing with the subject you are concerned about – for example ‘my employer has not paid my salary’ or ‘builder has delayed possession of my flat’.\n\n" + DISCLAIMER });
  }

  const best = res[0].entry;
  let text = best.kind === "topic" ? topicAnswer(best.obj) : docAnswer(best.obj);
  if (res.length > 1) text += "\n\nRELATED PAGES\n" + bul(res.slice(1, 3).map(r => r.entry.title));

  return { answer: text + "\n\n" + DISCLAIMER, intent: intent, confidence: res[0].score,
    sources: res.slice(0, 3).map(x => ({ kind: x.entry.kind, id: x.entry.id, title: x.entry.title, score: x.score })),
    suggestions: suggestFor(best) };
}

const TABS = [
  ["home", "Home"], ["areas", "Areas of Law"], ["docs", "Documents"],
  ["chat", "Ask the Assistant"], ["glossary", "Glossary"],
  ["sos", "Emergency Help"], ["about", "About"]
];

/* ---------------------------------------------------------------
   4. VIEWS
   --------------------------------------------------------------- */
let state = { route: "home", arg: null };

function go(route, arg) {
  state = { route: route, arg: arg || null };
  stopSpeech();
  render();
  window.scrollTo({ top: 0, behavior: "instant" });
  document.querySelectorAll("#tabs button").forEach(b =>
    b.setAttribute("aria-current", b.dataset.r === route ? "true" : "false"));
}

function render() {
  const v = view();
  const r = state.route;
  if (r === "home") v.innerHTML = viewHome();
  else if (r === "areas") v.innerHTML = viewAreas();
  else if (r === "category") v.innerHTML = viewCategory(state.arg);
  else if (r === "topic") v.innerHTML = viewTopic(state.arg);
  else if (r === "docs") v.innerHTML = viewDocs();
  else if (r === "doc") { v.innerHTML = viewDoc(state.arg); markBlanks(); syncSaveButton(); }
  else if (r === "chat") { v.innerHTML = viewChat(); initChat(); }
  else if (r === "glossary") v.innerHTML = viewGlossary("");
  else if (r === "sos") v.innerHTML = viewSos();
  else if (r === "sosCard") { v.innerHTML = viewSosCard(state.arg); }
  else if (r === "search") v.innerHTML = viewSearch(state.arg);
  else if (r === "about") v.innerHTML = viewAbout();
  else v.innerHTML = viewHome();
}

function viewHome() {
  const s = DB.stats;
  const feat = ["fundamental-rights", "fir-filing", "rent-and-tenancy", "consumer-complaint", "employee-rights", "cybercrime-reporting"].map(topicOf).filter(Boolean);
  const docs = ["rental-agreement", "nda", "legal-notice", "will-testament", "offer-letter", "rti-application"].map(docOf).filter(Boolean);
  return `
  <section class="hero">
    <div class="eyebrow">Indian law, in plain English</div>
    <h1>Every law, <em>explained simply</em>.</h1>
    <p class="lede">From your fundamental rights to company incorporation, from a rent agreement to an international treaty &mdash; find the law you need, and ask the assistant anything by typing or speaking.</p>
    <div class="askbox">
      <input id="heroAsk" placeholder="e.g. my landlord is not returning my deposit" aria-label="Ask a question">
      <button class="btn seal" onclick="askFromHero()">Find the law</button>
    </div>
    <div class="row">
      <button class="btn ghost" onclick="go('chat')">Talk to the assistant</button>
      <button class="btn ghost" onclick="go('areas')">Browse all areas of law</button>
    </div>
    <div class="figures tnum">
      <div><b>${s.categories}</b><span>Areas of law</span></div>
      <div><b>${s.topics}</b><span>Legal topics</span></div>
      <div><b>${s.documents}</b><span>Templates</span></div>
      <div><b>${s.faqs}</b><span>Answered FAQs</span></div>
      <div><b>${s.glossary}</b><span>Glossary terms</span></div>
    </div>
  </section>

  <section style="margin-bottom:34px">
    <div class="head"><h2>Need help right now?</h2><p>Action-first cards for situations where you have minutes, not days.</p></div>
    <div class="grid g3">
      ${DB.emergency.slice(0, 6).map(c => `
        <button class="card" onclick="go('sosCard','${c.id}')">
          <h3>${esc(c.title)}</h3>
          <p>${esc(c.immediate[0])}</p>
          <div class="foot"><span class="tag seal">Urgent</span><span class="tag">${c.immediate.length} steps</span></div>
        </button>`).join("")}
    </div>
  </section>

  <section style="margin-bottom:34px">
    <div class="head"><h2>Every branch of law, A to Z</h2><p>Pick the area your problem belongs to &mdash; or just describe it to the assistant.</p></div>
    <div class="grid g4">
      ${DB.categories.map(c => `
        <button class="card" onclick="go('category','${c.id}')">
          <h3>${esc(c.name)}</h3>
          <p>${esc(c.tagline)}</p>
          <div class="foot"><span class="tag">${topicsIn(c.id).length} topics</span></div>
        </button>`).join("")}
    </div>
  </section>

  <section style="margin-bottom:34px">
    <div class="head"><h2>Most read topics</h2><p>The questions people actually arrive with.</p></div>
    <div class="grid g3">
      ${feat.map(t => `
        <button class="card" onclick="go('topic','${t.id}')">
          <h3>${esc(t.title)}</h3>
          <p>${esc(t.summary.slice(0, 155))}&hellip;</p>
          <div class="foot"><span class="tag">${t.key_points.length} key points</span><span class="tag">${t.faqs.length} FAQs</span></div>
        </button>`).join("")}
    </div>
  </section>

  <section>
    <div class="head"><h2>Ready-to-use templates</h2><p>Every blank is marked in [SQUARE BRACKETS] so you know exactly what to replace.</p></div>
    <div class="grid g3">
      ${docs.map(d => `
        <button class="card" onclick="go('doc','${d.id}')">
          <h3>${esc(d.title)}</h3>
          <p>${esc(d.purpose)}</p>
          <div class="foot"><span class="tag brass">Template</span><span class="tag">${d.checklist.length}-point checklist</span></div>
        </button>`).join("")}
    </div>
  </section>`;
}

function viewAreas() {
  return `
  <div class="head"><div class="eyebrow">Coverage</div><h1>All ${DB.categories.length} Areas of Law</h1>
  <p>Law is not one subject but many. Each branch has its own statutes, its own forum and its own procedure.</p></div>
  <div class="grid g2">
    ${DB.categories.map(c => `
      <div class="card static">
        <h3>${esc(c.name)}</h3>
        <p>${esc(c.description)}</p>
        <ul style="margin:6px 0 0;padding-left:1.1rem;font-size:.87rem">
          ${topicsIn(c.id).map(t => `<li><button style="background:none;border:none;padding:0;color:var(--seal);cursor:pointer;font:inherit;text-align:left" onclick="go('topic','${t.id}')">${esc(t.title)}</button></li>`).join("")}
        </ul>
        <div class="foot">
          <span class="tag">${topicsIn(c.id).length} topics</span>
          ${docsIn(c.id).length ? `<span class="tag brass">${docsIn(c.id).length} templates</span>` : ""}
          <button class="btn sm ghost" style="margin-left:auto" onclick="go('category','${c.id}')">Open</button>
        </div>
      </div>`).join("")}
  </div>`;
}

function viewCategory(id) {
  const c = catOf(id); if (!c) return notFound("area of law");
  const ts = topicsIn(id), ds = docsIn(id);
  return `
  <div class="head"><div class="eyebrow"><button style="background:none;border:none;padding:0;color:var(--ink-3);cursor:pointer;font:inherit" onclick="go('areas')">Areas of law</button> / ${esc(c.name)}</div>
  <h1>${esc(c.name)}</h1><p>${esc(c.description)}</p></div>
  <div class="head"><h2>Topics in this area</h2></div>
  <div class="grid g3" style="margin-bottom:30px">
    ${ts.map(t => `<button class="card" onclick="go('topic','${t.id}')"><h3>${esc(t.title)}</h3><p>${esc(t.summary.slice(0,150))}&hellip;</p><div class="foot"><span class="tag">${t.key_points.length} key points</span><span class="tag">${t.laws.length} laws</span></div></button>`).join("")}
  </div>
  ${ds.length ? `<div class="head"><h2>Templates for this area</h2></div><div class="grid g3">
    ${ds.map(d => `<button class="card" onclick="go('doc','${d.id}')"><h3>${esc(d.title)}</h3><p>${esc(d.purpose)}</p><div class="foot"><span class="tag brass">Template</span></div></button>`).join("")}
  </div>` : ""}`;
}

function viewTopic(id) {
  const t = topicOf(id); if (!t) return notFound("topic");
  const c = catOf(t.category);
  const rel = topicsIn(t.category).filter(x => x.id !== id).slice(0, 3);
  const rd = docsIn(t.category).slice(0, 3);
  return `
  <div class="head"><div class="eyebrow"><button style="background:none;border:none;padding:0;color:var(--ink-3);cursor:pointer;font:inherit" onclick="go('category','${c.id}')">${esc(c.name)}</button></div>
  <h1>${esc(t.title)}</h1></div>
  <div class="layout">
    <article id="readable">
      <div class="pull">${esc(t.summary)}</div>
      <div class="row" style="margin-bottom:20px">
        <button class="btn sm ghost" id="readBtn" onclick="readPage()">Listen to this page</button>
        <button class="btn sm ghost" onclick="go('chat')">Ask a follow-up</button>
      </div>
      <h2>Key points to remember</h2><ul>${t.key_points.map(p => `<li>${esc(p)}</li>`).join("")}</ul>
      ${t.steps && t.steps.length ? `<h2>What you should actually do</h2><ol class="steps">${t.steps.map(s => `<li>${esc(s)}</li>`).join("")}</ol>` : ""}
      <h2>The law that applies</h2><ul class="laws">${t.laws.map(l => `<li>${esc(l)}</li>`).join("")}</ul>
      ${t.faqs && t.faqs.length ? `<h2>Frequently asked questions</h2>${t.faqs.map(f => `<details class="faq"><summary>${esc(f.q)}</summary><div class="body">${esc(f.a)}</div></details>`).join("")}` : ""}
      <div class="note warn" style="margin-top:24px"><b>Remember:</b> this page explains the general position for learning. Statutes are amended, states differ, and the outcome of a real case depends on its own facts. Consult a qualified advocate before acting.</div>
    </article>
    <aside>
      <div class="panel dark"><h4>Ask about this</h4><p>Not sure how this applies to your situation? Describe it to the assistant &mdash; type it or speak it.</p><button class="btn seal" onclick="go('chat')">Open the assistant</button></div>
      ${rel.length ? `<div class="panel"><h4>Related topics</h4><ul>${rel.map(x => `<li><a onclick="go('topic','${x.id}')" tabindex="0" role="button">${esc(x.title)}</a></li>`).join("")}</ul></div>` : ""}
      ${rd.length ? `<div class="panel"><h4>Documents you may need</h4><ul>${rd.map(d => `<li><a onclick="go('doc','${d.id}')" tabindex="0" role="button">${esc(d.title)}</a></li>`).join("")}</ul></div>` : ""}
      <div class="panel"><h4>Emergency numbers</h4><ul>${DB.helplines.slice(0, 5).map(h => `<li class="hlrow"><span>${esc(h.name)}</span> <b>${esc(h.number)}</b></li>`).join("")}</ul></div>
    </aside>
  </div>`;
}

function viewDocs() {
  return `
  <div class="head"><div class="eyebrow">Drafting</div><h1>Legal Document Templates</h1>
  <p>${DB.documents.length} ready-to-use drafts. Every blank is written as [SQUARE BRACKETS] so you can see exactly what to replace.</p></div>
  <div class="card static" style="margin-bottom:18px">
    <label for="docFilter" style="font-size:.85rem;font-weight:600">Filter templates</label>
    <input id="docFilter" oninput="filterDocs(this.value)" placeholder="rent, notice, affidavit, employment&hellip;"
      style="padding:10px 13px;border:1px solid var(--rule);border-radius:var(--r);background:var(--paper);color:var(--ink);font:inherit">
    <div class="muted" id="docCount" style="font-size:.82rem">${DB.documents.length} templates shown</div>
  </div>
  <div class="grid g3" id="docGrid">
    ${DB.documents.map(d => `
      <button class="card" data-f="${esc((d.title + " " + d.purpose + " " + d.keywords.join(" ")).toLowerCase())}" onclick="go('doc','${d.id}')">
        <h3>${esc(d.title)}</h3><p>${esc(d.purpose)}</p>
        <div class="foot"><span class="tag brass">${esc(catName(d.category).split(" ")[0])}</span><span class="tag">${d.checklist.length}-point checklist</span></div>
      </button>`).join("")}
  </div>
  <div class="note warn" style="margin-top:24px"><b>Before you use any template:</b> stamp duty and registration requirements are fixed by each State and change from time to time. Always have an advocate review the final document before signing.</div>`;
}

function filterDocs(q) {
  const n = q.toLowerCase().trim();
  let shown = 0;
  document.querySelectorAll("#docGrid [data-f]").forEach(el => {
    const ok = el.dataset.f.includes(n);
    el.style.display = ok ? "" : "none";
    if (ok) shown++;
  });
  document.getElementById("docCount").textContent = shown + " of " + DB.documents.length + " shown";
}

function viewDoc(id) {
  const d = docOf(id); if (!d) return notFound("template");
  const c = catOf(d.category);
  const rel = docsIn(d.category).filter(x => x.id !== id).slice(0, 3);
  return `
  <div class="head"><div class="eyebrow"><button style="background:none;border:none;padding:0;color:var(--ink-3);cursor:pointer;font:inherit" onclick="go('docs')">Documents</button> / ${esc(c.name)}</div>
  <h1>${esc(d.title)}</h1><p>${esc(d.purpose)}</p></div>
  <div class="layout">
    <article>
      <div class="note info"><b>When to use this:</b> ${esc(d.when_to_use)}</div>
      <h2>Keep this ready before you start</h2><ul>${d.checklist.map(x => `<li>${esc(x)}</li>`).join("")}</ul>
      <h2>Stamp duty, registration and signing</h2><div class="note warn">${esc(d.stamp)}</div>
      <h2>The template</h2>
      <p class="muted" style="font-size:.86rem">Everything highlighted is a blank you must replace with your own details. Delete any clause that does not apply to you.</p>
      <div class="toolbar">
        <span class="name">${esc(d.title)}</span>
        <button class="btn sm ghost" style="color:#fff;border-color:rgba(255,255,255,.3)" onclick="copyTpl(this)">Copy text</button>
        <button class="btn sm ghost" id="saveBtn" style="color:#fff;border-color:rgba(255,255,255,.3)" onclick="downloadTpl('${d.id}', this)">Download .txt</button>
      </div>
      <pre class="tpl" id="tpl">${esc(d.body)}</pre>
      <div class="note danger" style="margin-top:20px"><b>This is a learning sample, not legal advice.</b> A document that is wrongly drafted, insufficiently stamped or not registered where the law requires registration may be unenforceable.</div>
    </article>
    <aside>
      <div class="panel dark"><h4>Not sure this is right?</h4><p>Describe your situation and the assistant will point you to the correct document.</p><button class="btn seal" onclick="go('chat')">Ask the assistant</button></div>
      ${rel.length ? `<div class="panel"><h4>Related templates</h4><ul>${rel.map(x => `<li><a onclick="go('doc','${x.id}')" tabindex="0" role="button">${esc(x.title)}</a></li>`).join("")}</ul></div>` : ""}
      <div class="panel"><h4>Learn the law behind it</h4><ul><li><a onclick="go('category','${c.id}')" tabindex="0" role="button">${esc(c.name)}</a></li><li><a onclick="go('glossary')" tabindex="0" role="button">A&ndash;Z legal glossary</a></li></ul></div>
    </aside>
  </div>`;
}

function markBlanks() {
  const el = document.getElementById("tpl");
  if (!el) return;
  el.dataset.raw = el.textContent;
  el.innerHTML = esc(el.textContent).replace(/\[([^\]]+)\]/g, "<mark>[$1]</mark>");
}
function copyTpl(btn) {
  const el = document.getElementById("tpl");
  const text = el.dataset.raw || el.textContent;
  const done = () => { const o = btn.textContent; btn.textContent = "Copied"; setTimeout(() => btn.textContent = o, 1500); };
  if (navigator.clipboard) navigator.clipboard.writeText(text).then(done).catch(() => fallbackCopy(text, done));
  else fallbackCopy(text, done);
}
function fallbackCopy(text, done) {
  const a = document.createElement("textarea");
  a.value = text; a.style.position = "fixed"; a.style.opacity = "0";
  document.body.appendChild(a); a.select();
  try { document.execCommand("copy"); done(); } catch (e) {}
  document.body.removeChild(a);
}
/* Saving a file works differently depending on where this page is opened, so
   the host's downloads capability is resolved once at start-up and we fall
   back to an ordinary blob link when the file is opened straight from disk -
   which is how the project is demonstrated offline. */
let DOWNLOADS = null, DOWNLOADS_READY = false;
if (typeof window !== "undefined" && window.claude && typeof window.claude.use === "function") {
  window.claude.use("downloads")
    .then(function (d) { DOWNLOADS = d; DOWNLOADS_READY = true; syncSaveButton(); })
    .catch(function () { DOWNLOADS_READY = true; syncSaveButton(); });
} else {
  DOWNLOADS_READY = true;
}
function hostedHere() { return typeof window !== "undefined" && !!window.claude; }
function supportsBlobSave() {
  return typeof URL !== "undefined" && typeof URL.createObjectURL === "function" && !hostedHere();
}
function syncSaveButton() {
  const b = document.getElementById("saveBtn");
  if (b && DOWNLOADS_READY && !DOWNLOADS && !supportsBlobSave()) b.style.display = "none";
}

function templateFileText(d) {
  const line = "=".repeat(74);
  return line + "\n" + d.title.toUpperCase() + "\n" + line +
    "\n\nPURPOSE      : " + d.purpose + "\nWHEN TO USE  : " + d.when_to_use +
    "\n\nSTAMP DUTY / REGISTRATION\n" + d.stamp +
    "\n\nBEFORE YOU START, KEEP READY\n" + d.checklist.map(x => "  - " + x).join("\n") +
    "\n\n" + "-".repeat(74) + "\nReplace every [SQUARE BRACKET] with your own details.\n" + "-".repeat(74) + "\n\n" +
    d.body + "\n\n" + "-".repeat(74) +
    "\nGenerated by LegalMitra - an academic project.\nThis is a sample draft for learning, NOT legal advice.\n" + "-".repeat(74) + "\n";
}

async function downloadTpl(id, btn) {
  const d = docOf(id);
  if (!d) return;
  const text = templateFileText(d);
  const filename = id + ".txt";
  const label = btn ? btn.textContent : null;
  const restore = () => { if (btn && label) setTimeout(() => { btn.textContent = label; }, 1700); };

  if (DOWNLOADS) {
    try {
      if (btn) btn.textContent = "Saving...";
      await DOWNLOADS.save({ filename: filename, data: text });
      if (btn) btn.textContent = "Saved";
      restore();
    } catch (err) {
      const code = err && err.code;
      if (btn) btn.textContent = (code === "declined") ? label : "Could not save";
      restore();
      if (code === "unavailable" || code === "not_granted") syncSaveButton();
    }
    return;
  }

  if (supportsBlobSave()) {
    const url = URL.createObjectURL(new Blob([text], { type: "text/plain;charset=utf-8" }));
    const a = document.createElement("a");
    a.href = url; a.download = filename;
    document.body.appendChild(a); a.click(); document.body.removeChild(a);
    setTimeout(() => URL.revokeObjectURL(url), 1000);
    return;
  }

  /* Nowhere to save it - copy the text instead, which always works. */
  fallbackCopy(text, () => { if (btn) { btn.textContent = "Copied instead"; restore(); } });
}

function viewGlossary(letter) {
  const letters = [...new Set(DB.glossary.map(g => g.term[0].toUpperCase()))].sort();
  const terms = DB.glossary.slice().sort((a, b) => a.term.localeCompare(b.term))
    .filter(g => !letter || g.term.toUpperCase().startsWith(letter));
  return `
  <div class="head"><div class="eyebrow">Vocabulary</div><h1>A&ndash;Z Legal Glossary</h1>
  <p>${DB.glossary.length} legal words, each explained in one sentence.</p></div>
  <div class="az">
    <button onclick="go('glossary')" aria-pressed="${!letter}">All</button>
    ${letters.map(L => `<button onclick="setLetter('${L}')" aria-pressed="${letter === L}">${L}</button>`).join("")}
  </div>
  <div class="card static" style="margin-bottom:16px">
    <input id="gFilter" oninput="filterTerms(this.value)" placeholder="Start typing: bail, decree, tort&hellip;"
      style="padding:10px 13px;border:1px solid var(--rule);border-radius:var(--r);background:var(--paper);color:var(--ink);font:inherit">
  </div>
  <div id="terms">${terms.map(g => `<div class="term" data-f="${esc((g.term + " " + g.meaning).toLowerCase())}"><b>${esc(g.term)}</b><p>${esc(g.meaning)}</p></div>`).join("")}</div>`;
}
function setLetter(L) { view().innerHTML = viewGlossary(L); }
function filterTerms(q) {
  const n = q.toLowerCase().trim();
  document.querySelectorAll("#terms [data-f]").forEach(el => { el.style.display = el.dataset.f.includes(n) ? "" : "none"; });
}

function viewSos() {
  return `
  <div class="head"><div class="eyebrow">Immediate help</div><h1>Emergency Quick Help</h1>
  <p>For situations where you have minutes, not days. Each card tells you what to do first, what <b>not</b> to do, and which number to call.</p></div>
  <div class="note danger"><b>If life or safety is in immediate danger, call 112 first.</b> Legal steps come after you are safe.</div>
  <div class="grid g2" style="margin-bottom:34px">
    ${DB.emergency.map(c => `
      <div class="sos">
        <h3>${esc(c.title)}</h3>
        <ul class="do">${c.immediate.slice(0, 4).map(s => `<li>${esc(s)}</li>`).join("")}</ul>
        <div class="row"><span class="tag seal">${esc(c.helpline.split("|")[0].trim())}</span>
        <button class="btn sm ghost" style="margin-left:auto" onclick="go('sosCard','${c.id}')">Full steps</button></div>
      </div>`).join("")}
  </div>
  <div class="head"><h2>National helpline numbers</h2><p>Free, 24x7, available across India.</p></div>
  <div class="grid g4">${DB.helplines.map(h => `<div class="hl-card"><b class="tnum">${esc(h.number)}</b><span>${esc(h.name)}</span></div>`).join("")}</div>`;
}

function viewSosCard(id) {
  const c = DB.emergency.find(x => x.id === id); if (!c) return notFound("card");
  const t = topicOf(c.topic);
  return `
  <div class="head"><div class="eyebrow"><button style="background:none;border:none;padding:0;color:var(--ink-3);cursor:pointer;font:inherit" onclick="go('sos')">Emergency help</button></div>
  <h1>${esc(c.title)}</h1><p>${esc(c.helpline)}</p></div>
  <div class="layout">
    <article id="readable">
      <div class="note danger"><b>If you are in immediate physical danger, call 112 now.</b> Do the legal steps below once you are safe.</div>
      <div class="row" style="margin-bottom:18px"><button class="btn sm ghost" id="readBtn" onclick="readPage()">Listen to these steps</button></div>
      <h2>Do this now</h2><ol class="steps">${c.immediate.map(s => `<li>${esc(s)}</li>`).join("")}</ol>
      <h2>Do NOT do this</h2><ul class="dont">${c.do_not.map(s => `<li>${esc(s)}</li>`).join("")}</ul>
      <h2>Who to call</h2><div class="note info"><b>${esc(c.helpline)}</b></div>
      ${t ? `<h2>Understand the law behind this</h2><p>Once the immediate situation is handled, read the full topic so you know what happens next.</p><button class="btn" onclick="go('topic','${t.id}')">${esc(t.title)}</button>` : ""}
    </article>
    <aside>
      <div class="panel dark"><h4>Ask something specific</h4><p>Describe what is happening and get an immediate answer, by voice or text.</p><button class="btn seal" onclick="go('chat')">Ask the assistant</button></div>
      <div class="panel"><h4>All helplines</h4><ul>${DB.helplines.map(h => `<li class="hlrow"><span>${esc(h.name)}</span> <b>${esc(h.number)}</b></li>`).join("")}</ul></div>
    </aside>
  </div>`;
}

function viewSearch(q) {
  const res = ENGINE.search(q, 20);
  const gl = DB.glossary.filter(g => g.term.toLowerCase().includes(q.toLowerCase()) || g.meaning.toLowerCase().includes(q.toLowerCase())).slice(0, 4);
  return `
  <div class="head"><div class="eyebrow">Search</div><h1>Results for &ldquo;${esc(q)}&rdquo;</h1>
  <p>${res.length} matching page${res.length === 1 ? "" : "s"}, ranked by the same relevance score the assistant uses.</p></div>
  ${gl.length ? `<div class="card static" style="margin-bottom:18px"><h3>Glossary matches</h3>${gl.map(g => `<div class="term"><b>${esc(g.term)}</b><p>${esc(g.meaning)}</p></div>`).join("")}</div>` : ""}
  ${res.length ? res.map(r => `
    <button class="result" onclick="go('${r.entry.kind === "topic" ? "topic" : "doc"}','${r.entry.id}')">
      <h3>${esc(r.entry.title)}</h3>
      <p>${esc((r.entry.obj.summary || r.entry.obj.purpose || "").slice(0, 210))}</p>
      <div class="row" style="align-items:center;font-size:.76rem">
        <span class="tag ${r.entry.kind === "document" ? "brass" : ""}">${r.entry.kind === "document" ? "Template" : "Topic"}</span>
        <span class="muted">${esc(catName(r.entry.category))}</span>
        <span class="meter"><i style="width:${Math.min(100, Math.round(r.score * 100))}%"></i></span>
        <span class="muted tnum">${r.score.toFixed(3)}</span>
      </div>
    </button>`).join("") : `
    <div class="card static" style="text-align:center;padding:38px">
      <h3>Nothing matched that</h3>
      <p>Try describing the problem instead of naming the law &mdash; for example &ldquo;my employer has not paid my salary&rdquo;.</p>
      <div class="row" style="justify-content:center"><button class="btn seal" onclick="go('chat')">Ask the assistant</button><button class="btn ghost" onclick="go('areas')">Browse areas of law</button></div>
    </div>`}`;
}

function viewAbout() {
  const s = DB.stats;
  return `
  <div class="head"><div class="eyebrow">Second year engineering mini project</div><h1>About this Project</h1>
  <p>LegalMitra is a legal information portal with a voice-enabled assistant, built from scratch in Python and plain HTML, CSS and JavaScript.</p></div>
  <div class="layout">
    <article>
      <h2>The idea</h2>
      <p>Most people meet the law only when something has already gone wrong &mdash; a cheque bounces, a landlord keeps a deposit, a salary goes unpaid, a builder misses a possession date. At that moment they face two problems at once: they do not know which branch of law their problem belongs to, and everything written about it is written for lawyers.</p>
      <p>We wanted to build the thing we wished existed: one place where a person can describe a problem in ordinary words &mdash; or simply speak it &mdash; and get back a plain-English explanation, the practical steps to take, the Act that applies, and the document they will need.</p>

      <h2>What it contains</h2>
      <ul>
        <li><b>${s.categories} areas of law</b>, from constitutional and criminal to infrastructure, environment, medical and international law.</li>
        <li><b>${s.topics} legal topics</b>, each with a summary, key points, a step-by-step procedure, the statutes that apply and FAQs.</li>
        <li><b>${s.documents} document templates</b> with every blank marked, plus notes on stamp duty and registration.</li>
        <li><b>${s.glossary} glossary terms</b> and <b>${s.faqs} answered questions</b>.</li>
        <li>Ten emergency quick-help cards and a talking assistant that listens, searches, answers and speaks.</li>
      </ul>

      <h2>How the assistant works</h2>
      <p>There is no pre-trained model. The steps are:</p>
      <ol class="steps">
        <li><b>Clean</b> &mdash; the question is lower-cased, punctuation stripped, split into words.</li>
        <li><b>Stem</b> &mdash; word endings are removed so &ldquo;filing&rdquo;, &ldquo;filed&rdquo; and &ldquo;file&rdquo; all match.</li>
        <li><b>Expand</b> &mdash; everyday words are mapped to legal ones, so &ldquo;my boss fired me&rdquo; also searches for &ldquo;termination&rdquo;.</li>
        <li><b>Weigh</b> &mdash; every word gets a TF-IDF score, so a rare word like &ldquo;gratuity&rdquo; counts far more than a common one like &ldquo;law&rdquo;.</li>
        <li><b>Match</b> &mdash; cosine similarity compares the question against all ${ENGINE.size} indexed entries and picks the closest.</li>
        <li><b>Compose</b> &mdash; the winner becomes a structured answer: explanation, key points, steps, and the law.</li>
      </ol>
      <p>An intent layer sits on top, so greetings, definitions, emergencies and requests for a document format are handled differently from an ordinary legal question. If nothing scores above a confidence floor, the assistant says plainly that it does not know rather than guessing &mdash; in a legal context a confidently wrong answer is the most damaging output possible.</p>

      <h2>Technology</h2>
      <div class="scroll-x"><table class="data">
        <tr><th>Layer</th><th>Technology</th><th>Why</th></tr>
        <tr><td>Backend</td><td>Python 3 + Flask</td><td>Smallest possible web framework; one function per page</td></tr>
        <tr><td>Templates</td><td>Jinja2</td><td>Ships with Flask; keeps HTML and Python separate</td></tr>
        <tr><td>Frontend</td><td>HTML5, CSS3, vanilla JavaScript</td><td>No build tools, no dependencies, fully readable</td></tr>
        <tr><td>Database</td><td>SQLite 3</td><td>Built into Python; the whole database is one file</td></tr>
        <tr><td>Search</td><td>TF-IDF + cosine similarity, hand-written</td><td>Explainable maths instead of a black-box library</td></tr>
        <tr><td>Voice</td><td>Web Speech API</td><td>Recognition and synthesis are already in the browser</td></tr>
      </table></div>

      <h2>Measured results</h2>
      <p>The assistant was evaluated on 30 questions phrased the way a non-lawyer would type them. The first version returned the correct page first 66.7% of the time. Inspecting the failures showed document templates were outranking the topics that explained the same subject; adding an intent-conditioned ranking adjustment raised <b>Top-1 accuracy to 93.3%</b> and <b>Top-3 accuracy to 100%</b>, while format requests still reached a template in 10 out of 10 cases.</p>

      <h2>Honest limitations</h2>
      <ul>
        <li>The knowledge base is hand-written and simplified for learning; it is not a substitute for the bare Acts.</li>
        <li>Statutes are amended frequently, and many rules &mdash; especially stamp duty and tenancy &mdash; differ from State to State.</li>
        <li>The engine matches words, not meaning, so an unusual phrasing can still miss the right topic.</li>
        <li>Voice input needs a Chromium-based browser and microphone permission.</li>
        <li>This is an academic project. It is not a law firm and it gives no legal advice.</li>
      </ul>
    </article>
    <aside>
      <div class="panel"><h4>Project at a glance</h4><ul class="tnum">
        <li class="hlrow"><span>Areas of law</span><b>${s.categories}</b></li>
        <li class="hlrow"><span>Legal topics</span><b>${s.topics}</b></li>
        <li class="hlrow"><span>Templates</span><b>${s.documents}</b></li>
        <li class="hlrow"><span>Glossary terms</span><b>${s.glossary}</b></li>
        <li class="hlrow"><span>FAQs</span><b>${s.faqs}</b></li>
        <li class="hlrow"><span>Indexed entries</span><b>${ENGINE.size}</b></li>
        <li class="hlrow"><span>Top-1 accuracy</span><b>93.3%</b></li>
        <li class="hlrow"><span>Top-3 accuracy</span><b>100%</b></li>
      </ul></div>
      <div class="panel dark"><h4>Try it</h4><p>The assistant is the heart of the project. Ask it anything, by voice or text.</p><button class="btn seal" onclick="go('chat')">Open the assistant</button></div>
    </aside>
  </div>`;
}

function notFound(thing) {
  return `<div class="card static" style="text-align:center;padding:50px">
    <h1>That ${esc(thing)} could not be found</h1>
    <p>Try searching instead, or ask the assistant in your own words.</p>
    <div class="row" style="justify-content:center"><button class="btn seal" onclick="go('chat')">Ask the assistant</button><button class="btn ghost" onclick="go('home')">Go home</button></div>
  </div>`;
}

/* ---------------------------------------------------------------
   5. CHAT VIEW + VOICE
   --------------------------------------------------------------- */
const STARTERS = [
  "What are my rights if I am arrested?",
  "My landlord is not returning my security deposit",
  "How do I register a trademark?",
  "Give me a rent agreement format",
  "Builder has delayed possession of my flat",
  "My employer has not paid my salary",
  "A cheque given to me has bounced",
  "How do I file an RTI application?"
];

function viewChat() {
  return `
  <div class="head"><div class="eyebrow">Ask anything</div><h1>Talk to LegalMitra</h1>
  <p>Ask any legal question in your own words &mdash; type it, or press the microphone and speak. The assistant searches ${DB.topics.length} legal topics and ${DB.documents.length} templates, explains the answer, and reads it aloud.</p></div>
  <div class="chat">
    <div class="chat-top">
      <div class="msg"><div class="av">LM</div></div>
      <div class="who"><b>LegalMitra Assistant</b><span><i class="dot"></i> Online &mdash; offline knowledge engine</span></div>
      <div class="acts">
        <button class="iconbtn" id="muteBtn" title="Voice replies are on" aria-label="Toggle voice">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5 6 9H3v6h3l5 4V5z"/><path d="M16 9a4 4 0 0 1 0 6"/><path d="M19 6a8 8 0 0 1 0 12"/></svg>
        </button>
        <button class="iconbtn" onclick="stopSpeech()" title="Stop speaking" aria-label="Stop speaking">
          <svg viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="6" width="12" height="12" rx="2"/></svg>
        </button>
        <button class="iconbtn" onclick="clearChat()" title="New conversation" aria-label="New conversation">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6h18M8 6V4h8v2M6 6l1 14h10l1-14"/></svg>
        </button>
      </div>
    </div>
    <div class="chat-log" id="log"></div>
    <div class="chat-in">
      <div class="line">
        <button class="round" id="micBtn" title="Speak your question" aria-label="Speak your question">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="2" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v4"/></svg>
        </button>
        <textarea id="say" rows="1" placeholder="Type your legal question&hellip;" aria-label="Your question"></textarea>
        <button class="round send" id="sendBtn" title="Send" aria-label="Send">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 12h15M13 6l6 6-6 6"/></svg>
        </button>
      </div>
      <div class="voicebar" id="vbar">
        <span>Press the mic and speak &mdash; Enter sends, Shift+Enter adds a line.</span>
        <span>Voice: <select id="voiceSel" aria-label="Voice"></select></span>
        <span>Speed: <select id="rateSel" aria-label="Speed"><option value="0.8">Slow</option><option value="1" selected>Normal</option><option value="1.25">Fast</option></select></span>
      </div>
    </div>
  </div>
  <div class="head" style="margin:26px 0 12px"><h2>Try one of these</h2></div>
  <div class="row">${STARTERS.map(s => `<button class="chip" onclick="ask(${JSON.stringify(s).replace(/"/g, "&quot;")})">${esc(s)}</button>`).join("")}</div>
  <div class="grid g3" style="margin-top:26px">
    <div class="card static"><h3>How the answer is found</h3><p>Your question is cleaned, stemmed and turned into a TF-IDF vector, then compared by cosine similarity against every topic and template. The closest match is explained back to you.</p></div>
    <div class="card static"><h3>How the voice works</h3><p>Speech recognition and synthesis both run inside your browser using the Web Speech API. Nothing is sent to a paid speech service; it works best in Chrome or Edge.</p></div>
    <div class="card static"><h3>What is stored</h3><p>Nothing. This page keeps the conversation in memory only. No login, no account, no personal data, no server.</p></div>
  </div>
  <div class="note warn" style="margin-top:22px"><b>Important:</b> LegalMitra gives general legal information for learning. It cannot replace an advocate, it does not know the facts of your case, and it must not be relied on for any decision with legal consequences.</div>`;
}

let speakOn = true, busy = false;

function initChat() {
  const say = document.getElementById("say");
  document.getElementById("sendBtn").onclick = () => ask();
  document.getElementById("muteBtn").onclick = toggleMute;
  say.addEventListener("keydown", e => { if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); ask(); } });
  say.addEventListener("input", () => { say.style.height = "auto"; say.style.height = Math.min(say.scrollHeight, 120) + "px"; });
  loadVoices();
  setupMic();
  botSay({
    answer: "Namaste! I am LegalMitra, your legal information assistant.\n\nI can explain any area of law – criminal, civil, property, company, contract, labour, intellectual property, cyber, family, consumer, tax, banking, motor vehicle, environment, infrastructure, medical, education and international law – and I can give you ready-to-use document formats.\n\nYou can type your question, or press the microphone and simply speak.",
    sources: [], suggestions: STARTERS.slice(0, 4), confidence: 1
  }, true);
  say.focus();
}

function fmt(text) {
  return esc(text).split("\n").map(line => {
    const t = line.trim();
    const head = t.length > 2 && t.length < 60 && t === t.toUpperCase() && /[A-Z]/.test(t) && !t.startsWith("-") && !/^\d+\./.test(t);
    return head ? `<span class="hl">${t}</span>` : line;
  }).join("\n");
}

function meSay(text) {
  const log = document.getElementById("log");
  const d = document.createElement("div");
  d.className = "msg me";
  d.innerHTML = `<div class="av">You</div><div class="bubble"></div>`;
  d.querySelector(".bubble").textContent = text;
  log.appendChild(d); log.scrollTop = log.scrollHeight;
}

function botSay(reply, silent) {
  const log = document.getElementById("log");
  const d = document.createElement("div");
  d.className = "msg bot";
  const b = document.createElement("div");
  b.className = "bubble";
  b.innerHTML = fmt(reply.answer);

  const src = document.createElement("div");
  src.className = "src";
  const badge = document.createElement("span");
  badge.className = "tag brass";
  badge.textContent = "Knowledge base";
  src.appendChild(badge);
  (reply.sources || []).slice(0, 3).forEach(s => {
    const btn = document.createElement("button");
    btn.textContent = s.title;
    btn.onclick = () => go(s.kind === "topic" ? "topic" : "doc", s.id);
    src.appendChild(btn);
  });
  b.appendChild(src);

  d.innerHTML = `<div class="av">LM</div>`;
  d.appendChild(b);
  log.appendChild(d);

  if (reply.suggestions && reply.suggestions.length) {
    const c = document.createElement("div");
    c.className = "chips";
    reply.suggestions.forEach(s => {
      const ch = document.createElement("button");
      ch.className = "chip"; ch.textContent = s;
      ch.onclick = () => ask(s);
      c.appendChild(ch);
    });
    log.appendChild(c);
  }
  log.scrollTop = log.scrollHeight;
  if (!silent && speakOn) speak(reply.answer);
}

function ask(text) {
  const say = document.getElementById("say");
  if (!say) { go("chat"); setTimeout(() => ask(text), 60); return; }
  const msg = (text !== undefined ? text : say.value).trim();
  if (!msg || busy) return;
  busy = true;
  stopSpeech();
  meSay(msg);
  say.value = ""; say.style.height = "auto";

  const log = document.getElementById("log");
  const wait = document.createElement("div");
  wait.className = "msg bot"; wait.id = "wait";
  wait.innerHTML = `<div class="av">LM</div><div class="bubble"><div class="typing"><i></i><i></i><i></i></div></div>`;
  log.appendChild(wait); log.scrollTop = log.scrollHeight;

  setTimeout(() => {
    const reply = answer(msg);
    const w = document.getElementById("wait"); if (w) w.remove();
    botSay(reply);
    busy = false;
  }, 260);
}

function askFromHero() {
  const el = document.getElementById("heroAsk");
  const q = el.value.trim();
  if (!q) return;
  go("chat");
  setTimeout(() => ask(q), 80);
}

function clearChat() {
  if (!confirm("Clear this conversation and start fresh?")) return;
  stopSpeech();
  document.getElementById("log").innerHTML = "";
  botSay({ answer: "New conversation started.\n\nAsk me anything about Indian law – your rights, a procedure, a deadline, or a document format you need.",
    sources: [], suggestions: STARTERS.slice(0, 4) }, true);
}

function toggleMute() {
  speakOn = !speakOn;
  const b = document.getElementById("muteBtn");
  b.style.background = speakOn ? "" : "var(--seal-soft)";
  b.style.color = speakOn ? "" : "var(--seal)";
  b.title = speakOn ? "Voice replies are on" : "Voice replies are off";
  if (!speakOn) stopSpeech();
}

/* ---- speech synthesis ---- */
const synth = window.speechSynthesis;
let voices = [];
function loadVoices() {
  if (!synth) { const v = document.getElementById("vbar"); if (v) v.firstElementChild.textContent = "This browser cannot speak. Chrome or Edge is recommended."; return; }
  voices = synth.getVoices().filter(v => v.lang.indexOf("en") === 0);
  const sel = document.getElementById("voiceSel");
  if (!sel) return;
  sel.innerHTML = "";
  voices.forEach((v, i) => {
    const o = document.createElement("option");
    o.value = i; o.textContent = v.name.replace(/Microsoft |Google /, "") + " (" + v.lang + ")";
    if (v.lang === "en-IN") o.selected = true;
    sel.appendChild(o);
  });
}
if (synth && typeof synth.onvoiceschanged !== "undefined") synth.onvoiceschanged = loadVoices;

function cleanSpeech(t) {
  return t.replace(/^\s*[-*]\s*/gm, "").replace(/\n{2,}/g, ". ").replace(/\n/g, ", ").replace(/\s{2,}/g, " ").trim();
}
function speak(text) {
  if (!synth || !speakOn) return;
  stopSpeech();
  const clean = cleanSpeech(text);
  const pieces = clean.match(/[^.!?]+[.!?]*/g) || [clean];
  const queue = []; let buf = "";
  pieces.forEach(p => { if ((buf + p).length > 200) { if (buf) queue.push(buf); buf = p; } else buf += p; });
  if (buf) queue.push(buf);
  const sel = document.getElementById("voiceSel");
  const rate = document.getElementById("rateSel");
  queue.forEach(part => {
    const u = new SpeechSynthesisUtterance(part.trim());
    if (sel && voices.length && voices[+sel.value]) u.voice = voices[+sel.value];
    u.rate = rate ? parseFloat(rate.value) : 1;
    synth.speak(u);
  });
}
function stopSpeech() { if (synth && synth.speaking) synth.cancel(); const b = document.getElementById("readBtn"); if (b) b.textContent = "Listen to this page"; }

function readPage() {
  const el = document.getElementById("readable");
  const btn = document.getElementById("readBtn");
  if (!el || !synth) return;
  if (synth.speaking) { stopSpeech(); return; }
  const text = el.innerText.replace(/\n{2,}/g, ". ").replace(/\n/g, ", ");
  const pieces = text.match(/[^.!?]+[.!?]*/g) || [text];
  const queue = []; let buf = "";
  pieces.forEach(p => { if ((buf + p).length > 200) { if (buf) queue.push(buf); buf = p; } else buf += p; });
  if (buf) queue.push(buf);
  const indian = voices.filter(v => v.lang === "en-IN")[0];
  queue.forEach((part, i) => {
    const u = new SpeechSynthesisUtterance(part.trim());
    if (indian) u.voice = indian;
    if (i === queue.length - 1) u.onend = () => { if (btn) btn.textContent = "Listen to this page"; };
    synth.speak(u);
  });
  if (btn) btn.textContent = "Stop reading";
}

/* ---- speech recognition ---- */
let recog = null, listening = false;
function setupMic() {
  const Rec = window.SpeechRecognition || window.webkitSpeechRecognition;
  const mic = document.getElementById("micBtn");
  const say = document.getElementById("say");
  if (!Rec || !mic) {
    if (mic) mic.style.display = "none";
    const v = document.getElementById("vbar");
    if (v) v.firstElementChild.textContent = "Voice input needs Chrome or Edge. You can still type your question.";
    return;
  }
  recog = new Rec();
  recog.lang = "en-IN";
  recog.continuous = false;
  recog.interimResults = true;

  recog.onstart = () => { listening = true; mic.classList.add("live"); say.placeholder = "Listening… speak now"; };
  recog.onend = () => { listening = false; mic.classList.remove("live"); say.placeholder = "Type your legal question…"; };
  recog.onerror = (e) => {
    listening = false; mic.classList.remove("live"); say.placeholder = "Type your legal question…";
    if (e.error === "not-allowed") alert("Microphone access was blocked. Allow the microphone in your browser settings to use voice input.");
  };
  recog.onresult = (e) => {
    let text = "";
    for (let i = e.resultIndex; i < e.results.length; i++) text += e.results[i][0].transcript;
    say.value = text;
    if (e.results[e.results.length - 1].isFinal) setTimeout(() => ask(), 400);
  };
  mic.onclick = () => {
    if (listening) recog.stop();
    else { stopSpeech(); try { recog.start(); } catch (err) {} }
  };
}

/* ---------------------------------------------------------------
   6. BOOT
   --------------------------------------------------------------- */
document.getElementById("tabs").innerHTML = TABS.map(([r, label]) =>
  `<li><button data-r="${r}" onclick="go('${r}')">${label}</button></li>`).join("");

document.getElementById("fCat").textContent = DB.stats.categories;
document.getElementById("fTop").textContent = DB.stats.topics;
document.getElementById("fDoc").textContent = DB.stats.documents;
document.getElementById("fHelp").innerHTML = DB.helplines.slice(0, 6)
  .map(h => `<li class="hlrow"><span>${esc(h.name)}</span> <b>${esc(h.number)}</b></li>`).join("");

const omni = document.getElementById("omni");
omni.addEventListener("keydown", e => {
  if (e.key === "Enter") { const q = omni.value.trim(); if (q) go("search", q); }
});

document.getElementById("themeBtn").onclick = () => {
  const root = document.documentElement;
  const dark = root.getAttribute("data-theme") === "dark" ||
    (!root.getAttribute("data-theme") && window.matchMedia("(prefers-color-scheme: dark)").matches);
  root.setAttribute("data-theme", dark ? "light" : "dark");
  try { localStorage.setItem("lm-theme", dark ? "light" : "dark"); } catch (e) {}
};
try {
  const saved = localStorage.getItem("lm-theme");
  if (saved) document.documentElement.setAttribute("data-theme", saved);
} catch (e) {}

window.addEventListener("beforeunload", stopSpeech);
go("home");
</script>
"""


def main():
    data = export_data()
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    html = HTML.replace("__DATA__", payload)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "legalmitra.html")
    with open(out, "w", encoding="utf-8") as handle:
        handle.write(html)

    print("Static site written to:", out)
    print("  size            : %.0f KB" % (len(html.encode("utf-8")) / 1024.0))
    print("  categories      :", len(data["categories"]))
    print("  topics          :", len(data["topics"]))
    print("  documents       :", len(data["documents"]))
    print("  glossary terms  :", len(data["glossary"]))
    print("  emergency cards :", len(data["emergency"]))
    return out


if __name__ == "__main__":
    main()
