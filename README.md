---
type: Guide
related_to: "[[vault]]"
_organized: true
surface_for:
  - "[[vault]]"
---

# Second Brain Template Repository Guide

This repository is a neutral, empty Markdown Second Brain template. It provides portable note types, vault instructions, procedures, thin skill wrappers, saved views, and automation documentation without becoming a living memory store.

Do not add personal or work context, raw source dumps, credentials, attachments, local roots, caches, or generated agent state here.

## What it provides

- [[vault]] as the deployable root Project;
- root Type notes for the starter ontology;
- [`AGENTS.md`](AGENTS.md) as the generic vault contract;
- [`procedures/`](procedures) as portable workflow sources of truth;
- [`.agents/skills/`](.agents/skills) as thin activation wrappers;
- [`skills/`](skills) as visible Skill catalogue notes;
- [`views/`](views) as starter Tolaria work surfaces;
- [[tolaria-saved-views]] as the on-demand saved-view syntax reference;
- [[vault-automations]] as a per-vault automation documentation pattern;
- portable external-file pointers using `root_key` plus `relative_path`.

The template also contains [[procedures/review-multi-vault-consistency|Review Multi-Vault Consistency]] for deployments explicitly designated as routing/control vaults. Ordinary personal, research, project, or team deployments remove its installed Skill package and active routes; they may retain only the Procedure as clearly archived provenance.

## Deploy or upgrade

For a new repository, follow [[deploy-vault-from-template]]. For an existing deployed vault, follow [[upgrade-existing-vault-from-template]] and port reviewed interfaces selectively; never overlay or merge the template wholesale.

New deployment, in outline:

1. Verify the reviewed template commit is the exact GitHub default-branch tip, then create and clone the destination repository and compare its tree hash.
2. Rename and customize [[vault]], `AGENTS.md`, this README, and the automation guide for the deployed scope and privacy boundary.
3. Configure a stable logical vault role through the user's machine-local global instructions. Project pointers use that role, not an embedded local vault path.
4. Review Types, Procedures, skills, views, and optional workflows; remove what the deployed vault does not need.
5. Delete or archive template-only residue such as active bootstrap templates in ordinary deployed vaults.
6. If external files remain outside the vault, create ignored `.local/roots.yml` mappings and Source bridges, then run [[procedures/check-external-raw-references|Check External Raw References]].
7. Run mechanical, semantic, retrieval, and rollback validation, then review the customized diff and checkpoint it under the user's current Git authorization policy.

## Core model

Markdown, YAML frontmatter, wikilinks, saved views, and Git are authoritative. Tolaria is a viewer, not the storage layer. Agents should retrieve progressively from the smallest high-signal entry note and inspect underlying files before making claims or edits.

Project notes are compact resumption surfaces: normally 600–1,200 words, with concise current state, 3–7 actions, prioritized Questions and Important Notes, and only 3–5 milestones. Detailed evidence and reusable knowledge live in linked Sources, Events, Concepts, Opinions, Questions, Procedures, or ADRs. Long evidence/reference notes keep their payload but start with a short summary.

Canonical relationship fields are `belongs_to`, `related_to`, `has`, and `surface_for`. Canonical Type identities remain in English; deployed vaults may use Type display metadata such as `_sidebar_label` for localization.

## Normal use after deployment

- Capture ambiguous material in unprocessed notes or [[ready-to-ingest]].
- Ingest external material through [[procedures/ingest-source|Ingest Source]] with visible provenance.
- Resume work from Project or Responsibility entry notes, not broad searches.
- Refresh project synthesis with [[procedures/update-project-summary|Update Project Summary]] and [[procedures/update-project-next-actions|Update Project Next Actions]] instead of appending chronology.
- Keep active Project views small with [[procedures/maintain-project-human-view|Maintain Project Human View]].
- Create or repair saved-view YAML through [[tolaria-saved-views|Tolaria Saved Views]].
- Diagnose mechanics with [[procedures/lint-vault|Lint Vault]] and strategy with [[procedures/review-vault-health|Review Vault Health]].

Workspace-local `AGENTS.md` files are pointers, not handbooks. [[procedures/initialize-project-memory|Initialize Project Memory]] keeps them near 80 words, targets one entry note or explicit vault scope, and adds a minimal Claude shim when needed. Durable project knowledge stays in the vault; workspace documentation remains implementation-local, generated, or transient.

## External raw files

Do not copy maintained external folders into the vault by default. Use a `Source` note with fields such as:

```yaml
type: Source
storage_system: External folder
root_key: documents_basedir
relative_path: "Example/important-file.pdf"
access: guarded-write
last_checked: YYYY-MM-DD
```

Machine-specific candidates belong in ignored `.local/roots.yml`. `guarded-write` means read-only by default; writing requires explicit authorization for the specific external action.

## Skills and automations

Procedures contain full reusable workflows. Their Skill packages require the complete Procedure, which is authoritative on conflict, and may retain operational detail; prefer thinness only after a clause audit shows that no trigger, prerequisite, hard guard, command, or bundled-resource instruction will be lost. A genuinely specialized Skill may instead own its executable detail when no durable Procedure does; its catalogue note must make that ownership explicit. Do not create one skill per Procedure unless repeated use shows that discovery is the actual problem.

The template creates no active automations. A deployed vault documents its jobs in [[vault-automations]], uses its own working directory and privacy policy, keeps read-only jobs read-only, and gives write-capable jobs narrow authorization. Cross-vault review remains exclusive to a designated routing/control vault.

## Git and safety

Git is the audit and rollback layer. Follow [[procedures/git-checkpoint-vault-changes|Git Checkpoint Vault Changes]]: preserve unrelated edits, stage only authorized files, separate local commit from network push authorization, and never force-push without explicit approval.

## Status

This is a starter template. A useful deployment replaces placeholders and acquires real scope; the template itself remains neutral and content-free.
