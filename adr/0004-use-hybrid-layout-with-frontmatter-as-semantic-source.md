---
type: ADR
status: Accepted
belongs_to: "[[vault]]"
related_to:
  - "[[tolaria-saved-views|Tolaria Saved Views]]"
_organized: true
---

# ADR 0004: Use Hybrid Layout with Frontmatter as Semantic Source

## Context

The viewer can scan subfolders, but its semantic model comes from Markdown frontmatter and wikilinks. The starter vault keeps Type definitions at the root while saved views live in `views/`.

## Decision

> [!note]
> Use a hybrid layout. Keep core notes and Type definitions at the vault root, place ADRs in `adr/`, Procedures in `procedures/`, views in `views/`, and any raw material in a dedicated folder the deployment chooses. Treat frontmatter relationships as the source of meaning, not folder location.

## Consequences

The vault remains simple to browse while allowing operational documents to be grouped. Moving files later does not change their semantic meaning if frontmatter relationships are maintained. Root links use filename stems and folder notes use vault-relative path stems.

## Revisit When

> [!question]
> Revisit if the viewer's recommended Type-file layout changes, or if folder organization starts improving retrieval more than flat root navigation.

## Provenance

Ported on 2026-10-22 from the maintainer's work/control vault, ADR 0005 *Use Hybrid Layout with Frontmatter as Semantic Source* (2026-04-30); work-specific names and examples were replaced by generic wording.
