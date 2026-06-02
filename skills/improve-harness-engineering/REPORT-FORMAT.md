# Harness Engineering Report Format

The report must show the whole harness before ranking implementation-ready recommendations.

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

- **Current state**: what exists and where
- **Issues found**: evidence-bound gaps, contradictions, or friction
- **Candidate improvements**: viable options, not only the favorite
- **Preferred recommendation**: the best option for this dimension and why
- **Do not build yet**: tempting controls to defer and why

## 3. Prioritized Recommendations

Rank the cross-dimension prioritized recommendations. Explain the ordering using leverage, confidence, effort, time-to-feedback, and maintenance cost. The first recommendation is the default implementation candidate.

For every prioritized recommendation, include:

- **Evidence**: concrete file references, commands, configs, or observed behavior
- **Current behavior**: how it works today, including exact files, commands, config paths, and the conditions where it does or does not apply
- **Observed gap**: the mismatch, missing route, contradiction, weak signal, or navigation friction
- **Expected new behavior**: what will be true after the change
- **Why prioritized here**: why this outranks lower items or follows higher items
- **Implementation approach**: concrete change shape, not code-level design unless needed
- **Files and commands likely to change**: expected edit surface and command surface
- **Proof plan**: checks, dry-runs, file reads, or runtime observations that would prove the gap is closed
- **Risks and alignment questions**: decisions that must be settled before implementation
- **Do not build yet**: tempting adjacent controls to defer and why

For instruction-surface recommendations, also include what stays in `AGENTS.md`, what moves out, destination artifact, content classification, expected always-on token impact when relevant, and acceptance criteria.

When instruction-surface refactoring is a prioritized recommendation, make it implementation-ready: quote only the current headings or bullets being changed, classify each change as remove/rewrite/relocate/add, name the destination file and section for relocated content, and specify the resulting `AGENTS.md` / skills / docs / scripts structure.

Group lower-priority items by audit dimension so the user can still see the full option space.

## 4. Alignment Questions

Ask one question at a time when alignment is needed. Include the recommended answer or preferred direction with each question.
