---
type: Procedure
status: Active
belongs_to: "[[vault]]"
related_to:
  - "[[procedures/configure-global-agent-instructions|Configure Global Agent Instructions]]"
  - "[[procedures/maintain-project-human-view|Maintain Project Human View]]"
_organized: true
---

# Initialize Project Memory

Use this procedure to establish project memory and, only when justified, connect a substantive workspace to a configured vault through a compact local pointer.

## Steps

1. Resolve the logical vault role, external-project-file strategy, and `attachments/` policy. Apply [[procedures/route-project-work-and-artifacts|Route Project Work And Artifacts]] before creating a folder. If no promotion condition is met, update only the Brain entry point and use an existing vault-scoped task or project.
2. Confirm the selected vault root is readable and contains `AGENTS.md`; never guess or create a vault root.
3. Prepare a final workspace folder only when durable technical artifacts, specialized local requirements, persistent execution, or explicit user choice justify it. An agent-application project is a separate decision.
4. Confirm entry-point scope versus vault scope. For entry-point scope, search existing notes before creating a new one and default to Project only when it fits the work.
5. Read the selected vault's `AGENTS.md` and relevant Type. Create or update the entry note with compact current synthesis and high-confidence relationships.
6. Resolve the Project's durable non-versioned file location:
   - for `convention-based`, propose the configured root plus `<project-slug>/` without embedding the resolved absolute root in the vault;
   - for `linked-per-project`, confirm a distinct external folder and do not infer one from unrelated folders;
   - for `workspace-only`, keep only Git-tracked or reproducible artifacts until the user explicitly adds an external location.
   - when retained work must survive machine loss before a dedicated folder is justified, use the deployment's configured `Working/<project-or-context-slug>/` convention.
   Link maintained inputs, outputs, deliverables, or folders through confirmed Source notes with `root_key` plus `relative_path`. Do not deep-scan shared or private roots.
7. For a new active Project, follow [[project]] and create a small human view only when it would add a useful working surface. Absence of a view is valid and does not require `Project view: false`.
8. Inside an existing or justified workspace, inspect its instruction files and any generator that owns them. Preview the diff and preserve a private recovery copy. Add or update only the marked memory section of `AGENTS.md`, normally near 80 words; preserve the rest of the file. That size target applies to the added section, not the existing technical instructions. Never create a folder merely for a pointer, and avoid a duplicate memory section on repeat runs.
9. Use the selected runtime's existing instruction-loading mechanism. Claude Code can read local `AGENTS.md` directly in supported setups; add `@AGENTS.md` to its existing `CLAUDE.md` only when needed, preserving its content. Apply the same additive rule for a Gemini `GEMINI.md` import. Keep generated files under their existing source and regeneration mechanism.
10. Apply the user's local repository and backup policy. Keep credentials, raw data, controlled material, caches, environments, and unversioned durable outputs out of Git. Use an ignored project `.tmp/` for task-specific temporary files and `/tmp/` for truly disposable files. Apply the deployed `attachments/` policy rather than creating that folder by default.
11. Review workspace and vault diffs. If a workspace was promoted, report its exact path and whether an agent-application project is justified; otherwise state that the Brain entry point is sufficient.

## Entry-point pointer

```md
## Second Brain memory

Vault role: `<vault-role>`. Entry note: `<confirmed-wikilink>`.

Resolve the vault root from global instructions. If it is unknown or unreadable, ask rather than guessing or creating it. Read its `AGENTS.md`, then the entry note and relevant links. Preserve this project's technical instructions, tools and canonical documentation; save selected durable context in the Brain within the agreed scope.
```

## Vault-scoped pointer

```md
## Second Brain memory

Vault role: `<vault-role>`. Entry note: none (vault-scoped).

Resolve the vault root from global instructions. If it is unknown or unreadable, stop and ask. Read the vault `AGENTS.md`, then start from relevant Type and topic surfaces. Do not create a Project unless asked.
```

When a workspace exists, the final handoff must name its absolute path. The local pointer is routing, not a reason to create a workspace or a second policy system.
