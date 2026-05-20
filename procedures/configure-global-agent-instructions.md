---
type: Procedure
status: Active
belongs_to: "[[vault]]"
_organized: true
---

# Configure Global Agent Instructions

## Goal

Install or check machine-local global agent instructions from [[global-agent-instructions-template]]. Replace `<VAULT_ROOT>` only in the machine-local instruction surface, not in portable vault notes. Verify that the configured root is readable and contains `AGENTS.md`.

## Steps

1. Read `AGENTS.md` and [[global-agent-instructions-template]].
2. Identify the agent's machine-local instruction surface. Examples include a global/custom-instructions UI, an agent-specific global guidance file, or another explicitly machine-local configuration location.
3. Confirm the intended concrete vault root with the user or with the deployed vault's local setup note. Do not infer a path from the template repository itself.
4. Copy the template text from [[global-agent-instructions-template]] into the machine-local instruction surface.
5. Replace `<VAULT_ROOT>` only in that machine-local instruction surface.
6. Verify that the configured vault root is readable and contains `AGENTS.md`.
7. Compare the installed instruction text against [[global-agent-instructions-template]]. Expected differences should be limited to the concrete vault root and any wording required by the target agent's instruction surface.
8. If the installed instructions contain stale vault roots, copied project-local rules, or machine-specific details that belong elsewhere, report the drift and ask before rewriting broad sections.
9. Report the final configured root, the instruction surface checked or updated, and any intentional remaining placeholders.

## Boundaries

Keep concrete local paths out of portable vault notes. Real vault roots belong in the machine-local instruction surface or in an explicitly deployment-local setup note.

Do not put secrets, credentials, tokens, cache files, generated dumps, or private source material into global instructions.

Do not overwrite unrelated custom user guidance while installing this template. Merge narrowly around the Second Brain memory block when possible.
