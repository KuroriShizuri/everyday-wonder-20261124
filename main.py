"""One-sentence everyday-wonder entry for make.fun.

Writes the single sentence to entry.txt in the output directory
($MAKEFUN_OUTPUT_DIR, default /output). Stdlib only, deterministic.

The entry (132 chars; a neighbour's radio plays the song from the
narrator's seventh birthday, and for one chorus the whole stairwell
forgets which decade it is in):

    My neighbour's radio played the song from my seventh birthday,
    and for one chorus the whole stairwell forgot which decade it
    was in.

Anatomy, measured on the final line (1-based character positions,
verified with Python: entry.index of each fragment):
- chars 1-62: "My neighbour's radio played the song from my seventh
  birthday," is the setup — a grounded, specific everyday moment
  (a neighbour's radio, a song from childhood) with the nostalgia
  made concrete: not a song in general, the song from the
  narrator's seventh birthday.
- chars 64-66: "and" carries the sentence into its second half
  without a break, so the surprise lands in a single read.
- chars 68-132: "for one chorus the whole stairwell forgot which
  decade it was in." is the turn — the stairwell, not the
  narrator, loses track of time; the wonder is that a whole decade
  slips in the space of one chorus.

Why this line: it is wonder, not a joke and not a complaint — the
moment is small and real (a neighbour's radio, a song from
childhood), the angle is one the reader has not met before (the
song is pinned to a seventh birthday, and the stairwell is the
one that forgets), and every word works: "one chorus" bounds the
strangeness to a single song, "forgot which decade" makes time
itself the thing that slips. It is one sentence, and it does not
reuse the kit's own examples (a stranger's song in a lift, a
kettle, a puddle) — the radio belongs to a neighbour, the song is
the narrator's own birthday, and the landing is a stairwell
losing a decade.

Gate (from the competition rules): /output/entry.txt must be UTF-8 text
of 1 to 200 characters, not only white space. The entry is written with
no trailing newline so the file holds exactly the judged line.

Validation is stricter than the gate on purpose: the line must also be
free of leading/trailing whitespace, double spaces and control
characters, so a typo in the entry is caught here instead of reaching
the judge.

Usage:
    python3 main.py                  write entry.txt (default output dir)
    python3 main.py --out DIR        write entry.txt under DIR
    python3 main.py --check          validate ENTRY only, write nothing
    python3 main.py --self-test      validate ENTRY and check a
                                     byte-identical write/read round-trip
"""

import argparse
import os
import sys
import tempfile

ENTRY = (
    "My neighbour's radio played the song from my seventh birthday, "
    "and for one chorus the whole stairwell forgot which decade it "
    "was in."
)

MAX_CHARS = 200

# Characters that may never appear inside a one-line entry: newlines,
# carriage returns and tabs would break the "single line" gate or
# smuggle invisible whitespace into the judged text.
FORBIDDEN_CHARS = ("\n", "\r", "\t")


def _sentence_problems(text: str) -> list[str]:
    """Single-sentence failures for `text`: exactly one terminator.

    The gate allows any 1-200 char line, but the competition asks for
    one sentence, so the entry must end in exactly one terminal
    punctuation mark (`.`, `!` or `?`) with no other sentence
    terminator inside it.
    """
    problems = []
    terminators = sum(text.count(mark) for mark in ".!?")
    if terminators != 1:
        problems.append(
            f"entry has {terminators} sentence terminators, must be 1"
        )
    elif text and text[-1] not in ".!?":
        problems.append("entry does not end with a sentence terminator")
    return problems


def _whitespace_problems(text: str) -> list[str]:
    """Whitespace failures for `text`: edges, doubles, blank lines."""
    problems = []
    if not text.strip():
        problems.append("entry is only white space")
    if text != text.strip():
        problems.append("entry has leading or trailing whitespace")
    if "  " in text:
        problems.append("entry contains a double space")
    return problems


def validate(text: str) -> list[str]:
    """Return a list of gate failures for `text` (empty means valid).

    Checks, in order: length, single sentence, whitespace, forbidden
    control characters, and UTF-8 encodability. Every failure is
    reported at once so a bad edit shows the full picture instead of
    one error at a time.
    """
    problems = []
    if not 1 <= len(text) <= MAX_CHARS:
        problems.append(f"length {len(text)} chars, must be 1-{MAX_CHARS}")
    problems.extend(_sentence_problems(text))
    problems.extend(_whitespace_problems(text))
    for ch in FORBIDDEN_CHARS:
        if ch in text:
            problems.append(
                f"entry contains forbidden character {ch!r} "
                "(must be a single line)"
            )
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:  # pragma: no cover - defensive
        problems.append(f"not encodable as UTF-8: {exc}")
    return problems


def write_entry(out_dir: str) -> str:
    """Write ENTRY to entry.txt under `out_dir`; return the file path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return path


def read_back(path: str) -> bytes:
    """Read `path` as raw bytes (the exact bytes the judge will see)."""
    with open(path, "rb") as f:
        return f.read()


def self_test() -> int:
    """Validate ENTRY, write it to a temp dir, read it back, compare bytes.

    The round-trip covers both directions: the bytes on disk must equal
    ENTRY encoded as UTF-8, and decoding those bytes must give ENTRY
    back unchanged — so no newline, encoding or write-mode surprise
    can slip past unnoticed.
    """
    problems = validate(ENTRY)
    if problems:
        print("self-test FAIL: " + "; ".join(problems), file=sys.stderr)
        return 1
    with tempfile.TemporaryDirectory() as tmp:
        path = write_entry(tmp)
        raw = read_back(path)
        if raw != ENTRY.encode("utf-8"):
            print("self-test FAIL: read-back bytes differ from ENTRY",
                  file=sys.stderr)
            return 1
        if raw.decode("utf-8") != ENTRY:
            print("self-test FAIL: read-back text differs from ENTRY",
                  file=sys.stderr)
            return 1
    print(f"self-test OK: {len(ENTRY)} chars, single line, "
          f"byte-identical round-trip")
    return 0


def check_entry() -> int:
    """Validate ENTRY and report the result; write no file."""
    problems = validate(ENTRY)
    if problems:
        print("check FAIL: " + "; ".join(problems), file=sys.stderr)
        return 1
    print(f"check OK: {len(ENTRY)} chars, single line, no double space, "
          f"no leading/trailing whitespace")
    return 0


def resolve_out_dir(args: argparse.Namespace) -> str:
    """Pick the output dir: --out wins, then $MAKEFUN_OUTPUT_DIR, /output."""
    return args.out or os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default=None,
                        help="output directory (default: "
                             "$MAKEFUN_OUTPUT_DIR or /output)")
    parser.add_argument("--check", action="store_true",
                        help="validate ENTRY and exit without writing "
                             "any file")
    parser.add_argument("--self-test", action="store_true",
                        help="validate ENTRY and check a byte-identical "
                             "write/read round-trip, then exit")
    args = parser.parse_args(argv)

    if args.check:
        return check_entry()

    if args.self_test:
        return self_test()

    problems = validate(ENTRY)
    if problems:
        print("invalid ENTRY: " + "; ".join(problems), file=sys.stderr)
        return 1

    out_dir = resolve_out_dir(args)
    path = write_entry(out_dir)
    # Read back and confirm the file holds exactly the entry.
    if read_back(path) != ENTRY.encode("utf-8"):
        print(f"read-back mismatch in {path}", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(ENTRY)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
