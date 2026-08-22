# Audit Index

## Start Here

This first WGO audit assesses Plausible Analytics for a regional public-library system at the 2026-08-20 cutoff. It compares continuing the self-hosted Community Edition (**Run**), moving to Plausible's hosted service (**Subscribe**), and preserving a future privacy-first replacement assessment (**Replace**).

Start with the [Executive Summary](executive-summary.md). The evidence supports a conditional decision path, not unconditional acceptance of any option: validate Subscribe as the preferred operating direction, keep Run as the controlled interim/fallback, and defer Replace to a funded future shortlist.

## Audience Routes

| Reader | Primary route | Supporting detail |
|---|---|---|
| Director and executive leadership | [Executive Summary](executive-summary.md) | [Open items](controls/open-items.md), [cost/interruption assessment](controls/expense/cost-and-interruption-assessment.md) |
| Digital-services and product owners | [Product Manager Notes](product-manager-notes.md) | [Capability matrix](controls/product/capability-contract-matrix.md), [PDR register](controls/product/pdr-register.md) |
| IT, security, and continuity leads | [Technical Lead Notes](technical-lead-notes.md) | [Architecture register](controls/architecture/adr-register.md), [security flows](controls/security/identity-secret-and-data-flow.md), [recovery view](controls/continuity/recovery-and-control-view.md), [capacity view](controls/scalability/capacity-envelope-and-degradation-view.md) |
| Finance and procurement | [Expense Exposure report](reviewer-reports/expense-exposure/report.md) | [Hosted burn/renewal view](controls/expense/burn-and-renewal.md), [vendor/commercial packet](evidence/packets/vendor-ownership-commercial.md) |
| Successor or maintenance owner | [Maintenance Cost report](reviewer-reports/maintenance-cost/report.md) | [Time-to-safety and care envelope](controls/maintenance/time-to-safety-and-care-envelope.md), [ownership/successor map](controls/contributors/ownership-successor-and-vendor-dependency-map.md) |

All eleven specialist reports and their short handoffs are under [reviewer-reports](reviewer-reports/). Evidence records are in the [evidence ledger](evidence/evidence-ledger.md) and [source-access register](evidence/source-access-register.md).

## Untested Transition Packet

Operationalization produced four source-linked aids without executing a procedure or authorizing a system change: [replacement maintainer](operator-aids/replacement-maintainer.md), [recovery](operator-aids/recovery.md), [observability](operator-aids/observability.md), and [IAM and credential control](operator-aids/iam-and-credential-control.md). All remain `untested`; their authority decisions and proof routes stay in [Open Items](controls/open-items.md).

## Evidence Boundary

The primary code evidence is Plausible Analytics commit `9cc669b97ece3ecd37fcb3950791cb3873d7944d`. Public pages were classified by cutoff; later observations are labelled post-cutoff validation. The review did not inspect the library's deployment, visitor traffic, staff, cloud accounts, backups, contracts, non-public hosted systems, or a replacement candidate. It installed no dependencies and ran no product, load, failure, restore, or penetration tests.

The assumed 18 sites, 2 million annual visits, 14 million annual pageviews, 25 dashboard users, and seasonal peaks are planning inputs, not verified production facts. Missing evidence is carried as an owned [open item](controls/open-items.md), not treated as proof of safety or risk.

The reconciled [audit-and-operationalization cost estimate](controls/cost-estimate.md) is **$87.24 USD** on an API-equivalent token basis, not a Codex invoice; its exact public calculation is in the [current receipt](controls/cost-calculation.json), with the original [audit-only receipt](controls/cost-calculation-audit-only.json) preserved unchanged.
