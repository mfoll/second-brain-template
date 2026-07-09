---
type: Guide
_organized: true
surface_for:
  - "[[vault]]"
---

# AGENTS.md — Second Brain Vault Template

This repository is a neutral deployable Markdown Second Brain template. Markdown files, YAML frontmatter, wikilinks, saved views, and Git history are the durable source of truth. Customize this file during deployment for the vault's real scope, privacy boundary, and evidence needs.

Keep changes small, portable, and easy to review. Current user instructions override this guide.

## Instruction ownership

- Machine-local global instructions resolve logical vault roles to local roots and hold cross-context authorization rules.
- Project-local `AGENTS.md` files are short pointers: one logical vault role, one entry note (or explicit vault scope), and a missing-root guard.
- This file owns vault-wide invariants and routing.
- Root Type notes define note semantics. Procedures own detailed workflows. Skill packages are thin activation wrappers.

Do not duplicate policy across layers or let workspace `docs/` become a parallel memory store. Keep implementation-local, generated, or transient documentation beside project artifacts; promote durable context, decisions, questions, and state into typed vault notes.

## Retrieval

Start from the narrowest durable surface:

1. For project work, read the workspace pointer, its entry note, the project view, and only task-relevant linked notes.
2. For exact lookup, use known paths, frontmatter, wikilinks, saved views, and direct file search.
3. For fuzzy recall, start from likely Projects, Responsibilities, Topics, Sources, Opinions, Questions, Concepts, recent Events, and Inbox surfaces before widening.

Read progressively: inspect frontmatter, H1, the opening summary, and headings first; then relevant sections. Read a full long note only when complete evidence or wording is required. Broad search output is scouting, not proof; inspect the underlying Markdown before making claims or edits.

Do not depend on machine-local retrieval indexes by default. Any optional index must be documented as a disposable cache with a benchmarked need, privacy scope, refresh path, and Markdown fallback.

## Note and graph contract

- One Markdown note per file; use kebab-case filenames.
- Durable notes need YAML frontmatter, a canonical English `type`, a first H1, and `_organized: true` once they have a retrieval path.
- Type definitions remain root notes. Inspect the relevant Type before creating or materially reshaping a note.
- Use lowercase relationships: `belongs_to` for parent context, `related_to` for lateral relevance, `has` for selective child or entry-point links, and `surface_for` only for small human project surfaces.
- Root wikilinks use filename stems; folder notes use vault-relative path stems.
- Use `_archived: true` for retained material removed from active use. Delete only when useful content and provenance have a better durable home.

Project notes are compact resumption surfaces, not archives. Follow [[project]]:

- 600–1,200 words by default; a complex umbrella may reach about 1,500.
- `Current State`: current truth only, normally no more than five bullets or 250 words.
- `Next Actions`: 3–7 outcome-level actions; review lists above 10.
- `Open Questions` and `Important Notes`: normally 3–7 prioritized links each.
- `Maintenance Log`: the latest 3–5 meaningful milestones; Git carries routine edit history.

Replace or reconcile old synthesis instead of appending another dated report. Keep each fact in one canonical durable note and link to it. Long Sources, Events, and Methods may preserve their payload, but should open with a 100–150-word summary above roughly 2,000 words. Review Questions above roughly 750 words for answers or analysis that belong in a maintained synthesis note.

## Writing and evidence

Read whenever prior vault context matters. Write only when the user asks to save, remember, ingest, process, organize, update, or maintain durable knowledge, except for direct high-confidence project writeback after significant work in a linked workspace.

Keep project writeback proportional: update the entry Project and directly affected notes, reconcile its summary, actions, and human view, and propose broad or uncertain cascades before applying them.

Sources preserve provenance in both frontmatter and readable body sections. External raw-file notes use portable `root_key` plus `relative_path`; `access: guarded-write` means read-only unless the user authorizes the specific external write.

During ingestion, answer resolvable question-shaped material first. Create a Question only when the unresolved issue is consequential, recurring, decision-driving, or a needed retrieval anchor. Treat Opinions as challengeable user context, not evidence.

## Workflow router

| Work | Source of truth |
| --- | --- |
| Create or normalize a note | Matching root Type note |
| Refresh project state or actions | [[procedures/update-project-summary|Update Project Summary]] and [[procedures/update-project-next-actions|Update Project Next Actions]] |
| Maintain a project workbench | [[procedures/maintain-project-human-view|Maintain Project Human View]] |
| Process Inbox or ingest a source | [[procedures/process-inbox|Process Inbox]] or [[procedures/ingest-source|Ingest Source]] |
| Verify external raw locations | [[procedures/check-external-raw-references|Check External Raw References]] |
| Diagnose structure or review strategy | [[procedures/lint-vault|Lint Vault]] or [[procedures/review-vault-health|Review Vault Health]] |
| Initialize a project pointer | [[procedures/initialize-project-memory|Initialize Project Memory]] |
| Checkpoint authorized edits | [[procedures/git-checkpoint-vault-changes|Git Checkpoint Vault Changes]] |

The template includes [[procedures/review-multi-vault-consistency|Review Multi-Vault Consistency]] only for deployments explicitly designated as routing/control vaults. Ordinary deployed vaults should omit or leave it dormant and must not schedule it.

## Template and deployment boundary

This repository is structure, not memory. Do not add private or work content, credentials, local paths, caches, or generated dumps. After deployment, replace placeholders, customize scope and privacy, and delete or archive template-only residue.

When a generic rule changes, update the template first, then deliberately port compatible changes to selected deployed-vault interface files. Preserve intentional local differences and do not inspect private content as part of propagation.

## Git and safety

Review status and diff, preserve unrelated user changes, and stage only task-scoped files. A local commit may accompany an authorized vault edit. Push requires explicit authorization through the user's current global or vault policy; a persisted approval never broadens task scope. Never force-push without explicit approval for that rewrite.

Read-only automations never stage, commit, or push. Write-capable automations operate only within their documented vault, scope, and command authorization.
