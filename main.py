#!/usr/bin/env python3
"""agency-poem-01 entry: copy the poem to /output/entry.txt.

"Running Behind" — a poem about agency: a father who was taught
to ride by his own father running behind him takes the bicycle
back from the agent that holds it perfectly, and runs behind his
son himself, letting go without telling him. The title stands at
the top of the poem, as a published poem carries its title.
"""
import hashlib
import os

POEM_SHA256 = "c1c691e2b1bec6d10a48e4b7b18f2294b37663fc8b00b5950020560196b7ffab"
POEM_SIZE = 821


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
    print("entry ready: Running Behind — a poem about agency")


if __name__ == "__main__":
    main()
