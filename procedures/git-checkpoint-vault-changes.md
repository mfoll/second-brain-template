---
type: Procedure
status: Active
belongs_to: "[[vault]]"
related_to:
  - "[[procedures/maintain-project-human-view|Maintain Project Human View]]"
_organized: true
---

# Git Checkpoint Vault Changes

Use this procedure after an authorized vault edit when the work should receive a reviewed local checkpoint. Commit and network push are separate authorization decisions.

## Authorization

- A request to change, save, ingest, organize, or maintain the vault may authorize a task-scoped local commit under the deployed vault's policy.
- Push only when the current user instruction, approved shortcut, publish flow, or narrowly configured automation explicitly authorizes it.
- Persisted command approval is an execution mechanism, never broader permission.
- Keep credentials, raw sensitive documents and generated dumps out of the checkpoint. Ask before mixing unrelated work, broad restructuring, bulk ingestion, attachments, material outside the destination's agreed data scope, or unclear scope. Reuse existing authorization for approved project context.

## Steps

1. Check branch and status.
2. Reconcile affected Project summaries, actions, and human views when state changed.
3. Review the relevant full diff and preserve unrelated user changes.
4. Stage only task-scoped files and review the staged file list and high-risk content.
5. Commit with a concise description of the durable change.
6. Push only when explicitly authorized, never with force unless that exact rewrite was approved after its risk was stated.
7. Verify final status and report the commit, push result, and intentionally uncommitted files.

Use a `codex/<topic>` branch for broad, risky, experimental, or review-heavy changes. Read-only automations never stage, commit, or push; write-capable jobs operate only within their documented vault, scope, and command authorization.
