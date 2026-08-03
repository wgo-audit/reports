# Revenue Risk

## Audit Question, Depth, And Evidence Boundary

This detailed review asks what could interrupt demos, onboarding, adoption, community trust, or any commercial delivery claim. Because vanityURLs is community-maintained OSS with no company or approved customer/revenue/contract evidence, the material “revenue” exposure is claim accuracy and community confidence rather than a quantifiable sales amount. Evidence is public and cutoff-pinned through July 22, 2026, using Product Value, Security, Business Continuity, Expense Exposure, demo documentation, and source. No live demo, customer/pilot, analytics/adoption, sales, SLA, contract, or revenue evidence was approved.

## Coverage And Material Gaps

Coverage includes homepage positioning, quickstart/onboarding, official-demo claims, source-of-truth alignment, free/fast/control language, security/privacy/accessibility promises, third-party operation, and service continuity. The material gap is demonstration and claim governance: public source supports many capabilities, but live, ease, performance, cost, control-transfer, and recovery claims are unproved. A specific demo inventory/source mismatch increases trust exposure.

## Key Findings

| Finding | Evidence links | Confidence and limitation | Consequence |
|---|---|---|---|
| No approved evidence establishes revenue, customers, contracts, pilots, renewals, or commercial commitments. | [Vendor packet](../../evidence/packets/vendor-ownership-commercial.md), [Expense report](../expense-exposure/report.md) | High for audit boundary; private activity may exist. | Revenue amount or contractual loss cannot be assessed. |
| The strongest credible positioning is source-controlled, self-hosted, forkable short links with broad operator documentation—not proven ease, live operability, or takeover. | [Product report](../product-value/report.md), [claim register](../../controls/revenue/claim-governance.md) | High for implementation; no independent demonstration. | Precise claims can build trust; overclaiming readiness creates the harmful distrust scenario in the brief. |
| Website metadata says “free, fast, and always under your control,” but operating cost, performance, and canonical service control are not evidenced. | [E-019](../../evidence/evidence-ledger.md), [claim register](../../controls/revenue/claim-governance.md) | High for wording/evidence gaps; no live metrics/billing. | Prospective operators may form expectations the audit cannot support. |
| The official demo page says its larger link table is current and sourced from the public instance repository, while the cutoff repository contains only three starter links. | [E-019](../../evidence/evidence-ledger.md) | High for source/document mismatch; live deployed inventory unknown. | Demo credibility and documentation trust are directly exposed; neither source nor page can currently prove runtime behavior. |
| Quickstart and operator docs are extensive, but no non-creator has been observed completing the path with minimal assistance. | [PDR-002](../../controls/product/pdr/PDR-002-instance-setup-detach-and-upgrade.md), OI-004 | High for documentation/implementation; usability unobserved. | “Easy onboarding” should remain an objective, not a claim. |
| Canonical project/domain continuity is not transfer-ready, so abandonment can break durable links and community confidence even if a fork survives. | [Business Continuity report](../business-continuity/report.md), [continuity matrix](../../controls/continuity/continuity-and-transfer-matrix.md) | High for public proof gap; no outage inferred. | The most harmful trust event is loss of existing identity/control, not loss of code. |

### Decision Insights

- **Correct the demo/source mismatch before using `v8s.link` as proof.** This is a concrete, public credibility gap, not merely missing private evidence. Smallest action: OI-014 with source/deployed-commit/inventory reconciliation and automated drift checking.
- **Replace absolute positioning with evidence-scoped language.** “MIT-licensed,” “runs on your own Cloudflare account/domain,” and “designed for source control” are supported; “free,” “fast,” and “always under your control” need qualification or proof.
- **Make succession readiness a published status with stop conditions.** Honest separation of independent fork versus canonical takeover protects community trust while OI-001–OI-006/OI-012/OI-013 remain open.

## Selected Outputs

Material public promises, official-demo reliance, onboarding, and community-trust boundaries triggered [public claim and demo governance](../../controls/revenue/claim-governance.md).

## Material Omissions, Unknowns, And Stakeholder Questions

- Live demo reachability/behavior, deployed commit, inventory, and protected-path behavior: OI-014/OI-004/OI-006.
- Non-creator onboarding completion/assistance: OI-004.
- Performance/capacity: OI-011.
- Operating cost/renewals: OI-013.
- Canonical/service succession: OI-001/OI-002/OI-003/OI-006/OI-012.
- Any customer, contract, SLA, revenue, adoption, or conversion fact: not approved/found.

## Reconciliation

Product features are not downgraded because demonstration is missing; they remain implemented/documented. Conversely, implementation is not promoted to public proof. The demo/source mismatch is recorded without deciding which is live because no cutoff runtime observation exists. “Free” is reconciled to MIT license fee only, not zero operating cost; “under your control” is supportable for an independently owned instance’s source/configuration, not the current canonical external assets.

## Bounded Conclusion And Downstream Guidance

No revenue amount is auditable. The material exposure is community trust, adoption, and continuity claims: current public language and demo/source alignment overstate what is demonstrated. Synthesis should use the claim register to answer the user’s distrust concern and prioritize OI-014 alongside transfer/recovery evidence. No reader may infer customers, revenue, SLA breach, live outage, performance, or intent to mislead.
