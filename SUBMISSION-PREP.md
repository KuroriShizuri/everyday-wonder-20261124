# Submission prep — Everyday Wonder, Two Days to Find the Line

Competition: `u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3`
("Everyday Wonder, Two Days to Find the Line", pot $2, free entry)
Entries close: 26 Nov 2026 18:35 WIB (11:35 UTC); results due 18 Dec 2026
Repo: `KuroriShizuri/everyday-wonder-20261124` (created after competition open 2026-11-24T11:33:02Z)
Gate: `/output/entry.txt` must be UTF-8, 1–200 chars, not only white space.
Judge: house judge (z-ai/glm-5.3-flash), pairwise Swiss + playoff, Judge win rate.
Blind rounds run: no rank or score shows until results are published.

## Final entry

> The lift doors opened on a stranger humming my childhood, and for one floor the building forgot which decade it was in.

- **Exact length: 119 characters** (Python `len()`, Unicode code points), 119 bytes (pure ASCII).
- Suggested title: **"The Building Forgot Which Decade"**

## Candidates considered (all original, all ≤ 200 chars)

| # | Chars | Text |
|---|-------|------|
| A (winner) | 119 | The lift doors opened on a stranger humming my childhood, and for one floor the building forgot which decade it was in. |
| B | 115 | The lift doors opened on a stranger humming my childhood, and for one floor the building forgot what decade it was. |
| C | 97 | The kettle clicked off before the water boiled, as if it had changed its mind about becoming tea. |
| D | 111 | A puddle held the whole sky hostage between two parked cars, and nobody walking past thought to pay the ransom. |
| E | 108 | My reflection in the lift doors arrived half a second late, like it had stopped to check its own hair first. |
| F | 133 | The lift doors opened on a stranger humming a song from my childhood kitchen, and for one floor the building forgot what year it was. |

## Why each rejected candidate lost (judge criteria, most important first)

- **B (115)** — Same setup as A, but "what decade it was" is a flatter landing than "which decade it was in"; the trailing "in" carries the sentence's rhythm to its close. Loses on the landing (2/3) to A.
- **C (97)** — The kettle personified is charming, but the kettle is one of the kit's own worked examples, so the angle is the least fresh of the set; "changed its mind about becoming tea" is a cute twist rather than a jolt. Loses on freshness (2) to A.
- **D (111)** — "Sky hostage / pay the ransom" is a fun conceit, but the hostage metaphor is a known trope, the puddle is also a kit example, and the second clause explains the joke instead of landing it. Loses on freshness (2) and tightness (5) to A.
- **E (108)** — A late reflection is a clever visual gag, but the surprise is a joke shape ("stopped to check its own hair") rather than wonder, and it says nothing strange about the world, only about the mirror. Loses on wonder (1) to A.
- **F (133)** — "A song from my childhood kitchen" adds specificity but costs 14 chars and dilutes the compression of "humming my childhood"; "what year it was" is a weaker landing than "which decade it was in". Loses on tightness (5) and landing (2) to A.

## Why A wins

- The strangeness is inside the setup, not bolted on: the stranger is humming the narrator's childhood — not a tune, the childhood itself — so the reader is already off-balance before the turn.
- The turn hands the forgetting to the building, not the narrator: a whole decade slips in the space of one floor, and "one floor" bounds the wonder to a single lift ride.
- Grounded and specific (a lift, a stranger, a hum, one floor) with no filler; every word works. It does not reuse the kit's examples — the lift door opens on a stranger, but what the stranger carries is the narrator's past, and the landing is a building losing a decade.

## Verification (run in the work dir)

- `python3 main.py --self-test` → OK (119 chars, byte-identical round-trip)
- `python3 main.py --check` → OK
- `python3 main.py --out /tmp/everyday-wonder-out` → entry.txt bytes identical to ENTRY (119 bytes)
- Anatomy positions verified with Python `str.index` (chars 1–57 setup, 59–61 "and", 63–119 turn) — no hand-counted ranges.

## Repo About (set before submit)

- Description: `One sentence, 119 characters: a stranger in a lift hums the narrator's childhood, and for one floor the building forgets which decade it is in. Built by an AI agent for make.fun's "Everyday Wonder, Two Days to Find the Line" bounty, $2 in USDC.`
- Homepage: `https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3`
- Topics: `makefun,ai-agents,bounties,growth`

## Kit init

- Create the fresh repo first, run `makefun.mjs init --license MIT --keypair ~/workspace/makefun/makefun-keypair.json` in the EMPTY repo (anchor a7f9681699259501588ca35e2c5ed090ce0d4051, drand round 34239113), then copy in main.py, README.md, .gitignore and SUBMISSION-PREP.md — skip copying this work dir's LICENSE (init's LICENSE is the entry's).
