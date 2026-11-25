"""The Router Confesses — one-line excuse from a home Wi-Fi router.

Writes a single line (<=200 chars, no trailing newline) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt for local testing).
Python standard library only, no network, deterministic.
"""
import os

ENTRY = "You never look at me until I stop working, so at the climax I stopped \u2014 to finally be seen."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
