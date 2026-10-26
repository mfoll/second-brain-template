---
type: Type
_icon: rocket
_color: "#3b82f6"
_organized: true
_order: 0
---

# Project

A Project is a finite effort larger than one sitting. Its note is the live resumption surface for humans and agents, not a full archive or task database.

`status` values: `Active` (work expected), `Paused` (deliberately parked, no current actions expected, resume condition stated in the Maintenance Log), `Completed` (outcome reached or deliberately closed), `Idea` (not yet started), `Superseded` (replaced by another note, linked). Mark a Project Paused or Completed rather than leaving it Active without activity.

A Project must have an end condition you could tick off: an outcome that is reached, delivered, submitted or decided. An outcome that reads as maintaining or establishing something ongoing belongs to a Responsibility; split its finite deliverables into Projects. Name a Project as you would say it aloud, in two to five words, and keep the filename stem matching the name.

## Compact front-page contract

- For an established Project, target 600–1,200 words; a complex umbrella may reach about 1,500. A new or simple Project can be much shorter. Do not pad it to meet a word target.
- `Current State` contains current truth only: normally no more than five bullets or 250 words.
- `Next Actions` contains 3–7 outcome-level actions. Keep microtasks in the active chat or task system.
- `Open Questions` and `Important Notes` normally contain 3–7 prioritized links each.
- `Maintenance Log` keeps the latest 3–5 meaningful milestones. Git carries routine edit history.
- Replace or reconcile old synthesis when work changes; do not append another dated mini-report.
- Keep each fact in one canonical durable note and link to it from the Project.
- Compactness is subordinate to preservation. A long Project may be a justified temporary state when unique durable details have not yet been routed safely.

Project frontmatter is navigational, not exhaustive. Child notes normally link back with `belongs_to`; use Project `has` only for active subprojects and high-value entry points. Active Projects may have a 3–5-note human view following [[procedures/maintain-project-human-view|Maintain Project Human View]] when a saved-view workbench adds value. Some active Projects may not benefit from a human view; `Project view: false` can record an explicit opt-out, but it is not required merely because no view exists.

Before removing a Project `has` value or body entry-point link, verify that the target remains findable through its own relationships, another hub or Project link, a saved view, backlinks, or an explicit Inbox/archive convention.

## Umbrellas and subprojects

Create a child Project when a work package has its own outcome, state, actions, collaborators, artifacts, or publication trajectory. The umbrella keeps shared context and a selective subproject list; it does not repeat child details. Use `belongs_to` from child to umbrella and point project workspaces to the most specific active entry note.

A Project belongs to the Responsibility or umbrella Project that will resume it, never to a Topic. Keep one primary `belongs_to`; declare two parents only for a Project genuinely co-owned across two trees, mark that note with `accepted_double_parent: true` so the lint hierarchy audit reports it as deliberate, and put the second context of other notes in `related_to`. A `has` link is an entry point, never a child's only link: the child's own `belongs_to` must reach a hub. See [[adr/0011-root-belongs-to-at-responsibilities-and-home-exploration-clusters-in-topics|ADR 0011]].

## Workspace promotion

A Project note does not imply a matching filesystem folder, repository, or agent-application project. Follow [[procedures/route-project-work-and-artifacts|Route Project Work And Artifacts]]. Promote to a dedicated workspace only for durable technical artifacts, specialized local requirements, persistent execution, collaboration, or an artifact set that has outgrown the deployment's cloud `Working/` convention. Never create an `AGENTS.md`-only folder as the default representation of a Project.

## Template

### Minimal starter

Replace the owning Responsibility and the example text. A few useful lines are enough to begin:

```md
---
type: Project
status: Active
belongs_to: "[[owning-responsibility]]"
_organized: true
---

# Prepare workshop

## Outcome

Deliver a workshop that helps the audience practise the chosen topic.

## Current State

- The audience and date are known; the exercises remain to be chosen.

## Next Actions

- [ ] Choose one useful reference and draft the first exercise.
```

Link saved references or ideas from the Project when they exist. Add sections as the work needs them.

### Expanded template

For a project with more context, use the sections below and omit empty or misleading ones.

```md
---
type: Project
status: Active
belongs_to: "[[owning-responsibility]]"
_organized: true
---

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
