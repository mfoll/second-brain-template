---
type: Type
_icon: rocket
_color: "#3b82f6"
_organized: true
_order: 0
---

# Project

A Project is a finite effort larger than one sitting. It has an intended outcome, active context, and eventually an end state.

A Project's frontmatter relationships should support navigation and project resumption. They do not need to exhaustively list every note that mentions the project. Notes that belong to the project should normally link back through their own `Belongs to` relationship or appear in relevant Project body sections or views.

Project notes are the live entry points for human and agent work. They are not just summaries and they are not full archives: they should stay coherent enough that opening the Project note tells the user or an agent what the project is, where it stands, what to read first, and what to do next.

Active Projects normally have a small human-facing saved view unless the Project note has `Project view: false`. The view is a human working surface, not an index: aim for 3-5 notes including the Project note, and use 8-10 only as a soft maximum for unusually active projects. Use `Surface for` with the real Project wikilink only on notes the user is likely to open now. Keep agent-only memory and low-level support notes linked elsewhere, not in the view.

## Project Note Structure

Use this structure for new Project notes and as the normalization target when refreshing existing Project notes:

```md
# Project Name

One or two sentences describing the project.

## Outcome

What success means.

## Current State

Where the project stands now. Keep this short and update it when ingestion, project work, or decisions change the project state.

## Scope and Boundaries

What belongs in the project, what does not, and any important privacy, routing, or responsibility boundaries.

## Working Context

Domain-specific synthesis. Rename or split this section when a clearer project-specific heading is useful, such as `Working Thesis`, `Current Principles`, `Candidate Tools`, `Draft Artifacts`, or `Package Management Policy`.

## Active Workflows

Procedures, automations, recurring routines, active work surfaces, or operating loops.

## Next Actions

Small, scannable resumption list.

## Open Questions

Links to Question notes, plus only short inline questions that do not yet deserve their own note.

## Important Notes

Curated links a human or agent should read first. Do not list every backlink.

## Do Not Do Yet

Optional guardrails against premature work, unsafe automation, or distracting implementation paths.

## Maintenance Log

Dated project-state changes. Keep this as a short audit trail, not a full transcript.
```

Sections may be omitted only when they would be empty or misleading. Domain-specific middle sections are welcome, but `Outcome`, `Current State`, `Scope and Boundaries`, `Next Actions`, `Open Questions`, `Important Notes`, and `Maintenance Log` should remain predictable in active Project notes.
