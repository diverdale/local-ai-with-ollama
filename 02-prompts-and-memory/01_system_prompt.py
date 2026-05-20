"""Lesson 02 - Step 1: a system prompt changes the model's behavior.

Run it:  uv run 02-prompts-and-memory/01_system_prompt.py
"""
from rich import print

from shared.ollama_client import get_client, require_model

MODEL = "qwen3.5"

client = get_client()
require_model(client, MODEL)

question = "What is a local language model?"

for persona in [
    "You are a terse pirate. Answer in one sentence.",
    "You are a patient teacher explaining to a 10-year-old.",
]:
    messages = [
        {"role": "system", "content": persona},
        {"role": "user", "content": question},
    ]
    reply = client.chat(model=MODEL, messages=messages)
    print(f"[bold cyan]System:[/bold cyan] {persona}")
    print(f"[green]Answer:[/green] {reply.message.content}\n")
