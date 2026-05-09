---
type: Procedure
status: Active
Belongs to: "[[vault]]"
_organized: true
---

# Lint Vault

Use this procedure when the user asks for a mechanical or structural vault check.

## Goal

Find concrete issues that reduce retrieval, provenance, portability, or agent usability. Do not turn linting into broad organizing or strategic redesign.

## Checks

- Markdown notes missing YAML frontmatter or a first H1.
- Frontmatter that is invalid YAML or uses unexpected relationship fields.
- Durable notes using relationship keys other than `Belongs to`, `Related to`, and `Has` for normal vault relationships.
- Broken, ambiguous, or non-portable wikilinks.
- Type notes with duplicate display metadata aliases or inconsistent Type naming.
- Saved views with invalid YAML, missing root `all` or `any`, stale field names, or filters that no longer match current conventions.
- Active Project notes without outcome, current state, scope and boundaries, next actions, open questions, important links, or maintenance history.
- Project `Has` lists that look exhaustive rather than navigational.
- Question notes missing status or using statuses outside `Open`, `Answered`, `Deferred`, and `Superseded` without explanation.
- Source notes without provenance such as `url`, `source_file`, citation data, or an explicit reason provenance is unavailable.
- ADRs missing status, context, decision, or consequences.
- Procedure notes that are too vague for another agent to follow.
- Visible Skill notes whose `package_path` does not point to an existing `.agents/skills/<name>/` package with `SKILL.md`.
- Package folders with no visible Skill note when they are intended to be discoverable.
- Local junk files such as `.DS_Store`, `__pycache__`, `.pyc`, logs, temporary files, or generated artifacts.
- Durable template content that contains unscoped local paths, cache paths, or machine-specific setup details.
- In deployed non-template vaults, active template-only notes such as unarchived deployment guides or `global-agent-instructions-template.md` copies that should have been deleted, archived, or converted into implemented local guidance.

## Steps

1. Check Git state first so lint findings are not confused with unrelated local edits.
2. Inventory Markdown files, Type notes, Procedure notes, Skill notes, `.agents/skills/` packages, and saved views.
3. Run targeted searches for missing frontmatter, missing H1s, relationship-field drift, broken view fields, local path leakage, and junk files.
4. Check wikilinks with the portable resolver: exclude `.agents/**`, `.git/**`, `attachments/**`, caches, generated artifacts, and implementation files from normal note resolution; prefer exact vault-relative path-stem matches first; then exact filename-stem matches when unique; use H1/title/humanized-title matching only as fallback and report fallback-required links as non-portable. Report ambiguous links only when more than one normal durable note remains plausible after path-stem and filename-stem precedence. `.agents/skills/**/SKILL.md` files remain part of skill-package consistency checks, not normal wikilink target resolution.
5. Check visible Skill notes against package directories and package `SKILL.md` files.
6. Group findings by severity: errors that break retrieval or execution, warnings that reduce portability, and suggestions for later health review.
7. Stay read-only unless the user explicitly asks for focused fixes.
8. Recommend follow-up workflows when appropriate, such as [[procedures/process-inbox|Process Inbox]], [[procedures/update-project-summary|Update Project Summary]], [[procedures/update-project-next-actions|Update Project Next Actions]], or [[procedures/review-vault-health|Review Vault Health]].

## Output Standard

Lead with findings, ordered by severity. Include file paths and line numbers when available. If there are no findings, say so and name any checks that were not run.


## Guardrails

- Keep edits scoped to the user's request and the relevant Project or Source.
- Use `Belongs to`, `Related to`, and `Has` for relationships.
- Do not add secrets, credentials, local cache paths, generated dumps, or machine-specific setup details unless the note is explicitly about that local setup.
- Ask before creating new Types, broad relationship rewrites, mass moves, deletions, or public/private visibility changes.
