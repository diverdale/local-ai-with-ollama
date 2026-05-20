# Lesson 01 — First chat & streaming

## What you'll see

Two ways to talk to a local model: a single blocking response, and a streamed
response that prints token-by-token as the model generates it.

## Why it matters

Streaming is what makes a local model feel fast and interactive — the same
experience as a cloud chatbot, running entirely on your own hardware.

## Run it

```bash
uv run 01-first-chat/01_basic_generate.py
uv run 01-first-chat/02_streaming_chat.py
```

## Expected output

`01` prints a two-sentence answer after a short pause. `02` prints a haiku that
appears word-by-word as it is generated.

## Talking points

- `client.generate()` is one prompt in, one response out.
- `client.chat()` takes a list of messages and supports `stream=True`.
- Streaming yields chunks; each `chunk.message.content` is a piece of the reply.
- No tokens-per-minute limit — the model runs as fast as the host GPU allows.

## Try this

Change `MODEL` to `qwen2.5:14b` and rerun — a larger model, slightly slower,
often a richer answer. Same code, different trade-off.
