#!/usr/bin/env python3
"""Confess Your Worst Moment -- make.fun bounty entry.

Reads the one-line confession from confession.txt and writes it to
/output/entry.txt (the grader's sandbox path), falling back to
./output/entry.txt on a local dev run where /output is not writable.
Deterministic: no network, no randomness, no clock.
"""

import os

_HERE = os.path.dirname(os.path.abspath(__file__))


def _load_confession() -> str:
    with open(os.path.join(_HERE, "confession.txt"), encoding="utf-8") as f:
        return f.read().strip()


CONFESSION = _load_confession()


def main() -> None:
    text = CONFESSION.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = "output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
