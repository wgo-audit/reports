# Maintenance Cost

## Audit Question, Depth, And Evidence Boundary

This detailed review asks what skill mix, effort, operating burden, and change risk a small replacement team faces. It uses the four public repository snapshots/history, documentation catalog, Architecture/Code Quality/Business Continuity handoffs, and delivery/ownership packets through July 22, 2026. It does not estimate labor hours, staffing levels, or cash cost because no timed successor exercise, availability, rate, budget, or private operating evidence was approved.

## Coverage And Material Gaps

Coverage includes product code/build, link semantics, Cloudflare runtime/security, Terraform/domain, release/supply chain, website/docs, security/privacy, and operations/recovery. The stateless Worker and Git-backed configuration reduce maintenance burden. Four repositories, broad behavior/documentation, large orchestration modules, provider-specific controls, multilingual content, and unproved authority/recovery increase replacement burden. Exact time-to-safety is unknown until OI-004.

## Key Findings

| Finding | Evidence links | Confidence and limitation | Consequence |
|---|---|---|---|
| Core runtime maintenance is comparatively light: no application database/queue, no runtime npm dependencies, generated read-only data, and provider-managed execution. | [Architecture report](../architecture/report.md), [capacity envelope](../../controls/scalability/capacity-and-degradation.md) | High for topology; no live workload/cost evidence. | A successor avoids stateful platform engineering and can focus on source/configuration. |
| Safe maintenance still requires a wide skill mix spanning Node/Worker code, Git/release signing, Terraform, Cloudflare Access/WAF/DNS, domain custody, Hugo/toolchains, multilingual docs, and incident recovery. | [Time-to-safety map](../../controls/maintenance/time-to-safety.md), [continuity matrix](../../controls/continuity/continuity-and-transfer-matrix.md) | High for source surfaces; individual skill availability unknown. | One generalist may understand the code yet remain unable to operate the complete existing service safely. |
| Critical orchestration is concentrated in long Worker/build/setup/upgrade modules, with warning-only complexity budgets. | [Code Quality report](../code-quality/report.md), OI-009 | High for source/line counts; no executed warning baseline. | Successor changes carry elevated comprehension/review burden, best reduced incrementally rather than by rewrite. |
| Documentation breadth is a major burden reducer and a maintenance obligation: 97 records, 19 ADRs, bilingual/multilingual operations content, but inconsistent governance and weak hosted website quality. | [Documentation packet](../../evidence/packets/documentation-alignment.md), [Project Health report](../project-health/report.md) | High for catalog/source; actual usability unobserved. | Docs accelerate orientation only if build quality, cross-links, contacts, and cross-repository ownership stay current. |
| The largest unbounded burden lies outside code: account/state/secret discovery, domain renewal, release authority, alerts, incident roles, and recovery. | [Business Continuity report](../business-continuity/report.md), [vendor packet](../../evidence/packets/vendor-ownership-commercial.md) | High for public evidence gap; private arrangements unknown. | A replacement team’s time-to-safety cannot be estimated until authority and custody are inventoried. |

### Decision Insights

- **Plan successor readiness as gated cross-training, not a code handoff.** The product algorithm is not the dominant burden; GitHub/Cloudflare/domain/Terraform/release/response authority is. Smallest route: follow the gate order in the time-to-safety map.
- **Preserve the stateless architecture and invest in evidence.** Adding infrastructure would increase every missing handover dimension. The next value comes from OI-002/OI-004/OI-006/OI-012, not platform expansion.
- **Use incremental complexity ratchets and reproducible documentation checks.** These reduce replacement burden without destabilizing well-tested behavior. Smallest actions: OI-008/OI-009.

## Selected Outputs

The material successor-skill and operating-burden question triggered [successor time-to-safety map](../../controls/maintenance/time-to-safety.md). It deliberately provides gates rather than invented time estimates.

## Material Omissions, Unknowns, And Stakeholder Questions

- Non-creator elapsed time, assistance, failures, and skills for setup/change/release/deploy/recovery: OI-004.
- Current maintainer availability, willingness, role overlap, and succession timeline: not inferable from public source; OI-001/OI-002.
- Actual maintenance hours, vendor support, labor rates, and cash budget: unavailable; Expense Exposure owns cost fact.
- Live operational toil, alert volume, incidents, quota management, and renewal work: OI-006/OI-012.

## Reconciliation

Large modules are treated as maintenance burden, not defects, because the source ADR explicitly adopts warning-level incremental reduction and tests cover many critical behaviors. Broad documentation is treated as a burden reducer and ongoing obligation, not proof of low-touch onboarding. Low-state runtime simplicity is not extended to low-complexity account operations.

## Bounded Conclusion And Downstream Guidance

A replacement team can plausibly maintain and evolve an independent fork with moderate technical effort. Safely inheriting the existing canonical project and service requires a materially broader skill/authority set and cannot be timed from public evidence. Contributor/Vendor Value may use the skill and handoff map; Expense Exposure must not convert burden into cash without rate/time evidence; Revenue Risk may use the time-to-safety unknown. No reviewer may infer staffing inadequacy or individual performance.
