# My Digital Twin

Welcome to my digital twin repo. If I had a better name for this, I would name her something interesting like my name spelled backwards. But alas, I have a foreign-sounding name and Marhcs-Dier Nej doesn't really work. 

The purpose of my digital twin is simply to answer questions about my work experience, personal projects, and my consulting businesses: Third Gear Solutions (AI consultancy work) and LevelUp Learning Experiences (personal AI coaching for executives). 

## What it does

Inspired by Ed Donner's excellent series of Agentic Development courses, this initial version mostly follows the architecture taught there: 

- A Gradio chat app UI
- OpenAI model (currently gpt-5.4-mini)
- Context store including my resume, example-bank, and other text
- Pushover for lead capture notifications

## Create your own digital twin

To run your own version of this tool, simply clone/fork the code and do the following:

1. Run these commands in your terminal to set up your python virtual environment and install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt 
```

1. Add your OPEN_API_KEY (or whatever model you're using), PUSHOVER_USER, and PUSHOVER_TOKEN variables to the `.env` file.
2. Add your own context and replace the filenames read by `context.py`

