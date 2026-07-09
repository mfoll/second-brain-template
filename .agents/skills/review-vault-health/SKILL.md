---
name: review-vault-health
description: Use for a strategic review of whether the current vault is useful, expressive, compact, and aligned with the user's working model.
---

# Review Vault Health

## Source of truth

- Vault rules: `AGENTS.md`
- Complete workflow: `procedures/review-vault-health.md`
- Helper: `.agents/skills/lint-vault/scripts/compactness_audit.py`

## Guardrails

- Default to read-only and inventory canonical notes only.
- Inspect entry points, Types, active Projects and Responsibilities, views, Questions, synthesis, Procedures, ADRs, and skills.
- Judge low counts rather than enforcing quotas.
- Distinguish lint findings from strategic issues such as overloaded entry notes, append-only writeback, weak resumption, or hidden knowledge.
- Use compactness metrics as evidence, not a reason to shorten cold Sources or Events.
- Prefer a few high-value recommendations and propose broad changes before applying them.
