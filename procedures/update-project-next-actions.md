---
type: Procedure
status: Active
Belongs to: "[[vault]]"
Related to:
  - "[[procedures/update-project-summary]]"
_organized: true
---

# Update Project Next Actions

Use this procedure when project-scoped work changes what should happen next.

## Goal

Keep a Project note's `## Next Actions` section aligned with actual project state.

## When To Run

- The user asks to save, update, remember, maintain, or reconcile project work.
- A listed action was completed, partially completed, invalidated, or replaced.
- A chat, source ingestion, or project review creates a durable follow-up.
- A Project summary update changes what should happen next.

## Steps

1. Identify the active Project note from the workspace pointer, explicit user request, or nearby vault context.
2. Read the current `## Next Actions` section and nearby project context.
3. Remove completed actions unless the completion should be preserved in the Maintenance Log.
4. Rewrite partially completed actions so they describe only the remaining work.
5. Remove stale or duplicate actions that no longer help project resumption.
6. Add new durable actions as outcome-oriented checkboxes or bullets, preserving the Project's existing style.
7. For each added or changed action, decide whether it implies a durable typed note such as Question, Concept, Responsibility, Procedure, ADR, Source, or Project.
8. Create or update typed notes only when the need is direct and high-confidence. Link them from `## Open Questions`, `## Important Notes`, `## Active Workflows`, `Has`, `Related to`, or another appropriate section.
9. If an action answers an existing Question, update that Question's status or current answer instead of leaving it stale.
10. Keep the list scannable. A short list is preferred, but do not enforce an arbitrary count when the active project genuinely needs more.
11. Add a short Maintenance Log entry for meaningful state changes.
12. If the next-action update changes project state, important context, scope, open questions, important notes, active workflows, or guardrails, run or apply [[procedures/update-project-summary]] so the Project note stays current as the live project home.
13. Review the diff and report remaining work.

## Style

Phrase actions as resumable outcomes, not tiny implementation steps. Keep one-off microtasks in the active chat or external task system. Do not hide durable questions inside next actions; promote them to Question notes when they should be findable later. Preserve the standard Project structure from [[project]] when editing: Outcome, Current State, Scope and Boundaries, Next Actions, Open Questions, Important Notes, and Maintenance Log should remain easy to find in active Project notes.


## Guardrails

- Keep edits scoped to the user's request and the relevant Project or Source.
- Use `Belongs to`, `Related to`, and `Has` for relationships.
- Do not add secrets, credentials, local cache paths, generated dumps, or machine-specific setup details unless the note is explicitly about that local setup.
- Ask before creating new Types, broad relationship rewrites, mass moves, deletions, or public/private visibility changes.
