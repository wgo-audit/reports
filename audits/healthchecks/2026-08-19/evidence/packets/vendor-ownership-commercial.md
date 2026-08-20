# Vendor Ownership And Commercial Evidence Packet

Use when: A reviewer needs the documented commercial bounds of the hosted option or the license/ownership facts relevant to pull and make.

## Scope And Evidence Boundary

- Reader question: What public facts establish the hosted service's current list price, billing/account lifecycle, standard commercial limitations, vendor concentration, and source-license rights?
- Evidence cutoff: 2026-08-19.
- Approved sources and actions: Read-only review of `https://healthchecks.io/pricing/`, `https://healthchecks.io/terms/`, `https://healthchecks.io/faq/`, `https://status.healthchecks.io/`, and pinned source `HC-CODE-001` commit `fafac59eeb00cfdc87166242544fa071ecad1723` (`README.md`, `LICENSE`).
- Exclusions and sensitivity: No account console, invoice, subscription, contract, support correspondence, private staffing record, or deployment was available. All observations are public or pinned public-source evidence.

## Observations

| Observation | Source type and exact locator | Observed/effective time | What it establishes | Limitation |
|---|---|---|---|---|
| Hosted list price and included limits | `https://healthchecks.io/pricing/` lines 27-57, 89-96, 129-132; E-036 | Observed 2026-08-19 | Business: $20/month or $192/year, 100 jobs, 1,000 log entries/job, 50 combined SMS/WhatsApp credits and 20 call credits monthly. Business Plus: $80/month or $768/year, 1,000 jobs, 1,000 log entries/job, 500 combined SMS/WhatsApp credits and 100 call credits monthly. The stated annual saving is 20%. | Public list price is not an Acme quote, tax-inclusive total, selected plan, credit-consumption forecast, or committed future price. |
| Subscription, fee-change, refund, and availability terms | `https://healthchecks.io/terms/` lines 6-20, 35-45; `https://healthchecks.io/pricing/` lines 67-79; E-036 | Observed 2026-08-19 | Standard subscription billing is recurring and monthly in advance; it automatically renews unless cancelled. Fee changes take effect after the current cycle with reasonable prior notice. Pricing says cancellation has no prorated refund except the documented wrong-account case. Terms allow suspension/termination and disclaim uninterrupted, secure, or available service. | This is standard public legal text, not a negotiated SLA, support commitment, refund agreement, or evidence of actual billing/termination. |
| Vendor and account-lifecycle statements | `https://healthchecks.io/faq/` lines 87-108, 134-153, 154-200; E-037 | Observed 2026-08-19 | The FAQ identifies SIA Monkey See Monkey Do as the service operator and describes it as a one-person company. It states multi-hour or multi-day outages are possible; ordering is self-service and the vendor will not complete vendor-management questionnaires. A payment failure past 60 days causes downgrade to Hobbyist; over-limit Hobbyist accounts can eventually be deleted after weekly owner-email notices. Accounts inactive for more than one year may be deleted after notice. | Vendor-authored facts do not prove staffing availability, operational performance, Acme billing ownership, notice receipt, account recovery, or negotiated protections. |
| Self-host eligibility and license | `HC-CODE-001:README.md:15-23`; `HC-CODE-001:LICENSE:1-12`; E-037 | Pinned commit effective 2026-08-19 | Healthchecks declares BSD-3-Clause licensing and hosted availability. The license permits redistribution and modification subject to notice/non-endorsement conditions. FAQ positions self-hosting as a possible choice for in-house compliance or custom features and says production-grade operation is ongoing work. | License permission is not a cost, deployment plan, security assessment, maintenance capacity, support entitlement, or proof that forked operation improves reliability. |
| Public status presence | `https://status.healthchecks.io/en/` | Observed 2026-08-19 | A public status page is available. | A current vendor-controlled status page is not historical availability, an SLA, an incident process, a recovery objective, or an independent assurance. |

## Material Unknowns And Access Limits

- Acme has not selected a hosted plan, confirmed job count growth, forecast notification-credit consumption, received a quote, or identified taxes/currency/payment controls.
- No agreement establishes Acme-specific availability, support response, recovery, incident notification, price protection, data export, termination assistance, or account-recovery terms.
- No source shows who will own the hosted account, monitor billing/owner email, maintain payment details, or execute a service exit.
- No production workload, topology, cloud account, deployment, or team-capability evidence permits self-host or fork cost calculation.

## Reuse Guidance

- Expense Exposure may use E-036 only as the dated hosted list-price and included-limit basis; retain the listed unknowns in any total-cost comparison.
- Business Continuity, Maintenance Cost, Revenue Risk, and Project Health may use E-037 for vendor concentration/account-lifecycle and license-rights context, but may not turn it into an availability guarantee or a staffing conclusion.
- Architecture and Security/Privacy may reuse E-037 to establish that pull/make are license-permitted; they must separately establish Acme's design, capacity, and controls.
- Do not use this packet as proof of actual payment, contract, account configuration, service history, SLA, or transition readiness.
