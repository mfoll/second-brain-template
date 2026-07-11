---
type: Guide
related_to: "[[vault]]"
_organized: true
surface_for:
  - "[[vault]]"
---

# Deploy Vault From Template

Use this guide to create a new concrete vault from this template. If the destination repository or vault already exists, stop and follow [[upgrade-existing-vault-from-template|Upgrade an Existing Vault From the Template]] instead. Do not reuse the fresh-deployment commands as an upgrade mechanism.

## Inputs

Collect these values before changing files:

- `<NEW_VAULT_NAME>`
- `<TEMPLATE_REPOSITORY>`: the reviewed GitHub template in `OWNER/REPOSITORY` form.
- `<REVIEWED_TEMPLATE_COMMIT>`: the exact reviewed template commit to deploy.
- `<REVIEWED_TEMPLATE_TREE>`: the tree hash derived from that commit during preflight and checked after repository creation.
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

Confirm this checkout's `origin` is `<TEMPLATE_REPOSITORY>`, then verify that `<REVIEWED_TEMPLATE_COMMIT>` is the exact current tip of the template's remote default branch. GitHub's template action creates from that tip and does not accept a reviewed commit argument, so ancestry alone is insufficient.

```bash
git remote get-url origin
git fetch origin --prune
test "$(gh repo view <TEMPLATE_REPOSITORY> --json isTemplate --jq '.isTemplate')" = "true"
TEMPLATE_DEFAULT_BRANCH="$(gh repo view <TEMPLATE_REPOSITORY> --json defaultBranchRef --jq '.defaultBranchRef.name')"
git cat-file -e '<REVIEWED_TEMPLATE_COMMIT>^{commit}'
test "$(git rev-parse HEAD)" = "$(git rev-parse <REVIEWED_TEMPLATE_COMMIT>)"
test "$(gh api repos/<TEMPLATE_REPOSITORY>/commits/<REVIEWED_TEMPLATE_COMMIT> --jq '.sha')" = "$(git rev-parse <REVIEWED_TEMPLATE_COMMIT>)"
test "$(git rev-parse "origin/${TEMPLATE_DEFAULT_BRANCH}")" = "$(git rev-parse <REVIEWED_TEMPLATE_COMMIT>)"
git rev-parse '<REVIEWED_TEMPLATE_COMMIT>^{tree}'
```

Record the final command's output as `<REVIEWED_TEMPLATE_TREE>`. The repository must be a GitHub template; the API result, local `HEAD`, and remote default-branch tip must all equal the reviewed commit. If any check fails, stop. Push or merge the candidate into the remote default branch and review that exact tip first; a local-only commit or an unreviewed newer tip cannot be deployed safely through GitHub's template action.

Confirm the target repository does not already exist unless the user explicitly wants to reuse it:

```bash
gh repo view <GITHUB_OWNER>/<REPOSITORY_NAME>
```

If the command succeeds, use [[upgrade-existing-vault-from-template|Upgrade an Existing Vault From the Template]] or ask before choosing another repository. If it fails because the repository does not exist, continue.

Confirm the destination folder does not already exist:

```bash
test -e <LOCAL_DESTINATION_ROOT>/<REPOSITORY_NAME> && echo "Destination exists" || echo "Destination is available"
```

## Create GitHub Repo From Template

Create the new repository from the reviewed template with the chosen visibility:

```bash
gh repo create <GITHUB_OWNER>/<REPOSITORY_NAME> <VISIBILITY_FLAG> --template <TEMPLATE_REPOSITORY>
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
test "$(git rev-parse 'HEAD^{tree}')" = "<REVIEWED_TEMPLATE_TREE>"
```

If the tree check fails, stop before customization. The generated repository does not match the reviewed template snapshot.

Before customization, record the new repository's baseline commit and create a dated rollback tag. Use a unique suffix if the name already exists:

```bash
git rev-parse HEAD
git tag before-vault-customization-YYYY-MM-DD
git show --no-patch --oneline before-vault-customization-YYYY-MM-DD
```

Create a vault-local deployment Event or equivalent ledger that records `<REVIEWED_TEMPLATE_COMMIT>`, `<REVIEWED_TEMPLATE_TREE>`, this baseline commit and tag, planned interface changes, validation results, and the final reviewed commit. Match its detail to the destination repository's privacy boundary; omit sensitive local names or content from a shared repository. The tag is recovery infrastructure; the ledger makes selective restoration understandable.

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

Do not create translated type identities such as `Personne` unless the user explicitly wants an incompatible local ontology. An older deployed vault is outside this fresh-deployment workflow; follow [[upgrade-existing-vault-from-template]] and scope any graph-wide Type migration separately rather than normalizing it implicitly.

## Configure Global Instruction Routing

First choose one of the two deployment modes in [[procedures/configure-global-agent-instructions|Configure Global Agent Instructions]]. Do not combine them.

### Existing controlled multi-vault system

Use the routing/control system's documented executable global-instruction source. Add the new logical vault role and concrete root there, regenerate or install through that source's normal mechanism, and verify the installed output. Do not copy this vault's [[global-agent-instructions-template]] over the controlled global instructions.

After verification, retain the deployed `global-agent-instructions-template.md` only as `_archived: true`, explicitly non-authoritative provenance while any retained Guide, Procedure, or router still links to it. Delete it only after removing or updating every backlink and route and passing link validation. The routing/control source remains authoritative.

### Standalone vault

Use [[global-agent-instructions-template]] as the source for the Second Brain block in the machine-local instruction surface. Replace `<VAULT_ROOT>` and `<VAULT_ROLE>` only there, merge narrowly around unrelated custom guidance, and verify the configured root contains this vault's `AGENTS.md`.

For either mode, project-local `AGENTS.md` pointers name the logical role and entry note but omit concrete roots. Add a minimal project-local `CLAUDE.md` shim importing `AGENTS.md` when needed. Do not duplicate vault policy into project pointers.

Likewise, keep deployment guides only when they remain useful. If retained only as provenance, mark them `_archived: true`, remove them from active `AGENTS.md`, README, root-Project, and `surface_for` routes, and state that they are not active workflows. If deleting one, update every backlink in the same change and pass link validation.

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

Keep only the generic skills that make sense for the new vault. For an unused vault-owned Skill, remove its installed package and archive or remove its visible catalogue note plus active routes in the same change. Do not leave a dormant package under `.agents/skills/`, where runtimes may still discover it.

Keep the `lint-vault` package available through mandatory validation. If the final deployment intentionally omits it, validate first, remove its pair and routes, then rerun the mechanical checks with the helper from the reviewed template checkout or an equivalent reviewed tool.

Treat every retained vault-owned Skill as the coherent catalogue/package pair defined by [[skill]]. List both sides:

```bash
find skills -maxdepth 1 -type f -name '*-skill.md' | sort
find .agents/skills -mindepth 2 -maxdepth 2 -type f -name 'SKILL.md' | sort
```

For each active pair, verify that the visible note's `package_path` exists, its `wraps` link resolves to an existing Procedure, the package directory matches the package `name`, and both sides name the same Procedure, purpose, and lifecycle. Verify named scripts or support files. Add or update both sides together. To retire a Skill, remove the installed package and archive or remove its catalogue note and active routes; record any intentional runtime-only exception.

## Review Saved Views

Open each file in `views/` and confirm that filters match the deployed vault's Type and relationship conventions. Follow [[tolaria-saved-views|Tolaria Saved Views]] for the current file contract. Active views should normally exclude notes with `_archived: true`.

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

## Mandatory Deployment Validation

Do not checkpoint or report the deployment complete until all four groups pass. Resolve hard errors; only non-blocking warnings may remain when their rationale and consequence are explicitly recorded in the deployment ledger.

### Mechanical validation

- Follow [[procedures/lint-vault|Lint Vault]] and run `.agents/skills/lint-vault/scripts/compactness_audit.py <LOCAL_DESTINATION_ROOT>/<REPOSITORY_NAME>`.
- Verify frontmatter, first H1s, Type resolution, portable wikilinks, relationships, `_archived` exclusions, and saved-view syntax.
- Confirm active Projects have usable resumption sections and deliberate 4–10-note human views unless explicitly opted out.
- Confirm every retained Skill catalogue/package pair satisfies [[skill]] and has a resolvable Procedure.
- Re-run the placeholder and scope checks, then inspect the complete Git diff.

### Semantic validation

- Re-read the customized `AGENTS.md` and confirm its scope, privacy, language, evidence, authorization, and automation behavior are coherent.
- Confirm Type semantics and detailed Procedures remain reachable through the instruction router, root Project, or installed Skills when a task needs them.
- Confirm template-only control-vault Skill packages and active routes are absent from ordinary vaults; any retained Procedure is clearly archived provenance.
- Record intentional deviations from the template instead of treating byte-for-byte equality as success.

### Retrieval validation

Test the deployed system through its intended entry points:

1. resolve the logical vault role from installed global instructions;
2. open the root or primary Project and identify its outcome, current blocker, and next three actions;
3. follow one project view to a relevant linked note;
4. retrieve one Procedure through a task route and, when retained, its Skill package;
5. retrieve one Source provenance or external-location pointer when the vault uses external files.

Record the query, expected result, files read, and actual result. Link resolution alone does not prove useful retrieval.

### Rollback validation

- Verify `before-vault-customization-YYYY-MM-DD` still resolves to the recorded baseline commit.
- In the deployment ledger, list every removed or archived template interface and any useful replacement location.
- Record `<REVIEWED_TEMPLATE_COMMIT>`, the baseline commit, final commit, validation results, and selective restoration instructions.
- Do not prescribe destructive reset as the normal rollback path.

## Checkpoint And Optional Push

Review the changed scope:

```bash
git status --short --branch
test "$(git branch --show-current)" = "<TARGET_BRANCH>"
git diff --stat
git diff
```

If the branch check fails, stop and create or switch to the intended branch under the repository's current branch policy before staging.

Stage only the reviewed deployment files. Replace the example paths with the exact task-scoped files; do not use `git add .`:

```bash
git add -- <PATH_1> <PATH_2>
git diff --cached --stat
git diff --cached --name-only
git diff --cached
git commit -m "Deploy <NEW_VAULT_NAME> from template"
```

After the commit and mandatory validation, create and verify a dated reviewed tag. Use a unique suffix if the name already exists:

```bash
git tag vault-deployment-reviewed-YYYY-MM-DD
git show --no-patch --oneline vault-deployment-reviewed-YYYY-MM-DD
```

Push only when the user's current authorization permits it and after verifying the intended remote and branch:

```bash
git remote -v
test "$(git branch --show-current)" = "<TARGET_BRANCH>"
git push origin <TARGET_BRANCH>
```

If push is not authorized, stop after the local commit and report that the checkpoint remains local. Follow [[procedures/git-checkpoint-vault-changes|Git Checkpoint Vault Changes]] for scope review and authorization.

## Report Final State

Report:

- local path;
- GitHub repository URL;
- visibility;
- root note name;
- reviewed template commit, baseline commit and rollback tag;
- commit hash;
- reviewed deployment tag;
- whether push was authorized and performed, including the remote and branch when applicable;
- any placeholders intentionally left in template or setup guides;
- mechanical, semantic, retrieval, and rollback results, including any recorded warnings.
