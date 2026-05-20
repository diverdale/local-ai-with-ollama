"""Lesson 02 - Step 2: a multi-turn chat that remembers the conversation.

The whole `messages` list is sent every turn — that list IS the memory.
Run it:  uv run 02-prompts-and-memory/02_conversation_memory.py
"""
from rich import print

from shared.ollama_client import get_client, require_model

MODEL = "qwen3.5"

client = get_client()
require_model(client, MODEL)

messages = [{"role": "system", "content": "You are a concise, friendly assistant."}]

print("[bold]Chat with a local model.[/bold] Type 'exit' to quit.\n")
while True:
    user_text = input("you> ")
    if user_text.strip().lower() in {"exit", "quit"}:
        break
    messages.append({"role": "user", "content": user_text})
    reply = client.chat(model=MODEL, messages=messages, options={"temperature": 0.7})
    answer = reply.message.content
    messages.append({"role": "assistant", "content": answer})
    print(f"[cyan]ai>[/cyan] {answer}\n")
