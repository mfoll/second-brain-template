---
type: ADR
status: Accepted
belongs_to: "[[vault]]"
related_to:
  - "[[adr/0007-keep-hot-path-memory-compact-and-single-sourced|ADR 0007]]"
  - "[[procedures/lint-vault|Lint Vault]]"
  - "[[upgrade-existing-vault-from-template|Upgrade an Existing Vault From the Template]]"
_organized: true
---

# ADR 0008: Require Semantic Reachability and Reversible Compaction

## Context

[[adr/0007-keep-hot-path-memory-compact-and-single-sourced|ADR 0007]] correctly identified that routinely loaded instructions and Project front pages had become too large, and a compaction migration substantially reduced that cost. A clause-by-clause preservation audit then found that some deleted rules and machine-administration facts had not reached the Type, Procedure or reference note that was supposed to own them. They remained recoverable from Git, but an agent could not know when to read them.

Mechanical checks had passed because the files were valid, links resolved and word budgets were met. Those checks did not establish semantic coverage or activation. "The detail exists somewhere" is insufficient when no reliably loaded instruction routes the task to that detail.

## Decision

> [!note]
> Keep the compact, retrieval-first architecture and add these preservation requirements:

1. A hot-path rule may move to a cold Type, Procedure, ADR or Guide only when the destination is authoritative and the hot path contains a reliable activation route. Matching Procedures must be read before acting; Type notes must be read whenever Type semantics affect selection, interpretation, lifecycle, structure or an edit.
2. Safety, authorization, privacy, evidence, lifecycle and retrieval-orientation rules take precedence over word targets. Compactness thresholds are diagnostic defaults, not deletion quotas.
3. A Project or Responsibility compaction must classify removed material as duplicated synthesis, routine Git history, private or out-of-scope content, or unique durable knowledge. Unique durable knowledge needs an explicit linked home before deletion. If privacy prevents rerouting during the migration, record the exact Git recovery point and the unresolved destination rather than copying it into the wrong vault.
4. Instruction compaction requires a clause-by-clause pre/post coverage table. Every removed clause must be classified as retained, moved with an activation route, superseded by an explicit decision, duplicated elsewhere, or intentionally retired with a reason.
5. Validation must include retrieval drills for important rules and facts, not only syntax, link, view and word-count checks. At least one drill must begin from an ordinary workspace pointer and reach a vault-routed Type or Procedure that is not linked from the Project note.
6. A structural migration must record each affected repository's pre-migration commit, final reviewed commit, rollback tag, generated-file source relationship, non-Git files and safe recovery instructions. Rollback guidance favours a new inspection branch or `git revert`, never an unreviewed destructive reset.
7. Generic interface changes are propagated deliberately, template first, through [[upgrade-existing-vault-from-template|Upgrade an Existing Vault From the Template]] and, where a routing/control vault exists, [[procedures/review-multi-vault-consistency|Review Multi-Vault Consistency]]. Interface audits may inspect another vault's rules and automation configuration, but not its content unless the user explicitly authorizes that scope.

## Consequences

The hot path remains small, but it can contain a few extra routing and safety clauses when those clauses are necessary to make cold detail reachable. Type and Procedure notes become more important and must be complete enough to serve as true sources of truth. Migrations take longer because semantic preservation and rollback evidence are reviewed explicitly.

## Revisit When

- Runtime-enforced instruction imports can guarantee that a matching Type or Procedure is loaded automatically.
- Retrieval drills show that a required cold rule still cannot be found from a normal task surface.
- Rollback metadata becomes mechanically generated and independently verified.
- The compactness defaults repeatedly force useful current synthesis out of active Projects even after duplicate history is removed.

## Provenance

Ported on 2026-10-22 from the maintainer's work/control vault, ADR 0021 *Require Semantic Reachability and Reversible Compaction* (2026-07-10); work-specific names and examples were replaced by generic wording.
