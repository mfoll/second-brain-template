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

Create a traceable Source note, preserve provenance, extract only useful durable knowledge, and link the source into the vault without over-atomizing it.

## Steps

1. Confirm the source input: URL, file path, pasted text, repository, document, or attachment.
2. Read enough of the source to identify title, author or owner when available, date or access date, source type, and why it matters.
3. Search the vault for likely Projects, Responsibilities, Topics, Concepts, Questions, Procedures, ADRs, and existing Source notes before creating a new note.
4. Create one `type: Source` note with a kebab-case filename and a clear H1 matching the source title or repository/tool name.
5. Add provenance frontmatter such as `url`, `source_file`, `source_type`, `author`, `date_published`, or `date_accessed` when available. Do not invent missing metadata.
6. Add only strong relationships. Use `Belongs to` when the source belongs to a project or collection; use `Related to` for concepts, questions, topics, tools, or methods; use `Has` only for selected child notes or deliverables.
7. Write concise sections: `## Summary`, `## Why It Matters`, `## Key Details`, `## Caveats`, and `## Links Or Follow-Up` when relevant.
8. Extract separate typed notes only when they improve future retrieval. Common extractions are Concepts, Questions, Procedures, ADRs, Responsibilities, or Project updates.
9. If the source changes an active Project's understanding, update that Project's summary or next actions using the matching procedure.
10. If the source cannot be confidently scoped, leave it unprocessed or mark `_organized: false` rather than forcing weak links.
11. Review the diff and report created notes, updated notes, caveats, and unresolved placement questions.

## Source Note Minimum

A usable Source note has:

- `type: Source` frontmatter;
- a first H1;
- provenance sufficient to re-check the source;
- a short summary in the vault owner's words;
- at least one clear retrieval path or an explicit unprocessed state.


## Guardrails

- Keep edits scoped to the user's request and the relevant Project or Source.
- Use `Belongs to`, `Related to`, and `Has` for relationships.
- Do not add secrets, credentials, local cache paths, generated dumps, or machine-specific setup details unless the note is explicitly about that local setup.
- Ask before creating new Types, broad relationship rewrites, mass moves, deletions, or public/private visibility changes.
