---
type: Skill
status: Active
belongs_to:
  - "[[vault]]"
wraps: "[[procedures/process-ready-ingestion-inbox|Process Ready Ingestion Inbox]]"
package_path: ".agents/skills/process-ready-ingestion-inbox/"
_organized: true
---

# Process Ready Ingestion Inbox Skill

Process only captures marked `ingest_ready: true`, preserving the reusable [[ready-to-ingest]] note and leaving other Inbox material untouched. This is an optional entry point for explicit intake queues, including scheduled processing; it enables no schedule by itself.

This Skill supports optional deferred capture; direct saving does not require an Inbox or Tolaria.

Example request: “Process only the captures I marked ready.”

This workflow selects ready-marked captures, then follows [[skills/process-inbox-skill|Process Inbox]], which delegates external material to [[skills/ingest-source-skill|Ingest Source]]. For a broader requested Inbox scope, choose Process Inbox directly.

The matching Procedure owns the workflow; the package under `.agents/skills/process-ready-ingestion-inbox/` makes it discoverable to compatible agents.
