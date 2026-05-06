---
type: Procedure
status: Active
Belongs to: "[[vault]]"
_organized: true
---

# Update Project Summary

Use this procedure when project-scoped work changes what a future human or agent needs to know to resume the project.

## Goal

Keep a Project note useful as an entry point without turning it into a full archive.

## When To Run

- The user asks to update, refresh, reconcile, maintain, or save project state.
- Source ingestion changes project-level understanding, evidence, caveats, or next steps.
- Project work changes outcome, scope, status, active workflows, important sources, ADRs, open questions, or several linked notes.
- A lint or health review reports that the Project note appears stale.
- Next-action reconciliation changes enough context that the summary would mislead future work.

## Steps

1. Identify the active Project note from the user request, workspace pointer, or linked context.
2. Read the Project note's current structure before editing.
3. Review relevant linked notes through `Belongs to`, `Related to`, `Has`, backlinks, body links, and saved views.
4. Update only affected sections, commonly `## Purpose`, `## Current Context`, `## Active Workflows`, `## Important Notes`, `## Sources`, `## Open Questions`, `## Next Actions`, and `## Maintenance Log`.
5. Preserve uncertainty. Do not present provisional answers, unverified source claims, or user ideas as settled policy.
6. Link to detailed notes instead of copying long content into the Project note.
7. Check whether changed context should create or update typed notes such as Question, Concept, Responsibility, Procedure, ADR, Source, or another current Type.
8. Make only direct high-confidence typed-note updates. Defer broad cascade effects to [[procedures/review-vault-health]].
9. Add a dated Maintenance Log entry when the update changes project state.
10. Review the diff and report what changed.

## Output Standard

After the update, the Project note should tell a future agent where to start, what is known, what is unresolved, and which linked notes matter most.


## Guardrails

- Keep edits scoped to the user's request and the relevant Project or Source.
- Use `Belongs to`, `Related to`, and `Has` for relationships.
- Do not add secrets, credentials, local cache paths, generated dumps, or machine-specific setup details unless the note is explicitly about that local setup.
- Ask before creating new Types, broad relationship rewrites, mass moves, deletions, or public/private visibility changes.
