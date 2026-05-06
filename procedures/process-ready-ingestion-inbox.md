---
type: Procedure
status: Active
Belongs to: "[[vault]]"
_organized: true
---

# Process Ready Ingestion Inbox

## Goal

Process [[ready-to-ingest]] when `ingest_ready: true`. Route its body through [[procedures/process-inbox]], preserve the reusable note, and clear only content that has been processed or deliberately deferred elsewhere.

## Steps

1. Read `AGENTS.md` and the relevant Project note before changing the vault.
2. Confirm the current scope and avoid unrelated edits.
3. Make the smallest useful change that satisfies the workflow.
4. Validate links, frontmatter, and retrieval paths touched by the change.
5. Report what changed, what was left alone, and any follow-up needed.

## Boundaries

Do not add private source material, secrets, credentials, cache files, generated dumps, or machine-specific paths to durable vault notes.
