---
type: ADR
status: Accepted
belongs_to: "[[vault]]"
related_to:
  - "[[project]]"
  - "[[procedures/route-project-work-and-artifacts|Route Project Work And Artifacts]]"
  - "[[procedures/initialize-project-memory|Initialize Project Memory]]"
_organized: true
---

# ADR 0010: Decouple Brain Projects From Local Workspaces

## Context

An earlier project-memory workflow routinely created a local folder and agent-application project containing only `AGENTS.md` and `CLAUDE.md` pointers to a Second Brain Project. An audit found that these shells added inventory and backup ambiguity without owning real artifacts. Modern tasks can retrieve the correct Project from the vault when it is named in the prompt or inferred from bounded context.

Temporary work also needs a destination before it is clear whether a project deserves a repository or a permanent external folder. Keeping such files only in local launcher folders exposes them to machine loss.

## Decision

> [!note]
> A Second Brain Project note is the default project representation. Create a local workspace or agent-application project only after a technical or operational promotion threshold is met; use the deployment's cloud `Working/<slug>/` convention for retained work before that threshold.

Work files that must survive machine loss use the deployment's configured cloud root through a portable `root_key` and `Working/<project-or-context-slug>/` unless the Project already has a confirmed canonical external Source location.

Dedicated workspaces remain appropriate for durable code, configuration, tests, reproducible analysis, versioned technical inputs, specialized dependencies or instructions, persistent tasks or automations, builds, deployments, collaboration, or an artifact set that has clearly outgrown `Working/`. A workspace and an agent-application project remain separate decisions.

Within a justified Git workspace, delegated tasks use the existing primary checkout directly unless useful concurrent writing or an intentionally isolated review branch requires a worktree. Repository presence alone is not a reason for isolation. Worktree creation must name the concurrency or review need and the task responsible for integration and cleanup.

## Consequences

- `AGENTS.md`-only launcher folders are no longer created by default and should be retired when they have no technical role.
- Agents start from the appropriate Brain Project and create scratch files in a disposable temporary location unless retained work needs cloud `Working/`.
- Useful temporary artifacts are promoted during the task instead of waiting for a later cleanup audit.
- Repositories represent durable versionable artifact sets, not every conceptual Project.
- Source notes keep cloud locations portable through root keys and relative paths.
- Sequential delegation no longer incurs worktree integration and cleanup; bounded parallel code work retains isolation when it provides real value.

## Revisit When

- Agent applications gain a durable project abstraction that changes the workspace promotion decision.
- Cloud `Working/` creates material navigation or cleanup friction.
- Multi-machine operation requires a stronger automated inventory or lifecycle mechanism.

## Provenance

Ported on 2026-10-22 from the maintainer's work/control vault, ADR 0023 *Decouple Brain Projects From Local Workspaces* (2026-09-02); work-specific names and examples were replaced by generic wording.
