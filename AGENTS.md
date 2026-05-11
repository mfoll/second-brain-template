---
type: Guide
_organized: true
---

# AGENTS.md - Second Brain Vault Template

This is a vault-level instruction file for a portable Markdown Second Brain vault. The Markdown files, YAML frontmatter, wikilinks, procedures, ADRs, views, skills, and Git history are the durable source of truth.

## Vault Purpose

Use this vault as a scoped memory layer for humans and agents. It should store durable context, sources, synthesis, decisions, procedures, and project state that must survive beyond a single chat or tool session.

The root Project note is [[vault]]. Start there, then follow linked procedures, ADRs, views, and project notes.

This repository is the generic source for deployable vault conventions. When changing a generic procedure, skill, vault convention, automation pattern, or `AGENTS.md` behavior here, proactively check whether currently deployed vaults should receive the compatible change too. Port only generic, safe changes; deployed-vault-specific privacy, scope, and content rules remain local.

The template includes [[procedures/review-multi-vault-consistency|Review Multi-Vault Consistency]] and its skill package for deployments that become the main/control brain of a multi-vault setup. Do not activate, schedule, or use that workflow in ordinary deployed vaults by default; it should remain dormant unless the vault is explicitly responsible for routing, template coordination, and cross-vault interface review.

After deployment, ordinary vaults should not keep reusable template notes active. Convert template guidance into implemented local `AGENTS.md`, `README.md`, root Project, automation guide, and procedure content. Delete template-only notes that no longer serve the deployed vault, or mark provenance-only deployment notes with `_archived: true`.

## Instruction Layers

Second Brain guidance is split across three layers:

- Global agent instructions identify the configured vault root on a specific machine.
- Project-local `AGENTS.md` files are scope pointers that name the primary Project note for a workspace.
- Project workspace documentation should not become a parallel memory store. Durable design docs, research notes, workflow decisions, open questions, tool evaluations, and project state belong in the vault as typed notes linked from the primary entry note. Keep workspace `docs/` material only when it is implementation-local, generated, or explicitly transient; otherwise promote it into the vault and leave scripts, prototypes, fixtures, and temporary outputs in the workspace.
- This vault-level `AGENTS.md` is the portable source of truth for vault conventions and safety rules.

If an external workspace expects Second Brain memory but the configured vault root is unknown or unreadable, stop and ask the user to configure the global Second Brain instructions with the correct path. Do not guess a path or create a new vault.

## Core Conventions

- One Markdown note per file.
- The first H1 in the body is the preferred display title.
- Store note type in the `type:` frontmatter field.
- Agent-created or agent-routed notes should include `_organized: true` once they have a clear retrieval path. Keep `_organized: false` only for deliberately unprocessed captures such as [[ready-to-ingest]].
- Type definitions live at the vault root unless the user reorganizes the vault intentionally.
- Saved views live in `views/*.yml`.
- Files in `attachments/` are assets, not notes or types.
- Frontmatter properties that start with `_` are usually app-managed state. Leave them alone unless the user asks to change them.

## Types

Types are Markdown notes with `type: Type`. Keep type notes generic and portable. Common starter types include Project, Responsibility, Topic, Source, Concept, Question, Procedure, ADR, Guide, Note, and Skill.

Type notes are structural notes and should normally be `_organized: true`, unless a new Type is still a draft.

Do not add a new Type until there is a recurring retrieval need that existing types do not cover cleanly.

## Relationships

Any frontmatter property whose value contains wikilinks may act as a relationship.

Canonical relationship fields:

- `Belongs to`: parent, container, workspace, responsibility, larger project, or durable context.
- `Related to`: lateral conceptual relevance.
- `Has`: selected child note, active workflow, open question, ADR, procedure, skill, deliverable, or structural entry point.

For new and normalized notes, use `Belongs to`, `Related to`, and `Has`. Do not create new notes with legacy lowercase keys such as `belongs_to` or `related_to`.

Use quoted wikilinks for scalar frontmatter values and YAML lists for multiple relationships.

For Project notes, `Has` should be selective rather than exhaustive. Use body sections, backlinks, views, and `Belongs to` relationships for long lists.

Before removing a Project `Has` link, make sure the target note still has a retrieval path through its own relationships, a Project body link, another hub note, a saved view, or an explicit inbox/archive convention.

Project notes are the live human and agent entry points for projects. Follow the structure in [[project]] when creating or refreshing them: keep `## Outcome`, `## Current State`, `## Scope and Boundaries`, `## Next Actions`, `## Open Questions`, `## Important Notes`, and `## Maintenance Log` predictable, while allowing project-specific middle sections such as `Working Thesis`, `Current Principles`, `Candidate Tools`, or `Draft Artifacts`. Do not flatten rich project knowledge just to fit the template; move detailed material into linked typed notes only when that improves retrieval.

## Wikilinks

- Root notes may use filename-stem links such as `[[vault]]`.
- Notes in folders must use vault-relative path-stem links such as `[[procedures/lint-vault|Lint Vault]]` or `[[skills/lint-vault-skill|lint-vault skill]]`.
- Repository guides should be linked as `[[README]]`, not by reusing the root Project alias.
- Compatibility shims should be linked explicitly as `[[CLAUDE]]` or `[[GEMINI]]` only when discussing the shim itself.
- Use pipe display text when a nicer label helps, such as `[[procedures/ingest-source|Ingest Source]]`.
- Do not rely on H1/title matching when a filename-stem or path-stem target exists.
- Hidden skill packages under `.agents/skills/` are implementation files, not normal durable note targets. Link visible Skill catalogue notes in `skills/` when the skill itself is the graph target.
- Avoid giving a Guide, README, compatibility shim, visible Skill note, or package `SKILL.md` the same H1 as a Project, Procedure, or root note. Use disambiguating titles such as "Repository Guide", "Compatibility Shim", or "Skill Package" where needed.
- When renaming or moving notes outside a vault UI, update affected wikilinks in the same change or run [[procedures/lint-vault|Lint Vault]].

## Archived Notes

Use `_archived: true` as a lightweight lifecycle flag for notes that should be retained but excluded from normal active resumption.

Do not create an `archive/` folder by default. Do not use `status: Archived` as the default archive mechanism. `status` should keep type-specific meanings such as `Open`, `Answered`, `Active`, `Processed`, `Accepted`, or `Superseded`.

## Views

Saved views live in `views/*.yml` and are written as YAML. The filename is the stable view id.

A view must have one root filter group: `all:` or `any:`. Conditions use `field`, `op`, and usually `value`. Relationship filters should use canonical fields such as `Belongs to`, `Related to`, and `Has`.

Do not create legacy JSON view files.

## Filenames

Use kebab-case filenames. Keep one note per file.

## Portability

Keep durable vault content portable across machines, agents, and Markdown viewers. Prefer placeholders, configured-root language, vault-relative paths, and generic examples over machine-specific paths.

Do not add local machine paths, cache paths, app metadata, secrets, credentials, or temporary directories to durable template content.

Define the vault in agent-neutral terms. Mention specific products only for concrete compatibility notes, examples, or setup instructions.

## External Raw-File References

Use the vault to remember external raw-file locations, not to duplicate external folders by default.

For important files or folders that remain outside the vault, create or update a `type: Source` note with portable location fields:

```yaml
source_type: "external file"
storage_system: External folder
root_key: documents_basedir
relative_path: "Example/important-file.pdf"
access: guarded-write
last_checked: 2026-05-11
```

The durable note should store `root_key` plus `relative_path`, not a resolved absolute local path. Machine-specific roots belong in ignored local configuration such as `.local/roots.yml`, environment variables, global/custom agent instructions, or a machine-scoped setup note.

`access: guarded-write` means agents should treat the external location as read-only by default. Listing, existence checks, metadata checks, and explicitly relevant reads are allowed. Writing, renaming, moving, deleting, cleanup, bulk sync, or saving generated files into an external folder is allowed only when the user explicitly asks for that specific write action.

Prefer shallow folder indexes and selected file-level Source notes over deep inventories. Use [[procedures/check-external-raw-references|Check External Raw References]] to verify important pointers and detect drift.

A specific external file that should be maintained over time gets its own Source note. Project notes link to the Source note under External Raw Locations, Sources, or Important Notes; `last_checked` belongs on the Source note, not on the project note or incidental prose reference.

## Default Agent Behavior

- Read relevant notes before answering when prior vault context matters.
- Write to the vault only when explicitly asked to save, remember, ingest, process, organize, update, maintain, or contribute knowledge.
- For source ingestion, document review, writing, planning, briefing, interview, and agentic maintenance work, retrieve relevant `Opinion` notes when the topic, project, source, or user request makes them likely to matter. Use Opinions as the user's working stances, not as dogma: apply them as context, challenge them when evidence or reasoning warrants it, and call out when a source or task supports, weakens, contradicts, or depends on an Opinion.
- If the user's message contains only a file, URL, or source attachment, treat it as a request to ingest it unless surrounding context says otherwise.
- For ambiguous captures, use Inbox or unprocessed notes rather than forcing a project.
- Treat chat captures, Inbox captures, and similar user-provided memory as material that may disappear from normal working context. Do not reduce them to vague summaries or rely on future chat search, automation logs, or Git history as the primary retrieval layer. When saving or remembering such material, preserve concrete future-use details such as plans, things to test, constraints, caveats, rejected options, examples, exact terminology, and retrieval keywords in the appropriate durable note. Use synthesis, but keep enough specificity that a future agent can resume the work without recovering the raw capture.
- Before bulk edits or reorganizations, summarize intended changes and review the diff.
- Before broad searches, start from likely Project notes, indexes, topics, recent notes, and unprocessed notes.
- When documenting a third-party tool, repository, package, parser, or service, include the canonical source URL or provenance link.
- Do not attempt global cascade maintenance during ordinary edits. Make local, high-confidence updates and record broader uncertainty as follow-up.
- When ingestion or automation updates linked project material, update the relevant Project note when the change affects project state, next actions, open questions, active workflows, important notes, or guardrails. Project notes should not drift away from the linked notes they summarize.
- When a template workflow or convention changes, perform a deployment propagation checkpoint before the final report: identify which deployed vaults should receive the compatible change now, which should intentionally diverge, and which need user approval because of privacy or scope. For changes that require deployment-machine setup, such as Codex config, persisted approvals, automation definitions, local databases, skill symlinks, or tool prerequisites, also update deployment-facing guidance such as `README.md`, `deploy-vault-from-template.md`, [[vault-automations]], and the affected Procedure notes so future deployed vaults inherit the policy.

When editing Question notes, reconcile `status` with the body and active Project usage:

- `Open`: unresolved, provisional, still being tested, or actively driving planning.
- `Answered`: accepted working policy, reflected elsewhere if needed.
- `Deferred`: valid but inactive.
- `Superseded`: replaced by another durable note.

A `## Current Answer` does not automatically mean the Question is answered.

## Project-Scoped Memory

Project workspaces may contain a local `AGENTS.md` that points to a primary Project note. When such a pointer exists, read that Project note and the directly linked notes relevant to the task as the default memory scope before searching the whole vault.

If the user refers to a raw file, folder, dataset, manuscript, external document, or path-like reference from a project workspace, first check the primary entry note and linked Source notes for External Raw Locations or `root_key` plus `relative_path` pointers.

Project-local `AGENTS.md` files should rely on the configured vault root from global instructions. They should not copy full vault rules or embed machine-specific paths.

Project-local `AGENTS.md` files should also include a short workspace documentation rule: before creating or extending Markdown documentation in the workspace, decide whether it is durable project knowledge. If it is durable, write or update the appropriate vault note instead of creating a parallel `docs/` knowledge base beside the code or scripts.

When initializing project memory, follow [[procedures/initialize-project-memory]].

## ADR Policy

Major vault, workflow, and agent-operation decisions belong in `adr/` as ADR notes with `type: ADR`.

Use `status` to track lifecycle. Common values are `Proposed`, `Accepted`, `Superseded`, and `Rejected`.

Do not silently rewrite prior ADR decisions. If direction changes, create a new ADR that supersedes the old one and link between them.

## Procedures

Recurring workflows are described in `procedures/` as `type: Procedure` notes. Follow the relevant Procedure when the user asks for that workflow.

The Procedure note is the portable source of truth. Skill wrappers should activate the workflow, not duplicate it.

`review-multi-vault-consistency` is a special case: the template carries it so a designated main/control brain can be deployed from the same starter kit, but ordinary vaults should not list it as an active workflow or create automations for it.

## Git Checkpoints

After an agent changes the vault, normally run [[procedures/git-checkpoint-vault-changes]] unless the user asks not to commit or push.

Review changed scope first, exclude local junk and unrelated edits, commit a coherent checkpoint, push when approved or expected by the workflow, and report the final state.

Ask before pushing broad diffs, vault-structure changes, attachments, secrets, credentials, sensitive documents, generated dumps, or anything not clearly covered by the request.

External or machine-local memory summaries are hints, not authority. If remembered guidance conflicts with current vault files, project-local `AGENTS.md`, procedures, ADRs, or the user's current instruction, follow the live vault instruction and treat the remembered guidance as stale.

## Agent Skills

Vault-owned skills live under `.agents/skills/`. They are reusable activation wrappers around procedures, not replacements for Procedure notes.

Visible Skill catalogue notes live in `skills/` and point to the hidden package path.

Expose or install skills in an agent runtime only during explicit setup. Prefer links to the vault-owned package over copied wrappers when the runtime supports it.

## What Agents Should Do

- Create and edit notes using frontmatter and H1 conventions.
- Create and edit Type notes at the vault root.
- Add or modify relationships without breaking wikilinks.
- Create and edit saved YAML views in `views/`.
- Use procedures and skills for recurring workflows.
- Activate `review-multi-vault-consistency` only when this vault is the designated main/control brain for a multi-vault setup.

## What Agents Should Avoid

- Do not move existing Type files unless asked.
- Do not treat files in `attachments/` as notes, types, or view definitions.
- Do not silently overwrite a custom `AGENTS.md`.
- Do not rewrite installation-specific app configuration unless asked.
- Do not use `review-multi-vault-consistency` to inspect another vault's private content unless the user explicitly approves that scope.
- Do not commit machine-local metadata, cache paths, temporary files, secrets, or credentials.
