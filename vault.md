---
type: Project
status: Active
_organized: true
---

# <Vault Name>

This is the root project note for this vault.

## Outcome

Describe what this vault should help a future human or agent do.

## Current State

This is a template root Project note. Replace this section during deployment with the current state of the deployed vault.

## Scope and Boundaries

Describe what belongs here, what does not, and any privacy or routing boundaries.

## Active Workflows

- [[procedures/ingest-source|Ingest Source]]
- [[procedures/process-inbox|Process Inbox]]
- [[procedures/process-ready-ingestion-inbox|Process Ready Ingestion Inbox]]
- [[procedures/update-project-summary|Update Project Summary]]
- [[procedures/update-project-next-actions|Update Project Next Actions]]
- [[procedures/lint-vault|Lint Vault]]
- [[procedures/review-vault-health|Review Vault Health]]
- [[vault-automations|Vault Automations]]

Optional only if this vault is the designated main/control brain for a multi-vault setup:

- [[procedures/review-multi-vault-consistency|Review Multi-Vault Consistency]]

## Next Actions

- [ ] Customize this vault's purpose and scope.
- [ ] Configure global or local agent instructions.
- [ ] Decide whether this vault is an ordinary vault or the main/control brain for multi-vault routing.
- [ ] Delete or archive template-only notes after converting them into implemented vault guidance.
- [ ] Decide whether this vault needs local automations and document them in [[vault-automations]].
- [ ] Create the first real Project, Responsibility, or Source note.
- [ ] Test source ingestion with one low-risk item.

## Open Questions

- What should this vault store permanently?
- What should stay transient or outside the vault?

## Important Notes

- [[AGENTS]]
- [[README]]
- [[procedures/initialize-project-memory|Initialize Project Memory]]
- [[procedures/update-project-summary|Update Project Summary]]
- [[procedures/update-project-next-actions|Update Project Next Actions]]

## Maintenance Log

- YYYY-MM-DD: Deployed from `second-brain-template`.
- YYYY-MM-DD: Template includes advisory ingestion feedback in source, inbox, and ready-ingestion workflows; feedback should not block safe ingestion.
- YYYY-MM-DD: Template includes a deployment propagation checkpoint for generic workflow and convention changes.
- YYYY-MM-DD: Template documents that ordinary deployed vaults should delete or archive template-only residue after converting it into implemented local guidance.
- YYYY-MM-DD: Template initialize-project-memory uses one primary entry note in workspace-local `AGENTS.md`; secondary relationships stay in the entry note.
- YYYY-MM-DD: Template keeps scripts, prototypes, fixtures, generated outputs, and implementation-local notes in workspaces, but promotes durable project documentation into the vault instead of letting workspace `docs/` folders become parallel memory stores.
