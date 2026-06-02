---
name: harness-engineering
description: Diagnose, prioritize, align, implement, verify, and publish codebase harness improvements for coding-agent workflows. Use when the user wants to audit a repo's agent harness, improve guides or sensors, reduce repeated agent failures, strengthen validation workflows, or apply harness engineering based on Martin Fowler's article.
---

# Harness Engineering

Use this as an execution skill with a mandatory alignment gate. Source framing: Birgitta Bockeler, "Harness engineering for coding agent users" on Martin Fowler's site: https://martinfowler.com/articles/harness-engineering.html

A codebase harness is the outer system of guides, sensors, workflows, and codebase properties that helps coding agents get work right, self-correct quickly, and leave the right decisions to humans.

## Hard Gate

Do not edit files, commit, push, or open a PR during audit or grilling. Read files and run non-mutating commands only.

Before implementation, get explicit user approval of a concrete plan. If the user says "just implement", still audit first, recommend a plan, and ask for approval. Even small fixes require alignment when this skill is active.

If scope changes materially after approval, run a new alignment checkpoint before expanding the implementation.

## Audit Flow

First identify repo topology: app/service/library/monorepo shape; language, runtime, framework, package manager, test framework, CI, release/deploy model, and current agent workflow.

Discover exact commands from real repo evidence: package files, Makefiles, task runners, CI, docs, and existing agent instructions. Do not assume default commands.

Run the fastest representative checks where feasible. Inspect failures. Distinguish "harness exists on paper" from "harness works in this checkout". If a check is slow, flaky, expensive, credential-gated, or destructive, skip it and record why.

## Harness Map

Evaluate all harness types:

- **Feedforward guides**: `AGENTS.md`, skills, docs, rules, examples, templates, generated-code guidance, bootstrap instructions, LSP/code-intelligence affordances, codemods.
- **Feedback sensors**: tests, type checks, linters, architecture checks, scripts, browser/runtime inspection, logs, CI, mutation testing, coverage quality, dependency and drift checks, AI review.
- **Human workflow**: alignment gates, PR standards, review instructions, ownership, escalation points, manual verification, and where human judgment is still required.
- **Harnessability / architecture**: module boundaries, type strength, framework affordances, fixture quality, debuggability, local dev reliability, readable failures, runtime observability, and stable test data.

Tag serious findings with regulation category:

- **Maintainability harness**: internal quality, duplication, complexity, style, type safety, coverage, dead code, dependency hygiene.
- **Architecture fitness harness**: boundaries, layering, performance, security, observability, API shape, cross-module contracts.
- **Behavior harness**: whether the application functionally behaves as intended.

Also map controls as `feedforward` or `feedback`, and `computational` or `inferential`. Prefer cheap, reliable computational controls; use inferential controls for semantic judgment, prioritization, and gaps deterministic tools cannot cover.

## Behavior Harness Standard

Do not treat AI-generated tests alone as a strong behavior oracle. Look for independent behavioral confidence: approved fixtures, golden files, contract tests, e2e smoke paths, manual verification scripts, seeded test data, production/runtime signals, or user-approved examples.

Explicitly flag when behavior confidence depends mostly on agent-written tests or human manual review.

## Scoring

For each serious improvement, score or qualitatively assess: leverage, confidence, implementation effort, time-to-feedback, and ongoing maintenance cost.

Group recommendations by harness type. Within each group, identify the preferred recommendation and explain why it is preferred over alternatives using the rubric.

Include a **do not build yet** lane for attractive but premature controls: generic prose instead of executable checks, AI review replacing deterministic tests, custom tooling before basic commands work, CI-only feedback agents cannot run locally, and controls with unclear ownership or maintenance path.

## Grilling And Alignment

When alignment is unclear, interview relentlessly one question at a time. Make a recommendation with each major question; do not act as a neutral questionnaire.

Challenge anti-patterns:

- vague `AGENTS.md` rules where a script or check would work
- contradictory guides and sensors
- docs pointing to commands that do not exist or fail
- repeated agent failures with no guide or sensor
- behavior claims backed only by newly generated tests
- broad AI review before deterministic feedback is reliable
- heavyweight static analysis before basic local validation works

Alignment checkpoint format: preferred option, why this moves the needle, alternatives considered, files and commands likely to change, verification plan, and do-not-build-yet items.

Ask for explicit approval before implementation.

## Implementation

After approval, check `git status` before editing. Preserve unrelated user changes. If approved edits overlap dirty files, inspect them and work with them; ask only if the overlap makes the plan unsafe.

Implement the smallest coherent batch that materially improves self-correction and trust. Valid implementations include scripts, tests, CI checks, architecture rules, lint/type checks, fixtures, docs, agent instructions, review skills, PR templates, MCP/tool setup, or validation workflows. Aspirational docs alone are not enough unless they encode a durable repo-specific decision or workflow.

Verify with the agreed commands. If verification exposes issues within the approved scope, fix and rerun. If it points to new scope, stop for alignment.

When GitHub and `gh` are available, commit, push, and open or update a PR. Write the PR body with harness audit findings, implemented changes, and validation.

## Output Shape

For audits, report: repo topology, current harness map, findings by harness type, preferred recommendations, do not build yet, and alignment questions.

For closeout, report the harness delta: which guide, sensor, workflow, or harnessability property improved; which regulation category it protects; what validation proved; what remains weak; and the PR URL if opened.
