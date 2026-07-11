---
type: Guide
related_to: "[[vault]]"
_organized: true
---

# Global Agent Instructions Template

Use this text only to bootstrap a standalone vault. If an existing routing/control vault or configuration repository owns generated global instructions, follow [[procedures/configure-global-agent-instructions|Configure Global Agent Instructions]] and update that executable source instead; do not install this template as a competing instruction layer.

## Second Brain Memory

I maintain a `<VAULT_ROLE>` Second Brain vault at `<VAULT_ROOT>`. The Markdown vault is the durable source of truth. Vault-level rules are in `<VAULT_ROOT>/AGENTS.md`.

When prior context may help, read relevant vault notes before answering. If the current workspace has a local `AGENTS.md` declaring a Second Brain vault role and pointing to an entry note, use that named vault root plus the entry note and linked notes as the primary memory scope before searching more broadly.

Read progressively from frontmatter, H1, summary, and headings into only the relevant sections and evidence. External memory summaries and search snippets are hints, not authority; current user instructions, vault and project rules, Types, Procedures, and accepted ADRs take precedence.

When the user asks for a concrete output, such as an email, message, plan, checklist, recommendation, administrative draft, decision support, or supplier/order request, and the request clearly depends on facts that are missing from the prompt, first look for the missing context in the relevant Second Brain vault before answering. Use targeted searches based on named entities, objects, people, places, projects, dates, brands, suppliers, filenames, or obvious synonyms. Only produce a generic template with placeholders after that retrieval attempt fails, or when the user explicitly asks for a generic/template answer.

Do not perform Second Brain retrieval when the prompt already contains the information needed, when the task is genuinely self-contained, or when the user explicitly asks for a generic answer.

When outside a specific project, search conservatively from the vault rules, project notes, indexes, topics, recent notes, and Inbox/Unprocessed notes.

Do not let workspace `docs/` folders become parallel Second Brain stores. Keep scripts, prototypes, fixtures, generated outputs, and implementation-local notes in the workspace. Durable design docs, workflow decisions, research notes, open questions, tool evaluations, and project state belong in the relevant vault as typed notes linked from the project or entry note.

If a workspace expects Second Brain memory but the configured root for its named vault role is unknown or unreadable, stop and ask the user to configure the global Second Brain instructions with the correct vault path. Do not guess the path or create a new vault.

Read from the vault when useful. Write when the user explicitly asks to save, remember, ingest, process, organize, update, maintain, or contribute knowledge. Significant work in a linked workspace also authorizes direct, high-confidence project-state writeback under the vault's rules; propose broad or uncertain cascades.

When multiple vaults are configured, keep durable knowledge in its authoritative vault. Do not duplicate it across vaults unless the user explicitly asks; when cross-vault context is necessary, prefer the smallest useful non-sensitive pointer.

For an explicit memory capture, choose the appropriate existing Type rather than merely appending text to a Project. Preserve concrete future-use details such as plans, constraints, caveats, rejected options, examples, exact terminology, and retrieval hooks needed to resume the work.

Before creating, renaming, broadening, or replacing a workflow, Procedure, Skill, automation, Type, or ADR, compare the request with the live vault. If it overlaps, duplicates, or conflicts with what exists, summarize the current state and smallest compatible change, then ask for confirmation unless the user already approved the change after that comparison.

If the user's message contains only a file, URL, or source attachment, treat it as a request to ingest it into the vault unless surrounding context clearly says otherwise.

For external source ingestion, use the `ingest-source` skill when available. Ingested external material should use `type: Source`.

For ambiguous captures, use Inbox/Unprocessed rather than forcing a project. Before bulk edits or reorganizations, summarize the intended changes first.

## Codex Automations

When creating or updating Codex automations, explicitly set the automation model to the latest available default-capable Codex model unless the user explicitly asks for another model. Do not create or recreate automations with stale older defaults just because Codex suggests them.

After creating or updating a Codex automation, verify the stored model in the automation configuration and, when Codex Desktop uses a local automation database, verify the database row too. If either still shows an older model, fix it before reporting the automation as done.

For write-capable automations, a persisted `git push` approval or configured network path is only an execution mechanism, not authorization. Push only when the current user and vault policy explicitly authorize that repository and action; otherwise stop after the permitted local commit.
