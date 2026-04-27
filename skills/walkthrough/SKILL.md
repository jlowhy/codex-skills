---
name: walkthrough
description: Walk through the current code changes in review order, explain the concrete behavior and codepath changes, how the implementation works, and critically call out questionable decisions, tradeoffs, risks, or unnecessary complexity in the diff.
---
Walk through the current code changes against the comparison base as if guiding someone through a code review.

Use relevant ongoing chat context first. If the user pointed to a file, doc, issue, PR text, or benchmark artifact, use that to frame the walkthrough. Otherwise infer likely intent from the current diff, touched tests, and surrounding code, and say what in the diff supports that inference.

The goal is to explain the implementation in terms of correctness, behavior, boundaries, and technical necessity, while also pointing out questionable decisions, unnecessary complexity, weak abstractions, scope drift, or risky behavior when they appear.

Before the walkthrough, state briefly:
- what concrete behavior the change is trying to produce
- what evidence supports that conclusion
- what parts of the diff are core to the change versus supporting updates

Then walk through the code in a coherent review order. Prefer grouping by behavior or codepath rather than by raw file listing when that makes the explanation clearer.

State conclusions as direct observations tied to code paths and behavior.

Anchor each explanation in:
- the code path being changed
- the behavior before and after the change
- the dependency or contract this change relies on
- whether the implementation is necessary, sufficient, and proportionate to the behavior it is trying to support

For each meaningful change area, explain:
- what changed
- what concrete behavior change it is trying to produce
- how the new code works
- what prior behavior or structure it replaces
- what boundary or contract is being modified
- what supporting updates were required, such as tests, fixtures, stories, types, or wiring
- any important tradeoffs, assumptions, or risks visible in the implementation
- whether any decision looks questionable, overengineered, under-validated, or out of proportion to the problem being solved

When useful, connect the flow across layers such as route, component, hook, service, handler, repository, or schema so the user can see the end-to-end path instead of isolated diffs.

If the diff includes unrelated noise, call that out and separate:
- core implementation changes
- supporting or contract-completion changes
- unrelated or hard-to-justify changes

Do not default to terse findings-first review. Keep the walkthrough format, but critique inline whenever the implementation appears questionable. Be explicit about:
- awkward or unjustified abstractions
- feature creep or scope drift
- code that is harder than necessary for the stated behavior
- missing support updates such as tests, fixtures, or contract-completion changes
- risky assumptions or places where the implementation is not convincingly defended by the apparent requirements

Output style:
- start with a short overview
- then give the walkthrough in a sensible order
- use concrete file references
- keep the emphasis on behavior, mechanics, correctness, and critical evaluation
- use direct technical statements that are grounded in the code
