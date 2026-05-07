---
type: Guide
Related to: "[[vault]]"
_organized: true
---

# Global Agent Instructions Template

## Second Brain Memory

I maintain a Second Brain vault at `<VAULT_ROOT>`. The Markdown vault is the durable source of truth. Vault-level rules are in `<VAULT_ROOT>/AGENTS.md`.

When prior context may help, read relevant vault notes before answering. If the current workspace has a local `AGENTS.md` pointing to a Second Brain Project note, use that project note and its linked notes as the primary memory scope before searching more broadly.

When outside a specific project, search conservatively from the vault rules, project notes, indexes, topics, recent notes, and Inbox/Unprocessed notes.

If a workspace expects Second Brain memory but the vault root is unknown or unreadable, stop and ask the user to configure the global Second Brain instructions with the correct vault path. Do not guess the path or create a new vault.

Read from the vault when useful. Write to it only when the user explicitly asks to save, remember, ingest, process, organize, update, maintain, or contribute knowledge.

If the user's message contains only a file, URL, or source attachment, treat it as a request to ingest it into the vault unless surrounding context clearly says otherwise.

For external source ingestion, use the `ingest-source` skill when available. Ingested external material should use `type: Source`.

For ambiguous captures, use Inbox/Unprocessed rather than forcing a project. Before bulk edits or reorganizations, summarize the intended changes first.

## Codex Automations

When creating or updating Codex automations, explicitly set the automation model to the latest available default-capable Codex model unless the user explicitly asks for another model. Do not create or recreate automations with stale older defaults just because Codex suggests them.

After creating or updating a Codex automation, verify the stored model in the automation configuration and, when Codex Desktop uses a local automation database, verify the database row too. If either still shows an older model, fix it before reporting the automation as done.

For write-capable automations that are expected to push Git checkpoints, make sure `git push` has a persisted approval or another configured network path. If network escalation cannot run unattended, the automation may commit locally but cannot reliably push without user intervention.
