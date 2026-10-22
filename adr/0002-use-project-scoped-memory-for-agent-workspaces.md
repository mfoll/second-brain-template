---
type: ADR
status: Accepted
belongs_to: "[[vault]]"
related_to:
  - "[[project-scoped-memory]]"
  - "[[procedures/initialize-project-memory|Initialize Project Memory]]"
_organized: true
---

# ADR 0002: Use Project-Scoped Memory for Agent Workspaces

## Context

Agent work may happen inside specific project workspaces. Searching the whole vault by default can be noisy, but project-specific context should be easy to retrieve.

## Decision

> [!note]
> A substantive project workspace may carry a compact memory section in its existing `AGENTS.md` that names the vault role, one primary Second Brain Project note and a missing-root guard. Agents start from that Project note and its linked notes before widening search.

## Consequences

Project context becomes explicit and portable. Agents can retrieve relevant notes without relying on hidden state. Local workspace setup needs a repeatable onboarding procedure, [[procedures/initialize-project-memory|Initialize Project Memory]], and the pointer must stay a section added to existing instructions rather than a folder created to host it.

## Revisit When

> [!question]
> Revisit if project boundaries become too fluid for one primary Project note, or if agents repeatedly miss relevant cross-project context.

## Provenance

Ported on 2026-10-22 from the maintainer's work/control vault, ADR 0002 *Use Project-Scoped Memory for Agent Workspaces* (2026-04-30); work-specific names and examples were replaced by generic wording.
