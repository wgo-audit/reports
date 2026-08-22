# Expense Exposure

## Audit Question, Depth, And Evidence Boundary

This detailed review asks what actual or potential cash and interruption exposure arises from infrastructure, software, staffing, commitments, quota, and failure modes across Run, Subscribe, and Replace. The cutoff is 2026-08-20 at onboarding start, America/Toronto. Evidence is the approved `primary-code` snapshot at commit `9cc669b97ece3ecd37fcb3950791cb3873d7944d`, Architecture/Product Value/Business Continuity/Cloud Security evidence, one bounded [vendor/commercial packet](../../evidence/packets/vendor-ownership-commercial.md), cutoff-effective public billing/terms pages, and a current price-table observation used only as post-cutoff validation.

The review used the working assumptions of 18 sites, 2 million annual visits, 14 million annual pageviews, 25 dashboard staff, and seasonal peaks. It did not access invoices, cloud accounts, staff hours/rates, a hosted account/quote/contract, taxes, actual usage, procurement approval, non-public systems, or a replacement candidate; it did not buy, change, load-test, or make a legal conclusion. No dependency was converted into spend.

## Coverage And Material Gaps

Coverage includes CE license/operating responsibility, public hosted quotas and site/member limits, pageview-plus-event billing, traffic spikes, plan changes, annual billing/discount arithmetic, taxes, renewal/price-change/cancellation/support terms, option-specific operating categories, interruption paths, and Replace selection/migration/overlap categories. Exact calculations and formulas are in the [cost/interruption assessment](../../controls/expense/cost-and-interruption-assessment.md) and [burn/renewal view](../../controls/expense/burn-and-renewal.md).

Material cash exposure cannot be bounded until [OI-017](../../controls/open-items.md#oi-017) supplies actual Run records, a monthly billable-volume profile, and an Enterprise quote. Affordability cannot be judged until [OI-018](../../controls/open-items.md#oi-018) sets first-year/recurring ceilings and a horizon. [OI-002](../../controls/open-items.md#oi-002)/[OI-007](../../controls/open-items.md#oi-007) remain unanswered and [OI-008](../../controls/open-items.md#oi-008) remains governance.

## Key Findings

| Finding | Severity | Effort | Evidence links | Confidence and limitation | Consequence | Taxonomy |
|---|---|---|---|---|---|---|
| None of Run, Subscribe, or Replace has an evidenced total cash amount. Run lacks bills/resources/hours/rates, Subscribe requires a custom Enterprise quote, and Replace has no funded candidate. | High | M | [E-001](../../evidence/evidence-ledger.md#e-001), [E-039](../../evidence/evidence-ledger.md#e-039), [E-044](../../evidence/evidence-ledger.md#e-044), [assessment](../../controls/expense/cost-and-interruption-assessment.md), [OI-017](../../controls/open-items.md#oi-017) | High confidence in evidence absence within the approved boundary; no claim that any option is expensive or affordable. | A recommendation based on “free CE,” a public hosted list price, or assumed replacement savings could materially misstate budget and operating burden. | project-defined cost-evidence control |
| The assumed 18 sites and 25 staff exceed published Business limits of 10 sites and 10 team members. Under an intended one-team role/reporting model, hosted Subscribe requires custom Enterprise entitlement regardless of traffic; a separately billed multi-team topology is unassessed. | High | S | [E-018](../../evidence/evidence-ledger.md#e-018), [E-044](../../evidence/evidence-ledger.md#e-044), [burn/renewal view](../../controls/expense/burn-and-renewal.md) | High against public plan limits and working assumptions; actual role/reporting topology and vendor quote are unknown. | Using one 2M Business list price as the library budget would be an unsupported and likely materially understated scenario. | project-defined entitlement/pricing control |
| Fourteen million assumed annual pageviews average 1,166,666.67/month before custom events; hosted billing counts pageviews plus custom events and evaluates sustained monthly overage, so annual pageviews alone cannot size the quota. | High | S | [E-044](../../evidence/evidence-ledger.md#e-044), [E-045](../../evidence/evidence-ledger.md#e-045), [burn/renewal view](../../controls/expense/burn-and-renewal.md), [OI-017](../../controls/open-items.md#oi-017) | Arithmetic is exact; input, event volume, monthly distribution, and peaks are unverified. | Two consecutive peak months can trigger an upgrade decision and, if unhandled within the documented week, a dashboard lock during reporting demand while collection continues. | project-defined quota/availability control |
| Run removes Plausible subscription fees but retains every evidenced infrastructure and operating responsibility, including two datastores, backups/recovery, capacity, edge/security, monitoring, reporting/deletion, upgrades, support triage, and successor control. | High | M | [E-001](../../evidence/evidence-ledger.md#e-001), [E-003](../../evidence/evidence-ledger.md#e-003), [E-035](../../evidence/evidence-ledger.md#e-035)–[E-041](../../evidence/evidence-ledger.md#e-041), [assessment](../../controls/expense/cost-and-interruption-assessment.md) | High for responsibility categories; actual deployment, resources, hours, rates, and spend unknown. | “No vendor fee” can hide recurring cash, staff opportunity cost, and failure/expedite exposure that hosted pricing transfers but does not eliminate. | project-defined total-cost control |
| Public hosted terms leave material commercial continuity with the library: automatic billing, possible tax, non-refundable fees, price/service changes, cancellation/export timing, reasonable-effort support, and no uninterrupted/error-free guarantee. | Medium | M | [E-039](../../evidence/evidence-ledger.md#e-039), [E-045](../../evidence/evidence-ledger.md#e-045), [burn/renewal view](../../controls/expense/burn-and-renewal.md), [OI-015](../../controls/open-items.md#oi-015) | High for public terms; no negotiated contract, SLA, account owner, or effective vendor control was reviewed. | Subscribe can reduce technical care yet still interrupt reporting or create unplanned spend if billing, notices, support, and exit lack owners and accepted terms. | none |
| Replace cannot be assigned savings or spend from the current evidence; only selection, review, implementation, migration, dual-run, training, exit, and future operating categories are supportable. | Medium | L | [E-015](../../evidence/evidence-ledger.md#e-015), [assessment](../../controls/expense/cost-and-interruption-assessment.md) | High that no candidate/quote is in scope; candidate economics unknown. | Premature replacement scoring could consume unfunded fiscal-year capacity and obscure transition/overlap costs. | none |

## Mandate-Relevant Strengths

- CE has no Plausible fee and source-visible application site/member limits are unlimited, so 18 sites/25 staff do not create a source-visible licence or seat charge for Run ([E-018](../../evidence/evidence-ledger.md#e-018), [E-039](../../evidence/evidence-ledger.md#e-039)).
- Public hosted documentation states that a one-month spike adds no overage fee, collection continues during a quota-related dashboard lock, changes are pro-rated, and annual billing displays two months free. These are useful cash/continuity terms to verify in a quote ([E-044](../../evidence/evidence-ledger.md#e-044), [E-045](../../evidence/evidence-ledger.md#e-045)).
- A 15% introductory nonprofit/education discount exists for a first annual Business payment; it is a procurement lead, not an Enterprise entitlement or approved saving ([E-045](../../evidence/evidence-ledger.md#e-045)).

### Decision Insights

1. **Entitlement/topology, not traffic alone, is the first Subscribe price gate.** The 18-site/25-member assumption exceeds one Business team's limits, making one standard-tier amount only a calibration. Through [OI-017](../../controls/open-items.md#oi-017), obtain either a one-team Enterprise entitlement/quote or an accepted multi-team topology with all separate subscriptions before comparing cash.
2. **Instrumentation design changes hosted burn.** Search/registration custom events count alongside pageviews, so Product Value acceptance and the unresolved ordered-journey requirement change quota demand. Inventory representative monthly event counts before choosing headroom.
3. **Run must be compared as total operated service, not zero licence.** The dual-store/recovery/security/reporting responsibility set creates infrastructure, labour, opportunity, and interruption exposure. Capture actual records through [OI-017](../../controls/open-items.md#oi-017), then let Maintenance Cost quantify care.
4. **Replace is a deferred option-definition cost, not an evidenced saving.** Carry the existing requirements into a future funded shortlist and include migration plus dual-run overlap; do not score unknown vendor/infrastructure prices.

## Selected Outputs

- [Vendor, ownership, and commercial evidence packet](../../evidence/packets/vendor-ownership-commercial.md)
- [Cost and interruption exposure assessment](../../controls/expense/cost-and-interruption-assessment.md)
- [Hosted burn, renewal, and vendor-control view](../../controls/expense/burn-and-renewal.md)

The burn/renewal view was triggered because quota, standard-plan entitlement, automatic billing, price-change, cancellation, support, and dashboard-lock boundaries materially affect the decision.

## Material Omissions, Unknowns, And Auditor Questions

The material auditor question is routed through [OI-018](../../controls/open-items.md#oi-018): **What maximum first-year cash exposure, recurring annual cash exposure, and comparison horizon should make Run or Subscribe unacceptable?** This can change the option recommendation; no ceiling is inferred.

[OI-017](../../controls/open-items.md#oi-017) carries proof-only needs: actual Run spend/resources/hours, 12-month pageview-plus-event usage with peaks, and a dated Enterprise quote with ISO currency, tax, entitlement, term, renewal, discount, support/SLA, and exit. No actual spend, payable currency, hosted price, tax, discount eligibility, staff cost, interruption value, or replacement cost is established.

## Reconciliation

Architecture's option/source boundary and Product Value's hosted-entitlement/journey limits are retained. Business Continuity and Cloud Security establish responsibility and interruption categories, not cash. CE's source-visible unlimited site/member limits do not establish capacity or zero operating cost. Public current prices [E-044](../../evidence/evidence-ledger.md#e-044) are post-cutoff validation and do not change cutoff state; dated plan/billing/terms evidence [E-045](../../evidence/evidence-ledger.md#e-045) supplies the cutoff-effective commercial rules. No material conflict was found. The single vendor/commercial collector completed once and was reconciled.

Exactly one independent artifact-quality worker returned `REVISE`. This single revision made Enterprise conditional on the intended one-team role/reporting model, exposed the separately billed multi-team unknown, and made Run cash categories explicitly conditional on effective configuration. No quality issue remains unresolved.

## Bounded Conclusion And Downstream Guidance

The evidence supports an expense shape, not an affordability verdict. Run has no Plausible subscription fee but retains broad and unpriced operating/failure exposure. Subscribe likely reduces technical operations, but the assumed site/member shape requires either a custom one-team Enterprise quote or an accepted separately billed multi-team design, and its quota depends on pageviews plus custom events and seasonal peaks. Replace is not currently priceable and should remain a future funded selection boundary.

Maintenance Cost should quantify recurring care categories in hours without inventing rates; Contributor and Vendor Value may evaluate what the hosted quote transfers. Scalability should supply monthly peak and event-volume scenarios. No downstream reviewer may treat public Business prices as the library price, displayed `$` as a known currency, source responsibility as actual spend, or absent replacement evidence as savings.
