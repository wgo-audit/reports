# Product Manager Notes

## Capability, Workflow, And Promise Position

vanityURLs is more than a redirect table. The audited source implements source-controlled links, readable and splat paths, schedules and lifecycle states, ownership metadata, target policy/blocking, localized public and trust pages, private operational views, optional analytics, and setup/detach/upgrade workflows. The core value proposition—an MIT-licensed, Git-reviewed short-link service deployed to an operator-controlled Cloudflare account and domain—is supported by public source and documentation. See the [Product Value report](reviewer-reports/product-value/report.md), [product decision register](controls/product/pdr-register.md), and [configuration contract](controls/product/config-contract-matrix.md).

The successor workflow is credible in design:

1. Fork or clone the product and instance sources.
2. Configure links and policies in Git.
3. Build and validate a generated, read-only registry.
4. Deploy a stateless Worker and edge controls.
5. Operate changes through reviewable source history.
6. Use tagged upstream releases for upgrades while retaining local control.

What is **implemented** must remain distinct from what is **demonstrated**. Public evidence supports the feature set, source-controlled workflow, and independent-instance design. It does not show a non-creator completing the full workflow with minimal help, a successor taking over the existing service, or the live demo matching the cutoff source.

Public positioning should therefore prefer evidence-supported statements such as:

- MIT-licensed and forkable;
- designed to run in the operator’s own Cloudflare account and domain;
- link configuration and history are source-controlled;
- the runtime is stateless and has no application database;
- analytics is optional and disabled in the reference source.

“Easy onboarding,” “free,” “fast,” “always under your control,” “production-ready takeover,” or “recoverable” should not be asserted without the corresponding exercise, cost, performance, custody, and recovery evidence. The [claim/demo governance register](controls/revenue/claim-governance.md) records the current boundaries.

## Decisions And Specialist Sign-Off Boundaries

The first product decision is not a feature priority. It is the continuity promise in [OI-001](controls/open-items.md):

- **Independent-fork continuity:** the community promises that anyone can create and evolve a separately controlled instance.
- **Canonical continuity:** the community also promises continuity of the existing repositories, release trust, `v8s.link` domain, demo, contacts, and community identity.

These outcomes require separate acceptance criteria. A successful clean-room fork does not prove control of the existing service, while an account-transfer inventory does not prove that the product is usable by a new maintainer.

Specialist approval remains necessary before making stronger claims:

| Claim or change | Required boundary |
|---|---|
| Security effectiveness, signed supply chain, or absence of vulnerabilities | Security review plus exercised release/upgrade and live-control evidence |
| Privacy/compliance for enabled analytics | Operator-specific purpose, field/IP mode, retention, deletion, processor, and legal review |
| Performance, scale, or availability | Measured workload/capacity envelope with provider quotas and degradation/rollback evidence |
| Free or predictable operating cost | Current plan, quota, renewal, and billing evidence for the actual operator |
| Recoverability or third-party operation | Redacted authority/custody proof and independent deploy/rollback/recovery exercise |
| Trust, contact, or policy pages | Current owner/contact validation and any relevant legal/content approval |

Analytics should remain disabled in the successor baseline. It is not necessary for redirects and introduces privacy, vendor, quota, cost, and data-governance obligations.

## Material Gaps, Risks, And Next Work

The most important product-management risks are:

- **Continuity ambiguity:** “the project can be operated by a third party” currently conflates forkability with canonical takeover.
- **Public credibility:** the official demo page describes a larger “current” link inventory than the three links in the stated reference-instance source, and the deployed commit is unknown.
- **Promise overreach:** “free, fast, and always under your control” is broader than the available cost, performance, and transfer evidence.
- **Usability uncertainty:** extensive documentation and tooling do not replace an observed non-creator journey with measured assistance.
- **Governance friction:** contributors cannot derive one authoritative path from contribution to cross-repository maintainer authority.
- **Knowledge concentration:** two public contributors account for 95.3% of supported feature/change units; this is useful for staging onboarding, but it does not establish appointment authority or performance.
- **Version drift:** the reference-instance source declares product version 3.6.3 while the cutoff product release is 3.7.0; live equivalence is unknown.

The smallest safe sequence is:

1. Decide the continuity promise and publish its acceptance criteria.
2. Correct signed-upgrade and demo/claim mismatches.
3. Inventory the authority, service, renewal, and alert dependencies required by that promise.
4. Align governance and build the handover packet from verified facts, using the [contributor value assessment](controls/contributors/contribution-value.md) as a learning-path map.
5. Have a non-creator execute the complete isolated workflow.
6. Publish readiness as demonstrated, partially demonstrated, or blocked—without converting unknowns into assurances.

The authoritative work routes are [OI-001 through OI-014](controls/open-items.md); this document does not create a second backlog.

## Evidence And Limits

The capability position is based on cutoff-eligible source, docs, Git history, and public GitHub records through July 22, 2026. No product analytics, user research, customer interviews, support records, roadmap approval, live-demo equivalence, authenticated configuration, or local audit execution was available. No revenue or customer commitments were evidenced.

For detail, use:

- [Product Value report](reviewer-reports/product-value/report.md)
- [Revenue Risk report](reviewer-reports/revenue-risk/report.md)
- [Documentation alignment packet](evidence/packets/documentation-alignment.md)
- [Operator-to-redirect flow](controls/product/diagrams/operator-to-redirect-flow.md)
- [Audit brief](audit-brief.md) and [source-access register](evidence/source-access-register.md)
