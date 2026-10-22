---
type: Type
_icon: tag
_color: "#f59e0b"
_order: 2
_organized: true
---

# Topic

A Topic is a broad retrieval surface for related notes, sources, concepts, and questions.

## Hierarchy

Topics are lateral context and link through `related_to`; a Topic never owns a Project. A Topic carries `belongs_to` in two cases only: an area-scoped context bucket under the Responsibility or Project whose reusable context it holds, and an exploration cluster under the Responsibility the deployment designates for exploratory reading, until a Project absorbs the cluster, when the Topic is re-parented under that Project and its notes follow. A Topic may root an area only when the user's work in that area has no owning Responsibility; record the exception with `hierarchy_root: true` in its frontmatter and in an ADR, so that the lint hierarchy audit treats it as deliberate. See [[adr/0011-root-belongs-to-at-responsibilities-and-home-exploration-clusters-in-topics|ADR 0011]].
