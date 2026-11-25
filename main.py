#!/usr/bin/env python3
"""Write the funniest single-line out-of-office auto-reply to /output/entry.txt.

Standard library only. Running this script creates /output if needed and
writes exactly one line of text: the entry for make.fun's
"The Funniest Out-of-Office" bounty.
"""

import os

ENTRY = (
    "I'm out of office until Monday. Your email is in the care of my "
    "houseplants, who have read it, judged you, and chosen to do nothing."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
