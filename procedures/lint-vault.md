---
type: Procedure
status: Active
belongs_to: "[[vault]]"
related_to:
  - "[[procedures/review-vault-health|Review Vault Health]]"
  - "[[procedures/check-external-raw-references|Check External Raw References]]"
_organized: true
---

# Lint Vault

Use this procedure for read-only mechanical and structural diagnosis. Strategic ontology or usefulness questions belong in [[procedures/review-vault-health|Review Vault Health]].

## Canonical scope

Inventory tracked vault notes. Exclude `.git`, `.agents`, `.local`, attachments, caches, generated output, vendored content, and similar support trees from ordinary note counts and link resolution.

## Checks

- Missing or invalid frontmatter, H1, canonical Type, status, or required lifecycle fields.
- Broken, ambiguous, title-fallback-only, or non-portable wikilinks; orphaned or unreachable active notes.
- Relationship-key drift, duplicated aliases, invalid `surface_for`, saved-view filters using obsolete fields, and configured icons absent from Tolaria's curated registry.
- Active Projects missing useful resumption sections or a human view unless `Project view: false` is set.
- Project `has` lists or views that have become exhaustive rather than selective.
- Sources without human-visible provenance; external Source bridges missing `storage_system`, `root_key`, `relative_path`, `access`, or `last_checked`.
- ADRs, Procedures, and project pointers that violate their current contracts.
- Skill pair drift: a visible active Skill without its `package_path`, an installed package without an active catalogue note, a package-directory/`name` mismatch, a missing package-bundled relative support file, or an archived catalogue note whose package remains discoverable under `.agents/skills/`. For Procedure-backed pairs, also flag missing or divergent Procedure pointers; for standalone pairs, flag missing explicit package ownership or a duplicated existing Procedure. Treat semantic purpose or lifecycle drift as a warning unless executable behavior contradicts it; document and check external prerequisites at execution. Allow only documented runtime-only exceptions.
- Unscoped local paths, credentials, caches, or generated dumps in portable notes.

Type-aware compactness warnings:

- `AGENTS.md` above 1,200 words; ordinary workspace pointer above 80 words; specialized pointer above 300 without a real safety reason.
- Active Project above 1,500 body words; above 3,000 requires a structural split or explicit justification.
- Project Current State above 250 words, more than 10 unchecked actions, or more than five Maintenance Log entries.
- Question above 750 body words: review whether its answer or analysis belongs in maintained synthesis.
- Source, Event, or Method above 2,000 body words: preserve the payload, but require a concise opening summary rather than blanket shortening.

Compactness findings are triage signals only. Recommended follow-up must say `review and route` rather than imply blanket shortening. A focused fix must not delete unique durable content until a preservation ledger identifies and verifies a canonical destination for each removed block.

## Steps

1. Inspect Type definitions and the canonical tracked-note tree.
2. Run `.agents/skills/lint-vault/scripts/compactness_audit.py <vault-root>` for deterministic compactness warnings and `.agents/skills/lint-vault/scripts/tolaria_icon_audit.py <vault-root>` for saved-view and frontmatter icon names. Verify warned emoji or URL icons in the current Tolaria UI.
3. Verify findings against the actual files; broad search output is not proof.
4. Report errors and warnings by severity and note. Treat compactness thresholds as review signals, not arbitrary failures.
5. Stay read-only unless the user asks for focused fixes. Do not process Inbox, rewrite summaries, normalize broad relationships, or delete notes from lint.

## Wikilink precedence

Resolve exact vault-relative path stems first, then unique filename stems. H1 or humanized-title matching is fallback only and should be reported when a portable target exists. Ignore clearly illustrative placeholder links in examples.
