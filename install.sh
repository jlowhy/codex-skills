#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
target="${CODEX_HOME:-$HOME/.codex}/skills"

usage() {
  echo "Usage: $0 <skill...> | --bundle <bundle>"
}

skills=()

if [[ "$#" -eq 0 ]]; then
  usage >&2
  exit 1
fi

while [[ "$#" -gt 0 ]]; do
  case "$1" in
    --bundle)
      if [[ "$#" -lt 2 ]]; then
        usage >&2
        exit 1
      fi
      bundle_file="$repo_dir/bundles/$2.txt"
      if [[ ! -f "$bundle_file" ]]; then
        echo "Missing bundle: $2" >&2
        exit 1
      fi
      while IFS= read -r skill || [[ -n "$skill" ]]; do
        [[ -z "$skill" || "$skill" == \#* ]] && continue
        skills+=("$skill")
      done < "$bundle_file"
      shift 2
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      skills+=("$1")
      shift
      ;;
  esac
done

mkdir -p "$target"
backup_dir="$target/.backup/$(date +%Y%m%d-%H%M%S)"

for skill in "${skills[@]}"; do
  src="$repo_dir/skills/$skill"
  dest="$target/$skill"

  if [[ ! -d "$src" ]]; then
    echo "Missing skill: $skill" >&2
    exit 1
  fi

  if [[ -L "$dest" ]]; then
    rm "$dest"
  elif [[ -e "$dest" ]]; then
    mkdir -p "$backup_dir"
    mv "$dest" "$backup_dir/$skill"
    echo "Backed up $dest -> $backup_dir/$skill"
  fi

  ln -s "$src" "$dest"
  echo "Installed $skill -> $dest"
done
