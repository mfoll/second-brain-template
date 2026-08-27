---
type: Procedure
status: Active
belongs_to:
  - "[[vault]]"
related_to:
  - "[[procedures/update-project-summary|Update Project Summary]]"
  - "[[procedures/update-project-next-actions|Update Project Next Actions]]"
_organized: true
surface_for:
  - "[[vault]]"
---

# Maintain Project Human View

Use this procedure when creating, refreshing, or checking the small human-facing saved view for a Project.

## Goal

Keep an active Project's saved view small when a human workbench is useful, not as a project index. Not every Project needs a saved view; some are better resumed from the Project note, linked notes, or other existing surfaces.

## Frontmatter Contract

Human views are optional. Create one when a small saved-view workbench would help the user resume the Project. A Project may remain without a view when that workbench does not add enough value.

The Project note may record an explicit opt-out when useful:

```yaml
Project view: false
```

Agents must not add this opt-out unless the user explicitly chooses it. The absence of a view does not itself require this marker.

Notes that belong on the human surface use:

```yaml
surface_for:
  - "[[vault]]" # replace with the real Project note wikilink
```

The Project note itself counts as part of the view and should usually carry its own `surface_for` marker.

## View Shape

Create the view as `views/surface-<project-stem>.yml` unless a clearer existing filename should be preserved. Use a plain human-facing view name without a `Surface` prefix or suffix; the filename already carries the surface role. In YAML examples, replace `[[vault]]` with the real Project note wikilink.

```yaml
name: <Project Title>
icon: null
color: null
sort: modified:desc
listPropertiesDisplay:
- type
- status
filters:
  all:
  - field: surface_for
    op: contains
    value: "[[vault]]" # replace with the real Project note wikilink
```

## Inclusion Rule

The target size is 3-5 notes including the Project note. A larger active project may temporarily reach 8-10 notes, but more than 10 is a warning sign.

Include only notes that are meaningful to open as a human project surface:

- the Project note;
- a current draft, deliverable, plan, or review surface;
- a decision-driving Question;
- a key source packet or synthesis note;
- an active workflow note that the user may intentionally open.

Exclude notes that are useful only to agents:

- raw provenance or old captures;
- low-level Sources and broad candidate lists;
- stale, archived, superseded, or historical notes;
- implementation details and hidden package files;
- notes that are retrievable through backlinks or Project `Important Notes` but do not belong in the human working set.

## Project Surface Check

Run this check after important project-scoped changes and before the Git checkpoint:

1. Identify the affected active Project.
2. If no useful saved-view workbench is warranted, leave the Project without a view and do not treat that absence as a defect.
3. If the Project has `Project view: false`, do not create a view.
4. If the Project is not active, do not require a view unless the user asks.
5. Inspect the changed notes plus the current view members when a view exists.
6. Add `surface_for` only to notes the user is likely to open now.
7. Remove `surface_for` from stale, archived, superseded, agent-only, or low-level notes.
8. Keep the view near 3-5 notes when possible; if it would exceed 10, demote lower-priority notes back to normal Project links.
9. If a surface change is ambiguous, report the proposed add/remove instead of silently changing the view.
10. Run `.agents/skills/lint-vault/scripts/tolaria_icon_audit.py <vault-root>`, reload Tolaria, and confirm that any configured icon renders.
11. Review the diff.

## Output Standard

The saved view should feel like a clean project workbench: open it and see the main Project note, the current work artifacts, and only the few notes that matter for human resumption.
