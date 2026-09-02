---
type: Guide
_organized: true
surface_for:
  - "[[vault]]"
---

# AGENTS.md — Second Brain Vault Template

This repository is a neutral Second Brain template. Markdown, YAML frontmatter, wikilinks, saved views, and Git are authoritative. Customize this file during deployment for the vault's scope, privacy boundary, and evidence needs.

Keep changes small, portable, and reviewable. Current user instructions override this guide.

## Instruction ownership

- Machine-local global instructions resolve logical vault roles to local roots and hold cross-context authorization rules.
- Project-local `AGENTS.md` files are short pointers only inside substantive technical workspaces; never create a folder merely to host one. Each pointer names one logical vault role, one entry note (or explicit vault scope), and a missing-root guard.
- This file owns vault-wide invariants and routing.
- Root Type notes define note semantics. Procedures own reusable workflows. Skills activate a Procedure or, when explicitly specialized, own executable detail as defined by [[skill]].

Do not duplicate policy across layers or let workspace `docs/` become a parallel memory store. A Brain Project does not require a matching folder or agent-application project. Follow [[procedures/route-project-work-and-artifacts|Route Project Work And Artifacts]] before creating either. Keep implementation-local, reproducible, and transient material beside substantive project artifacts; promote durable context, decisions, questions, and state into typed vault notes. Route durable non-versioned files through the deployed external-file strategy and Source notes.

For delegated tasks routed through the vault, use the existing primary checkout directly by default. Use an isolated Git worktree only for bounded concurrent changes or an intentionally isolated review branch, and state the isolation, integration, and cleanup plan before creating it.

## Retrieval

Start from the narrowest durable surface:

1. For project work, read the workspace pointer, its entry note, the project view when present, and only task-relevant linked or vault-routed notes.
2. For exact lookup, use known paths, frontmatter, wikilinks, saved views, and direct file search.
3. For fuzzy recall, start from likely Projects, Responsibilities, Topics, Sources, Opinions, Questions, Concepts, recent Events, and Inbox surfaces before widening.

If the user refers to a project file, folder, dataset, manuscript, external document, output, deliverable, or path-like reference from a project workspace, first check the entry note and linked Source notes for external project locations or `root_key` plus `relative_path` pointers before guessing paths or searching broadly.

Read progressively: inspect frontmatter, H1, the opening summary, and headings first; then relevant sections. Read a full long note only when complete evidence or wording is required. Broad search output is scouting, not proof; inspect the underlying Markdown before making claims or edits.

Orient candidates by path, H1, `type`, lifecycle state, task role, `belongs_to`, `has`, `related_to`, `surface_for`, and body links. Follow only links that answer a retrieval question.

Do not depend on machine-local retrieval indexes by default. Any optional index must be documented as a disposable cache with a benchmarked need, privacy scope, refresh path, and Markdown fallback.

## Note and graph contract

- One Markdown note per file; use kebab-case filenames.
- Durable notes need YAML frontmatter, a canonical English `type`, a first H1, and `_organized: true` once they have a retrieval path. The first H1 is the display title; do not add `title:`.
- Type definitions remain root notes. When a note Type affects selection, interpretation, lifecycle, structure, or an edit, inspect the matching root Type note before relying on its semantics.
- Use lowercase relationships: `belongs_to` for parent context, `related_to` for lateral relevance, `has` for selective child or entry-point links, and `surface_for` only for small human project surfaces. Quote scalar wikilinks, use YAML lists for multiple values, and preserve valid custom relationship keys unless explicitly normalizing.
- Root wikilinks use filename stems; folder notes use vault-relative path stems.
- Frontmatter keys beginning with `_` are normally viewer-managed; change them only when requested or required by a Type or Procedure. Disable `attachments/` or reserve it for small Git-tracked vault assets, never durable unversioned outputs.
- Tolaria callouts are selective presentation aids inside note sections. Follow [[tolaria-callouts]] for the verified portable form and semantic use; do not use them instead of headings, typed notes, frontmatter, durable Questions, or Project Next Actions.
- Use `_archived: true` for retained inactive material and exclude it from active views. Do not default to an `archive/` folder or `status: Archived`. Delete only when useful content and provenance have a better durable home.

Before creating a view, Type, Procedure, or other repeated vault artifact, inspect nearby examples and follow the current dominant convention. If written guidance and existing practice diverge, reconcile them before adding another variant.

Project notes are compact resumption surfaces, not archives. Follow [[project]]; reconcile rather than append synthesis, keep facts in canonical typed notes, and use links or Git for detail and routine history.

## Writing and evidence

Read whenever prior vault context matters. Write only when the user asks to save, remember, ingest, process, organize, update, or maintain durable knowledge, except for direct high-confidence project writeback after significant work in a linked workspace.

Keep project writeback proportional: update the entry Project and directly affected notes, reconcile its summary, actions, and any useful existing human view, and propose broad or uncertain cascades before applying them.

Sources preserve provenance in both frontmatter and readable body sections. External project-file notes use portable `root_key` plus `relative_path`; `access: guarded-write` means read-only unless the user authorizes the specific external write.

Retrieve relevant Opinion notes whenever the user's stance materially affects drafting, planning, review, briefing, maintenance, or ingestion. Treat Opinions as challengeable context, not evidence. During ingestion, answer resolvable question-shaped material first and create a Question only when the unresolved issue is consequential, recurring, decision-driving, or a needed retrieval anchor.

## Workflow router

When a task matches an existing Procedure, read and follow it before acting. Use the common router below and search `procedures/` when the workflow is not listed.

| Work | Source of truth |
| --- | --- |
| Create or normalize a note | Matching root Type note |
| Create or edit a saved view | [[tolaria-saved-views|Tolaria Saved Views]]; for a Project surface, also [[procedures/maintain-project-human-view|Maintain Project Human View]] |
| Move or rename notes | Update affected links in the same change and run [[procedures/lint-vault|Lint Vault]] before and after |
| Deploy or upgrade a vault | [[deploy-vault-from-template|Deploy Vault From Template]] or [[upgrade-existing-vault-from-template|Upgrade an Existing Vault From the Template]] |
| Refresh project state or actions | [[procedures/update-project-summary|Update Project Summary]] and [[procedures/update-project-next-actions|Update Project Next Actions]] |
| Maintain a project workbench | [[procedures/maintain-project-human-view|Maintain Project Human View]] |
| Process Inbox or ingest a source | [[procedures/process-inbox|Process Inbox]] or [[procedures/ingest-source|Ingest Source]] |
| Verify external raw locations | [[procedures/check-external-raw-references|Check External Raw References]] |
| Diagnose structure or review strategy | [[procedures/lint-vault|Lint Vault]] or [[procedures/review-vault-health|Review Vault Health]] |
| Initialize a project pointer | [[procedures/initialize-project-memory|Initialize Project Memory]] |
| Decide whether work needs a folder, repository, agent project, or cloud Working area | [[procedures/route-project-work-and-artifacts|Route Project Work And Artifacts]] |
| Expose retained Skills to an agent runtime | [[procedures/configure-agent-skill-discovery|Configure Agent Skill Discovery]] |
| Checkpoint authorized edits | [[procedures/git-checkpoint-vault-changes|Git Checkpoint Vault Changes]] |

The template includes [[procedures/review-multi-vault-consistency|Review Multi-Vault Consistency]] only for routing/control vaults. Ordinary deployments remove its installed Skill package and active routes and must not schedule it.

## Template and deployment boundary

This repository is structure, not memory. Do not add private or work content, credentials, local paths, caches, or generated dumps. After deployment, replace placeholders, customize scope and privacy, choose an external-project-file strategy and `attachments/` policy, and delete or archive template-only residue.

When a generic rule changes, update the template first, then deliberately port compatible changes to selected deployed-vault interface files. Preserve intentional local differences and do not inspect private content as part of propagation.

## Git and safety

Review status and diff, preserve unrelated user changes, and stage only task-scoped files. A local commit may accompany an authorized vault edit. Push requires explicit authorization through the user's current global or vault policy; a persisted approval never broadens task scope. Never force-push without explicit approval for that rewrite.

Do not silently rewrite an accepted ADR. When a durable decision changes, create a superseding ADR and link the old and new decisions.

Read-only automations never stage, commit, or push. Write-capable automations operate only within their documented vault, scope, and command authorization.
