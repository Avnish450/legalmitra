/* ==========================================================================
   main.js - small helpers used on every page except the chat page
   Plain JavaScript, no libraries.
   ========================================================================== */

(function () {
    "use strict";

    /* ------------------------------------------------------------------
       1. MOBILE NAVIGATION
       The hamburger button shows and hides the menu on small screens.
       ------------------------------------------------------------------ */
    var toggle = document.getElementById("navToggle");
    var menu = document.getElementById("navMenu");
    if (toggle && menu) {
        toggle.addEventListener("click", function () {
            menu.classList.toggle("open");
        });
    }

    /* ------------------------------------------------------------------
       2. HIGHLIGHT THE BLANKS IN A DOCUMENT TEMPLATE
       Every place the user must fill in is written as [LIKE THIS] in the
       template text. Here we wrap each one in a <mark> tag so it stands out
       in yellow, without changing the stored template itself.
       ------------------------------------------------------------------ */
    var template = document.getElementById("templateBody");
    if (template) {
        var raw = template.textContent;
        var escaped = raw
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;");
        template.innerHTML = escaped.replace(/\[([^\]]+)\]/g, "<mark>[$1]</mark>");
    }

    /* ------------------------------------------------------------------
       3. COPY THE TEMPLATE TO THE CLIPBOARD
       ------------------------------------------------------------------ */
    var copyBtn = document.getElementById("copyBtn");
    if (copyBtn && template) {
        copyBtn.addEventListener("click", function () {
            var text = template.textContent;
            var done = function () {
                var original = copyBtn.textContent;
                copyBtn.textContent = "Copied";
                setTimeout(function () { copyBtn.textContent = original; }, 1600);
            };

            if (navigator.clipboard && window.isSecureContext) {
                navigator.clipboard.writeText(text).then(done);
            } else {
                /* Fallback for plain http:// during a local demo */
                var area = document.createElement("textarea");
                area.value = text;
                area.style.position = "fixed";
                area.style.opacity = "0";
                document.body.appendChild(area);
                area.select();
                try { document.execCommand("copy"); done(); } catch (e) { /* ignore */ }
                document.body.removeChild(area);
            }
        });
    }

    /* ------------------------------------------------------------------
       4. PRINT THE TEMPLATE
       The print stylesheet in style.css hides the header, footer and
       sidebar so only the document itself goes on paper.
       ------------------------------------------------------------------ */
    var printBtn = document.getElementById("printBtn");
    if (printBtn) {
        printBtn.addEventListener("click", function () { window.print(); });
    }

    /* ------------------------------------------------------------------
       5. LIVE FILTER ON THE DOCUMENTS AND GLOSSARY PAGES
       Typing in the filter box hides the cards that do not match, without
       reloading the page.
       ------------------------------------------------------------------ */
    var filterBox = document.getElementById("filterBox");
    if (filterBox) {
        var targets = document.querySelectorAll("[data-filter]");
        var countLabel = document.getElementById("filterCount");

        filterBox.addEventListener("input", function () {
            var needle = filterBox.value.toLowerCase().trim();
            var shown = 0;
            targets.forEach(function (item) {
                var hay = item.getAttribute("data-filter").toLowerCase();
                var match = hay.indexOf(needle) !== -1;
                item.style.display = match ? "" : "none";
                if (match) { shown++; }
            });
            if (countLabel) {
                countLabel.textContent = shown + " of " + targets.length + " shown";
            }
        });
    }

    /* ------------------------------------------------------------------
       6. READ A PAGE ALOUD
       The topic pages have a "Listen" button. It uses the same browser
       speech engine as the chatbot, so no extra software is needed.
       ------------------------------------------------------------------ */
    var listenBtn = document.getElementById("listenBtn");
    var readable = document.getElementById("readable");

    if (listenBtn && readable && window.speechSynthesis) {
        var synth = window.speechSynthesis;
        var reading = false;

        listenBtn.addEventListener("click", function () {
            if (reading || synth.speaking) {
                synth.cancel();
                reading = false;
                listenBtn.textContent = "🔊 Listen to this page";
                return;
            }

            var text = readable.innerText
                .replace(/\n{2,}/g, ". ")
                .replace(/\n/g, ", ")
                .replace(/\s{2,}/g, " ");

            /* Split into chunks so long pages are not cut off */
            var pieces = text.match(/[^.!?]+[.!?]*/g) || [text];
            var buffer = "";
            var queue = [];
            pieces.forEach(function (piece) {
                if ((buffer + piece).length > 200) {
                    if (buffer) { queue.push(buffer); }
                    buffer = piece;
                } else {
                    buffer += piece;
                }
            });
            if (buffer) { queue.push(buffer); }

            var voices = synth.getVoices().filter(function (v) {
                return v.lang.indexOf("en") === 0;
            });
            var indian = voices.filter(function (v) { return v.lang === "en-IN"; })[0];

            queue.forEach(function (part, index) {
                var utterance = new SpeechSynthesisUtterance(part.trim());
                if (indian) { utterance.voice = indian; }
                utterance.rate = 1;
                if (index === queue.length - 1) {
                    utterance.onend = function () {
                        reading = false;
                        listenBtn.textContent = "🔊 Listen to this page";
                    };
                }
                synth.speak(utterance);
            });

            reading = true;
            listenBtn.textContent = "⏹ Stop reading";
        });

        window.addEventListener("beforeunload", function () { synth.cancel(); });
    } else if (listenBtn) {
        listenBtn.style.display = "none";
    }

    /* ------------------------------------------------------------------
       7. BACK TO TOP after a long page
       ------------------------------------------------------------------ */
    var topBtn = document.getElementById("topBtn");
    if (topBtn) {
        window.addEventListener("scroll", function () {
            topBtn.style.display = window.scrollY > 600 ? "block" : "none";
        });
        topBtn.addEventListener("click", function () {
            window.scrollTo({ top: 0, behavior: "smooth" });
        });
    }
})();
