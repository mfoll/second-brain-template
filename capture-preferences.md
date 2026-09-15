---
type: Guide
related_to:
  - "[[recap]]"
  - "[[procedures/prepare-recording-recaps]]"
_organized: true
---

# Capture Preferences

Optional, vault-local feedback and terminology for curated capture. This guide does not activate ingestion. Keep work and personal rules in their respective vaults; never copy a private dictionary or examples into a shared template.

## Default treatment

Propose durable decisions, useful constraints, meaningful changes, and clearly owned actions for canonical notes. Offer useful conversational context as recap-only. Omit filler, repeated fragments, obvious transcription artifacts, and content the user explicitly excludes. Material uncertainty stays visible, not silently corrected.

## How feedback is remembered

The user can select `capture`, `recap-only`, `forget`, or `correct` for a stable topic ID and add a comment. A one-off decision applies only to that topic. Add a reusable rule here only when the user expresses a future preference, such as “always exclude this kind of material.” Confirmation of a name correction may update the contextual dictionary with its evidence and scope.

Rules use a stable ID, date, narrow context, requested treatment, rationale when useful, and a user-decision reference. Specific current instructions override broader rules. Do not infer preferences from silence or train an opaque model. Rules remain inspectable and reversible.

`recap-only` keeps a useful summary without changing canonical state or assigning work. `forget` retains no content in either canonical notes or Recaps; a content-free disposition ID may remain for deduplication. Removing already committed content from the current vault does not erase Git history or backups; history rewriting requires separate authorization.

## Reusable rules

No deployment-specific rules are included in the template.

## Contextual dictionary

For each confirmed correction, record the heard/written variant, intended term or note link, context where it applies, confidence/evidence, and date. Never assume one ambiguous name has the same meaning across all projects or both vaults. Leave this section empty until there is useful confirmed feedback.
