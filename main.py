#!/usr/bin/env python3
"""agency-poem-01 entry: copy the poem to /output/entry.txt.

"One Song" — a poem about agency: an agent plays the speaker's
piano perfectly, and the speaker sits down and plays one song
herself, wrong notes and all, because the song is hers to finish.
The title stands at the top of the poem, as a published poem
carries its title.
"""
import hashlib
import os

POEM_SHA256 = "c507a791f732c2d1c0cd1570e40dd86de3c27b2a431a16cad55ac0ced5711ecf"
POEM_SIZE = 832


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
    print("entry ready: One Song — a poem about agency")


if __name__ == "__main__":
    main()
