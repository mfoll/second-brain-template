---
type: ADR
status: Accepted
belongs_to: "[[vault]]"
_organized: true
---

# ADR 0001: Treat Markdown Graph As Portable Brain

## Context

A durable second brain should remain useful outside any single app, agent, or chat system.

## Decision

The vault treats Markdown files, YAML frontmatter, wikilinks, procedures, ADRs, views, skills, and Git history as the portable source of truth.

Vault UIs and agents may improve access and maintenance, but they must not become the only place where meaning exists.

## Consequences

- Notes should be readable in ordinary Markdown tools.
- Relationships should use explicit wikilinks and frontmatter.
- Procedures should be portable Markdown before they are agent-specific skills.
- Machine-local setup belongs outside durable template content.
