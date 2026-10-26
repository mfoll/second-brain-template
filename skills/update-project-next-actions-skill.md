---
type: Skill
status: Active
belongs_to:
  - "[[vault]]"
wraps: "[[procedures/update-project-next-actions|Update Project Next Actions]]"
package_path: ".agents/skills/update-project-next-actions/"
_organized: true
---

# Update Project Next Actions Skill

Reconcile what should happen next: remove completed actions, rewrite remaining work and merge overlaps. Refresh related project state when the action changes affect it.

Example request: “Update this Project’s next actions now that the pilot is complete.”

For a broader refresh of current state, scope, blockers and links, use [[skills/update-project-summary-skill|Update Project Summary]]. Both workflows keep actions and state consistent.

The matching Procedure owns the workflow; the package under `.agents/skills/update-project-next-actions/` makes it discoverable to compatible agents.
