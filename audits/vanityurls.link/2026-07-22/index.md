# vanityURLs Continuity And Third-Party Operability Audit

## Start Here

This detailed, public-evidence audit answers whether vanityURLs can survive a sudden departure or shift in interest by its creators/current maintainers.

- **Canonical maintainer onboarding with minimal creator involvement:** **No.**
- **A new independent third-party instance:** **Plausible, but not yet proven easy.**
- **Third-party takeover of the existing project/domain/demo:** **No, not on public evidence.**
- **Fork and continued technical evolution after abandonment:** **Yes, probably with moderate effort; preserving the existing identity and service is not assured.**

The codebase’s portability is a real strength. The decisive gaps are external authority, cross-repository governance, release/domain/cloud custody, recovery and alert ownership, and independent end-to-end proof. Read the [Executive Summary](executive-summary.md) for the reconciled assessment and 30–90 day plan.

## Audience Routes

| Reader | Start with | Then use |
|---|---|---|
| Project creators and current maintainers | [Executive Summary](executive-summary.md) | [Business Continuity](reviewer-reports/business-continuity/report.md), [continuity/transfer matrix](controls/continuity/continuity-and-transfer-matrix.md), [open items](controls/open-items.md) |
| Existing and prospective OSS contributors | [Product Manager Notes](product-manager-notes.md) | [Contributor value assessment](controls/contributors/contribution-value.md), [Project Health](reviewer-reports/project-health/report.md), [ownership/successor map](controls/contributors/ownership-and-successor.md) |
| Third party evaluating operation | [Technical Lead Notes](technical-lead-notes.md) | [Architecture](reviewer-reports/architecture/report.md), [Security/Privacy](reviewer-reports/security-privacy/report.md), [Business Continuity](reviewer-reports/business-continuity/report.md), [Maintenance Cost](reviewer-reports/maintenance-cost/report.md) |
| Auditor tracing a claim | [Evidence ledger](evidence/evidence-ledger.md) | [Source-access register](evidence/source-access-register.md), [audit brief](audit-brief.md), reviewer-linked artifacts |

## Evidence Boundary

- **Cutoff:** July 22, 2026.
- **Repositories:** product `code`, Terraform `v8s-config`, reference instance `v8s-link`, and documentation `website`, each pinned to the commit recorded in the [audit brief](audit-brief.md).
- **Documentation:** local `docs/` plus `website/content/docs/`. The requested `website/context/docs/` path did not exist; the correction is recorded.
- **Hosted evidence:** public GitHub pull requests, issues, projects, releases, Actions, and public website material.
- **Excluded:** authenticated/private repository settings; cloud, registrar, secret, Terraform-state, billing, contract, and private operating records; post-cutoff facts except explicitly labeled validation.
- **Execution:** zero local dependency restores, tests, builds, Terraform operations, deployments, or recovery exercises.

An absent public control may exist privately. It is still unavailable to an independent successor until it is safely documented, transferred, and exercised.

## Key Control Maps

- [Canonical open-item register](controls/open-items.md)
- [Cross-repository control boundary](controls/architecture/diagrams/cross-repository-control-boundary.md)
- [Build, deploy, and request path](controls/architecture/diagrams/build-deploy-request-path.md)
- [Continuity and transfer matrix](controls/continuity/continuity-and-transfer-matrix.md)
- [Observability and response path](controls/business-continuity/diagrams/observability-and-response-path.md)
- [Change-safety matrix](controls/quality/change-safety-matrix.md)
- [Secret and identity surface](controls/security/secret-and-identity-surface.md)
- [Capacity and degradation envelope](controls/scalability/capacity-and-degradation.md)
- [Contributor value assessment](controls/contributors/contribution-value.md)
- [Burn, renewal, and interruption register](controls/expense/burn-and-renewal.md)
- [Public claim and demo governance](controls/revenue/claim-governance.md)

## Untested Transition Packet

These aids translate the audit into a successor-facing operating packet. They are documentation only: no procedure was executed, no authority was granted, and every aid remains `untested`.

- [Replacement maintainer](operator-aids/replacement-maintainer.md)
- [Recovery](operator-aids/recovery.md)
- [Observability and response](operator-aids/observability.md)
- [IAM and credential control](operator-aids/iam-and-credential-control.md)
- [Isolated rebuild acceptance](operator-aids/isolated-rebuild.md)

## Reviewer Reports

All 11 approved reviewers completed with open verification where public evidence could not establish live or private controls.

1. [Architecture](reviewer-reports/architecture/report.md)
2. [Product Value](reviewer-reports/product-value/report.md)
3. [Project Health](reviewer-reports/project-health/report.md)
4. [Code Quality](reviewer-reports/code-quality/report.md)
5. [Security/Privacy](reviewer-reports/security-privacy/report.md)
6. [Scalability](reviewer-reports/scalability/report.md)
7. [Business Continuity](reviewer-reports/business-continuity/report.md)
8. [Maintenance Cost](reviewer-reports/maintenance-cost/report.md)
9. [Contributor/Vendor Value](reviewer-reports/contributor-vendor-value/report.md)
10. [Expense Exposure](reviewer-reports/expense-exposure/report.md)
11. [Revenue Risk](reviewer-reports/revenue-risk/report.md)

## Shared Evidence

- [GitHub history and hosted CI](evidence/packets/github-history-and-hosted-ci.md)
- [Delivery and quality](evidence/packets/delivery-and-quality.md)
- [Recovery and operations](evidence/packets/recovery-and-operations.md)
- [Vendor, ownership, and commercial boundary](evidence/packets/vendor-ownership-commercial.md)
- [Documentation alignment](evidence/packets/documentation-alignment.md)
- [Documentation catalog](documentation/catalog.md)

The synthesis does not create a second decision queue or backlog. Status and closure routes remain authoritative in [open-items.md](controls/open-items.md).
