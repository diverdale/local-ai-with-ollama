# Local AI with Ollama

A hands-on tutorial series for building real things with **local** large language
models — no cloud APIs, no usage bills, no data leaving your network.

Each lesson is a self-contained folder you can run on its own. Code runs in
Python and is managed with [uv](https://docs.astral.sh/uv/).

## Why local models?

- **Private** — your prompts and documents never leave your machines.
- **Free** — no per-token billing, no rate limits.
- **Offline** — works without an internet connection.
- **Yours** — pick the model, pin the version, keep it forever.

## Setup

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/).
2. Clone this repo and `cd` into it.
3. Copy the environment file and point it at your Ollama host:
   ```bash
   cp .env.example .env
   ```
4. Sync the project (creates `.venv` and installs everything):
   ```bash
   uv sync
   ```
5. Confirm the connection:
   ```bash
   uv run 00-setup/01_check_connection.py
   ```

Every lesson script runs the same way: `uv run <folder>/<script>.py`.

## Models used

| Model | Size | Used for |
|-------|------|----------|
| `qwen3.5` | 6.6 GB | Fast general chat |
| `qwen2.5:14b` | 9.0 GB | Structured output, tool calling |
| `mistral-nemo:12b` | 7.1 GB | Long context (128k) |
| `qwen3-coder:30b` | 18 GB | Coding assistant |
| `nemotron3:33b` | 27 GB | Heavy reasoning |
| `llama3.2-vision:11b` | 7.9 GB | Image understanding (pull in Lesson 05) |
| `nomic-embed-text` | 0.3 GB | Embeddings (pull in Lesson 06) |

## Lessons

| # | Lesson | What it shows |
|---|--------|---------------|
| 00 | Setup & connecting | Install uv, sync, connect to a remote Ollama host |
| 01 | First chat & streaming | Single responses and token streaming |
| 02 | Prompts & memory | System prompts, multi-turn conversation, parameters |
| 03 | Structured output | Clean JSON output with Pydantic schemas |
| 04 | Tool calling | The model calls your Python functions |
| 05 | Vision | Describe images and OCR with a vision model |
| 06 | Embeddings & semantic search | Search by meaning, not keywords |
| 07 | RAG — chat with your docs | Private Q&A over local PDFs |
| 08 | Coding assistant | Generate, explain, and refactor code |
| 09 | Batch automation | Process a whole folder of files for $0 |
| 10 | Long context & reasoning | Huge documents and hard reasoning prompts |
| 11 | Model comparison & tuning | Benchmark models; OpenAI-compatible API |
| 12 | Capstone: local agent | Tools + RAG + a loop = a working assistant |

## Smoke test

Run every lesson's first script at once to confirm nothing is broken:

```bash
uv run check_all.py
```
