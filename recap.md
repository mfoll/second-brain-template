---
type: Type
_icon: calendar
_color: "#6366f1"
_organized: true
_list_properties_display:
  - period
  - period_start
  - review_status
---

# Recap

An optional, curated memory of useful discussions, activities and captured knowledge over a day, month, or year. A Recap preserves what was decided, why, alternatives, constraints, and unresolved points without retaining a raw transcript or paraphrasing every exchange.

This Type and the associated capture workflow are opt-in extensions, not requirements for using the vault. A deployment may omit them. Their presence grants no recording, scheduling, private-source access, ingestion or deletion authority.

## Contract

- `period`: `daily`, `monthly`, or `yearly`.
- `period_start` and `period_end`: inclusive local calendar dates (`YYYY-MM-DD`); equal for a daily Recap, full calendar bounds for monthly/yearly Recaps.
- `timezone`: the configured IANA timezone used to interpret source times and date boundaries.
- `review_status`: `reviewed` for accepted daily content, `derived` for a roll-up of accepted content, or `needs-review` when a material correction remains unresolved. Proposals stay outside the durable vault until authorized.
- `related_to`: relevant canonical Project, Person, Topic, Responsibility, or other note links in this vault.
- `based_on`: daily Recap links for a monthly Recap, monthly links for a yearly Recap. Add direct daily anchors when needed to preserve important decision evidence.
- `source_runs`: optional stable preparation IDs, not raw text, credentials, device identifiers, or machine paths.
- `review_refs`: optional review-decision references without raw text; selected message IDs may remain in source metadata.
- `capture_refs`: optional captured-topic references, each with `id` (unified topic), `decision_ref` (explicit approval), and `captured_on` (capture date). Used for deduplication and verification, never displayed in the body.
- `updated`: last meaningful synthesis revision date.

Suggested paths: `recaps/daily/YYYY/YYYY-MM-DD.md`, `recaps/monthly/YYYY/YYYY-MM.md`, and `recaps/yearly/YYYY.md`. Do not create empty daily notes just to complete a calendar.

## Selection and retrieval

Use the most specific canonical note for current truth and actionable knowledge. Use Recaps for historical conversational context, including useful material deliberately kept as recap-only. Do not create a daily Event or generic Note as a substitute. Use Event when a distinct occurrence independently deserves a note, not merely because recording happened that day.

Search canonical structure first. For remembered discussions, dates, rationale, or decision evolution, also search relevant Recaps and follow their links. Check later corrections and superseding decisions before answering what was finally decided. A summary is not a verbatim quotation or proof of speaker identity.

## Body and retention

A daily combines two source-appropriate views: “What did I do on this day?” for evidenced activities, and “What did we discuss?” for selected meeting notes, transcripts or recordings. Retain the main subjects, useful decisions and open questions of those conversations; do not reduce them to a task list or omit substantive discussion because it produced no action. Keep only meaningful activities and useful outcomes, usually one sentence per activity, two if a qualification is needed. Group related topics into one highlight. Knowledge, arguments and detail remain in canonical notes without duplication. Agent-only ingestion does not establish user activity and may be omitted. Monthly/yearly summaries retain the main progress and activities without reintroducing ingested detail. Explicit Recap-only selections remain briefly retained.

Write for human reading: topic headings without proposal numbers, with prose centred on decisions, rationale, alternatives and meaningful limits. Topic IDs, submission references, UUIDs, hashes, clip counts and approval receipts belong in structured metadata or existing private receipts, not the body. Omit narration about capture operations and actions the agent did not perform. Retain coverage limits only where they affect interpretation, in readable terms. Keep useful canonical wikilinks with explicit labels; reading copies replace them with those labels, without vault paths or import footers. Never remove a factual qualification, attribution or decision merely because it expresses uncertainty.

Organize by activity or related topic, not minute or clip. In the selected summary, preserve the facts and qualifications needed to understand that activity. Keep detailed decisions, rationale, conditions, owners, dates, numbers and rejected options in canonical notes when captured there; where Recap-only is the sole retained memory, retain its useful essence briefly. Distinguish a suggestion from a decision and a mentioned task from an assigned commitment. Link canonical updates instead of copying them in full.

Retain approved daily Recaps for the deployment's chosen retention period, with explicit treatment of information about other people. Configure that policy once alongside source and backup retention; reuse it during routine preparation. If no period has been chosen, preserve existing notes without claiming indefinite retention or authorizing deletion. Monthly/yearly notes are maintained topic-based syntheses and navigation, not replacements for dailies during their retention period. Do not recursively compress away qualifiers or resolve contradictions by guessing. Revisit daily evidence when a roll-up is ambiguous. Late sources or corrections update the affected daily, monthly, and yearly notes without duplicating accepted topics. Apply authorized corrections and exclusions to derived summaries, and handle Git history, backups and provider copies according to the deployment's separate policy.

Follow [[procedures/prepare-recording-recaps|Prepare Recording Recaps]] and the vault's [[capture-preferences|Capture Preferences]] when this extension is enabled.
