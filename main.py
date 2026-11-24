# One Word From Grandma entry: exactly one word, nothing else.
#
# The word is a fixed string: the program is deterministic by construction,
# so two runs write the same bytes. It reads $MAKEFUN_OUTPUT_DIR when set,
# else /output, and writes entry.txt there.

import os

ENTRY = "Witchcraft"

# The gate requires 1-30 characters of non-whitespace UTF-8 text; guard
# the fixed word so a future edit cannot silently break that contract.
assert 1 <= len(ENTRY) <= 30 and ENTRY.strip() == ENTRY and " " not in ENTRY

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
