"""Shared Ollama connection helper used by every lesson in this series.

Every lesson imports `get_client()` so the connection pattern is written once.
"""
from __future__ import annotations

import os
import sys

from dotenv import load_dotenv
from ollama import Client

DEFAULT_HOST = "http://192.168.2.20:11434"


def get_client() -> Client:
    """Return an Ollama client for OLLAMA_HOST, or exit with a clear message."""
    load_dotenv()  # read .env so OLLAMA_HOST works without a manual export
    host = os.getenv("OLLAMA_HOST", DEFAULT_HOST)
    client = Client(host=host)
    try:
        client.list()
    except Exception as exc:  # noqa: BLE001 -- any failure means we cannot continue
        sys.exit(
            f"\nCould not reach Ollama at {host}.\n"
            f"  - Is the server running?  Try:  curl {host}/api/version\n"
            f"  - Check OLLAMA_HOST in your .env file (copy it from .env.example).\n"
            f"  (original error: {exc})\n"
        )
    return client


def list_models(client: Client) -> set[str]:
    """Return the set of model names available on the host."""
    return {m.model for m in client.list().models if m.model}


def require_model(client: Client, model: str) -> None:
    """Exit with a pull hint if `model` is not available on the host."""
    available = list_models(client)
    if model in available or f"{model}:latest" in available:
        return
    sys.exit(
        f"\nModel '{model}' is not on the Ollama host.\n"
        f"  Pull it with:  ollama pull {model}\n"
        f"  Currently available: {', '.join(sorted(available)) or '(none)'}\n"
    )
