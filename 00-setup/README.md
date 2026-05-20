# Lesson 00 — Setup & connecting

## What you'll see

Installing the uv toolchain, syncing the project, and connecting Python to an
Ollama server running on another machine on the network.

## Why it matters

Everything in this series runs against a local Ollama host — no cloud account,
no API key, no bill. This lesson proves the pipe works before we write any
model code.

## Run it

```bash
# 1. Install uv (one time): https://docs.astral.sh/uv/getting-started/installation/
# 2. Point the project at your Ollama host:
cp .env.example .env

# 3. Create the environment and install everything:
uv sync

# 4. Confirm the connection:
uv run 00-setup/01_check_connection.py

# 5. Inspect what models are installed:
uv run 00-setup/02_list_and_pull.py
```

## Expected output

`01_check_connection.py` prints `Connected to Ollama.` followed by the list of
installed models. `02_list_and_pull.py` prints a table of models with sizes.

## Talking points

- uv replaces `python -m venv` + `pip` + `requirements.txt` with one fast tool.
- `uv sync` reads `pyproject.toml` / `uv.lock` and builds `.venv` reproducibly.
- `uv run` auto-syncs, so you never activate a virtualenv by hand.
- The connection host lives in `.env`; `shared/ollama_client.py` reads it once.

## Try this

Stop the Ollama server (or set a wrong `OLLAMA_HOST` in `.env`) and rerun
`01_check_connection.py` — note the friendly error message instead of a stack trace.
