---
name: initialize-project-memory
description: Use when creating or updating a workspace so it points to the correct vault and one entry note, or deliberately uses vault-scoped memory.
---

# Initialize Project Memory

## Source of truth

- Vault rules: `AGENTS.md`
- Complete workflow and pointer templates: `procedures/initialize-project-memory.md`

Read the vault rules and Procedure completely before acting.

## Guardrails

- Resolve the logical vault role from global instructions; never guess a path.
- Confirm entry-point versus vault scope before creating notes.
- Keep pointers near 80 words and target one entry note. Do not copy vault rules, raw paths, inventories, or project documentation.
- Preserve custom local instructions and add only the minimal Claude import shim when appropriate.
- Do not deep-scan shared or private roots. Use confirmed Source bridges for maintained external files.
- Prepare the final folder, review affected diffs, and tell the user the exact folder to open.
- Apply the user's repository policy and push only with current explicit authorization.
