---
type: Guide
Related to: "[[vault]]"
_organized: true
---

# Vault Automations

Use this guide to document local automations for a deployed vault.

The template does not define active automations. Each deployed vault should decide whether to create automations after its scope, privacy boundary, and Git policy are clear.

## Ownership

Automations are per-vault. A job should run with the target vault as its working directory, follow that vault's `AGENTS.md`, Procedure notes, and Skill packages, and respect that vault's privacy and Git checkpoint policies.

The work/control vault may track routing and template decisions, but it should not run maintenance jobs over another vault's private content unless the user explicitly asks.

## Candidate Automations

Common starting points:

- process the reusable [[ready-to-ingest]] note with [[procedures/process-ready-ingestion-inbox]];
- run read-only mechanical diagnostics with [[procedures/lint-vault]];
- run read-only strategic review with [[procedures/review-vault-health]].

## Prompt Pattern

Keep automation prompts thin:

```text
In <VAULT_ROOT>, run the <skill-name> skill. Follow AGENTS.md, the skill, and procedures/<procedure>.md. Keep the run <read-only or task-scoped write mode>. Report findings or commit only as allowed by the procedure.
```

For private or sensitive vaults, include an explicit stop rule for sensitive material.

## Schedule Pattern

Stagger schedules across vaults so jobs do not collide. For example, if the work/control vault runs lint at 09:00, a personal vault could run lint at 09:15.

## Deployment Checklist

- Decide which candidate automations fit the deployed vault.
- Keep read-only jobs explicitly read-only.
- Give write-capable jobs narrow permission and a clear Git checkpoint rule.
- Record active jobs in the deployed vault's automation guide.
- Do not copy another vault's automation prompts without checking scope, privacy, and working directory.
