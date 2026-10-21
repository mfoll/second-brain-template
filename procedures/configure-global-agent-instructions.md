---
type: Procedure
status: Active
belongs_to: "[[vault]]"
_organized: true
---

# Configure Global Agent Instructions

## Goal

Add a small Brain routing section to selected runtimes while preserving their existing instructions. This is optional for cross-project use; a human editing notes or an agent working only in the vault can keep its local setup.

The vault's `AGENTS.md` owns daily knowledge rules, with local `CLAUDE.md` and `GEMINI.md` imports for compatible runtimes. Global configuration supplies a role-to-root pointer, not a second copy of that rulebook.

## Choose the ownership mode

Read `AGENTS.md` and inspect only the selected runtime's instruction surface and its source, if generated. Determine who owns it before editing:

- **Controlled multi-vault:** an existing executable source owns vault roots, routing, shared preferences, and authorization. Add this vault's logical role and root through that source and its documented regeneration path. Do not replace it with [[global-agent-instructions-template]].
- **Standalone:** use only the marked block from [[global-agent-instructions-template]], merged alongside existing user guidance. An existing global file is normal and does not need to be replaced.

If ownership or a real instruction conflict is unclear, resolve that setup choice with the user. Reuse the decision on later runs. Choose one owner per instruction surface.

## Preserve before installation

1. Find an existing Second Brain section or import before adding one. Compare its scope and reuse it when suitable.
2. Record the exact destination and preview the proposed change. Keep a recovery copy of existing instructions or their source in private machine-local storage outside the vault; instruction backups can contain personal information.
3. Preserve unrelated text, imports, runtime settings and project policies. A broad backup is recovery, not permission to replace the whole file.
4. Add or update one bounded block, using the `BEGIN SECOND BRAIN` / `END SECOND BRAIN` markers or the existing owner's section/import mechanism. A repeated installation should leave one block and make no change when it is already current.
5. Resolve conflicts explicitly during setup rather than silently weakening an existing policy. Install no Skills, services or automation as a side effect.

## Select runtime instruction surfaces

Configure each agent runtime that will work from the vault or from linked project workspaces:

- Codex: use the controlled configuration source when one exists; for a standalone setup, the default is `${CODEX_HOME:-$HOME/.codex}/AGENTS.md`. Inspect `AGENTS.override.md` and the selected `CODEX_HOME` before choosing the active surface; an existing override can hide the base file. See the [official instruction-loading reference](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
- Claude Code: use the controlled configuration source when one exists; for a standalone setup, merge the block into `${CLAUDE_CONFIG_DIR:-$HOME/.claude}/CLAUDE.md`. Retain the vault-root `CLAUDE.md` shim. Project workspaces need none because Claude Code reads `AGENTS.md` directly, unless the deployment uses a provider or setting where that loading is unavailable.
- Gemini CLI: use its existing configuration owner, or add the block to the default `~/.gemini/GEMINI.md`. Retain the vault-root import and preserve any existing Gemini-specific instructions.
- Another agent: use only its documented user and project instruction surfaces. When it supports imports, make its project entry point import `AGENTS.md`; otherwise maintain the smallest adapter possible and keep `AGENTS.md` authoritative.

Do not assume that instruction loading also enables Skill discovery. Configure retained Skill packages separately through [[procedures/configure-agent-skill-discovery|Configure Agent Skill Discovery]].

## Controlled multi-vault steps

1. Read the routing/control vault's global-instruction architecture note and the executable source's own instructions.
2. Confirm the new logical vault role, concrete root, privacy boundary, and any cross-vault restrictions.
3. Add or update only the role-to-root routing in that source. Preserve other vault mappings, global guidance and authorization rules; avoid introducing a second competing Brain block.
4. Run the source's documented generator or installer; never hand-edit a generated output when its source is available.
5. Compare source, generated artifact, and installed instruction surface. Verify the new role resolves to a readable root containing `AGENTS.md` and that existing roles still resolve correctly.
6. Compare unrelated instruction content with the recovery copy as well as checking the new mapping. Mark the deployed `global-agent-instructions-template.md` `_archived: true` and explicitly non-authoritative while any retained Guide, Procedure or router links to it. Delete it only after updating its backlinks and passing link validation.

## Standalone steps

1. Read [[global-agent-instructions-template]] completely and identify the agent's machine-local instruction surface.
2. Confirm `<VAULT_ROLE>` and `<VAULT_ROOT>` with the user or an explicitly local setup note; never infer them from the template checkout.
3. Add or update only the template's marked Second Brain block, preserving the rest of the file. Use the runtime's existing import mechanism if that is its established convention; do not add the whole Guide or vault `AGENTS.md` globally.
4. Replace placeholders only in the machine-local surface, not in portable vault notes.
5. Verify the configured root is readable and contains `AGENTS.md`.
6. Verify routing and the missing-root guard, then read the vault's daily rules through the new pointer. Confirm unrelated instructions are unchanged and a repeat install would not duplicate the block.

## Validation and report

For either mode:

- verify every selected runtime loads its intended machine-global instruction surface;
- test role-to-root resolution from a workspace pointer;
- read the resolved vault `AGENTS.md` and entry note without using an embedded project-local root;
- confirm stale roots, copied project rules, or broad machine details are absent from portable notes;
- inspect the complete task-scoped diff in the executable source and installed surface;
- verify an existing project still loads its technical instructions alongside any added memory section;
- report the chosen ownership mode, authoritative source, generated or installed surface, configured role and root, tests, and intentional placeholders.

## Boundaries

Keep concrete local paths out of portable vault notes. Real vault roots belong in the machine-local instruction surface or in an explicitly deployment-local setup note.

Do not put secrets, credentials, tokens, cache files, generated dumps, or private source material into global instructions.

Do not overwrite unrelated custom user guidance. In controlled mode, do not bypass the generator. In standalone mode, merge narrowly around the Second Brain memory block.

For rollback, restore the changed source or remove only the installed Brain block/import, then regenerate through its owner when required. Preserve unrelated edits made since installation; avoid restoring an old full file over newer work.
