---
name: check-external-raw-references
description: Use when checking, refreshing, or auditing external raw-file Source notes that use root_key plus relative_path.
---

# Check External Raw References

## Source of truth

- Vault rules: `AGENTS.md`
- Complete workflow: `procedures/check-external-raw-references.md`

Read the vault rules and Procedure completely before acting.

## Guardrails

- Resolve roots from ignored local configuration; never commit machine-specific mappings to portable notes.
- Treat external locations as read-only unless the user explicitly authorizes a specific write.
- Update only vault-side Source metadata and shallow indexes allowed by the Procedure.
- Preserve human-visible provenance and report unresolved roots, missing paths, and drift clearly.
- Avoid deep inventories, unrelated cleanup, credentials, and external moves or deletions.
- Review task-scoped diffs before checkpointing; push only with current explicit authorization.
