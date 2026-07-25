---
type: Guide
related_to: "[[vault]]"
_organized: true
---

# Vault Automations

Use this guide to document automations after deployment. The template defines no active jobs.

## Ownership and safety

- Each job runs from one deployed vault and follows that vault's `AGENTS.md`, Procedure, Skill, privacy boundary, and Git policy.
- Read-only lint and health jobs never stage, commit, or push.
- Write-capable jobs need an explicit scope and narrowly authorized commands. Persisted network approval is only an execution mechanism, not general permission.
- Set the latest available default-capable Codex model unless the user requests another, then verify the stored automation file and local database state.
- Stagger schedules across vaults and document whether a job is active, paused, or manual.

Cross-vault consistency review belongs only to a vault explicitly designated as routing/control. Ordinary personal, research, project, or team vaults must not schedule it.

## Candidate jobs

- Process [[ready-to-ingest]] through [[procedures/process-ready-ingestion-inbox|Process Ready Ingestion Inbox]] in manual or scheduled write mode.
- Run [[procedures/lint-vault|Lint Vault]] read-only, including the type-aware compactness and Tolaria icon helpers.
- Run [[procedures/review-vault-health|Review Vault Health]] read-only for strategic drift and overloaded hot paths.

Start with manual runs. Add a schedule only after the workflow, privacy boundary, failure behavior, and value have been observed.

## Thin prompt pattern

```text
In <VAULT_ROOT>, run the <skill-name> skill. Follow AGENTS.md, the skill, and the linked Procedure. Keep the run <read-only or task-scoped write mode>. Report findings or checkpoint only as authorized.
```

For sensitive vaults, add an explicit stop rule before private sources or Inbox bodies. Advisory feedback should not block safe ingestion; durable user questions should be reserved for genuine routing or safety blockers.

## Deployment checklist

- Record job name, purpose, working directory, model, mode, cadence, and active/paused state.
- Keep prompts thin and route logic to Procedures.
- Verify read-only jobs cannot write.
- Give write jobs task-scoped commit rules and separate push authorization.
- Check both automation files and any local database row after schedule or model changes.
- Do not copy another vault's automation unchanged without reviewing scope and privacy.
