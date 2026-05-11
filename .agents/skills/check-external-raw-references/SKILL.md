---
name: check-external-raw-references
description: Use when the user asks to check, refresh, maintain, re-index, verify, or audit external raw-file Source notes in the Second Brain vault, including OneDrive or other root_key + relative_path references. Updates only vault Source notes with last_checked and shallow indexes, reports drift, and never writes to external raw folders.
---

# Check External Raw References

Use this skill to maintain external raw-file Source notes in the Second Brain vault.

## Source of truth

- Second Brain vault: this repository/vault root
- Vault rules: `AGENTS.md`
- Detailed procedure: `procedures/check-external-raw-references.md`
- Script: `.agents/skills/check-external-raw-references/scripts/check_external_raw_references.py`

Read the vault rules and procedure before making changes.

## Workflow

1. Confirm the vault root is the current working directory and `.local/roots.yml` exists or report unresolved roots.
2. Run the bundled script from the vault root:

   ```bash
   python3 .agents/skills/check-external-raw-references/scripts/check_external_raw_references.py --write
   ```

3. Review the script report:
   - unresolved roots;
   - missing external paths;
   - source-type mismatches;
   - shallow-index drift;
   - Source notes updated in the vault.
4. Inspect the vault diff. The only expected edits are `type: Source` notes with external raw-file metadata.
5. If the run is part of a write-capable maintenance request or automation, commit and push the vault-only updates when allowed by the vault Git checkpoint rules.

## Rules

- Never write, rename, move, delete, clean, or save generated files into OneDrive, iCloud Drive, or any other external raw folder unless the user explicitly asks for that exact external write.
- This skill may write only vault notes: `last_checked` and shallow folder index sections in Source notes.
- A specific external file that should be maintained over time gets its own Source note. Project notes should link to that Source note rather than keeping their own `last_checked`.
- If a project note contains an external path directly, report that it should be promoted to a Source note when it needs maintenance.
- Keep shallow folder indexes shallow. Do not create deep inventories of shared folders.
- Do not touch Inbox or ready-ingestion notes as part of this skill.
