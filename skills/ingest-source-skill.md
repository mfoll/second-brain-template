---
type: Skill
status: Active
belongs_to:
  - "[[vault]]"
wraps: "[[procedures/ingest-source|Ingest Source]]"
package_path: ".agents/skills/ingest-source/"
_organized: true
---

# Ingest Source Skill

Incorporate a paper, webpage, document or other external material into the vault, preserving provenance and connecting useful knowledge to existing notes.

Example request: “Add this paper to my brain.”

For mixed or unclassified captures, use [[skills/process-inbox-skill|Process Inbox]], which delegates external material to this workflow.

The matching Procedure owns the workflow; the package under `.agents/skills/ingest-source/` makes it discoverable to compatible agents.
