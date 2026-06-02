---
name: implement-with-alignment
description: Normalize an implementation brief, get explicit alignment, then execute, verify, and prepare the completed change for publication. Use when a proposed change needs approval before code edits, regardless of whether it came from an audit, review, spec, diagnosis, or user request.
---

# Implement With Alignment

Use this as the generic bridge from proposed change to completed implementation. Treat any upstream input as an `implementation brief`: the normalized plan for what to change, why it matters, how to verify it, and what to defer.

## Hard Gate

Do not edit files, commit, push, or start PR publication until the user explicitly approves a concrete implementation plan.

If the user says "just implement", still normalize the brief, state the recommended path, and ask for approval. Even small fixes require alignment when this skill is active. Non-mutating investigation and verification commands are allowed before approval.

If scope changes materially after approval, stop and get approval for the new scope before continuing.

## Normalize The Brief

Inspect the relevant local code and commands before proposing implementation.

If the brief references a ticket, PR, issue, review thread, spec, design doc, commit, branch, or URL, inspect every accessible referenced artifact before proposing a plan. Include source details that could affect scope: acceptance criteria, comments, diffs, unresolved threads, checks, linked issues, and status. If something is inaccessible, say what could not be read and whether that blocks confident alignment.

Assess whether the human instructions are complete enough to execute. Humans often omit key constraints, acceptance criteria, edge cases, rollout details, or verification expectations. Fill obvious gaps from source context; raise missing facts that could change scope, correctness, or risk.

Present the brief in this shape:

- **Source context reviewed**: local code, commands, tickets, PRs, docs, comments, or other artifacts inspected
- **Preferred option**: the smallest coherent batch worth doing now
- **Why this**: leverage, confidence, effort, time-to-feedback, and maintenance cost
- **Alternatives**: what was considered and why it is not preferred
- **Expected changes**: likely files, commands, workflows, or docs
- **Verification**: exact checks to run and any known limits
- **Do not build yet**: tempting scope to defer
- **Open questions**: risks or unknowns that block confident execution

If important facts are missing, ask one question at a time. Make a recommendation with each major question; do not act as a neutral questionnaire.

Ask for explicit approval before editing.

## Implementation

After approval, check `git status`. Preserve unrelated user changes. If approved edits overlap dirty files, inspect them and work with them; ask only if the overlap makes the plan unsafe.

Implement the approved brief only. Prefer existing repo patterns, helpers, scripts, tests, and docs locations. Avoid unrelated cleanup unless it is necessary for the approved outcome.

If verification exposes issues within the approved plan, fix and rerun. If it exposes new scope, stop for alignment.

## Verification And Handoff

Run the agreed checks. Record skipped checks with concrete reasons.

After the implementation verifies, run `codex-review` against the completed work. Address accepted findings and rerun relevant validation. When review findings are settled, run `post-implementation-cleanup-loop` for behavior-preserving cleanup before publication.

If the repo uses git, commit the approved implementation when requested or when the agreed workflow includes publication. If the user wants a PR, hand off to the repo's PR-authoring workflow or skill instead of prescribing PR format here.

## Closeout

Report what changed, what validation proved, what remains weak or deferred, and the commit hash when created. If PR publication is next, state that the implementation is ready for the PR-authoring skill.
