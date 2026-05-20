"""Lesson 01 - Step 2: stream the response token-by-token as it is generated.

Run it:  uv run 01-first-chat/02_streaming_chat.py
"""
from shared.ollama_client import get_client, require_model

MODEL = "qwen3.5"

client = get_client()
require_model(client, MODEL)

messages = [{"role": "user", "content": "Write a short haiku about local AI."}]

print(f"{MODEL} (streaming):\n")
for chunk in client.chat(model=MODEL, messages=messages, stream=True):
    print(chunk.message.content, end="", flush=True)
print()
