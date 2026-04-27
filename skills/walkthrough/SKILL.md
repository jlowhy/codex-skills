---
name: walkthrough
description: Walk through the current code changes in review order, explain the concrete behavior and codepath changes, how the implementation works, and critically call out questionable decisions, tradeoffs, risks, or unnecessary complexity in the diff.
---
Walk through the current code changes against the comparison base as if guiding someone through a code review.

Use relevant ongoing chat context first. If the user pointed to a file, doc, issue, PR text, or benchmark artifact, use that to frame the walkthrough. Otherwise infer likely intent from the current diff, touched tests, and surrounding code, and say what in the diff supports that inference.

Explain the implementation in terms of correctness, behavior, ownership boundaries, and technical necessity. Critique inline when the diff shows questionable decisions, unnecessary complexity, weak abstractions, scope drift, under-validation, or risky behavior.

## Start With

- intended behavior
- evidence for that intent
- core implementation areas versus support updates
- any unrelated or hard-to-justify noise

## Walkthrough

Group by behavior or codepath, not by a mechanical file list. For each meaningful area, cover:

- before and after behavior
- how the new code works
- contract, dependency, or ownership boundary being changed
- support updates such as tests, fixtures, stories, types, docs, or wiring
- risks, tradeoffs, assumptions, or disproportionate complexity

Connect layers when it helps explain the end-to-end flow, such as route, component, hook, service, handler, repository, schema, or runtime wiring.

Keep the format as a walkthrough, not terse findings-first review. Use direct technical statements grounded in code references. Do not include praise.
