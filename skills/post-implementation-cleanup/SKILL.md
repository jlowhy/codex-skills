---
name: post-implementation-cleanup
description: Clean up an implementation that already works. Use when the user asks to refactor, simplify, de-duplicate, remove dead code, or align a finished change with repo conventions without changing behavior.
---
Get context of the current code changes against the comparison base. Improve the shape of an implemented change without changing its intended behavior.

Treat the cleanup target as the full branch plus working tree relative to mainline. Do not assume the last commit is the whole implementation.

Include non-touched code when the implementation clearly made it unused, redundant, misleading, or ownership-confused. Prefer expanding to directly connected callers, callees, obsolete helpers, and compatibility leftovers before expanding by pattern alone.

When shared ownership or a local contract changes, include directly coupled support surfaces such as tests, stories, fixtures, harnesses, docs, and query or configuration wiring that still encode the old shape.

When removing a function, helper, API, or compatibility path, treat contract-completion cleanup as in scope. Follow reachable call sites and any wrappers, tests, mocks, docs, stories, types, or configuration that still depend on that symbol or existed only to support it.

If the branch includes unrelated work, narrow the scope to the files and commits that match the user request and say what was excluded.

## Before Patching

State the current behavior that must stay stable, the boundary being cleaned up, why any non-touched code is in scope, the structural improvement being attempted, and the smallest validation that should prove behavior stayed stable.

Before deleting or inlining a wrapper, confirm whether it owns a real invariant, policy, normalization step, architectural boundary, or future extension point.

## Cleanup Order

1. delete dead code, stale branches, unused helpers, and compatibility leftovers
2. collapse duplicated paths into one clear owner
3. remove wrappers, mirror types, forwarding layers, and repeated wiring that do not enforce a real invariant, create a stable boundary, or perform precise normalization
4. simplify control flow, data flow, and state transitions
5. extract helpers or subviews only when they make ownership clearer
6. align with current repo conventions only if scope stays tight

Stop once the remaining cleanup ideas are low-value, speculative, or uncertain to preserve behavior. It is valid to conclude that no further cleanup work is warranted.

Prefer deletion over wrapper churn.

For abstraction cleanup, prefer upstream-derived types over mirror types, scalar parameters over single-field input objects, and upstream outputs or errors unless the local layer is adding real policy or a more precise contract.

When a boundary already owns ordering, shaping, or state derivation, prefer deleting downstream re-derivation instead of preserving duplicate local logic.

Do not remove or inline a function only because it looks like a thin wrapper. If it crosses a named architectural boundary such as service, handler, controller, repository, adapter, or client, first verify whether that seam is intentional and what contract or ownership it preserves.

## Guardrails

- keep public behavior, services and APIs stable
- do not widen into unrelated files just because the same pattern exists elsewhere
- do not treat repo-wide opportunistic tidying as part of cleanup unless the user asked for that broader sweep
- do not mix cleanup with migrations, dependency upgrades, or broad renames
- do not keep cosmetic abstractions or helper extractions that only move complexity around
- do not replace upstream types, outputs, or errors with local mirrors unless the local contract is meaningfully stricter or clearer
- do not collapse a named architectural layer without stating why that layer no longer owns a real boundary, policy, or future extension point

## Report

- cleanup passes that landed
- behavior-preservation assumptions
- why any non-touched code was included
- what was intentionally left alone to avoid scope drift
- validation actually run
