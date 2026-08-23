# Revenue Risk

## Audit Question, Depth, And Evidence Boundary

What could interrupt a Plausible demo, sales/onboarding flow, renewal,
expansion, trust, or customer delivery, and what should that change in the CTO
decision? This detailed, read-only review is bounded to approved public product,
legal, status, Git, issue, and pull-request evidence through 2026-08-22 22:08:28
EDT and `primary-code` commit
`9cc669b97ece3ecd37fcb3950791cb3873d7944d`. It reused Product Value and
Business Continuity evidence; public positioning was not treated as proof of
live operation, customer-effective entitlement, acceptance, contract scope,
commercial ownership, revenue, or financial health.

No safe demo identity, fixture, or environment was approved, so no golden-path
observation ran. No customer contract, order form, renewal/support record,
production record, or internal commercial/vendor record was available. Current
August security-page expansions have unknown cutoff-effective timing and were
excluded from cutoff assurance.

## Coverage And Material Gaps

`[Verified audit observation]` Coverage includes plan/entitlement and usage
boundaries, Enterprise raw export, Events API integration semantics, privacy
claims, Cloud/CE responsibility, backup/recovery/monitoring claims, public
incident communication, native export, SSO, and the CE import-loss report/fix
history. Relevant public GitHub history was inspected specifically rather than
using counts: raw-export PR #5963 and predecessor-linked #5574; import issue
#6515 and proposed PR #6547; Events API issue #1246 and PR #2351; plan-gating PR
#6393 and predecessor-linked v5 history.

The material gaps remain the live demo under
[OI-008](../../controls/open-items.md#oi-008), customer-effective entitlement
under [OI-009](../../controls/open-items.md#oi-009), premium raw-export delivery
under [OI-010](../../controls/open-items.md#oi-010), privacy/observability claim
reconciliation under [OI-011](../../controls/open-items.md#oi-011) and
[OI-015](../../controls/open-items.md#oi-015), integration contract/durability
under [OI-001](../../controls/open-items.md#oi-001) and
[OI-012](../../controls/open-items.md#oi-012), and Cloud recovery/response under
[OI-021](../../controls/open-items.md#oi-021) and
[OI-023](../../controls/open-items.md#oi-023). No duplicate evidence or open
item was allocated; E-001–E-081/OI-001–OI-028 retain their existing meanings.

## Key Findings

| Finding | Severity | Effort | Evidence links | Confidence and limitation | Consequence | Taxonomy |
|---|---|---|---|---|---|---|
| `[Verified source/history finding]` The pinned CE failure-classification path can purge completed imported analytics; issue #6515 reports the outcome and proposed PR #6547 was still open and unreviewed at the cutoff. | Critical | M | [E-016](../../evidence/evidence-ledger.md#e-016), [claim register](../../controls/revenue/claim-governance-and-exposure-register.md) | High for the source path and cutoff PR state; deployed versions, incidence, affected users, and actual revenue/customer effects are unknown. | A destructive onboarding/import path can cause data loss and materially damage retention and trust. | none |
| `[Plausible public claim]` Enterprise offers scheduled raw-event delivery; `[verified bounded search]` exact benefit history exists, but no scheduler, destination delivery, schema/version, or fulfillment service was established in the approved monorepo. | High | M | [E-029](../../evidence/evidence-ledger.md#e-029), [E-035](../../evidence/evidence-ledger.md#e-035), [claim register](../../controls/revenue/claim-governance-and-exposure-register.md) | High for the promise and bounded repository result; an internal service and customer-effective terms may exist outside scope. | Expansion or customer delivery can depend on a premium promise whose service, security, acceptance, and support boundaries are unproved. | none |
| `[Verified fact]` Public plan groupings broadly match visible gates, but plan generations, Paddle prices, custom terms, grandfathering, CE/EE paths, and tracker variants make customer-effective entitlement unknown. | High | M | [E-025](../../evidence/evidence-ledger.md#e-025), [E-033](../../evidence/evidence-ledger.md#e-033), [claim register](../../controls/revenue/claim-governance-and-exposure-register.md) | High for source/public alignment; no customer price, contract, entitlement, acceptance, or renewal record was available. | Quotes, onboarding, upgrades, and renewals can present the wrong capability, limit, price, or access outcome. | none |
| `[Verified source/public conflicts]` Public privacy wording conflicts with a 48-hour salt-row cleanup boundary and with source that can attach raw IP/User-Agent to Sentry context; actual DSN use, error occurrence, vendor receipt/retention, and specialist interpretation are unknown. | High | M | [E-027](../../evidence/evidence-ledger.md#e-027), [E-031](../../evidence/evidence-ledger.md#e-031), [E-037](../../evidence/evidence-ledger.md#e-037), [claim register](../../controls/revenue/claim-governance-and-exposure-register.md) | High for the source/copy conflict; this does not establish actual disclosure or noncompliance. | Repeating categorical privacy claims without reconciliation can undermine assurance, sales, and customer trust. | none |
| `[Plausible public claim]` Managed Cloud owns availability, backup, security, maintenance, capacity, and monitoring; `[verified public history]` a November 2025 status update said ingestion resumed while lost data was being restored, but completed restoration, reconciliation, RPO/RTO, and alert-to-closure proof were unavailable. | High | M | [E-046](../../evidence/evidence-ledger.md#e-046), [E-047](../../evidence/evidence-ledger.md#e-047), [E-048](../../evidence/evidence-ledger.md#e-048), [E-050](../../evidence/evidence-ledger.md#e-050), [claim register](../../controls/revenue/claim-governance-and-exposure-register.md) | High for responsibility claims/configuration/public incident text; live effectiveness, loss amount, completion, customer effect, and contractual consequence are unknown. | A renewal or trust conversation can depend on recovery assurances the incoming CTO cannot yet substantiate. | none |
| `[Verified contract mismatch]` Events API docs show `{}` while source and repository checks use text `ok`; documented `202` can include policy-dropped events and is not durable insertion. | High | M | [E-002](../../evidence/evidence-ledger.md#e-002), [E-021](../../evidence/evidence-ledger.md#e-021), [E-032](../../evidence/evidence-ledger.md#e-032), [claim register](../../controls/revenue/claim-governance-and-exposure-register.md) | High for the source/docs/history; deployed behavior, client parsing, loss frequency, and customer impact were not observed. | Integrators can parse the wrong body or treat acceptance as durable analytics, producing false success or trust loss. | none |
| `[Unknown]` Demo readiness cannot be classified because the approved audit boundary contains no safe identity, fixture, or environment. | Medium | S | [audit brief](../../audit-brief.md), [OI-008](../../controls/open-items.md#oi-008) | Certain evidence limit; it is neither evidence of readiness nor evidence of failure. | Making a sales/readiness claim from source alone would convert an unobserved journey into false confidence. | none |

## Mandate-Relevant Strengths

- `[Verified fact]` The public capability story is broadly represented in a
  coherent tracker, query, goals, collaboration, SSO, import/export, billing,
  and edition surface. [E-020](../../evidence/evidence-ledger.md#e-020)
- `[Verified fact]` Public guidance candidly states many limits: dropped-event
  `202` cases, API heuristics, imported-data constraints, export exclusions,
  usage grace/locking, and Cloud/CE responsibility differences.
  [E-021](../../evidence/evidence-ledger.md#e-021)
  [E-022](../../evidence/evidence-ledger.md#e-022)
  [E-026](../../evidence/evidence-ledger.md#e-026)
  [E-047](../../evidence/evidence-ledger.md#e-047)
- `[Verified fact]` Central feature gates and public PR history make
  entitlement changes more traceable than scattered marketing-only behavior,
  even though customer-effective state is unavailable.
  [E-025](../../evidence/evidence-ledger.md#e-025)
  [E-033](../../evidence/evidence-ledger.md#e-033)
- `[Verified fact]` Public status history gives incoming leadership a starting
  point for incident and claim reconciliation rather than hiding all service
  interruption from public view. [E-050](../../evidence/evidence-ledger.md#e-050)

### Decision Insights

- **Normal product-governance onboarding:** Build a versioned claim-to-proof map
  across product, billing, legal/privacy, operations, and support after joining.
  Customer-effective and live evidence is private by nature, so its absence is
  neutral for accepting the role. The linked claim register plus representative
  entitlement, raw-export, recovery, and demo evidence provides a practical
  first-month route without presuming hidden obligations or failure.
- **Immediate risk sequence:** Correct/prove the destructive CE import path and
  conditional Sentry disclosure before using broader product positioning as a
  reassurance. Both are source-visible harm paths, whereas many other gaps are
  proof deficits. [OI-006](../../controls/open-items.md#oi-006)
  [OI-015](../../controls/open-items.md#oi-015)
- **Commercial statement boundary:** Until OI-001/OI-010/OI-012 close, describe
  Events API `202` as acceptance rather than durability and scheduled raw
  export only as a public Enterprise capability pending customer-effective
  service proof. A wrong wording choice can turn technical ambiguity into a
  sales or delivery commitment.
- **First-30-day verification:** Observe one approved tracker-to-dashboard
  golden path, one current and one grandfathered entitlement result, one
  scheduled raw-export delivery, one native export lifecycle, and one
  backup/alert-to-recovery exercise. These observations verify distinct claims;
  none should substitute for the others.

## Selected Outputs

- Required claim/demo/commercial assessment: this report.
- Triggered [claim-governance and commercial-exposure register](../../controls/revenue/claim-governance-and-exposure-register.md),
  because material plan, Enterprise, API, privacy, Cloud, recovery, import,
  export, and SSO promises are evidenced.
- Golden-path observation was not produced because the audit brief approved no
  safe identity, fixture, or environment. This means demo readiness remains
  unclassified—not failed—and [OI-008](../../controls/open-items.md#oi-008)
  carries the observation route.
- The `vendor-ownership-commercial` packet was not requested because no
  approved vendor agreement, customer contract/order form, renewal/support
  record, tenant entitlement record, or commercial ownership record could
  populate it. Public terms and source references are not substitutes;
  [OI-009](../../controls/open-items.md#oi-009) and
  [OI-022](../../controls/open-items.md#oi-022) carry the smallest evidence
  expansion.

## Material Omissions, Unknowns, And Auditor Questions

No auditor question is required. The remaining decision-changing needs require
Plausible-held customer, service, billing, legal/privacy, operational, support,
and ownership proof—not an auditor assertion. Contract terms, customer counts,
revenue amount/mix, renewal probability, financial health, actual customer
impact, and individual/team performance remain unknown and are not inferred.

`Documented outside audited scope; not independently verified.` This applies to
the separate Community Edition packaging/upgrade repository, any internal
raw-export or managed-proxy service, private Cloud controls, customer contracts,
Paddle/customer records, and support/renewal records.

No reviewer-specific application or dependency-free executable test was run:
0 passed, 0 failed, 0 errored, 0 skipped. No dependency was installed or
restored, and no live demo, billing call, export, support workflow, or production
operation ran. Read-only source navigation and public GitHub/API inspection are
evidence collection, not product tests.

## Reconciliation

Product Value's broadly aligned product surface and Business Continuity's
source-visible operating primitives were retained, but neither was promoted to
live delivery or customer acceptance. The public Cloud responsibility/security
claims conflict with unavailable control-effectiveness proof, and the public
incident update lacks accessible completion/reconciliation. The raw-export,
Events API, salt, Sentry, and CE-import conflicts remain routed through their
existing open items; no new OI was needed.

Specific GitHub inspection confirmed cutoff state without changing predecessor
evidence: PR #5963 merged the raw-export Enterprise benefit; issue #6515 and PR
#6547 left the destructive CE-import correction open; issue #1246/PR #2351
explain the `ok`/drop-header response history; PR #6393 applied a visible plan
gate. Public metadata does not prove deployment or customer outcome.

The single delegated artifact-quality review returned `revision required`. One
bounded revision added the conditional Sentry claim conflict, removed an
unsupported customer-agreed cadence implication, bounded the raw-export absence
to the approved monorepo, and linked the audit boundary for the demo/packet
decisions. No second quality pass ran.

Structural validation ran with Python 3.13.11 using `python3
plugins/wgo/skills/wgo/scripts/validate_audit_structure.py
_whats-going-on-20260822` from the project root and returned `0 error(s), 0
warning(s)`. This validates structure, link/form conventions, and portability,
not live behavior or commercial conclusions.

## Bounded Conclusion And Downstream Guidance

`[Verified audit conclusion]` Plausible has a broad, source-visible product and
candid public constraints, but the approved corpus cannot support unconditional
claims about demo readiness, customer-effective entitlements, premium
fulfillment, privacy assurance, recovery completion, or customer delivery. The
decision-changing revenue exposure is governance: the CTO needs authority and
evidence access to map each material promise to implementation, live proof,
customer scope, owner, and correction.

Project Health may use the source-visible claim conflicts, specific GitHub
history, and open verification routes. It must not infer contracts, customers,
revenue amount, probability, financial health, live operation, customer harm,
or people performance.
