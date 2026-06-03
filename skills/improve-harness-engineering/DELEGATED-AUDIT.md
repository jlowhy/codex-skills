# Delegated Audit

Delegated audit is mandatory. The main agent reconstructs repo topology first, then delegates one focused audit for each harness-map dimension: feedforward guides, feedback sensors, human workflow, and harnessability.

Each delegated audit must return:

- surfaces searched
- surfaces inspected
- surfaces not covered, with reason
- concrete findings with evidence
- confidence level: high, medium, or low
- evidence needed to raise confidence
- candidate improvements, preferred recommendation, and do-not-build-yet items

The main agent owns final judgment. It must validate important subagent findings against files, commands, docs, or runtime behavior before using them in the final report. Reject duplicated, speculative, unactionable, or weakly evidenced findings.

## Subagent Response Review

When each delegated audit returns, the main agent must review the response before using it.

Check:

- did it cover the required surfaces for that dimension?
- are uncovered surfaces listed with reasons?
- is confidence justified by coverage and evidence?
- are the findings detailed enough to explain how the current system works?
- does each important finding include a concrete example, actual behavior, expected behavior, and why it matters?
- are recommendations detailed enough to support prioritization and action?

If the response is insufficient, either delegate a follow-up audit with a narrower question, or mark the missing coverage as `[not covered]`, downgrade confidence, and reduce or remove implementation-ready claims.

## Feedforward Guides Requirement

The feedforward guides delegated audit must perform a full instruction-surface audit. A targeted pass over root `AGENTS.md` and obvious linked docs is not sufficient.

It must search for and account for:

- root and nested `AGENTS.md`
- repo-local skills and `SKILL.md`
- provider or runtime-specific instruction files
- workflow packs, contributor docs, and subsystem READMEs
- scripts, hooks, CI, or feedback sensors that could replace prose instructions
- linked docs that agents or humans are expected to follow

A recommendation to refactor `AGENTS.md` or other instruction surfaces is not valid unless it includes a relocation inventory: what stays, what moves, where it moves, what becomes executable, and what can be deleted.

If coverage is incomplete, the final report must say so and lower confidence for the affected recommendation.
