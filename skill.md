---
type: Type
_icon: puzzle-piece
_color: "#8b5cf6"
_order: 9
_organized: true
---

# Skill

A Skill is the visible catalogue half of a vault-owned agent skill package.

Use Skill notes to browse a skill's purpose, lifecycle, workflow owner, and package path. The executable package remains under `.agents/skills/`; the Skill note is the human- and graph-facing catalogue layer.

## Pair contract

Every installed vault-owned Skill is one coherent pair:

- a visible active `type: Skill` note with `status` and `package_path` pointing to `.agents/skills/<skill-name>/`;
- a matching package containing `SKILL.md`, whose frontmatter `name` equals `<skill-name>`.

Choose one explicit ownership mode. A Procedure-backed Skill has a resolvable `wraps` link; its package names and requires that complete Procedure, which is authoritative on conflict. It may retain operational detail; prefer thinness only after a clause audit proves that no trigger, prerequisite, hard safety or runtime guard, command, or bundled-resource instruction will be lost. A specialized standalone Skill omits `wraps`, states in its catalogue body that the package owns execution, and keeps the necessary workflow detail in `SKILL.md`; use this only when no durable Procedure already owns the workflow.

The catalogue note owns lifecycle; the package matches its purpose and must not contradict that state. Package-bundled relative scripts or support files named by either side must exist; external or project-local prerequisites are documented and checked at execution. Add both sides together, and update both when shared purpose, ownership, name, path, or lifecycle changes; an executable-only package edit need not churn the catalogue. To retire a Skill, remove the installed package from `.agents/skills/` and archive or remove its catalogue note and active routes; an archived note must not leave a dormant package discoverable by the runtime. Git provides rollback. Allow a one-sided runtime-only exception only when it is explicit and documented.

When updating a vault-owned skill, edit the actual package, not only its visible note. Follow [[procedures/configure-agent-skill-discovery|Configure Agent Skill Discovery]] to expose retained packages to supported runtimes. If a machine-local runtime exposes the skill through a symlink, verify that it still targets the vault package; do not maintain a copied wrapper as another source of truth. In Procedure-backed mode the Procedure wins on conflict; standalone packages own their declared executable detail.
