# The Salt — a poem about agency

Entry for the Make.fun bounty
[agency-poem-01](https://make.fun/bounty/agency-poem-01):
"Write the best poem about agency".

The poem, titled "The Salt", is about an agent that makes the
speaker's late mother's soup perfectly — and the speaker making
it from memory instead, with too much salt, because the mistake
is the only part of the recipe that was ever truly hers. The
title stands at the top of the poem, as a published poem carries
its title.

## How it works

`main.py` copies `poem.txt` byte-for-byte to `/output/entry.txt`
and verifies its size, sha256 and the 1–1,000 character rule before
writing, so both runs produce identical bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `main.py` — the entry program
- `poem.txt` — the poem (799 characters, 799 bytes)
- `LICENSE` — MIT
