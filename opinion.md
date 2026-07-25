---
type: Type
_icon: chat-dots
_color: "#ec4899"
_order: 11
_organized: true
---

# Opinion

An Opinion is the user's current working stance on a specific topic, method, claim, tool, preference, or direction.

Use Opinion notes for judgments that should remain retrievable as the user's own interpretation, not as external evidence, neutral concept notes, open questions, or operational decisions.

## How Agents Should Use Opinions

Relevant Opinion notes should be retrieved and considered during source ingestion, document review, writing, planning, briefings, interviews, and other agentic workflows where the stance could affect interpretation or recommendations.

Opinions are working stances, not dogma. Agents should use them as user context, but they may challenge them when new evidence, better reasoning, or changed circumstances warrant it. When a source or task supports, weakens, contradicts, or depends on an Opinion, the agent should say so explicitly.

Agents should not inject every Opinion into every task. Retrieve Opinion notes only when the topic, project, source, or user request makes them relevant.

When appropriate, agents should ask whether an Opinion should be created, revised, superseded, or left unchanged, especially when the task touches the note's `## What Would Change My Mind` section.

## Recommended Sections

- `## Stance`: the opinion in direct language.
- `## Scope`: where the opinion applies and where it may not.
- `## Why I Think This`: reasons, evidence, experience, or source links behind the stance.
- `## What Would Change My Mind`: observations, evidence, or context that should revise the stance.
- `## Implications`: practical consequences for reading, deciding, organizing, or working.

## Suggested Metadata

Opinion notes may use `status` and `confidence` when useful.

Recommended `status` values are `Active`, `Revising`, `Superseded`, and `Archived`.

Recommended `confidence` values are `Low`, `Medium`, and `High`.
