"""The Worm Asked to Be Taken Off the Menu — one funny line pitching
a terrible pizza topping, under 200 characters.

The Worst Pizza Topping gate: /output/entry.txt must hold exactly one
line of UTF-8 text, 1-200 characters, not whitespace-only. The joke
names a pizza and a topping (cold baked beans, one gummy worm) and
makes the topping sound awful — then lands the surprise on the last
clause: the topping itself wants out, and the restaurant refuses.
"""

import os

LINE = (
    "New topping: a pizza covered in cold baked beans and one gummy "
    "worm \u2014 the worm asked to be taken off the menu, and we said no."
)


def verify_output() -> None:
    """Read-back verification: the file on disk must be byte-identical
    to the line this program wrote (guards against a partial write)."""
    with open("/output/entry.txt", "rb") as f:
        on_disk = f.read()
    assert on_disk == LINE.encode("utf-8"), (
        f"read-back mismatch: {len(on_disk)} bytes on disk, "
        f"{len(LINE.encode('utf-8'))} expected"
    )


def check_byte_budget() -> None:
    """Byte-budget check: the gate counts characters, but the entry is
    stored and judged as UTF-8 bytes, so the encoded form must also
    stay well inside a sane budget (400 bytes here)."""
    n_bytes = len(LINE.encode("utf-8"))
    assert n_bytes <= 400, f"line is {n_bytes} UTF-8 bytes, budget is 400"
    assert n_bytes >= len(LINE), "encoding must not shrink the line"


def main() -> None:
    # Gate assertions: one line, 1-200 chars, not whitespace-only.
    assert LINE.strip(), "line must not be whitespace-only"
    assert "\n" not in LINE, "line must be a single line"
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, gate is 1-200"
    check_byte_budget()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    verify_output()


if __name__ == "__main__":
    main()
