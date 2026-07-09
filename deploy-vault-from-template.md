---
type: Guide
related_to: "[[vault]]"
_organized: true
surface_for:
  - "[[vault]]"
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
- `<TARGET_BRANCH>`: the branch intended for the first reviewed checkpoint, normally `main` for a new deployment.
- `<VISIBILITY_FLAG>`: use `--private` or `--public`; default to `--private` when unsure.

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
gh repo create <GITHUB_OWNER>/<REPOSITORY_NAME> <VISIBILITY_FLAG> --template <GITHUB_OWNER>/second-brain-template
```

Use `--private` or `--public` for `<VISIBILITY_FLAG>` after the user chooses visibility. Default to `--private` when unsure.

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

Customize the deployed vault's `AGENTS.md` for the vault's purpose, privacy boundary, evidence standards, and domain-specific workflows. Do not copy every template, work/control-vault, or personal-vault rule wholesale when the deployed vault has a different role.

Keep `CLAUDE.md` as a root compatibility shim pointing to `AGENTS.md`. Do not duplicate the full instruction body into the shim.

## Customize Type Localization

Keep canonical type identity stable across vaults: filenames, H1s, and `type:` values should stay in English, for example `Person`, `Project`, `Operation`, and `Event`.

If the deployed vault should display localized type names, set `_sidebar_label` on the Type note instead of translating the canonical type. For a French personal vault, use labels such as:

```yaml
_sidebar_label: Personnes
```

Do not create translated type identities such as `Personne` unless the user explicitly wants an incompatible local ontology. If an older deployed vault already has translated type identities, rename the Type note to the canonical English filename/H1, update existing note `type:` values, and preserve the user-facing language through `_sidebar_label`.

## Customize Global Instruction Placeholders

Use [[global-agent-instructions-template]] to create the machine-local global instruction text. Replace `<VAULT_ROOT>` and choose a stable `<VAULT_ROLE>` only in the machine-local instruction surface or generic templates, not in ordinary portable vault notes unless the note is explicitly a local setup note.

When preparing project-local `AGENTS.md` pointers for workspaces attached to this deployed vault, include the deployed vault's logical role, such as `personal`, `work/control`, `research`, or `team`, and continue to omit concrete local vault paths. Add a project-local `CLAUDE.md` shim importing `AGENTS.md` for Claude Code compatibility. Do not duplicate the vault-level project memory writeback policy into project-local pointers.

After the installed global instructions are configured, decide whether `global-agent-instructions-template.md` still belongs in the deployed vault. For ordinary deployed vaults in a multi-vault setup, it usually does not: delete it or archive it as provenance, and rely on the work/control vault's global-instruction source plus this vault's implemented `AGENTS.md`. Keep an active local global-instruction template only for a standalone vault that must bootstrap itself without a separate control vault or template repository.

Likewise, keep deployment guides only when they remain useful. If retained only as deployment provenance, mark them `_archived: true` and state that they are not active workflows.

## Decide Retrieval Needs

Start with direct graph-aware retrieval: Project notes, Type notes, frontmatter, wikilinks, saved views, source notes, `rg`, and file inspection. Small and medium vaults should not need a local retrieval index when notes have clear types, project entry points, and relationships.

Add a local retrieval index only after real use shows a repeated retrieval failure or excessive reading cost. If an index is added, keep the index and model cache machine-local. Do not commit index databases, model caches, or resolved local paths. In the deployed vault, document:

- the benchmarked retrieval problem;
- index scope and privacy boundary;
- collection names or path filters;
- any non-default model or tool dependency;
- refresh cadence and maintenance owner;
- fallback behavior when the index is unavailable or stale;
- the graph-orientation rule agents should use after candidate discovery.

Do not move durable notes to make local indexes cleaner. If type-level retrieval needs emerge, create an ignored generated mirror or symlink layer under `.local/` rather than changing the Tolaria vault structure.

If the deployed vault participates in a multi-vault setup, update the machine-local global agent instructions so agents know whether and when to use that vault's index from external workspaces.

## Review Generic Skills

Keep only the generic skills that make sense for the new vault. Remove or archive unused visible Skill notes only if they would confuse users or agents.

Check visible Skill notes against package folders:

```bash
find skills .agents/skills -maxdepth 3 -type f | sort
```

## Review Saved Views

Open each file in `views/` and confirm that filters match the deployed vault's Type and relationship conventions. Active views should normally exclude notes with `_archived: true`.

## Configure External Raw Roots

If the deployed vault will point to raw files that stay outside the vault, create `.local/roots.yml` in the deployed vault root and keep it ignored by Git. This file maps portable `root_key` values in Source notes to local folders on this machine.

Example:

```yaml
roots:
  documents_basedir:
    access: guarded-write
    candidates:
      - "~/Documents"
```

Use [[procedures/check-external-raw-references|Check External Raw References]] to verify the local resolver and any external raw-file Source notes. Do not commit `.local/roots.yml`; commit only the Source notes and portable procedures/views.

## Configure Per-Vault Automations

Review [[vault-automations]] and decide whether this deployed vault should have local automations.

Leave ready ingestion disabled and manual-first by default. Start with read-only jobs unless the user explicitly wants a write-capable intake job. Common candidates are:

- process [[ready-to-ingest]] manually with [[procedures/process-ready-ingestion-inbox]], then schedule it only after the workflow and privacy boundary have been observed;
- run read-only [[procedures/lint-vault]];
- run read-only [[procedures/review-vault-health]].

Do not deploy `review-multi-vault-consistency` into ordinary vaults. That workflow belongs only in a vault explicitly designated as the routing/control vault for a multi-vault setup.

Each automation must run with this deployed vault as its working directory, not with another vault's working directory. If the user enables a schedule, let them choose the cadence, record its time zone and active or paused state in the deployed vault's automation guide, and stagger it against other vault jobs. The template defines no default ready-ingestion cadence or start time.

For any write-capable automation that should push unattended, decide and document the exact allowed Git command before enabling the job. Prefer narrow persisted command approval such as `git push origin <TARGET_BRANCH>`, after verifying the intended remote and branch, rather than broad global full access. This is only an execution mechanism; the automation still needs explicit repository, scope, and push authorization. Update the deployed vault's automation guide and the machine-local global agent instructions with the automation name, working directory, allowed command, and stop conditions. Read-only automations must explicitly say not to edit, stage, commit, or push.

Do not let a work/control vault automation read or maintain a private vault's contents unless the user explicitly asks for that vault to be inspected.

## Validate Placeholders

Search for placeholders:

```bash
grep -R "<[A-Z0-9_]*>" -n .
```

Expected placeholders may remain in this deployment guide and in [[global-agent-instructions-template]] while still working from the template repository. In deployed vaults, placeholders should remain only in archived provenance notes or explicitly local setup snippets. Other placeholder hits should be reviewed and replaced before the deployment checkpoint.

## Validate Scope

Review the changed files and confirm that the deployed vault contains only content appropriate for `<VAULT_SCOPE>`. Remove template-only examples, private material that does not belong in the new vault, generated dumps, local machine paths, credentials, and unrelated project content before committing.

## Checkpoint And Optional Push

Review the changed scope:

```bash
git status --short --branch
git diff --stat
git diff
```

Stage only the reviewed deployment files. Replace the example paths with the exact task-scoped files; do not use `git add .`:

```bash
git add -- <PATH_1> <PATH_2>
git diff --cached --stat
git diff --cached --name-only
git diff --cached
git commit -m "Deploy <NEW_VAULT_NAME> from template"
```

Push only when the user's current authorization permits it and after verifying the intended remote and branch:

```bash
git remote -v
git branch --show-current
git push origin <TARGET_BRANCH>
```

If push is not authorized, stop after the local commit and report that the checkpoint remains local. Follow [[procedures/git-checkpoint-vault-changes|Git Checkpoint Vault Changes]] for scope review and authorization.

## Report Final State

Report:

- local path;
- GitHub repository URL;
- visibility;
- root note name;
- commit hash;
- whether push was authorized and performed, including the remote and branch when applicable;
- any placeholders intentionally left in template or setup guides;
- any validation warnings.
