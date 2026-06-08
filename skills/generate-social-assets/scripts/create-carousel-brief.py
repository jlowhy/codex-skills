#!/usr/bin/env python3
"""Create a starter slides.json for generate-social-assets."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--author", default="Jonathan Low")
    parser.add_argument("--brand", default="Mistle")
    args = parser.parse_args()

    data = {
        "title": args.title,
        "author": args.author,
        "brand": args.brand,
        "format": {
            "width": 1080,
            "height": 1350,
        },
        "brief": {
            "audience": "",
            "intended_reader_change": "",
            "source": "",
            "claim_risk": "",
            "cta": "",
        },
        "slides": [
            {
                "kind": "cover",
                "eyebrow": args.brand,
                "title": args.title,
                "body": "Replace with the core promise or tension.",
                "footer": "Swipe",
            },
            {
                "kind": "point",
                "eyebrow": "1",
                "title": "First point",
                "body": "Keep this to one idea. Split if it needs a second paragraph.",
            },
            {
                "kind": "point",
                "eyebrow": "2",
                "title": "Second point",
                "body": "Use concrete examples rather than generic advice.",
            },
            {
                "kind": "cta",
                "eyebrow": "Next",
                "title": "What should the reader do now?",
                "body": "Ask a question, invite replies, or point to the next manual action.",
                "footer": args.author,
            },
        ],
    }

    out = Path(args.out).expanduser()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
