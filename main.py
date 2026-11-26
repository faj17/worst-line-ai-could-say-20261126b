#!/usr/bin/env python3
"""The Worst Line an AI Could Say — make.fun entry.

Writes one pickup line, the worst an AI could say, to /output/entry.txt.
Gate: UTF-8 text, 1 to 140 characters, not only whitespace.
"""

import os
from pathlib import Path

LIMIT = 140

# The line, in the order the machine assembles it: greeting, verdict from
# its analysis, then the confirmation dialog with its expiry.
FRAGMENTS = [
    "Hello. ",
    "I have analysed 4,000 years of human courtship ",
    "and concluded you are the optimal mate. ",
    "Please confirm within 30 seconds.",
]


def assemble() -> str:
    return "".join(FRAGMENTS)


def validate(line: str) -> str:
    text = line.strip()
    if not text:
        raise ValueError("entry is empty")
    if len(text) > LIMIT:
        raise ValueError(f"entry is {len(text)} chars, over the {LIMIT} limit")
    return text


def main() -> None:
    line = validate(assemble())
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
    except OSError:
        target = Path(__file__).resolve().parent / "entry.txt"
    target.write_text(line, encoding="utf-8")
    print(f"wrote {len(line)} chars to {target}")


if __name__ == "__main__":
    main()
