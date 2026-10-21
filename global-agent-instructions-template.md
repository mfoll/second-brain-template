---
type: Guide
related_to: "[[vault]]"
_organized: true
---

# Global Agent Instructions Template

This Guide supplies an optional routing block for using the Brain from other folders. Follow [[procedures/configure-global-agent-instructions|Configure Global Agent Instructions]] to add it alongside existing instructions. Install only the marked block below, replacing its two placeholders in the machine-local copy.

If a generator or configuration repository owns the destination, update that source through its normal mechanism. The generator remains optional infrastructure; the template does not install one or replace existing global guidance.

## Block to install

```markdown
<!-- BEGIN SECOND BRAIN -->
## Second Brain memory

Vault role: `<VAULT_ROLE>`. Root: `<VAULT_ROOT>`.

When relevant prior context would help, read the vault's `AGENTS.md`, then its
entry note or the entry named in the current project's memory section. Follow
only task-relevant links and inspect evidence before making claims. Self-contained
requests need no vault lookup.

Respect existing project instructions, tools, canonical documents and privacy
boundaries. Write to the Brain when asked or within an agreed standing scope;
reuse that authorization for routine work. Memory access grants no permission
to share content, change external files or push Git commits.

If the configured root is unknown or unreadable, report the gap and pause only
vault-dependent work. Ask for its location rather than guessing or creating one.
<!-- END SECOND BRAIN -->
```

## Keep detailed behavior in its owning files

Vault [[AGENTS]] owns progressive retrieval, typed capture, workflow comparison and Git boundaries; [[procedures/ingest-source]] and [[procedures/process-inbox]] own ingestion. [[vault-automations]] holds optional runtime-specific automation settings and verification. Keep multi-vault routing in an existing owner's configuration when one exists. Choose automatic capture or project writeback explicitly during setup; a file, URL or workspace link alone does not install those policies for every project.
