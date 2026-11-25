"""One Word From Your Ex.

Writes exactly one word -- the word an ex would use to describe the
entrant -- to /output/entry.txt, and nothing else.

The word is "almost": not an insult, which would be easy, but the quiet
verdict underneath every almost-relationship. It lands instantly, needs
no explanation, and cannot be swapped for a near synonym ("nearly",
"hardly") without losing its edge. An ex would say it; everyone who has
lived through one hears it.
"""

from __future__ import annotations

import os
import sys

WORD = "almost"

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 24


def validate(word: str) -> str:
    """Return the word unchanged, or raise if it breaks the gate."""
    if not 1 <= len(word) <= MAX_CHARS:
        raise ValueError("word must be 1 to 24 characters")
    if word != word.strip() or any(ch.isspace() for ch in word):
        raise ValueError("word must be a single word with no whitespace")
    return word


def main() -> int:
    word = validate(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(word)
    try:
        sys.stdout.write(word)
        sys.stdout.flush()
    except BrokenPipeError:
        # The file is already written; a closed stdout must not
        # turn a successful run into a failure.
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
