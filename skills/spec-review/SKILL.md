---
name: spec-review
description: Review the current code changes against the intended spec, reconstruct the expected behavior and scope first, then return prioritized, actionable findings about spec drift, missing coverage, feature creep, or overengineering.
---
Review the current code changes against the comparison base, but first reconstruct the intended spec and implementation scope.

Spec reconstruction order:
- if there is relevant ongoing chat context, use that first
- if the user pointed to a file, doc, issue, follow-up note, PR text, or benchmark artifact, use that next
- otherwise infer the most likely intended behavior and scope from the current diff, touched tests, and surrounding code

Before giving findings, state:
- what the key specs and behaviors are
- what the technical implementation is supposed to cover
- what it is not supposed to cover
- what looks like feature creep, speculative work, or overengineering risk
- what evidence you used to infer the above when the spec was not explicitly provided

Then review against that reconstructed spec.

Prioritize findings where the implementation:
- does not actually satisfy the intended behavior
- partially satisfies the behavior but leaves important gaps
- drifts beyond the intended scope
- introduces architectural churn, abstraction churn, or complexity that the spec did not require
- mixes unrelated improvements into a spec-bound change
- adds future-facing flexibility without a demonstrated need in the current change

If the intended spec is materially uncertain, say so explicitly and separate:
- likely spec violations
- likely overengineering or feature-creep concerns
- questions or assumptions that would change the review outcome

In your findings, explain:
- what the problem is
- what effect the problem will have
- whether it is a spec miss, spec drift, feature creep, or overengineering
- what potential fixes exist, if more than one
- what the recommended fix is and why
- the key file references for the fix
- what the behavior will be after the fix

Prefer review comments that defend the intended behavior and scope over comments that only point out local code quality.
