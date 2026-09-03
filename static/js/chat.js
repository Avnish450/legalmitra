/* ==========================================================================
   chat.js - the talking chatbot
   --------------------------------------------------------------------------
   Plain JavaScript. No React, no jQuery, no npm packages.

   THREE THINGS HAPPEN IN THIS FILE

   1. TEXT CHAT
      The typed message is sent to the Flask server at /api/chat using fetch().
      The server replies with JSON, and we draw the reply as a chat bubble.

   2. SPEECH TO TEXT  (the microphone button)
      Uses the browser's built-in Web Speech API - webkitSpeechRecognition.
      The browser itself does the recognition, so no paid speech service and
      no API key is needed. Works in Chrome and Edge.

   3. TEXT TO SPEECH  (the bot speaks the answer)
      Uses window.speechSynthesis, which is also built into the browser.
      The user can pick a voice, change the speaking speed, mute it, or stop
      speech in the middle.

   Everything degrades gracefully: if a browser does not support speech, the
   buttons are hidden and the chat still works by typing.
   ========================================================================== */

(function () {
    "use strict";

    /* ---------------------------------------------------------------- */
    /* Grab the elements we need from the page                          */
    /* ---------------------------------------------------------------- */
    var body       = document.getElementById("chatBody");
    var input      = document.getElementById("chatInput");
    var sendBtn    = document.getElementById("sendBtn");
    var micBtn     = document.getElementById("micBtn");
    var speakBtn   = document.getElementById("speakBtn");
    var stopBtn    = document.getElementById("stopBtn");
    var clearBtn   = document.getElementById("clearBtn");
    var voiceBox   = document.getElementById("voiceSelect");
    var rateBox    = document.getElementById("rateSelect");
    var voiceNote  = document.getElementById("voiceNote");

    if (!body || !input) { return; }   // not on the chat page

    var busy = false;
    var speakOn = true;        // read answers aloud by default

    /* ================================================================== */
    /* PART 1 - DRAWING MESSAGES                                          */
    /* ================================================================== */

    /* The server sends plain text with UPPERCASE HEADINGS on their own line.
       This turns those headings into styled lines and escapes any HTML so a
       user cannot inject markup into the page. */
    function formatAnswer(text) {
        var safe = text
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;");

        var lines = safe.split("\n");
        var out = [];
        for (var i = 0; i < lines.length; i++) {
            var line = lines[i];
            var trimmed = line.trim();
            var isHeading =
                trimmed.length > 2 &&
                trimmed.length < 60 &&
                trimmed === trimmed.toUpperCase() &&
                /[A-Z]/.test(trimmed) &&
                !trimmed.startsWith("-") &&
                !/^\d+\./.test(trimmed);

            if (isHeading) {
                out.push('<span class="head-line">' + trimmed + "</span>");
            } else {
                out.push(line);
            }
        }
        return out.join("\n");
    }

    function scrollDown() {
        body.scrollTop = body.scrollHeight;
    }

    function addUserMessage(text) {
        var row = document.createElement("div");
        row.className = "msg user";
        row.innerHTML =
            '<div class="who">👤</div>' +
            '<div class="bubble"></div>';
        row.querySelector(".bubble").textContent = text;
        body.appendChild(row);
        scrollDown();
    }

    function addBotMessage(reply) {
        var row = document.createElement("div");
        row.className = "msg bot";

        var bubble = document.createElement("div");
        bubble.className = "bubble";
        bubble.innerHTML = formatAnswer(reply.answer);

        /* Footer: which pages the answer came from, and which engine wrote it */
        var foot = document.createElement("div");
        foot.className = "bubble-foot";

        var badge = document.createElement("span");
        badge.className = "pill " + (reply.engine === "ai" ? "green" : "gold");
        badge.textContent = reply.engine === "ai" ? "AI answer" : "Knowledge base";
        foot.appendChild(badge);

        if (reply.sources && reply.sources.length) {
            var label = document.createElement("span");
            label.textContent = "Read more:";
            foot.appendChild(label);
            reply.sources.slice(0, 3).forEach(function (source) {
                var link = document.createElement("a");
                link.href = source.url;
                link.textContent = source.title;
                foot.appendChild(link);
            });
        }
        bubble.appendChild(foot);

        row.innerHTML = '<div class="who">⚖️</div>';
        row.appendChild(bubble);
        body.appendChild(row);

        /* Follow-up suggestion chips */
        if (reply.suggestions && reply.suggestions.length) {
            var chips = document.createElement("div");
            chips.className = "chips";
            reply.suggestions.forEach(function (idea) {
                var chip = document.createElement("button");
                chip.className = "chip";
                chip.type = "button";
                chip.textContent = idea;
                chip.onclick = function () { send(idea); };
                chips.appendChild(chip);
            });
            body.appendChild(chips);
        }

        scrollDown();
        if (speakOn) { speak(reply.answer); }
    }

    function showTyping() {
        var row = document.createElement("div");
        row.className = "msg bot";
        row.id = "typingRow";
        row.innerHTML =
            '<div class="who">⚖️</div>' +
            '<div class="bubble"><div class="typing">' +
            "<span></span><span></span><span></span></div></div>";
        body.appendChild(row);
        scrollDown();
    }

    function hideTyping() {
        var row = document.getElementById("typingRow");
        if (row) { row.remove(); }
    }

    /* ================================================================== */
    /* PART 2 - TALKING TO THE SERVER                                     */
    /* ================================================================== */

    function send(text) {
        var message = (text !== undefined ? text : input.value).trim();
        if (!message || busy) { return; }

        busy = true;
        sendBtn.disabled = true;
        stopSpeaking();
        addUserMessage(message);
        input.value = "";
        input.style.height = "auto";
        showTyping();

        fetch("/api/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: message })
        })
            .then(function (response) { return response.json(); })
            .then(function (reply) {
                hideTyping();
                if (reply.error) {
                    addBotMessage({
                        answer: reply.error,
                        engine: "offline",
                        sources: [],
                        suggestions: []
                    });
                } else {
                    addBotMessage(reply);
                }
            })
            .catch(function () {
                hideTyping();
                addBotMessage({
                    answer:
                        "Sorry, I could not reach the server. Please check that " +
                        "the Flask application is still running and try again.",
                    engine: "offline",
                    sources: [],
                    suggestions: []
                });
            })
            .then(function () {
                busy = false;
                sendBtn.disabled = false;
                input.focus();
            });
    }

    /* Expose send() so the starter buttons in the HTML can call it */
    window.askLegalMitra = send;

    /* ================================================================== */
    /* PART 3 - TEXT TO SPEECH (the bot speaks)                           */
    /* ================================================================== */

    var synth = window.speechSynthesis;
    var voices = [];

    function loadVoices() {
        if (!synth) { return; }
        voices = synth.getVoices().filter(function (v) {
            return v.lang.indexOf("en") === 0;   // English voices only
        });
        if (!voiceBox) { return; }
        voiceBox.innerHTML = "";
        voices.forEach(function (voice, index) {
            var option = document.createElement("option");
            option.value = index;
            option.textContent = voice.name.replace(/Microsoft |Google /, "") +
                                 " (" + voice.lang + ")";
            /* Prefer an Indian English voice if the system has one */
            if (voice.lang === "en-IN") { option.selected = true; }
            voiceBox.appendChild(option);
        });
    }

    if (synth) {
        loadVoices();
        /* Chrome loads voices asynchronously, so we listen for them */
        if (typeof synth.onvoiceschanged !== "undefined") {
            synth.onvoiceschanged = loadVoices;
        }
    } else if (voiceNote) {
        voiceNote.textContent = "This browser cannot speak. Chrome or Edge is recommended.";
    }

    /* The answer contains bullets, dashes and headings that sound wrong when
       read literally, so we clean it before speaking. */
    function cleanForSpeech(text) {
        return text
            .replace(/^\s*[-*]\s*/gm, "")
            .replace(/\n{2,}/g, ". ")
            .replace(/\n/g, ", ")
            .replace(/\s{2,}/g, " ")
            .replace(/_/g, " ")
            .trim();
    }

    function speak(text) {
        if (!synth || !speakOn) { return; }
        stopSpeaking();

        var clean = cleanForSpeech(text);
        /* Some browsers cut off very long utterances, so we split the answer
           into sentence-sized chunks and queue them one after another. */
        var chunks = clean.match(/[^.!?]+[.!?]*/g) || [clean];
        var buffer = "";
        var queue = [];

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
            var utterance = new SpeechSynthesisUtterance(part.trim());
            if (voiceBox && voices.length) {
                var chosen = voices[parseInt(voiceBox.value, 10)];
                if (chosen) { utterance.voice = chosen; }
            }
            utterance.rate = rateBox ? parseFloat(rateBox.value) : 1;
            utterance.pitch = 1;
            utterance.volume = 1;
            synth.speak(utterance);
        });
    }

    function stopSpeaking() {
        if (synth && synth.speaking) { synth.cancel(); }
    }

    /* ================================================================== */
    /* PART 4 - SPEECH TO TEXT (the microphone)                           */
    /* ================================================================== */

    var Recognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    var recogniser = null;
    var listening = false;

    if (Recognition && micBtn) {
        recogniser = new Recognition();
        recogniser.lang = "en-IN";          // Indian English accent model
        recogniser.continuous = false;      // stop after one sentence
        recogniser.interimResults = true;   // show words as they are spoken

        recogniser.onstart = function () {
            listening = true;
            micBtn.classList.add("listening");
            micBtn.title = "Listening... click to stop";
            input.placeholder = "Listening... speak now";
        };

        recogniser.onresult = function (event) {
            var text = "";
            for (var i = event.resultIndex; i < event.results.length; i++) {
                text += event.results[i][0].transcript;
            }
            input.value = text;

            /* When the browser is confident the sentence is finished, send it */
            if (event.results[event.results.length - 1].isFinal) {
                setTimeout(function () { send(); }, 400);
            }
        };

        recogniser.onerror = function (event) {
            listening = false;
            micBtn.classList.remove("listening");
            input.placeholder = "Type your legal question...";
            if (event.error === "not-allowed") {
                alert("Microphone access was blocked. Please allow the microphone " +
                      "in your browser settings to use voice input.");
            }
        };

        recogniser.onend = function () {
            listening = false;
            micBtn.classList.remove("listening");
            micBtn.title = "Speak your question";
            input.placeholder = "Type your legal question...";
        };

        micBtn.addEventListener("click", function () {
            if (listening) {
                recogniser.stop();
            } else {
                stopSpeaking();          // do not listen to ourselves
                try { recogniser.start(); } catch (e) { /* already started */ }
            }
        });
    } else if (micBtn) {
        /* Browser has no speech recognition - hide the microphone */
        micBtn.style.display = "none";
        if (voiceNote) {
            voiceNote.textContent =
                "Voice input needs Chrome or Edge. You can still type your question.";
        }
    }

    /* ================================================================== */
    /* PART 5 - BUTTONS AND KEYBOARD                                      */
    /* ================================================================== */

    sendBtn.addEventListener("click", function () { send(); });

    /* Enter sends, Shift+Enter makes a new line */
    input.addEventListener("keydown", function (event) {
        if (event.key === "Enter" && !event.shiftKey) {
            event.preventDefault();
            send();
        }
    });

    /* Grow the text box as the user types */
    input.addEventListener("input", function () {
        input.style.height = "auto";
        input.style.height = Math.min(input.scrollHeight, 130) + "px";
    });

    if (speakBtn) {
        speakBtn.addEventListener("click", function () {
            speakOn = !speakOn;
            speakBtn.classList.toggle("on", speakOn);
            speakBtn.title = speakOn ? "Voice replies are ON" : "Voice replies are OFF";
            speakBtn.textContent = speakOn ? "🔊" : "🔇";
            if (!speakOn) { stopSpeaking(); }
        });
        speakBtn.classList.add("on");
    }

    if (stopBtn) {
        stopBtn.addEventListener("click", stopSpeaking);
    }

    if (clearBtn) {
        clearBtn.addEventListener("click", function () {
            if (!confirm("Clear this conversation and start fresh?")) { return; }
            stopSpeaking();
            fetch("/api/clear", { method: "POST" }).then(function () {
                body.innerHTML = "";
                addBotMessage({
                    answer:
                        "New conversation started.\n\nAsk me anything about Indian " +
                        "law - your rights, a procedure, a deadline, or a document " +
                        "format you need.",
                    engine: "offline",
                    sources: [],
                    suggestions: [
                        "What are my fundamental rights?",
                        "How do I file an FIR?",
                        "Give me a rent agreement format",
                        "What is anticipatory bail?"
                    ]
                });
            });
        });
    }

    /* Stop the voice if the user leaves the page */
    window.addEventListener("beforeunload", stopSpeaking);

    /* ================================================================== */
    /* PART 6 - THE OPENING GREETING                                      */
    /* ================================================================== */

    window.addEventListener("load", function () {
        setTimeout(function () {
            addBotMessage({
                answer:
                    "Namaste! I am LegalMitra, your legal information assistant.\n\n" +
                    "I can explain any area of law - criminal, civil, property, " +
                    "company, contract, labour, intellectual property, cyber, " +
                    "family, consumer, tax, banking, motor vehicle, environment, " +
                    "infrastructure, medical, education and international law - " +
                    "and I can give you ready-to-use document formats.\n\n" +
                    "You can type your question, or press the microphone and " +
                    "simply speak.",
                engine: "offline",
                sources: [],
                suggestions: [
                    "What are my rights if I am arrested?",
                    "My landlord is not returning my deposit",
                    "How do I register a trademark?",
                    "Give me a rent agreement format"
                ]
            });
            input.focus();
        }, 350);
    });
})();
