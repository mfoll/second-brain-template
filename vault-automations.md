---
type: Guide
related_to: "[[vault]]"
_organized: true
---

# Vault Automations

Use this guide to document local automations for a deployed vault.

The template does not define active automations. Each deployed vault should decide whether to create automations after its scope, privacy boundary, and Git policy are clear.

When creating or updating Codex automations, explicitly set the latest available default-capable Codex model unless the user explicitly asks for another model. Verify the model in both the automation file and any local automation database before reporting the automation as done.

When this template's generic automation patterns change, check whether currently deployed vault automation guides should receive the same compatible change. Deployed vaults may intentionally diverge for privacy, scope, cadence, or local execution reasons, but that divergence should be explicit.

Write-capable automations that are expected to push Git checkpoints need a persisted Git network approval or another configured network path. Prefer narrow command-scoped approval for the exact scheduled-run command, such as `git push origin main`, over broad global full access. Without that, a sandboxed automation may commit locally but fail to push until the user approves network escalation.

## Ownership

Automations are per-vault. A job should run with the target vault as its working directory, follow that vault's `AGENTS.md`, Procedure notes, and Skill packages, and respect that vault's privacy and Git checkpoint policies.

The work/control vault may track routing and template decisions, but it should not run maintenance jobs over another vault's private content unless the user explicitly asks.

Cross-vault consistency review is a routing/control-vault responsibility, not a generic deployed-vault workflow. The template includes `review-multi-vault-consistency` so a main/control brain can be deployed from the same starter kit, but ordinary personal, research, project, or team vaults should not list it as active or schedule it unless that vault is explicitly designated as the routing/control vault.

## Candidate Automations

Common starting points:

- process the reusable [[ready-to-ingest]] note with [[procedures/process-ready-ingestion-inbox]], either manually/paused for low-frequency use or on an explicit schedule such as daily at 09:00 local time;
- run read-only mechanical diagnostics with [[procedures/lint-vault]];
- run read-only strategic review with [[procedures/review-vault-health]].

Do not treat cross-vault routing/interface review as a common starting point. It belongs only to the routing/control vault; if this deployed vault is the main/control brain, document that explicitly before creating a `review-multi-vault-consistency` automation.

## Prompt Pattern

Keep automation prompts thin:

```text
In <VAULT_ROOT>, run the <skill-name> skill. Follow AGENTS.md, the skill, and procedures/<procedure>.md. Keep the run <read-only or task-scoped write mode>. Report findings or commit only as allowed by the procedure.
```

For private or sensitive vaults, include an explicit stop rule for sensitive material.

For ready-ingestion automation, advisory feedback should not block safe ingestion, commit, or push. Use `## Ingestion Questions` only when user input is required before coherent or safe processing.

## Schedule Pattern

Stagger schedules across vaults so jobs do not collide. For example, if the work/control vault runs lint at 09:00, a personal vault could run lint at 09:15.

Ready-ingestion inbox processing can stay paused for manual triggering when captures are infrequent. If a deployed vault schedules it, use explicit times in that vault's automation guide and verify both the automation file and local database row. In the user's current multi-vault setup, the work/control and personal ready-ingestion automations are intentionally paused for manual triggering, with stored schedules of daily 09:00 local time if later re-enabled.

## Deployment Checklist

- Decide which candidate automations fit the deployed vault.
- Keep read-only jobs explicitly read-only.
- Give write-capable jobs narrow permission and a clear Git checkpoint rule.
- Record active jobs in the deployed vault's automation guide.
- Activate [[procedures/review-multi-vault-consistency|Review Multi-Vault Consistency]] only for the designated main/control brain.
- Do not copy another vault's automation prompts without checking scope, privacy, and working directory.
