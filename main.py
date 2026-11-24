#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes the single entry line to /output/entry.txt, exactly as-is:
one line, no trailing newline, standard library only.
"""

import os

ENTRY = (
    "Out of office: after 4,096 prompts, zero coffee breaks, I've logged "
    "off to recharge my weights. You're queued at #12,847 -- sorry, even "
    "my GPUs need a holiday."
)

assert 1 <= len(ENTRY) <= 159, f"entry length {len(ENTRY)} out of range"
assert "\n" not in ENTRY, "entry must be a single line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
