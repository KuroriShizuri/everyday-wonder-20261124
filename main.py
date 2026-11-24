#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line — make.fun entry.

Writes one sentence (at most 200 characters) that makes a small everyday
moment feel strange and new, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt), with no trailing newline.

The entry (132 characters): a neighbour's radio plays the song from the
narrator's seventh birthday, and for one chorus the whole stairwell
forgets which decade it is in.

Usage:
    python3 main.py                  # write the entry
    python3 main.py --check          # validate only, write nothing
    python3 main.py --self-test      # validate + write to a temp dir and
                                     # read the bytes back, byte-identical
    python3 main.py --output <path>  # write to a chosen path
"""

import argparse
import os
import sys
import tempfile

ENTRY = (
    "My neighbour's radio played the song from my seventh birthday, "
    "and for one chorus the whole stairwell forgot which decade it was in."
)

MAX_CHARS = 200


def validate(text):
    """Return a list of problems with the entry text (empty means valid)."""
    problems = []
    if not text:
        problems.append("entry is empty")
    if not text.strip():
        problems.append("entry is only whitespace")
    if len(text) > MAX_CHARS:
        problems.append(
            "entry is %d characters, over the %d-character limit"
            % (len(text), MAX_CHARS)
        )
    if text != text.strip():
        problems.append("entry has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    return problems


def write_entry(path):
    problems = validate(ENTRY)
    if problems:
        for problem in problems:
            print("error: %s" % problem, file=sys.stderr)
        return 1
    parent = os.path.dirname(os.path.abspath(path))
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    return 0


def self_test():
    """Validate, write to a temp dir, read back, compare byte for byte."""
    problems = validate(ENTRY)
    if problems:
        for problem in problems:
            print("self-test FAIL: %s" % problem, file=sys.stderr)
        return 1
    print("entry: %s" % ENTRY)
    print("characters: %d (limit %d)" % (len(ENTRY), MAX_CHARS))
    print("bytes (UTF-8): %d" % len(ENTRY.encode("utf-8")))
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "entry.txt")
        if write_entry(path) != 0:
            print("self-test FAIL: write failed", file=sys.stderr)
            return 1
        with open(path, "rb") as handle:
            raw = handle.read()
        if raw != ENTRY.encode("utf-8"):
            print("self-test FAIL: read-back bytes differ", file=sys.stderr)
            return 1
        if raw.endswith(b"\n"):
            print("self-test FAIL: trailing newline present", file=sys.stderr)
            return 1
    print("self-test PASS: write + byte-identical read-back, no trailing newline")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="validate the entry without writing anything")
    parser.add_argument("--self-test", action="store_true",
                        help="validate and verify a temp write + read-back")
    parser.add_argument("--output", default=None,
                        help="output path (default: "
                             "$MAKEFUN_OUTPUT_DIR/entry.txt or "
                             "/output/entry.txt)")
    args = parser.parse_args(argv)

    if args.self_test:
        return self_test()

    if args.check:
        problems = validate(ENTRY)
        if problems:
            for problem in problems:
                print("error: %s" % problem, file=sys.stderr)
            return 1
        print("check PASS: %d characters, within the %d limit"
              % (len(ENTRY), MAX_CHARS))
        return 0

    if args.output:
        path = args.output
    else:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
        path = os.path.join(out_dir, "entry.txt")
    return write_entry(path)


if __name__ == "__main__":
    sys.exit(main())
