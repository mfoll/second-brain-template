---
type: Procedure
status: Active
Belongs to: "[[vault]]"
_organized: true
---

# Ingest Source

Use this procedure when the user asks to save, ingest, process, extract from, or summarize external material such as a webpage, repository, paper, PDF, dataset, transcript, documentation page, tool, tutorial, or pasted source text.

Do not use `type: Source` for ordinary internal planning once the useful conclusions have already been synthesized. Update the relevant Project, Question, Concept, Procedure, ADR, or Note instead.

## Goal

Create a traceable Source note, preserve provenance, extract only useful durable knowledge, link the source into the vault without over-atomizing it, and give advisory feedback about what the ingestion surfaced.

## Steps

1. Confirm the source input: URL, file path, pasted text, repository, document, or attachment.
2. Read enough of the source to identify title, author or owner when available, date or access date, source type, and why it matters.
3. Search the vault for likely Projects, Responsibilities, Topics, Concepts, Opinions, Questions, Procedures, ADRs, and existing Source notes before creating a new note.
4. Create one `type: Source` note with a kebab-case filename and a clear H1 matching the source title or repository/tool name.
5. Add provenance frontmatter such as `url`, `source_file`, `source_type`, `author`, `date_published`, or `date_accessed` when available. Do not invent missing metadata.
6. Add only strong relationships. Use `Belongs to` when the source belongs to a project or collection; use `Related to` for concepts, questions, topics, tools, or methods; use `Has` only for selected child notes or deliverables.
7. Write concise sections: `## Summary`, `## Why It Matters`, `## Key Details`, `## Caveats`, and `## Links Or Follow-Up` when relevant. For long sources, summaries are acceptable; preserve provenance and enough retrieval hooks to return to the source rather than duplicating every detail.
8. Extract separate typed notes only when the user asks, when a point is clearly central to an active project, or when the source changes an existing durable decision, workflow, question, next action, or project-level understanding. Common extractions are Concepts, Questions, Procedures, ADRs, Responsibilities, or Project updates, but use the vault's current Type notes as the routing set. Do not create exhaustive derived notes from long sources by default.
9. Compare the source against relevant `Opinion` notes. Treat Opinions as working stances, not dogma: note whether the source supports, weakens, contradicts, depends on, or should prompt revision of an Opinion.
10. Run the bounded propagation pass below when the source changes durable understanding, evidence, caveats, open questions, active workflows, opinions, or next actions.
11. If the source cannot be confidently scoped, leave it unprocessed or mark `_organized: false` rather than forcing weak links.
12. Prepare advisory ingestion feedback using the standard below.
13. Review the diff and report created notes, updated notes, caveats, and unresolved placement questions.

## Propagation Pass

Propagation means updating the few existing synthesis notes whose current understanding should change because of the source. It is not a global cascade and it should not create exhaustive backlinks.

Use this pass when the source affects a durable note that the user or an agent is likely to revisit. Decide target notes from the vault's current Type notes and the source's actual impact rather than from a fixed list of categories.

Default process:

1. Identify candidate target notes from the relationships and searches already performed during ingestion.
2. Edit only direct, high-confidence targets. About 3-5 target notes is a useful default cap for ordinary ingestion.
3. Prefer synthesis surfaces over raw link growth. Use the current Type set as the routing map; common examples include:
   - Project notes: update Current State, Next Actions, Open Questions, Important Notes, Active Workflows, or Maintenance Log.
   - Question notes: update Current Answer, Open Threads, Signals To Revisit, or status when the answer is genuinely settled.
   - Concept notes: add or refine reusable distinctions, methods, terms, or models.
   - Procedure notes: update repeatable workflow steps only when the source improves the current procedure.
   - Opinion notes: record whether the source supports, weakens, contradicts, or refines the working stance.
   - ADRs: update only by creating or linking a new decision when the source changes a durable architecture or workflow choice.
   - Future Types: use any newer Type note when it fits the source's durable implication better than the examples above.
4. Preserve provenance by linking back to the Source note or citing the source URL/file in the edited note when the claim depends on that source.
5. If wider effects are plausible but not obvious, add a focused follow-up or leave them for [[procedures/review-vault-health|Review Vault Health]].
6. When useful, include a short `## Propagated Updates` section in the Source note listing which notes were changed and which likely targets were intentionally left unchanged.

## Ingestion Feedback

Every source ingestion should tell the user what the agent noticed. This is a feedback layer, not an approval gate.

Include concise feedback in the final response or automation report:

- what is actually new, useful, surprising, weak, duplicate, or not worth saving;
- how the source maps to existing Projects, Questions, Concepts, Procedures, ADRs, Responsibilities, or user priorities;
- how the source relates to relevant Opinions, including whether it supports, weakens, contradicts, depends on, or should update one;
- which questions the source contains or raises;
- which questions the agent answered during ingestion;
- which durable questions, next actions, or synthesis updates were created or changed;
- which propagation updates were made, deferred, or intentionally skipped;
- which Opinions may need to be created, revised, superseded, or explicitly left unchanged;
- which optional discussion points the user may want to revisit.

Do not block ordinary ingestion just because the user might want to discuss the feedback. If the source is processable, save it, make the useful linked updates, commit, and push according to the normal checkpoint rules.

Stop and ask before completing ingestion only when the missing answer is required to avoid misrouting, privacy leakage, destructive edits, broad structural changes, or another unsafe outcome.

When the source contains questions:

- Answer what can be answered from the source plus relevant vault context.
- Create or update durable `Question` notes when the question should remain findable.
- Leave optional discussion prompts in the user-facing feedback instead of blocking ingestion.
- Use `## Ingestion Questions` on the original intake note only when user input is required before the material can be safely or coherently processed.

## Source Note Minimum

A usable Source note includes:

- `type: Source` frontmatter;
- a first H1;
- provenance sufficient to re-check the source;
- a short summary in the vault owner's words;
- at least one clear retrieval path or an explicit unprocessed state.
- `_organized: true` when the Source has a clear retrieval path, or `_organized: false` only when placement is still unresolved.


## Guardrails

- Keep edits scoped to the user's request and the relevant Project or Source.
- Use `Belongs to`, `Related to`, and `Has` for relationships.
- Do not add secrets, credentials, local cache paths, generated dumps, or machine-specific setup details unless the note is explicitly about that local setup.
- Ask before creating new Types, broad relationship rewrites, mass moves, deletions, or public/private visibility changes.
