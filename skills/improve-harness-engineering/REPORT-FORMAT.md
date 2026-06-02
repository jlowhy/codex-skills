# Harness Engineering Report Format

The report must show the whole harness before ranking implementation-ready recommendations.

## Reply Style

Write in technical, precise, easy-to-understand language. Prefer concrete workflow names, commands, files, and observed behavior over harness taxonomy. Use harness taxonomy as trailing classification, not as the main explanation.

## 1. Repo Topology

Summarize the repo shape, runtime, package manager, test framework, CI model, release/deploy model, current agent workflow, and commands verified or skipped.

Also summarize the apparent operating model: root command surface, workspace/package boundaries, bootstrap/startup path, graph-aware task execution, and CI/local alignment. Mark blocked or uninspected areas as `[not covered]`.

## 2. Harness Map

Create one subsection for each audit dimension:

- **Feedforward guides**
- **Feedback sensors**
- **Human workflow**
- **Harnessability**

Each subsection must include:

- **Coverage**: surfaces searched, inspected, and not covered
- **Current state**: what exists and where
- **Issues found**: evidence-bound gaps, contradictions, or friction
- **Candidate improvements**: viable options, not only the favorite
- **Preferred recommendation**: the best option for this dimension and why
- **Confidence**: high, medium, or low, with reason if not high
- **Do not build yet**: tempting controls to defer and why

## 3. Prioritized Recommendations

Rank the cross-dimension prioritized recommendations. Explain the ordering using leverage, confidence, effort, time-to-feedback, and maintenance cost. The first recommendation is the default implementation candidate.

Every prioritized recommendation must have a concrete title, such as `Fix validate:changed so changed integration tests actually run`. Avoid taxonomy-only titles.

For every prioritized recommendation, include:

- **Finding**: one or two clear sentences that explain the concrete issue or improvement
- **Example**: one representative file, command, workflow, or user path that shows the issue
- **Actual behavior**: what happens today
- **Expected behavior**: what should happen instead
- **Why it matters**: the concrete risk, false confidence, repeated failure, or wasted effort
- **Evidence**: concrete file references, commands, configs, or observed behavior
- **Current behavior**: how it works today, including exact files, commands, config paths, and the conditions where it does or does not apply
- **Observed gap**: the mismatch, missing route, contradiction, weak signal, or navigation friction
- **Expected new behavior**: what will be true after the change
- **Why prioritized here**: why this outranks lower items or follows higher items
- **Dependencies and sequencing**: what this depends on and what it unlocks
- **Implementation approach**: concrete change shape, not code-level design unless needed
- **Files and commands likely to change**: expected edit surface and command surface
- **Proof plan**: checks, dry-runs, file reads, or runtime observations that would prove the gap is closed
- **Classification**: audit dimension, control type, and regulation category
- **Risks and alignment questions**: decisions that must be settled before implementation
- **Do not build yet**: tempting adjacent controls to defer and why

For validation or command-routing recommendations, include the repro command, actual planned command or observed behavior, expected command or behavior, and the exact reason the current command does not cover the changed surface.

For instruction-surface recommendations, also include what stays in `AGENTS.md`, what moves out, destination artifact, content classification, expected always-on token impact when relevant, and acceptance criteria.

When instruction-surface refactoring is a prioritized recommendation, make it implementation-ready: quote only the current headings or bullets being changed, classify each change as remove/rewrite/relocate/add, name the destination file and section for relocated content, and specify the resulting `AGENTS.md` / skills / docs / scripts structure.

Group lower-priority items by audit dimension so the user can still see the full option space.

## 4. Alignment Questions

Ask one question at a time when alignment is needed. Include the recommended answer or preferred direction with each question.
