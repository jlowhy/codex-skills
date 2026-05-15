---
name: github-pr-review
description: Review a GitHub pull request from live PR state, follow the real code path, and post precise inline review comments with gh api plus PR-level comments with gh pr comment.
---

## Start

Fetch the current PR state with `gh pr view` and inspect the diff with `gh pr diff` before reviewing.

Before judging the diff, read relevant repo-local instructions: `AGENTS.md`, issue or PR skills, test guidance, docs lists, maintainer runbooks, or contribution notes.

## Classify The Change

State the change type before findings: bug fix, feature, refactor, config/runtime, dependency, docs, test-only, or mixed.

Use this review shape:

```text
Ref: PR #456 / <url> against <base>, from <head>
Surface: <runtime/CLI/provider/channel/docs/etc>
Change type: <bug/feature/refactor/config/runtime/dependency/docs/test-only/mixed>

Intent: <what the PR is trying to change, based on PR text, issues, commits, tests, and diff>
Boundary: <where the change should live, and whether ownership/abstraction is right>
Implementation: <main code path touched and confidence>
Findings: <blocking findings first, or no blocking correctness issues found>
Proof: <tests/CI/local/live/source/docs/dependency contract checked>
Risk: <remaining uncertainty>
Judgment: <best available shape / symptom-level / over-broad / not proven>
```

For bug fixes, also answer:

- what behavior was broken
- whether the root cause is identified in code
- whether the fix addresses the cause or only the symptom
- whether a refactor would make the invariant clearer without widening risk

## Review Depth

Read past the first touched file. Follow the real call path when relevant:

- entrypoint -> validation/parsing -> routing/dispatch -> owner module -> shared helper -> persistence/network/runtime boundary
- config/schema/docs -> runtime usage -> doctor/migration/fix path
- provider/channel/plugin owner code -> generic core only when multiple owners need the behavior
- tests around the touched surface plus adjacent regression tests

When behavior depends on a dependency, read current upstream docs, source, types, or package contract before assuming.

Prefer source and executable proof over PR comments. Treat issue comments, old CI, and old release behavior as hints until rechecked.

Good PRs usually:

- live at the ownership boundary where the change belongs
- preserve public and backward-compatible behavior unless the PR intentionally retires it
- make the invariant, workflow, or contract clearer rather than hiding behavior in special cases
- add or update proof at the smallest meaningful seam: tests, stories, fixtures, docs, type coverage, migration checks, or runtime validation
- avoid broad special cases, hidden migrations, semantic sentinels, and provider or channel IDs in generic core
- update docs, changelog, setup guidance, or examples when user-visible behavior changes
- fail clearly in runtime paths and repair through doctor, migration, setup, or recovery paths when that is the established contract

For non-bug changes, judge the relevant quality bar:

- feature: workflow completeness, state model, compatibility, docs, and regression coverage
- refactor: behavior preservation, clearer ownership, reduced complexity, and unchanged contracts
- config/runtime: schema, defaults, runtime usage, docs, validation, and repair path
- dependency: current upstream contract, version compatibility, fallback behavior, and tests
- docs: accuracy against shipped behavior and no unsupported promises
- tests-only: asserts real behavior instead of codifying incidental implementation

Call out changes that only address the visible symptom, move complexity to the wrong layer, or make future behavior harder to reason about. Recommend a slightly larger refactor only when it makes the invariant clearer, reduces repeated bug classes, or improves ownership without widening risk. If the refactor adds risk without improving the change class, say so.

## Output

Lead with findings. Findings must include file, line or symbol, concrete failure mode, impact, and smallest recommended fix. Avoid vague `consider` comments.

If there are no blocking issues, say:

- no blocking correctness issues found
- strongest proof checked
- residual risk or test gaps
- whether the change is the best available shape

## Publishing Comments

Publish the review to the PR by default. Use chat-only output only when the user explicitly asks for a dry run, preview, or local-only review.

Use the right GitHub surface:

- Use `gh api` for inline review comments on exact changed diff lines.
- Use `gh pr comment` for the PR-level summary, proof checked, residual risk, broad design concerns, and non-line-specific questions.
- Post inline review comments first, then the PR-level summary.
- Always post one PR-level comment with the overall review result and judgment.

Inline comments must be specific and actionable:

- point to the smallest relevant changed line
- state the concrete failure mode
- explain why that line causes or exposes the issue
- recommend the smallest fix

Do not use `gh pr comment` for a code-specific finding when an exact diff line exists. Do not force an inline comment onto a nearby changed line when the issue is architectural, cross-file, or not present in the diff. If a comment cannot be anchored to a valid diff line, make it part of the PR-level comment and name the file or symbol.
