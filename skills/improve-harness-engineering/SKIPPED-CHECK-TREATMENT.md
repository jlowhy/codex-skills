# Skipped Check Treatment

Do not treat every skipped check as a bug. For each relevant check that is not run, classify the skipped check and recommend the right treatment.

## Skipped Check Classification

- **Cheap and targeted**: local, deterministic, low-cost, and directly mapped to the changed surface.
- **Expensive but relevant**: slow, infra-heavy, flaky, credential-gated, or broad, but relevant to the changed surface.
- **Policy-excluded**: intentionally outside this workflow's scope by team policy.
- **Irrelevant**: not meaningfully connected to the changed surface.

## Recommended Treatment

- **Run** cheap targeted lanes in the local or changed-file workflow.
- **Warn** for expensive but relevant lanes: make the validation output say the lane was intentionally skipped and show the exact follow-up command.
- **Document** policy-excluded checks, and prefer surfacing the policy in validation output or dry-run.
- **Ignore** irrelevant lanes only when the mapping is defensible.

When a check is deliberately skipped, the harness issue is not absence alone. The issue is silent skipping that creates false confidence for users or agents.
