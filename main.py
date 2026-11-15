#!/usr/bin/env python3
"""agency-poem-01 entry: copy the poem to /output/entry.txt.

"My Own Hand" — a poem about agency: a house given with every
room already decided, and the speaker learning, one moved chair
at a time, to choose and act for herself. The title stands at
the top of the poem, as a published poem carries its title.
"""
import hashlib
import os

POEM_SHA256 = "851cc886a1b16050269b7f5d33a42d4e3d5de0c2663c022cb4531497b6cc331a"
POEM_SIZE = 799


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "poem.txt")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    with open(src, "rb") as f:
        data = f.read()
    assert len(data) == POEM_SIZE, f"poem.txt size {len(data)} != {POEM_SIZE}"
    assert hashlib.sha256(data).hexdigest() == POEM_SHA256, "poem.txt sha256 mismatch"
    text = data.decode("utf-8")
    assert 1 <= len(text) <= 1000, f"poem is {len(text)} chars, must be 1-1000"
    assert text.strip(), "poem must not be only whitespace"
    with open(dst, "wb") as f:
        f.write(data)
    print(f"wrote {dst} ({len(text)} chars, {len(data)} bytes)")
    print("entry ready: My Own Hand — a poem about agency")


if __name__ == "__main__":
    main()
