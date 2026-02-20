# Chatbot using OpenAI's GPT-3.5 and Flask

A simple web application that demonstrates how to build a chatbot using OpenAI's GPT-3.5 model and the Flask framework.

## Overview

This project provides a browser-based chat interface powered by the OpenAI API. Users can type messages and receive AI-generated responses in real time.

## Prerequisites

Before running the application, make sure you have the following installed:

- **Python** >= 3.6
- **Flask** – `pip install Flask`
- **OpenAI Python library** – `pip install openai`

## Configuration

1. [Sign up](https://platform.openai.com/signup) for an OpenAI account and obtain an API key.
2. Open `main.py` and replace the empty string with your API key:

```python
openai.api_key = "your-api-key-here"
```

## Usage

Start the Flask development server:

```bash
python main.py
```

Then open your browser and navigate to `http://127.0.0.1:5000` to start chatting.

## Project Structure

```
chatbot-openai_api/
├── main.py          # Flask application and OpenAI integration
└── static/
    ├── index.html   # Chat UI
    ├── script.js    # Frontend logic
    └── styles.css   # Styling
```


