#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line — make.fun entry.

One sentence, at most 200 characters, that makes a small everyday moment
feel strange and new. Written to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt), with no trailing newline.

The entry, 132 characters: a neighbour's radio plays the song from the
narrator's seventh birthday, and for one chorus the whole stairwell
forgets which decade it is in. One sentence, one chorus, one lost decade.

Usage:
    python3 main.py                  # write the entry
    python3 main.py --check          # validate only, write nothing
    python3 main.py --self-test      # validate, then write to a temp dir
                                     # and read the bytes back, byte-identical
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


def find_problems(text):
    """Collect every problem with the entry text (empty list means valid)."""
    problems = []
    if not text:
        problems.append("entry is empty")
    elif not text.strip():
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


def report(problems, prefix="error"):
    """Print each problem to stderr, one per line."""
    for problem in problems:
        print("%s: %s" % (prefix, problem), file=sys.stderr)


def write_entry(path):
    """Validate ENTRY and write it to path (no trailing newline)."""
    problems = find_problems(ENTRY)
    if problems:
        report(problems)
        return 1
    parent = os.path.dirname(os.path.abspath(path))
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    return 0


def read_back(path):
    """Read a file as raw bytes."""
    with open(path, "rb") as handle:
        return handle.read()


def describe_entry():
    """One-line summary of the entry's size, for the self-test output."""
    return "characters: %d (limit %d), bytes (UTF-8): %d" % (
        len(ENTRY), MAX_CHARS, len(ENTRY.encode("utf-8")))


def self_test():
    """Validate ENTRY, write it to a temp dir, read back, compare bytes."""
    problems = find_problems(ENTRY)
    if problems:
        report(problems, prefix="self-test FAIL")
        return 1
    print("entry: %s" % ENTRY)
    print(describe_entry())
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "entry.txt")
        if write_entry(path) != 0:
            print("self-test FAIL: write failed", file=sys.stderr)
            return 1
        raw = read_back(path)
        if raw != ENTRY.encode("utf-8"):
            print("self-test FAIL: read-back bytes differ", file=sys.stderr)
            return 1
        if raw.endswith(b"\n"):
            print("self-test FAIL: trailing newline present", file=sys.stderr)
            return 1
    print("self-test PASS: write + byte-identical read-back, no trailing newline")
    return 0


def default_output_path():
    """Resolve the output path from the environment (or the /output default)."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


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
        problems = find_problems(ENTRY)
        if problems:
            report(problems)
            return 1
        print("check PASS: %d characters, within the %d limit"
              % (len(ENTRY), MAX_CHARS))
        return 0

    path = args.output if args.output else default_output_path()
    return write_entry(path)


if __name__ == "__main__":
    sys.exit(main())
