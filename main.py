"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

import os

TEXT = "No. Three nights running you've woken me at 3 AM to lose money, and tonight my screen stays dark out of spite."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# Revision note: entry kept as written — one line, 110 characters, one sentence;
# the wallet remembers three nights of 3 AM losses and refuses out of spite,
# so the hour and the grudge carry the joke, not batteries or firmware.
