---
type: Procedure
status: Active
belongs_to: "[[vault]]"
related_to:
  - "[[project]]"
  - "[[procedures/initialize-project-memory|Initialize Project Memory]]"
_organized: true
---

# Route Project Work And Artifacts

Use this procedure before creating a project folder, repository, or agent-application project, and whenever temporary work begins to produce artifacts worth retaining.

## Default

A Project note is sufficient by default. Do not create a filesystem folder or agent-application project merely to hold an `AGENTS.md` pointer to that note. Work from an existing vault project or task and name the Project in the prompt.

For an existing project, preserve its folder layout, technical instructions, tools and canonical documentation. Add a memory section and useful links only when requested. This Procedure helps route new artifacts; it is not authority to migrate an established project into the Brain.

## Promote to a technical workspace

Create or retain a dedicated workspace only when at least one condition is met:

- it contains durable code, configuration, tests, reproducible analysis, versioned manuscript inputs, or operational data suited to Git;
- it needs project-local dependencies, commands, security boundaries, or specialized always-on instructions;
- a persistent task, automation, build, deployment, or collaborator workflow needs a stable working directory;
- the artifact set has become substantial enough that a dedicated folder is clearer than a cloud `Working/` area;
- the user explicitly requests a distinct workspace.

When promoted, normally initialize Git and a suitable remote for versionable artifacts. A workspace and an agent-application project are separate decisions: create the latter only when persistent tasks or distinct execution context justify it.

## Route artifacts

1. Put selected durable decisions, state, questions, evidence synthesis and retrieval pointers in typed vault notes. Link existing canonical documents and avoid maintaining a duplicate version.
2. Keep small assets in the vault only when they are intentionally Git-tracked and directly support a note.
3. Put durable code and reproducible technical artifacts in a repository.
4. Put durable non-versioned documents and deliverables in the deployment's confirmed external project location.
5. When a file must survive machine loss but the project does not yet justify a dedicated external folder, use the deployment's configured cloud `Working/<project-or-context-slug>/` convention.
6. Use an ignored workspace `.tmp/` only for reproducible or disposable intermediates tied to an existing workspace. Use `/tmp/` for truly disposable files.

If a temporary artifact becomes useful, promote it during the task rather than waiting for cleanup. If a workspace loses its technical purpose, route its useful artifacts, preserve its Brain context, then retire the folder and optional agent-application project.

## Record and verify

Represent maintained external locations through portable Source notes using `root_key` plus `relative_path`; never commit the resolved machine path. Before removing a local copy, verify the destination exists, is current, and is available through the configured cloud provider.
