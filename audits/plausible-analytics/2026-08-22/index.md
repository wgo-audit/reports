# Plausible Analytics CTO Inheritance Audit

## Start Here

This audit supports a **positive lean toward accepting the CTO role**, assuming the people, mandate, expectations, authority, and compensation are attractive. Plausible's public monorepo shows a coherent product, an understandable Phoenix/OTP architecture, deliberate PostgreSQL/ClickHouse boundaries, broad automated checks, meaningful security hygiene, and public examples of substantive review and remediation. Nothing public suggests a sloppy team, poor architecture, or a product in technical distress. The audit also identifies one important Community Edition import defect and a short list of targeted corrections, best understood as a normal engineering backlog rather than evidence of organizational failure.

Read the [executive summary](executive-summary.md) first for the realistic role assessment, tailored interview questions, and first-30-day learning and verification plan.

## Audience Routes

- CTO candidate and executive sponsor: [Executive Summary](executive-summary.md)
- Product, pricing, documentation, and customer commitments: [Product Manager Notes](product-manager-notes.md)
- Architecture, quality, operations, security, and safe-change detail: [Technical Lead Notes](technical-lead-notes.md)
- Canonical evidence: [Evidence Ledger](evidence/evidence-ledger.md), [Source Access Register](evidence/source-access-register.md), and [Open Items](controls/open-items.md)
- Specialist reports: [Reviewer Reports](reviewer-reports/)
- Architecture and data flows: [System Flow](controls/architecture/diagrams/system-component-and-data-flow.md), [Deployment Path](controls/architecture/diagrams/deployment-and-runtime-path.md), and [Deletion Path](controls/architecture/diagrams/deletion-consistency-path.md)
- Security and operations: [Application Attack Paths](controls/application-security/attack-path-and-control-view.md), [Cloud Control View](controls/cloud-security/cloud-iam-network-runtime-control-view.md), and [Continuity View](controls/continuity/continuity-control-view.md)
- Scale, cost, and delivery: [Capacity View](controls/scalability/capacity-and-degradation-view.md), [Expense Boundary](controls/expense/burn-and-renewal.md), and [Release/Change Control](controls/project-health/release-change-control.md)
- Audit execution cost: [API-Equivalent Cost Estimate](controls/cost-estimate.md) and [Aliased Calculation Receipt](controls/cost-calculation.json)

## Evidence Boundary

The audit is read-only and bounded to public Plausible evidence through **2026-08-22 22:08:28 EDT**: `plausible/analytics` on `master` at commit `9cc669b97ece3ecd37fcb3950791cb3873d7944d`, its public GitHub history, issues, pull requests, reviews, releases, Actions, advisory records, and approved `plausible.io` pages. Relevant GitHub issues and pull requests were inspected individually, including the CE import-loss, Stats API, ingestion, deletion, tracker, migration, security, and release records cited in the ledger.

No production environment, cloud account, internal repository, customer record, contract, bill, private incident record, staff interview, or live control test was available. Missing public proof is neutral: it is never evidence that a control or practice is absent, never evidence of sloppiness, and never by itself an offer condition. Those topics become normal onboarding discovery if the role proceeds. Current privacy/security pages that identify themselves as August 2026 contain expanded claims whose cutoff-effective timing is unknown and therefore do not backfill the cutoff assessment. The audit does not grade people, infer morale, declare regulatory compliance, or infer financial health.

Local application tests did not run: **0 passed, 0 failed, 0 errors, 0 skipped**. Required toolchains, dependencies, and services were absent, and installation or restoration was not authorized. Source-level and dependency-free audit checks, hosted GitHub job evidence, and each reviewer's exact test limits are preserved in the specialist reports.

The audit's recorded model requests have a final API-equivalent estimate of **$109.29 USD**; this is not a Codex invoice. See the [cost estimate](controls/cost-estimate.md) for the frozen boundary, exact basis, and limitations.
