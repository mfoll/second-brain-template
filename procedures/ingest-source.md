---
type: Procedure
status: Active
belongs_to: "[[vault]]"
related_to:
  - "[[procedures/maintain-project-human-view|Maintain Project Human View]]"
_organized: true
---

# Ingest Source

Use this procedure when the user asks to save, ingest, process, extract from, or summarize external material such as a webpage, repository, paper, PDF, dataset, transcript, documentation page, tool, tutorial, or pasted source text.

Do not use `type: Source` for ordinary internal planning once the useful conclusions have already been synthesized. Update the relevant Project, Question, Concept, Procedure, ADR, or Note instead.

## Goal

Create a traceable Source note, preserve provenance, extract only useful durable knowledge, link the source into the vault without over-atomizing it, think through how the source can be used in future work or decisions, and give advisory feedback about what the ingestion surfaced.

## Steps

1. Confirm the source input: URL, file path, pasted text, repository, document, or attachment.
2. Read enough of the source to identify title, author or owner when available, date or access date, source type, and why it matters.
3. Search the vault for likely Projects, Responsibilities, Topics, Concepts, Opinions, Questions, Procedures, ADRs, and existing Source notes before creating a new note.
4. Create one `type: Source` note with a kebab-case filename and a clear H1 matching the source title or repository/tool name.
5. Add provenance frontmatter such as `url`, `source_file`, `source_type`, `author`, `date_published`, or `date_accessed` when available. Do not invent missing metadata.
6. Add only strong relationships. Use `belongs_to` for the Project or Responsibility that would resume or answer for the source; use `related_to` for concepts, questions, topics, tools, or methods; use `has` only for selected child notes or deliverables. Every durable note needs a `belongs_to` that reaches a Responsibility. If no Project or Responsibility owns the source yet, file it under the matching exploration Topic of the Responsibility the deployment designates for exploratory reading; creating a new cluster Topic there needs no separate approval once at least three notes share the theme. Never leave a durable note attached by `related_to` alone; when the deployment designates no exploration Responsibility, leave the note unprocessed under step 13 instead ([[adr/0011-root-belongs-to-at-responsibilities-and-home-exploration-clusters-in-topics|ADR 0011]]).
7. Write concise sections: `## Summary`, `## Why It Matters`, `## Key Details`, `## Caveats`, and `## Links Or Follow-Up` when relevant. For long sources, summaries are acceptable; preserve provenance and enough retrieval hooks to return to the source rather than duplicating every detail. If provenance fields such as `url`, `urls`, `source_file`, DOI, repository, `root_key`, or `relative_path` are present in frontmatter, also include the useful pointer in the readable body, usually as `## Source Links` or `## Source Location`.
8. Extract separate typed notes only when the user asks, when a point is clearly central to an active project, or when the source changes an existing durable decision, workflow, question, next action, or project-level understanding. Common extractions are Concepts, Questions, Procedures, ADRs, Responsibilities, or Project updates, but use the vault's current Type notes as the routing set. Do not create exhaustive derived notes from long sources by default. For question-shaped material, use the answer-first standard below before creating or updating a `Question` note.
9. Compare the source against relevant `Opinion` notes. Treat Opinions as working stances, not dogma: note whether the source supports, weakens, contradicts, depends on, or should prompt revision of an Opinion.
10. Run the Application To Future Use pass below when the source is likely to influence future projects, responsibilities, decisions, writing, planning, recurring workflows, or durable opinions.
11. Run the bounded propagation pass below when the source changes durable understanding, evidence, caveats, open questions, active workflows, opinions, reusable framing, or next actions.
12. Run a Project Surface Check from [[procedures/maintain-project-human-view|Maintain Project Human View]] when the source becomes a human-meaningful project artifact or changes what belongs in the Project's saved view.
13. If the source cannot be confidently scoped, leave it unprocessed or mark `_organized: false` rather than forcing weak links.
14. Prepare advisory ingestion feedback using the standard below.
15. Review the diff and report created notes, updated notes, caveats, and unresolved placement questions.

## Application To Future Use Pass

For important sources, do not stop at provenance plus summary. Before finalizing ingestion, explicitly ask how the source could influence future projects, responsibilities, decisions, writing, planning, recurring workflows, caveats, opinions, or strategy.

This pass is required when the source is clearly consequential for an active project or responsibility. Skip it only when the source is peripheral, duplicate, or being saved only as raw provenance.

Default process:

1. Identify the few active Projects, Responsibilities, Concepts, Opinions, Questions, Procedures, or Source collections that the source could realistically affect.
2. Decide whether the source supports, weakens, refines, contradicts, or creates a working stance, reusable argument, caveat, project angle, decision input, or future action idea.
3. Add a `## What This Could Be Useful For` section to the Source note when the source has plausible future uses beyond archival provenance.
4. Capture reusable framing or wording candidates in the Source note when they may help future writing or decision-making, while keeping the section descriptive and source-anchored rather than turning the Source into synthesis.
5. Apply high-confidence updates directly through the Propagation Pass, normally capped at about 3-5 target notes for ordinary ingestion.
6. For plausible but broader, speculative, or cross-project uses, record a short proposed propagation list for user validation instead of silently editing many notes.

## Propagation Pass

Propagation means updating the few existing synthesis notes whose current understanding should change because of the source. It is not a global cascade and it should not create exhaustive backlinks.

Use this pass when the source affects a durable note that the user or an agent is likely to revisit. Decide target notes from the vault's current Type notes, the Application To Future Use pass, and the source's actual impact rather than from a fixed list of categories.

Default process:

1. Identify candidate target notes from the relationships and searches already performed during ingestion.
2. Edit only direct, high-confidence targets. About 3-5 target notes is a useful default cap for ordinary ingestion.
3. Before changing a Project, read its existing synthesis and reconcile it in place. Replace stale or duplicate statements; do not append another dated mini-report. Keep only the source's current project implication and a link, while detailed evidence and chronology remain in the Source, an appropriate Event or Method, or Git history.
4. Prefer synthesis surfaces over raw link growth. Use the current Type set as the routing map; common examples include:
   - Project notes: replace or reconcile Current State, Next Actions, Open Questions, Important Notes, Active Workflows, or Maintenance Log instead of accumulating parallel updates.
   - Project human views: add or remove `surface_for` only when the source changes the small set of notes the user should open.
   - Question notes: update Current Answer, Open Threads, Signals To Revisit, or status when the answer is genuinely settled.
   - Concept notes: add or refine reusable distinctions, methods, terms, or models.
   - Procedure notes: update repeatable workflow steps only when the source improves the current procedure.
   - Opinion notes: record whether the source supports, weakens, contradicts, or refines the working stance.
   - ADRs: update only by creating or linking a new decision when the source changes a durable architecture or workflow choice.
   - Future Types: use any newer Type note when it fits the source's durable implication better than the examples above.
5. Preserve provenance by linking back to the Source note or citing the source URL/file in the edited note when the claim depends on that source.
6. If wider effects are plausible but not obvious, add a focused follow-up or leave them for [[procedures/review-vault-health|Review Vault Health]].
7. When useful, include a short `## Propagated Updates` section in the Source note listing which notes were changed and which likely targets were intentionally left unchanged.
8. When useful, include a short `## Proposed Propagation For Validation` section for broader implications that may matter for future use but are not high-confidence enough for direct editing.

## Answer-First Question Handling

Question-shaped material is not automatically a durable `Question` note. During ingestion, classify each question or uncertainty before writing it into the graph:

- `Resolved now`: answer it from the source plus relevant vault context, state the answer in the ingestion feedback, and update the relevant Source, Project, Concept, Procedure, ADR, Opinion, or existing Question only when that answer changes durable understanding.
- `Durable open issue`: create or update a `Question` note only when the issue is consequential, likely to recur, decision-driving, expected to guide active work, or needed as a future retrieval anchor.
- `Optional discussion point`: mention it in the user-facing feedback, but do not create a durable note.
- `True blocker`: use `## Ingestion Questions` on the original intake note only when user input is required before safe routing, privacy handling, destructive edits, structural changes, or coherent processing can continue.

Normal ingestion should create zero new `Question` notes by default. Creating one or two is reasonable when the durable-use rationale is clear; creating more should be called out in the final report with the reason they are worth maintaining.

## Ingestion Feedback

Every source ingestion should tell the user what the agent noticed. This is a feedback layer, not an approval gate.

Include concise feedback in the final response or automation report:

- what is actually new, useful, surprising, weak, duplicate, or not worth saving;
- how the source maps to existing Projects, Questions, Concepts, Procedures, ADRs, Responsibilities, or user priorities;
- how the source relates to relevant Opinions, including whether it supports, weakens, contradicts, depends on, or should update one;
- which questions the source contains or raises;
- which questions the agent answered during ingestion;
- which durable questions, next actions, or synthesis updates were created or changed;
- which future-use ideas, reusable framing candidates, or future action ideas were captured;
- which propagation updates were made, deferred, or intentionally skipped;
- which proposed propagation targets need the user's validation before broader editing;
- which Opinions may need to be created, revised, superseded, or explicitly left unchanged;
- which optional discussion points the user may want to revisit.

Do not block ordinary ingestion just because the user might want to discuss the feedback. If the source is processable, save it, make the useful linked updates, commit, and push according to the normal checkpoint rules.

Stop and ask before completing ingestion only when the missing answer is required to avoid misrouting, privacy leakage, destructive edits, broad structural changes, or another unsafe outcome.

When the source contains questions:

- Answer what can be answered from the source plus relevant vault context, using explicit assumptions when needed.
- Create or update durable `Question` notes only for unresolved issues that pass the durable open issue standard above.
- Leave optional discussion prompts in the user-facing feedback instead of blocking ingestion or writing them into durable notes.
- Use `## Ingestion Questions` on the original intake note only for true blockers where user input is required before the material can be safely or coherently processed.

## Source Note Minimum

A usable Source note includes:

- `type: Source` frontmatter;
- a first H1;
- provenance sufficient to re-check the source;
- the useful source link or location repeated in the note body, not only in YAML;
- a short summary in the vault owner's words;
- at least one clear retrieval path or an explicit unprocessed state.
- `_organized: true` when the Source has a clear retrieval path, or `_organized: false` only when placement is still unresolved.


## Guardrails

- Keep edits scoped to the user's request and the relevant Project or Source.
- Use `belongs_to`, `related_to`, and `has` for relationships.
- Do not add secrets, credentials, local cache paths, generated dumps, or machine-specific setup details unless the note is explicitly about that local setup.
- Ask before creating new Types, broad relationship rewrites, mass moves, deletions, or public/private visibility changes.
