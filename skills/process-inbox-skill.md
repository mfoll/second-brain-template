---
type: Skill
status: Active
belongs_to:
  - "[[vault]]"
wraps: "[[procedures/process-inbox|Process Inbox]]"
package_path: ".agents/skills/process-inbox/"
_organized: true
---

# Process Inbox Skill

Triage and organize unprocessed captures within the requested scope: internal ideas, questions, project updates and external material. Preserve useful details and leave blocked items unresolved.

This Skill supports optional deferred capture; direct saving does not require an Inbox or Tolaria.

Example request: “Organize last week’s captures.”

For external material supplied directly, use [[skills/ingest-source-skill|Ingest Source]]. To process only explicitly ready-marked captures, use [[skills/process-ready-ingestion-inbox-skill|Process Ready Ingestion Inbox]].

The matching Procedure owns the workflow; the package under `.agents/skills/process-inbox/` makes it discoverable to compatible agents.
