# Contributor And Vendor Value

## Audit Question, Depth, And Evidence Boundary

This controlled detailed rerun asks what usable contribution, knowledge
concentration, handoff, vendor dependence, and successor need are supported by
public evidence through July 22, 2026. It uses the four approved repositories,
public GitHub PR/commit/review/profile records, approved documentation, the
vendor packet, and relevant reviewer handoffs. It does not infer individual
performance, hours, compensation, legal ownership, availability, account
control, customer adoption, or contractual acceptance.

## Coverage And Material Gaps

The new feature-level assessment covers source-linked product, safety,
operability, documentation, infrastructure, and bounded external changes. It
replaces raw commit-share reasoning with attributed feature/change units. Public
evidence still lacks linked acceptance criteria for most PRs, private work,
material review records, outcome/adoption data, and exercised successor paths.

## Key Findings

| Finding | Evidence links | Confidence and limitation | Consequence |
|---|---|---|---|
| Two public contributors account for 41 of 43 supported feature-value units (95.3%) across the project history. | [Contribution value assessment](../../controls/contributors/contribution-value.md); [E-020](../../evidence/evidence-ledger.md) | High for public authorship and stated unit scope; feature value is a coarse, evidence-bounded ordering, not a performance measure. | A new maintainer should plan knowledge transfer around the two primary contribution histories while retaining the long-tail record. |
| In the most recent cutoff-anchored year, one contributor accounts for 19 of 22 supported units (86.4%). | [Contribution value assessment](../../controls/contributors/contribution-value.md) | High for source authorship; live operation, acceptance, and hidden work remain unknown. | Current technical and documentation context is especially concentrated, strengthening the need for a non-creator handover exercise. |
| Félix Léger's public work includes dynamic redirects/configuration, link-management reliability, and a root redirect application; Benoît H. Dicaire's spans the foundation, current setup/upgrade/release controls, runtime/security, documentation, and example operations. | [CV-001–CV-009](../../controls/contributors/contribution-value.md) | High for authored PR/commit attribution; no claim of exclusive ownership or all value. | The audit can identify concrete learning paths rather than treating raw commit volume as a proxy for value. |
| Publicly acknowledged ideas/user-testing and bare approval evidence are insufficient to allocate a feature-value share. | [CV limits](../../controls/contributors/contribution-value.md); [E-020](../../evidence/evidence-ledger.md) | High for the public attribution boundary. | Preserve recognition, but do not use the result for employment, compensation, or contractual decisions. |
| Cross-repository successor and vendor/control-plane weaknesses remain unchanged. | [Ownership/successor map](../../controls/contributors/ownership-and-successor.md); [continuity matrix](../../controls/continuity/continuity-and-transfer-matrix.md) | Public roles/source only; actual authority/access unknown. | Contribution history can guide onboarding but cannot appoint a successor or prove third-party operation. |

### Decision Insights

- **Use the feature-level list to design the handover, not to assign authority.**
  The evidence identifies concentrated learning paths, while OI-001/OI-002/OI-005
  still leave canonical appointment and account control unresolved. Smallest next
  move: base the non-creator exercise in OI-004 on CV-001–CV-009.

## Selected Outputs

[Contribution value assessment](../../controls/contributors/contribution-value.md)
is triggered by auditable feature-level GitHub/Git evidence. The existing
[ownership, vendor, and successor map](../../controls/contributors/ownership-and-successor.md)
remains the separate authority and continuity view.

## Material Omissions, Unknowns, And Stakeholder Questions

- Public source does not establish hidden implementation, testing, design,
  support, or operational work; it cannot establish hours or compensation.
- Most PRs lack linked acceptance/outcome records, so the assessment is not a
  customer-value, adoption, or revenue ranking.
- Current willingness, competency coverage, appointment authority, GitHub/
  Cloudflare/domain access, and an exercised transfer remain OI-001/OI-002/
  OI-004/OI-005/OI-006 matters.

## Reconciliation

This rerun replaces the previous raw contribution-concentration narrative with
feature-level attribution. It confirms, rather than changes, the ownership map:
high attributed contribution is neither account control nor successor authority.
No material conflict was found with Product Value, Revenue Risk, Project Health,
Maintenance Cost, or Business Continuity handoffs.

## Bounded Conclusion And Downstream Guidance

The project has a useful, source-linked contribution record: two people account
for the overwhelming majority of supported feature units, and current work is
especially concentrated. This makes the assessment decision-useful for
onboarding and continuity planning. It does not prove operation, transfer,
acceptance, or any person's performance. Expense Exposure and Revenue Risk may
use the continuity consequence but must not infer cost, revenue, or commercial
obligation.
