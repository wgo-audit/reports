# Scalability

## Audit Question, Depth, And Evidence Boundary

This detailed review asks whether Healthchecks supports Acme's slightly-below-100 monitored jobs and reasonable growth across ingress, overlap, data, notification queues, providers, degradation, and resource footprint. The cutoff is 2026-08-19. Evidence is bounded to `HC-CODE-001` commit `fafac59eeb00cfdc87166242544fa071ecad1723`, approved repository/public GitHub evidence, public Healthchecks.io material, and the approved workload statement. Primary evidence is [E-031 through E-035](../../evidence/evidence-ledger.md), with directly linked predecessor evidence used for architecture/product semantics.

No approved evidence establishes Acme cadence, bursts, body sizes, retention, data volumes, topology, workers, replicas, provider quotas, runtime metrics, or load results. Source and operator anecdotes are not production capacity proof.

## Coverage And Material Gaps

The review traced request/body handling, same-check concurrency, database writes/indexes, count retention, relational/object pruning, uWSGI/worker settings, due-check/flip processing, notification concurrency, provider retries, metrics/health, hosted tiers, and public operator reports. OI-006 remains the five-minute/no-silent-loss route; OI-007 owns cleanup/recovery; OI-010/OI-011 own ingress hardening/payload minimization; [OI-014](../../controls/open-items.md) owns production-shaped capacity proof.

The approved source has no capacity guide or benchmark. No live collector ran because no runtime, quota, replica, database-volume, provider, or metric evidence exists. No code collector was needed: the narrow workload path was inspected directly.

### Executed Checks

| Working directory | Command/tool | Intended coverage | Result | Dependency/installation state | Bounded conclusion |
|---|---|---|---|---|---|
| `HC-CODE-001:./` | `git rev-parse HEAD`; `git show -s --format=... HEAD` | Verify source identity/time | Pass: pinned SHA and 2026-08-19 time matched | Existing Git; no install | Findings are commit-bounded. |
| `HC-CODE-001:./` | `codegraph status <absolute-root>`; CodeGraph 1.5.0 | Index coverage/freshness | Pass: 701 files, 7,177 nodes, 19,074 edges; up to date | Existing index; no install | Navigation coverage is broad; not throughput proof. |
| `HC-CODE-001:./` | `codegraph query --path <absolute-root> 'Check.ping' --limit 10`; same for `sendalerts` | Locate ingress/alert symbols and tests | Pass: implementation/test files returned | Existing index; no install | Paths were traceable; not execution. |
| `HC-CODE-001` GitHub repository | Read-only `gh api` search and issue/comment reads for #1023/#1186 | Public operator evidence | Pass: timestamped issue evidence retrieved | Existing read-only access | Reports define sensitivities/tests, not capacity. |
| `HC-CODE-001:./` | Product tests/load commands | Runtime throughput/storage/queue/five-minute behavior | Not run: deployment/load/install/mutation outside scope | No dependencies/environment authorized | 0 passed, 0 failed, 0 errors, 0 skipped; runner not started. |
| Audit root | `python3 core:scripts/validate_audit_structure.py <audit-root>` | Canonical audit structure and reviewer handoff contract | Pass: 0 errors, 0 warnings | Existing Python; no installation | Scalability artifacts satisfy the structural validator; conclusions remain evidence-bounded. |

## Key Findings

| Finding | Severity | Effort | Evidence links | Confidence and limitation | Consequence | Taxonomy |
|---|---|---|---|---|---|---|
| No approved production capacity envelope exists; intake 1-2 vCPU, 1-2 GB RAM, and 10-20 GB SSD figures lack workload, benchmark, topology, or storage evidence. | High | L | [E-035](../../evidence/evidence-ledger.md), [capacity envelope](../../controls/scalability/capacity-envelope.md), [OI-014](../../controls/open-items.md) | High that claims are unsupported; actual need can be lower/higher | Sizing/costing a critical option from them can create an under-sized failure point or unnecessary spend. | none |
| A synchronized missed-job burst or due-check calculation fault has no proven T0-to-T1 margin: due checks are discovered one at a time; a calculation exception defers the affected check for one hour; delivery defaults to `W=1`; channels within a flip are sequential; generic HTTP permits three attempts with a 30-second timeout each; processed marking precedes delivery; and the container probe does not test alert-worker liveness. | High | L | [E-033](../../evidence/evidence-ledger.md), [bottleneck view](../../controls/scalability/bottleneck-and-degradation-view.md), [OI-006](../../controls/open-items.md) | High for source behavior; Acme burst, channels, provider behavior, worker count, supervision, and independent path are unknown | The one-hour deferral exceeds 300 seconds by construction; with `W=1`, four fully timing-out generic-HTTP deliveries consume 360 seconds of request-timeout budget before due-scan, queue, retry overhead, and human routing. This is stress-case arithmetic, not measured throughput. | none |
| Every ping writes relational state and serializes same-check overlaps; no source ping limiter was found, and 100 kB retention requires a larger limit while bodies are read before truncation. | Medium | M | [E-031](../../evidence/evidence-ledger.md#E-031), [capacity envelope](../../controls/scalability/capacity-envelope.md) | High for source; edge, overlap, bodies, DB capacity unknown | Burst, abuse, or overlap can consume web/database capacity and delay signals. | CWE-400 |
| Retention is count-bounded for healthy active checks but prunes on every 100th ping; object storage makes upload synchronous, starts pruning threads, and needs separate orphan cleanup. Flips remain at least 93 days. | Medium | M | [E-032](../../evidence/evidence-ledger.md#E-032), [capacity envelope](../../controls/scalability/capacity-envelope.md), [OI-007](../../controls/open-items.md#OI-007) | High for mechanism; cleanup, payloads, objects, dead tuples/backups unknown | Larger history/bodies or failed cleanup can increase latency, storage, backup time, and recovery cost. | none |
| Hosted 100-check tier is close to Acme's current count; public evidence does not establish hosted throughput, queue margin, provider quotas, or commitments. | Medium | S | [E-030](../../evidence/evidence-ledger.md#E-030), [OI-004](../../controls/open-items.md#OI-004) | High for plan boundary; internals/growth unknown | Growth can force an early tier change; buy still needs five-minute capacity/degradation proof. | none |

## Mandate-Relevant Strengths

- Per-check transactional locking, indexed due-check state, a partial unprocessed-flip index, and per-check flip-history index are deliberate controls, though not capacity proof ([E-031](../../evidence/evidence-ledger.md), [E-032](../../evidence/evidence-ledger.md)).
- Count-based ping retention and at-least-93-day flip history are explicit growth levers. Default retention makes sub-100-check row counts modest in successful-prune arithmetic; row size and throughput remain unmeasured.
- Web-process count, alert-worker count, and object storage are configurable without a fork ([E-031](../../evidence/evidence-ledger.md), [E-032](../../evidence/evidence-ledger.md), [E-033](../../evidence/evidence-ledger.md)); this supports testing pull before considering make.
- Unprocessed-flip count and dwell/send/provider metrics plus an S3 read circuit are useful target-control inputs, not evidence of operation ([E-033](../../evidence/evidence-ledger.md)).

### Decision Insights

1. **Job count does not decide pull sizing.** Cadence, bursts, bodies, retention, database, and fan-out can change work by orders of magnitude. Close OI-001, select OI-005 topology, then run OI-014 and OI-006 together.
2. **Capacity evidence does not justify make.** Material controls are configurable around upstream. Fork only if production-shaped proof isolates a source limit operational controls cannot close.
3. **Buy changes rather than removes the envelope.** Acme is close to the 100-check boundary and hosted internals are opaque. Price 1,000 checks and close OI-004/OI-014 with vendor limits plus Acme burst/T0-T1 evidence.

## Selected Outputs

- Triggered: [capacity envelope](../../controls/scalability/capacity-envelope.md)
- Triggered: [bottleneck and degradation view](../../controls/scalability/bottleneck-and-degradation-view.md)

Both were triggered by material request, retention, object-store, queue, provider, and hosted-tier boundaries. They show unknown live boundaries rather than treating defaults as deployment.

## Material Omissions, Unknowns, And Auditor Questions

No Scalability question is raised. The gaps require inventory/measured proof, not assertion. OI-014 owns capacity; OI-006 five-minute faults; OI-004 hosted internals; OI-005 topology; OI-007 cleanup/recovery; OI-010/OI-011 edge/body controls.

Unknowns are schedules/event multiplicity, alignment/growth, payloads, retention, data-store engine/volume, resource headroom, worker/channels, provider quotas, metrics/alarms, and hosted capacity. The source has no sizing guide. These limits prevent validation of the intake estimates.

E-034 contributes two staging-case inputs—simultaneous ping spam and aged multi-million-row query plans—but establishes neither an Acme threshold nor a current pinned-source defect.

**Documented outside audited scope; not independently verified.** Provider quotas, Acme producers/infrastructure/telemetry, and vendor capacity plans are outside approved live evidence. The smallest expansion is OI-001, OI-004, and OI-014.

## Reconciliation

Fresh audit; no prior Scalability item to retain/supersede. Predecessor handoffs were navigation; direct evidence was checked. No material conflict was found. Current source has query/index optimizations while public reports used different versions, engines, hardware, data, and settings; issue 1186 closed without confirmed cause. Reports define verification cases, not defects/capacity.

No card collector started because direct inspection covered the narrow source and no live environment existed. The single required quality worker's initial invocation completed blocked because it inherited a nonexistent working directory; the coordinator reactivated that same canonical worker with explicit working directory `/`. The retry completed read-only, returned a `REVISE` outcome, and this single revision corrected alert-fault coverage, flow sequencing, conditional arithmetic, links, evidence bounds, and effort. No other child task started; both starts have one terminal outcome and no child remains active.

## Bounded Conclusion And Downstream Guidance

The source has sensible retention, indexing, concurrency, worker, metric, and object-storage mechanisms, but no CPU, RAM, storage, request-rate, burst, or five-minute envelope. Fewer than 100 jobs is plausibly modest only as a count; schedules, overlap, bodies, retention, failure alignment, and channels decide load. The 1-2 vCPU, 1-2 GB RAM, and 10-20 GB estimates remain unsupported.

Pull is the simplest self-host capacity hypothesis to test. Make lacks scalability justification. Buy avoids Acme sizing internals but needs hosted limits/commitments, tier planning, and the same end-to-end proof. Expense Exposure should price tier/topology/testing; Maintenance Cost should include capacity review. Neither may assume capacity fit, live metrics, provider margin, or headroom from missing evidence.
