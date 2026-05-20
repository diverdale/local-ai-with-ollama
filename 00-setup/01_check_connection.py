"""Lesson 00 - Step 1: confirm we can reach the Ollama host.

Run it:  uv run 00-setup/01_check_connection.py
"""
from rich import print

from shared.ollama_client import get_client, list_models

client = get_client()
print("[bold green]Connected to Ollama.[/bold green]")

models = list_models(client)
print(f"\n{len(models)} model(s) available on the host:")
for name in sorted(models):
    print(f"  - {name}")
