# Product Provenance Notes

## Evidence Boundary

The implementation boundary is `primary-code` at master commit `9cc669b97ece3ecd37fcb3950791cb3873d7944d` (2026-08-19). Approved Plausible website material is treated as provider-authored promise/documentation. Pages re-read on 2026-08-23 are post-cutoff validation; their dated revisions and the catalog establish what was available by the 2026-08-22 22:08:28 EDT cutoff where stated. Mutable web content is not a customer contract snapshot.

## Evidence Dimensions Used

Implementation and public promise are broad. Public GitHub rationale is targeted rather than exhaustive. Customer contracts, product telemetry, Paddle records, support/usage data, internal decision records, live configuration, and specialist/legal assessment are unknown.

## Current Source-Bounded Position

| Source/provenance | Use | Supersession/cutoff treatment | Limitation |
|---|---|---|---|
| `primary-code:README.md`, `CHANGELOG.md` | Product/edition map and released/unreleased change history | Pinned commit controls source state; `Unreleased` is not treated as shipped | A changelog entry is not deployment or adoption evidence. |
| `primary-code:tracker/ARCHITECTURE.md`, tracker README/changelog/workflows | Tracker rationale, variants, release controls | Current pinned files supersede older source descriptions | No npm registry or cloud-promotion proof. |
| `primary-code:priv/plans_v5.json`, billing feature/benefit/plan/quota modules | Visible plan and entitlement semantics | Multiple plan generations and runtime Paddle/custom inputs remain active boundaries | Not a customer-specific price/entitlement record. |
| Plausible homepage, docs, data policy, security, DPA, privacy, terms | Provider claims and disclosed behavior | Re-read after cutoff only to validate the approved catalog; dated page revisions are recorded in ledger evidence | Claims do not prove operating controls, acceptance, compliance, or legal sign-off. |
| Public GitHub commits/issues/PRs/reviews | [E-031](../../evidence/evidence-ledger.md#e-031), [E-032](../../evidence/evidence-ledger.md#e-032), [E-033](../../evidence/evidence-ledger.md#e-033), [E-034](../../evidence/evidence-ledger.md#e-034), [E-035](../../evidence/evidence-ledger.md#e-035), and [E-036](../../evidence/evidence-ledger.md#e-036) supply targeted salt, Events API, v5 plan, tracker-release, Enterprise-benefit, and edition history | State is bounded at cutoff; later state is validation only | Open PRs are proposals; merged PRs are not deployment proof. Exact benefit strings do not prove implementing services. |
| `plausible/docs`, `plausible/community-edition`, internal services/runbooks | Referenced but not approved primary corpus | `Documented outside audited scope; not independently verified.` | Cannot close CE operations, raw-export fulfillment, or documentation workflow. |

## Material Unknowns And Closure Routes

- Customer-specific price, grandfathered plan, overrides, and entitlement output: [OI-009](../open-items.md#oi-009).
- Scheduled raw-export implementation and delivered output: [OI-010](../open-items.md#oi-010).
- Privacy/legal interpretation and deployed salt/data-lifecycle evidence: [OI-011](../open-items.md#oi-011).
- Live golden path and customer acceptance: [OI-008](../open-items.md#oi-008); no safe demo identity/environment was approved.
