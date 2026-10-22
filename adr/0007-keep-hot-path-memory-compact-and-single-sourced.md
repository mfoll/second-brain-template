---
type: ADR
status: Accepted
belongs_to: "[[vault]]"
related_to:
  - "[[project]]"
  - "[[global-agent-instructions-template]]"
  - "[[procedures/update-project-summary|Update Project Summary]]"
_organized: true
---

# ADR 0007: Keep Hot-Path Memory Compact And Single-Sourced

## Context

A vault's graph, Types, provenance, project views and Git history work well, but automatically and routinely read surfaces accumulate duplicated policy, chronology and backlogs. In the originating deployment, global plus vault instructions cost roughly 13,700 estimated tokens before project context, and active Project notes had a median above 3,000 words, with most prose concentrated in Current State, Next Actions and Maintenance Log.

The problem was not total vault size. Most Sources, Concepts, Questions and other selectively retrieved notes were reasonably compact. The cost came from hot-path notes that every task had to read.

## Decision

> [!note]
> Adopt a compact-front-page and linked-detail model:

- Global instructions contain only machine-local routing, cross-context preferences and authorization rules, with one executable source per machine.
- Vault `AGENTS.md` is a constitution and workflow router, not a duplicated manual.
- Ordinary project pointers contain only the logical vault role, one entry note and a missing-root guard.
- Type notes and Procedures own detailed semantics, syntax, templates and workflows; Procedure-wrapper Skills stay thin.
- Active Project notes target 600–1,200 words, with about 1,500 allowed for complex umbrellas. They keep current synthesis, 3–7 actions, prioritized links and only recent meaningful milestones.
- New work replaces or reconciles synthesis instead of appending chronology. Each durable fact has one canonical home; Projects link to detailed Sources, Events, Concepts, Questions, Opinions, Procedures or ADRs. Git carries routine edit history.
- Agents read progressively: identity and opening summary first, relevant sections next, full long notes only when complete evidence is needed.
- Long evidence notes may remain detailed. Compactness checks are Type-aware warnings, not blanket deletion rules.

Local commits may accompany authorized vault edits. Network push remains separately authorized by the deployment's explicit wording, recognized shortcut, approved publication flow or narrowly scoped automation.

## Consequences

Project resumption becomes faster for humans and agents, and instruction changes have one executable source. Some historical duplication is removed from live front pages, but unique facts and decisions remain in linked notes or Git. Existing Types, relationship keys, wikilinks and saved-view behaviour do not change.

Compactness becomes an ongoing maintenance concern. Lint and health review report hot-path drift, while Project update and ingestion workflows prevent append-only growth.

## Revisit When

- Retrieval tests show that compact entry notes routinely omit context that cannot be recovered within one or two links.
- A future agent runtime can load structured sections without paying for full instruction or Project files.
- The 600–1,200-word Project target repeatedly proves too small for a well-defined class of active work.
- A different instruction-distribution mechanism provides a clearer executable source without duplicating policy.

## Provenance

Ported on 2026-10-22 from the maintainer's work/control vault, ADR 0020 *Keep Hot-Path Memory Compact And Single-Sourced* (2026-07-09); work-specific names and examples were replaced by generic wording.
