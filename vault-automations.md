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
- A scheduled lint job diagnoses and proposes ownership. It may identify a responsible Codex task, but must report the candidate and wait for user confirmation before contacting it. If none exists, it proposes doing the focused follow-up in the current task.
- Write-capable jobs need an explicit scope and narrowly authorized commands. Persisted network approval is only an execution mechanism, not general permission.
- Set the deployment's approved standalone automation model and reasoning effort. For Codex, when a low-cost model is appropriate, use the vendor's currently supported low-cost model with its highest reasoning setting unless the user requests another model or effort. Same-task heartbeats inherit their attached task's settings, so verify that task instead.
- Stagger schedules across vaults and document whether a job is active, paused, or manual.

Cross-vault consistency review belongs only to a vault explicitly designated as routing/control. Ordinary personal, research, project, or team vaults must not schedule it.

Template upgrades are never a candidate job: [[upgrade-existing-vault-from-template|Upgrade an Existing Vault From the Template]] needs the owner's review of each change, because deployed vaults diverge from the template on purpose.

## Candidate jobs

- Process [[ready-to-ingest]] through [[procedures/process-ready-ingestion-inbox|Process Ready Ingestion Inbox]] in manual or scheduled write mode.
- Run [[procedures/lint-vault|Lint Vault]] read-only, including the type-aware compactness and Tolaria icon helpers.
- Run [[procedures/review-vault-health|Review Vault Health]] read-only for strategic drift and overloaded hot paths.

Start with manual runs. Add a schedule only after the workflow, privacy boundary, failure behavior, and value have been observed.

## Thin prompt pattern

```text
In <VAULT_ROOT>, run the <skill-name> skill. Follow AGENTS.md, the skill, and the linked Procedure. Keep the run <read-only or task-scoped write mode>. For lint, preserve important information: compactness is not a goal by itself and may call for no change, careful reduction, reorganization, routing, or structural splitting. Identify any current responsible Codex task, report the candidate and proposed workflow, and wait for user confirmation before contacting it. If none exists, say so and offer to perform the focused follow-up in the current task. Report findings or checkpoint only as authorized.
```

Document the job's permitted sources, AI tools and storage destinations during setup, following [[README]]. Reuse that scope on later runs. Stop only the affected operation when it would access an excluded source, disclose content to a new unapproved destination or otherwise exceed its authority. Reuse existing authorization for routine work. Advisory feedback should not block safe ingestion; durable user questions should be reserved for genuine routing or safety blockers.

## Deployment checklist

- Record job name, purpose, working directory, model, mode, cadence, and active/paused state.
- Keep prompts thin and route logic to Procedures.
- Verify read-only jobs cannot write.
- Give write jobs task-scoped commit rules and separate push authorization.
- Check both automation files and any local database row after schedule or model changes. Confirm they agree on the selected model and reasoning effort; when using a low-cost default model, verify the stored model ID against the current Codex model selection. For a heartbeat, verify the attached task's inherited settings.
- Do not copy another vault's automation unchanged without reviewing scope and privacy.
