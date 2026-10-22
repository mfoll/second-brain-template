---
type: ADR
status: Accepted
belongs_to: "[[vault]]"
related_to:
  - "[[source]]"
  - "[[procedures/ingest-source|Ingest Source]]"
  - "[[source-note-vs-synthesis-note]]"
_organized: true
---

# ADR 0005: Use Source as the Single External Ingestion Type

## Context

An earlier vault design had both `Source` and `Resource` Types. The intended distinction was that sources were evidence-bearing items, while resources were useful external references or tools.

In practice the distinction is too subtle for an ingestion workflow. A webpage, repository, paper, dataset or tool can all be a source of information once it is ingested and interpreted.

## Decision

> [!note]
> Use `Source` as the single Type for externally ingested material: papers, PDFs, datasets, documents, webpages, repositories, tools, tutorials, videos, transcripts and reports.

There is no separate `Resource` Type. Distinguish source kinds with fields such as `source_type`, `url`, `source_file`, citation metadata, and the note body.

## Consequences

The ingestion workflow is simpler and [[procedures/ingest-source|Ingest Source]] has one default note Type. Agents no longer need to decide between `Source` and `Resource`.

If a vault later needs a visible distinction between evidence sources and lightweight bookmarks, a future ADR can introduce a new Type or property.

## Revisit When

> [!question]
> Revisit if the vault accumulates many external notes that are only bookmarks and do not require extraction, provenance or synthesis.

## Provenance

Ported on 2026-10-22 from the maintainer's work/control vault, ADR 0008 *Use Source as the Single External Ingestion Type* (2026-04-30); work-specific names and examples were replaced by generic wording.
