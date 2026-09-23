---
type: Procedure
status: Active
belongs_to: "[[vault]]"
_organized: true
---

# Configure Global Agent Instructions

## Goal

Install or check machine-local global instructions without creating a second competing source of truth. Choose exactly one mode: join an existing controlled multi-vault system, or configure this as a standalone vault.

## Choose the ownership mode

Read `AGENTS.md` and inspect the current machine-local instruction surface before editing. Determine whether a routing/control vault or machine-local configuration repository already owns generated global instructions.

- **Controlled multi-vault:** an existing executable source owns vault roots, routing, shared preferences, and authorization. Add this vault's logical role and root through that source and its documented regeneration path. Do not replace it with [[global-agent-instructions-template]].
- **Standalone:** no other control source exists. Use [[global-agent-instructions-template]] as the source for a narrowly installed Second Brain block.

If ownership is unclear, stop and ask. Do not combine the two modes.

## Select runtime instruction surfaces

Configure each agent runtime that will work from the vault or from linked project workspaces:

- Codex: use the controlled configuration source when one exists; for a standalone setup, merge the block into `${CODEX_HOME:-$HOME/.codex}/AGENTS.md`.
- Claude Code: use the controlled configuration source when one exists; for a standalone setup, merge the block into `${CLAUDE_CONFIG_DIR:-$HOME/.claude}/CLAUDE.md`. Retain the vault-root `CLAUDE.md` shim. Project workspaces need none because Claude Code reads `AGENTS.md` directly, unless the deployment uses a provider or setting where that loading is unavailable.
- Another agent: use only its documented user and project instruction surfaces. When it supports imports, make its project entry point import `AGENTS.md`; otherwise maintain the smallest adapter possible and keep `AGENTS.md` authoritative.

Do not assume that instruction loading also enables Skill discovery. Configure retained Skill packages separately through [[procedures/configure-agent-skill-discovery|Configure Agent Skill Discovery]].

## Controlled multi-vault steps

1. Read the routing/control vault's global-instruction architecture note and the executable source's own instructions.
2. Confirm the new logical vault role, concrete root, privacy boundary, and any cross-vault restrictions.
3. Update only the executable source files that own role-to-root routing. Preserve unrelated global guidance and authorization rules.
4. Run the source's documented generator or installer; never hand-edit a generated output when its source is available.
5. Compare source, generated artifact, and installed instruction surface. Verify the new role resolves to a readable root containing `AGENTS.md` and that existing roles still resolve correctly.
6. Mark the deployed `global-agent-instructions-template.md` `_archived: true` and explicitly non-authoritative while any retained Guide, Procedure, or router links to it. Delete it only after removing or updating every backlink and passing link validation.

## Standalone steps

1. Read [[global-agent-instructions-template]] completely and identify the agent's machine-local instruction surface.
2. Confirm `<VAULT_ROLE>` and `<VAULT_ROOT>` with the user or an explicitly local setup note; never infer them from the template checkout.
3. Merge the template's Second Brain block narrowly into the machine-local surface. Preserve unrelated custom user guidance.
4. Replace placeholders only in the machine-local surface, not in portable vault notes.
5. Verify the configured root is readable and contains `AGENTS.md`.
6. Compare installed text with the template. Confirm progressive retrieval, typed capture, workflow comparison, missing-root guard, and explicit push authorization remain present.

## Validation and report

For either mode:

- verify every selected runtime loads its intended machine-global instruction surface;
- test role-to-root resolution from a workspace pointer;
- read the resolved vault `AGENTS.md` and entry note without using an embedded project-local root;
- confirm stale roots, copied project rules, or broad machine details are absent from portable notes;
- inspect the complete task-scoped diff in the executable source and installed surface;
- report the chosen ownership mode, authoritative source, generated or installed surface, configured role and root, tests, and intentional placeholders.

## Boundaries

Keep concrete local paths out of portable vault notes. Real vault roots belong in the machine-local instruction surface or in an explicitly deployment-local setup note.

Do not put secrets, credentials, tokens, cache files, generated dumps, or private source material into global instructions.

Do not overwrite unrelated custom user guidance. In controlled mode, do not bypass the generator. In standalone mode, merge narrowly around the Second Brain memory block.
