---
name: lint-vault
description: Use to diagnose mechanical, structural, retrieval, compactness, or convention problems in the current vault without broad rewrites.
---

# Lint Vault

## Source of truth

- Vault rules: `AGENTS.md`
- Checks and severity: `procedures/lint-vault.md`
- Compactness helper: `.agents/skills/lint-vault/scripts/compactness_audit.py`
- Tolaria icon helper: `.agents/skills/lint-vault/scripts/tolaria_icon_audit.py`
- Curated icon snapshot: `.agents/skills/lint-vault/references/tolaria-icon-names.txt`

Read the vault rules and Procedure completely before acting.

## Guardrails

- Inventory canonical tracked notes and exclude implementation, local, generated, cache, attachment, and support trees.
- Use both helpers for deterministic warnings, then inspect actual notes before conclusions. The current Tolaria icon picker remains authoritative when it differs from the bundled snapshot.
- Compactness thresholds are review signals, not blanket failures for long evidence.
- Recommend preservation-led routing, never blanket shortening; a threshold does not authorize deletion. A valid result may be no change, safe wording reduction, reorganization or routing, or a structural split.
- In scheduled runs, identify a narrowly matched responsible Codex task when possible, report it with the proposed workflow, and wait for user confirmation before contacting it. If none exists, offer to perform the focused follow-up in the current task.
- Project human views are optional. Validate existing views, but do not report absence solely because an active Project has no saved-view surface; honor an explicit `Project view: false` marker. Respect Inbox boundaries, UI-authored Type state, and deliberate local conventions.
- Do not process Inbox, rewrite summaries, normalize broad relationships, delete notes, or apply fixes unless authorized.
- Route strategic questions to `review-vault-health`.
