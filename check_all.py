"""Smoke test: run the first script of every lesson and report pass/fail.

Run it:  uv run check_all.py
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent


def first_scripts():
    """Yield the first numbered script in each numbered lesson folder."""
    for lesson in sorted(p for p in ROOT.iterdir() if p.is_dir() and p.name[:2].isdigit()):
        scripts = sorted(lesson.glob("[0-9][0-9]_*.py"))
        if scripts:
            yield scripts[0]


def main() -> int:
    failed = []
    for script in first_scripts():
        rel = script.relative_to(ROOT)
        print(f"running {rel} ... ", end="", flush=True)
        result = subprocess.run(
            [sys.executable, str(script)], capture_output=True, text=True
        )
        if result.returncode == 0:
            print("ok")
        else:
            print("FAIL")
            failed.append((rel, result.stderr.strip()))

    if failed:
        print(f"\n{len(failed)} lesson(s) failed:")
        for rel, err in failed:
            print(f"\n--- {rel} ---\n{err}")
        return 1
    print("\nAll lessons passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
