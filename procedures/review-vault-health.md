---
type: Procedure
status: Active
Belongs to: "[[vault]]"
Related to:
  - "[[procedures/lint-vault]]"
_organized: true
---

# Review Vault Health

Use this procedure when the user asks whether the vault is useful, expressive, and aligned with its intended scope.

## Goal

Assess the vault as a thinking and retrieval system, not only as a mechanically valid file tree.

## Checks

- Whether Projects expose outcome, current state, scope and boundaries, important notes, active workflows when applicable, next actions, open questions, and maintenance history.
- Whether Responsibilities capture ongoing ownership that should not be treated as finite projects.
- Whether Topics provide useful retrieval surfaces without becoming vague tags.
- Whether Questions are visible, statused, and not buried in project prose or next actions.
- Whether Concepts capture reusable distinctions, methods, models, vocabulary, or synthesis.
- Whether Sources preserve provenance and feed synthesis instead of becoming a raw archive.
- Whether Procedures and Skills cover recurring workflows without duplicating each other.
- Whether ADRs capture durable decisions rather than rewriting history silently.
- Whether Project `Has` relationships are selective and navigational.
- Whether archived, deferred, or unprocessed notes still have clear lifecycle signals.
- Whether views help users and agents resume work.

## Steps

1. Read `AGENTS.md`, [[vault]], recent Maintenance Log entries, and saved views.
2. Inventory note counts by Type and identify obvious gaps or imbalances.
3. Inspect active Projects and Responsibilities before broad searching.
4. Look for hidden Questions, Concepts, Responsibilities, Procedures, or ADR candidates inside project prose, source summaries, generic notes, and next actions.
5. Separate mechanical findings from strategic recommendations. Mechanical issues belong to [[procedures/lint-vault]].
6. Recommend a short list of high-leverage improvements, such as promoting specific Questions, refreshing a stale Project summary, creating a missing Responsibility, simplifying a relationship list, or improving a view.
7. Stay read-only by default. Ask before creating new Types, broad relationship rewrites, large reorganizations, or automation changes.
8. If the user approves edits, apply focused changes and then run the relevant follow-up procedure.

## Output Standard

Lead with judgment: structurally sound or not, expressive enough or not, and the next few changes that would most improve retrieval. Do not require arbitrary minimum counts for any Type.


## Guardrails

- Keep edits scoped to the user's request and the relevant Project or Source.
- Use `Belongs to`, `Related to`, and `Has` for relationships.
- Do not add secrets, credentials, local cache paths, generated dumps, or machine-specific setup details unless the note is explicitly about that local setup.
- Ask before creating new Types, broad relationship rewrites, mass moves, deletions, or public/private visibility changes.
