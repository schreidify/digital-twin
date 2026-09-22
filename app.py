from openai import OpenAI
from context import TWIN_SYSTEM_PROMPT
from tools import tools, handle_tool_calls
from styles import CSS, JS, EXAMPLES
from dotenv import load_dotenv
from pathlib import Path
import base64
import os
import gradio as gr

load_dotenv(override=True)

MODEL_NAME = "gpt-5.4-mini"

openai = OpenAI()

system = [{"role": "system", "content": TWIN_SYSTEM_PROMPT}]

_LOGO_PATH = Path(__file__).parent / "twin-mark-logo_1.png"
_LOGO_SRC = (
    "data:image/png;base64,"
    + base64.b64encode(_LOGO_PATH.read_bytes()).decode("ascii")
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

    with gr.Blocks(fill_height=True) as demo:
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

    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860)),
        css=CSS,
        js=JS,
        theme=gr.themes.Base(),
    )