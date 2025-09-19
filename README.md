# Summarizer

A text summarization application built with FastAPI backend and Streamlit frontend, powered by local LLM inference through Ollama.

## Overview

This project provides an easy-to-use interface for summarizing text using locally hosted language models. No API keys required - everything runs on your machine.

## Features

- Clean web interface for text input and summary output
- Local LLM processing using Ollama
- FastAPI REST API backend
- Streamlit frontend
- No external dependencies or API keys needed

## Quick Start

1. **Install Ollama and pull a model:**
   ```bash
   # Install Ollama (visit https://ollama.com for instructions)
   ollama pull llama3.2
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the backend:**
   ```bash
   cd backend
   python main.py
   ```

4. **Start the frontend (in a new terminal):**
   ```bash
   cd frontend
   streamlit run app.py
   ```

5. **Open your browser to `http://localhost:8501`**

## Project Structure

```
Summarizer/
├── backend/
│   └── main.py          # FastAPI application
├── frontend/
│   └── app.py           # Streamlit web interface
├── requirements.txt     # Python dependencies
└── README.md
```

## Usage

1. Open the Streamlit app in your browser
2. Paste or type the text you want to summarize
3. Click the "Summarize" button
4. View your generated summary

## API Endpoint

The backend exposes a simple REST API:

**POST** `/summarize/`
- **Input:** Form data with `text` field
- **Output:** JSON with `summary` field

Example:
```bash
curl -X POST -F "text=Your text here" http://localhost:8000/summarize/
```

## Requirements

- Python 3.8+
- Ollama with a compatible language model
- Dependencies listed in `requirements.txt`
