---
type: Skill
status: Active
belongs_to:
  - "[[vault]]"
wraps: "[[procedures/update-project-summary|Update Project Summary]]"
package_path: ".agents/skills/update-project-summary/"
_organized: true
---

# Update Project Summary Skill

Refresh a Project’s current synthesis after significant work: state, scope, blockers and useful links. Reconcile next actions when the changed state affects them.

Example request: “Bring this Project up to date after today’s work.”

For a focused change to what should happen next, use [[skills/update-project-next-actions-skill|Update Project Next Actions]]. Both workflows update related project sections when needed.

The matching Procedure owns the workflow; the package under `.agents/skills/update-project-summary/` makes it discoverable to compatible agents.
