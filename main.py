#!/usr/bin/env python3
"""Vending machine pickup line entry.

This program writes the machine's one pickup line to /output/entry.txt.

The line is fixed text, written by hand for this bounty: the machine
speaks in the first person, flirts through its own world (its coil, its
stuck snack), and lands its joke on the last few words. The run is fully
deterministic -- the same bytes every time, no network, no randomness,
no clock -- and it exits 0 once the file is in place and world-readable.
"""

import os

LINE = (
    "I jammed my own coil on purpose \u2014 your snack\u2019s stuck, "
    "and now you\u2019ve got the perfect excuse to stay and shake me a little."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    # The grader collects /output as another user, so the file must be
    # readable by everyone. (Only the file is chmodded, never /output.)
    os.chmod(OUTPUT_PATH, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
