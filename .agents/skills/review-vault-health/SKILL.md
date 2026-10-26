---
name: review-vault-health
description: "Assess vault usefulness, current state and retrieval in the selected deployed vault; recommend maintenance priorities, read-only by default."
---

# Review Vault Health

Assess whether the vault remains useful, current and easy to navigate. Recommend a few high-value improvements, read-only by default.

For mechanical defects, use `lint-vault`. Health review interprets some of the same audit evidence; a structurally valid vault can still contain stale summaries or buried decisions.

## Source of truth

- Vault rules: `AGENTS.md`
- Complete workflow: `procedures/review-vault-health.md`
- Helper: `.agents/skills/lint-vault/scripts/compactness_audit.py`

Read the vault rules and Procedure completely before acting.

## Guardrails

- Default to read-only and inventory canonical notes only.
- Inspect entry points, Types, active Projects and Responsibilities, views, Questions, synthesis, Procedures, ADRs, and skills.
- Judge low counts rather than enforcing quotas.
- Distinguish lint findings from strategic issues such as overloaded entry notes, append-only writeback, weak resumption, or hidden knowledge.
- Use compactness metrics as evidence, not a reason to shorten cold Sources or Events.
- Prefer a few high-value recommendations and propose broad changes before applying them.

Select this package by the requested vault role, not its name alone. Reuse rules and the complete Procedure already read in this session while they remain current; reread after a relevant change.
