# Product Provenance Notes

## Evidence Boundary

- Approved source: `primary-code` commit `9cc669b97ece3ecd37fcb3950791cb3873d7944d` (2026-08-19).
- Targeted history: commit `380fad72adc14b67d4c601fdbba8e7cd641db627` (2025-06-19) updated the Cloud/CE comparison to keep it consistent with the public website; the current snapshot later includes SSO in the CE exclusions.
- Public pages observed 2026-08-21 are post-cutoff validation only ([E-020](../../evidence/evidence-ledger.md#e-020)–[E-022](../../evidence/evidence-ledger.md#e-022)).
- Public CI for the exact commit is bounded in [E-010](../../evidence/evidence-ledger.md#e-010); its EE-only dashboard E2E does not demonstrate CE or library workflows.

## Claim Reconciliation

| Claim | Source/history support | Bounded conclusion |
|---|---|---|
| Goals, custom events, trends, CSV/API, roles, and monthly email exist | Current implementation plus README/changelog | Implemented in assessed source; not deployed/accepted proof. |
| CE omits marketing funnels/user journeys | README comparison, `on_ee` routes, targeted comparison history | Strong source-backed edition boundary; exact deployed CE tag still unknown. |
| Hosted includes all features | README promise and EE implementation | Product promise/implementation only; plan entitlement and hosted operation were not inspected. |
| CE supports 18 sites and 25 users | CE source compiles unlimited application limits | No application limit in assessed source; not a performance, storage, or operational-capacity conclusion. |
| Monthly reporting is available | Scheduler/sender/controller source and current public docs | Fixed prior-month email summary exists in source; delivery, content acceptance, and recipient governance unknown. |

## Demonstration And Acceptance Limit

No golden-path observation was attempted because no safe configured environment, test identity, and fixture were approved. [OI-006](../open-items.md#oi-006) is the smallest non-production validation route. No product source establishes privacy/security/legal sign-off, procurement acceptance, or a replacement product's fit.
