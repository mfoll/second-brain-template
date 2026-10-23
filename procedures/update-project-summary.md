---
type: Procedure
status: Active
belongs_to: "[[vault]]"
related_to:
  - "[[procedures/maintain-project-human-view|Maintain Project Human View]]"
  - "[[procedures/update-project-next-actions|Update Project Next Actions]]"
_organized: true
---

# Update Project Summary

Use this procedure after significant project work, ingestion, or a direct request would otherwise leave the Project entry note stale.

## Contract

Follow [[project]]: 600–1,200 words by default, up to about 1,500 for a complex umbrella; no more than roughly five Current State bullets or 250 words; 3–7 actions; 3–7 prioritized Questions and Important Notes; and 3–5 meaningful milestones.

The Project is current synthesis, not an archive. Replace superseded text instead of appending another dated report. Keep each fact in one canonical linked note; use Git for routine chronology.

The same applies to any agent writeback into a Project, Responsibility, Topic or Guide: update the section that owns each fact rather than appending to the note. Never add a dated `##` section such as "Follow-up, October 2026", and never write below `## Maintenance Log`; a dated occurrence with lasting value goes to its Event, linked from a compact bullet in the owning section. Add at most one Maintenance Log entry per change.

Compactness targets never authorize information loss. Before shortening a Project, make a preservation ledger for every section or block that may disappear. Classify it as:

- retained in the Project because it is required for resumption;
- moved to a named canonical note that has been inspected and updated in the same change;
- already duplicated in a named canonical note whose payload has been verified, not merely inferred from its title;
- obsolete or contradicted, with the superseding fact identified;
- routine edit history that Git can safely carry.

Exact decisions, parameters, provenance, caveats, rejected options, approvals, external-system state, identifiers, named handoffs, and revisit triggers are not routine history. Do not delete or reduce them to a lossy summary unless their complete future-use value is preserved in a verified durable destination. If no suitable destination exists, create or propose one, or leave the Project above its target and report the justified exception.

## Steps

1. Read frontmatter, H1, opening summary, and headings; open only the sections and linked notes needed for the change.
2. Check relationships, backlinks, and the current human view for relevant context.
3. Refresh the affected sections: Outcome, Current State, Scope and Boundaries, project-specific working context, Active Workflows, Next Actions, Open Questions, Important Notes, optional Do Not Do Yet, and Maintenance Log.
4. Build the preservation ledger before removing anything. Inspect each proposed destination and record the exact target note for moved or already-duplicated material.
5. Remove stale or duplicated synthesis only after the ledger proves where its future-use value remains. Route detailed evidence, chronology, reusable knowledge, consequential uncertainty, repeatable workflows, and decisions to the appropriate existing Type.
6. Update directly affected typed notes only when the implication is high-confidence. Preserve provenance and uncertainty; defer broad cascades.
7. Reconcile Next Actions through [[procedures/update-project-next-actions|Update Project Next Actions]].
8. Run the Project Surface Check in [[procedures/maintain-project-human-view|Maintain Project Human View]] when the notes a human should open next changed.
9. Review the diff against the preservation ledger. Verify that every removed durable detail is present in its stated destination and that every new link resolves before checkpointing.

## Output standard

A returning human or agent should be able to identify the outcome, current state, boundaries, blockers, next actions, open decisions, and best notes to open within a few minutes.
