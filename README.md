# LLaMA Text Summarizer

A lightweight end‑to‑end application that provides concise multi‑bullet summaries for arbitrary pasted text using a locally hosted LLM (via [Ollama](https://ollama.com/)) exposed through a FastAPI backend and a Streamlit web UI.

## Key Features
- 3–5 bullet point abstractive summarization
- Local inference (no external API keys required) using `llama3.2`
- Simple REST endpoint (`/summarize/`) returning JSON
- Responsive Streamlit frontend
- CORS configured for local development
- Easily swappable model + configurable Ollama endpoint

## Tech Stack
| Layer      | Technology |
|----------- |----------- |
| LLM Runtime | Ollama (pulls `llama3.2:latest`) |
| Backend API | FastAPI + Uvicorn |
| Frontend UI | Streamlit |
| HTTP Client | `requests` |

## Environment / Setup Note
If you already have a local Conda environment in this folder (e.g. `env/`), you can keep using it. Do not commit that directory—add `env/` (or your env name) to `.gitignore`. For broader reproducibility, the README shows BOTH Conda and virtualenv options.

## Project Structure
```
project-1/
├─ backend/
│  └─ main.py           # FastAPI application exposing /summarize/
├─ frontend/
│  └─ app.py            # Streamlit UI
├─ requirements.txt      # (Full environment export – large; see minimal below)
├─ README.md
└─ env/ (optional local conda/venv dir – do not commit)
```

## API Overview
### Endpoint
`POST /summarize/`

### Form Data
| Field | Type | Description |
|-------|------|-------------|
| text  | string (required) | Raw input text to summarize |

### Response (200)
```json
{
  "summary": "• Bullet 1...\n• Bullet 2..."
}
```

### Errors
| Code | Reason |
|------|--------|
| 400  | Empty text submitted |
| 500  | Upstream / model / network failure |

## Quick Start (Minimal)
1. Install Ollama and pull the model:
   ```bash
   ollama pull llama3.2
   ```
2. Create / activate a Python environment (choose ONE):
   - Conda (recommended if you already maintain an Anaconda setup):
     ```bash
     conda create -n llama-summarizer -y python=3.12
     conda activate llama-summarizer
     ```
   - Or built‑in venv (lightweight, portable):
     ```pwsh
     python -m venv .venv
     .venv\Scripts\Activate.ps1  # PowerShell on Windows
     ```
3. Minimal dependencies (create a `minimal-requirements.txt` or install directly):
   ```text
   fastapi
   uvicorn
   streamlit
   requests
   ```
   Install with Conda + pip hybrid (packages are pure Python):
   ```bash
   pip install -r minimal-requirements.txt
   ```
4. Start the backend API:
   ```pwsh
   uvicorn backend.main:app --reload --port 8000
   ```
5. In a second terminal, start the frontend:
   ```pwsh
   streamlit run frontend/app.py --server.port 8501
   ```
6. Open http://localhost:8501, paste text, click Summarize.

## Configuration
Environment variables (optional):
| Name | Default | Description |
|------|---------|-------------|
| OLLAMA_URL | http://localhost:11434/api/generate | Base URL for Ollama generation endpoint |
| MODEL_NAME | llama3.2:latest | Model tag to use |

To change, you can adapt constants in `backend/main.py` or refactor to read from `os.environ`.

## Development Notes
- `requirements.txt` is a large exported environment; prefer a trimmed list (see minimal file) for deployment.
- Add `.gitignore` entry for any local environment directory (e.g. `env/`, `.venv/`).
- Add tests (see Roadmap) to validate endpoint behavior.
- Consider Docker for reproducibility (Ollama + API + Streamlit multi‑container setup with Docker Compose).

## Example cURL
```bash
curl -X POST -F "text=Paste your long article here" http://localhost:8000/summarize/
```

## Production Suggestions
- Front behind reverse proxy (nginx / Traefik) with HTTPS.
- Enable request timeout / rate limiting.
- Add input length guardrails (token / char limit) to protect the model.
- Cache identical input summaries (e.g., in Redis) if throughput matters.

## Roadmap
- [ ] Environment variable driven config
- [ ] Input length + toxicity validation
- [ ] Unit & integration tests (pytest + httpx TestClient)
- [ ] Docker & docker-compose
- [ ] Streaming response option
- [ ] Model selection dropdown in UI
- [ ] Frontend styling polish / dark mode
- [ ] Add CI workflow (lint + tests) via GitHub Actions

## Contributing
1. Fork & branch: `feat/your-feature`
2. Run lint & tests before PR (add tooling: `ruff` / `flake8`, `pytest`).
3. Open PR with concise description and screenshots (if UI changes).

## License
Choose an OSI approved license (e.g., MIT) and add a `LICENSE` file. Update this section accordingly.

## Security / Privacy
All inference is local; no text leaves the machine unless you modify the backend to call external services. Do not expose the service publicly without authentication / rate limiting.

## Troubleshooting
| Issue | Resolution |
|-------|------------|
| 422 Unprocessable Entity | Ensure form field key is `text` and method is POST |
| ConnectionError from frontend | Confirm backend is on port 8000 and CORS origin matches Streamlit URL |
| Model load latency | First request is a warm start; subsequent calls are faster |
| Large text slows response | Consider truncation or chunking before summarization |

## Acknowledgements
- FastAPI project & community
- Streamlit project
- Meta LLaMA models (served locally through Ollama)

---
Generated README template.
