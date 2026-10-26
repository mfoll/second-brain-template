---
name: lint-vault
description: "Check vault metadata, links, hierarchy and structural contracts in the selected deployed vault; report defects without automatic fixes."
---

# Lint Vault

Check metadata, links, hierarchy and other structural contracts. Report errors and warnings without applying fixes.

For judgment about usefulness, stale project state or unnecessary workflows, use `review-vault-health`. Lint findings can inform that review.

## Source of truth

- Vault rules: `AGENTS.md`
- Checks and severity: `procedures/lint-vault.md`
- Contracts helper: `.agents/skills/lint-vault/scripts/contracts_audit.py` (requires the sibling `links_audit.py`; note headers, Type identities and Skill pairs, not full YAML or semantic validation)
- Compactness helper: `.agents/skills/lint-vault/scripts/compactness_audit.py`
- Tolaria icon helper: `.agents/skills/lint-vault/scripts/tolaria_icon_audit.py`
- Hierarchy helper: `.agents/skills/lint-vault/scripts/hierarchy_audit.py` (`belongs_to` drift per the vault's hierarchy ADR, exceptions read from `hierarchy_root` and `accepted_double_parent` frontmatter flags; `--tree` prints the inferred home tree)
- Link helper: `.agents/skills/lint-vault/scripts/links_audit.py` (unresolved or ambiguous wikilinks, missing relative Markdown link targets and relationship values that are not wikilinks; fenced code and code spans are ignored; exit status 1 on errors)
- MIT-licensed Phosphor name list: `.agents/skills/lint-vault/references/phosphor-icon-names.txt`

Read the vault rules and Procedure completely before acting.

## Guardrails

- Inventory canonical tracked notes and exclude implementation, local, generated, cache, attachment, and support trees.
- Use the five helpers for deterministic contract, compactness, icon, hierarchy and link findings, then inspect actual notes before conclusions. The pinned Phosphor name list checks identifiers, not glyph rendering or a live app registry; the current Tolaria picker remains authoritative. The Procedure documents reproducible refresh and upstream notices.
- Compactness thresholds are review signals, not blanket failures for long evidence.
- Recommend preservation-led routing, never blanket shortening; a threshold does not authorize deletion. A valid result may be no change, safe wording reduction, reorganization or routing, or a structural split.
- In scheduled runs, identify a narrowly matched responsible agent task when possible, report it with the proposed workflow, and wait for user confirmation before contacting it. If none exists, offer to perform the focused follow-up in the current task.
- Project human views are optional. Validate existing views, but do not report absence solely because an active Project has no saved-view surface; honor an explicit `Project view: false` marker. Respect Inbox boundaries, UI-authored Type state, and deliberate local conventions.
- Do not process Inbox, rewrite summaries, normalize broad relationships, delete notes, or apply fixes unless authorized.
- Route strategic questions to `review-vault-health`.

Select this package by the requested vault role, not its name alone. Reuse rules and the complete Procedure already read in this session while they remain current; reread after a relevant change.
