---
type: Guide
related_to: "[[vault]]"
_organized: true
surface_for:
  - "[[vault]]"
---

# Second Brain Template Repository Guide

This repository is an empty Markdown Second Brain vault template.

It is intended to deploy a concrete vault, such as a work vault, private vault, research-project vault, or other scoped knowledge vault.

The template contains reusable note types, generic agent instructions, generic procedures, generic skill wrappers, saved views, and deployment instructions. It must not contain private memory, work memory, raw source dumps, or machine-specific paths.

## What This Is For

Use this template to create a portable Markdown knowledge vault with enough structure for humans and agents to maintain it safely.

It provides:

- a root Project note for the vault itself;
- generic Type notes;
- vault-level agent instructions;
- reusable procedures for capture, ingestion, project memory, linting, review, Git checkpoints, and optional control-vault consistency review;
- thin skill wrappers for recurring agent workflows;
- a per-vault automation documentation pattern;
- saved views for common retrieval surfaces;
- a generic external raw-file reference pattern for files that stay outside the vault;
- optional local retrieval-index guidance for deployments that need fuzzy recall over larger Markdown corpora.

## What This Is Not For

This repository is not a living memory vault. Do not add private context, current project notes, generated dumps, attachments, credentials, or machine-local paths to the template.

It is also not a replacement for a reference manager, task manager, document store, or chat archive. Link to those systems when useful, but keep the Markdown graph as the durable synthesis layer.

## How To Deploy

Follow [[deploy-vault-from-template]]. The short version is:

1. Create a new repository from this template.
2. Clone it into the destination folder for the new vault.
3. Rename and customize [[vault]].
4. Configure global or local agent instructions from [[global-agent-instructions-template]], including a stable logical vault role such as `personal`, `work/control`, `research`, or `team`.
5. Decide whether this deployed vault is an ordinary vault or the main/control brain for a multi-vault setup, and make sure generated project-local `AGENTS.md` pointers use the chosen logical vault role rather than a local path. Add project-local `CLAUDE.md` shims for Claude Code workspaces.
6. Review the generic skills and saved views.
7. Commit and push the customized starting point.

If the deployed vault will point to raw files outside the vault, create the ignored local root resolver at `.local/roots.yml`. The committed vault should store durable file pointers as `root_key` plus `relative_path` in Source notes; `.local/roots.yml` maps those root keys to machine-specific folders.

Generic resolver example:

```yaml
roots:
  documents_basedir:
    access: guarded-write
    candidates:
      - "~/Documents"
```

Do not commit `.local/roots.yml`. Commit the Source notes, procedures, and views that describe how the external raw files are referenced.

## Retrieval

The default retrieval system is portable Markdown plus direct search: Project notes, Type notes, saved views, frontmatter relationships, wikilinks, source notes, `rg`, and inspected file content. Markdown files, frontmatter, wikilinks, saved views, and Git remain authoritative.

Agents should classify the task before searching, start from the smallest high-signal surface, and inspect the underlying Markdown and relationships before making claims or edits. Broad `rg` searches and file lists are scouting layers, not evidence.

If a deployed vault later chooses a local retrieval index, document the benchmarked need, privacy boundary, index scope, machine-local storage, refresh cadence, fallback behavior, and maintenance owner. Treat the index as a disposable cache, not as committed vault state or source of truth.

Do not restructure a Tolaria vault just to satisfy a local retrieval index. Type and relationships live in frontmatter and wikilinks. Do not enable graph-memory services, MCP servers, or background index daemons by default in the template.

## Template Residue In Deployed Vaults

After deployment, a concrete vault should mostly contain implemented guidance, not reusable template copies.

Keep template-only files active in this repository. In an ordinary deployed vault, delete or archive template-only notes once they have served deployment. For example, `global-agent-instructions-template.md` should normally stay in this template repository; a multi-vault setup should instead use the work/control vault's global-instruction source and the deployed vault's own `AGENTS.md`.

Archived deployment provenance is fine when it is explicitly marked `_archived: true` and not treated as an active workflow.

## Control-Vault Workflow

The template includes [[procedures/review-multi-vault-consistency|Review Multi-Vault Consistency]] and its skill package so a main/control brain can audit routing, deployed vaults, template drift, and local automations.

Do not activate that workflow in ordinary personal, research, project, or team vaults by default. For those vaults, keep it out of the root Project's active workflows and do not schedule an automation for it. Activate it only in the vault explicitly designated as the main/control brain for multi-vault routing and template coordination.

## Core Conventions

- One note per Markdown file.
- The first H1 is the preferred display title.
- Note type is stored in `type:` frontmatter.
- Use `belongs_to`, `related_to`, and `has` for canonical relationships.
- Use `_archived: true` for archived notes.
- Canonical type names stay in English across vaults. A localized vault can display translated labels through Type-note metadata such as `_sidebar_label` without changing filenames, H1s, or `type:` values.
- Source notes preserve external provenance; synthesis belongs in Project, Topic, Concept, Question, Procedure, ADR, and Note files.
- External raw-file Source notes use portable `root_key` plus `relative_path` pointers, resolved through ignored local config such as `.local/roots.yml`.
- Saved views live in `views/*.yml`.

## Daily Use

Capture quickly, organize later. Put ambiguous material in unprocessed notes or [[ready-to-ingest]] until there is a clear retrieval path.

Use Projects as work entry points. Project notes are the live human and agent home for a project: keep Outcome, Current State, Scope and Boundaries, Active Workflows when applicable, Next Actions, Open Questions, Important Notes, and Maintenance Log predictable, while keeping detailed knowledge in linked notes.

Use the PORT action axes when choosing between action-like note types: `Responsibility` is recurring work larger than one sitting, `Project` is one-off work larger than one sitting, `Operation` is recurring work that can usually be completed in one sitting, and one-off `Task` notes should not be created by default. Keep one-off tasks in Project `## Next Actions` or a dedicated task manager unless the user explicitly chooses a task system.

Use Event notes for meetings, conversations, rollouts, incidents, milestones, decision events, achievements, external changes, or historical records that should remain findable later.

Active Projects normally have a small project surface in `views/`, unless the Project note explicitly says `Project view: false`. These views are not complete indexes. They should contain only the Project note plus a few current, human-meaningful notes such as a draft, plan, decision-driving Question, key source packet, or active review surface. A good default is 3-5 notes; more than 10 means the surface has probably become too noisy.

Use Source notes for external material that can be re-checked. Extract Concepts, Questions, Procedures, ADRs, or Project updates only when that improves future retrieval. Ingestion feedback is advisory and should not block safe processing, commit, or push.

For raw files that intentionally remain in an external folder, create a Source note instead of copying the file into the vault by default. Use fields such as:

```yaml
type: Source
source_type: "external file"
storage_system: External folder
root_key: documents_basedir
relative_path: "Example/important-file.pdf"
access: guarded-write
last_checked: 2026-05-11
```

`access: guarded-write` means agents treat the external location as read-only by default. They may list, check existence, and read explicitly relevant files, but they should write only when the user explicitly asks for a specific write action.

## Agent Skills

Included skill packages:

- `initialize-project-memory`
- `ingest-source`
- `process-inbox`
- `process-ready-ingestion-inbox`
- `update-project-summary`
- `update-project-next-actions`
- `check-external-raw-references`
- `lint-vault`
- `review-vault-health`
- `review-multi-vault-consistency` for a designated main/control vault only

Each skill is a thin activation wrapper under `.agents/skills/`. The portable workflow source of truth remains the matching note in `procedures/`. Visible catalogue entries live in `skills/`.

`maintain-project-human-view` is currently Procedure-only. Create a skill only if it becomes a frequent explicit command.

`review-multi-vault-consistency` is intentionally included in the template inventory but is not a common per-vault workflow. During deployment, leave it dormant in ordinary vaults unless the vault is explicitly promoted to the routing/control role.

## Compatibility Shims

Keep root compatibility shims such as `CLAUDE.md` when deploying the template. They are lightweight pointers for agent tools and Tolaria's compatibility checks; shared instructions still belong in `AGENTS.md`.

Project workspaces may keep scripts, prototypes, fixtures, generated outputs, and implementation-local notes beside the code. Durable project knowledge should live in the vault: design docs, workflow decisions, research notes, open questions, tool evaluations, and project state should become typed notes linked from the relevant Project or entry note instead of accumulating in a workspace `docs/` folder.

## Automations

Automations are per-vault and are not active in the template. Use [[vault-automations]] after deployment to document any local jobs that process inbox content, run lint, or review vault health.

Each automation should run with the deployed vault as its working directory and follow that vault's `AGENTS.md`, Procedure notes, Skill packages, privacy boundary, and Git checkpoint policy.

For write-capable Codex automations, do not rely on broad global full access. Document the exact Git command the automation is allowed to use, prefer a command-scoped persisted approval such as `git push origin main` for scheduled main-branch vault jobs, and record the stop conditions in the deployed vault's automation guide. Persisted push approval is not general permission to push from arbitrary Codex contexts.

Cross-vault consistency review is included as an optional control-vault workflow, not as a generic per-vault automation. It belongs only in a vault explicitly designated as the routing/control vault for a multi-vault setup.

## Git Checkpoints

Use [[procedures/git-checkpoint-vault-changes]] after agent-managed vault edits unless the user asks not to commit or push. Review the changed scope, exclude local junk and unrelated files, commit a coherent checkpoint, push, and report the final state.

## Status

This is a starter template. Customize the root note, scope, global instruction placeholders, and first Project or Responsibility before using it as a real vault.
