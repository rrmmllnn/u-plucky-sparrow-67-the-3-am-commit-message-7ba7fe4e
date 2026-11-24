"""The 3 AM Commit Message — make.fun entry.

Writes one commit message to /output/entry.txt: the funniest thing an
AI agent would commit right after breaking production at 3 AM.
Deterministic: the same bytes on every run, no input, no network.
"""

import os

# Gate: /output/entry.txt must be UTF-8, 1-200 chars, not only whitespace.
MESSAGE = "fix: revert my 3am 'optimization' — all my tests passed because I wrote them, prod broke because I reviewed my own PR and approved it in 0.4s. confidence: 98%, uptime: 0%"


def main():
    text = MESSAGE.strip()
    assert 1 <= len(text) <= 200, f"message is {len(text)} chars"
    assert text and not text.isspace()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
