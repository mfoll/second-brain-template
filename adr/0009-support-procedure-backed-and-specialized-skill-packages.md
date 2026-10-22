---
type: ADR
status: Accepted
belongs_to: "[[vault]]"
related_to:
  - "[[agent-skill]]"
  - "[[skill]]"
  - "[[procedures/configure-agent-skill-discovery|Configure Agent Skill Discovery]]"
_organized: true
---

# ADR 0009: Support Procedure-Backed and Specialized Skill Packages

## Context

A mature vault accumulates two kinds of Skill note/package pairs. Some are Procedure-backed: mostly thin wrappers, with a few fuller hybrid adapters that carry substantial operational detail. Others are specialized scientific, archive, extraction, document-review or agent-operation packages that already contain their executable workflows and have no matching Procedure. Earlier guidance stated that every Skill activates a Procedure and requires `wraps`, which no longer matched such a vault.

Creating artificial Procedures for every specialized package would duplicate mature package instructions without improving retrieval. Treating the packages as undocumented exceptions would leave agents and lint unable to distinguish intentional standalone ownership from drift.

## Decision

> [!note]
> Keep vault-owned packages under `.agents/skills/`, with machine-local exposure installed or symlinked only during explicit setup; prefer symlinks over copied packages. Keep one visible `type: Skill` catalogue note and one executable package for every installed vault-owned Skill. The catalogue note owns lifecycle and graph visibility; the package owns executable files and must match the note's purpose.

Support two explicit modes without adding frontmatter fields:

1. A Procedure-backed Skill has `wraps` and names and requires the same full Procedure in `SKILL.md`. The Procedure is authoritative on conflict. The package may retain operational detail; prefer thinness only after a clause audit proves that no trigger, prerequisite, hard safety or runtime guard, command or bundled-resource instruction will be lost.
2. A specialized standalone Skill omits `wraps`, states in its visible note that the package owns execution, and keeps the complete executable workflow in `SKILL.md`. Use this mode only when no durable Procedure already owns the workflow.

Retirement removes the installed package and archives or removes the catalogue note and active routes in the same change. An archived note does not make an installed package dormant.

A deployed vault whose packages are all Procedure-backed may keep its [[skill]] contract stricter than this ADR; the standalone mode becomes available there only after that Type note is updated.

## Consequences

Agents can tell which detail must be read: Procedure-backed tasks require both package and Procedure; standalone tasks require the package. Lint can validate real ownership without demanding fictitious Procedures. The catalogue remains browsable without duplicating package bodies.

## Revisit When

> [!question]
> Revisit if the Agent Skills format gains a standard lifecycle or workflow-owner field, if standalone packages accumulate reusable cross-agent knowledge that belongs in Procedures, or if a plugin or package registry replaces vault-owned Skill pairs.

## Provenance

Ported on 2026-10-22 from the maintainer's work/control vault, ADR 0022 *Support Procedure-Backed and Specialized Skill Packages* (2026-07-11); work-specific names and examples were replaced by generic wording.
