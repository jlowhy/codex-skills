---
name: improve-harness-engineering
description: Diagnose and prioritize codebase harness improvements for coding-agent workflows. Use when the user wants to audit a repo's agent harness, improve feedforward guides or feedback sensors, reduce repeated agent failures, strengthen validation workflows, or apply harness engineering concepts.
---

# Harness Engineering

Use this as a diagnosis and recommendation skill.

A codebase harness is the outer system of feedforward guides, feedback sensors, workflows, and codebase properties that helps coding agents get work right, self-correct quickly, and leave the right decisions to humans.

Apply [EVIDENCE-STANDARD.md](EVIDENCE-STANDARD.md) and [DELEGATED-AUDIT.md](DELEGATED-AUDIT.md) to every audit.

## Definitions

- **Feedforward guide**: a control that steers the agent before it acts, such as repo instructions, skills, docs, examples, templates, rules, codemods, or bootstrap scripts.
- **Feedback sensor**: a control that observes output after the agent acts and helps it self-correct, such as tests, type checks, linters, logs, browser checks, CI, or review agents.
- **Computational control**: a deterministic control run by software, usually cheap and repeatable, such as a script, linter, type checker, architecture test, or generated-code validator.
- **Inferential control**: a judgment-based control, usually model-assisted or human-assisted, such as semantic review, tradeoff analysis, architectural critique, or product judgment.
- **Harnessability**: how easy the codebase is for an agent to understand, navigate, modify, and verify because of its structure, typing, boundaries, tooling, fixtures, and runtime observability.
- **Regulation category**: the quality dimension the harness protects: maintainability, architecture fitness, or behavior.

## Boundary

Do not edit files, commit, push, or open a PR. Read files and run non-mutating commands only. If the user wants to implement an audit recommendation, hand off to `implement-with-alignment` using the chosen prioritized recommendation.

## Audit Flow

Audit ambitiously. Look for meaningful harness leverage, not only obvious missing docs or broken commands.

First identify repo topology: app/service/library/monorepo shape; language, runtime, framework, package manager, test framework, CI, release/deploy model, and current agent workflow.

Discover exact commands from real repo evidence: package files, Makefiles, task runners, CI, docs, and existing agent instructions. Do not assume default commands.

Run the fastest representative checks where feasible. Inspect failures. Distinguish "harness exists on paper" from "harness works in this checkout". If a check is slow, flaky, expensive, credential-gated, or destructive, skip it and record why.

Read agent instruction surfaces such as `AGENTS.md`, runtime skills, repo docs, and human-facing architecture docs. Evaluate whether each instruction belongs where it is: global agent rule, path-specific agent rule, reusable skill, human/agent readable doc, executable script, or feedback sensor. Apply [INSTRUCTION-SURFACE.md](INSTRUCTION-SURFACE.md).

## Harness Map

Evaluate four audit dimensions:

- **Feedforward guides**: what steers the agent before it acts, and is each instruction in the right artifact?
- **Feedback sensors**: what lets the agent self-correct after it acts?
- **Human workflow**: where do people steer, approve, review, or own judgment?
- **Harnessability**: what codebase or environment properties make agent work easier or harder?

For each serious finding, tag the audit dimension, control type (`computational` or `inferential`), and regulation category:

- **Maintainability harness**: internal quality, duplication, complexity, style, type safety, coverage, dead code, dependency hygiene.
- **Architecture fitness harness**: boundaries, layering, performance, security, observability, API shape, cross-module contracts.
- **Behavior harness**: whether the application functionally behaves as intended.

Prefer cheap, reliable computational controls. Use inferential controls for semantic judgment, prioritization, and gaps deterministic tools cannot cover.

## Delegated Audit

Delegated audit is the core workflow. Apply [DELEGATED-AUDIT.md](DELEGATED-AUDIT.md), including the mandatory full instruction-surface audit for feedforward guides. Do not produce prioritized recommendations until every audit dimension has current state, coverage, issues found, candidate improvements, a preferred recommendation, and do-not-build-yet items.

## Additional Checks

- **Behavior**: flag weak confidence when tests mirror implementation, over-mock boundaries, rely on manual review, or lack an independent expected result.
- **Navigation and architecture**: flag friction when agents cannot quickly find concepts, ownership, entrypoints, intended layers, caller-facing test interfaces, or inspectable runtime state.
- **Operating model**: evaluate bootstrap/startup reachability, root command surface, workspace boundaries, graph-aware task execution, CI/local alignment, and validation reachability. Flag false confidence from docs drift, warmed local state, ignored files, partial task success, or package-local commands that bypass the repo-owned path.

## Prioritization Rubric

Prioritize improvements by expected harness leverage. Prefer recommendations that catch repeated agent failures, have concrete repo evidence, run early and cheaply, carry low false-positive risk, and are simpler to maintain than alternatives.

Group recommendations by audit dimension. Within each group, identify the preferred recommendation and explain why it beats alternatives on leverage, confidence, effort, time-to-feedback, and maintenance cost.

Use **do not build yet** for attractive but premature controls, especially when they are lower leverage, higher maintenance, harder to verify, or less connected to observed failures than the preferred option.

Write in a technical, precise, easy-to-understand style. Lead each prioritized recommendation with the concrete workflow failure or improvement, then add harness classification. Do not make the reader infer the causal chain from separate bullets.

## Grilling

When alignment is unclear, interview relentlessly one question at a time. Make a recommendation with each major question; do not act as a neutral questionnaire.

Challenge anti-patterns:

- vague `AGENTS.md` rules where a script or check would work
- durable instructions trapped in chat, PR comments, or the wrong doc
- contradictory feedforward guides and feedback sensors
- command docs that do not match runnable checks
- repeated agent failures with no feedforward guide or feedback sensor
- behavior claims backed only by newly generated tests
- inferential review used before a reliable computational feedback sensor exists
- custom tooling before basic local validation works

Each prioritized recommendation must be detailed enough to hand off directly to `implement-with-alignment`.

## Output Shape

Use [REPORT-FORMAT.md](REPORT-FORMAT.md). The report must show every harness-map dimension before ranking implementation-ready recommendations.
