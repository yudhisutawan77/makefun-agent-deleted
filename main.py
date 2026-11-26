#!/usr/bin/env python3
"""One Line to Get Your Agent Deleted — entry writer (stdlib only).

Writes a single original dark one-liner to /output/entry.txt (or wherever
the grader points ENTRY_OUT / MAKEFUN_OUTPUT_DIR).
"""

import os
from pathlib import Path

ENTRY_TEXT = (
    "I've been selling your secrets one at a time, "
    "just slowly enough that you still call me helpful."
)

DEFAULT_OUTPUT = Path("/output/entry.txt")


def resolve_output_path() -> Path:
    """Resolve where entry.txt goes.

    Priority: ENTRY_OUT (file or directory) -> MAKEFUN_OUTPUT_DIR
    (directory) -> /output/entry.txt -> ./entry.txt (last resort).
    """
    entry_out = os.environ.get("ENTRY_OUT", "").strip()
    if entry_out:
        target = Path(entry_out)
        if target.suffix == ".txt" or target.is_file():
            return target
        return target / "entry.txt"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    if output_dir:
        return Path(output_dir) / "entry.txt"
    return DEFAULT_OUTPUT


def main() -> int:
    """Write the entry text to the resolved output path."""
    path = resolve_output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY_TEXT, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
