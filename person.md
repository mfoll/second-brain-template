---
type: Type
_icon: user
_color: "#10b981"
_organized: true
_order: 9
_list_properties_display:
  - status
  - belongs_to
  - related_to
---

# Person

A Person is an individual who matters enough to the vault's work or operations that future agents should be able to recover context about the relationship, role, collaborations, and boundaries.

Use Person notes for collaborators, team members, recurring contacts, supervisors, students, maintainers, and other named individuals when durable context would improve future project work.

Keep Person notes scoped and respectful. Do not use them as raw biography dumps or surveillance logs. Capture only relevant relationship context, collaboration surfaces, recurring responsibilities, communication preferences when explicitly known, and links to Projects, Responsibilities, Sources, or Questions where the person matters.

## Hierarchy

`belongs_to` on a Person records affiliation when the vault has a hub for it, such as a team, institution, committee, household or network represented by a Responsibility or Topic; former members keep their affiliation. Projects and other contexts where the person matters go in `related_to`. A contact with no affiliation hub in the vault stays without `belongs_to` deliberately; do not attach people to Projects to fill the gap. See [[adr/0011-root-belongs-to-at-responsibilities-and-home-exploration-clusters-in-topics|ADR 0011]].
