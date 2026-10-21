---
type: Procedure
status: Active
belongs_to: "[[vault]]"
related_to:
  - "[[skill]]"
  - "[[procedures/configure-global-agent-instructions|Configure Global Agent Instructions]]"
_organized: true
---

# Configure Agent Skill Discovery

## Goal

Expose the deployed vault's retained Agent Skills packages to a supported runtime without copying or forking them. The canonical packages remain under `.agents/skills/`; runtime directories contain machine-local symlinks only.

Skill installation is optional. The installer links packages only; it does not generate, replace or install vault or global instruction files.

Instructions and skills are separate interfaces. `AGENTS.md` owns shared vault policy, which Claude Code reads directly or through the vault-root `CLAUDE.md` import, and this procedure configures on-demand Skill discovery.

## Before installation

1. Complete the deployment's Skill review and remove packages the deployed vault does not need.
2. Confirm every retained `.agents/skills/<skill-name>/SKILL.md` has a matching active catalogue note as required by [[skill]].
3. Decide which runtime owns the machine-local discovery directory. In an existing controlled multi-vault setup, use that setup's installer instead of creating competing links.
4. Inspect the target directory for same-name packages. Never overwrite a file, directory, or symlink owned by another vault or installer.

## Install retained skills

From the deployed vault root, expose every retained package to Codex:

```bash
./scripts/configure-agent-skills.sh --runtime codex
./scripts/configure-agent-skills.sh --runtime codex --check
```

For Claude Code:

```bash
./scripts/configure-agent-skills.sh --runtime claude
./scripts/configure-agent-skills.sh --runtime claude --check
```

The defaults are `${CODEX_HOME:-$HOME/.codex}/skills` and `${CLAUDE_CONFIG_DIR:-$HOME/.claude}/skills`. The links are intentionally machine-local and must not be committed.

For another runtime that discovers Agent Skills packages from a known directory, supply that documented directory explicitly:

```bash
./scripts/configure-agent-skills.sh --target <RUNTIME_SKILLS_DIRECTORY>
./scripts/configure-agent-skills.sh --target <RUNTIME_SKILLS_DIRECTORY> --check
```

Do not infer an undocumented path merely because the runtime uses `SKILL.md`. If it lacks Agent Skills discovery, the Procedures remain usable through `AGENTS.md`, but automatic Skill activation is not configured.

## Runtime-specific instruction bridge

- Codex reads the vault and workspace `AGENTS.md` instruction hierarchy directly in the supported setup.
- Claude Code v2.1.277 or later reads a workspace `AGENTS.md` directly when no `CLAUDE.md` or `CLAUDE.local.md` exists in that directory or above it; retain the vault-root `@AGENTS.md` shim and add project shims only where direct loading is unavailable.
- Gemini CLI can use the vault-root `GEMINI.md` import. Preserve existing Gemini-specific guidance when adding that import.
- For another agent, add only the smallest documented compatibility entry point that loads `AGENTS.md`. Keep shared policy in `AGENTS.md` and do not maintain a copied instruction body.

For use from other workspaces, machine-global instructions resolve the vault role and root through [[procedures/configure-global-agent-instructions|Configure Global Agent Instructions]]. Add routing alongside existing instructions or through their generator. Skill links do not replace that routing; vault-local use needs no new global memory block.

## Validation

1. Run the installer in `--check` mode and require zero unresolved entries.
2. Start or reload the runtime when its documentation requires it after creating a new top-level skills directory.
3. From a workspace that points to this vault, verify that the runtime can list or invoke one retained Skill and that the Skill resolves its vault Procedure.
4. Verify that the runtime loaded the expected global instructions and workspace pointer independently of Skill discovery.
5. Record the runtime, discovery directory, retained Skill set, verification result, and any intentional exclusions in the deployment ledger.

## Boundaries

The installer adds missing links and verifies links it owns. It does not delete stale links, replace conflicts, edit runtime settings, or install external prerequisites. Resolve removals and collisions deliberately after identifying their owner.

Global exposure makes a Skill available from every workspace handled by that runtime. Expose only packages whose scope and privacy boundary are appropriate at that level. Prefer a runtime's documented project-local Skill directory when global exposure would be too broad.
