---
type: Procedure
status: Active
belongs_to: "[[vault]]"
related_to:
  - "[[procedures/review-vault-health|Review Vault Health]]"
  - "[[procedures/check-external-raw-references|Check External Raw References]]"
_organized: true
---

# Lint Vault

Use this procedure for read-only mechanical and structural diagnosis. Strategic ontology or usefulness questions belong in [[procedures/review-vault-health|Review Vault Health]].

## Canonical scope

Inventory tracked vault notes. Exclude `.git`, `.agents`, `.local`, attachments, caches, generated output, vendored content, and similar support trees from ordinary note counts and link resolution.

## Checks

- Missing or invalid frontmatter, H1, canonical Type, status, or required lifecycle fields.
- Broken, ambiguous, title-fallback-only, or non-portable wikilinks; orphaned or unreachable active notes.
- Relationship-key drift, duplicated aliases, invalid `surface_for`, saved-view filters using obsolete fields, and configured icon names absent from the pinned Phosphor catalogue. Confirm compatibility in the current viewer before treating a catalogue difference as an invalid icon.
- Active Projects missing useful resumption sections; validate human-view contracts only when a saved view exists. A missing human view is not itself a lint finding, and `Project view: false` is optional documentation rather than a required exemption.
- Project `has` lists or views that have become exhaustive rather than selective.
- Sources without human-visible provenance; external Source bridges missing `storage_system`, `root_key`, `relative_path`, `access`, or `last_checked`.
- ADRs, Procedures, and project pointers that violate their current contracts.
- Skill pair drift: a visible active Skill without its `package_path`, an installed package without an active catalogue note, a package-directory/`name` mismatch, a missing package-bundled relative support file, or an archived catalogue note whose package remains discoverable under `.agents/skills/`. For Procedure-backed pairs, also flag missing or divergent Procedure pointers; for standalone pairs, flag missing explicit package ownership or a duplicated existing Procedure. Treat semantic purpose or lifecycle drift as a warning unless executable behavior contradicts it; document and check external prerequisites at execution. Allow only documented runtime-only exceptions.
- Hierarchy drift against [[adr/0011-root-belongs-to-at-responsibilities-and-home-exploration-clusters-in-topics|ADR 0011]]: Projects without `belongs_to` or parented by a Topic not flagged `hierarchy_root: true`, durable notes whose `belongs_to` chain reaches no Responsibility, Project or Topic, notes reachable only through `has`, notes with two parents at the same distance and no `accepted_double_parent: true`, Note, Concept, Person or Source notes acting as parents of three or more notes while reaching no hub themselves, and clusters of three or more `related_to`-only notes sharing a first link. Recaps, Guides, Operations, archived notes, Persons without an affiliation hub, and the notes of any Type whose definition carries `hierarchy_exempt: true` are exempt.
- Unscoped local paths, credentials, caches, or generated dumps in portable notes.

Type-aware compactness warnings:

- Vault `AGENTS.md` above 2,000 words; an added workspace memory section above 80 words; a specialized pointer above 300 without a real safety reason. Preserve the existing project's technical instructions; these pointer targets do not limit the full file.
- Active Project above 1,500 body words; above 3,000 requires a structural split or explicit justification.
- Project Current State above 250 words, more than 10 unchecked actions, or more than five Maintenance Log entries.
- In Projects, Responsibilities, Topics, Guides and Operations: a `##` heading that carries a date (a bare year is allowed), sections below `## Maintenance Log`, or more than one Maintenance Log heading. These mark session output appended instead of reconciled into the owning section.
- Question above 750 body words: review whether its answer or analysis belongs in maintained synthesis.
- Source, Event, or Method above 2,000 body words: preserve the payload, but require a concise opening summary rather than blanket shortening.

Compactness findings are triage signals only. The goal is the smallest trustworthy resumption surface, not a lower word count or fewer notes for its own sake. Valid outcomes include no change, safe wording reduction, reorganization or better routing, and a structural split. Reorganization is often the right response when detail remains useful but obscures current state. Recommended follow-up must say `review and route` rather than imply blanket shortening. A focused fix must not delete unique durable content until a preservation ledger identifies and verifies a canonical destination for each removed block.

## Follow-up routing and confirmation

For a scheduled diagnostic run, identify the current responsible Codex task, if one exists, for each actionable finding. Match narrowly from the affected Project or workspace, exact task title, and recent activity; task summaries are orientation only, not authority.

Report the candidate task, why it appears responsible, and the proposed focused workflow to the user. Do not message or resume that task until the user confirms. If no relevant task is found, say so and propose completing the focused follow-up in the current task. After confirmation, send a preservation-first brief that names the finding, canonical procedure, validation required, and the prohibition on deleting unique information or pushing without separate authorization.

## Steps

1. Inspect Type definitions and the canonical tracked-note tree.
2. Run `.agents/skills/lint-vault/scripts/contracts_audit.py <vault-root>` for required note headers, declared Types and Skill-pair contracts (its sibling `links_audit.py` must be present), then `.agents/skills/lint-vault/scripts/compactness_audit.py <vault-root>` for deterministic compactness warnings, `.agents/skills/lint-vault/scripts/tolaria_icon_audit.py <vault-root>` for saved-view and frontmatter icon names, then `.agents/skills/lint-vault/scripts/hierarchy_audit.py <vault-root>` for `belongs_to` hierarchy drift (add `--tree` to print the inferred home tree), and `.agents/skills/lint-vault/scripts/links_audit.py <vault-root>` for unresolved or ambiguous wikilinks, missing relative Markdown link targets and relationship values that are not wikilinks. Verify warned emoji or URL icons in the current Tolaria UI.
3. Verify findings against the actual files; broad search output is not proof.
4. Report errors and warnings by severity and note. Treat compactness thresholds as review signals, not arbitrary failures. Include responsible-task candidates and proposed follow-up workflows, but wait for user confirmation before contacting a task.
5. Stay read-only unless the user asks for focused fixes. Do not process Inbox, rewrite summaries, normalize broad relationships, or delete notes from lint.

## Automated coverage and manual review

`contracts_audit.py` checks required frontmatter, H1 outside code, canonical Type names from root Type definitions, active Skill/package pairs, package names, wrapped Procedure paths and explicit package support paths. Its top-level scalar parser is not a general YAML validator. Link, hierarchy, compactness and icon helpers cover the named checks above.

Manual review remains necessary for source fidelity, write authority, useful resumption, Type-specific required fields and lifecycle, saved-view semantics, ambiguous naming and standalone Skill ownership. A green CI run establishes only the automated checks, not every item in this Procedure. Test the contract helper with `python3 -I scripts/test_vault_contracts.py`.

## Hierarchy Heuristic

Hierarchy findings are warnings. Report each list from `hierarchy_audit.py` with a one-line reason per item where one is known, and distinguish drift from deliberate choices recorded in [[adr/0011-root-belongs-to-at-responsibilities-and-home-exploration-clusters-in-topics|ADR 0011]] and in frontmatter: Topics flagged `hierarchy_root: true`, notes flagged `accepted_double_parent: true`, lateral-only Topics, Recaps and Guides outside the hierarchy, and Persons without an affiliation hub. The fix for a `has`-only or homeless note is its own `belongs_to`; the fix for a non-hub parent of many notes is usually a Topic or Responsibility; a `related_to`-only cluster is a promotion candidate for [[procedures/review-vault-health|Review Vault Health]], not a lint fix. Do not re-parent Projects or Responsibilities from lint.

## Refresh the icon-name reference

The optional icon checker reads `.agents/skills/lint-vault/references/phosphor-icon-names.txt`, a list of regular SVG filenames from the MIT-licensed `@phosphor-icons/core` package. It contains no images or application code. Keep the Phosphor copyright and permission notice in `THIRD_PARTY_NOTICES.txt`. The catalogue is an offline identifier check; confirm actual glyphs in the selected viewer.

Maintainers can reproduce the current list from the vault root with Python's standard library. This downloads and verifies a pinned source archive without installing a package or extracting SVGs. Normal vault use requires none of this:

```bash
python3 - <<'PY'
import base64, hashlib, io, json, re, tarfile, urllib.request
from pathlib import Path

version = "2.1.1"
url = f"https://registry.npmjs.org/@phosphor-icons/core/-/core-{version}.tgz"
integrity = "sha512-v4ARvrip4qBCImOE5rmPUylOEK4iiED9ZyKjcvzuezqMaiRASCHKcRIuvvxL/twvLpkfnEODCOJp5dM4eZilxQ=="
data = urllib.request.urlopen(url, timeout=30).read()
actual = "sha512-" + base64.b64encode(hashlib.sha512(data).digest()).decode()
if actual != integrity:
    raise SystemExit("Source archive integrity mismatch")
with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as archive:
    metadata = json.load(archive.extractfile("package/package.json"))
    if (metadata["name"], metadata["version"], metadata["license"]) != ("@phosphor-icons/core", version, "MIT"):
        raise SystemExit("Unexpected source package, version or licence")
    names = sorted({match.group(1) for name in archive.getnames()
                    if (match := re.fullmatch(r"package/assets/regular/([a-z0-9-]+)\.svg", name))})
if not names:
    raise SystemExit("No icon names found")
header = ("# Phosphor icon names (regular SVG filenames)\n"
          f"# Source: @phosphor-icons/core@{version} (MIT)\n"
          f"# Archive: {url}\n"
          f"# Integrity: {integrity}\n"
          "# Refresh: procedures/lint-vault.md\n"
          "# Upstream notice: THIRD_PARTY_NOTICES.txt\n")
Path(".agents/skills/lint-vault/references/phosphor-icon-names.txt").write_text(
    header + "\n".join(names) + "\n", encoding="utf-8")
print(f"Wrote {len(names)} icon names")
PY
```

For a version upgrade, review its package licence and integrity from the official registry, update the pin and notice together, regenerate, and run the icon audit. Check configured icons in the viewer before propagating the reference to another vault.

## Wikilink precedence

Resolve exact vault-relative path stems first, then unique filename stems. H1 or humanized-title matching is fallback only and should be reported when a portable target exists. Ignore clearly illustrative placeholder links in examples.

`links_audit.py` implements this resolver: it strips fenced code blocks and inline code spans before scanning bodies, scans frontmatter separately, reports unresolved and ambiguous targets as errors, title-only matches and missing relative Markdown link targets as warnings, and never reports placeholders inside code. A placeholder in normal prose is a real error until it is moved into a code span.
