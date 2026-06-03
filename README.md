# Codex Skills

Personal Codex skills for writing and transcript workflows.

This repository is the source of truth. The runtime install location is:

```bash
${CODEX_HOME:-$HOME/.codex}/skills
```

## Skills

- `improve-harness-engineering`: audit and prioritize codebase harness improvements for coding-agent workflows.
- `implement-with-alignment`: normalize an implementation brief, align it, then execute, verify, and prepare the completed change for publication.
- `file-issues`: create handoff-ready issues in an issue tracker from issue material, context, and references.
- `youtube-transcript-capture`: capture YouTube metadata and transcript-derived notes into the notes vault.
- `writing-grill`: grill a piece of writing until its essence, narrative structure, tension, and payoff are clear.
- `writing-sharpen`: clean up existing writing by cutting AI-ish scaffolding, filler, and vague synthesis.

## Install

Install selected skills as symlinks:

```bash
./install.sh improve-harness-engineering
./install.sh implement-with-alignment
./install.sh file-issues
./install.sh youtube-transcript-capture
./install.sh writing-grill
./install.sh writing-sharpen
```

By default, existing installed skill folders are replaced with symlinks to this repository. A timestamped backup is created under:

```bash
${CODEX_HOME:-$HOME/.codex}/skills/.backup/
```

## Layout

```text
skills/<skill-name>/SKILL.md
install.sh
```

Each folder under `skills/` is an installable Codex skill.

## Attributions

- `improve-harness-engineering` vocabulary adapted from Birgitta Bockeler's ["Harness engineering for coding agent users"](https://martinfowler.com/articles/harness-engineering.html).
