# Customer And Revenue Exposure Register

## Evidence Boundary

This register maps evidenced interruption and false-assurance mechanisms to
commercially relevant stages. It uses [E-051 through E-055](../../evidence/evidence-ledger.md),
the [capability matrix](../product/capability-contract-matrix.md), and the
[continuity path](../continuity/environment-and-service-continuity.md). No
contract, customer mapping, incident history, demo, renewal record, claim
inventory, or revenue amount was approved. Severity reflects potential harm to
Acme's mandate; probability and monetary exposure are unknown.

## Evidence Dimensions Used

| Dimension | Position |
|---|---|
| Implementation | Present for the pinned open-source product and selected failure mechanisms. |
| Observed operation | unknown for pull, make, and buy. |
| Customer/contract | unknown. |
| Ownership/approval | unknown except the CTO's five-minute, RTO, RPO, and planning decisions. |
| Cost/commercial | Public hosted list price and standard terms only; no Acme agreement. |

## Exposure Register

| Exposure | Stage affected | Applicable option(s) | Evidence-bounded mechanism | Potential consequence | Current mitigation/route | Stop condition |
|---|---|---|---|---|---|---|
| False green from heartbeat-only success | Customer delivery, renewal, trust | Pull / Make / Buy | A received success ping establishes a signal, not correct business output. | A failed customer-facing process may appear healthy and delay response. | Per-job business-outcome contract under OI-009; impact mapping under OI-021. | Do not call a critical job “protected” before both close. |
| Late, lost, or unacknowledged alert | Customer delivery, trust, incident response | Pull / Make / Buy | Grace, polling, queueing, sequential channels, retries, provider delivery, and human acknowledgement consume the five-minute budget; “Delivered” is not human receipt. | A responsible human may not act before operational impact expands. | T0/T1 fault test and independent route under OI-006. | No five-minute claim or production approval without passing evidence. |
| Misconfigured onboarding | Pilot, onboarding, customer delivery | Pull / Make / Buy | Each job needs correct schedule/timezone/grace, endpoint handling, outcome signaling, routes, and ownership; generic examples do not prove Acme configuration. | False alerts, silent gaps, or inconsistent coverage can reduce operator trust and adoption. | Critical-job contract/golden path under OI-009; capacity and inventory under OI-001/OI-014. | Do not scale onboarding from a generic template without per-job acceptance. |
| Monitoring-service interruption | Demo, customer delivery, trust | Pull / Make | Self-host operation requires supervised workers, durable state, recovery, and external monitoring; source does not prove them. | Healthchecks can fail at the same time it is expected to detect job failure. | OI-005..OI-008, independent OI-006 path, RTO 30 minutes/RPO 5 minutes. | Do not deploy the sample topology as the core control. |
| Hosted outage or vendor/account interruption | Demo, onboarding, renewal, customer delivery | Buy | Public terms disclaim availability; vendor says long outages are possible; billing/account events can reduce entitlement or eventually delete an over-limit account. | Monitoring visibility or alerting can stop without an Acme-controlled runtime fix. | OI-004, OI-012, OI-015, OI-016, plus independent alert and exit rehearsal. | Do not represent subscription purchase as continuity transfer or SLA. |
| Fork diversion and change risk | Roadmap delivery, customer delivery, trust | Make | No source-level gap currently justifies a fork; make adds permanent merge, security, release, and succession work. | Engineering opportunity time moves away from customer features while fork defects or lag can weaken the control. | Keep make stopped under OI-017 until a measured gap and stewardship charter exist. | No fork for deployment-only controls or unmeasured reassurance. |
| Sensitive payload or capability exposure | Trust, onboarding, customer delivery | Pull / Make / Buy | Ping URLs are bearer capabilities; request bodies and integrations can expose diagnostic/customer context. | Forged health, suppressed detection, or inappropriate data visibility can damage trust. | Data minimization and credential lifecycle under OI-004/OI-011. | No sensitive body by default; no critical shared/slug capability path. |
| Unsupported or stale claim | Demo, sales, onboarding, renewal, executive reporting | Pull / Make / Buy | Public product wording and UI status can be broader than demonstrated Acme outcomes. | A failed promise can amplify incident and renewal consequences even when the product behaved as implemented. | Evidence-tiered claim control under OI-020. | Withdraw or qualify a claim when evidence is absent, expired, or contradicted. |

## Option-Level Commercial Position

| Option | Revenue-risk strength | Material exposure retained | Current position |
|---|---|---|---|
| Pull | Acme retains source, deployment, data, and release timing; no fork delta. | Acme owns the entire service, notification, recovery, account, and claim chain. | Plausible only after operational proof; no customer-protection claim is currently supported. |
| Make | Same control as pull plus ability to change source. | Every pull exposure plus unbounded fork stewardship and feature opportunity cost. | No evidenced revenue-protection benefit justifies make today; keep stopped under OI-017. |
| Buy | Vendor operates the application and publishes a low list price/status view. | Acme still owns job correctness, account/billing, data minimization, alert receipt, independent protection, claims, and exit; no SLA is evidenced. | Commercially plausible only after vendor review and independent proof; purchase is not risk transfer. |

## Material Unknowns And Closure Routes

- Probability, affected customers, contractual consequence, support burden,
  renewal sensitivity, and revenue magnitude remain unknown under
  [OI-021](../open-items.md#OI-021).
- No golden-path demo was observed. If later authorized, use a non-production
  fixture and test success, explicit failure, missing completion, provider
  degradation, acknowledgement, and recovery without customer data.
- No option-level loss estimate is supportable from this evidence.
