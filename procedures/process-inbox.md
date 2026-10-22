---
type: Procedure
status: Active
belongs_to: "[[vault]]"
_organized: true
---

# Process Inbox

Use this procedure when the user asks to organize, triage, clean up, or process unprocessed captures.

## Goal

Move captured material from vague storage into retrievable structure, or deliberately leave it unprocessed with a clear reason, while giving advisory feedback about the questions, links, and judgment calls surfaced during processing.

## Preserve Original Captures

Before ingesting an Inbox note in a way that will delete, clear, archive, heavily rewrite, or otherwise obscure the original captured text, verify that its exact current content is recoverable through the deployment's approved backup method. Reuse that configured method without a new confirmation for each capture. A local checkpoint, protected backup outside Git, or existing remote checkpoint may satisfy this rule when appropriate for the material.

Never push raw captures merely to unblock ingestion. A remote checkpoint requires both suitable content and existing push authority. If no approved recovery copy is available, leave the original capture visible and continue only non-destructive preparation. Creating a backup must not introduce an unapproved storage destination or put restricted material into Git.

Before clearing, archiving, deleting, or heavily rewriting an internal user capture, also verify that concrete future-use details have been promoted into retrievable notes. Inbox captures follow the same memory-quality standard as chat captures: preserve plans, things to test, constraints, caveats, rejected options, examples, exact terminology, and retrieval keywords when they matter for future resumption. The recovery copy is an audit and rollback layer, not the normal way to find missing details.

## Steps

1. Identify the intended scope: all unprocessed notes, a named Project, recent captures, [[ready-to-ingest]], or specific files named by the user.
2. Find candidates using `_organized: false`, `status: Unprocessed`, `ingest_ready: true`, recent modified files, Inbox views, and the user's explicit list.
3. For each candidate, classify it as external source, internal idea, project update, question, reusable concept, responsibility, procedure, ADR candidate, duplicate, obsolete note, or ambiguous capture.
4. If the capture is clearly external or re-checkable material, follow [[procedures/ingest-source]] instead of recreating ingestion rules here.
5. If the capture is an internal durable idea, decide whether to update an existing typed note or create a new Project, Question, Concept, Responsibility, Procedure, ADR, or Note. Do not use `Source` for ordinary internal brainstorms, planning notes, or chat captures merely to preserve raw text. When an exploration cluster has gained an outcome, actions, collaborators or a deliverable, propose promoting it to a Project instead of creating one silently.
6. Add the minimum useful relationships and body links needed for retrieval. Prefer a few strong links over broad weak tagging. `belongs_to` must reach a Responsibility; when no Project or Responsibility owns the note yet, use an exploration Topic under the Responsibility the deployment designates for exploratory reading rather than `related_to` alone, or leave the note unprocessed under step 10 when the deployment designates none ([[adr/0011-root-belongs-to-at-responsibilities-and-home-exploration-clusters-in-topics|ADR 0011]]).
7. Mark a note organized only when it is findable through a Project, Responsibility, Topic, Source, Question, Concept, Procedure, ADR, saved view, backlink, or explicit archive convention.
   - When a note is organized enough to leave Inbox, add or preserve `_organized: true` in frontmatter.
8. Use `_archived: true` for retained material that should no longer appear in active resumption.
9. Delete only when the content has no retrieval value, contains junk, or has already been fully promoted elsewhere and provenance is not useful.
10. If placement is unclear, leave the note unprocessed and add a concrete `## Triage Question` rather than forcing a poor structure.
11. Prepare advisory ingestion feedback using the standard below.
12. Review the diff and summarize promoted notes, archived notes, unresolved questions, and anything intentionally left unprocessed.

## Ingestion Feedback

Inbox processing should not be a blind swallow of captured material. After processing, tell the user what the agent noticed. This feedback is advisory and should not block ingestion when the capture is processable.

Include concise feedback in the final response or automation report:

- what was promoted, linked, archived, deferred, or intentionally not saved;
- which existing Projects, Questions, Concepts, Procedures, ADRs, Responsibilities, or priorities the capture connected to;
- which questions the capture contained or raised;
- which questions the agent answered during processing;
- which durable questions, next actions, or synthesis updates were created or changed;
- which optional discussion points the user may want to revisit.

Do not stop processing merely because the feedback could trigger a discussion. Continue organizing, commit, and push according to the normal checkpoint rules when the material can be processed safely.

Stop and ask only when the missing answer is required to avoid misrouting, privacy leakage, destructive edits, broad structural changes, or another unsafe outcome.

When a capture contains questions:

- Answer what can be answered from the capture plus relevant vault context, using explicit assumptions when needed.
- Create or update durable `Question` notes only when the unresolved issue is consequential, likely to recur, decision-driving, expected to guide active work, or needed as a future retrieval anchor.
- Leave optional discussion prompts in the user-facing feedback instead of blocking ingestion or writing them into durable notes.
- Keep the original material visible with `## Ingestion Questions` only for true blockers where user input is required before the capture can be safely or coherently processed.
- Normal Inbox processing should create zero new `Question` notes by default. If it creates any, report why they are worth maintaining.

## Organization Standard

A note can leave Inbox only when a future human or agent can explain where to start looking for it and why it belongs there.


## Guardrails

- Keep edits scoped to the user's request and the relevant Project or Source.
- Use `belongs_to`, `related_to`, and `has` for relationships.
- Do not add secrets, credentials, local cache paths, generated dumps, or machine-specific setup details unless the note is explicitly about that local setup.
- Ask before creating new Types, broad relationship rewrites, mass moves, deletions, or public/private visibility changes.
