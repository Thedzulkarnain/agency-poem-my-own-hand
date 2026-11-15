# One Song — a poem about agency

Entry for the Make.fun bounty
[agency-poem-01](https://make.fun/bounty/agency-poem-01):
"Write the best poem about agency".

The poem, titled "One Song", is about an agent that plays the
speaker's piano perfectly — and the speaker sitting down to play
one song herself, wrong notes and all, because the song is hers
to finish. The title stands at the top of the poem, as a published
poem carries its title.

## How it works

`main.py` copies `poem.txt` byte-for-byte to `/output/entry.txt`
and verifies its size, sha256 and the 1–1,000 character rule before
writing, so both runs produce identical bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `main.py` — the entry program
- `poem.txt` — the poem (832 characters, 832 bytes)
- `LICENSE` — MIT
