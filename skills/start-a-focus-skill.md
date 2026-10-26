---
type: Skill
status: Active
belongs_to:
  - "[[vault]]"
wraps: "[[procedures/start-a-focus|Start a Focus]]"
package_path: ".agents/skills/start-a-focus/"
_organized: true
---

# Start a Focus Skill

Start something new in the Brain through a short interview: an ongoing area, a finite outcome, a subject to explore or a first item to keep. The interview decides whether it becomes a Responsibility, a Project, a Topic or an addition to an existing note, and the agent proposes the smallest structure before writing.

Example request: “Start a new focus for the workshop I am preparing.”

Setup uses the same workflow for the first focus. For a single external item under existing work, use [[skills/ingest-source-skill|Ingest Source]] directly.

The matching Procedure owns the workflow; the package under `.agents/skills/start-a-focus/` makes it discoverable to compatible agents.
