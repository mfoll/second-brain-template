---
type: Procedure
status: Active
Belongs to: "[[vault]]"
Related to:
  - "[[source]]"
_organized: true
---

# Check External Raw References

Use this procedure to verify that vault notes pointing to external raw files or folders still resolve without copying those files into the vault.

## Goal

Keep portable raw-file pointers useful while preserving the external file system as the source of truth.

## Source Pattern

External raw-file Source notes should use:

```yaml
type: Source
source_type: "external file"
storage_system: External folder
root_key: documents_basedir
relative_path: "Example/important-file.pdf"
access: guarded-write
last_checked: 2026-05-11
```

The durable vault note stores `root_key` and `relative_path`, not a resolved absolute local path. Resolve `root_key` through ignored local configuration such as `.local/roots.yml`, environment variables, or known local candidates documented in the relevant Source note.

`.local/roots.yml` is intentionally gitignored. It is a per-machine adapter, not the durable memory of the external file. When deploying this vault on a new machine, create the resolver before relying on external raw-file references.

A specific external file that should be maintained over time gets its own Source note. Project notes should link to the Source note; they should not carry separate `last_checked` fields for individual file references.

## Guarded-Write Policy

Treat external raw references as read-only by default. Agents may list folders, check existence, read metadata, and read explicitly relevant files. They must not write, rename, move, delete, clean, reformat, or save generated files into external folders unless the user explicitly asks for that specific write action.

## Steps

1. Find active Source notes where `root_key` and `relative_path` are present, or where `storage_system` suggests an external raw-file system.
2. For each note, verify `storage_system`, `root_key`, `relative_path`, `access`, and `last_checked` exist.
3. Resolve `root_key` using `.local/roots.yml` when available. If the local config is missing, report that it should be created before relying on references from this machine.
4. Join the resolved root and `relative_path`.
5. Check whether the resulting path exists and whether its kind matches `source_type` as a file, folder, or collection root.
6. For notes with a shallow folder index, compare the note's index with a shallow read-only listing and report likely additions, removals, or renames.
7. When this procedure is run as a maintenance workflow or through the `check-external-raw-references` skill, update only vault notes: set `last_checked` to today's date and refresh the shallow folder index section when present.
8. Never modify the external raw folder as part of this procedure.
9. Report unresolved roots, missing paths, kind mismatches, stale indexes, notes updated in the vault, and notes that use absolute local paths instead of `root_key` plus `relative_path`.

## Report Shape

Group findings as:

- Missing or unresolved roots.
- Missing external paths.
- Source-type mismatches.
- Stale shallow indexes.
- Vault Source notes updated.
- Non-portable absolute paths in durable notes.
- Suggested vault-only updates.

## Validation

The procedure succeeds when all referenced external paths resolve or produce clear warnings, and no external raw folder was modified.
