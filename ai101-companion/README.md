# AI 101 Companion

A web app to help new AI users learn prompting, find tools, and master AI.

## Features

- **Prompt Builder** - Build effective prompts step-by-step
- **Prompt Analyzer** - Get feedback on any prompt
- **Prompt Library** - Copy-paste templates for common tasks
- **Tool Finder** - Quiz to recommend the right AI tools
- **AI Glossary** - Plain-language AI terminology

## Deploy to Replit

1. Create a new Replit
2. Import from GitHub or upload these files
3. Click Run

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Visit http://localhost:5000

## Structure

```
ai101-companion/
├── app.py              # Flask backend
├── requirements.txt    # Python dependencies
├── .replit            # Replit config
├── replit.nix         # Nix packages
├── templates/
│   └── index.html     # Main page
├── static/
│   ├── css/style.css  # Styles
│   └── js/app.js      # Frontend JS
└── data/
    ├── glossary.json  # AI terms
    ├── prompts.json   # Prompt templates
    └── tools.json     # AI tools database
```
