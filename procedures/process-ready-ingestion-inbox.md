---
type: Procedure
status: Active
belongs_to: "[[vault]]"
related_to:
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

## Preserve original captures

Before clearing processed body content from [[ready-to-ingest]], follow the original-capture preservation rule in [[procedures/process-inbox]]. Verify an approved recovery copy of the exact current capture; reuse the configured backup method and existing authorization.

A push is not a prerequisite for ingestion. If no suitable recovery copy is available, keep the original body visible and continue only non-destructive preparation. A later checkpoint of synthesized notes cannot recover original text that was never preserved.

## Steps

1. Find notes with `ingest_ready: true`.
2. Ignore ordinary Inbox notes that do not have the ready flag.
3. For [[ready-to-ingest]], inspect only body content below the H1. If there is no content below the H1, make no changes.
4. Treat ready body content as unprocessed capture and follow [[procedures/process-inbox]]. Delegate clear external sources to [[procedures/ingest-source]].
5. Create or update only notes directly required by the ready-marked content.
6. Clear processed body content from [[ready-to-ingest]] only after the preservation rule above is satisfied and the content has been moved, synthesized, archived, or deliberately discarded.
7. Preserve the frontmatter, H1, and `ingest_ready: true` flag on [[ready-to-ingest]].
8. If user feedback would be useful but is not required for safe processing, ingest anyway, clear the preserved and processed body, and report the optional discussion point in the automation result. Create a `Question` or `Next Actions` item only when the issue is durable, decision-driving, or creates real follow-up work.
9. If a concrete ambiguity about meaning, routing, a new disclosure risk or a broad structural change requires user input, keep the affected original content visible and add a concrete `## Ingestion Questions` section. Reuse agreed source, tool and destination permissions for routine items.
10. Review the task-scoped diff. If this runs from automation, commit and push only when the automation has explicit permission and the diff contains only material permitted in that destination. For scheduled main-branch jobs, use an explicit command such as `git push origin main` rather than a bare `git push`, so persisted approvals can stay command-scoped.

## Ingestion Feedback

Ready-ingestion feedback is advisory, not a blocking gate. Continue processable work without waiting for optional feedback; clear original text only after preservation and commit or push only under existing authorization.

Use the feedback standards from [[procedures/process-inbox]] and delegated workflows such as [[procedures/ingest-source]]. In the automation report, briefly state:

- what was ingested or organized;
- what was new, useful, weak, duplicate, or intentionally ignored;
- which existing notes or projects the material connected to;
- which questions were answered, created as durable `Question` notes with a maintenance rationale, or left as optional discussion points;
- whether any material remains blocked in [[ready-to-ingest]] under `## Ingestion Questions`.

Do not leave optional feedback inside [[ready-to-ingest]] if the underlying content has already been safely processed. Use `## Ingestion Questions` there only for true blockers. Ready-ingestion should create zero new `Question` notes by default; create them only when the unresolved issue is consequential, likely to recur, decision-driving, expected to guide active work, or needed as a future retrieval anchor.

## Stop Conditions

Keep secrets, credentials, raw sensitive documents and generated dumps out of the checkpoint. Ask before including unrelated edits, attachments, material outside the destination's agreed data scope, or content not clearly derived from ready-marked notes. Reuse existing authorization for content within the agreed scope.


## Guardrails

- Keep edits scoped to the user's request and the relevant Project or Source.
- Use `belongs_to`, `related_to`, and `has` for relationships.
- Do not add secrets, credentials, local cache paths, generated dumps, or machine-specific setup details unless the note is explicitly about that local setup.
- Ask before creating new Types, broad relationship rewrites, mass moves, deletions, or public/private visibility changes.
