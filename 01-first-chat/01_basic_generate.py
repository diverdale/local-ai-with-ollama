"""Lesson 01 - Step 1: a single request/response with a local model.

Run it:  uv run 01-first-chat/01_basic_generate.py
"""
from rich import print

from shared.ollama_client import get_client, require_model

MODEL = "qwen3.5"

client = get_client()
require_model(client, MODEL)

response = client.generate(
    model=MODEL,
    prompt="In two sentences, explain why running an LLM locally is useful.",
)
print(f"[bold]{MODEL}[/bold] says:\n")
print(response.response)
