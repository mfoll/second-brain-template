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

Instructions and skills are separate interfaces. `AGENTS.md` owns shared vault policy, `CLAUDE.md` imports that policy for Claude Code, and this procedure configures on-demand Skill discovery.

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
- Claude Code reads `CLAUDE.md`; retain the root shim and project-local shims that import `@AGENTS.md`.
- For another agent, add only the smallest documented compatibility entry point that loads `AGENTS.md`. Keep shared policy in `AGENTS.md` and do not maintain a copied instruction body.

Machine-global instructions must resolve the deployed vault's logical role and root as described by [[procedures/configure-global-agent-instructions|Configure Global Agent Instructions]]. Skill links do not replace that routing.

## Validation

1. Run the installer in `--check` mode and require zero unresolved entries.
2. Start or reload the runtime when its documentation requires it after creating a new top-level skills directory.
3. From a workspace that points to this vault, verify that the runtime can list or invoke one retained Skill and that the Skill resolves its vault Procedure.
4. Verify that the runtime loaded the expected global instructions and workspace pointer independently of Skill discovery.
5. Record the runtime, discovery directory, retained Skill set, verification result, and any intentional exclusions in the deployment ledger.

## Boundaries

The installer adds missing links and verifies links it owns. It does not delete stale links, replace conflicts, edit runtime settings, or install external prerequisites. Resolve removals and collisions deliberately after identifying their owner.

Global exposure makes a Skill available from every workspace handled by that runtime. Expose only packages whose scope and privacy boundary are appropriate at that level. Prefer a runtime's documented project-local Skill directory when global exposure would be too broad.
