---
type: Project
status: Active
belongs_to: "[[maintain-vault]]"
_organized: true
surface_for:
  - "[[vault]]"
---

# <Vault Name>

This is the root Project note for the deployed vault. Replace every placeholder with current scope and state.

## Outcome

Describe what this vault should help a future human or agent do.

## Current State

- This repository is still a template deployment until its purpose, privacy boundary, and entry surfaces are customized.

## Scope and Boundaries

Describe what belongs here, what remains outside, and any privacy, evidence, or routing constraints.

## Active Workflows

- [[procedures/ingest-source|Ingest Source]]
- [[procedures/process-inbox|Process Inbox]]
- [[procedures/update-project-summary|Update Project Summary]]
- [[procedures/lint-vault|Lint Vault]]
- [[procedures/review-vault-health|Review Vault Health]]

Activate [[procedures/review-multi-vault-consistency|Review Multi-Vault Consistency]] only if this deployment is explicitly the routing/control vault.

## Next Actions

- [ ] Define the deployed vault's purpose, scope, privacy boundary, and logical role.
- [ ] Replace template placeholders and remove workflows the vault does not need.
- [ ] Configure compact project pointers and any optional automations.
- [ ] If Skill installation is selected, configure and verify its discovery without replacing existing entries.
- [ ] Create the first real Project, Responsibility, or Source and test retrieval.
- [ ] If external raw files are needed, configure ignored root mappings and verify Source bridges.

## Open Questions

- What should this vault store permanently?
- What should remain transient or outside the vault?

## Important Notes

- [[AGENTS]]
- [[README]]
- [[project]]
- [[tolaria-callouts|Tolaria Callouts]]
- [[tolaria-saved-views|Tolaria Saved Views]]
- [[upgrade-existing-vault-from-template|Upgrade an Existing Vault From the Template]]
- [[procedures/initialize-project-memory|Initialize Project Memory]]
- [[procedures/configure-agent-skill-discovery|Configure Agent Skill Discovery]]
- [[vault-automations|Vault Automations]]

## Maintenance Log

- 2026-09-23: Updated the portable automation guide to describe Luna as the currently supported low-cost Codex model when that trade-off is appropriate, while keeping deployed model IDs in their local configurations.
- YYYY-MM-DD: Deployed from `second-brain-template` and customized its scope.
- YYYY-MM-DD: Confirmed compact project, pointer, retrieval, and Git contracts.
- YYYY-MM-DD: Reviewed optional workflows and removed template-only residue.
