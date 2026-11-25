#!/usr/bin/env python3
"""The One-Liner Groan-Off entry.

Writes one original one-line dad joke to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR, default /output). Stdlib only,
no network, fully deterministic.
"""

import os

JOKE = "I told my plants I'm rooting for them. They said, 'We're already grounded.'"


def main() -> None:
    # Self-check against the competition gate: 1-140 characters.
    if not 1 <= len(JOKE) <= 140 or not JOKE.strip():
        raise SystemExit("joke fails the 1-140 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file holds exactly the joke, nothing else.
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
