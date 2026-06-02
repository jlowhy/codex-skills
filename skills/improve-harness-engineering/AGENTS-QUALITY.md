# AGENTS.md Quality

Use `AGENTS.md` for short, always-loaded rules that apply broadly and prevent real mistakes: exact commands, non-obvious repo workflows, path ownership, project-specific conventions, and links to durable docs.

Prefer another artifact when it fits better:

- detailed human/agent explanation -> docs, linked from `AGENTS.md`
- repeatable workflow -> skill
- deterministic action -> script, hook, CI, or feedback sensor
- path-specific rule -> nested `AGENTS.md`
- volatile status or one-off decision -> issue, PR, ADR, or task brief

Flag weak `AGENTS.md` when it is long, generic, duplicated, stale, tutorial-like, self-evident, or contains instructions that should be executable checks.

Use a soft cap: target under 80 lines for root `AGENTS.md`; require justification above 120 lines. Treat Codex's 32 KiB load limit as a hard ceiling, not a quality target.
