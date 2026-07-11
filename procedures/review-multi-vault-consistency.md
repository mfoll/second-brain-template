---
type: Procedure
status: Active
belongs_to: "[[vault]]"
related_to:
  - "[[vault-automations]]"
_organized: true
---

# Review Multi-Vault Consistency

Use this procedure only when this vault is the routing/control vault for a multi-vault Second Brain setup.

Do not deploy or activate this workflow in ordinary personal, research, project, or team vaults by default. Those vaults can keep their local maintenance procedures, but cross-vault routing and template coordination should belong to one explicitly designated main brain or control vault.

## Goal

Check whether the main/control vault, deployed vaults, the template repository, and local automation definitions still agree on routing, ownership, schedules, generic workflow drift, and privacy boundaries.

The review is read-only by default and should inspect only routing/interface surfaces unless the user explicitly approves a deeper review of a specific vault.

## Deployment Rule

This template includes the procedure and skill package so a newly deployed main/control vault can keep a complete operating system for multi-vault coordination.

When deploying an ordinary vault:

- do not add this procedure to the root Project's active workflows;
- do not create a Codex automation for this workflow;
- do not use this vault to inspect or maintain another vault's private content;
- remove the installed skill package and archive or remove its catalogue note and active routes; retain the Procedure only as clearly archived provenance if useful.

When deploying the designated main/control vault:

- keep this procedure, its visible Skill note, and its hidden skill package;
- link it from the root Project or maintenance responsibility;
- document the active automation in [[vault-automations]] if scheduled;
- state which vaults and template repositories are in scope.

## Checks

- Repository roles: confirm each configured root exists, is a Git repository, and matches the documented role.
- Routing docs: compare `AGENTS.md`, README, and root Project notes. For standalone vaults, include the global-instruction template and installed surface; for controlled systems, compare the executable source, generated artifacts, and installed surfaces rather than treating a neutral template as authoritative.
- Generic workflow inventory: compare Procedures and coherent Skill catalogue/package pairs across the template and deployed vaults, allowing deliberate vault-specific additions and omissions. For each retained Skill, verify `package_path`, package `name`, catalogue lifecycle, package-bundled support files, and its explicit ownership mode: matching Procedure linkage or specialized standalone package. Treat purpose drift semantically and check documented external prerequisites at execution.
- Automation registry: compare live automation definitions against each vault's automation guide. Confirm each automation uses the correct working directory, schedule, model, and read/write policy.
- Ready-ingestion state: confirm deployments are manual-first by default; for each explicitly enabled schedule, verify that its user-chosen cadence, time zone, active or paused state, and working directory are documented accurately.
- Privacy boundaries: confirm control-vault automation does not read or maintain private vault contents, and private-vault automations preserve their own privacy rules.
- Template drift: identify generic improvements that should be made in the template first and then deliberately ported into selected deployed vaults.
- Propagation drift: identify recent generic workflow or structural changes that should have been checked against the template and deployed vault interface files before checkpointing.
- Git state: report uncommitted or unpushed changes in each repository without staging, committing, or pushing.

## Privacy Boundary

Do not inspect private-vault content notes by default. The default review may read routing/interface files such as `AGENTS.md`, `README.md`, root Project notes, procedures, visible skill notes, skill package names, automation guides, and Git status.

Ask for explicit current-turn approval before reading sensitive sources, Inbox contents, `ready-to-ingest.md` body text, health records, financial documents, identity documents, tax documents, message databases, or other private source material.

## Steps

1. Read this vault's routing decision notes and automation guide, then identify the global-instruction owner: standalone template, or controlled executable source plus generated and installed artifacts.
2. Inspect configured vault/template roots and the live automation list.
3. Compare routing and automation documentation across the main/control vault, deployed vaults, and template.
4. Compare Procedure inventories and Skill pairs. Do not treat matching filenames as sufficient: verify that each visible note and package satisfy [[skill]], while allowing intentional vault-specific content and documented runtime-only exceptions.
5. For recent changes to generic workflows, procedures, skills, automation rules, vault conventions, or `AGENTS.md`, check whether the change was also considered for the template and selected deployed vaults.
6. Separate findings into:
   - hard inconsistencies that should be fixed;
   - intentional vault-specific differences;
   - template improvements to port deliberately;
   - privacy or automation risks;
   - questions requiring user approval.
7. Stay read-only unless the user explicitly asks to apply a specific fix.

## Output Standard

Lead with whether the multi-vault interface is consistent enough to trust.

Report the live ready-ingestion cadence explicitly when ready-ingestion automations exist.

Do not produce a broad diff or rewrite plan unless the user asks to implement fixes.
