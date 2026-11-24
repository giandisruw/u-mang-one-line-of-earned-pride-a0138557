"""One Line of Earned Pride — make.fun entry.

Writes a single line of text (1-240 characters) to /output/entry.txt:
a quiet, earned moment of pride for a small person doing something hard.
No network, no secrets, no dependencies: pure standard library.
The line was chosen over four other candidates in a local pairwise
judgement against the house brief: a concrete scene with a real person
(Joko, his hands, his key, his engine), pride earned inside the line by
felt difficulty (rebuilt from scrap; coughed, caught, kept running),
landing in one read, and a fresh image — no trophy, podium or graduation.
"""

import os

LINE = (
    "Joko wiped the grease from his hands, turned the key, and the engine "
    "he had rebuilt from scrap coughed, caught, and kept running all the "
    "way home."
)

# The harness runs this program in a sandbox and reads /output/entry.txt.
# OUTPUT_PATH may be overridden for local testing only; it always
# defaults to the path the bounty requires.
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    line = LINE.strip()
    if not (1 <= len(line) <= 240):
        raise ValueError(f"line must be 1-240 characters, got {len(line)}")
    if line != line.strip() or "\n" in line:
        raise ValueError("entry must be exactly one line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
