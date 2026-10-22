---
type: ADR
status: Accepted
belongs_to: "[[vault]]"
related_to:
  - "[[adr]]"
_organized: true
---

# ADR 0003: Use ADRs for Vault Design Decisions

## Context

The vault evolves as its owner learns which workflows, note Types and agent procedures work. Those decisions need durable explanations rather than being buried in chat history.

## Decision

> [!note]
> Record major vault, workflow and agent-operation decisions as ADR notes in `adr/`, following the [[adr]] Type's lifecycle: a changed decision gets a new ADR that supersedes the old one instead of a silent rewrite.

## Consequences

Agents can understand why the vault is structured a certain way. Future changes can supersede older decisions instead of silently rewriting history. Generic decisions can be ported between the template and deployed vaults with their rationale intact.

## Revisit When

> [!question]
> Revisit if ADRs become too heavy for small changes or if another decision-log format proves easier to maintain.

## Provenance

Ported on 2026-10-22 from the maintainer's work/control vault, ADR 0003 *Use ADRs for Vault Design Decisions* (2026-04-30); work-specific names and examples were replaced by generic wording.
