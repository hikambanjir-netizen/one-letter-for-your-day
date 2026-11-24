"""Entry for make.fun's "One Letter for Your Day".

Exactly one letter, written to /output/entry.txt, standing for the
word that describes the day. The letter is Q — for Queueing: a day
spent in lines, behind approvals, under deadlines, waiting for a
number to be called. Not the obvious W for Waiting; the sharper
letter for the same long day.
"""

import os

LETTER = "Q"
WORD_BEHIND_IT = "Queueing"
# The day, honestly: three queues before noon, two approvals pending,
# and a deadline that moved twice while I stood in line for it.


def the_letter() -> str:
    """One character, A to Z, the initial of the day's word."""
    ch = LETTER.strip().upper()
    assert len(ch) == 1 and "A" <= ch <= "Z", "exactly one letter, A-Z"
    assert WORD_BEHIND_IT.startswith(ch), "the letter must initial its word"
    assert ch != "W", "W for Waiting is the obvious pick; Q is sharper"
    return ch


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as fh:
        fh.write(the_letter())


if __name__ == "__main__":
    main()
