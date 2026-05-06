---
type: Procedure
status: Active
Belongs to: "[[vault]]"
_organized: true
---

# Configure Global Agent Instructions

## Goal

Install or check machine-local global agent instructions from [[global-agent-instructions-template]]. Replace `<VAULT_ROOT>` only in the machine-local instruction surface. Verify that the configured root is readable and contains `AGENTS.md`.

## Steps

1. Read `AGENTS.md` and the relevant Project note before changing the vault.
2. Confirm the current scope and avoid unrelated edits.
3. Make the smallest useful change that satisfies the workflow.
4. Validate links, frontmatter, and retrieval paths touched by the change.
5. Report what changed, what was left alone, and any follow-up needed.

## Boundaries

Do not add private source material, secrets, credentials, cache files, generated dumps, or machine-specific paths to durable vault notes.
