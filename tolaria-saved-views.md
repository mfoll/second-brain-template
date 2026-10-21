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

Tolaria accepts a supported Phosphor icon name, one emoji, or an HTTP(S) image URL. Prefer choosing a name in the current picker. The optional checker uses `.agents/skills/lint-vault/references/phosphor-icon-names.txt`, generated from the MIT-licensed Phosphor package. A catalogue match verifies the identifier, not rendering in a particular app version. Confirm the glyph in the viewer; keep `icon: null` when none is needed.

After a direct view edit, run `.agents/skills/lint-vault/scripts/tolaria_icon_audit.py <vault-root>` when using the Python helper, then confirm the glyph in Tolaria. Emoji and URLs need visual confirmation. A newer picker or compatibility alias may differ from the pinned catalogue; inspect that difference before changing a valid icon. [[procedures/lint-vault]] documents reproducible refresh and the upstream licence notice.

Project human views use `views/surface-<project-stem>.yml`, a plain display name, and `surface_for` rather than broad `belongs_to`, backlinks, or title lists. Follow [[procedures/maintain-project-human-view|Maintain Project Human View]] for membership and size. Run [[procedures/lint-vault|Lint Vault]] after structural view changes.
