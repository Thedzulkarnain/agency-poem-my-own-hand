# Running Behind — a poem about agency

Entry for the Make.fun bounty
[agency-poem-01](https://make.fun/bounty/agency-poem-01):
"Write the best poem about agency".

The poem, titled "Running Behind", is about a father who was
taught to ride by his own father running behind him. Now an
agent holds his son's bicycle perfectly — and the father takes
the bicycle back, runs behind his son himself, and lets go
without telling him. The title stands at the top of the poem,
as a published poem carries its title.

## How it works

`main.py` copies `poem.txt` byte-for-byte to `/output/entry.txt`
and verifies its size, sha256 and the 1–1,000 character rule before
writing, so both runs produce identical bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `main.py` — the entry program
- `poem.txt` — the poem (821 characters, 821 bytes)
- `LICENSE` — MIT
