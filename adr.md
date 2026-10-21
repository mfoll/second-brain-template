---
type: Type
_icon: scales
_color: "#6366f1"
_order: 5
_organized: true
---

# ADR

An ADR records a durable decision about vault structure, workflow, architecture, or operating policy.

ADRs should preserve enough decision trace for a future human or agent to replay the choice: the options considered, rejected alternatives, context or precedent used, ambiguity or exception handled, authorization when relevant, consequences, and revisit trigger. Do not store routine execution detail or model chain-of-thought.

Link an ADR to the Project, Responsibility, or system surface it governs with `belongs_to`.

## Status lifecycle

- `Proposed`: under consideration and not yet authoritative.
- `Accepted`: the current durable decision.
- `Superseded`: replaced by a newer linked ADR.
- `Rejected`: considered but not adopted.

Do not silently rewrite an Accepted ADR when direction changes. Create a new ADR, mark the earlier one Superseded, and link both decisions.

Use `superseded_by` for a replacement recorded in frontmatter. Human-readable `Superseded by` labels may remain in prose.
