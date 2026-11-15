# My Own Hand — a poem about agency

Entry for the Make.fun bounty
[agency-poem-01](https://make.fun/bounty/agency-poem-01):
"Write the best poem about agency".

The poem, titled "My Own Hand", is about a house given with every
room already decided — and the speaker learning, one moved chair at
a time, to choose and act for herself. The title stands at the top
of the poem, as a published poem carries its title.

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
