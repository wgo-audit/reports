# Hosted Burn, Renewal, And Vendor-Control View

Reader question: How do usage, entitlement, billing cadence, renewal, and vendor-control terms affect hosted cash and reporting availability?

## Evidence Boundary

This view uses the [vendor/commercial packet](../../evidence/packets/vendor-ownership-commercial.md), [E-044](../../evidence/evidence-ledger.md#e-044), [E-045](../../evidence/evidence-ledger.md#e-045), and cutoff-effective public terms/exit evidence in [E-039](../../evidence/evidence-ledger.md#e-039). Current price-table amounts were observed on 2026-08-21 and are post-cutoff validation. No account, invoice, Enterprise quote, contract, tax record, discount approval, actual usage, peak profile, or billing owner was accessed.

The public page dynamically retrieves a symbol and displayed `$`; it does not establish an ISO currency for procurement. Amounts below are therefore **displayed `$` units, currency code unknown**. They are not CAD, USD, tax-inclusive, or binding-quote claims.

## Evidence Dimensions Used

Public list-price, quota, discount, overage, cancellation, renewal, account-role, and terms evidence is present. Negotiated entitlement, quote, tax, currency, library authority, actual usage, support/SLA, and payment/renewal operation are unknown.

## Current Source-Bounded Position

### Entitlement and quota gate

| Gate | Transparent calculation | Result |
|---|---|---|
| Average pageviews | 14,000,000 / 12 | **1,166,666.67/month** before custom events. |
| Billable volume | `B_m = pageviews_m + custom_events_m` | `custom_events_m` and peak `B_m` are unknown. |
| 1M tier | 1,000,000 - 1,166,666.67 | **-166,666.67** before custom events; insufficient even at the annual-average assumption. |
| 2M traffic headroom | 2,000,000 - 1,166,666.67 | **833,333.33** for custom events and peak variance only if pageviews were uniform; they are not verified uniform. |
| Business site/member limits | 18 - 10 sites; 25 - 10 members | Exceeds published limits by **8 sites** and **15 members**; Enterprise configuration is required for one team. A multi-team topology is separately billed and unassessed. |

### Public traffic-only calibrations—not library prices

| Business traffic tier | Monthly list x 12 | Annual display (`10 x monthly`) | First annual payment after stated 15% Business discount | Applicability |
|---|---:|---:|---:|---|
| 1M | `$139 x 12 = $1,668` | `$139 x 10 = $1,390` | `$1,390 x 0.85 = $1,181.50` | Insufficient for assumed average pageviews; also fails site/member limits. |
| 2M | `$179 x 12 = $2,148` | `$179 x 10 = $1,790` | `$1,790 x 0.85 = $1,521.50` | Traffic-only lower-bound calibration; fails site/member limits and excludes custom-event/peak uncertainty. |
| 5M | `$259 x 12 = $3,108` | `$259 x 10 = $2,590` | `$2,590 x 0.85 = $2,201.50` | Sensitivity calibration if 2M is insufficient; still fails site/member limits. |

The annual display saves two displayed monthly payments: 2M saves `$358` versus 12 monthly payments and 5M saves `$518`. The public 15% nonprofit/education offer applies only to the first annual Business payment; qualification is not approved and no evidence extends it to Enterprise. Taxes may be added. Under a one-team role/reporting model, the Enterprise quote, currency, included pageview-plus-event quota, 18-site/25-member entitlement, and ordered-journey/API/support terms remain unknown. A multi-team model would require separate subscriptions and Product Value/governance acceptance.

### Burn, renewal, and interruption controls

| Control point | Public position | Exposure | Required control |
|---|---|---|---|
| Seasonal quota | One over-limit month requires no action. Two consecutive over-limit months trigger notice and an upgrade request; no action within the stated week can lock dashboards while collection continues. | Annual totals do not neutralize consecutive peak months. Custom search/registration events increase billed volume. | Forecast monthly `B_m`, retain peak headroom, assign an owner and successor to notices, and pre-authorize the approval path. Preserve the unanswered outage tolerance in [OI-002](../open-items.md#oi-002). |
| Plan change | Changes are described as pro-rated on monthly and annual billing. | Emergency upgrades can create unplanned cash and procurement delay. | Obtain Enterprise price bands or an approved change mechanism in the quote. |
| Renewal and price change | Paid customers are billed automatically; public terms allow changes and state at least 30 days' email notice for existing-customer price changes. | A missed notice, payment failure, or unapproved renewal can interrupt dashboard access or create unauthorized spend. | Name billing/procurement primary and successor owners, renewal date, notice mailbox, payment path, approval ceiling, and cancellation deadline through [OI-015](../open-items.md#oi-015). |
| Cancellation/termination | Paid-period access continues after cancellation; public documentation describes dashboard lock/export access and later collection stop/deletion. Terms permit suspension/termination and do not guarantee uninterrupted/error-free service. | Exit without a verified export can break reporting continuity; support is reasonable-effort email in public terms, not an SLA. | Contract for accepted notice/support/export/deletion terms and exercise a bounded export before acceptance. |
| Multi-team billing | Each team has a separate subscription. | Splitting sites or staff can multiply subscriptions and fragment access/reporting; it is not evidenced as an entitlement workaround. | Require one written architecture/quote for the intended 18-site/25-member role model; do not optimize by team splitting without Product Value and governance acceptance. |

## Material Unknowns And Closure Routes

Close [OI-017](../open-items.md#oi-017) with a dated Enterprise quote and a verified monthly pageview-plus-custom-event profile, including seasonal peaks. The quote must identify ISO currency, tax, site/member/role entitlement, billable-usage definition, quota-change prices, discount, term, automatic renewal, price-change notice, support/SLA, cancellation, export, and deletion. Close ownership/exit through [OI-015](../open-items.md#oi-015) and define affordability through [OI-018](../open-items.md#oi-018). Recheck public pricing at procurement time; current public amounts do not bind the vendor.
