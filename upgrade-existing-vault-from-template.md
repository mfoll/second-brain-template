---
type: Guide
related_to:
  - "[[vault]]"
  - "[[deploy-vault-from-template]]"
_organized: true
surface_for:
  - "[[vault]]"
---

# Upgrade an Existing Vault From the Template

Use this guide to port reviewed generic improvements into an existing deployed vault without replacing its memory, local ontology choices, privacy boundary, instructions, or Git history.

This is a preservation-first comparison, not a template merge. The deployed vault remains authoritative for its content and intentional local behavior. Import only compatible interfaces whose value is understood.

> [!warning]
> An upgrade is a reviewed, human-approved operation, never an unattended or scheduled job. Once a vault is in use, its owner may have edited, superseded or deleted ADRs, Procedures, Skills, Types and `AGENTS.md` sections on purpose, and a template file with the same name is not evidence that the local version is outdated.

Treat every difference in those files as a possible local decision: propose the port file by file, show the diff, and apply only what the owner approves. Never overwrite a local ADR; when a template ADR conflicts with a local one, report the conflict and let the owner decide whether to supersede either.

## Folder-only upgrade

For a vault without Git, keep its existing private backup method. Preserve a recovery copy of the files in scope, inspect the current instructions and notes, and port only the selected compatible sections. Compare retrieval before and after the change. Add a memory block or import alongside existing guidance, using its generator if one owns it. Apply the global-routing and Skill procedures only when those integrations are selected.

The remaining walkthrough supplies Git/GitHub provenance, tags and review checkpoints for repositories that use them. A folder-only upgrade does not need those tools or a new repository.

## Inputs

Confirm:

- `<DEPLOYED_VAULT_ROOT>`;
- `<TEMPLATE_REPOSITORY>` in `OWNER/REPOSITORY` form;
- `<REVIEWED_TEMPLATE_COMMIT>` that has passed template review;
- the deployed vault's role, privacy boundary, and current branch;
- whether a designated routing/control vault owns cross-vault coordination;
- which interface families are in scope: instructions, Types, Procedures, Skills, views, automation documentation, or deployment guides.

If the requested scope is broad or ambiguous, inventory first and propose the file-level port before editing.

## Establish a Rollback Point

Work from the deployed vault. Preserve unrelated work and do not hide a dirty tree:

```bash
cd <DEPLOYED_VAULT_ROOT>
git status --short --branch
git rev-parse HEAD
git branch --show-current
```

If changes already exist, separate them or ask how to proceed. When the tree is reviewed and safe, create a dated pre-upgrade tag at the exact current commit. Use a unique suffix if the name already exists:

```bash
git tag before-template-upgrade-YYYY-MM-DD
git show --no-patch --oneline before-template-upgrade-YYYY-MM-DD
```

Record the branch, commit, tag, requested scope, and template commit in a vault-local migration Event or equivalent deployment ledger. Match its detail to the deployed repository's privacy boundary; do not put private note names or content into a shared control record.

Before editing, record a small baseline retrieval packet from the current deployed interfaces: representative query, expected answer or path, entry files read, and result. Include the root Project, one detailed or historical fact, one Procedure or Skill route, and any safety-critical rule affected by the proposed port. Re-run the same packet after editing so semantic preservation is comparable rather than inferred.

## Verify the Template Source

Confirm `<REVIEWED_TEMPLATE_COMMIT>` exists in the named GitHub template repository and is reachable from its default branch. Do not upgrade from an unpushed local template commit.

```bash
gh repo view <TEMPLATE_REPOSITORY> --json isTemplate,defaultBranchRef,url
gh api repos/<TEMPLATE_REPOSITORY>/commits/<REVIEWED_TEMPLATE_COMMIT> --jq '.sha'
TEMPLATE_DEFAULT_BRANCH="$(gh repo view <TEMPLATE_REPOSITORY> --json defaultBranchRef --jq '.defaultBranchRef.name')"
git fetch https://github.com/<TEMPLATE_REPOSITORY>.git "${TEMPLATE_DEFAULT_BRANCH}"
TEMPLATE_DEFAULT_COMMIT="$(git rev-parse FETCH_HEAD)"
git fetch https://github.com/<TEMPLATE_REPOSITORY>.git <REVIEWED_TEMPLATE_COMMIT>
git merge-base --is-ancestor <REVIEWED_TEMPLATE_COMMIT> "${TEMPLATE_DEFAULT_COMMIT}"
```

The repository must report `isTemplate: true`; the API and ancestry checks must succeed. `FETCH_HEAD` now names the reviewed commit for comparison without merging it:

```bash
git show --no-patch --oneline FETCH_HEAD
```

Use `FETCH_HEAD` only as a read-only comparison source. Never run `git merge FETCH_HEAD`, copy the repository wholesale over the deployed vault, or resolve conflicts by preferring all template files.

## Inventory Before Editing

Read the deployed vault's current `AGENTS.md`, root Project, relevant Type notes, Procedures, visible Skill notes, skill packages, views, automation guide, and accepted ADRs. Inspect only interface files unless the requested validation genuinely requires a content note; keep private content out of cross-vault reviews.

Classify each candidate change as:

- compatible generic improvement to port;
- local rule or content to preserve;
- obsolete local interface to supersede deliberately;
- template-only bootstrap material to omit;
- unresolved conflict requiring user direction.

Compare purpose and semantics, not just filenames. A deployed vault may intentionally omit Types, Procedures, Skills, views, or control-vault workflows.

## Port by Interface Family

Apply the smallest compatible edits manually.

### Instructions

Compare `AGENTS.md` section by section. Preserve the deployed vault's scope, privacy, evidence, language, authorization, automation, and domain-specific rules. Port generic invariants and routes without replacing those local instructions or copying a control vault's policy into an ordinary vault.

Keep only the added memory section short; preserve the rest of the project's instruction file and any generator that owns it. Preview the diff, keep a private recovery copy and reuse the same section or import rather than appending duplicates.

If the reviewed interface scope includes global instruction routing, follow [[procedures/configure-global-agent-instructions|Configure Global Agent Instructions]] and preserve its single-owner split:

- in a controlled multi-vault system, update the existing executable source, run its documented generator or installer, and verify the installed output; do not port or activate the neutral standalone template;
- in a standalone vault, port relevant changes from [[global-agent-instructions-template]] narrowly into the machine-local instruction surface and preserve unrelated custom guidance.

Do not combine the modes. Keep the deployed standalone template `_archived: true` and non-authoritative in controlled mode while retained notes still link to it; delete it only with all backlinks and routes updated in the same validated change.

When retiring any Guide, Procedure, or bootstrap interface, remove it from active `AGENTS.md`, README, root-Project, Skill, and `surface_for` routes. If deleting it, update every backlink in the same change. An archived interface must not remain advertised as active.

### Types and relationships

Read both Type definitions before changing a note contract. Preserve canonical Type identity and valid local fields. Do not add a Type, rename relationship keys, rewrite lifecycle state, or normalize `_` fields merely because the template differs.

### Procedures and Skills

Port a workflow only when the deployed vault needs it. Reusable vault workflows remain in Procedures; their packages require the complete Procedure, which is authoritative on conflict, and may retain operational detail. Prefer thinning only after a clause audit. Preserve an intentional specialized standalone Skill only when no durable Procedure owns it and its catalogue note explicitly identifies the package as the workflow owner.

Treat every installed vault-owned Skill as a coherent pair:

- one visible active `type: Skill` catalogue note with `status` and `package_path`;
- one matching `.agents/skills/<skill-name>/SKILL.md` whose frontmatter `name` matches the package directory;
- both sides describe the same active lifecycle, purpose, and ownership mode: matching `wraps` plus Procedure pointer, or explicit specialized standalone package ownership;
- package-bundled relative scripts or support files named by either side exist, while external or project-local prerequisites are documented for execution checks;
- no active note or package is left orphaned unless a documented runtime-only exception is intentional.

Update both sides when shared purpose, ownership, name, path, or lifecycle changes. To retire a Skill, remove its installed package and archive or remove the catalogue note and active routes; do not leave a dormant package discoverable under `.agents/skills/`. Do not force a standalone package into a fictitious Procedure merely for template conformity; for a Procedure-backed package, the Procedure wins on conflict and duplication is reduced only after a clause audit.

If the upgrade includes runtime discovery, port [[procedures/configure-agent-skill-discovery|Configure Agent Skill Discovery]] and `scripts/configure-agent-skills.sh` together. Run the installer only after the retained Skill set is final. Preserve an existing controlled multi-vault installer and collision policy; do not add a competing set of links.

Port a changed helper together with its referenced resources and applicable upstream notices. Preserve any existing repository licence; adding MIT-licensed template material is not authority to relicense the vault's other content or overwrite its licence file.

### Views and automations

Validate saved-view syntax against [[tolaria-saved-views|Tolaria Saved Views]], preserve deliberate local display choices, and exclude `_archived: true` from active views. Do not activate a schedule merely because the template documents one. Cross-vault review belongs only in a designated routing/control vault.

## Validation for the selected upgrade

For the Git-backed walkthrough, complete the applicable groups before checkpointing. Resolve hard errors in changed interfaces and record the rationale for non-blocking warnings. The folder-only route uses the same preservation and retrieval principles without the Git or unselected-integration commands.

### Mechanical

- Follow [[procedures/lint-vault|Lint Vault]] for affected interfaces. When Python-assisted checks are selected, run the relevant bundled helpers: `compactness_audit.py` and `tolaria_icon_audit.py`.
- Check frontmatter, first H1s, Type resolution, portable wikilinks, relationships, views, active Project surfaces, and orphaned active notes.
- Confirm each installed Skill catalogue/package pair satisfies [[skill]].
- For runtime Skill discovery included in the upgrade, run the authoritative installer in check mode and require zero missing or conflicting retained packages. Instruction-only changes need no Skill installation.
- Inspect `git status`, the complete task-scoped diff, and changed-file list.

### Semantic

- Confirm the deployed vault's scope, privacy, language, evidence, authorization, and automation rules still mean what they did before.
- Confirm Type selection and lifecycle behavior remain reachable from `AGENTS.md` and the workflow router.
- Confirm detailed workflows remain in Procedures and are actually routed or activated where needed.
- Record intentional divergences from the template instead of normalizing them away.

### Retrieval

Test from the same entry surfaces an agent will use:

1. resolve the logical vault role without an embedded project-local root;
2. retrieve the root or primary Project and identify current outcome, blocker, and next actions;
3. retrieve one linked detailed or historical fact without reading unrelated notes;
4. retrieve one Procedure through its task route and, when installed, through its Skill package;
5. resolve one saved project view and one Source provenance or external-location pointer when those features are used.

When runtime discovery changed, perform step 4 through each configured runtime's actual Skill discovery surface.

Record the query, expected answer or path, files read, and result. Compare against the baseline packet recorded before editing. A link checker alone is not a retrieval test.

### Rollback

- Verify the pre-upgrade tag still resolves to the recorded commit.
- Record every changed, added, archived, or removed interface file and where displaced useful detail now lives.
- Record the reviewed template commit and the post-upgrade commit.
- Explain selective restoration from the pre-upgrade tag; do not prescribe a destructive reset.

## Checkpoint

Follow [[procedures/git-checkpoint-vault-changes|Git Checkpoint Vault Changes]]. Stage only reviewed files and make a local task-scoped commit. After validation, create a dated reviewed tag such as the following; use a unique suffix if it already exists:

```bash
git tag template-upgrade-reviewed-YYYY-MM-DD
git show --no-patch --oneline template-upgrade-reviewed-YYYY-MM-DD
```

Push commits or tags only when current authorization explicitly permits it.

## Report

Report the deployed vault, pre-upgrade tag and commit, reviewed template commit, changed interface families, intentional divergences, mechanical and semantic results, retrieval-test results, post-upgrade commit and tag, and whether anything remains local-only.
