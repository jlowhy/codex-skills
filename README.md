# Codex Skills

Personal Codex skills for review, cleanup, and implementation workflows.

This repository is the source of truth. The runtime install location is:

```bash
${CODEX_HOME:-$HOME/.codex}/skills
```

## Skills

- `post-implementation-cleanup`: behavior-preserving cleanup after an implementation works.
- `simple-review`: prioritized review findings against the comparison base.
- `spec-review`: review implementation drift against an intended spec.
- `walkthrough`: explain and critique the current diff in review order.

## Install

Install selected skills as symlinks:

```bash
./install.sh post-implementation-cleanup
./install.sh simple-review spec-review walkthrough
```

Install a bundle:

```bash
./install.sh --bundle review
./install.sh --bundle cleanup
```

By default, existing installed skill folders are replaced with symlinks to this repository. A timestamped backup is created under:

```bash
${CODEX_HOME:-$HOME/.codex}/skills/.backup/
```

## Layout

```text
skills/<skill-name>/SKILL.md
bundles/<bundle-name>.txt
install.sh
```

Each folder under `skills/` is an installable Codex skill.
