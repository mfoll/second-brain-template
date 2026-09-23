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
- [`scripts/configure-agent-skills.sh`](scripts/configure-agent-skills.sh) as the machine-local Codex, Claude Code, or explicit Agent Skills discovery bridge;
- [`views/`](views) as starter Tolaria work surfaces;
- [[tolaria-saved-views]] as the on-demand saved-view syntax reference;
- [[tolaria-callouts]] as the portable callout syntax and restraint reference;
- [[vault-automations]] as a per-vault automation documentation pattern;
- portable external-file pointers using `root_key` plus `relative_path`.

The template also contains [[procedures/review-multi-vault-consistency|Review Multi-Vault Consistency]] for deployments explicitly designated as routing/control vaults. Ordinary personal, research, project, or team deployments remove its installed Skill package and active routes; they may retain only the Procedure as clearly archived provenance.

## Deploy or upgrade

For a new repository, follow [[deploy-vault-from-template]]. For an existing deployed vault, follow [[upgrade-existing-vault-from-template]] and port reviewed interfaces selectively; never overlay or merge the template wholesale.

New deployment, in outline:

1. Verify the reviewed template commit is the exact GitHub default-branch tip, then create and clone the destination repository and compare its tree hash.
2. Rename and customize [[vault]], `AGENTS.md`, this README, and the automation guide for the deployed scope and privacy boundary.
3. Configure a stable logical vault role through each selected runtime's machine-local global instructions. Project pointers use that role, not an embedded local vault path.
4. Choose the external-project-file strategy and `attachments/` policy. Configure ignored `.local/roots.yml` mappings and Source bridges when durable files stay outside Git.
5. Review Types, Procedures, skills, views, and optional workflows; remove what the deployed vault does not need.
6. Follow [[procedures/configure-agent-skill-discovery|Configure Agent Skill Discovery]] for each runtime that should discover the retained Skill packages.
7. Delete or archive template-only residue such as active bootstrap templates in ordinary deployed vaults.
8. Run external-reference, mechanical, semantic, retrieval, and rollback validation, then review the customized diff and checkpoint it under the user's current Git authorization policy.

## Agent runtime setup

Agent compatibility has two independent layers. Configure both for every runtime that should use the deployed vault:

| Layer | Canonical source | Runtime adapter |
| --- | --- | --- |
| Always-loaded instructions and vault routing | Vault and workspace `AGENTS.md` files | The runtime's machine-global and project instruction surfaces |
| On-demand workflows | Retained `.agents/skills/<skill-name>/` packages | Symlinks in the runtime's documented Agent Skills directory |

For a standalone Codex deployment, merge [[global-agent-instructions-template]] into `${CODEX_HOME:-$HOME/.codex}/AGENTS.md`. Codex uses the vault and project `AGENTS.md` hierarchy directly. After removing unneeded Skill packages, install and verify the retained set:

```bash
./scripts/configure-agent-skills.sh --runtime codex
./scripts/configure-agent-skills.sh --runtime codex --check
```

For a standalone Claude Code deployment, merge the same global block into `${CLAUDE_CONFIG_DIR:-$HOME/.claude}/CLAUDE.md`. Keep this repository's root `CLAUDE.md`. Project pointers need no shim because Claude Code reads `AGENTS.md` directly; add a `CLAUDE.md` containing `@AGENTS.md` only where that direct loading is unavailable. Then install and verify the retained Skill set:

```bash
./scripts/configure-agent-skills.sh --runtime claude
./scripts/configure-agent-skills.sh --runtime claude --check
```

For another agent, first confirm its documented user/project instruction files and Agent Skills discovery directory. Keep `AGENTS.md` authoritative, add the smallest supported instruction adapter, and pass the documented skills directory explicitly:

```bash
./scripts/configure-agent-skills.sh --target <RUNTIME_SKILLS_DIRECTORY>
./scripts/configure-agent-skills.sh --target <RUNTIME_SKILLS_DIRECTORY> --check
```

Do not guess a path merely because an agent understands `SKILL.md`. If it has no compatible discovery mechanism, agents can still follow the Procedures routed from `AGENTS.md`, but automatic Skill activation is unavailable.

The installer links every package still present under `.agents/skills/`; prune the deployment first. It preflights the complete target, never overwrites a same-name entry, and makes no changes when a conflict exists. Runtime links are machine-local and are not committed. In a controlled multi-vault setup, use the existing configuration source and installer instead of creating a competing global instruction file or second set of links.

See [[procedures/configure-global-agent-instructions|Configure Global Agent Instructions]] and [[procedures/configure-agent-skill-discovery|Configure Agent Skill Discovery]] for ownership choices, validation, collision handling, and deployment-ledger requirements.

## Core model

Markdown, YAML frontmatter, wikilinks, saved views, and Git are authoritative. Tolaria is a viewer, not the storage layer. Agents should retrieve progressively from the smallest high-signal entry note and inspect underlying files before making claims or edits.

Project notes are compact resumption surfaces: normally 600–1,200 words, with concise current state, 3–7 actions, prioritized Questions and Important Notes, and only 3–5 milestones. Detailed evidence and reusable knowledge live in linked Sources, Events, Concepts, Opinions, Questions, Procedures, or ADRs. Long evidence/reference notes keep their payload but start with a short summary.

Canonical relationship fields are `belongs_to`, `related_to`, `has`, and `surface_for`. Canonical Type identities remain in English; deployed vaults may use Type display metadata such as `_sidebar_label` for localization.

## Normal use after deployment

Optional extension: [[recap|Recap]] provides curated daily, monthly, and yearly conversational memory through [[procedures/prepare-recording-recaps]]. It is disabled until explicitly configured and is not required for the core vault. Deployments may omit the Type, Procedure, preference guide, and their links together. No recorder or scheduled job is bundled or enabled by these notes.

- Capture ambiguous material in unprocessed notes or [[ready-to-ingest]].
- Ingest external material through [[procedures/ingest-source|Ingest Source]] with visible provenance.
- Resume work from Project or Responsibility entry notes, not broad searches.
- Refresh project synthesis with [[procedures/update-project-summary|Update Project Summary]] and [[procedures/update-project-next-actions|Update Project Next Actions]] instead of appending chronology.
- Keep Project views small when used with [[procedures/maintain-project-human-view|Maintain Project Human View]].
- Create or repair saved-view YAML through [[tolaria-saved-views|Tolaria Saved Views]].
- Use [[tolaria-callouts|Tolaria Callouts]] only for compact, semantically useful opening prose blocks.
- Diagnose mechanics with [[procedures/lint-vault|Lint Vault]] and strategy with [[procedures/review-vault-health|Review Vault Health]].

Brain Projects do not require matching folders or agent-application projects. [[procedures/route-project-work-and-artifacts|Route Project Work And Artifacts]] defines the promotion gate and cloud `Working/` fallback. Inside a justified technical workspace, `AGENTS.md` is a pointer, not a handbook; [[procedures/initialize-project-memory|Initialize Project Memory]] keeps it near 80 words and adds a minimal Claude shim when needed.

The canonical Skill packages remain under `.agents/skills/`. After deployment and pruning, [[procedures/configure-agent-skill-discovery|Configure Agent Skill Discovery]] links those packages into Codex, Claude Code, or another runtime's documented Agent Skills directory. Runtime links are machine-local adapters, not copied workflow sources.

## External project files

Do not copy maintained external folders into the vault by default. A deployment chooses one default strategy:

- `convention-based`: derive each project folder from a configured external root and project slug;
- `linked-per-project`: confirm and link a distinct external folder for each project;
- `workspace-only`: allow no durable non-versioned outputs unless a project explicitly adds an external location.

Use a `Source` note for maintained inputs, outputs, or deliverables with fields such as:

```yaml
type: Source
storage_system: External folder
root_key: documents_basedir
relative_path: "Example/important-file.pdf"
access: guarded-write
last_checked: YYYY-MM-DD
```

Machine-specific candidates belong in ignored `.local/roots.yml`. `guarded-write` means read-only by default; writing requires explicit authorization for the specific external action.

A deployed vault may disable `attachments/` or reserve it for small Git-tracked vault assets. It must not become a generic store for durable unversioned outputs. Configure `Working/<project-or-context-slug>/` under the chosen cloud root for retained work before a dedicated external folder is justified. Use an ignored workspace `.tmp/` only for reproducible or disposable intermediates and `/tmp/` for truly disposable files.

## Skills and automations

Procedures contain full reusable workflows. Their Skill packages require the complete Procedure, which is authoritative on conflict, and may retain operational detail; prefer thinness only after a clause audit shows that no trigger, prerequisite, hard guard, command, or bundled-resource instruction will be lost. A genuinely specialized Skill may instead own its executable detail when no durable Procedure does; its catalogue note must make that ownership explicit. Do not create one skill per Procedure unless repeated use shows that discovery is the actual problem.

The template creates no active automations. A deployed vault documents its jobs in [[vault-automations]], uses its own working directory and privacy policy, keeps read-only jobs read-only, and gives write-capable jobs narrow authorization. Cross-vault review remains exclusive to a designated routing/control vault.

## Git and safety

Git is the audit and rollback layer. Follow [[procedures/git-checkpoint-vault-changes|Git Checkpoint Vault Changes]]: preserve unrelated edits, stage only authorized files, separate local commit from network push authorization, and never force-push without explicit approval.

## Status

This is a starter template. A useful deployment replaces placeholders and acquires real scope; the template itself remains neutral and content-free.
