---
type: Type
_icon: puzzle
_color: "#8b5cf6"
_order: 9
_organized: true
---

# Skill

A Skill is the visible catalogue half of a vault-owned agent skill package.

Use Skill notes to browse a skill's purpose, lifecycle, related Procedure, and package path. The executable package remains under `.agents/skills/`; the Skill note is the human- and graph-facing catalogue layer.

## Pair contract

Every installed vault-owned Skill is one coherent pair:

- a visible `type: Skill` note with `status`, a resolvable `wraps` link to its Procedure, and `package_path` pointing to `.agents/skills/<skill-name>/`;
- a matching package containing `SKILL.md`, whose frontmatter `name` equals `<skill-name>` and whose source-of-truth pointer names the same Procedure.

The two sides must describe the same active purpose and lifecycle. Any scripts or supporting files they name must exist. Add or update both sides together. To retire a Skill, remove the installed package from `.agents/skills/` and archive or remove its catalogue note and active routes; an archived note must not leave a dormant package discoverable by the runtime. Git provides rollback. Allow a one-sided runtime-only exception only when it is explicit and documented.

When updating a vault-owned skill, edit the actual package, not only its visible note. If a machine-local runtime exposes the skill through a symlink, verify that it still targets the vault package; do not maintain a copied wrapper as another source of truth. Detailed execution remains in the Procedure rather than being duplicated into `SKILL.md`.
