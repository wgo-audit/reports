# Revenue Exposure Register

Coordinator mapping: local RR-OI-002 is serialized as canonical OI-024. Local labels remain below for traceability to the reviewer draft.

## Boundary And Use

This register translates evidenced product, continuity, scalability, and commercial dependencies into testable business scenarios. It does not estimate loss, probability, customer reaction, contract breach, conversion, renewal, or revenue. All quantities are deliberately unpopulated until named authorities approve them under OI-017 and proposed RR-OI-002.

## Unpopulated Variables And Formulas

| Symbol | Required approved input | Formula or test | Interpretation and limit |
|---|---|---|---|
| `M` | Eligible customer-visible service minutes in the applicable measured calendar month after authority-approved exclusions | Signing unavailability allowance = `0.005 × M`; onboarding unavailability allowance = `0.01 × M` | Target allowance only. OI-014 must define measurement points, exclusions, partial failure, and retained evidence. |
| `U_sign`, `U_onboard` | Approved equivalent/countable customer-visible unavailable minutes by indicator | Signing excess = `max(0, U_sign - 0.005M)`; onboarding excess = `max(0, U_onboard - 0.01M)` | Degraded or partial minutes count only under OI-014's approved weighting/counting rules. Does not assign customer impact, service credits, breach, or money. |
| `I` | Interruption/pause duration in an approved low/base/high scenario | Measure separately from recovery and catch-up | Permission to pause onboarding does not prove target compliance or eliminate backlog. |
| `λ_i` | Approved onboarding arrival rate for scenario `i`, expressed in the same time unit as `I` and `μ_i` | Initial waiting work under a full pause: `B_i = λ_i × I`, only if arrivals are constant during `I`, every arrival waits, and none is withdrawn | Replace constant-rate/no-withdrawal assumptions with observed or authority-approved behavior where available; this is not a forecast. |
| `μ_i` | Demonstrated constant safe catch-up completion rate for scenario `i` after normal demand resumes, in the same time unit as `λ_i` | `T_catch,i = B_i / (μ_i - λ_i)` only when `μ_i > λ_i` | If rates vary, use interval-specific measurement rather than this simple formula. If `μ_i ≤ λ_i`, backlog does not clear under the constant-rate model. Queue, artifact, provider, and downstream readiness must all be included. |
| `L_evidence` | Time from relational completion to accepted evidence-package and downstream readiness | Compare percentile/max values to approved onboarding readiness SLO | `completed_at` alone is not the measured endpoint. No latency evidence exists. |
| `N_reconcile` | Count of committed transactions with missing, duplicate, stale, or unaccepted downstream effects after interruption | Count by SQL/blob/key/queue/artifact/mail/webhook/consumer category | A scenario oracle, not evidence that such outcomes occurred. |
| `R_delayed` | Authority-approved value measure for each delayed onboarding, if the organization elects to monetize delay | `R_delayed = Σ approved_value(j)` over the approved delayed population | Remains unpopulated. Do not substitute list price, average revenue, probability, or customer count without approved evidence. |
| `C_claim` | Authority-defined count/severity of unsupported or expired claims | Count by audience, claim, duration, affected decision/customer, and correction | Does not assert legal liability, regulatory breach, churn, or monetary loss. |

## Scenario Register

| Scenario | Evidenced trigger/dependency | What must be measured | Decision/stop condition | Existing route |
|---|---|---|---|---|
| S1 — signing path interruption | Rails/SQL/Redis/blob/provider/ingress dependency; 99.5% monthly target | `U_sign`, accepted in-flight state, safe pause, recovery, artifacts | Production gate remains closed until target measurement and recovery proof exist | OI-003/OI-014 |
| S2 — onboarding pause and catch-up | Auditor permits all new onboarding to pause; 99% monthly target | `I`, `λ_i`, `B_i`, `μ_i`, `T_catch,i`, backlog age and withdrawals | Scenario fails when backlog cannot safely clear within authority-approved objective or downstream state cannot reconcile | OI-014/OI-017/RR-OI-002 |
| S3 — accepted signer completion but incomplete evidence/delivery | SQL commit precedes artifact/mail/webhook work | `L_evidence`, missing/duplicate artifacts/events, `N_reconcile` | Do not activate customer/revenue state until OI-009 readiness oracle passes | OI-003/OI-005/OI-009 |
| S4 — maximum-RPO recovery and readiness | SQL/blob/key/queue form one recovery set; two-hour RPO | aligned restore points, accepted transaction loss window, artifact/trust integrity, downstream repair | RPO fails only if accepted data loss exceeds two hours. Independently, evidence/onboarding readiness remains closed until accepted artifacts can be reconstructed and downstream state reconciled. | OI-003/OI-006 |
| S5 — web/mobile Pro or contract mismatch | Required path crosses API/embed/identity/edition boundaries | entitlement/version/package mismatch, redesign lead time, blocked onboarding count | No integration commitment until release-specific contract and target-client proof | OI-001/OI-005/OI-020 |
| S6 — commercial/billing/support event | Public prices/terms are dynamic; owner and operative agreement unknown | affected entitlement/service, notification, grace/transition, escalation, duration | No vendor kill switch assumed; commercial approval remains closed without terms and owner | OI-019/OI-020/OI-013 |
| S7 — unsupported assurance claim | Public legal/compliance/KYC/verification language exceeds current Community proof | `C_claim`, evidence expiry, audience, correction and authority response | Stop external use until RR-OI-001 gates pass | RR-OI-001 |
| S8 — vendor, account, or maintainer transfer | Source, registry, keys, providers and support routes require successors | time to regain control, preserved artifacts/keys, deployment/recovery and escalation success | Production gate remains closed without tested primary/backup control | OI-015/OI-016 |

## Proposed Material Open Item

| Placeholder | Type / priority | Item and consequence | Proposed owner | Closure route |
|---|---|---|---|---|
| RR-OI-002 | verification / P1 | Populate and exercise the revenue-exposure scenarios using the approved low/base/high workload/SLO envelope, including pause duration, customer-visible availability, evidence-readiness lag, backlog/catch-up, reconciliation cases, and any authority-approved value measure. Without this proof, the organization cannot bound how a technical or commercial interruption affects onboarding decisions. | Product Manager, IT Operations Director, VP Software Engineering, with finance/commercial authority for any monetary input | Consume OI-017's approved envelope; define measurement rules with OI-014 and readiness under OI-009; run controlled failure/recovery/catch-up tests; retain inputs, formulas, outcomes, and stop decisions. |

RR-OI-002 does not duplicate capacity proof: OI-017 defines demand/SLO inputs and OI-003 proves system capacity/recovery. This item owns the business-consequence interpretation and any approved value mapping.
