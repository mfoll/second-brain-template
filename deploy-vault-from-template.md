---
type: Guide
Related to: "[[vault]]"
_organized: true
---

# Deploy Vault From Template

Use this guide to create a concrete vault from this template.

## Inputs

Collect these values before changing files:

- `<NEW_VAULT_NAME>`
- `<GITHUB_OWNER>`
- `<REPOSITORY_NAME>`
- `<LOCAL_DESTINATION_ROOT>`
- `<VAULT_SCOPE>`
- `<VAULT_ROOT_NOTE>`
- `<PRIVATE_OR_PUBLIC>`

## Preflight Checks

Confirm that the destination folder does not already exist. Confirm that the target GitHub repository does not already exist unless the user explicitly wants to reuse it.

Check that the template repository has no uncommitted changes before creating the new vault.

## Create GitHub Repo From Template

Create a new repository from the template using the chosen owner, repository name, and visibility. Do not make the repository public unless the user explicitly chooses public visibility.

## Clone Locally

Clone the new repository under `<LOCAL_DESTINATION_ROOT>`. Confirm that the local path is correct before editing.

## Customize Root Note

Rename or edit [[vault]] to match `<VAULT_ROOT_NOTE>` if needed. Replace `<Vault Name>` with `<NEW_VAULT_NAME>`. Fill in purpose, scope, first workflows, and first next actions for `<VAULT_SCOPE>`.

## Customize README

Update the README so it describes the concrete vault rather than the template. Remove template-only warnings that no longer apply after deployment, but keep portability and no-secret guidance.

## Customize AGENTS

Keep the vault conventions, but update wording that should name the concrete vault scope. Do not add machine-local paths.

## Customize Global Instruction Placeholders

Use [[global-agent-instructions-template]] to create the machine-local global instruction text. Replace `<VAULT_ROOT>` only in the machine-local instruction surface, not in portable vault notes unless the note is explicitly a local setup note.

## Review Generic Skills

Keep only the generic skills that make sense for the new vault. Remove or archive unused visible Skill notes only if they would confuse users or agents.

## Review Saved Views

Open each file in `views/` and confirm that the filters match the deployed vault's Type and relationship conventions.

## Validate Placeholders

Search for placeholders. Expected placeholders may remain in this deployment guide and in [[global-agent-instructions-template]]. Other placeholder hits should be reviewed and replaced.

## Commit And Push

Review the changed scope, commit a coherent deployment checkpoint, push to the configured remote, and confirm the final branch state.

## Report Final State

Report:

- local path;
- GitHub repository URL;
- visibility;
- root note name;
- commit hash;
- any placeholders intentionally left in template or setup guides;
- any validation warnings.
