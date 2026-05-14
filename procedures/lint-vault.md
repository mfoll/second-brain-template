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
- Project notes with `status: Active` without a matching human-facing saved view unless `Project view: false` is set. Project notes with `status: Idea` do not need a view.
- Project human views that exceed 10 `Surface for` members, include archived or superseded notes, or use title-only filters where `Surface for` should be used.
- `Surface for` values that do not resolve to a Project note.
- Question notes missing status or using statuses outside `Open`, `Answered`, `Deferred`, and `Superseded` without explanation.
- Source notes without provenance such as `url`, `source_file`, citation data, or an explicit reason provenance is unavailable.
- External raw-file Source notes with missing `storage_system`, `root_key`, `relative_path`, `access`, or `last_checked` fields.
- External raw-file Source notes that use committed absolute local paths where `root_key` plus `relative_path` should be used.
- ADRs missing status, context, decision, or consequences.
- Procedure notes that are too vague for another agent to follow.
- Visible Skill notes whose `package_path` does not point to an existing `.agents/skills/<name>/` package with `SKILL.md`.
- Package folders with no visible Skill note when they are intended to be discoverable.
- Ignore local OS/cache junk inside skill packages, including `.DS_Store`, `__pycache__`, `.pyc`, logs, temporary files, generated artifacts, and machine-specific cache files. These files should not trigger lint findings.
- Durable template content that contains unscoped local paths, cache paths, or machine-specific setup details.
- In deployed non-template vaults, active template-only notes such as unarchived deployment guides or `global-agent-instructions-template.md` copies that should have been deleted, archived, or converted into implemented local guidance.

## Steps

1. Check Git state first so lint findings are not confused with unrelated local edits.
2. Inventory Markdown files, Type notes, Procedure notes, Skill notes, `.agents/skills/` packages, and saved views.
3. Run targeted searches for missing frontmatter, missing H1s, relationship-field drift, broken view fields, local path leakage, and junk files.
4. Check wikilinks with the portable resolver: exclude `.agents/**`, `.git/**`, `attachments/**`, caches, generated artifacts, and implementation files from normal note resolution; prefer exact vault-relative path-stem matches first; then exact filename-stem matches when unique; use H1/title/humanized-title matching only as fallback and report fallback-required links as non-portable. Report ambiguous links only when more than one normal durable note remains plausible after path-stem and filename-stem precedence. `.agents/skills/**/SKILL.md` files remain part of skill-package consistency checks, not normal wikilink target resolution.
5. Check visible Skill notes against package directories and package `SKILL.md` files.
6. For Source notes that use external raw-file fields, check that the durable note uses `root_key` plus `relative_path`, not a resolved local absolute path. When the user asks to verify actual external paths, follow [[procedures/check-external-raw-references|Check External Raw References]].
7. For Project human views, require either a saved view in `views/*.yml` filtering on `Surface for` with that Project's wikilink, or an explicit `Project view: false` opt-out only for Project notes with `status: Active`. Do not require views for `status: Idea` Projects. Do not automatically add opt-outs; only the user chooses them. Do not automatically expand project views during lint.
8. Group findings by severity: errors that break retrieval or execution, warnings that reduce portability, and suggestions for later health review.
9. Stay read-only unless the user explicitly asks for focused fixes.
10. Recommend follow-up workflows when appropriate, such as [[procedures/process-inbox|Process Inbox]], [[procedures/update-project-summary|Update Project Summary]], [[procedures/update-project-next-actions|Update Project Next Actions]], [[procedures/maintain-project-human-view|Maintain Project Human View]], [[procedures/check-external-raw-references|Check External Raw References]], or [[procedures/review-vault-health|Review Vault Health]].

## Output Standard

Lead with findings, ordered by severity. Include file paths and line numbers when available. If there are no findings, say so and name any checks that were not run.


## Guardrails

- Keep edits scoped to the user's request and the relevant Project or Source.
- Use `Belongs to`, `Related to`, and `Has` for relationships.
- Do not add secrets, credentials, local cache paths, generated dumps, or machine-specific setup details unless the note is explicitly about that local setup.
- Ask before creating new Types, broad relationship rewrites, mass moves, deletions, or public/private visibility changes.
