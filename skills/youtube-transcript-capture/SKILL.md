---
name: youtube-transcript-capture
description: Capture YouTube metadata and transcript-derived notes into the user's notes vault. Use when the user asks to save, capture, clip, transcribe, or take detailed notes from a YouTube video into Obsidian, Clippings, or the notes vault.
---

# YouTube Transcript Capture

Use this to turn a YouTube URL into a durable note, usually in the notes vault. For non-YouTube video or audio sources, do not assume this skill applies unless captions can be fetched through `yt-dlp` or the user provides a transcript.

## Workflow

1. If the user says "notes vault", work in `~/Notes` and follow its local `AGENTS.md`.
2. Create or update a note under `Clippings/` unless the vault context clearly points elsewhere.
3. Capture metadata first: title, source URL, channel/author, video id, duration, thumbnail, requested timestamp, created date, and transcript source.
4. Fetch captions/transcript when available. For YouTube, prefer `scripts/fetch_youtube_transcript.py`.
5. Do not store a full verbatim transcript unless the user provided it directly or the source is clearly licensed for that use.
6. If full transcript storage is not appropriate, write detailed timestamped transcript-derived notes. These should be granular notes, not a short summary.
7. Mark transcript provenance and risk, for example: `YouTube auto-generated captions fetched on YYYY-MM-DD; captions may contain recognition errors.`
8. Add or update the daily note backlink when working in the notes vault.
9. Verify by reading the saved note and checking that timestamps, source link, and provenance are present.

## Caption Fetch

From this skill directory, run:

```bash
uv run --with youtube-transcript-api python scripts/fetch_youtube_transcript.py "https://www.youtube.com/watch?v=VIDEO_ID" --format tsv --output /tmp/video.transcript.tsv
```

If `yt-dlp` is available and the API helper fails, try it as a YouTube fallback:

```bash
yt-dlp --write-auto-subs --skip-download --sub-lang en --sub-format vtt "VIDEO_URL"
```

If both fail, inspect the page metadata for caption tracks and record that captions could not be fetched. For non-YouTube sources, only continue if the transcript is user-provided, directly exposed by the source, or fetchable through a reliable tool already available in the environment.

## Note Shape

Use this structure unless the vault has a stronger local pattern:

```md
---
categories:
  - "[[Clippings]]"
tags:
  - clippings
  - video
author: []
url: "VIDEO_URL"
created: YYYY-MM-DD
topics: []
source: YouTube
video_id: VIDEO_ID
duration: ""
requested_timestamp: ""
thumbnail: ""
transcript_source: ""
---

# Title

Source: VIDEO_URL

Requested timestamp: [H:MM:SS](VIDEO_URL&t=SECONDS)

## Context

Brief setup of the video and why it was captured.

## Chapters

- 0:00 ...

## Transcript

Full verbatim transcript not stored here. These are detailed, timestamped notes taken from SOURCE on YYYY-MM-DD. Captions may contain recognition errors.

## Detailed Notes

### 0:00 - Section

- Detailed transcript-derived note.
```

## Detailed Notes Standard

- Preserve the video's sequence.
- Use timestamped headings based on chapters or natural topic shifts.
- Capture concrete claims, examples, mechanisms, named people, numbers, and memorable distinctions.
- Prefer paraphrase over quotation. Use only short quotes when the exact wording matters.
- Avoid vague bullets like "they discuss leadership"; state the actual point made.
- Keep sponsor reads out unless the user asks to capture them.
