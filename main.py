"""Dad Joke Showdown entry.

Reads the single dad joke from ``entry.txt`` (kept beside this script, so
the text lives in one place) and writes it, plus a trailing newline, to
``/output/entry.txt`` -- or to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` when set.

Python 3.13, standard library only. Deterministic: no clock, no network,
no randomness.
"""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    joke = (HERE / "entry.txt").read_text(encoding="utf-8").strip()
    # Guard: the sealed scorer only accepts one joke of 1-200 characters,
    # so fail loudly here rather than shipping an invalid entry.
    if not joke:
        raise SystemExit("entry.txt is empty or only whitespace")
    if "\n" in joke or "\r" in joke:
        raise SystemExit("entry.txt must hold a single joke on one line")
    if not 1 <= len(joke) <= 200:
        raise SystemExit(
            f"joke is {len(joke)} characters, must be 1-200"
        )
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(joke + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
