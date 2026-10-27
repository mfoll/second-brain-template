---
type: Guide
related_to: "[[vault]]"
_organized: true
surface_for:
  - "[[vault]]"
---

# Deploy Vault From Template

Use this guide to create a new concrete vault from this template. If the destination repository or vault already exists, stop and follow [[upgrade-existing-vault-from-template|Upgrade an Existing Vault From the Template]] instead. Do not reuse the fresh-deployment commands as an upgrade mechanism.

## Choose the setup path

Start with the folder setup below, or let an agent run it through the agent-led setup that follows. The later GitHub walkthrough is optional when repository history, a verified template snapshot and rollback tags are useful. Global routing, Skills, external-file helpers and automation are separate choices; configure only the features selected by the user.

## Agent-led setup

The README's short setup request points an agent here. The agent runs the minimal folder setup below for the user, with an interview in place of hand-editing, and writes nothing until the user has answered.

1. **Inspect and copy.** Inspect the destination. If a vault already exists there, stop and follow [[upgrade-existing-vault-from-template]]. If the template is not already local, ask before downloading it, then copy it as in minimal step 1, excluding `.git`.
2. **Setup interview.** Ask one question at a time, offering a default or short choices where the runtime supports them, and skip anything the request already answers:
   - a name for the vault and what it is for;
   - what is in scope, what stays out, and what is sensitive;
   - where the user's material lives and which sources the agent may read;
   - which AI tools and accounts may process the notes;
   - storage, backup and retention, and whether to use Git;
   - whether meetings or other people's information will be recorded, and on what agreement (ask only if relevant);
   - what the agent may save without asking each time;
   - the language for notes;
   - whether to use the Brain from other folders, explained as below.
3. **Write the agreed setup.** Apply the answers through minimal steps 2, 3 and 5: [[vault]], `AGENTS.md` and the deployed README with its scope and responsible-use section. Show the user the result.
4. **Start the first focus** through [[procedures/start-a-focus|Start a Focus]] (minimal step 4).
5. **Offer the remaining options** without enabling them by default: importing an existing archive through [[procedures/import-archive|Import an Archive]], installing Skills for discovery, Git history and checkpoints, and the other optional connections. Then archive the setup material (minimal step 6), run the checks and report.

### Explain the choice to use the Brain from other folders

Ask this as its own question, in plain language, because it changes how every session of the selected agent behaves, not only work in the vault. Leave it off unless the user chooses it, and accept either answer.

- **What it does.** It adds one small marked block, about fifteen lines, to the user-level instruction file of each agent the user selects, for example `~/.claude/CLAUDE.md` for Claude Code, `~/.codex/AGENTS.md` for Codex or `~/.gemini/GEMINI.md` for Gemini CLI. The block names the vault folder. Every session of that agent, in any folder, then knows where the Brain is, reads it when earlier context would help, and saves to it when asked.
- **Why choose it.** Work in a code repository, a manuscript folder or any other project can draw on and update the same Brain without opening the vault first.
- **What to weigh.** Agents working on unrelated tasks may read relevant notes and send them to their model provider under that tool's terms. The change applies to all projects using that agent. It installs no Skills, services or automation and grants no permission to share content, change external files or push.
- **If unsure, choose no.** The Brain still works whenever the agent is opened in the vault folder, and this step can be added at any time.
- **Undo.** Remove the block between the `BEGIN SECOND BRAIN` and `END SECOND BRAIN` markers; a recovery copy of the previous file is kept.

If the user chooses it, follow [[procedures/configure-global-agent-instructions|Configure Global Agent Instructions]]: show the exact diff for each selected agent and wait for approval before writing, keep the recovery copy, then verify from another folder that the agent finds the vault.

## Minimal folder setup

1. Make a private copy in a new destination folder, using a downloaded template copy or an existing file-copy tool, and copy the hidden files too: `.agents/` holds the Skill packages and `.gitignore` the exclusions, and Finder drag-and-drop or a copy tool that skips dotfiles would lose them (`cp -R source/ destination/` keeps them). Do not copy a clone's `.git` directory: its `origin` would still point at the template, and a later push would send your notes there. Copy from a downloaded archive, exclude it (`rsync -a --exclude .git source/ destination/`), or delete `destination/.git` after copying. If you enable Git later, run `git init` in the new folder and confirm that `git remote -v` prints nothing before adding your own remote. Preserve any existing destination rather than overlaying it. See [[README]] for the human quickstart and agent setup request.
2. Open the folder in the existing Markdown editor. In [[vault]], replace the `<Vault Name>` heading and the three `<...>` placeholders (outcome, current state, log date) and delete its first line; the scope and privacy boundary are written once, in the README (step 5). Keep existing project documents, repositories and task tools in their canonical locations.
3. If agents will use the vault, customize the opening paragraph of its `AGENTS.md` (one sentence on what the vault is for is enough; the scope and privacy boundary themselves go in the README) and remove the section explicitly limited to the reusable template checkout. Its `CLAUDE.md` and `GEMINI.md` import those daily rules. Keep existing instruction files when joining an established setup; add only a needed memory section or import. Ordinary vaults retire the control-only multi-vault Procedure following the checklist under Retire The Control-Only Multi-Vault Procedure below.
4. Start from one real focus and one non-sensitive piece of useful material. Follow [[procedures/start-a-focus|Start a Focus]], or [[README#Start your first focus|Start your first focus]] by hand: interview the user about what they want to achieve, propose the smallest structure using existing Types, explain it in ordinary language, then create the agreed notes. Reuse existing notes where possible. Do not require a complete taxonomy or a bulk import.

   A typical start is a Responsibility (an ongoing area), a Project under it (a finite outcome), and a Source for an external reference. An internal idea can update the Project or use another suitable Type. For manual setup, use [[responsibility]], [[project]] and the selected knowledge Type templates. Use kebab-case files at the vault root: the Project has `belongs_to: "[[your-responsibility]]"`, the Source has `belongs_to: "[[your-project]]"`, and the Project links the useful note through `has` or its body.

   Verify that the files open and the material is retrievable from the Project. With an agent, try a fresh conversation asking what was saved, why it matters and what remains to do. Then tick the first Next Action in [[vault]]. The optional `python3 -I .agents/skills/lint-vault/scripts/hierarchy_audit.py . --tree` checks the hierarchy; it needs only Python 3.9 or later and works with or without Git.
5. Replace the template README with the short vault README under Customize README below. It records the scope, privacy boundary, AI tools and accounts, storage, backup and retention agreed once; [[vault]] and `AGENTS.md` refer to it rather than repeating it. Use the existing backup method, adding Git history only if selected. Keep `LICENSE` and applicable `THIRD_PARTY_NOTICES.txt` with retained template material; added content keeps its own ownership and confidentiality.

6. Mark the setup material you no longer need with `_archived: true`: this guide, [[upgrade-existing-vault-from-template]] and [[global-agent-instructions-template]]. They stay as provenance and drop out of active views; the placeholder check below excludes them by filename. In the same change, remove the active routes to them: the "Deploy or upgrade a vault" row of the Workflow router in `AGENTS.md`, and the links to the deployment guide and the global instruction template in [[agent-setup]]. Links from ADRs and Procedures are provenance and stay. Delete `assets/second-brain-overview.png` and its folder if the new README does not use it. Delete the archived guides later if you prefer, after the first checkpoint.

Stop here for a basic notes setup. Report what works and any optional choices still open; do not call unselected integrations installed or failed.

## Choose an everyday capture habit

Begin with direct requests to save supplied material, resume a Project and update it after meaningful work. Help the user try these on their first Project; the practical examples are in [[README#Everyday use|Everyday use]]. Agree one initial capture method rather than requiring an Inbox, a source integration or automation. An Inbox and the reusable [[ready-to-ingest]] scratchpad support optional deferred organization and require no particular viewer.

If repeated manual work later justifies a connection, configure it separately with explicit sources, privacy boundaries, review and write permissions. The template does not connect email, recordings or other applications. Preserve the user's existing tools; do not infer permission to read an account or schedule a job from a request to set up the vault.

## Optional connections

- To use the Brain from other project folders, follow [[procedures/configure-global-agent-instructions]] to add a small global routing block. Preserve existing instructions and use their generator when applicable.
- To connect a particular existing project, add a marked memory section through [[procedures/initialize-project-memory]], preserving its technical rules.
- For discoverable workflow shortcuts, select retained Skills and follow [[procedures/configure-agent-skill-discovery]]. The link installer does not install instruction files.
- For external-file helpers, saved views or automation, use only the corresponding sections below. Basic note use needs no Python, shell installer, service or schedule.

## Optional GitHub walkthrough

The remaining steps provide a reproducible Git-backed deployment. Keep the template snapshot, rollback and content-review checks when using this route; apply integration sections only to the features selected during setup.

## Inputs

For the GitHub route, collect these values before changing files; external-file settings are needed only when that feature is selected:

- `<NEW_VAULT_NAME>`
- `<TEMPLATE_REPOSITORY>`: the reviewed GitHub template in `OWNER/REPOSITORY` form.
- `<REVIEWED_TEMPLATE_COMMIT>`: the exact reviewed template commit to deploy.
- `<REVIEWED_TEMPLATE_TREE>`: the tree hash derived from that commit during preflight and checked after repository creation.
- `<GITHUB_OWNER>`
- `<REPOSITORY_NAME>`
- `<LOCAL_DESTINATION_ROOT>`
- `<VAULT_SCOPE>`
- `<VAULT_ROOT_NOTE>`
- `<EXTERNAL_PROJECT_FILE_STRATEGY>`: choose `convention-based`, `linked-per-project`, or `workspace-only`.
- `<ATTACHMENTS_POLICY>`: choose `disabled` or `tracked-vault-assets-only`.
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

Rename or edit [[vault]] to match `<VAULT_ROOT_NOTE>` if needed. Replace `<Vault Name>` with `<NEW_VAULT_NAME>`. Fill in purpose, first workflows, and first next actions for `<VAULT_SCOPE>`; link the README for the scope and privacy boundary instead of repeating them. Replace the `YYYY-MM-DD` placeholders in its Maintenance Log with real dates or remove the lines.

If the root note is renamed, update wikilinks that point to [[vault]].

## Customize README

Replace the template README with a short README for the concrete vault. The template documentation remains available in the upstream repository and in the two reference Guides, [[model-reference]] and [[agent-setup]], which stay in the vault. A starting point:

```markdown
---
type: Guide
related_to: "[[vault]]"
_organized: true
---

# <NEW_VAULT_NAME>

A Second Brain for <VAULT_SCOPE>, deployed from the Second Brain template
(<TEMPLATE_URL>: the repository or folder you copied from; drop this line if none).
Start from [[vault]]; agents follow [[AGENTS]].

## Scope and responsible use

Agreed once at setup; agents reuse these boundaries without asking again and ask only when a new source, tool or destination changes them.

- In scope: <what this vault records>.
- Out of scope: <what stays elsewhere, such as private or confidential material>.
- Sources it may use: <documents, folders, tools>.
- AI tools and accounts that may process it: <approved tools>.
- Storage, backup and retention: <where the folder lives, how it is backed up, how long material is kept; "local folder, no backup yet" is an honest answer>.
- Recording and people: <whether meetings may be recorded or transcribed, who must agree first, and what is kept about people>.

## Everyday use

Work from [[vault]] or the relevant Project. With an agent, ask “Save this useful idea or reference under my project”, “Where did we leave this?” or “Update what we decided and what comes next”. Review what was saved and try finding it again from the Project. Without an agent, make the same updates directly in the notes.

Start with material you supply manually. An Inbox, source connections and automation are optional additions when they fit your routine. Agents use only the sources and actions agreed in the scope and responsible-use section.

## Reference

[Model Reference](model-reference.md) · [Agent Setup](agent-setup.md) · [Licence](LICENSE)
```

The scope and responsible-use section is the deployed vault's permanent record of the boundaries agreed at setup; keep it, since `AGENTS.md` and [[vault]] refer to it. The template-only warnings are not needed.

## Customize AGENTS

Keep the vault conventions, but update wording that should name the concrete vault scope. Do not add machine-local paths.

Customize the deployed vault's `AGENTS.md` for the vault's purpose, privacy boundary, evidence standards, and domain-specific workflows. Do not copy every template, work/control-vault, or personal-vault rule wholesale when the deployed vault has a different role.

Use the responsible-use section in [[README]] to agree source scope, AI tools/accounts, storage destinations, backup and retention during setup. Record those choices in the deployed README only; `AGENTS.md` and [[vault]] refer to it. Reuse them for routine work; ask when a material new risk or change of scope requires a decision.

Keep `CLAUDE.md` and `GEMINI.md` as small runtime imports of the daily vault `AGENTS.md`. Preserve runtime-specific instructions when adding an import to an existing file. Do not copy the full rulebook into each runtime file, and do not generate per-runtime vault copies merely because global instructions elsewhere are generated.

## Choose External Project File Strategy

If external project files need a configured strategy, choose and record one in the deployed README or linked setup guide. Preserve established file locations; this is not a requirement to move existing documents:

- `convention-based`: durable non-versioned project files live beneath one configured external root, normally in `<project-slug>/`;
- `linked-per-project`: each Project links a confirmed external folder through a dedicated Source note; use this when folders are assigned independently, such as per-project shared-drive or OneDrive locations;
- `workspace-only`: the deployment expects only Git-tracked or reproducible project artifacts until a Project explicitly adds an external Source location.

For every strategy, keep concrete machine paths out of committed vault rules. Resolve external roots through ignored `.local/roots.yml`; store only `root_key` plus `relative_path` in Source notes. Use an ignored project `.tmp/` for task-specific temporary files and `/tmp/` for truly disposable files.

Choose `<ATTACHMENTS_POLICY>` separately. `disabled` forbids a generic vault `attachments/` folder. `tracked-vault-assets-only` permits only small assets that are intentionally tracked by Git and belong to the vault itself; it never permits durable unversioned project outputs.

## Customize Type Localization

Keep canonical type identity stable across vaults: filenames, H1s, and `type:` values should stay in English, for example `Person`, `Project`, `Operation`, and `Event`.

If the deployed vault should display localized type names, set `_sidebar_label` on the Type note instead of translating the canonical type. For a French personal vault, use labels such as:

```yaml
_sidebar_label: Personnes
```

Do not create translated type identities such as `Personne` unless the user explicitly wants an incompatible local ontology. An older deployed vault is outside this fresh-deployment workflow; follow [[upgrade-existing-vault-from-template]] and scope any graph-wide Type migration separately rather than normalizing it implicitly.

## Configure Global Instruction Routing

This connection is optional for work from other folders. If selected, follow [[procedures/configure-global-agent-instructions|Configure Global Agent Instructions]], preview the exact diff and preserve a private recovery copy. Choose one instruction owner for each selected runtime; preserve unrelated guidance and update an existing Brain section rather than adding a duplicate.

### Existing controlled multi-vault system

Use the routing/control system's documented executable global-instruction source. Add the new logical vault role and concrete root there, regenerate or install through that source's normal mechanism, and verify the installed output. Do not copy this vault's [[global-agent-instructions-template]] over the controlled global instructions.

After verification, retain the deployed `global-agent-instructions-template.md` only as `_archived: true`, explicitly non-authoritative provenance while any retained Guide, Procedure, or router still links to it. Delete it only after removing or updating every backlink and route and passing link validation. The routing/control source remains authoritative.

### Standalone vault

Use only the marked block in [[global-agent-instructions-template]]. Replace `<VAULT_ROOT>` and `<VAULT_ROLE>` in the machine-local copy, add or update that block alongside existing guidance, and verify the root contains this vault's `AGENTS.md`. Keep runtime-specific and user instructions intact.

For either mode, an optional memory section in a project's existing instructions names the logical role and entry note but omits concrete roots. Preserve the rest of the file and any generator that owns it. Claude Code v2.1.277 or later can read workspace `AGENTS.md` directly in supported setups. Add a Claude or Gemini import only where the selected runtime needs it, preserving existing content and avoiding a duplicate import.

Verify instruction loading for the runtimes selected for this connection. Skill discovery is a separate optional step after reviewing retained packages.

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

Python-assisted audits are optional. If selected, keep the helpers available until their checks pass. They can run from the reviewed template checkout without installing Skills globally; basic manual validation needs no package installation.

Treat every retained vault-owned Skill as the coherent catalogue/package pair defined by [[skill]]. List both sides:

```bash
find skills -maxdepth 1 -type f -name '*-skill.md' | sort
find .agents/skills -mindepth 2 -maxdepth 2 -type f -name 'SKILL.md' | sort
```

For each active pair, verify the visible note's `package_path`, matching package-directory `name`, catalogue lifecycle, and package-bundled relative support files. A Procedure-backed pair must have a resolvable `wraps` link and name the same Procedure on both sides; a specialized standalone pair must explicitly say that the package owns execution and must not duplicate an existing Procedure. Check documented external prerequisites at execution. Update both sides when shared purpose, ownership, name, path, or lifecycle changes; package-only implementation edits need not churn the catalogue. To retire a Skill, remove the installed package and archive or remove its catalogue note and active routes; record any intentional runtime-only exception.

## Retire The Control-Only Multi-Vault Procedure

[[procedures/review-multi-vault-consistency]] exists only for a vault that routes and coordinates other vaults; the template ships it without a Skill package. In every other deployment, retire it in one change:

1. Add `_archived: true` to `procedures/review-multi-vault-consistency.md` and leave its `status` as it is; the archive flag, not the status, retires a note.
2. Remove the paragraph about the Procedure just below the Workflow router table in `AGENTS.md`, and the paragraph about it at the end of External files and optional automation in [[agent-setup]].
3. Leave the links from [[adr/0008-require-semantic-reachability-and-reversible-compaction|ADR 0008]] and other provenance notes in place; they are history, not active routes.

A control vault that wants a package for it adds the catalogue note and package together, as [[skill]] requires.

Then rerun the catalogue and package listing above; both sides should show the same pairs, eight when the starter selection is kept unchanged.

## Configure Agent Skill Discovery

Only when Skill installation is selected, follow [[procedures/configure-agent-skill-discovery|Configure Agent Skill Discovery]] for those runtimes. Keep `.agents/skills/` canonical and use the provided installer to create machine-local links, preserving existing conflicting entries:

```bash
./scripts/configure-agent-skills.sh --runtime codex
./scripts/configure-agent-skills.sh --runtime codex --check
```

Replace `codex` with `claude` for Claude Code. For another Agent Skills-compatible runtime, pass its documented discovery directory with `--target`; do not guess unsupported paths. In a controlled multi-vault system, use its existing installer and collision policy rather than layering this standalone installer over it.

## Review Saved Views

Open each file in `views/` and confirm that filters match the deployed vault's Type and relationship conventions. Follow [[tolaria-saved-views|Tolaria Saved Views]] for the current file contract. Active views should normally exclude notes with `_archived: true`.

## Configure External Project File Roots

If the deployed vault will point to maintained inputs, outputs, or deliverables outside Git, create `.local/roots.yml` in the deployed vault root and keep it ignored by Git. This file maps portable `root_key` values in Source notes to local folders on this machine.

Example:

```yaml
roots:
  documents_basedir:
    access: guarded-write
    candidates:
      - "~/Documents"
```

Use [[procedures/check-external-raw-references|Check External Raw References]] to verify the local resolver and any external raw-file Source notes. Do not commit `.local/roots.yml`; commit only the Source notes and portable procedures/views.

## Optional recording Recaps

If the user enables [[recap|Recap]], follow [[procedures/prepare-recording-recaps]] and document the selected meeting sources, destination vaults, preparation/review hosts, timezone, source and summary retention, and review authority in a deployment guide. Reuse the agreed source/tool scope from setup. Participant suggestions are separately optional: specify the authorized calendar scope, relevant reviewed Person context, conversation-level confirmation and explicit unknown choice. Verify scoped calendar access and the review/decision path before claiming deployment works; observe an ordinary scheduled cycle separately if one is configured. Keep machine-local calendar identifiers, raw recordings and runtime state outside Git and the template. Existing pending reviews must survive upgrades. This interface does not record meetings, enable a schedule or authorize personal-calendar access.

## Configure Per-Vault Automations

Review [[vault-automations]] only if recurring help is useful. Collection jobs may prepare proposed knowledge updates from selected messages, documents, links or meeting material; maintenance jobs diagnose structure or usefulness. Source connections and schedulers are configured separately, never activated by this template.

Start from a useful manual run, then choose the job’s sources, review, permissions and cadence. Leave ready ingestion unscheduled unless selected. Examples include optional ready-intake processing and read-only maintenance:

- process [[ready-to-ingest]] manually with [[procedures/process-ready-ingestion-inbox]], then schedule it only after the workflow and privacy boundary have been observed;
- run read-only [[procedures/lint-vault]];
- run read-only [[procedures/review-vault-health]].

Do not deploy `review-multi-vault-consistency` into ordinary vaults. That workflow belongs only in a vault explicitly designated as the routing/control vault for a multi-vault setup.

Each automation must run with this deployed vault as its working directory, not with another vault's working directory. If the user enables a schedule, let them choose the cadence, record its time zone and active or paused state in the deployed vault's automation guide, and stagger it against other vault jobs. The template defines no default ready-ingestion cadence or start time.

For any write-capable automation that should push unattended, decide and document the exact allowed Git command before enabling the job. Prefer narrow persisted command approval such as `git push origin <TARGET_BRANCH>`, after verifying the intended remote and branch, rather than broad global full access. This is only an execution mechanism; the automation still needs explicit repository, scope, and push authorization. Update the deployed vault's automation guide and the machine-local global agent instructions with the automation name, working directory, allowed command, and stop conditions. Read-only automations must explicitly say not to edit, stage, commit, or push.

Do not let a work/control vault automation read or maintain a private vault's contents unless the user explicitly asks for that vault to be inspected.

## Validate Placeholders

Search for placeholders in notes, excluding the setup material that keeps them by design:

```bash
grep -R "<[A-Z0-9_]*>" -n --include='*.md' . \
  | grep -v -E '(^|/)(deploy-vault-from-template|upgrade-existing-vault-from-template|global-agent-instructions-template|vault-automations)\.md|procedures/configure-' \
  || true
```

The excluded files are setup guides and configuration snippets that legitimately contain `<PLACEHOLDER>` tokens; archive them with `_archived: true` once setup is done (minimal step 6). An empty result is a pass (the trailing `|| true` keeps the exit status at 0). The pattern does not catch `YYYY-MM-DD` lines or `<Vault Name>` prose in [[vault]]; replace those by hand.

## Validate Scope

Review the changed files and confirm that the deployed vault contains only content appropriate for `<VAULT_SCOPE>`. Remove template-only examples, private material that does not belong in the new vault, generated dumps, local machine paths, credentials, and unrelated project content before committing.

## Validate the selected setup

For the GitHub walkthrough, complete the applicable checks below before checkpointing and record skipped integrations as unselected. Resolve hard errors in selected features; record the rationale for non-blocking warnings. The basic folder route uses its smaller validation above.

### Mechanical validation

- Follow [[procedures/lint-vault|Lint Vault]] for structural checks. When Python-assisted audits are selected, run `python3 -I .agents/skills/lint-vault/scripts/contracts_audit.py <LOCAL_DESTINATION_ROOT>/<REPOSITORY_NAME>`, `python3 -I .agents/skills/lint-vault/scripts/compactness_audit.py <LOCAL_DESTINATION_ROOT>/<REPOSITORY_NAME>`, `python3 -I .agents/skills/lint-vault/scripts/tolaria_icon_audit.py <LOCAL_DESTINATION_ROOT>/<REPOSITORY_NAME>`, `python3 -I .agents/skills/lint-vault/scripts/hierarchy_audit.py <LOCAL_DESTINATION_ROOT>/<REPOSITORY_NAME>` and `python3 -I .agents/skills/lint-vault/scripts/links_audit.py <LOCAL_DESTINATION_ROOT>/<REPOSITORY_NAME>`; link validation passes when the links audit reports zero errors.
- Verify frontmatter, first H1s, Type resolution, portable wikilinks, relationships, `_archived` exclusions, and saved-view syntax.
- Confirm active Projects have usable resumption sections. Where a human view exists, validate its small, deliberate membership through [[procedures/maintain-project-human-view|Maintain Project Human View]]; absence of a view is valid.
- Confirm every retained Skill catalogue/package pair satisfies [[skill]] and has either a resolvable matching Procedure or explicit specialized standalone ownership.
- For installed Skills, follow [[procedures/configure-agent-skill-discovery|Configure Agent Skill Discovery]] and require its `--check` mode to report zero unresolved entries in each selected discovery directory.
- Re-run the placeholder and scope checks, then inspect the complete Git diff.

### Semantic validation

- Re-read the customized `AGENTS.md` and confirm its scope, privacy, language, evidence, authorization, and automation behavior are coherent.
- Confirm Type semantics and detailed Procedures remain reachable through the instruction router, root Project, or installed Skills when a task needs them.
- Confirm control-vault-only Skill packages and active routes are absent from ordinary vaults; any retained Procedure is clearly archived provenance.
- Record intentional deviations from the template instead of treating byte-for-byte equality as success.

### Retrieval validation

Test the deployed system through its intended entry points:

1. open the vault directly, or resolve its logical role through global instructions when that connection was installed;
2. open the root or primary Project and identify its outcome, current blocker, and next three actions;
3. follow a Project link to a relevant note; also exercise a project view if one was configured;
4. retrieve one Procedure through a task route and, when retained, its Skill package;
5. retrieve one Source provenance or external-location pointer when the vault uses external files.

For each runtime with Skills installed, perform Skill-package retrieval through its actual discovery surface. For instruction integration, confirm that pre-existing technical guidance still loads alongside the memory section and that a repeated installation would produce no duplicate block.

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

After the commit and applicable validation for this GitHub walkthrough, create and verify a dated reviewed tag. Use a unique suffix if the name already exists:

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
