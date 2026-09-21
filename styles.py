"""Styling constants for the digital twin Gradio app: mint-moss with fluorescent pink.

Design essentials: one big name with an outlined mirror of itself under it, a
twin mark made of three bars (solid + outlined mirror), questions set as
headlines, answers set as book text, 6px radii, 1px rules, no texture.
"""

from urllib.parse import quote

# ---------------------------------------------------------------------------
# Palette (single source of truth; the CSS variables below are built from it)
# ---------------------------------------------------------------------------
GROUND = "#E2F7E4"   # mint, behind everything
PAGE = "#F8FFE9"     # page surface
PAPER = "#F4FCF4"    # chips
BAR = "#F6F7E2"      # composer bar
INK = "#14240E"      # text, rules that matter, send button
MUTED = "#5C6B57"    # labels, placeholder (5.2:1 on every surface)
RULE = "#C0D4C0"     # hairlines
EDGE = "#7C8B7A"     # chip borders, echo outline
FIELD_EDGE = "#9CA89A"
PINK = "#FE3895"     # logo, underline, hover, focus. Never used as text colour.
PINK_WASH = "rgba(254, 56, 149, 0.16)"

# Names from the previous "Bothy Book" file, kept so existing imports don't break.
COVER, GRAPHITE, STAMP, MOSS = INK, INK, PINK, MUTED

EXAMPLES = [
    "Tell me about your background and experience.",
    "What kinds of projects are you working on now?",
    "What are your strongest skills?",
    "How can I get in touch with you?",
]


DISPLAY = "'Bricolage Grotesque', 'Helvetica Neue', sans-serif"
BODY = "'Source Serif 4', Georgia, serif"
MONO = "'JetBrains Mono', ui-monospace, Menlo, monospace"


def _mark(fill: str, stroke: str) -> str:
    """The twin mark as a CSS url(): three solid bars and their outlined mirror."""
    bars = "<path d='M0 0H45.9V20H0z'/><path d='M0 30H70V50H0z'/><path d='M0 60H65.2V80H0z'/>"
    svg = (
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='-2 -2 178 84'>"
        f"<g fill='{fill}'>{bars}</g>"
        f"<g fill='none' stroke='{stroke}' stroke-width='2.4' "
        f"transform='translate(174 0) scale(-1 1)'>{bars}</g></svg>"
    )
    return f'url("data:image/svg+xml,{quote(svg)}")'


# The up-arrow on the send button, drawn as a mask so it takes the button's colour.
_ARROW = (
    "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20' fill='none' "
    "stroke='black' stroke-width='1.75' stroke-linecap='square'>"
    "<path d='M10 16V4M5 9l5-5 5 5'/></svg>"
)
_ARROW_URL = f'url("data:image/svg+xml,{quote(_ARROW)}")'

_FONTS = (
    "@import url('https://fonts.googleapis.com/css2?"
    "family=Bricolage+Grotesque:wght@400;600;700"
    "&family=Source+Serif+4:ital,wght@0,400;0,500;1,400"
    "&family=JetBrains+Mono:wght@400;500&display=swap');\n"
)

# The design is light only, so the same values are applied under .dark as well.
# The Gradio variables (--body-background-fill and friends) do most of the work;
# the rules further down cover what variables can't reach.
_VARS = f"""
:root, .dark, body.dark, html:has(body.dark) {{
  --tw-ground: {GROUND};
  --tw-page: {PAGE};
  --tw-paper: {PAPER};
  --tw-bar: {BAR};
  --tw-ink: {INK};
  --tw-muted: {MUTED};
  --tw-rule: {RULE};
  --tw-edge: {EDGE};
  --tw-field-edge: {FIELD_EDGE};
  --tw-pink: {PINK};
  --tw-pink-wash: {PINK_WASH};
  --tw-mark: {_mark(PINK, INK)};
  --tw-display: {DISPLAY};
  --tw-body: {BODY};
  --tw-mono: {MONO};

  /* Gradio's own tokens */
  --body-background-fill: {PAGE};
  --body-text-color: {INK};
  --body-text-color-subdued: {MUTED};
  --background-fill-primary: {PAGE};
  --background-fill-secondary: {PAGE};
  --block-background-fill: transparent;
  --block-border-width: 0px;
  --block-shadow: none;
  --block-label-text-color: {MUTED};
  --border-color-primary: {RULE};
  --border-color-accent: {PINK};
  --color-accent: {PINK};
  --link-text-color: {INK};
  --link-text-color-hover: {INK};
  --link-text-color-active: {INK};
  --link-text-color-visited: {INK};
  --input-background-fill: #FFFFFF;
  --input-background-fill-focus: #FFFFFF;
  --input-border-color: {FIELD_EDGE};
  --input-border-color-focus: {FIELD_EDGE};
  --input-border-width: 1px;
  --input-radius: 6px;
  --input-shadow: none;
  --input-shadow-focus: none;
  --input-placeholder-color: {MUTED};
  --button-large-radius: 6px;
  --button-small-radius: 6px;
  --button-primary-background-fill: {INK};
  --button-primary-background-fill-hover: {PINK};
  --button-primary-text-color: {GROUND};
  --button-primary-text-color-hover: {INK};
  --button-primary-border-color: transparent;
  --button-primary-border-color-hover: transparent;
  --font: {BODY};
  --font-mono: {MONO};
}}
"""

_RULES = """
footer, .built-with, .show-api, .api-docs, button.show-api { display: none !important; }

html, body, gradio-app {
  background: var(--tw-page) !important;
  color: var(--tw-ink) !important;
  -webkit-font-smoothing: antialiased;
}

/* ---------- Page and masthead ---------- */
.gradio-container {
  position: relative !important;
  width: 100% !important;
  max-width: 1200px !important;
  margin: 0 auto !important;
  padding: 0 clamp(16px, 4vw, 48px) !important;
  overflow: visible !important;  /* lets the composer bar run edge to edge */
  background: transparent !important;
  color: var(--tw-ink) !important;
  font-family: var(--tw-body) !important;
}
.gradio-container::before {
  content: "Digital twin";
  display: block;
  box-sizing: border-box;
  height: 56px;
  border-bottom: 1px solid var(--tw-rule);
  font: 500 12px/56px var(--tw-mono);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--tw-muted);
}
.gradio-container main,
.gradio-container .main,
.gradio-container .wrap,
.gradio-container .contain,
.gradio-container .fillable,
.gradio-container .column {
  width: 100% !important;
  max-width: 100% !important;
  min-width: 0 !important;
  background: transparent !important;
}
.gradio-container main,
.gradio-container .main { padding: 0 !important; }
.gradio-container * { min-width: 0; }
html, body { overflow-x: clip; }

.block, .form, .styler {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
}

/* Optional header links: gr.HTML('<nav class="twin-nav"><a href="...">Résumé (PDF)</a></nav>') */
.twin-nav {
  position: absolute;
  top: 0;
  right: clamp(16px, 4vw, 48px);
  height: 56px;
  display: flex;
  align-items: center;
  gap: 32px;
  font: 500 13px/1 var(--tw-mono);
}

a, .gradio-container a {
  color: var(--tw-ink) !important;
  text-decoration: underline !important;
  text-decoration-color: var(--tw-pink) !important;
  text-decoration-thickness: 3px !important;
  text-underline-offset: 4px !important;
}
a:hover, .gradio-container a:hover {
  background: var(--tw-pink);
  color: var(--tw-ink) !important;
}

/* ---------- The name, with its outlined echo ----------
   The JS below copies the heading text into data-echo and wraps each word in a
   nowrap span, so "Reid-Schram" never breaks at the hyphen. */
.gradio-container h1 {
  position: relative;
  display: block;
  margin: 32px 0 0 !important;
  padding: 0 0 0.58em !important;
  overflow: hidden;
  border: 0 !important;
  text-align: left !important;
  color: var(--tw-ink) !important;
  font: 700 clamp(46px, 11.2vw, 132px)/0.94 var(--tw-display) !important;
  letter-spacing: -0.04em !important;
}
.gradio-container h1::after {
  content: attr(data-echo);
  position: absolute;
  left: 0;
  bottom: -0.217em;
  line-height: 0.94;
  white-space: nowrap;
  color: var(--tw-page);
  -webkit-text-stroke: 2px var(--tw-edge);
  paint-order: stroke fill;
  -webkit-mask-image: linear-gradient(to top, #000 0%, rgba(0, 0, 0, 0) 76%);
  mask-image: linear-gradient(to top, #000 0%, rgba(0, 0, 0, 0) 76%);
  transform: scaleY(-1);
  pointer-events: none;
}
.gradio-container .prose[data-testid="markdown"] p {
  max-width: 620px;
  margin: 28px 0 0 !important;
  padding: 0 !important;
  color: var(--tw-ink) !important;
  font: 400 20px/1.55 var(--tw-body) !important;
  font-style: normal !important;
  text-wrap: pretty;
}

/* ---------- The page the conversation happens on ---------- */
[data-testid="block-label"], .block-label { display: none !important; }

.bubble-wrap,
.wrapper:has(> .bubble-wrap),
div.block:has(.bubble-wrap),
.message-wrap {
  background: #FFFFFF !important;
  border: 0 !important;
  box-shadow: none !important;
  color: var(--tw-ink) !important;
}
.bubble-wrap {
  padding: 24px 0 24px !important;
  overflow-y: auto !important;
}
div.block:has(.bubble-wrap) { min-height: 46vh !important; }

/* Empty state: headline, then chips */
.placeholder-content {
  align-items: flex-start !important;
  justify-content: flex-start !important;
  height: auto !important;
  padding: 0 !important;
  text-align: left !important;
}
.placeholder-content .placeholder {
  display: flex !important;
  flex-direction: column !important;
  align-items: flex-start !important;
  justify-content: flex-start !important;
  text-align: left !important;
  padding: 0 !important;
}
.placeholder-content .placeholder::before {
  content: "";
  display: block;
  width: 120px;
  aspect-ratio: 178 / 84;
  margin-bottom: 28px;
  background-image: var(--tw-mark);
  background-repeat: no-repeat;
  background-position: left center;
  background-size: contain;
}
.placeholder-content .placeholder h2,
.placeholder-content .placeholder .prose h2 {
  max-width: 600px;
  margin: 0 !important;
  color: var(--tw-ink) !important;
  font: 600 clamp(28px, 4.4vw, 42px)/1.08 var(--tw-display) !important;
  font-style: normal !important;
  letter-spacing: -0.02em !important;
  text-wrap: balance;
}
.examples {
  display: flex !important;
  flex-wrap: wrap;
  gap: 10px !important;
  justify-content: flex-start !important;
  margin: 28px 0 0 !important;
  padding: 0 !important;
  background: transparent !important;
}
.examples::before {
  content: "Or start here";
  flex: 0 0 100%;
  margin-bottom: 2px;
  font: 500 12px/1.2 var(--tw-mono);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--tw-muted);
}
button.example, .examples button {
  box-sizing: border-box;
  width: auto !important;
  min-height: 44px !important;
  padding: 11px 16px !important;
  background: var(--tw-paper) !important;
  color: var(--tw-ink) !important;
  border: 1px solid var(--tw-edge) !important;
  border-radius: 6px !important;
  box-shadow: none !important;
  font: 500 15px/1.25 var(--tw-display) !important;
  letter-spacing: 0 !important;
  text-align: left !important;
  text-transform: none !important;
  cursor: pointer;
  transform: none !important;
}
button.example *, .examples button * {
  font: inherit !important;
  color: inherit !important;
  text-align: left !important;
}
button.example:hover, .examples button:hover {
  background: var(--tw-ink) !important;
  color: var(--tw-ground) !important;
  border-color: var(--tw-ink) !important;
}

/* ---------- Messages: label rail on the left, text beside it ---------- */
.message-wrap { gap: 0 !important; }
.message-row {
  position: relative;
  align-self: stretch !important;
  width: 100% !important;
  max-width: 100% !important;
  margin: 0 !important;
  padding: 0 0 0 152px !important;
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
}
.message-row.user-row { margin-top: 44px !important; }
.message-row.user-row:first-child { margin-top: 0 !important; }
.message-row.bot-row { margin-top: 20px !important; }
.message-row::before {
  position: absolute;
  left: 0;
  top: 10px;
  font: 500 12px/1.2 var(--tw-mono);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--tw-muted);
}
.message-row.user-row::before { content: "You"; }
.message-row.bot-row::before {
  content: "Twin";
  top: 6px;
  width: 64px;
  padding-bottom: 34px;
  background-image: var(--tw-mark);
  background-repeat: no-repeat;
  background-position: 0 26px;
  background-size: 44px 21px;
}

.message-row .flex-wrap,
.message-row .message,
.message-row .message > div {
  width: 100% !important;
  max-width: 100% !important;
  margin: 0 !important;
  padding: 0 !important;
  background: transparent !important;
  border: 0 !important;
  border-radius: 0 !important;
  box-shadow: none !important;
}
.message-row .message-content,
.message-row .prose,
.message-row span.md {
  opacity: 1 !important;
  background: transparent !important;
  color: var(--tw-ink) !important;
  max-width: 640px;
}

/* Visitor: the question, set as a headline */
.message-row.user-row .message-content,
.message-row.user-row .prose,
.message-row.user-row .prose p {
  font: 600 clamp(24px, 3vw, 32px)/1.16 var(--tw-display) !important;
  letter-spacing: -0.02em !important;
  text-wrap: balance;
}
/* Twin: the answer, set as book text */
.message-row.bot-row .message-content,
.message-row.bot-row .prose,
.message-row.bot-row .prose p,
.message-row.bot-row .prose li {
  font: 400 19px/1.62 var(--tw-body) !important;
  font-style: normal !important;
  text-wrap: pretty;
}
.message-row .prose p { margin: 0 !important; color: inherit !important; background: transparent !important; }
.message-row .prose p + p { margin-top: 18px !important; }
.message-row .prose ul, .message-row .prose ol { margin: 18px 0 0 !important; padding-left: 1.3em !important; }
.message-row .prose strong { font-weight: 600; }
.message-row .prose code,
.message-row .prose pre {
  font-family: var(--tw-mono) !important;
  font-size: 14px !important;
  background: var(--tw-paper) !important;
  border: 1px solid var(--tw-rule) !important;
  border-radius: 6px !important;
}
.message-row .prose code { padding: 1px 5px !important; }
.message-row .prose pre { padding: 12px 14px !important; }
.message-row .prose pre code { padding: 0 !important; border: 0 !important; }

/* Optional source note inside an answer:
   '<div class="twin-source"><b>Source · Résumé</b>Cirium: VP, Technology</div>' */
.message-row .twin-source {
  display: block;
  max-width: 320px;
  margin-top: 20px;
  padding-top: 10px;
  border-top: 1px solid var(--tw-ink);
  font: 400 15px/1.4 var(--tw-body);
}
.message-row .twin-source b {
  display: block;
  margin-bottom: 6px;
  font: 500 12px/1.2 var(--tw-mono);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--tw-muted);
}

.message-wrap .message-buttons { margin: 6px 0 0 152px !important; padding: 0 !important; }

/* Copy / retry / clear icons stay quiet */
.icon-button, .icon-button-wrapper button, .message-buttons button {
  background: transparent !important;
  color: var(--tw-muted) !important;
  border: 0 !important;
  box-shadow: none !important;
}
.icon-button:hover, .message-buttons button:hover { color: var(--tw-ink) !important; }

/* ---------- Composer bar ---------- */
.gr-group {
  position: sticky;
  bottom: 0;
  z-index: 5;
  padding: 16px 0 20px !important;
  overflow: visible !important;
  background: transparent !important;
  border: 0 !important;
  border-radius: 0 !important;
  box-shadow: none !important;
}
.gr-group::before {  /* the bar itself runs edge to edge */
  content: "";
  position: absolute;
  z-index: -1;
  top: 0;
  bottom: -40px;
  left: 50%;
  width: 100vw;
  transform: translateX(-50%);
  background: var(--tw-bar);
  border-top: 1px solid var(--tw-ink);
}
.gr-group .gr-group {  /* Gradio 6 nests a second group inside the first */
  position: static;
  padding: 0 !important;
}
.gr-group .gr-group::before { display: none; }
.gr-group .row, .gr-group .form, .gr-group .block { background: transparent !important; }
.input-container {
  display: flex !important;
  gap: 10px;
  align-items: center;
}
textarea,
input[type="text"],
[data-testid="textbox"] {
  box-sizing: border-box;
  min-height: 44px !important;
  padding: 10px 12px !important;
  background: #FFFFFF !important;
  color: var(--tw-ink) !important;
  border: 1px solid var(--tw-field-edge) !important;
  border-radius: 6px !important;
  box-shadow: none !important;
  font: 400 17px/1.4 var(--tw-body) !important;
}
textarea:focus, input[type="text"]:focus {
  outline: 2px solid var(--tw-pink) !important;
  outline-offset: 2px !important;
}
textarea::placeholder, input::placeholder {
  color: var(--tw-muted) !important;
  opacity: 1;
}

/* Send: ink square with the arrow, pink on hover */
.submit-button, button.submit-button, [data-testid="submit-button"], button.primary {
  flex: none !important;
  box-sizing: border-box;
  width: 44px !important;
  height: 44px !important;
  min-width: 44px !important;
  min-height: 44px !important;
  padding: 0 !important;
  display: inline-flex !important;
  align-items: center;
  justify-content: center;
  background: var(--tw-ink) !important;
  color: var(--tw-ground) !important;
  border: 0 !important;
  border-radius: 6px !important;
  box-shadow: none !important;
  cursor: pointer;
  transition: background 0.14s ease, color 0.14s ease;
}
.submit-button svg { display: none !important; }
.submit-button::after {
  content: "";
  width: 20px;
  height: 20px;
  background: currentColor;
  -webkit-mask-image: @arrow@;
  -webkit-mask-repeat: no-repeat;
  -webkit-mask-position: center;
  -webkit-mask-size: contain;
  mask-image: @arrow@;
  mask-repeat: no-repeat;
  mask-position: center;
  mask-size: contain;
}
.submit-button:hover, button.primary:hover {
  background: var(--tw-pink) !important;
  color: var(--tw-ink) !important;
}

/* ---------- Small things ---------- */
::-webkit-scrollbar { width: 10px; height: 10px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--tw-edge); border-radius: 6px; }
::selection { background: var(--tw-pink); color: var(--tw-ink); }
:focus-visible { outline: 2px solid var(--tw-pink) !important; outline-offset: 2px !important; }

/* ---------- Tablet and phone: labels move above the text ---------- */
@media (max-width: 900px) {
  .message-row {
    flex-direction: column !important;
    align-items: flex-start !important;
    padding-left: 0 !important;
  }
  .message-wrap .message-buttons { margin-left: 0 !important; }
  .message-row::before {
    position: static;
    display: block;
    margin-bottom: 12px;
  }
  .message-row.bot-row::before {
    display: inline-block;
    padding: 0 62px 0 0;
    background-position: 42px center;
    background-size: 44px 21px;
    background-color: transparent;
  }
}
/* Gradio re-scopes everything inside a media query under `.contain`, so rules in
   here can't target .gradio-container itself (its padding is fluid above). */
@media (max-width: 640px) {
  h1 { margin-top: 24px !important; }
  .prose[data-testid="markdown"] p { font-size: 17px !important; margin-top: 18px !important; }
  .placeholder-content .placeholder::before { width: 100px; margin-bottom: 20px; }
  .message-row.bot-row .message-content,
  .message-row.bot-row .prose,
  .message-row.bot-row .prose p { font-size: 17px !important; }
  .gr-group { padding: 12px 0 16px !important; }
}
"""

# Gradio re-serialises custom CSS, and it mangles a `font:` shorthand that contains
# var(); so the font stacks are written into the rules as literals.
_RULES = (
    _RULES.replace("var(--tw-display)", DISPLAY)
    .replace("var(--tw-body)", BODY)
    .replace("var(--tw-mono)", MONO)
    .replace("@arrow@", _ARROW_URL)
)

CSS = _FONTS + _VARS + _RULES

JS = """
() => {
  document.title = 'Jen Reid-Schram (Digital Twin)';

  // The name: wrap each word so it never breaks at the hyphen, and give the
  // outlined echo the text of the last line (the whole name when it fits on one).
  const setupName = () => {
    const h1 = document.querySelector('.gradio-container h1');
    if (!h1) return;
    const name = (h1.dataset.twinName || h1.textContent).trim().replace(/\\s+/g, ' ');
    if (h1.dataset.twinReady !== name) {
      h1.dataset.twinName = name;
      h1.dataset.twinReady = name;
      h1.textContent = '';
      name.split(' ').forEach((word, i) => {
        if (i) h1.appendChild(document.createTextNode(' '));
        const span = document.createElement('span');
        span.style.whiteSpace = 'nowrap';
        span.textContent = word;
        h1.appendChild(span);
      });
    }
    const words = Array.from(h1.querySelectorAll('span'));
    if (!words.length) return;
    const lastTop = words[words.length - 1].offsetTop;
    const lastLine = words.filter((w) => w.offsetTop === lastTop).map((w) => w.textContent);
    const echo = lastLine.join(' ');
    if (h1.dataset.echo !== echo) h1.dataset.echo = echo;
  };
  let queued = false;
  const queueName = () => {
    if (queued) return;
    queued = true;
    requestAnimationFrame(() => { queued = false; setupName(); });
  };
  queueName();
  window.addEventListener('resize', queueName);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(queueName);
  new MutationObserver(queueName).observe(document.body, { childList: true, subtree: true });

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
