---
type: Guide
status: Active
belongs_to: "[[vault]]"
related_to:
  - "[[procedures/maintain-project-human-view|Maintain Project Human View]]"
  - "[[procedures/lint-vault|Lint Vault]]"
_organized: true
---

# Tolaria Saved Views

Use this guide when creating or editing a saved view. Bundled Tolaria agent documentation remains authoritative for current product behavior; this note preserves the portable vault syntax and naming conventions. Inspect a nearby working view before introducing a new pattern.

Saved views are YAML files under `views/`. The kebab-case filename is the stable identifier. Do not create legacy JSON view files.

```yaml
name: Open Questions
icon: null
color: null
sort: modified:desc
listPropertiesDisplay:
  - type
  - status
filters:
  all:
    - field: type
      op: equals
      value: Question
    - field: status
      op: equals
      value: Open
    - field: _archived
      op: not_equals
      value: true
```

## Syntax contract

- `name` is required. `icon`, `color`, `sort`, and `listPropertiesDisplay` are optional.
- `sort` uses `option:direction`. Built-ins include `modified`, `created`, `title`, and `status`; custom fields use `property:<field>:asc` or `:desc`.
- `filters` has exactly one root `all:` or `any:` group. Conditions use `field`, `op`, and usually `value`; nested groups are allowed.
- Operators are `equals`, `not_equals`, `contains`, `not_contains`, `any_of`, `none_of`, `is_empty`, `is_not_empty`, `before`, and `after`. `any_of` and `none_of` take YAML lists. `regex: true` works with equality and containment operators.
- Relationship filters use canonical lowercase fields and quoted wikilinks, for example `value: "[[vault]]"`.

## Icon contract

Tolaria accepts three forms: a name from its curated icon registry, one emoji, or an HTTP(S) image URL. For a named icon, Phosphor-style kebab-case is necessary but not sufficient: a plausible name may still resolve to no glyph. Prefer choosing the icon in the current Tolaria picker. When editing YAML directly, use only a name already verified by that picker and by `.agents/skills/lint-vault/references/tolaria-icon-names.txt`; never infer a name from Lucide or from the full Phosphor catalogue. Keep `icon: null` when no verified icon is needed.

After any direct view edit, run `.agents/skills/lint-vault/scripts/tolaria_icon_audit.py <vault-root>`, reload Tolaria, and confirm that the glyph is visible. The helper certifies names present in the snapshot; it reports non-registry values, including emoji and URLs, for visual confirmation without claiming to validate them. The current picker remains authoritative. If it offers a name missing from the bundled snapshot, refresh the reference in the neutral template first, then port the reviewed update to deployed vaults.

Project human views use `views/surface-<project-stem>.yml`, a plain display name, and `surface_for` rather than broad `belongs_to`, backlinks, or title lists. Follow [[procedures/maintain-project-human-view|Maintain Project Human View]] for membership and size. Run [[procedures/lint-vault|Lint Vault]] after structural view changes.
