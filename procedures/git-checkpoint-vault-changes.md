---
type: Procedure
status: Active
Belongs to: "[[vault]]"
Related to:
  - "[[procedures/maintain-project-human-view|Maintain Project Human View]]"
_organized: true
---

# Git Checkpoint Vault Changes

Use this procedure after an agent changes vault files and the user has not asked to leave the work uncommitted.

## Goal

Keep Git as the audit trail, backup layer, and rollback path while avoiding accidental commits of unrelated or sensitive material.

## Steps

1. Check repository state with `git status --short --branch`.
2. Review changed scope with `git diff --stat` and `git diff` when useful.
3. Exclude local junk such as `.DS_Store`, caches, temporary renders, generated dumps, and unrelated files.
4. If unrelated user edits are present, stage only task-scoped files or ask before mixing them into the commit.
5. If the diff contains important project-scoped changes, confirm the Project Surface Check from [[procedures/maintain-project-human-view|Maintain Project Human View]] has been applied or intentionally skipped because the Project has `Project view: false`.
6. Stage the intended files.
7. Review staged scope with `git diff --cached --stat` and `git diff --cached --name-only`.
8. Commit with a concise message describing the knowledge, workflow, or structural change.
9. Push the current branch only when the user requested it, the workflow explicitly allows it, or the repository's operating policy makes push part of normal checkpointing.
10. Verify final state with `git status --short --branch`.
11. Report branch, commit hash, push result, files changed, and any files intentionally left uncommitted.

## Branch Policy

Use direct commits to `main` for small coherent vault maintenance changes. Use a short-lived branch such as `codex/<topic>` for broad, risky, experimental, or review-heavy changes.

## Stop Conditions

Ask before pushing broad diffs, attachments, secrets, credentials, sensitive documents, generated dumps, visibility changes, or changes outside the stated task scope. Never force-push unless the user explicitly asks and the risk has been stated.


## Guardrails

- Keep edits scoped to the user's request and the relevant Project or Source.
- Use `Belongs to`, `Related to`, and `Has` for relationships.
- Do not add secrets, credentials, local cache paths, generated dumps, or machine-specific setup details unless the note is explicitly about that local setup.
- Ask before creating new Types, broad relationship rewrites, mass moves, deletions, or public/private visibility changes.
