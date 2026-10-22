---
type: ADR
status: Accepted
belongs_to: "[[vault]]"
related_to:
  - "[[project]]"
  - "[[project-scoped-memory]]"
  - "[[procedures/initialize-project-memory|Initialize Project Memory]]"
_organized: true
---

# ADR 0006: Use Project Notes for Active Subprojects

## Context

A vault accumulates several overlapping meanings of "project":

- an agent-application project, which is a workspace folder plus a memory pointer;
- a Second Brain `Project`, which is a durable work context with outcome, current state, next actions, open questions, sources and decisions;
- an everyday project name, which may describe an umbrella programme, a publication or deliverable package, a dataset, a collaboration, an administrative label or a local team convention.

Some programmes have umbrella names with deliverable-scale subprojects. An umbrella programme, `<umbrella-project>`, may contain a distinct active subproject, `<child-project>`, that has its own outcome, deliverable trajectory, collaborators, files, deadlines, analyses and next actions.

## Decision

> [!note]
> Create a separate Second Brain `Project` note for an active subproject when it has its own outcome, project state, next actions, deadlines, collaborators, files, analyses, deliverable trajectory or workspace needs, even if it belongs scientifically or operationally under a larger umbrella Project.

Keep the umbrella Project as the programme-level entry point. It preserves shared context, common raw-file locations, cross-cutting definitions, interpretation principles and a selective list of active subprojects. It does not accumulate every subproject's detailed next actions, deliverable state or file-specific Source notes.

Use frontmatter and body links to preserve the hierarchy:

- child Project: `belongs_to: [[umbrella-project]]`;
- umbrella Project: selective `has` links and/or a `## Subprojects` body section for active child Projects;
- workspace pointer: the most specific active Project note for the task;
- shared Sources, Questions, Concepts and Opinions: attach to the most specific responsible Project when possible, and add `related_to` links to the umbrella or sibling Projects only when they genuinely support retrieval or interpretation.

Human-facing saved views stay small. A child Project note may appear on the umbrella surface when it is a current human-facing subproject, but low-level child Sources usually remain on the child Project's own surface.

## Example

> [!example]
> `<child-project>` is modelled as a child Project of `<umbrella-project>` because it has its own deliverable trajectory. The child note belongs to the umbrella, has its own guarded-write external Source note and its own workspace pointer. The umbrella note remains the entry point for the broader programme context and selectively links to the child as a subproject.

## Consequences

Project notes stay useful as resumption surfaces instead of becoming broad archives. Umbrella Projects remain navigable, while deliverable-scale work carries its own actions, sources and decision history.

Some notes relate to both the umbrella and the child. That is acceptable, but agents should avoid mechanically duplicating every relationship. Prefer one primary `belongs_to` path and add `related_to` links only when the second context is useful for future retrieval.

## Revisit When

> [!question]
> Revisit if umbrella Projects become too thin to be useful, if child Projects become too fragmented, or if deliverable packages need a dedicated Type distinct from `Project`.

## Provenance

Ported on 2026-10-22 from the maintainer's work/control vault, ADR 0016 *Use Project Notes for Active Subprojects* (2026-05-15); work-specific names and examples were replaced by generic wording.
