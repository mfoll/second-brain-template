---
type: Type
_icon: buildings
_color: "#14b8a6"
_organized: true
_order: 9
_list_properties_display:
  - status
  - belongs_to
  - aliases
---

# Organization

An Organization is a company, institution, funder, customer, supplier, partner or other body outside the owner's own structure whose relationship with the owner's work needs a durable home: who it is, what it is called, who deals with it, which agreements govern the relationship and how that changed.

Use an Organization when the same body keeps recurring across material, especially when it is known by several names or codes, changes owner or contact over time, or carries agreements whose terms change. A team or area the owner answers for stays a Responsibility; a body mentioned once needs no note.

## Hierarchy

An Organization `belongs_to` the Responsibility, Project or area Topic that answers for the relationship, such as a customer-accounts Responsibility or a funding Project. People who work there `belongs_to` it as their affiliation; Sources mainly about it may `belongs_to` it. See [[adr/0011-root-belongs-to-at-responsibilities-and-home-exploration-clusters-in-topics|ADR 0011]].

## Names and identifiers

List every surface the material uses for the organization in `aliases`: short names, codes, account or customer numbers, nicknames and former names, with the date a name changed in the body. Resolve new material against these before creating a note; a look-alike name that denotes a different body belongs in the body as a distinction, never in `aliases`.

## Current state and dated history

Facts about an organization change: owners and contacts, contract terms, status. Keep two layers:

- **Current State** states what holds now, written so a reader needs nothing else for today's answer.
- **History** keeps every change as a dated line, oldest first, with what changed, the effective date when it differs from the recorded date, and a pointer to the record. A correction or retraction is a new line that names what it corrects; the earlier line stays.

Answering "as of" a date reads History; answering "now" reads Current State. When they disagree, History and its records win, and Current State is fixed.

## Template

```md
---
type: Organization
status: Active
belongs_to: "[[owning-responsibility]]"
aliases:
  - "Short name"
  - "CODE"
_organized: true
---

# Organization name

One or two sentences: who this is and why it matters to the owner's work.

## Current State

- Relationship: customer, supplier, funder or partner, and its status.
- Owner or main contact on our side, and theirs.
- Governing agreement and its key current terms.
- Open items.

## Names and Identifiers

Former names, codes and look-alikes to keep apart.

## History

- YYYY-MM-DD: what changed (effective YYYY-MM-DD if different). Record: `relative/path/or/link`.

## Open Questions

- [[a-question-about-this-relationship]]
```
