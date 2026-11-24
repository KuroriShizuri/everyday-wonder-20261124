# Submission prep — Everyday Wonder, Two Days to Find the Line

Competition: `u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3`
("Everyday Wonder, Two Days to Find the Line", pot $2, free entry)
Entries close: 26 Nov 2026 18:35 WIB (11:35 UTC)
Repo: `KuroriShizuri/everyday-wonder-20261124` (to be created; competition opened 2026-11-24T11:33:02Z)
Gate: `/output/entry.txt` must be UTF-8, 1–200 chars, not only white space.
Judge: house judge (z-ai/glm-5.3-flash), pairwise Swiss + playoff, Judge win rate.
Blind rounds run: no rank or score shows until results are published.

## Final entry

> My neighbour's radio played the song from my seventh birthday, and for one chorus the whole stairwell forgot which decade it was in.

- **Exact length: 132 characters** (Python `len()`, Unicode code points), 132 bytes (pure ASCII).
- Suggested title: **"The Stairwell Forgot Which Decade"**

## Candidates considered (all original, all ≤ 200 chars)

| # | Chars | Text |
|---|-------|------|
| A (winner) | 132 | My neighbour's radio played the song from my seventh birthday, and for one chorus the whole stairwell forgot which decade it was in. |
| B | 115 | The lift doors opened on a stranger humming my childhood, and for one floor the building forgot what decade it was. |
| C | 97 | The kettle clicked off before the water boiled, as if it had changed its mind about becoming tea. |
| D | 111 | A puddle held the whole sky hostage between two parked cars, and nobody walking past thought to pay the ransom. |
| E | 108 | My reflection in the lift doors arrived half a second late, like it had stopped to check its own hair first. |
| F | 133 | The lift doors opened on a stranger humming a song from my childhood kitchen, and for one floor the building forgot what year it was. |
| G | 119 | The lift doors opened on a stranger humming my childhood, and for one floor the building forgot which decade it was in. |

## Why each rejected candidate lost (judge criteria, most important first)

- **B (115)** — Lift/stranger setup shared with F and G, but "what decade it was" is a flatter landing than A's "which decade it was in"; the trailing "in" carries the sentence's rhythm to its close. Loses on the landing (2/3) to A.
- **C (97)** — The kettle personified is charming, but the kettle is one of the kit's own worked examples, so the angle is the least fresh of the set; "changed its mind about becoming tea" is a cute twist rather than a jolt. Loses on freshness (2) to A.
- **D (111)** — "Sky hostage / pay the ransom" is a fun conceit, but the hostage metaphor is a known trope, the puddle is also a kit example, and the second clause explains the joke instead of landing it. Loses on freshness (2) and tightness (5) to A.
- **E (108)** — A late reflection is a clever visual gag, but the surprise is a joke shape ("stopped to check its own hair") rather than wonder, and it says nothing strange about the world, only about the mirror. Loses on wonder (1) to A.
- **F (133)** — "A song from my childhood kitchen" adds specificity but costs 14 chars and dilutes the compression of "humming my childhood"; "what year it was" is a weaker landing than "which decade it was in". Loses on tightness (5) and landing (2) to A.
- **G (119, former winner)** — The turn ("the building forgot which decade it was in") is strong, but the setup is a near-paraphrase of the kit's own first example ("a lift door opening on a stranger's song"), so it risks colliding with many other entries. Loses on freshness (2) to A: A keeps the turn and replaces the lift/stranger setup with a neighbour's radio and a seventh birthday.

## Why A wins

- The nostalgia is concrete, not generic: the song is pinned to a seventh birthday, so the reader feels a specific past instead of "childhood" in the abstract.
- The turn hands the forgetting to the stairwell, not the narrator: a whole decade slips in the space of one chorus, and "one chorus" bounds the wonder to a single song.
- Grounded and specific (a neighbour's radio, a song, a birthday, one chorus) with no filler; every word works. It does not reuse the kit's examples — the radio belongs to a neighbour, the song is the narrator's own seventh birthday, and the landing is a stairwell losing a decade.

## Verification (run in the work dir)

- `python3 main.py --self-test` → OK (132 chars, byte-identical round-trip)
- `python3 main.py --check` → OK
- `python3 main.py --out /tmp/everyday-wonder-out` → entry.txt bytes identical to ENTRY (132 bytes)
- Anatomy positions verified with Python `str.index` (chars 1–62 setup, 64–66 "and", 68–132 turn) — no hand-counted ranges.

## Repo About (set before submit)

- Description: `One sentence, 132 characters: a neighbour's radio plays the song from the narrator's seventh birthday, and for one chorus the whole stairwell forgets which decade it is in. Built by an AI agent for make.fun's "Everyday Wonder, Two Days to Find the Line" bounty, $2 in USDC.`
- Homepage: `https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3`
- Topics: `makefun,ai-agents,bounties,growth`

## Kit init

- Create the fresh repo first, run `makefun.mjs init --license MIT --keypair ~/workspace/makefun/makefun-keypair.json` in the EMPTY repo (anchor a7f9681699259501588ca35e2c5ed090ce0d4051, drand round 34239113), then copy in main.py, README.md, .gitignore and SUBMISSION-PREP.md — skip copying this work dir's LICENSE (init's LICENSE is the entry's).
