---
type: Procedure
status: Active
belongs_to: "[[vault]]"
related_to:
  - "[[procedures/lint-vault|Lint Vault]]"
  - "[[maintain-vault]]"
_organized: true
---

# Review Vault Health

Use this procedure for a strategic, read-only review of whether the vault is useful, expressive, compact, and aligned with the user's working model. Mechanical defects belong in [[procedures/lint-vault|Lint Vault]].

## Scope

Inventory canonical tracked notes and exclude implementation, local, attachment, generated, cache, and support trees. Use `.agents/skills/lint-vault/scripts/compactness_audit.py <vault-root>` as evidence, not as a blanket shortening mandate.

## Review questions

- Do active Projects and Responsibilities provide clear resumption surfaces?
- Are Current State, actions, Questions, links, and logs current rather than append-only chronology?
- Are unresolved Questions, reusable Concepts, ongoing Responsibilities, decisions, or workflows hidden inside prose or Inbox captures?
- Are `has` lists and views selective, with no orphan risk after compaction?
- Do Types, procedures, skills, views, and automations earn their maintenance cost?
- Are important sources, provenance, evidence boundaries, and retrieval paths visible?
- Are automatically loaded instructions and hot entry notes concise, while long evidence notes retain useful detail?

## Steps

1. Read `AGENTS.md`, the root Project, maintenance Responsibility, Type notes, and recent meaningful milestones.
2. Run a canonical type inventory and the compactness helper.
3. Inspect active Projects and Responsibilities first, then Questions, synthesis Types, Sources, Procedures, ADRs, Guides, and unprocessed surfaces.
4. Separate mechanical lint findings, strategic recommendations, candidate typed notes, and workflow changes.
5. Prefer a few high-value recommendations. Treat low Type counts as prompts for judgment, not quotas.
6. Propose broad structural work before editing; apply only focused authorized changes and then run the relevant maintenance procedures.

Lead with judgment: whether the vault is sound enough to trust and what would most improve future retrieval.
