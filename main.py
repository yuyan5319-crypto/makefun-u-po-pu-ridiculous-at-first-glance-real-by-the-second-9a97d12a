#!/usr/bin/env python3
"""Write one original pitch sentence to entry.txt.

The pitch: a bizarre startup idea that sounds ridiculous at first glance
but turns out to be a real business by the second.
"""

import os
import sys

SENTENCE = (
    "We rent herds of trained goats to mow suburban lawns, charging "
    "homeowners by the square foot, because the goats eat the weeds, "
    "fertilize as they go, and undercut every landscaping crew in town."
)

MAX_CHARS = 200


def main() -> int:
    sentence = SENTENCE.strip()
    if not sentence:
        print("error: sentence is empty", file=sys.stderr)
        return 1
    if len(sentence) > MAX_CHARS:
        print(
            f"error: sentence is {len(sentence)} chars, over the "
            f"{MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    if "\n" in sentence or "\r" in sentence:
        print("error: sentence must be a single line", file=sys.stderr)
        return 1
    if sentence != sentence.strip():
        print("error: sentence has leading/trailing whitespace",
              file=sys.stderr)
        return 1
    if "  " in sentence:
        print("error: sentence contains a double space", file=sys.stderr)
        return 1
    if not sentence.endswith("."):
        print("error: sentence must end with a full stop", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if not os.path.isdir(out_dir):
        out_dir = "./output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(sentence)  # no trailing newline: exactly one line
    print(f"wrote {len(sentence)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
