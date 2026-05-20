---
type: Procedure
status: Active
belongs_to: "[[vault]]"
related_to:
  - "[[procedures/maintain-project-human-view|Maintain Project Human View]]"
_organized: true
---

# Update Project Summary

Use this procedure when project-scoped work changes what a future human or agent needs to know to resume the project.

## Goal

Keep a Project note useful as the live human and agent entry point without turning it into a full archive.

The Project note should stay coherent enough that opening it gives the current state, the intended outcome, the key boundaries, the next useful actions, the unresolved questions, and the few notes worth reading first.

## When To Run

- The user asks to update, refresh, reconcile, maintain, or save project state.
- Source ingestion changes project-level understanding, evidence, caveats, open questions, important notes, active workflows, or next steps.
- Project work changes outcome, scope, status, active workflows, important sources, ADRs, open questions, or several linked notes.
- A lint or health review reports that the Project note appears stale.
- Next-action reconciliation changes enough context that the summary would mislead future work.

## Steps

1. Identify the active Project note from the user request, workspace pointer, or linked context.
2. Read the Project note's current structure before editing.
3. Review relevant linked notes through `belongs_to`, `related_to`, `has`, backlinks, body links, and saved views.
4. Normalize the note toward the Project structure in [[project]] when it has drifted: Outcome, Current State, Scope and Boundaries, useful project-specific working context, Active Workflows when applicable, Next Actions, Open Questions, Important Notes, optional Do Not Do Yet, and Maintenance Log.
5. Update only affected sections, commonly `## Outcome`, `## Current State`, `## Scope and Boundaries`, `## Active Workflows`, `## Important Notes`, `## Sources`, `## Open Questions`, `## Next Actions`, and `## Maintenance Log`.
6. Preserve uncertainty. Do not present provisional answers, unverified source claims, or user ideas as settled policy.
7. Link to detailed notes instead of copying long content into the Project note.
8. Check whether changed context should create or update typed notes such as Question, Concept, Responsibility, Procedure, ADR, Source, or another current Type.
9. Make only direct high-confidence typed-note updates. Defer broad cascade effects to [[procedures/review-vault-health]].
10. Add a dated Maintenance Log entry when the update changes project state.
11. Run a Project Surface Check from [[procedures/maintain-project-human-view|Maintain Project Human View]] when the summary update changes current drafts, deliverables, decision-driving Questions, active workflows, key Sources, or the notes a human should open next.
12. Review the diff and report what changed.

## Output Standard

After the update, the Project note should tell a future human or agent where to start, what is current, what is in or out of scope, what is unresolved, what to do next, and which linked notes matter most.

Ingestion can update any relevant note. When ingestion changes project-level understanding, actions, open questions, important sources, active workflows, or guardrails, update the Project note as the live project home as well.

If the project is active and does not have `Project view: false`, keep its saved view as a small human working set. The view should usually contain 3-5 notes, not every linked note.


## Guardrails

- Keep edits scoped to the user's request and the relevant Project or Source.
- Use `belongs_to`, `related_to`, and `has` for relationships.
- Do not add secrets, credentials, local cache paths, generated dumps, or machine-specific setup details unless the note is explicitly about that local setup.
- Ask before creating new Types, broad relationship rewrites, mass moves, deletions, or public/private visibility changes.
