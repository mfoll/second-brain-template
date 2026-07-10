---
type: Type
_icon: puzzle
_color: "#8b5cf6"
_order: 9
_organized: true
---

# Skill

A Skill is a visible catalogue note for an agent skill package.

Use Skill notes to browse a skill's purpose, lifecycle, related Procedure, and package path. The executable package remains under `.agents/skills/`; the Skill note is the human- and graph-facing catalogue layer.

When updating a vault-owned skill, edit the actual `.agents/skills/<skill-name>/` package, not only its visible note. Update the catalogue when purpose, lifecycle, Procedure linkage, or package metadata changes. If a machine-local runtime exposes the skill through a symlink, verify that it still targets the vault package; do not maintain a copied wrapper as another source of truth.
