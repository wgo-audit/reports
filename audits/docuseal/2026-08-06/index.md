# Audit Index

## Start Here

This audit assesses whether pinned DocuSeal Community `3.1.7` is a sound foundation for further technical evaluation and vendor/specialist discussions for a regulated SaaS provider's web/mobile onboarding flow. It does **not** approve production use or make a legal, regulatory, privacy, security-control, or eSignature-enforceability determination.

Start with the [Executive Summary](executive-summary.md). The evidence-supported recommendation is **continue evaluation conditionally**: the Community signing core is substantive and inspectable, while production reliance remains gated by edition, identity, evidence trust, readiness, target architecture, recovery, capacity, commercial, maintenance, ownership, claim, and release-authority decisions and proof.

This is a decision boundary, not a negative score for DocuSeal or its team. Legal, vendor, production, recovery, and organization-control evidence is normally private and its public absence is neutral. It becomes decision-relevant here only where the approved mandate specifically asks whether a regulated production deployment can be authorized. Direct source concerns remain findings; other private topics are due-diligence or target-implementation questions without adverse weight.

Canonical shared records:

- [Audit brief](audit-brief.md) — mandate, source boundary, approved targets, and source limits
- [Evidence ledger](evidence/evidence-ledger.md) — E-001–E-065 with source dates, cutoff eligibility, facts, and limitations
- [Open items](controls/open-items.md) — OI-001–OI-025, separated by authority decision, verification, or implementation action
- [Audit checklist](audit-checklist.md) — reviewer and synthesis lifecycle state
- [API-equivalent cost estimate — Unreconciled](controls/cost-estimate.md) — two Terra passes reconcile a USD 151.4883488 included-session subtotal; one collector lacks a terminal cutoff, so this is not a complete audit total or a Codex invoice

## Audience Routes

- CEO, CISO, IT Operations Director, VP Software Engineering, and Product Manager: [Executive Summary](executive-summary.md)
- Product Manager and customer/onboarding authorities: [Product Manager Notes](product-manager-notes.md)
- VP Software Engineering, IT Operations Director, CISO, and technical reviewers: [Technical Lead Notes](technical-lead-notes.md)
- Detailed reviewer findings: [Architecture](reviewer-reports/architecture/report.md), [Code Quality](reviewer-reports/code-quality/report.md), [Product Value](reviewer-reports/product-value/report.md), [Security & Privacy](reviewer-reports/security-privacy/report.md), [Business Continuity](reviewer-reports/business-continuity/report.md), [Expense Exposure](reviewer-reports/expense-exposure/report.md), [Scalability](reviewer-reports/scalability/report.md), [Contributor & Vendor Value](reviewer-reports/contributor-vendor-value/report.md), [Maintenance Cost](reviewer-reports/maintenance-cost/report.md), [Revenue Risk](reviewer-reports/revenue-risk/report.md), and [Project Health](reviewer-reports/project-health/report.md)

## Evidence Boundary

The assessed code boundary is the public `docusealco/docuseal` repository at tag `3.1.7`, commit `a2d8b855491793870b7b4acf176d2d95ae95ff83`. The audit cutoff is onboarding start on 2026-08-06 in America/Toronto. Later auditor answers and approved public pages are labeled `post-cutoff-validation` and are used only as decision criteria or validation context.

The review excluded DocuSeal Pro implementation, hosted DocuSeal Cloud, organization production/live state, penetration and load testing, dependency installation, code remediation, legal/regulatory determinations, operative vendor contracts, and access to organization or vendor specialists. External components, deployment templates, registry state, assurance records, and private `docusealco/wip` review are documented outside audited scope and were not independently verified.

The product repository was not changed. No local product, security, recovery, capacity, or production tests ran; upstream hosted CI/image-job results are reported only within their actual scope. Coverage remains unmeasured.

The 2026-08-23 publication correction passed the current WGO final/public structural validator. It removed temporary provider calculation evidence, introduced the canonical alias-only public cost receipt, and calibrated the conclusion without recollecting subject evidence or changing the 2026-08-06 cutoff.
