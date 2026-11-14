#!/usr/bin/env python3
"""Copy the ramen artwork into the runtime output folder."""

import os
import shutil
from pathlib import Path


def main() -> None:
    # Resolve where this script lives so we can find the bundled image.
    here = Path(__file__).resolve().parent
    source = here / "entry.png"

    # Honour the platform hint, otherwise fall back to the usual mount.
    target_dir_name = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target_dir = Path(target_dir_name)
    target_dir.mkdir(parents=True, exist_ok=True)

    destination = target_dir / "entry.png"

    # A straightforward byte-for-byte copy keeps the result deterministic.
    shutil.copyfile(source, destination)


if __name__ == "__main__":
    main()

# End of entry point — the picture does the talking.
