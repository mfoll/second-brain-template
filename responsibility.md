---
type: Type
_icon: target
_color: "#ef4444"
_order: 8
_organized: true
---

# Responsibility

A Responsibility is an ongoing area of ownership that may contain projects, recurring workflows, and durable context.

## Hierarchy

Responsibilities are the roots of the `belongs_to` hierarchy: every durable note rolls up through one primary `belongs_to` chain to the Responsibility that answers for it, and agents, Lint Vault and any graph viewer follow those chains. A Responsibility normally has no parent; it belongs to another Responsibility only when it is a sub-duty of that area, such as team operations or funding under a wider role. No Responsibility is an umbrella for all of the user's activities: each role with its own accountability is a root of its own. See [[adr/0011-root-belongs-to-at-responsibilities-and-home-exploration-clusters-in-topics|ADR 0011]].

## Template

```md
---
type: Responsibility
status: Active
related_to:
  - "[[a-topic-or-person-that-gives-context]]"
has:
  - "[[the-project-that-is-its-current-entry-point]]"
_organized: true
---

# Responsibility Name

One or two sentences on what this area of ownership covers and why it has no end date.

## Scope

- What belongs here and what stays elsewhere.

## Current State

- The few facts needed to resume this area.

## Active Projects and Workflows

- [[the-project-that-is-its-current-entry-point]]

## Next Actions

- [ ] Three to five outcome-level actions.

## Maintenance Log

- YYYY-MM-DD: Created.
```

A Responsibility is a root of the `belongs_to` hierarchy, so it normally has no `belongs_to` of its own; its Projects point to it.
