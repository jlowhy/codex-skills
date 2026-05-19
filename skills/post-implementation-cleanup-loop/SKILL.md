---
name: post-implementation-cleanup-loop
description: Run branch-wide post-implementation cleanup through repeated subagent review and fix rounds until no accepted cleanup findings remain. Use when a working implementation needs behavior-preserving cleanup, refactoring, de-duplication, or dead-code removal across the full branch/worktree.
---

# Post-Implementation Cleanup Loop

## Goal

Improve the shape of a working implementation without changing intended behavior.

- Treat the target as the full branch plus working tree relative to the comparison base, not just the last commit.
- If unrelated work exists, narrow to the files and commits matching the request and say what was excluded.
- Continue until a complete subagent review round returns no accepted/actionable cleanup findings.
- Stop when remaining ideas are consciously rejected as low-value, speculative, behavior-risky, or out of scope.

## Before Patching

State the stable behavior, comparison base, branch/worktree scope, cleanup boundary, structural improvement, any non-touched code included, and smallest validation needed.

Include non-touched code only when the implementation made it unused, redundant, misleading, or ownership-confused. Prefer connected callers, callees, obsolete helpers, and compatibility leftovers before expanding by pattern. If shared ownership or a local contract changes, include directly coupled tests, stories, fixtures, harnesses, docs, query/config wiring, and dependent wrappers or mocks.

## Cleanup Order

1. delete dead code, stale branches, unused helpers, and compatibility leftovers
2. collapse duplicated paths into one clear owner
3. remove wrappers, mirror types, forwarding layers, and repeated wiring that do not enforce a real invariant, create a stable boundary, or perform precise normalization
4. simplify control flow, data flow, and state transitions
5. extract helpers or subviews only when they make ownership clearer
6. align with current repo conventions only if scope stays tight

Prefer deletion over wrapper churn. Prefer upstream-derived types, scalar parameters, and upstream outputs/errors unless the local layer adds real policy or a stricter contract. If a boundary already owns ordering, shaping, or state derivation, delete downstream re-derivation.

## Round Structure

Each cleanup round is:

1. determine the comparison base and current branch/worktree scope
2. reconstruct the behavior that must remain stable
3. run one or more subagent cleanup reviews
4. verify every subagent finding in the real code path
5. apply only accepted fixes
6. rerun focused validation for changed behavior or ownership boundaries
7. rerun another cleanup round if code changed or accepted findings remain

## Subagents

Use subagents only for review. Keep the main agent responsible for final judgment, integration, and all file edits.

Ask subagents to return only accepted/actionable cleanup findings, rejected findings with one-line reasons, touched files/behavior paths, and focused validation to rerun.

Split independent review areas by ownership. Avoid duplicate reviews unless a second pass is checking whether the previous round is clean.

## Acceptance Rules

Accept a cleanup finding only when it is grounded in the current diff or directly connected code and preserves behavior.

Reject findings that are speculative, stylistic, repo-wide opportunistic cleanup, broad rewrites without a concrete bug class or ownership improvement, behavior-changing unless requested, or unsafe because the relevant contract/boundary is unclear.

Before deleting or inlining a wrapper, helper, API, or compatibility path, verify whether it owns an invariant, policy, normalization step, architectural boundary, or future extension point. If it crosses a named boundary such as service, handler, controller, repository, adapter, or client, state why that layer no longer owns a real contract.

## Guardrails

- keep public behavior, services, and APIs stable
- do not widen into unrelated files just because the same pattern exists elsewhere
- do not treat repo-wide opportunistic tidying as part of cleanup unless the user asked for that broader sweep
- do not mix cleanup with migrations, dependency upgrades, or broad renames
- do not keep cosmetic abstractions or helper extractions that only move complexity around
- do not replace upstream types, outputs, or errors with local mirrors unless the local contract is meaningfully stricter or clearer
- do not collapse a named architectural layer without stating why that layer no longer owns a real boundary, policy, or future extension point

## Test Support Ownership

If cleanup touches setup, assertions, fixtures, harness options, or inspection queries, first decide whether the code is test support or product logic. Do not move test-only behavior into production-like helpers, service modules, or generic domain modules. If shared test support is justified, place it under an explicit test-support/test-helpers path or give it a test-boundary name.

## Validation And Stop

After accepted fixes, run the smallest validation that proves behavior stayed stable. If validation fails, fix the failure or revert the cleanup that caused it, then rerun validation and another subagent review round.

Stop only when:

- a complete subagent review round reports no accepted/actionable cleanup findings, and
- focused validation for the final changes passes or the remaining validation gap is explicitly reported.

## Report

Include comparison base and scope reviewed, subagent rounds run, cleanup findings accepted/fixed, findings rejected and why, validation run, and the final clean-round result or reason remaining items were left alone.
