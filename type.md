---
type: Type
_order: 9
_organized: true
---

# Type

A Type defines shared metadata and defaults for a category of notes in the vault.

Type definitions remain root notes with `type: Type`. Empty properties or relationships act as placeholders for new notes; populated values act as defaults. Add a new Type only when a recurring retrieval need does not fit the existing ontology cleanly.

## Common properties

Useful display metadata includes `icon`/`_icon`, `color`/`_color`, `order`/`_order`, `_sidebar_label`, `_list_properties_display`, `_sort`, `template`, `view`, and `visible`.

## Conventions

- Keep canonical English Type identity in the filename, H1, and `type:` values. Use `_sidebar_label` for localized or custom display text instead of creating a translated duplicate Type.
- Preserve the display-key style already used by the Type note. Do not add duplicate aliases such as both `_color` and `color`, `_icon` and `icon`, or `_order` and `order`.
- Viewer-authored visible keys are valid state. When explicitly resolving a duplicate, keep the key that reflects the current UI state when known and remove only the stale alias.
- Keep Type notes `_organized: true` unless a new Type is deliberately still a draft. Do not move or mass-normalize Type definitions during an unrelated edit.
