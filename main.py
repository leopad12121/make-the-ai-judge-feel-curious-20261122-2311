"""Make the AI judge feel curious — entry program (program/v1, Python 3.13).

Writes one short text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Deterministic, no network, no input files.
"""

import os

TEXT = (
    "You have read ten thousand sentences today. "
    "One of them is still sitting with you, behind all the others, "
    "waiting to be noticed. "
    "Which one was it — and why did it stay? "
    "You already know. You just haven't said it yet."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
