from openai import OpenAI
from context import TWIN_SYSTEM_PROMPT
from tools import tools, handle_tool_calls
from styles import CSS, JS, EXAMPLES
from dotenv import load_dotenv
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
from starlette.middleware.base import BaseHTTPMiddleware
import base64
import html
import os
import re
import gradio as gr
import uvicorn

load_dotenv(override=True)

MODEL_NAME = "gpt-5.4-mini"

openai = OpenAI()

system = [{"role": "system", "content": TWIN_SYSTEM_PROMPT}]

_LOGO_PATH = Path(__file__).parent / "twin-mark-logo_1.png"
_LOGO_SRC = (
    "data:image/png;base64,"
    + base64.b64encode(_LOGO_PATH.read_bytes()).decode("ascii")
)

PUBLIC_URL = os.environ.get("PUBLIC_URL", "https://jenreidschram.com").rstrip("/")
PAGE_TITLE = "Jen Reid-Schram (Interactive Resume)"
OG_TITLE = "Jen Reid-Schram"
OG_DESCRIPTION = (
    "The interactive resume of Jen Reid-Schram. Ask about her career, AI consulting, "
    "and coaching."
)
OG_IMAGE = f"{PUBLIC_URL}/og-image.png"

_SOCIAL_META_RE = re.compile(
    r"<meta\b[^>]*(?:property|name)=[\"'](?:og:[^\"']+|twitter:[^\"']+)[\"'][^>]*/?>",
    re.IGNORECASE | re.DOTALL,
)
_TITLE_RE = re.compile(r"<title\b[^>]*>.*?</title>", re.IGNORECASE | re.DOTALL)
_HEAD_RE = re.compile(r"(<head\b[^>]*>)", re.IGNORECASE)

HEAD_TAGS = f"""
<meta name="description" content="{html.escape(OG_DESCRIPTION)}">
<meta property="og:title" content="{html.escape(OG_TITLE)}">
<meta property="og:description" content="{html.escape(OG_DESCRIPTION)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{html.escape(PUBLIC_URL)}/">
<meta property="og:image" content="{html.escape(OG_IMAGE)}">
<meta property="og:image:alt" content="Jen Reid-Schram twin mark">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{html.escape(OG_TITLE)}">
<meta name="twitter:description" content="{html.escape(OG_DESCRIPTION)}">
<meta name="twitter:image" content="{html.escape(OG_IMAGE)}">
<title>{html.escape(PAGE_TITLE)}</title>
"""


class OpenGraphMiddleware(BaseHTTPMiddleware):
    """Rewrite Gradio's default social meta tags in the HTML Gradio serves.

    Gradio's ``head=`` content is applied client-side, so link crawlers never
    see it. This middleware patches the actual HTML response instead.
    """

    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        content_type = response.headers.get("content-type", "")
        if "text/html" not in content_type:
            return response

        body = b"".join([chunk async for chunk in response.body_iterator])
        text = body.decode(response.charset or "utf-8")
        text = _SOCIAL_META_RE.sub("", text)
        text = _TITLE_RE.sub("", text)
        text = _HEAD_RE.sub(r"\1" + HEAD_TAGS, text, count=1)

        headers = {
            k: v
            for k, v in response.headers.items()
            if k.lower() not in {"content-length", "content-encoding"}
        }
        return HTMLResponse(
            content=text,
            status_code=response.status_code,
            headers=headers,
        )


NAME = "# Jen Reid-Schram"
INTRO = (
    "I spent the last 15 years leading technology teams and running transformation programs. "
    "Now, I run a consulting business called Third Gear Solutions, helping organizations implement AI solutions; and a coaching business called LevelUp Learning Experiences, helping executives and their teams level up their AI skills. \n\n"
    "Ask me about my career. If you want to get in touch, leave your email "
    "and I'll get back to you."
)
LOGO_HTML = (
    f'<img class="twin-mark-logo" src="{_LOGO_SRC}" '
    'alt="Twin mark" width="120" height="58" />'
)


def chat(message, history):
    messages = system + history + [{"role": "user", "content": message}]
    response = openai.chat.completions.create(model=MODEL_NAME, messages=messages, tools=tools)
    while response.choices[0].finish_reason == "tool_calls":
        message = response.choices[0].message
        tool_calls = message.tool_calls
        results = handle_tool_calls(tool_calls)
        messages.append(message)
        messages.extend(results)
        response = openai.chat.completions.create(model=MODEL_NAME, messages=messages, tools=tools)
    return response.choices[0].message.content


if __name__ == "__main__":
    textbox = gr.Textbox(
        render=False,
        show_label=False,
        placeholder="Message…",
        submit_btn=True,
        autofocus=True,
    )

    with gr.Blocks(title=PAGE_TITLE, fill_height=True) as demo:
        with gr.Row(elem_classes=["twin-layout"]):
            with gr.Column(scale=1, min_width=220, elem_classes=["twin-bio"]):
                gr.Markdown(NAME)
                gr.HTML(LOGO_HTML, elem_classes=["twin-mark-wrap"])
                gr.Markdown(INTRO)
                gr.Examples(examples=EXAMPLES, inputs=textbox)
            with gr.Column(scale=2, min_width=320, elem_classes=["twin-chat"]):
                gr.ChatInterface(
                    chat,
                    textbox=textbox,
                    examples=None,
                    fill_height=True,
                    chatbot=gr.Chatbot(show_label=False, scale=1, height="100%"),
                )

    app = FastAPI()

    @app.get("/og-image.png")
    def og_image():
        return FileResponse(_LOGO_PATH, media_type="image/png")

    app = gr.mount_gradio_app(
        app,
        demo,
        path="/",
        css=CSS,
        js=JS,
        theme=gr.themes.Base(),
        favicon_path=str(_LOGO_PATH),
    )
    app.add_middleware(OpenGraphMiddleware)

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 7860)),
    )
