---
type: Procedure
status: Active
Belongs to: "[[vault]]"
Related to:
  - "[[procedures/process-inbox]]"
  - "[[procedures/ingest-source]]"
_organized: true
---

# Process Ready Ingestion Inbox

Use this procedure when an agent or scheduled workflow processes notes explicitly marked as ready for ingestion.

## Goal

Process only ready-marked intake material, preserve the reusable intake note, provide advisory ingestion feedback, and avoid surprising edits to unrelated Inbox content.

## Scope

A note is in scope only when its frontmatter contains:

```yaml
ingest_ready: true
```

The standing intake note [[ready-to-ingest]] is reusable. Never delete, archive, rename, or move it during this workflow.

## Steps

1. Find notes with `ingest_ready: true`.
2. Ignore ordinary Inbox notes that do not have the ready flag.
3. For [[ready-to-ingest]], inspect only body content below the H1. If there is no content below the H1, make no changes.
4. Treat ready body content as unprocessed capture and follow [[procedures/process-inbox]]. Delegate clear external sources to [[procedures/ingest-source]].
5. Create or update only notes directly required by the ready-marked content.
6. Clear processed body content from [[ready-to-ingest]] only after it has been moved, synthesized, archived, or deliberately discarded.
7. Preserve the frontmatter, H1, and `ingest_ready: true` flag on [[ready-to-ingest]].
8. If user feedback would be useful but is not required for safe processing, ingest anyway, clear the processed body, and report the optional discussion point in the automation result or a durable linked `Question` or `Next Actions` item.
9. If user input is required to know what the content is, where it belongs, whether it is safe or private, or whether a broad structural change is approved, keep the original content visible and add a concrete `## Ingestion Questions` section.
10. Review the task-scoped diff. If this runs from automation, commit and push only when the automation has explicit permission and the diff contains no unrelated or sensitive material.

## Ingestion Feedback

Ready-ingestion feedback is advisory, not a blocking gate. The automation should keep ingesting, organizing, committing, and pushing processable material even if the user never answers the feedback.

Use the feedback standards from [[procedures/process-inbox]] and delegated workflows such as [[procedures/ingest-source]]. In the automation report, briefly state:

- what was ingested or organized;
- what was new, useful, weak, duplicate, or intentionally ignored;
- which existing notes or projects the material connected to;
- which questions were answered, created as durable `Question` notes, or left as optional discussion points;
- whether any material remains blocked in [[ready-to-ingest]] under `## Ingestion Questions`.

Do not leave optional feedback inside [[ready-to-ingest]] if the underlying content has already been safely processed. Use `## Ingestion Questions` there only for true blockers.

## Stop Conditions

Stop and ask before committing or pushing if the diff includes unrelated edits, attachments, secrets, credentials, sensitive documents, generated dumps, or material not clearly derived from ready-marked notes.


## Guardrails

- Keep edits scoped to the user's request and the relevant Project or Source.
- Use `Belongs to`, `Related to`, and `Has` for relationships.
- Do not add secrets, credentials, local cache paths, generated dumps, or machine-specific setup details unless the note is explicitly about that local setup.
- Ask before creating new Types, broad relationship rewrites, mass moves, deletions, or public/private visibility changes.
