# Lesson 02 — Prompts & memory

## What you'll see

How a system prompt steers the model's personality, and how to keep a
conversation going so the model remembers earlier turns.

## Why it matters

These two ideas — a system prompt and a running message list — are the
foundation of every chatbot, assistant, and agent built later in the series.

## Run it

```bash
uv run 02-prompts-and-memory/01_system_prompt.py
uv run 02-prompts-and-memory/02_conversation_memory.py
```

The second script is interactive — type messages, then `exit` to quit.

## Expected output

`01` answers the same question twice with two very different voices. `02` is a
live chat loop; ask a follow-up like "what did I just ask you?" to prove it
remembers.

## Talking points

- The `system` message sets behavior; `user` / `assistant` messages are the turns.
- Memory is not magic — you resend the full `messages` list every turn.
- `options={"temperature": 0.7}` controls randomness: lower = focused, higher = creative.
- A long conversation grows the message list; later lessons handle large context.

## Try this

Set `temperature` to `0.1` and then `1.2` and ask the same creative question.
Watch how the answers tighten up or get wilder.
