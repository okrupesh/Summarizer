from fastapi import FastAPI, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:latest"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8501", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/summarize/")
def summarize(text: str = Form(...)):
    if not text.strip():
        raise HTTPException(status_code=400, detail="Text is empty")
    payload = {
        "model": MODEL_NAME,
        "prompt": f"Summarize this text in 3-5 bullets:\n\n{text}",
        "stream": False
    }
    resp = requests.post(OLLAMA_URL, json=payload, timeout=60)
    resp.raise_for_status()
    data = resp.json()
    summary = data.get("response") or data.get("output") or str(data)
    return {"summary": summary}