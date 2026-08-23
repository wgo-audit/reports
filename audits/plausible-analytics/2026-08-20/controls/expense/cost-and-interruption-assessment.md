# Cost And Interruption Exposure Assessment

Reader question: What cash and interruption exposure can be responsibly compared for Run, Subscribe, and Replace from the approved evidence?

## Evidence Boundary

This assessment uses the approved source at commit `9cc669b97ece3ecd37fcb3950791cb3873d7944d`, the [vendor/commercial packet](../../evidence/packets/vendor-ownership-commercial.md), public pricing and terms, and the Architecture, Product Value, Business Continuity, and Cloud Security evidence boundaries. The cutoff is 2026-08-20 at onboarding start, America/Toronto. The public price table was observed on 2026-08-21 and is post-cutoff validation; dated public plan, billing, discount, cancellation, and terms pages were effective by the cutoff.

No library invoice, cloud bill, resource inventory, staff hours/rates, contract, hosted quote, tax decision, discount approval, replacement candidate, live traffic, or non-public service evidence was available. This is a planning assessment, not an actual-spend statement, quote, procurement conclusion, legal conclusion, or reliability-loss valuation.

## Evidence Dimensions Used

Implementation and responsibility evidence, public commercial terms, current public list-price calibration, and working scale assumptions are present. Actual operation, ownership/approval, library cost, procurement currency/tax, hosted entitlement/quote, replacement pricing, and the monetary consequence of interruption are unknown.

## Current Source-Bounded Position

### Planning basis and exact calculations

| Input or calculation | Value | Status and limit |
|---|---:|---|
| Annual visits | 2,000,000 | Working assumption, not hosted billing input. |
| Annual pageviews | 14,000,000 | Working assumption. |
| Average monthly pageviews | 14,000,000 / 12 = **1,166,666.67** | Lower bound for hosted monthly billable volume before custom events; seasonal peaks are unknown. |
| Pageviews per visit | 14,000,000 / 2,000,000 = **7.0** | Descriptive assumption ratio, not a capacity or pricing claim. |
| Hosted monthly billable volume | **pageviews + custom events** across all sites in one team | Custom-event volume is unknown; pageview goals do not add usage. |
| Sites and staff | 18 sites; 25 dashboard staff | Working assumptions. Published Business caps are 10 sites and 10 team members, so a custom Enterprise configuration is required if the intended role/reporting model uses one team. A multi-team topology is separately billed and unassessed. |

The current public Business table is useful only as a traffic-price calibration. At 2M pageviews/events it displays `$179` monthly, `$1,790` annually, and a mathematically discounted first annual payment of `$1,521.50` if the 15% nonprofit/education Business discount is approved. Those values do **not** price the library: the 18-site/25-member requirement exceeds Business limits, Enterprise pricing is custom, the page supplies only a `$` symbol rather than an ISO currency, tax is unknown, and the discount is not stated for Enterprise ([E-044](../../evidence/evidence-ledger.md#e-044), [E-045](../../evidence/evidence-ledger.md#e-045)).

### Option exposure

| Option | Evaluable cash position | Required cash categories/formula | Interruption and commitment exposure | Smallest closure route |
|---|---|---|---|---|
| Run | Plausible CE has no fee payable to Plausible and source-visible application limits are unlimited; actual total cash exposure is **unknown**. | `Run annual cash = sum of applicable compute, PostgreSQL, ClickHouse, storage, backup/restore, network/CDN, mail, geolocation, monitoring/logging, registry/security tooling, external support, and paid-labour cash`. Add applicable one-time recovery, provenance, edge, governance, and correction work. Do not assign values or assume a category is enabled until invoices, configuration, allocations, hours, and rates exist. | The library owns capacity, uptime, backup, security, upgrades, dual-store recovery, queue/reporting, deletion, and successor control. Unchosen loss/outage tolerances prevent monetary interruption modelling. | [OI-017](../open-items.md#oi-017), with service tolerance retained in [OI-002](../open-items.md#oi-002). |
| Subscribe | Public standard prices do not establish the 18-site/25-member shape. Under a one-team role/reporting model, an Enterprise quote is **unknown**; a separately billed multi-team model is unassessed. | `Subscribe first-year cash = quoted subscription(s) + applicable tax + implementation/instrumentation + security/privacy/procurement review + migration/export + overlap + training`. `Recurring cash = renewal quote(s) + tax + retained governance/reporting/account work`. | Two consecutive over-limit months can lead to a dashboard lock if the upgrade notice is not acted on within the documented week, though collection continues. Nonpayment, cancellation, suspension, service/price change, reasonable-effort support, and absent public uptime guarantee add retained vendor-control exposure. | Obtain a dated one-team Enterprise quote or an accepted multi-team topology with complete quotes, plus a 12-month billable-volume profile, through [OI-017](../open-items.md#oi-017); assign billing/renewal/exit owners through [OI-015](../open-items.md#oi-015). |
| Replace | No funded candidate, quote, or comparative operating evidence exists; cash exposure is **unknown**. | This fiscal year, bound categories only: requirements/selection, privacy/security/procurement review, proof of concept, instrumentation rewrite, data migration/export, reporting rebuild, training/change, dual-run overlap, contract/exit, and candidate subscription or infrastructure. Do not monetize or score a candidate before one is approved. | Selection and migration can consume scarce time, create duplicate-run costs, interrupt trend continuity, and leave two systems operating during overlap. Absence of a candidate is not evidence of savings or lower risk. | Retain as a future bounded selection using the same capability, governance, recovery, ownership, quota, and exit criteria; fund and approve a candidate before pricing. |

### Interruption valuation formula

No responsible dollar loss can be calculated from this corpus. If the library later supplies tolerances and an approved valuation basis, use:

`interruption exposure = outage duration x affected staff/service cost rate + recovery labour + replacement/expedite cash + approved value of lost or delayed measurement`.

Event-loss, reporting-outage, reputational, and governance consequences must remain separate; a missing advertising-revenue model is consistent with the mandate and must not be invented.

## Material Unknowns And Closure Routes

- [OI-017](../open-items.md#oi-017) requires one comparable evidence set: 12 months of Run cash/resource/hour records, a 12-month pageview-plus-custom-event profile with peak months, and a dated Enterprise quote naming currency, tax, entitlement, term, renewal, discount, support, and exit.
- [OI-018](../open-items.md#oi-018) asks the Director to set the first-year and recurring annual cash ceilings and comparison horizon. Without them, the audit can compare exposure but not affordability.
- [OI-002](../open-items.md#oi-002) and [OI-007](../open-items.md#oi-007) remain unanswered. [OI-008](../open-items.md#oi-008) remains the governing data/access/retention decision. No cost assumption closes them.
- Maintenance Cost may quantify internal care in hours after owner/activity evidence exists; it must not convert this category list into invented labour or infrastructure cash.
