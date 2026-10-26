---
type: Skill
status: Active
belongs_to:
  - "[[vault]]"
wraps: "[[procedures/review-vault-health|Review Vault Health]]"
package_path: ".agents/skills/review-vault-health/"
_organized: true
---

# Review Vault Health Skill

Assess whether the vault remains useful, current and easy to navigate. Recommend a few high-value improvements, read-only by default.

Example request: “Review whether this vault still helps me resume work.”

For mechanical defects, use [[skills/lint-vault-skill|Lint Vault]]. Health review interprets some of the same audit evidence; a structurally valid vault can still contain stale summaries or buried decisions.

The matching Procedure owns the workflow; the package under `.agents/skills/review-vault-health/` makes it discoverable to compatible agents.
