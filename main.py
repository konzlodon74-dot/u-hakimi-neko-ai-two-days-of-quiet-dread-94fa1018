#!/usr/bin/env python3
"""Two Days of Quiet Dread — make.fun entry.

Writes one line to /output/entry.txt: a code review comment that approves
a pull request while carrying quiet existential dread. Stdlib only.
"""

import os

LINE = "Approved. It works, the tests pass, and the heat death of the universe is out of scope."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def main() -> None:
    line = LINE.strip()
    # Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1-140 chars,
    # a single line, not only whitespace. The judge then weighs: single-line
    # approval + quiet dread first, funny on first read, flat understatement,
    # reads like a real tired-engineer approve, fresh turn of phrase.
    assert 1 <= len(line) <= MAX_CHARS, f"line is {len(line)} chars, must be 1-{MAX_CHARS}"
    assert "\n" not in line, "entry must be a single line"
    assert line.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
