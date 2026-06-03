# Codex Skills

Personal Codex skills for writing and transcript workflows.

This repository is the source of truth. The runtime install location is:

```bash
${CODEX_HOME:-$HOME/.codex}/skills
```

## Skills

- `implement-with-alignment`: normalize an implementation brief, align it, then execute, verify, and prepare the completed change for publication.
- `youtube-transcript-capture`: capture YouTube metadata and transcript-derived notes into the notes vault.
- `writing-grill`: critique, develop, and sharpen writing from nothing, notes, or drafts into a clear, forceful piece.

## Install

Install selected skills as symlinks:

```bash
./install.sh implement-with-alignment
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
install.sh
```

Each folder under `skills/` is an installable Codex skill. Some skills include one-level reference files loaded from `SKILL.md`.
