---
name: process-ready-ingestion-inbox
description: "Process only ingest_ready: true captures in the selected deployed vault; preserve the reusable intake note and leave other Inbox material untouched."
---

# Process Ready Ingestion Inbox

Process only captures marked `ingest_ready: true`, preserving the reusable `ready-to-ingest.md` note and leaving other Inbox material untouched. This is an optional entry point for explicit intake queues, including scheduled processing; it enables no schedule by itself.

This workflow selects ready-marked captures, then follows `process-inbox`, which delegates external material to `ingest-source`. For a broader requested Inbox scope, choose Process Inbox directly.

Read the vault `AGENTS.md` and `procedures/process-ready-ingestion-inbox.md` once for this task, then follow the Procedure as the source of truth. Verify its approved recovery copy before clearing original capture text; a push is not required. Reuse configured source, tool, destination and backup permissions. Keep edits task-scoped and report changed files, validation, and follow-up.

Select this package by the requested vault role, not its name alone. Reuse rules and the complete Procedure already read in this session while they remain current; reread after a relevant change.
