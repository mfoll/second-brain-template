# Review Multi-Vault Consistency

Use this skill when the user asks to check consistency across a main/control vault, deployed vaults, a template repository, and Codex automations.

This skill is only for a vault that owns multi-vault routing and template coordination. Do not activate it in ordinary deployed vaults by default.

## Workflow

1. Confirm this vault is the designated routing/control vault for the multi-vault setup.
2. Read the vault-level `AGENTS.md`.
3. Read `procedures/review-multi-vault-consistency.md`.
4. Follow that procedure as the source of truth.
5. Keep the review read-only unless the user explicitly asks to implement a specific fix.

Do not duplicate or replace the procedure body here; this package is only an activation wrapper.
