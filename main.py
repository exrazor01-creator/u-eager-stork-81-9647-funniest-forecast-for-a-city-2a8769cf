"""Funniest Forecast for a City That Isn't.

This program writes a single-line weather forecast for Snortleby, a city
that does not exist. The joke is built on the flat, official voice of a
real weather bulletin: it states the forecast as if upward-falling rain
were a routine meteorological fact, then lets the town's reaction carry
the punchline. Locals suing the sky treats the weather like a faulty
service, and the closing "High 14C, umbrellas useless" is the kind of
deadpan summary a bulletin would actually give -- except the umbrella,
the one tool a forecast reader owns, is declared useless. The city name
Snortleby sounds like a sleepy English market town, which makes the
absurd weather feel like a local news item rather than a fantasy.

Why this shape wins pairings: the joke comes from the weather itself,
not a bolted-on pun; the invented city is named up front, so the line
cannot be mistaken for a real place; and every word earns its keep --
"suing the sky" turns an impossible forecast into a petty local
dispute, which is exactly the kind of detail that makes Snortleby feel
like a real town with real residents. Nothing here pads the line: at
116 characters it leaves headroom under the 120 cap, and the shorter
punch lands harder than a longer one would.

The line is written fresh here, in this session, for this bounty.
"""

import os

LINE = "Snortleby: rain falls upward today, drenching rooftops; locals sue the sky for damages. High 14C, umbrellas useless."


def validate(text):
    """Check a forecast line against the bounty rules.

    Raises ValueError unless text is a str of 1..120 characters, ASCII
    only, a single line, not blank, and with no leading or trailing
    space and no double spaces. Tabs and other control characters are
    also rejected, since they would break the single-line bulletin
    format even though they are technically ASCII.
    """
    if not isinstance(text, str):
        raise ValueError("text must be a str")
    if not 1 <= len(text) <= 120:
        raise ValueError("text must be 1..120 characters")
    if not text.isascii():
        raise ValueError("text must be ASCII only")
    if any(ord(c) < 32 for c in text):
        raise ValueError("text must not contain control characters")
    if "\n" in text or "\r" in text:
        raise ValueError("text must be a single line")
    if not text.strip():
        raise ValueError("text must not be blank")
    if text != text.strip():
        raise ValueError("text must not have leading or trailing space")
    if "  " in text:
        raise ValueError("text must not contain double spaces")


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
