# Lesson 00 — Setup & connecting

## What you'll see

The uv toolchain from the ground up — creating a project, pinning Python,
adding dependencies — then connecting Python to an Ollama server running on
another machine on the network.

## Why it matters

Everything in this series runs against a local Ollama host — no cloud account,
no API key, no bill. This lesson sets up the toolchain and proves the pipe
works before we write any model code.

## Path A — Build a uv project from scratch (follow along)

This is how this project was created. Do it in a scratch folder to learn the
uv workflow — the actual lesson files come from Path B.

```bash
# 1. Install uv (one time): https://docs.astral.sh/uv/getting-started/installation/

# 2. Create the project — a flat app layout (we run scripts, we don't ship a package):
uv init local-ai-with-ollama
cd local-ai-with-ollama

# 3. Pin the Python version (uv downloads it if you don't have it):
uv python pin 3.13

# 4. Add the dependencies the early lessons use:
uv add ollama python-dotenv rich

# 5. Run something — uv syncs the environment automatically first:
uv run main.py
```

`uv init` writes `pyproject.toml`, `.python-version`, and a sample `main.py`.
The first `uv add` creates `.venv/` and the `uv.lock` lockfile. You never
activate a virtualenv by hand — `uv run` does it for you.

> One extra step in this repo: a small `[build-system]` block in
> `pyproject.toml` makes the `shared/` folder an installable package, so every
> lesson can `from shared.ollama_client import ...`. Peek at `pyproject.toml`.

## Path B — Or just clone this repo

To run the actual lessons, clone the finished repo:

```bash
git clone https://github.com/diverdale/local-ai-with-ollama
cd local-ai-with-ollama
uv sync          # builds .venv from uv.lock — reproducible and exact
```

## Connect to your Ollama host

```bash
# Copy the env file and edit OLLAMA_HOST if your host differs:
cp .env.example .env

# Confirm the connection:
uv run 00-setup/01_check_connection.py

# Inspect what models are installed:
uv run 00-setup/02_list_models.py
```

## Expected output

`01_check_connection.py` prints `Connected to Ollama.` followed by the list of
installed models. `02_list_models.py` prints a table of models with sizes.

## Talking points

- uv replaces `python -m venv` + `pip` + `requirements.txt` with one fast tool.
- `uv init` scaffolds the project; `uv add` manages dependencies; `uv run` runs code.
- Commit `pyproject.toml`, `uv.lock`, and `.python-version`; gitignore `.venv/`.
- `uv sync` rebuilds the exact environment from the lockfile on any machine.
- The connection host lives in `.env`; `shared/ollama_client.py` reads it once.

## Try this

Stop the Ollama server (or set a wrong `OLLAMA_HOST` in `.env`) and rerun
`01_check_connection.py` — note the friendly error message instead of a stack trace.
