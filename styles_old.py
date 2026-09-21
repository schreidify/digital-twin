"""Styling constants for the digital twin Gradio app — Bothy Book world."""

COVER = "#2F3D32"
PAPER = "#E6E1D6"
GRAPHITE = "#3A3A38"
STAMP = "#C45C26"
MOSS = "#8A9A8E"

EXAMPLES = [
    "Tell me about your background and experience.",
    "What kinds of projects are you working on now?",
    "What are your strongest skills?",
    "How can I get in touch with you?",
]

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,600;1,7..72,400&family=Zilla+Slab:wght@500;600;700&display=swap');

:root {
  --bothy-cover: #2F3D32;
  --bothy-cover-deep: #243028;
  --bothy-paper: #E6E1D6;
  --bothy-paper-edge: #C9BFAE;
  --bothy-rule: rgba(58, 58, 56, 0.16);
  --bothy-margin-rule: rgba(196, 92, 38, 0.28);
  --bothy-graphite: #3A3A38;
  --bothy-muted: #6B6B66;
  --bothy-stamp: #C45C26;
  --bothy-stamp-ink: #A3481C;
  --bothy-moss: #8A9A8E;
  --bothy-spine: #1E2821;
  --bothy-bg: #CABC9E;
  --bothy-cover-type: #E6E1D6;
  --bothy-room-label: rgba(230, 225, 214, 0.72);
}

/* Evening Bothy: room darkens; the paper page stays paper.
   Variables must live on html too — body.dark alone does not update html's --bothy-bg. */
html:has(body.dark),
body.dark {
  --bothy-bg: #141A16;
  --bothy-cover: #2F3D32;
  --bothy-cover-deep: #243028;
  --bothy-spine: #0E1210;
  --bothy-cover-type: #E6E1D6;
  --bothy-room-label: rgba(230, 225, 214, 0.65);
}

footer, .built-with, .show-api, .api-docs,
button.show-api { display: none !important; }

html, body, gradio-app {
  background:
    radial-gradient(ellipse 120% 70% at 50% -20%, rgba(47, 61, 50, 0.22), transparent 50%),
    var(--bothy-bg) !important;
  color: var(--bothy-graphite) !important;
}

/* ---------- Notebook shell (waterproof cover) ---------- */
.gradio-container {
  background:
    linear-gradient(90deg, rgba(0,0,0,0.18) 0 14px, transparent 14px),
    var(--bothy-cover) !important;
  color: var(--bothy-graphite) !important;
  font-family: 'Literata', Georgia, 'Times New Roman', serif !important;
  width: 100% !important;
  max-width: 720px !important;
  min-width: 0 !important;
  margin: 28px auto !important;
  padding: 22px 20px 26px !important;
  border-radius: 5px 12px 12px 5px !important;
  box-shadow:
    -12px 0 0 var(--bothy-spine),
    0 22px 48px rgba(14, 18, 16, 0.35),
    inset 0 1px 0 rgba(255, 255, 255, 0.1) !important;
  position: relative !important;
  overflow: visible !important;
}
.gradio-container::before {
  content: attr(data-bothy-room);
  position: absolute;
  top: 12px;
  right: 18px;
  font-family: 'Barlow Condensed', 'Arial Narrow', sans-serif;
  font-weight: 700;
  font-size: 11px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--bothy-room-label);
  pointer-events: none;
  z-index: 5;
}
.gradio-container .main,
.gradio-container .contain,
.gradio-container .wrap,
.gradio-container .fillable,
.gradio-container .column {
  width: 100% !important;
  max-width: 100% !important;
  min-width: 0 !important;
  background: transparent !important;
}
.gradio-container * { min-width: 0; }

/* ---------- Title on the cover ---------- */
.gradio-container h1 {
  color: var(--bothy-cover-type) !important;
  font-family: 'Zilla Slab', Georgia, serif !important;
  font-size: 28px !important;
  font-weight: 600 !important;
  font-style: normal !important;
  letter-spacing: -0.015em !important;
  line-height: 1.2 !important;
  border: 0 !important;
  padding: 10px 8px 2px !important;
  margin: 8px 0 0 !important;
  text-align: left !important;
}
.gradio-container .prose,
.gradio-container [data-testid="markdown"],
.gradio-container [data-testid="markdown"] span,
.gradio-container .md {
  color: rgba(230, 225, 214, 0.8) !important;
  font-family: 'Literata', Georgia, serif !important;
  font-size: 14px !important;
  font-style: italic !important;
  background: transparent !important;
}
.gradio-container [data-testid="markdown"] h1 + *,
.gradio-container .prose p,
.gradio-container .md p {
  color: rgba(230, 225, 214, 0.8) !important;
  padding: 0 8px 14px !important;
  margin: 0 !important;
}

.block, .form {
  background: transparent !important;
  box-shadow: none !important;
  border: 0 !important;
}

/* ---------- Ruled page: Gradio 5 uses .bubble-wrap, not .chatbot ---------- */
.bubble-wrap,
.wrapper:has(> .bubble-wrap),
div.block:has(.bubble-wrap),
div.block:has(.wrapper) {
  background:
    url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0.35 0 0 0 0 0.32 0 0 0 0 0.28 0 0 0 0.045 0'/%3E%3C/filter%3E%3Crect width='180' height='180' filter='url(%23n)'/%3E%3C/svg%3E"),
    repeating-linear-gradient(
      transparent,
      transparent 27px,
      var(--bothy-rule) 27px,
      var(--bothy-rule) 28px
    ),
    linear-gradient(
      90deg,
      transparent 36px,
      var(--bothy-margin-rule) 36px,
      var(--bothy-margin-rule) 37px,
      transparent 37px
    ),
    var(--bothy-paper) !important;
  background-blend-mode: multiply, normal, normal, normal !important;
  border: 1px solid var(--bothy-paper-edge) !important;
  border-radius: 3px !important;
  box-shadow:
    inset 0 0 0 1px rgba(255, 255, 255, 0.35),
    0 1px 0 rgba(0, 0, 0, 0.12) !important;
  min-height: 420px !important;
  color: var(--bothy-graphite) !important;
}
.bubble-wrap {
  padding: 8px 4px 12px !important;
  overflow-y: auto !important;
}
.bubble-wrap .placeholder,
.bubble-wrap .placeholder * {
  color: var(--bothy-muted) !important;
  font-family: 'Literata', Georgia, serif !important;
  font-style: italic !important;
}

/* Soft corners on controls */
button, input, textarea, .examples button {
  border-radius: 3px !important;
}

/* ---------- Message rows ---------- */
.message-row,
.message-row > div,
.message-row .role,
.message-wrap,
.bubble-wrap > div {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
}

.bubble-wrap .message,
.bubble-wrap .bot,
.bubble-wrap .user,
.message-row .message,
.message-row .message-bubble,
.message-row .bubble {
  border: 0 !important;
  box-shadow: none !important;
  background: transparent !important;
  border-radius: 0 !important;
  padding: 6px 14px 6px 48px !important;
  color: var(--bothy-graphite) !important;
  font-family: 'Literata', Georgia, serif !important;
  font-size: 15px !important;
  line-height: 28px !important;
  animation: bothy-write 0.45s cubic-bezier(0.16, 1, 0.3, 1) both;
}

/* Visitor: pencil italic */
.bubble-wrap .user,
.message-row.user-row .message,
.message-row.user-row .message-bubble,
.message-row.user-row .bubble,
.message-row[data-role="user"] .message,
.message-row[data-role="user"] .message-bubble {
  font-style: italic !important;
}

/* Twin: upright ink + rubber stamp */
.bubble-wrap .bot,
.message-row.bot-row .message,
.message-row.bot-row .message-bubble,
.message-row.bot-row .bubble,
.message-row[data-role="assistant"] .message,
.message-row[data-role="assistant"] .message-bubble {
  font-style: normal !important;
  position: relative !important;
}

.bubble-wrap .bot::before,
.message-row.bot-row .message::before,
.message-row.bot-row .bubble::before,
.message-row.bot-row .message-bubble::before,
.message-row[data-role="assistant"] .message::before,
.message-row[data-role="assistant"] .bubble::before,
.message-row[data-role="assistant"] .message-bubble::before {
  content: "JR";
  position: absolute;
  left: 8px;
  top: 8px;
  width: 28px;
  height: 28px;
  border: 1.5px solid var(--bothy-stamp);
  border-radius: 50%;
  color: var(--bothy-stamp);
  font-family: 'Barlow Condensed', 'Arial Narrow', sans-serif;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.04em;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0.9;
  transform: rotate(-8deg);
  pointer-events: none;
  font-style: normal !important;
}

.message-row.bot-row .message .message::before,
.message-row.bot-row .message .bubble::before,
.message-row.bot-row .message .message-bubble::before,
.message-row.bot-row .bubble .message::before,
.message-row.bot-row .bubble .bubble::before,
.message-row.bot-row .bubble .message-bubble::before,
.message-row.bot-row .message-bubble .message::before,
.message-row.bot-row .message-bubble .bubble::before,
.message-row.bot-row .message-bubble .message-bubble::before,
.message-row[data-role="assistant"] .message .message::before,
.message-row[data-role="assistant"] .message .bubble::before,
.message-row[data-role="assistant"] .message .message-bubble::before,
.message-row[data-role="assistant"] .bubble .message::before,
.message-row[data-role="assistant"] .bubble .bubble::before,
.message-row[data-role="assistant"] .bubble .message-bubble::before,
.message-row[data-role="assistant"] .message-bubble .message::before,
.message-row[data-role="assistant"] .message-bubble .bubble::before,
.message-row[data-role="assistant"] .message-bubble .message-bubble::before,
.bubble-wrap .bot .bot::before {
  content: none !important;
  display: none !important;
}

.bubble-wrap .message p,
.bubble-wrap .bot p,
.bubble-wrap .user p,
.message-row .message p,
.message-row .message-bubble p,
.message-row .bubble p,
.message-row .prose p {
  font-size: 15px !important;
  line-height: 28px !important;
  margin: 0 !important;
  color: inherit !important;
  background: transparent !important;
}
.bubble-wrap .message p + p,
.bubble-wrap .bot p + p,
.message-row .message p + p,
.message-row .prose p + p {
  margin-top: 28px !important;
}

.bubble-wrap .message *,
.bubble-wrap .bot *,
.bubble-wrap .user *,
.message-row .message *,
.message-row .message-bubble *,
.message-row .bubble * {
  background: transparent !important;
  box-shadow: none !important;
  color: inherit !important;
}
.bubble-wrap a,
.message-row .message a,
.message-row .message-bubble a {
  color: var(--bothy-stamp) !important;
  text-decoration: underline;
  text-underline-offset: 3px;
}

@keyframes bothy-write {
  from {
    opacity: 0;
    filter: blur(2px);
    transform: translateY(4px);
  }
  to {
    opacity: 1;
    filter: blur(0);
    transform: translateY(0);
  }
}

/* ---------- Input: pencil on paper slip ---------- */
.input-row,
.gr-input-row,
.chat-input-row,
form[class*="input"],
div.block:has(textarea),
div.block:has([data-testid="textbox"]),
form:has(textarea),
.contain form {
  align-items: stretch !important;
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
}
div.block:has(textarea) > *,
form:has(textarea) > * {
  background: transparent !important;
  border-color: transparent !important;
}

textarea,
input[type="text"],
[data-testid="textbox"] textarea {
  background: var(--bothy-paper) !important;
  border: 1px solid var(--bothy-paper-edge) !important;
  border-bottom: 2px solid var(--bothy-moss) !important;
  color: var(--bothy-graphite) !important;
  font-family: 'Literata', Georgia, serif !important;
  font-size: 15px !important;
  font-style: italic !important;
  padding: 12px 14px !important;
  line-height: 1.45 !important;
  min-height: 52px !important;
  border-radius: 3px !important;
  box-shadow: none !important;
}
textarea:focus,
input[type="text"]:focus,
[data-testid="textbox"] textarea:focus {
  border-color: var(--bothy-stamp) !important;
  border-bottom-color: var(--bothy-stamp) !important;
  outline: none !important;
  box-shadow: 0 2px 0 var(--bothy-stamp) !important;
}
textarea::placeholder,
input::placeholder {
  color: var(--bothy-muted) !important;
  font-style: italic !important;
}

/* ---------- Stamp buttons ---------- */
button {
  font-family: 'Barlow Condensed', 'Arial Narrow', sans-serif !important;
  letter-spacing: 0.14em !important;
  text-transform: uppercase !important;
  font-size: 13px !important;
  font-weight: 700 !important;
  border: 1.5px solid rgba(230, 225, 214, 0.45) !important;
  background: transparent !important;
  color: var(--bothy-cover-type) !important;
  padding: 0 16px !important;
  min-height: 52px !important;
  align-self: stretch !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  cursor: pointer;
  border-radius: 3px !important;
  transition:
    background 0.14s ease,
    color 0.14s ease,
    border-color 0.14s ease,
    transform 0.12s cubic-bezier(0.16, 1, 0.3, 1),
    box-shadow 0.12s ease;
}
button:hover {
  border-color: var(--bothy-cover-type) !important;
  background: rgba(230, 225, 214, 0.08) !important;
}
button:active {
  transform: scale(0.96) rotate(-1deg) !important;
}

button.primary,
button[variant="primary"],
button.submit,
button.submit-button,
.submit-button,
button.lg.primary,
[data-testid="submit-button"] {
  background: var(--bothy-stamp) !important;
  border: 2px solid var(--bothy-stamp-ink) !important;
  color: #F7F1E8 !important;
  min-height: 52px !important;
  min-width: 72px !important;
  padding: 0 14px !important;
  box-shadow:
    0 1px 0 rgba(0, 0, 0, 0.22),
    inset 0 0 0 1px rgba(247, 241, 232, 0.18) !important;
  position: relative !important;
  font-family: 'Barlow Condensed', 'Arial Narrow', sans-serif !important;
  font-size: 15px !important;
  font-weight: 700 !important;
  letter-spacing: 0.2em !important;
  text-transform: uppercase !important;
}
/* Rubber-stamp wordmark — hide Gradio's paper-plane SVG */
button.submit svg,
button.submit-button svg,
.submit-button svg,
[data-testid="submit-button"] svg,
button.primary svg {
  display: none !important;
}
[data-testid="submit-button"]::after,
button.submit-button::after,
.submit-button::after {
  content: "SEND";
  font-family: 'Barlow Condensed', 'Arial Narrow', sans-serif;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: 0.2em;
  color: #F7F1E8;
  line-height: 1;
}
button.primary:hover,
button.submit:hover,
.submit-button:hover,
[data-testid="submit-button"]:hover {
  background: var(--bothy-stamp-ink) !important;
  border-color: var(--bothy-stamp-ink) !important;
  color: #F7F1E8 !important;
}
button.primary:active,
button.submit:active,
.submit-button:active,
[data-testid="submit-button"]:active {
  transform: scale(0.94) rotate(-2deg) !important;
  box-shadow: inset 0 0 0 2px rgba(247, 241, 232, 0.45) !important;
}

/* ---------- Prompt stamps live ON the ruled page (Gradio empty state) ---------- */
.examples,
.examples-holder,
[data-testid="examples"],
.bubble-wrap .examples {
  background: transparent !important;
  padding: 8px 6px !important;
  margin: 0 !important;
}
.examples table,
.examples-table { background: transparent !important; border: 0 !important; }
.examples button,
.example,
.examples td button,
[data-testid="examples"] button,
.bubble-wrap .example {
  background: rgba(196, 92, 38, 0.06) !important;
  border: 2px solid rgba(58, 58, 56, 0.55) !important;
  box-shadow: inset 0 0 0 1px rgba(196, 92, 38, 0.22) !important;
  color: var(--bothy-graphite) !important;
  text-transform: none !important;
  letter-spacing: 0.01em !important;
  font-family: 'Literata', Georgia, serif !important;
  font-size: 13px !important;
  font-weight: 400 !important;
  font-style: italic !important;
  padding: 10px 14px !important;
  text-align: left !important;
  min-height: 0 !important;
  align-self: auto !important;
  display: inline-block !important;
  border-radius: 2px !important;
  transform: rotate(-0.4deg) !important;
}
.examples button:nth-child(even),
.example:nth-child(even),
.bubble-wrap .example:nth-child(even) {
  transform: rotate(0.55deg) !important;
}
.examples button:hover,
.example:hover,
[data-testid="examples"] button:hover,
.bubble-wrap .example:hover {
  border-color: var(--bothy-stamp) !important;
  color: var(--bothy-stamp-ink) !important;
  background: rgba(196, 92, 38, 0.12) !important;
  box-shadow: inset 0 0 0 1px rgba(196, 92, 38, 0.35) !important;
  transform: rotate(0deg) scale(1.01) !important;
}

.icon-button,
.bubble-wrap .icon-button {
  color: var(--bothy-muted) !important;
  background: transparent !important;
  border: 0 !important;
  min-height: 0 !important;
  padding: 4px !important;
  letter-spacing: 0 !important;
  text-transform: none !important;
}
.icon-button:hover {
  color: var(--bothy-stamp) !important;
  transform: none !important;
}

::-webkit-scrollbar { width: 10px; height: 10px; }
::-webkit-scrollbar-track { background: var(--bothy-cover-deep); }
::-webkit-scrollbar-thumb { background: var(--bothy-moss); border-radius: 2px; }
::-webkit-scrollbar-thumb:hover { background: var(--bothy-stamp); }

::selection { background: var(--bothy-stamp); color: #F7F1E8; }

:focus-visible {
  outline: 2px solid var(--bothy-stamp) !important;
  outline-offset: 2px !important;
}

@media (max-width: 640px) {
  .gradio-container {
    margin: 12px 10px 24px !important;
    padding: 16px 12px 20px !important;
    border-radius: 4px 8px 8px 4px !important;
    box-shadow:
      -7px 0 0 var(--bothy-spine),
      0 14px 32px rgba(14, 18, 16, 0.4) !important;
  }
  .gradio-container h1 { font-size: 22px !important; }
  .gradio-container::before { font-size: 10px; right: 12px; top: 10px; }
  .bubble-wrap .message,
  .bubble-wrap .bot,
  .bubble-wrap .user,
  .message-row .message,
  .message-row .message-bubble,
  .message-row .bubble {
    padding-left: 42px !important;
  }
  .bubble-wrap,
  .wrapper:has(> .bubble-wrap),
  div.block:has(.bubble-wrap) {
    min-height: 340px !important;
  }
}
"""

JS = """
() => {
  document.title = 'Jen Reid-Schram (Digital Twin)';

  const syncRoom = () => {
    const root = document.querySelector('.gradio-container');
    if (!root) return;
    const evening = document.body.classList.contains('dark');
    root.dataset.bothyRoom = evening ? 'Evening Wall' : 'Morning Wall';
  };
  syncRoom();
  new MutationObserver(syncRoom).observe(document.body, {
    attributes: true,
    attributeFilter: ['class'],
  });
  // Gradio remounts the container; keep the label attached.
  new MutationObserver(syncRoom).observe(document.body, {
    childList: true,
    subtree: true,
  });

  const focusInput = () => {
    const areas = document.querySelectorAll('textarea');
    if (areas.length) areas[areas.length - 1].focus();
  };
  setTimeout(focusInput, 300);

  const watchTextarea = (area) => {
    if (area.dataset.twinWatched) return;
    area.dataset.twinWatched = '1';
    let wasDisabled = area.disabled || area.readOnly;
    new MutationObserver(() => {
      const isDisabled = area.disabled || area.readOnly;
      if (wasDisabled && !isDisabled) area.focus();
      wasDisabled = isDisabled;
    }).observe(area, { attributes: true, attributeFilter: ['disabled', 'readonly'] });
  };

  const scan = () => document.querySelectorAll('textarea').forEach(watchTextarea);
  setTimeout(scan, 500);
  new MutationObserver(scan).observe(document.body, { childList: true, subtree: true });
}
"""
