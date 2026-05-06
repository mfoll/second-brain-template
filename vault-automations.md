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

Cross-vault consistency review is a routing/control-vault responsibility, not a generic deployed-vault workflow. Do not add or deploy a `review-multi-vault-consistency` procedure, skill, or automation into ordinary personal, research, or project vaults unless that vault is explicitly designated as the routing/control vault.

## Candidate Automations

Common starting points:

- process the reusable [[ready-to-ingest]] note with [[procedures/process-ready-ingestion-inbox]], normally every 12 hours unless the deployed vault has a reason for a different cadence;
- run read-only mechanical diagnostics with [[procedures/lint-vault]];
- run read-only strategic review with [[procedures/review-vault-health]].

Do not treat cross-vault routing/interface review as a common starting point. It belongs only to the routing/control vault.

## Prompt Pattern

Keep automation prompts thin:

```text
In <VAULT_ROOT>, run the <skill-name> skill. Follow AGENTS.md, the skill, and procedures/<procedure>.md. Keep the run <read-only or task-scoped write mode>. Report findings or commit only as allowed by the procedure.
```

For private or sensitive vaults, include an explicit stop rule for sensitive material.

## Schedule Pattern

Stagger schedules across vaults so jobs do not collide. For example, if the work/control vault runs lint at 09:00, a personal vault could run lint at 09:15.

Ready-ingestion inbox processing should default to every 12 hours. Use explicit times in the deployed vault's automation guide. In the user's current multi-vault setup, the work/control vault starts at 00:30 and the personal vault starts at 00:45, then each repeats every 12 hours.

## Deployment Checklist

- Decide which candidate automations fit the deployed vault.
- Keep read-only jobs explicitly read-only.
- Give write-capable jobs narrow permission and a clear Git checkpoint rule.
- Record active jobs in the deployed vault's automation guide.
- Do not copy another vault's automation prompts without checking scope, privacy, and working directory.
