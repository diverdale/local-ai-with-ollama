"""Lesson 00 - Step 2: inspect installed models and learn how to pull new ones.

Run it:  uv run 00-setup/02_list_models.py
"""
from rich import print
from rich.table import Table

from shared.ollama_client import get_client

client = get_client()
models = client.list().models

table = Table(title="Models installed on the Ollama host")
table.add_column("Name", style="cyan")
table.add_column("Size", justify="right", style="green")

for model in models:
    size_gb = (model.size or 0) / 1e9
    table.add_row(model.model, f"{size_gb:.1f} GB")

print(table)
print(
    "\nNeed a model that is not listed? Pull it on the host with:\n"
    "  [bold]ollama pull <model-name>[/bold]\n"
    "For example:  [bold]ollama pull llama3.2-vision:11b[/bold]\n"
    "We will pull a model live on screen in Lesson 06."
)
