#!/usr/bin/env python3
"""Fridge Roast: one line, biggest laugh.

The program writes a single roast of a smart fridge to /output/entry.txt:
exactly one line, at most 200 characters, and prints it to stdout.
Deterministic: the same fixed text on every run, no time, no randomness,
no network, no input read.
"""

import os

LINE = (
    "My smart fridge says the milk is 'experiencing difficulties' "
    "and offers a premium plan where it expires with dignity."
)


def _validate(line: str) -> None:
    """Mirror the competition gate: 1-200 characters, exactly one line."""
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")
    if line.strip() != line or "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line, no surrounding whitespace")


def main() -> None:
    _validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w",
              encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
