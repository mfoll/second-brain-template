---
type: Procedure
status: Active
belongs_to: "[[vault]]"
related_to:
  - "[[procedures/configure-global-agent-instructions|Configure Global Agent Instructions]]"
  - "[[procedures/maintain-project-human-view|Maintain Project Human View]]"
_organized: true
---

# Initialize Project Memory

Use this procedure to connect a workspace to a configured Second Brain vault through a compact local pointer. The scope may target one entry note, usually a Project, or deliberately use the whole vault.

## Steps

1. Resolve the logical vault role and project-root convention from current machine-local instructions. If ambiguous, ask.
2. Confirm the selected vault root is readable and contains `AGENTS.md`; never guess or create a vault root.
3. Prepare the final workspace folder before asking the user to open it in an agent application.
4. Confirm entry-point scope versus vault scope. For entry-point scope, search existing notes before creating a new one and default to Project only when it fits the work.
5. Read the selected vault's `AGENTS.md` and relevant Type. Create or update the entry note with compact current synthesis and high-confidence relationships.
6. Link maintained external files through confirmed Source notes. Do not deep-scan shared or private roots.
7. For a new active Project, follow [[project]] and create its small human view unless the user explicitly chooses `Project view: false`.
8. Create or update only the marked memory section of workspace `AGENTS.md`, keeping the complete pointer near 80 words. Do not copy vault rules, secondary notes, raw paths, artifact inventories, or runbooks.
9. Add a minimal `CLAUDE.md` containing `@AGENTS.md` when Claude Code may use the workspace and no deliberate custom shim exists.
10. Apply the user's local repository and backup policy, keeping credentials, raw data, controlled material, caches, environments, and generated bulk out of Git.
11. Review workspace and vault diffs, then tell the user the exact absolute folder to open.

## Entry-point pointer

```md
## Second Brain memory

Vault role: `<vault-role>`. Entry note: `<confirmed-wikilink>`.

Resolve the vault root from global instructions. If it is unknown or unreadable, stop and ask; do not guess or create a vault. Read the vault `AGENTS.md`, then the entry note and only task-relevant linked or vault-routed notes. Keep durable knowledge in the vault; workspace Markdown remains implementation-local, generated, or transient.
```

## Vault-scoped pointer

```md
## Second Brain memory

Vault role: `<vault-role>`. Entry note: none (vault-scoped).

Resolve the vault root from global instructions. If it is unknown or unreadable, stop and ask. Read the vault `AGENTS.md`, then start from relevant Type and topic surfaces. Do not create a Project unless asked.
```

The final handoff must name the prepared absolute folder. The local pointer is routing, not a second policy or memory system.
