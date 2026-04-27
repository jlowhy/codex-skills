#!/usr/bin/env bash

set -euo pipefail

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "ERROR: not inside a git repository" >&2
  exit 1
fi

current_branch="$(git branch --show-current 2>/dev/null || true)"
if [[ -z "${current_branch}" ]]; then
  current_branch="DETACHED_HEAD"
fi

base_ref=""
fallback_note=""

if git rev-parse --verify origin/main >/dev/null 2>&1; then
  base_ref="origin/main"
elif git rev-parse --verify main >/dev/null 2>&1; then
  base_ref="main"
elif git rev-parse --verify origin/master >/dev/null 2>&1; then
  base_ref="origin/master"
  fallback_note="Fallback base branch used because origin/main and main were not found."
elif git rev-parse --verify master >/dev/null 2>&1; then
  base_ref="master"
  fallback_note="Fallback base branch used because origin/main and main were not found."
else
  echo "ERROR: could not detect a mainline branch (tried origin/main, main, origin/master, master)" >&2
  exit 2
fi

merge_base="$(git merge-base HEAD "${base_ref}")"
head_sha="$(git rev-parse HEAD)"
status_porcelain="$(git status --short --branch)"

commit_count="$(git rev-list --count "${merge_base}..HEAD")"
branch_diff_stat="$(git diff --stat "${merge_base}..HEAD" || true)"
branch_files="$(git diff --name-only "${merge_base}..HEAD" || true)"
working_tree_files="$(git diff --name-only || true)"
staged_files="$(git diff --cached --name-only || true)"
untracked_files="$(git ls-files --others --exclude-standard || true)"
recent_commits="$(git log --reverse --oneline "${merge_base}..HEAD" || true)"

echo "# Cleanup Scope"
echo
echo "## Repository State"
echo "- Current branch: ${current_branch}"
echo "- Base branch: ${base_ref}"
echo "- Merge base: ${merge_base}"
echo "- HEAD: ${head_sha}"
echo "- Commits since merge base: ${commit_count}"
if [[ -n "${fallback_note}" ]]; then
  echo "- Base branch note: ${fallback_note}"
fi
echo
echo "## Status"
if [[ -n "${status_porcelain}" ]]; then
  printf '%s\n' "${status_porcelain}"
else
  echo "(clean working tree)"
fi
echo
echo "## Commit Range"
echo "\`${merge_base}..HEAD\`"
echo
echo "## Commits Since Merge Base"
if [[ -n "${recent_commits}" ]]; then
  printf '%s\n' "${recent_commits}"
else
  echo "(no commits ahead of base)"
fi
echo
echo "## Files Changed On Branch"
if [[ -n "${branch_files}" ]]; then
  printf '%s\n' "${branch_files}"
else
  echo "(no committed file changes relative to base)"
fi
echo
echo "## Branch Diff Stat"
if [[ -n "${branch_diff_stat}" ]]; then
  printf '%s\n' "${branch_diff_stat}"
else
  echo "(no committed diff stat relative to base)"
fi
echo
echo "## Unstaged Working Tree Files"
if [[ -n "${working_tree_files}" ]]; then
  printf '%s\n' "${working_tree_files}"
else
  echo "(none)"
fi
echo
echo "## Staged But Uncommitted Files"
if [[ -n "${staged_files}" ]]; then
  printf '%s\n' "${staged_files}"
else
  echo "(none)"
fi
echo
echo "## Untracked Files"
if [[ -n "${untracked_files}" ]]; then
  printf '%s\n' "${untracked_files}"
else
  echo "(none)"
fi
