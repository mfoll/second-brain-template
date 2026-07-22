---
type: Guide
related_to: "[[vault]]"
_organized: true
surface_for:
  - "[[vault]]"
---

# Tolaria Callouts

Tolaria renders Obsidian-style callouts in ordinary Markdown. Use them as a selective visual layer inside a note, while keeping headings, frontmatter, Type semantics, wikilinks, and Git-friendly text as the durable structure.

Source: [Tolaria](https://tolaria.md/)

## Syntax

```md
> [!warning]
> This claim should not be used without appropriate validation.
```

The verified portable form is exactly one compact prose block: the marker, followed immediately by one quoted content line. Do not insert a standalone `>` spacer, use `> <br>`, add a second prose line, or wrap a list, table, or fenced block. Tolaria may detach those blocks from the callout header.

Keep the single quoted content line at or below 900 characters. If the section needs more content or structure, leave it as ordinary Markdown rather than rewriting it to fit a callout.

For a longer section, it is safe to call out only its first compact prose paragraph and leave the following paragraphs or lists as ordinary Markdown. Use this when that opening paragraph genuinely provides the section's decision, answer, definition, recommendation, or orientation; do not force every section to have a callout.

The supported types are `note`, `abstract`, `info`, `todo`, `tip`, `success`, `question`, `warning`, `failure`, `danger`, `bug`, and `example`.

## Semantic Use

| Type | Suggested use |
| --- | --- |
| `note` | A decision or context worth distinguishing from surrounding prose. |
| `abstract` | A short summary or at-a-glance orientation. |
| `info` | Current state, working meaning, stance, or provisional answer. |
| `todo` | One bounded explicit next action. |
| `tip` | A practical recommendation or preferred method pattern. |
| `success` | A confirmed successful result or completed outcome. |
| `question` | One open question, revisit signal, or condition that could change a stance. |
| `warning` | A caveat, limitation, risk, known pitfall, or important guardrail. |
| `failure` | A confirmed failed attempt whose failure is itself useful evidence. |
| `danger` | A true stop condition, prohibition, or high-consequence unsafe action. |
| `bug` | A reproducible defect, not a general limitation or open question. |
| `example` | A bounded worked example or illustrative case. |

## Restraint Rules

- Keep the section heading. A callout emphasizes content inside the section; it does not replace the table-of-contents structure.
- Prefer zero to three callouts in an ordinary synthesis note. A fourth should be rare and reserved for a compact dashboard-like Project surface or four clearly distinct semantic blocks.
- Keep lists, checkboxes, multiple paragraphs, long evidence, transcripts, detailed extraction, tables, code, and multi-part analysis outside callouts.
- Leave an otherwise suitable section unstyled when its single prose block would exceed the 900-character source-line limit.
- In a longer section, stop the callout after the first compact prose paragraph. Do not pull subsequent block structure into it.
- Do not use color as the only durable signal. Status, ownership, lifecycle, provenance, and relationships remain explicit in frontmatter and prose.
- Do not manufacture `success`, `failure`, `danger`, or `bug` merely for visual variety. Use them only when the content actually has that meaning.
- Links and inline code are fine inside the single prose line. All block-level structure stays outside the callout.
