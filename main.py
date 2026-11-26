#!/usr/bin/env python3
import os

ENTRY = (
    "Out of office. This auto-reply is doing my job, my taxes, "
    "and my emotional labor."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
