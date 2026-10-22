---
type: ADR
status: Accepted
belongs_to: "[[vault]]"
related_to:
  - "[[responsibility]]"
  - "[[project]]"
  - "[[topic]]"
  - "[[person]]"
  - "[[adr/0006-use-project-notes-for-active-subprojects|ADR 0006]]"
  - "[[procedures/lint-vault|Lint Vault]]"
  - "[[procedures/review-vault-health|Review Vault Health]]"
  - "[[procedures/ingest-source|Ingest Source]]"
  - "[[procedures/process-inbox|Process Inbox]]"
_organized: true
---

# ADR 0011: Root belongs_to At Responsibilities And Home Exploration Clusters In Topics

## Context

`belongs_to` is how a vault routes retrieval and project work: agents start from a Project or Responsibility and follow its tree, Project notes are the resumption surface, and Lint Vault checks the same chains. When the originating deployment made its whole hierarchy visible in a graph viewer, the tree turned out to mix several principles: one Responsibility had become the umbrella of every activity, Projects belonged to a Topic, a registry of many records was reached only through `has` links, a plain Note was the parent of dozens of notes and itself had no parent, reading Sources were held by a Topic through `has` with no `belongs_to`, and many recent Sources were attached by `related_to` alone. Iterative ingestion caused most of this: the structure a theme needs only becomes clear after a few notes exist, and until then notes were attached wherever a link was at hand.

## Decision

> [!note]
> `belongs_to` records accountability, not theme. Every durable note rolls up through one primary `belongs_to` chain to the Responsibility that answers for it. Responsibilities are the roots, and the user's distinct roles are distinct roots; Projects sit under the Responsibility or umbrella Project that will resume them; Topics are lateral context that never own a Project, except that an exploration cluster may belong to a Topic under the Responsibility designated for exploratory reading until a Project absorbs it; `has` is a curated entry list and never a child's only link.

### Rules

- A Responsibility normally has no parent. Each of the user's roles with its own accountability is a root of its own. A Responsibility belongs to another only as a sub-duty of that area, for example team operations or funding under a wider role.
- A Project belongs to one Responsibility or one umbrella Project. Two parents are reserved for a Project genuinely co-owned across two trees; mark such a note `accepted_double_parent: true` so the lint hierarchy audit reports it as deliberate ([[adr/0006-use-project-notes-for-active-subprojects|ADR 0006]]). Umbrella membership follows the official container.
- Sources, Concepts, Questions, Notes, Events, Methods and Opinions carry one `belongs_to`: the most specific Project or Responsibility that would resume or answer for them. A second context is `related_to`. Never leave a durable note attached by `related_to` alone.
- A Topic links laterally through `related_to`. A Topic carries `belongs_to` in two cases only: an area-scoped context bucket under the Responsibility or Project whose reusable context it holds, and an exploration cluster under the Responsibility designated for exploratory reading. A Topic may root an area only when the user's work in that area has no owning Responsibility, for example the owner's own infrastructure work in a professional vault; mark it `hierarchy_root: true` and record it in an ADR. Any further Topic root needs a new ADR.
- `has` lists selective entry points. A note reachable only through `has` is a lint warning; the fix is the child's `belongs_to`.
- Notes, Concepts and Persons may be intermediate parents only when they themselves roll up to a hub, for example a committee Note under the Responsibility that sits on it. A note that parents many others and is a durable area should become a Topic or Responsibility.
- A Person's `belongs_to` is affiliation when the vault has a hub for it; Projects go in `related_to`; a contact without an affiliation hub stays parentless deliberately.
- Recaps, automatically loaded Guides, archived notes and the notes of any Type whose definition carries `hierarchy_exempt: true` (structured daily records produced by an automation, for example) are outside the hierarchy by design.

### Iterative ingestion and promotion

- "Home not yet known" is a legal state with a named place. When no Project or Responsibility owns a new note, file it under the matching exploration Topic of the Responsibility designated for exploratory reading. Creating a new cluster Topic there needs no separate approval once at least three notes share a theme. A deployment that designates no such Responsibility leaves the note unprocessed instead of attaching it by `related_to` alone.
- When a cluster gains an outcome, actions, collaborators or a deliverable, propose a Project; when a Project absorbs a cluster, re-parent the Topic under the Project and its notes follow. Creating or re-parenting Projects and Responsibilities keeps the usual approval gate.
- The regular Lint Vault run lists hierarchy drift with `.agents/skills/lint-vault/scripts/hierarchy_audit.py`, which reads its exceptions from the `hierarchy_root` and `accepted_double_parent` frontmatter flags; the periodic Review Vault Health decides promotions.

### Filing rule for a new note

Ask which Project or Responsibility would resume or answer for this note. That is `belongs_to`. Everything else is `related_to`. If nothing fits, use the exploration Responsibility, not a bare `related_to`.

## Consequences

Every root area reads as one accountability: a reader who starts from a Responsibility finds what the user answers for, and a graph viewer's colouring follows the same chains without special cases. Topics become purely thematic and cheaper to create. Exploratory reading has a home before it has a Project, so ingestion no longer has to guess or leave notes unattached, and promotion becomes a routine proposal surfaced by lint rather than a structural change nobody dares to make. The cost is one more root Responsibility per role and a small discipline on second parents.

## Revisit When

> [!question]
> Revisit if a Topic-rooted area gains an owning Responsibility, if exploration clusters accumulate without ever being promoted, if the single-parent rule for shared Sources loses retrieval that `related_to` plus `has` do not recover, or if a graph viewer and Lint Vault start disagreeing about homes.

## Provenance

Ported on 2026-10-22 from the maintainer's work/control vault, ADR 0028 *Root belongs_to At Responsibilities And Home Exploration Clusters In Topics* (2026-10-22); work-specific names and examples were replaced by generic wording.
