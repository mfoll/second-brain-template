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

Confirm the template checkout is clean:

```bash
git status --short --branch
```

Confirm the target repository does not already exist unless the user explicitly wants to reuse it:

```bash
gh repo view <GITHUB_OWNER>/<REPOSITORY_NAME>
```

If the command succeeds, stop and ask before reusing the repository. If it fails because the repository does not exist, continue.

Confirm the destination folder does not already exist:

```bash
test -e <LOCAL_DESTINATION_ROOT>/<REPOSITORY_NAME> && echo "Destination exists" || echo "Destination is available"
```

## Create GitHub Repo From Template

Create the new repository from this template with the chosen visibility:

```bash
gh repo create <GITHUB_OWNER>/<REPOSITORY_NAME> --<PRIVATE_OR_PUBLIC> --template <GITHUB_OWNER>/second-brain-template
```

Use `--private` or `--public` for `<PRIVATE_OR_PUBLIC>` after the user chooses visibility. Default to private when unsure.

## Clone Locally

Clone the new repository under the destination root:

```bash
git clone git@github.com:<GITHUB_OWNER>/<REPOSITORY_NAME>.git <LOCAL_DESTINATION_ROOT>/<REPOSITORY_NAME>
cd <LOCAL_DESTINATION_ROOT>/<REPOSITORY_NAME>
```

Verify the new checkout:

```bash
git status --short --branch
git remote -v
```

## Customize Root Note

Rename or edit [[vault]] to match `<VAULT_ROOT_NOTE>` if needed. Replace `<Vault Name>` with `<NEW_VAULT_NAME>`. Fill in purpose, scope, first workflows, and first next actions for `<VAULT_SCOPE>`.

If the root note is renamed, update wikilinks that point to [[vault]].

## Customize README

Update the README so it describes the concrete vault rather than the template. Remove template-only warnings that no longer apply after deployment, but keep portability and no-secret guidance.

## Customize AGENTS

Keep the vault conventions, but update wording that should name the concrete vault scope. Do not add machine-local paths.

## Customize Global Instruction Placeholders

Use [[global-agent-instructions-template]] to create the machine-local global instruction text. Replace `<VAULT_ROOT>` only in the machine-local instruction surface, not in portable vault notes unless the note is explicitly a local setup note.

## Review Generic Skills

Keep only the generic skills that make sense for the new vault. Remove or archive unused visible Skill notes only if they would confuse users or agents.

Check visible Skill notes against package folders:

```bash
find skills .agents/skills -maxdepth 3 -type f | sort
```

## Review Saved Views

Open each file in `views/` and confirm that filters match the deployed vault's Type and relationship conventions. Active views should normally exclude notes with `_archived: true`.

## Validate Placeholders

Search for placeholders:

```bash
grep -R "<[A-Z0-9_]*>" -n .
```

Expected placeholders may remain in this deployment guide and in [[global-agent-instructions-template]]. Other placeholder hits should be reviewed and replaced before the deployment checkpoint.

## Validate Scope

Review the changed files and confirm that the deployed vault contains only content appropriate for `<VAULT_SCOPE>`. Remove template-only examples, private material that does not belong in the new vault, generated dumps, local machine paths, credentials, and unrelated project content before committing.

## Commit And Push

Review the changed scope:

```bash
git status --short --branch
git diff --stat
git diff
```

Commit and push the customized starting point:

```bash
git add .
git diff --cached --stat
git diff --cached --name-only
git commit -m "Deploy <NEW_VAULT_NAME> from template"
git push
```

## Report Final State

Report:

- local path;
- GitHub repository URL;
- visibility;
- root note name;
- commit hash;
- any placeholders intentionally left in template or setup guides;
- any validation warnings.
