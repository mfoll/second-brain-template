#!/bin/sh

set -eu

usage() {
  cat <<'EOF'
Usage:
  scripts/configure-agent-skills.sh --runtime codex|claude [--check]
  scripts/configure-agent-skills.sh --target <skills-directory> [--check]

Links every retained package under .agents/skills into one runtime discovery
directory. Existing non-matching entries are reported and never overwritten.
EOF
}

runtime_name=""
target_dir=""
operation="install"

while [ "$#" -gt 0 ]; do
  case "$1" in
    --runtime)
      [ "$#" -ge 2 ] || { usage >&2; exit 2; }
      runtime_name=$2
      shift 2
      ;;
    --target)
      [ "$#" -ge 2 ] || { usage >&2; exit 2; }
      target_dir=$2
      shift 2
      ;;
    --check)
      operation="check"
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      usage >&2
      exit 2
      ;;
  esac
done

if [ -n "$runtime_name" ] && [ -n "$target_dir" ]; then
  echo "Choose --runtime or --target, not both." >&2
  exit 2
fi

case "$runtime_name" in
  codex)
    target_dir=${CODEX_HOME:-"${HOME}/.codex"}/skills
    ;;
  claude)
    target_dir=${CLAUDE_CONFIG_DIR:-"${HOME}/.claude"}/skills
    ;;
  "")
    [ -n "$target_dir" ] || { usage >&2; exit 2; }
    ;;
  *)
    echo "Unsupported runtime: $runtime_name" >&2
    echo "Use --target for another Agent Skills-compatible runtime." >&2
    exit 2
    ;;
esac

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
vault_root=$(dirname -- "$script_dir")
source_dir="$vault_root/.agents/skills"

if [ ! -d "$source_dir" ]; then
  echo "Canonical skill directory is missing: $source_dir" >&2
  exit 1
fi

# Validate the canonical packages before deciding anything about the runtime directory.
invalid_count=0
for package_dir in "$source_dir"/*; do
  [ -d "$package_dir" ] || continue
  if [ ! -f "$package_dir/SKILL.md" ]; then
    echo "Invalid package without SKILL.md: $package_dir" >&2
    invalid_count=$((invalid_count + 1))
  fi
done

if [ "$operation" = "install" ]; then
  mkdir -p "$target_dir"
elif [ ! -d "$target_dir" ]; then
  if [ "$invalid_count" -gt 0 ]; then
    echo "Result: 0 linked, 0 verified, $invalid_count unresolved (invalid packages; nothing installed)."
    exit 1
  fi
  echo "Nothing installed yet: runtime skill directory not found: $target_dir"
  echo "Result: 0 linked, 0 verified, 0 unresolved (nothing installed)."
  exit 0
fi

target_dir=$(CDPATH= cd -- "$target_dir" && pwd)
linked_count=0
verified_count=0
conflict_count=$invalid_count

# Preflight the complete target before changing the runtime directory.
for package_dir in "$source_dir"/*; do
  [ -d "$package_dir" ] || continue
  [ -f "$package_dir/SKILL.md" ] || continue

  skill_name=$(basename -- "$package_dir")
  runtime_entry="$target_dir/$skill_name"

  if [ -L "$runtime_entry" ]; then
    link_target=$(readlink "$runtime_entry")
    if [ "$link_target" = "$package_dir" ]; then
      verified_count=$((verified_count + 1))
    else
      echo "Conflict: $runtime_entry links to $link_target" >&2
      conflict_count=$((conflict_count + 1))
    fi
  elif [ -e "$runtime_entry" ]; then
    echo "Conflict: $runtime_entry already exists and is not the managed link." >&2
    conflict_count=$((conflict_count + 1))
  elif [ "$operation" = "check" ]; then
    echo "Missing: $runtime_entry -> $package_dir" >&2
    conflict_count=$((conflict_count + 1))
  fi
done

if [ "$conflict_count" -gt 0 ]; then
  if [ "$operation" = "check" ] && [ "$invalid_count" -eq 0 ] && [ "$verified_count" -eq 0 ] && ! ls -A "$target_dir" | grep -q .; then
    echo "Result: 0 linked, 0 verified, $conflict_count unresolved (nothing installed yet, directory empty)."
    exit 0
  fi
  echo "Result: 0 linked, $verified_count verified, $conflict_count unresolved."
  exit 1
fi

if [ "$operation" = "install" ]; then
  for package_dir in "$source_dir"/*; do
    [ -f "$package_dir/SKILL.md" ] || continue
    skill_name=$(basename -- "$package_dir")
    runtime_entry="$target_dir/$skill_name"
    [ -L "$runtime_entry" ] && continue
    ln -s "$package_dir" "$runtime_entry"
    echo "Linked: $runtime_entry -> $package_dir"
    linked_count=$((linked_count + 1))
  done
fi

echo "Result: $linked_count linked, $verified_count verified, $conflict_count unresolved."
