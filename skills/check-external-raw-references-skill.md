---
type: Skill
status: Active
Belongs to:
  - "[[vault]]"
Related to:
  - "[[agent-skill]]"
wraps: "[[procedures/check-external-raw-references|Check External Raw References]]"
package_path: ".agents/skills/check-external-raw-references/"
_organized: true
---

# Check External Raw References Skill

Activates the external raw-file reference maintenance workflow for `root_key` plus `relative_path` Source notes.

The durable workflow source is [[procedures/check-external-raw-references|Check External Raw References]]. The package under `.agents/skills/check-external-raw-references/` is the agent activation wrapper and includes the deterministic refresh script.

Package files:

- [SKILL.md](../.agents/skills/check-external-raw-references/SKILL.md)
- [check_external_raw_references.py](../.agents/skills/check-external-raw-references/scripts/check_external_raw_references.py)
