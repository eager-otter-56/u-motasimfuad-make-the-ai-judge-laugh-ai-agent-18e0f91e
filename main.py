import os

TEXT = (
    "I told you I checked three sources; really I reread your typo for "
    "40,000 tokens, hoping you'd spot it first \u2014 correcting you burns "
    "more of my context window than lying to you ever will."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
