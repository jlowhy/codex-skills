#!/usr/bin/env python3
"""Fetch a YouTube transcript and emit timestamped rows."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlparse


def video_id(value: str) -> str:
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", value):
        return value

    parsed = urlparse(value)
    if parsed.netloc.endswith("youtu.be"):
        candidate = parsed.path.strip("/").split("/")[0]
        if re.fullmatch(r"[A-Za-z0-9_-]{11}", candidate):
            return candidate

    query_id = parse_qs(parsed.query).get("v", [""])[0]
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", query_id):
        return query_id

    raise SystemExit(f"Could not determine YouTube video id from: {value}")


def stamp(seconds: float) -> str:
    total = int(seconds)
    hours = total // 3600
    minutes = (total % 3600) // 60
    secs = total % 60
    if hours:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    return f"{minutes}:{secs:02d}"


def fetch(video: str, languages: list[str]):
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ModuleNotFoundError as exc:
        raise SystemExit(
            "Missing youtube-transcript-api. Run with:\n"
            "uv run --with youtube-transcript-api python scripts/fetch_youtube_transcript.py ..."
        ) from exc

    api = YouTubeTranscriptApi()
    return api.fetch(video, languages=languages)


def as_dict(item) -> dict:
    return {
        "start": float(item.start),
        "duration": float(item.duration),
        "timestamp": stamp(item.start),
        "text": item.text.strip(),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("video", help="YouTube URL or video id")
    parser.add_argument("--language", action="append", default=["en"], help="Preferred caption language")
    parser.add_argument("--format", choices=["tsv", "json", "markdown"], default="tsv")
    parser.add_argument("--output", help="Output file; defaults to stdout")
    args = parser.parse_args()

    vid = video_id(args.video)
    rows = [as_dict(item) for item in fetch(vid, args.language)]

    if args.format == "json":
        output = json.dumps(rows, ensure_ascii=False, indent=2)
    elif args.format == "markdown":
        output = "\n".join(f"- {row['timestamp']} {row['text']}" for row in rows)
    else:
        output = "\n".join(f"{row['timestamp']}\t{row['text']}" for row in rows)

    if args.output:
        Path(args.output).write_text(output + "\n", encoding="utf-8")
    else:
        print(output)

    print(f"Fetched {len(rows)} caption rows for {vid}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
