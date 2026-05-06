---
type: Type
_icon: hand
_color: "#eab308"
_order: 1
---

# Question

A Question records an unresolved issue, uncertainty, or research direction that should remain findable.

## Status Lifecycle

Recommended Question statuses:

- `Open`: unresolved, provisional, still being tested, or still driving active project planning.
- `Answered`: the current answer is accepted as the working policy and has been reflected in the relevant Project, Concept, Procedure, ADR, or other durable note when needed.
- `Deferred`: valid but not active; revisit only if the related project or context changes.
- `Superseded`: replaced by a better Question, ADR, Procedure, Project direction, Concept, or other durable note.

A `## Current Answer` does not automatically make a Question `Answered`.
