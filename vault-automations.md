---
type: Guide
related_to: "[[vault]]"
_organized: true
---

# Vault Automations

Optional guidance and a register for recurring work you explicitly enable after deployment. This template installs no scheduler, connectors or active jobs. You can ignore this page while using the brain manually.

## When recurring help is useful

Try a workflow manually first. Add a schedule only when it repeatedly saves effort, its output is useful, and failures or incomplete coverage are visible. Choose your own tools, sources, cadence and review process.

| Purpose | Possible job | Starting boundary |
| --- | --- | --- |
| Collect useful knowledge | Review selected messages, saved links or documents for proposed knowledge updates | Explicitly selected sources through an approved tool; no account-wide scan by default. |
| Retain meeting outcomes | Prepare a summary and proposed Project updates from supplied notes or transcripts | Recording, transcription and source access are separate choices; reuse any established review workflow. |
| Process deferred captures | Process ready-marked material through [[procedures/process-ready-ingestion-inbox]] | Optional; only `ingest_ready: true` captures, with original-capture preservation. |
| Check structure | Run [[procedures/lint-vault]] | Read-only findings; no automatic fixes. |
| Review usefulness | Run [[procedures/review-vault-health]] | Read-only recommendations about current state, retrieval and maintenance priorities. |

Collection and maintenance are different jobs. A collection job can prepare proposals without being allowed to change notes; a maintenance report does not authorize repairs. The template includes no email, messaging, recording or transcription connector. Use the source-handling examples in [[README#What can you bring into the brain?|the README]] to choose a manual starting method.

## Introduce one job

1. Identify a repeated manual task and try it on a small, selected input.
2. Agree its sources, approved AI tools, storage destinations and coverage window. Define whether it reports, proposes updates, or applies narrowly authorized changes.
3. Define what happens when a source is unavailable, incomplete, already processed or ambiguous. Avoid duplicate updates on retries; preserve pending reviews.
4. Run it manually and inspect the result. Verify the actual configured permissions and output; an instruction saying “read-only” is not an access-control mechanism by itself.
5. Select a schedule only if useful, with a time zone, active/paused state and a way to disable it. Verify the stored configuration and observe a scheduled run before calling it reliable.

Reuse existing authorization for routine work. A new source, unapproved destination or expanded action needs a separate decision. Leave the original material unchanged unless specific retention or cleanup authority applies.

## Job register

No jobs are enabled in the template. Fill in a job record in a deployed vault only when a job is selected; do not put credentials or sensitive source contents here.

| Field | Record for each enabled job |
| --- | --- |
| Name and purpose | The useful result it should produce. |
| Workflow | The authoritative Procedure or existing deployment workflow. |
| Sources and selection | Exactly what it may read, including account/folder/list boundaries when relevant. |
| Destination and working directory | The one vault the job runs from and may update; cross-vault access needs separate explicit scope. |
| Runner and configuration | The chosen tool and location of its real configuration; keep machine-specific bindings in local setup. |
| Schedule and state | Cadence, time zone, active/paused/manual state, and how to disable it. |
| Permitted changes | Read-only report, proposals, or named task-scoped writes; commit and push authority are separate. |
| Review and failure handling | Who accepts proposals, how gaps are reported and how retries avoid duplication. |
| Verification | Last checked configuration and observed run, including remaining limits. |

## Execution boundaries

Each job follows its destination vault’s `AGENTS.md`, privacy rules and authoritative workflow. Read-only jobs never stage, commit or push. Write jobs need explicit scope; unattended pushes additionally need narrow repository/branch authorization and a working execution path. Persisted command approval grants no wider permission.

Keep detailed logic in Procedures and the actual scheduler configuration in its owning tool. A short prompt can name the vault, workflow, selected inputs and permitted mode; it must not silently broaden those boundaries. See [[agent-setup#Runtime-specific automation configuration|Agent Setup]] for runtime-specific checks.

Cross-vault review belongs only to an explicitly designated routing/control vault. Template upgrades are never an unattended job: [[upgrade-existing-vault-from-template]] requires reviewed, selective changes that preserve deployed differences.
