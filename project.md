---
type: Type
_icon: rocket
_color: "#3b82f6"
_organized: true
_order: 0
---

# Project

A Project is a finite effort larger than one sitting. Its note is the live resumption surface for humans and agents, not a full archive or task database.

## Compact front-page contract

- Target 600–1,200 words; a complex umbrella may reach about 1,500.
- `Current State` contains current truth only: normally no more than five bullets or 250 words.
- `Next Actions` contains 3–7 outcome-level actions. Keep microtasks in the active chat or task system.
- `Open Questions` and `Important Notes` normally contain 3–7 prioritized links each.
- `Maintenance Log` keeps the latest 3–5 meaningful milestones. Git carries routine edit history.
- Replace or reconcile old synthesis when work changes; do not append another dated mini-report.
- Keep each fact in one canonical durable note and link to it from the Project.
- Compactness is subordinate to preservation. A long Project may be a justified temporary state when unique durable details have not yet been routed safely.

Project frontmatter is navigational, not exhaustive. Child notes normally link back with `belongs_to`; use Project `has` only for active subprojects and high-value entry points. Active Projects normally have a 3–5-note human view following [[procedures/maintain-project-human-view|Maintain Project Human View]], unless the user has set `Project view: false`.

Before removing a Project `has` value or body entry-point link, verify that the target remains findable through its own relationships, another hub or Project link, a saved view, backlinks, or an explicit Inbox/archive convention.

## Umbrellas and subprojects

Create a child Project when a work package has its own outcome, state, actions, collaborators, artifacts, or publication trajectory. The umbrella keeps shared context and a selective subproject list; it does not repeat child details. Use `belongs_to` from child to umbrella and point project workspaces to the most specific active entry note.

## Template

```md
# Project Name

One or two sentences describing the project.

## Outcome

What success means.

## Current State

- Current facts, blockers, and active decisions only.

## Scope and Boundaries

What belongs here, what does not, and important responsibility or privacy boundaries.

## Working Context

Only the synthesis needed for resumption. Rename this section when a project-specific heading is clearer.

## Active Workflows

Current procedures, recurring loops, or work surfaces.

## Next Actions

- [ ] Three to seven outcome-level actions.

## Open Questions

- Prioritized Question links.

## Important Notes

- The few notes worth opening next.

## Do Not Do Yet

> [!danger]
> Optional guardrails against premature or unsafe work.

## Maintenance Log

- YYYY-MM-DD: Meaningful state transition or decision; include a compact decision trace only when it will matter later.
```

Omit a section only when it would be empty or misleading. Detailed evidence, chronology, exact methods, and reusable decisions belong in linked Sources, Events, Concepts, Questions, Opinions, Procedures, ADRs, or any other suitable Type present in the deployed vault. Before removing them from a Project, inspect and update the destination; a link or filename alone is not proof that the payload was preserved. Git may carry routine edit history, but it is not the sole durable home for future-use decisions or exact project context.

Use the `danger` callout shown in the template only when the section contains one compact prose block. Keep lists and multi-block sections as ordinary Markdown. See [[tolaria-callouts]] for the vault-wide convention.
