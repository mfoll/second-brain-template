---
type: Procedure
status: Active
Belongs to: "[[vault]]"
_organized: true
---

# Process Inbox

Use this procedure when the user asks to organize, triage, clean up, or process unprocessed captures.

## Goal

Move captured material from vague storage into retrievable structure, or deliberately leave it unprocessed with a clear reason.

## Steps

1. Identify the intended scope: all unprocessed notes, a named Project, recent captures, [[ready-to-ingest]], or specific files named by the user.
2. Find candidates using `_organized: false`, `status: Unprocessed`, `ingest_ready: true`, recent modified files, Inbox views, and the user's explicit list.
3. For each candidate, classify it as external source, internal idea, project update, question, reusable concept, responsibility, procedure, ADR candidate, duplicate, obsolete note, or ambiguous capture.
4. If the capture is clearly external or re-checkable material, follow [[procedures/ingest-source]] instead of recreating ingestion rules here.
5. If the capture is an internal durable idea, decide whether to update an existing typed note or create a new Project, Question, Concept, Responsibility, Procedure, ADR, Source, or Note.
6. Add the minimum useful relationships and body links needed for retrieval. Prefer a few strong links over broad weak tagging.
7. Mark a note organized only when it is findable through a Project, Responsibility, Topic, Source, Question, Concept, Procedure, ADR, saved view, backlink, or explicit archive convention.
   - When a note is organized enough to leave Inbox, add or preserve `_organized: true` in frontmatter.
8. Use `_archived: true` for retained material that should no longer appear in active resumption.
9. Delete only when the content has no retrieval value, contains junk, or has already been fully promoted elsewhere and provenance is not useful.
10. If placement is unclear, leave the note unprocessed and add a concrete `## Triage Question` rather than forcing a poor structure.
11. Review the diff and summarize promoted notes, archived notes, unresolved questions, and anything intentionally left unprocessed.

## Organization Standard

A note can leave Inbox only when a future human or agent can explain where to start looking for it and why it belongs there.


## Guardrails

- Keep edits scoped to the user's request and the relevant Project or Source.
- Use `Belongs to`, `Related to`, and `Has` for relationships.
- Do not add secrets, credentials, local cache paths, generated dumps, or machine-specific setup details unless the note is explicitly about that local setup.
- Ask before creating new Types, broad relationship rewrites, mass moves, deletions, or public/private visibility changes.
