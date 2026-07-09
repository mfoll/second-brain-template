---
type: Type
_icon: hand
_color: "#eab308"
_order: 1
_organized: true
---

# Question

A Question records an unresolved issue, uncertainty, or research direction that should remain findable.

About 750 words is a review threshold, not a hard cap. When a Current Answer or evidence review becomes maintained synthesis, move it to an appropriate Concept, Opinion, ADR, Project, Source, or other suitable Type and leave the Question as a concise pointer to what remains unresolved.

## Creation Standard

Create a Question only when the unresolved issue should remain findable and has a plausible future use: it is consequential, likely to recur, decision-driving, expected to guide active work, or needed as a retrieval anchor.

Do not create Question notes for rhetorical prompts, curiosity-only points, optional discussion prompts, questions answerable from the current source plus relevant context, or issues with no plausible owner or future path to answer. During ingestion and Inbox processing, prefer answering question-shaped material first, then update the relevant Source, Project, Concept, Procedure, ADR, Opinion, or existing Question only when the answer changes durable understanding.

Normal ingestion should create zero new Question notes by default. If an ingestion creates one or two, the final report should state why they are worth maintaining. More than that usually means the source needs synthesis or advisory feedback rather than a batch of new open Questions.

## Status Lifecycle

Recommended Question statuses:

- `Open`: unresolved, provisional, still being tested, or still driving active project planning.
- `Answered`: the current answer is accepted as the working policy and has been reflected in the relevant Project, Concept, Procedure, ADR, or other durable note when needed.
- `Deferred`: valid but not active; revisit only if the related project or context changes.
- `Superseded`: replaced by a better Question, ADR, Procedure, Project direction, Concept, or other durable note.

A `## Current Answer` does not automatically make a Question `Answered`.
