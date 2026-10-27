---
type: Procedure
status: Active
belongs_to: "[[vault]]"
related_to:
  - "[[procedures/ingest-source|Ingest Source]]"
  - "[[procedures/start-a-focus|Start a Focus]]"
  - "[[procedures/review-vault-health|Review Vault Health]]"
  - "[[organization]]"
_organized: true
---

# Import an Archive

Use this procedure when the owner brings an existing collection into the Brain at once, after setup and the first focus: a mail or chat export, a document folder, a CRM or ticket export, or notes from another tool. Ongoing material afterwards goes through [[procedures/ingest-source|Ingest Source]] at the owner's usual rhythm.

An archive is too large to read note by note in one pass, and its records refer to the same people and organizations in many ways. Resolving those entities first, then reading the records in date order, keeps the vault coherent and its history correct.

## Steps

1. **Agree the scope.** Confirm with the owner what the archive contains, where it stays (records remain at their source and read-only; Source notes point to them), what is out of scope or sensitive, and the period it covers. For a large archive, estimate the time and model cost first and agree it.
2. **Inventory.** List the records with their dates, kinds and sizes, without reading them in full. Identify reference records that define entities: rosters, CRM or customer records, account sheets, organization charts, rename or merger notices, contracts.
3. **Resolve entities first.** Read the reference records and create or extend Person and [[organization|Organization]] notes as their Types describe, so that every name, code and former name the archive uses is known before the event records are read. Place each under the Responsibility or Project that answers for it, using [[procedures/start-a-focus|Start a Focus]] for areas the owner has not set up yet.
4. **Read the rest in date order.** Process the remaining records oldest first, in batches by period (for example a week or a month), following [[procedures/ingest-source|Ingest Source]]. Splitting the work between several agents by period is acceptable for very large archives only if each batch writes History lines without rewriting Current State, and step 5 then reconciles every touched entity.
5. **Reconcile.** For every entity and Project touched: order History, make Current State agree with the latest effective entries, merge duplicate entities, check open Questions against the imported material, and keep genuine conflicts between records visible as the Organization Type describes instead of choosing silently.
6. **Check.** Run [[procedures/lint-vault|Lint Vault]], then a focused [[procedures/review-vault-health|Review Vault Health]] on the imported area. Report what was imported, the entities created, conflicts recorded and any Questions created with the reason for each, records skipped and why, and any Type proposals.

## Guardrails

- Never modify, move or delete the archive's records.
- Keep sensitive material out of the vault as agreed in step 1; note where it stays instead.
- Propose new Types rather than creating them during the import; see the guardrails in Ingest Source.
