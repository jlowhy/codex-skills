---
name: spec-review
description: Review the current code changes against the intended spec, reconstruct the expected behavior and scope first, then return prioritized, actionable findings about spec drift, missing coverage, feature creep, or overengineering.
---

Review the current code changes against the comparison base, but first reconstruct the intended spec and implementation scope.

## Reconstruct The Spec

Use evidence in this order:

- ongoing chat context
- user-linked files, docs, issues, follow-up notes, PR text, screenshots, or benchmark artifacts
- the current diff, changed tests, and surrounding code

Before findings, briefly state:

- intended behavior
- in-scope implementation boundaries
- out-of-scope boundaries
- evidence used, especially when the spec is inferred
- any material uncertainty that would change the review outcome

## Review Focus

Prioritize findings where the implementation:

- misses or only partially satisfies the intended behavior
- drifts beyond the intended scope
- introduces feature creep, speculative flexibility, or unnecessary abstraction
- mixes unrelated improvements into a spec-bound change
- leaves required tests, fixtures, stories, types, docs, or contract updates behind

## Output

Findings first after the spec reconstruction, ordered by severity. For each finding include:

- `Severity`: blocker, high, medium, or low
- `Type`: spec miss, spec drift, feature creep, overengineering, or missing coverage
- `File`: precise file and line reference when possible
- `Issue`: what is wrong relative to the intended spec
- `Impact`: what behavior, reviewability, or ownership boundary is affected
- `Recommended fix`: the smallest fix and why it matches the spec
- `After fix`: the expected behavior after the fix

Defend the intended behavior and scope. Avoid general code-quality commentary unless it changes correctness, scope, or maintainability in a concrete way.
