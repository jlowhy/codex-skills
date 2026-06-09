# Codex Skills

Personal Codex skills for writing, research, transcript, and asset workflows.

This repository is the source of truth. The runtime install location is:

```bash
${CODEX_HOME:-$HOME/.codex}/skills
```

## Skills

- `generate-social-assets`: generate local social assets from notes, drafts, articles, transcripts, or briefs, starting with LinkedIn carousel PDFs.
- `research-reddit-communities`: research and compare Reddit communities through agent-led discovery, then recommend one first community for credible participation.
- `youtube-transcript-capture`: capture YouTube metadata and transcript-derived notes into the notes vault.
- `writing-grill`: critique, develop, and sharpen writing from nothing, notes, or drafts into a clear, forceful piece.

## Install

Install selected skills as symlinks:

```bash
./install.sh generate-social-assets
./install.sh research-reddit-communities
./install.sh youtube-transcript-capture
./install.sh writing-grill
```

By default, existing installed skill folders are replaced with symlinks to this repository. A timestamped backup is created under:

```bash
${CODEX_HOME:-$HOME/.codex}/skills/.backup/
```

## Layout

```text
skills/<skill-name>/SKILL.md
skills/<skill-name>/<reference>.md
skills/<skill-name>/scripts/<helper>.py
install.sh
```

Each folder under `skills/` is an installable Codex skill. Some skills include one-level reference files loaded from `SKILL.md`; scripts are deterministic helpers for bounded tasks such as fetching metadata, creating note shells, or validating inputs.

## Research Helpers

`research-reddit-communities` includes:

- `RESEARCH-TEMPLATE.md`: the qualitative report shape for comparing communities and selecting one first channel.
- `scripts/make_research_note.py`: creates a structured research artifact outside the skill directory.
- `scripts/inspect_with_praw.py`: optional read-only Reddit API helper for bounded subreddit metadata/rules/post sampling when official credentials are available.

The Reddit skill is manual-first. API helpers accelerate inspection when available, but they are not required and do not produce final suitability scores or rankings.

## Asset Helpers

`generate-social-assets` includes:

- `scripts/create-carousel-brief.py`: creates a starter `slides.json` for a LinkedIn carousel.
- `scripts/render-carousel.py`: renders `slides.json` to a local HTML preview, PNG slides, and `carousel.pdf` using Playwright and ReportLab.

The asset skill is local-first. It creates reviewable files for manual upload and does not automate publishing.

## Context

`CONTEXT.md` records the glossary decisions for this skills repo, including the distinction between agent-led community research, investigation aids, research artifacts, and action-style skill names.
