---
type: Guide
Related to: "[[vault]]"
_organized: true
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
- saved views for common retrieval surfaces.

## What This Is Not For

This repository is not a living memory vault. Do not add private context, current project notes, generated dumps, attachments, credentials, or machine-local paths to the template.

It is also not a replacement for a reference manager, task manager, document store, or chat archive. Link to those systems when useful, but keep the Markdown graph as the durable synthesis layer.

## How To Deploy

Follow [[deploy-vault-from-template]]. The short version is:

1. Create a new repository from this template.
2. Clone it into the destination folder for the new vault.
3. Rename and customize [[vault]].
4. Configure global or local agent instructions from [[global-agent-instructions-template]].
5. Decide whether this deployed vault is an ordinary vault or the main/control brain for a multi-vault setup.
6. Review the generic skills and saved views.
7. Commit and push the customized starting point.

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
- Use `Belongs to`, `Related to`, and `Has` for canonical relationships.
- Use `_archived: true` for archived notes.
- Source notes preserve external provenance; synthesis belongs in Project, Topic, Concept, Question, Procedure, ADR, and Note files.
- Saved views live in `views/*.yml`.

## Daily Use

Capture quickly, organize later. Put ambiguous material in unprocessed notes or [[ready-to-ingest]] until there is a clear retrieval path.

Use Projects as work entry points. Project notes should summarize purpose, context, active workflows, next actions, open questions, and important linked notes.

Use Source notes for external material that can be re-checked. Extract Concepts, Questions, Procedures, ADRs, or Project updates only when that improves future retrieval. Ingestion feedback is advisory and should not block safe processing, commit, or push.

## Agent Skills

Included skill packages:

- `initialize-project-memory`
- `ingest-source`
- `process-inbox`
- `process-ready-ingestion-inbox`
- `update-project-summary`
- `update-project-next-actions`
- `lint-vault`
- `review-vault-health`
- `review-multi-vault-consistency` for a designated main/control vault only

Each skill is a thin activation wrapper under `.agents/skills/`. The portable workflow source of truth remains the matching note in `procedures/`. Visible catalogue entries live in `skills/`.

`review-multi-vault-consistency` is intentionally included in the template inventory but is not a common per-vault workflow. During deployment, leave it dormant in ordinary vaults unless the vault is explicitly promoted to the routing/control role.

## Compatibility Shims

Keep root compatibility shims such as `CLAUDE.md` when deploying the template. They are lightweight pointers for agent tools and Tolaria's compatibility checks; shared instructions still belong in `AGENTS.md`.

## Automations

Automations are per-vault and are not active in the template. Use [[vault-automations]] after deployment to document any local jobs that process inbox content, run lint, or review vault health.

Each automation should run with the deployed vault as its working directory and follow that vault's `AGENTS.md`, Procedure notes, Skill packages, privacy boundary, and Git checkpoint policy.

Cross-vault consistency review is included as an optional control-vault workflow, not as a generic per-vault automation. It belongs only in a vault explicitly designated as the routing/control vault for a multi-vault setup.

## Git Checkpoints

Use [[procedures/git-checkpoint-vault-changes]] after agent-managed vault edits unless the user asks not to commit or push. Review the changed scope, exclude local junk and unrelated files, commit a coherent checkpoint, push, and report the final state.

## Status

This is a starter template. Customize the root note, scope, global instruction placeholders, and first Project or Responsibility before using it as a real vault.
