---
type: Procedure
status: Active
belongs_to: "[[vault]]"
related_to:
  - "[[responsibility]]"
  - "[[project]]"
  - "[[topic]]"
  - "[[procedures/ingest-source|Ingest Source]]"
  - "[[procedures/initialize-project-memory|Initialize Project Memory]]"
  - "[[adr/0011-root-belongs-to-at-responsibilities-and-home-exploration-clusters-in-topics|ADR 0011]]"
_organized: true
---

# Start a Focus

Use this procedure when the user wants the Brain to help with something new: an ongoing area, a finite outcome, a subject to explore, or a first item to keep. A focus is the user's word for that thing, not a Type; the interview decides which existing Type, if any, should hold it. Deployment uses this procedure for the first focus, so the same workflow serves onboarding and everyday use.

## Interview

Ask one question at a time, offer a default or short choices where the runtime supports them, and stop when the answers are enough. Do not ask more than about six questions; skip any the user's request already answers.

1. What do you want to achieve or keep track of?
2. Does it end? If so, what will count as done?
3. Is it part of something you already look after? Name the area or role.
4. What useful material exists already, and where does it live? A link, file or folder is enough; nothing needs to move.
5. Who else is involved, if anyone?
6. Is anything sensitive or outside the scope recorded in [[README]]?

Answers about other people stay relevant and proportionate. A material change to the agreed scope, sources or tools is a setup decision for the user, not something to resolve inside this workflow.

## Choose the smallest structure

Search existing notes first: matching Responsibilities, Projects, Topics and titles, and the user's named area. Reuse or extend an existing note before creating another. Then map the answers:

| Answer pattern | Structure |
| --- | --- |
| Ongoing, no end, something the user answers for | [[responsibility]] (a root, or a sub-duty of an existing one) |
| Finite outcome with a done condition | [[project]] under the Responsibility or umbrella Project that will resume it |
| A subject to read about or explore, no outcome yet | [[topic]] following [[adr/0011-root-belongs-to-at-responsibilities-and-home-exploration-clusters-in-topics|ADR 0011]]: lateral context, or an exploration cluster under the Responsibility designated for exploratory reading |
| A single item for existing work | No new container; add it to the existing note, or follow [[procedures/ingest-source|Ingest Source]] for external material |

Read the matching root Type notes before writing. Create a Responsibility only when no existing one answers for the work; a Project with no owning area needs one. If placement stays unclear, ask rather than force a category.

## Propose, then write

1. Present the proposal in plain language with a short table: each note, its Type, its parent and why it exists. Name notes that will be reused.
2. Wait for the user's agreement or edits. Approval covers the listed notes only.
3. Create or update the agreed notes from the Type templates, with valid frontmatter, a first H1, a `belongs_to` chain that reaches a Responsibility, and `_organized: true`. Link existing material as pointers; keep documents where they are.
4. If the user supplied a first item, save it through [[procedures/ingest-source|Ingest Source]] for external material, or into the right note for the user's own idea.
5. If the focus needs a code repository or other technical workspace connected to the Brain, hand over to [[procedures/initialize-project-memory|Initialize Project Memory]]; do not create a folder or pointer here.

## Verify and report

- Run the links and hierarchy audits from `.agents/skills/lint-vault/scripts/` when Python is available; fix new errors.
- Check retrieval: in a fresh session, or by reading only from the entry note, answer what the focus is for, what was saved and what comes next.
- Report the notes created or updated, where they sit, what was reused, what could not be read, and any question left open.

Do not install Skills, connect sources, schedule jobs or change global instructions as part of this procedure.
