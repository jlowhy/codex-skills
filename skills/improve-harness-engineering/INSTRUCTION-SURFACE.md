# Instruction Surface

Treat the repo as an instruction system:

- `AGENTS.md`: always-on control plane for cross-cutting rules and routing
- skills: progressive-discovery modules for conditional workflows
- references, templates, and scripts: bulky support material and deterministic procedures
- docs: durable human/agent readable explanations
- nested instruction files: path-specific local deltas

Search repo-wide for root and nested `AGENTS.md`, `SKILL.md`, provider-specific files, repo-local skills, workflow packs, and subsystem READMEs that define local operating rules.

Classify instruction content as always-on rule, conditional workflow, reference material, deterministic procedure, or provider-specific guidance before recommending where it belongs.

Evaluate routing quality, clarity, duplication, progressive disclosure, provider coupling, skill-contract quality, and unnecessary always-on token cost.

Target structure:

- keep `AGENTS.md` minimal, cross-cutting, and routing-focused
- move conditional workflows to skills
- move bulky support material to references, templates, or docs
- move deterministic procedures to scripts, hooks, CI, or feedback sensors
- keep nested instruction files for path-specific deltas
- isolate provider-specific packaging from repository-general guidance

When recommending an instruction refactor, state what stays in `AGENTS.md`, what moves out, destination artifact, content classification, estimated always-on token impact when relevant, and acceptance criteria.

Use `AGENTS.md` for short, always-loaded rules that apply broadly and prevent real mistakes: exact commands, non-obvious repo workflows, path ownership, project-specific conventions, and links to durable docs.

Prefer another artifact when it fits better:

- detailed human/agent explanation -> docs, linked from `AGENTS.md`
- repeatable workflow -> skill
- deterministic action -> script, hook, CI, or feedback sensor
- path-specific rule -> nested `AGENTS.md`
- volatile status or one-off decision -> issue, PR, ADR, or task brief

Flag weak `AGENTS.md` when it is long, generic, duplicated, stale, tutorial-like, self-evident, or contains instructions that should be executable checks.

Use a soft cap: target under 80 lines for root `AGENTS.md`; require justification above 120 lines. Treat Codex's 32 KiB load limit as a hard ceiling, not a quality target.
