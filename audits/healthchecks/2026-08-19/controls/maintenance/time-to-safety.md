# Time To Safety And Maintenance Burden

Reader question: What opportunity-time work must Acme complete before each option is safe enough for a core service, and what work persists over 36 months?

## Evidence Boundary

This assessment uses the pinned source, cutoff-bounded Git history, upstream operator guidance, completed quality and continuity evidence, and Acme's 36-month/RTO/RPO decisions. It does not observe an Acme deployment, job inventory, staff capability, task duration, incident rate, selected hosted plan, or vendor internals. Evidence: [E-035](../../evidence/evidence-ledger.md#E-035), [E-039](../../evidence/evidence-ledger.md#E-039), [E-040](../../evidence/evidence-ledger.md#E-040), and [E-046 through E-050](../../evidence/evidence-ledger.md#E-046).

## Evidence Dimensions Used

Implementation, public change history, upstream operator guidance, hosted public declarations, and auditor-set objectives are present. Observed Acme operation, team capability, ownership approval, task timing, incident demand, and opportunity-cost conversion are **unknown**. Relative burden below is not hours, staffing, or cash.

## Time-To-Safety Path

| Gate | Pull | Make | Buy | Completion proof and route |
|---|---|---|---|---|
| Monitor contract and data boundary | Define each critical job's schedule, failure semantics, retry, payload, credential, responder, and Windows behavior where applicable. | Same as pull. | Same job-side work, plus minimized hosted payload/metadata contract. | OI-009 and OI-011 accepted. |
| Production boundary | Select resilient topology; harden TLS/proxy, identity, secrets, egress, database, retention, workers, and independent watchdog. | Same as pull; a fork does not replace deployment controls. | Complete vendor/security review, account/billing design, integration routing, and independent watchdog. | Pull/make: OI-005 and OI-010. Buy: OI-004 and OI-015. All: OI-012. |
| Outcome acceptance | Test `T1 - T0 <= 300 seconds` under worker/provider/backlog faults and capacity envelope. | Same as pull, including custom-diff behavior. | Equivalent Acme-controlled end-to-end tests plus vendor limits/commitments. | OI-006 and OI-014. |
| Recovery and exit | Restore database/objects/configuration, roll back a release, restart workers, and meet RTO 30 minutes/RPO 5 minutes while the independent alert path remains available. | Same as pull after every upstream merge/fork release; retain fork rebuild inputs. | Prove vendor recovery commitments, Acme export/reconstruction/cutover, and replacement path to the same targets. | OI-007, OI-013, and OI-016. |
| Safe change | Pin an upstream release/digest; review release/security/dependency changes; run upstream and Acme acceptance gates; promote or defer. | Perform every pull gate plus review/rebase/merge the fork diff, resolve conflicts, test compatibility, build/sign/publish, document, and support the fork. | Review service/terms/security changes; rerun job, notification, quota, account, and exit checks when the contract or behavior changes. | OI-008; make also requires OI-017. |

## 36-Month Relative Burden

| Option | Initial opportunity-time burden | Recurring and surge burden | Burden drivers | Bounded position |
|---|---|---|---|---|
| Pull | **High** | **Material; event-driven** | Production topology, hardening, job contracts, alert/recovery/capacity proof, then upstream release/security review, platform/database/TLS/backup/cleanup/watchdog operations and incidents. | Lowest source-ownership burden among self-hosted options. The sample stack shortens mechanics, not production acceptance. |
| Make | **High, no lower than pull** | **High; event-driven and fork-dependent** | Every pull duty plus custom design, upstream merge/conflict resolution, regression, documentation, security patching, artifact release, and successor-maintainer work. | Burden cannot be bounded until a necessary source change and narrow fork charter exist. Make is stopped by OI-017. |
| Buy | **Material** | **Lower runtime/source burden, but not zero** | Security/vendor review, data minimization, job integration, notification routes, account/billing, independent watchdog, service-change review, recovery/exit evidence, and incidents/escalations. | Avoids Acme application/database/runtime patching, but public material does not prove support, recovery, or exit performance. |

## Test Of Preliminary Estimates

| Intake claim | Result | Why | Responsible replacement |
|---|---|---|---|
| 2-5 working days initial setup | **Not validated as production-safe setup.** It may be compatible with starting the sample under favorable prerequisites, but no task-duration evidence exists. | The window has no allowance or proof for selected topology, hardening, approximately 100 job contracts, end-to-end fault/capacity tests, recovery/rollback to the approved objectives, account succession, or acceptance. | Measure a production-shaped pilot by activity and retain elapsed/active opportunity time under OI-018. |
| 4-8 hours/month ongoing operations | **Not validated as a planning baseline.** | Maintenance is event-driven: 26 upstream tags and material dependency/deployment churn occurred in the prior 36 months, while security patches, incidents, restores, certificates, credentials, provider quotas, capacity and successor drills are not monthly constants. Make adds an unbounded fork stream. | Record routine and surge time separately across at least one release/vendor-change cycle and the required exercises; plan a range plus surge reserve under OI-018/OI-019. |

No responsible hour, FTE, or monetized total can be derived from the approved evidence. Engineering time remains opportunity cost, and Acme application-architecture-change effort is excluded from pull/make as directed; deployment, hardening, integration, testing, recovery, upgrades, and operations remain included.

## Material Unknowns And Closure Routes

The selected topology/plan, exact job contracts, automation, update policy, release uptake, incident frequency, staff coverage, and measured task times are unknown. OI-018 owns effort measurement; OI-019 owns the operating model; OI-002 and OI-016 own accountable skill/successor coverage. Until those close, use the relative bands only.
