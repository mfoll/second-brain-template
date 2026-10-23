---
type: Procedure
status: Active
belongs_to: "[[vault]]"
related_to:
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
4. Resolve the target within the configured root. Reject absolute paths, parent traversal (`..`) and symlinks that escape that root; leave rejected notes unchanged. Skip symlinked Markdown notes and the checker's local/support exclusions.
5. Check whether the resulting path exists and whether its kind matches `source_type` as a file, folder, or collection root.
6. For notes with a shallow folder index, compare the note's index with a shallow read-only listing and report likely additions, removals, or renames. Omit directory symlinks from generated indexes.
7. When this procedure is run as a maintenance workflow, update only vault notes: set `last_checked` to today's date and refresh the shallow folder index section when present.
8. Never modify the external raw folder as part of this procedure.
9. Report unresolved roots, unsafe references, missing paths, kind mismatches, stale indexes, notes updated in the vault, and notes that use absolute local paths instead of `root_key` plus `relative_path`. Use portable note/root-key references in reports; do not print resolved machine paths or configured local root candidates.

## Run

From the vault root, with `.local/roots.yml` in place:

```bash
python3 -I scripts/check_external_raw_references.py            # dry run
python3 -I scripts/check_external_raw_references.py --write    # update last_checked
python3 -I scripts/check_external_raw_references.py --write --date YYYY-MM-DD
```

The checker takes no path argument; it reads the current directory. Without `.local/roots.yml` it prints an INFO line and checks nothing, which is the expected result in a vault that has no external Source notes yet. Run its unit test with `python3 -I scripts/test_check_external_raw_references.py`; the test writes its fixtures to the system temporary directory and removes them.

## Report Shape

Group findings as:

- Missing or unresolved roots.
- Unsafe or unresolvable references left unchanged.
- Missing external paths.
- Source-type mismatches.
- Stale shallow indexes.
- Vault Source notes updated.
- Non-portable absolute paths in durable notes.
- Suggested vault-only updates.

## Validation

The procedure succeeds when all referenced external paths resolve or produce clear warnings, and no external raw folder was modified.

For changes to the checker, run `python3 scripts/test_check_external_raw_references.py`. Its disposable fixtures verify that outside-root references remain unchanged and valid indexes refresh without following directory symlinks.
