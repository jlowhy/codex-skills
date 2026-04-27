---
name: simple-review
description: Review the current code changes against the comparison base and return prioritized, actionable findings.
---

Review the current code changes against the comparison base and return prioritized, actionable findings.

## Scope

Find the comparison base directly. Prefer `origin/main`, then `main`, then `origin/master`, then `master`; use the merge base with `HEAD` when available. Review the diff, changed files, diff stat, and commits since that base.

Only report material issues: correctness bugs, behavioral regressions, contract breaks, missing required coverage, risky edge cases, or changes that are likely to fail in real use. If there are no material findings, say so clearly and mention any residual validation gap.

## Output

Findings first, ordered by severity. For each finding include:

- `Severity`: blocker, high, medium, or low
- `File`: precise file and line reference when possible
- `Issue`: what is wrong
- `Impact`: what breaks or becomes risky
- `Recommended fix`: the smallest fix and why it is the right one
- `After fix`: the expected behavior after the fix

Keep the review concise and evidence-based. Do not include praise, broad summaries, or style-only comments unless they affect correctness or maintainability in a concrete way.
