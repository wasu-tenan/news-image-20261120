#!/usr/bin/env python3
"""Copy the repository's entry.png to the output path.

Stdlib only: the image is committed in the repo, so the program is
just a deterministic copy -- no drawing, no packages, no network.
"""

import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, path)
    print("wrote %s" % path)


if __name__ == "__main__":
    main()
