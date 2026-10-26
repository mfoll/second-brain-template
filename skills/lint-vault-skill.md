---
type: Skill
status: Active
belongs_to:
  - "[[vault]]"
wraps: "[[procedures/lint-vault|Lint Vault]]"
package_path: ".agents/skills/lint-vault/"
_organized: true
---

# Lint Vault Skill

Check metadata, links, hierarchy and other structural contracts. Report errors and warnings without applying fixes.

Example request: “Check the vault for broken links and structural defects.”

For judgment about usefulness, stale project state or unnecessary workflows, use [[skills/review-vault-health-skill|Review Vault Health]]. Lint findings can inform that review.

The matching Procedure owns the workflow; the package under `.agents/skills/lint-vault/` makes it discoverable to compatible agents.
