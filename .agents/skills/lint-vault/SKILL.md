---
name: lint-vault
description: Use to diagnose mechanical, structural, retrieval, compactness, or convention problems in the current vault without broad rewrites.
---

# Lint Vault

## Source of truth

- Vault rules: `AGENTS.md`
- Checks and severity: `procedures/lint-vault.md`
- Helper: `.agents/skills/lint-vault/scripts/compactness_audit.py`

## Guardrails

- Inventory canonical tracked notes and exclude implementation, local, generated, cache, attachment, and support trees.
- Use the helper for deterministic warnings, then inspect actual notes before conclusions.
- Compactness thresholds are review signals, not blanket failures for long evidence.
- Respect `Project view: false`, Inbox boundaries, UI-authored Type state, and deliberate local conventions.
- Do not process Inbox, rewrite summaries, normalize broad relationships, delete notes, or apply fixes unless authorized.
- Route strategic questions to `review-vault-health`.
