# Architecture

## Audit Question, Depth, And Evidence Boundary

This detailed review asks whether Healthchecks' components, contracts, data,
jobs, dependencies, runtime boundaries, and material technical decisions are
understood well enough for safe change and for Acme's pull/make/buy decision.
The cutoff is 2026-08-19. Evidence is bounded to `HC-CODE-001` commit
`fafac59eeb00cfdc87166242544fa071ecad1723`, its repository documentation and
configuration, local Git metadata available in the shallow clone, and the
auditor-approved business boundary. Reusable evidence is [E-001 through E-008](../../evidence/evidence-ledger.md).

No Acme environment, job producer, database, object store, alert provider,
staffing, ownership, security standard, or hosted-service runtime was observed.
Source structure is not treated as live state, approval, ownership, capacity,
or proof of the five-minute outcome.

## Coverage And Material Gaps

The review traced HTTP/SMTP ingestion, schedule and grace calculation, database
state transitions, alert claiming and notification delivery, UI/API composition,
versioned contracts, integration dispatch, relational/object persistence,
retention, migrations, image build, Compose, and uWSGI runtime wiring.

Material gaps are routed as follows:

- Acme producer schedules, payloads, and alert ownership: [OI-001](../../controls/open-items.md#OI-001).
- Hosted internals and Acme security requirements: [OI-004](../../controls/open-items.md#OI-004).
- Self-host production topology and failure domains: [OI-005](../../controls/open-items.md#OI-005).
- End-to-end five-minute measurement and fault proof: [OI-006](../../controls/open-items.md#OI-006).
- Self-host backup, restore, rollback, and recurring maintenance: [OI-007](../../controls/open-items.md#OI-007).

Repository-linked GitHub issue `#1207` and discussion `#851` were attempted
through approved read-only access but were not retrieved because the available
browser returned no content and the CLI lacked network access. Their details
were not used, and no material conclusion depends on them.

### Executed Checks

| Working directory | Command/tool | Intended coverage | Result | Dependency/installation state | Bounded conclusion |
|---|---|---|---|---|---|
| `HC-CODE-001:./` | `codegraph status <absolute-root>`; CodeGraph 1.5.0 | Index freshness and topology scope | Pass: up to date; 701 files, 7,177 nodes, 19,074 edges; 653 Python, 42 JavaScript, 6 YAML | Existing index; no installation | The pinned source was broadly indexed; this does not prove behavior. |
| `HC-CODE-001:./` | CodeGraph `query`, `explore`, `node`, and `impact` with `--path <absolute-root>` | Trace ping ingestion, `Check.ping`, alert worker, callers, and affected symbols | Pass: relevant source/call trails returned; `Check.ping` impact reported 31 symbols | Existing index; no installation | The central database-mediated path and change surface were traceable. |
| `HC-CODE-001:./` | `git rev-parse HEAD` and commit metadata | Verify source identity and effective time | Pass: exact pinned SHA; commit timestamp 2026-08-19 15:12:46 +03:00 | Git available; clone history shallow | Findings are commit-bounded; historical rationale is limited. |
| `HC-CODE-001:./` | `python3 -c 'import django; ...'`; Python 3.14.6 | Determine whether source tests could run without changing dependencies | Error: `ModuleNotFoundError: django` | Dependencies absent; installation not authorized | No dependency-backed tests were run. Test runner totals: 0 passed, 0 failed, 0 errors, 0 skipped; execution was not started. Source tests were inspected only. |
| Audit root | `python3 core:scripts/validate_audit_structure.py <audit-root>` | Validate canonical audit structure and required handoff sections | Pass after fixing four missing handoff headings: 0 errors, 0 warnings | Existing Python; no installation | Architecture artifacts satisfy the structural validator; conclusions remain evidence-bounded. |

## Key Findings

| Finding | Severity | Effort | Evidence links | Confidence and limitation | Consequence | Taxonomy |
|---|---|---|---|---|---|---|
| The supplied Compose topology is explicitly one database and one web service on one host; uWSGI couples web serving with the alert/report daemons and startup migrations. It is a reference setup, not a production resilience design. | High | M | [E-004](../../evidence/evidence-ledger.md#E-004), [ADR-002](../../controls/architecture/adr/ADR-002-reference-container-process-coupling.md) | High for repository configuration; no Acme deployment evidence | Using it unchanged would put ingestion, alerting, and state into shared failure domains and cannot support a responsible pull decision. | none |
| Alert work is claimed by setting `Flip.processed` before asynchronous delivery; one worker is the default, a flip's channels are sequential, and an HTTP channel may take three 30-second attempts. The reviewed source records failure but does not durably redeliver the flip. | High | M | [E-003](../../evidence/evidence-ledger.md#E-003), [ADR-001](../../controls/architecture/adr/ADR-001-database-mediated-alert-state.md) | High for source semantics; live configuration, latency, and provider behavior unknown | A worker crash, provider degradation, or failure burst can silently lose or delay the only actionable alert beyond five minutes. | none |
| Upstream requires `sendalerts` to remain running and tells operators to independently monitor ping acceptance and alert sending, but no such independent control exists in the supplied topology. | High | M | [E-007](../../evidence/evidence-ledger.md#E-007), [alert-path diagram](../../controls/architecture/diagrams/heartbeat-to-human-alert-path.md) | High for guidance and sample absence; Acme controls unknown | The monitoring system can share the same blind spot as the jobs it is meant to protect. | none |
| Container startup applies migrations before serving; migration history includes transformations/deletions, while the approved evidence contains no tested backup, restore, or rollback design. | High | M | [E-008](../../evidence/evidence-ledger.md#E-008), [OI-007](../../controls/open-items.md#OI-007) | High for source; production data and recovery state unknown | A failed upgrade or damaged state can stop monitoring and make recovery duration unbounded. | none |
| Optional external body storage creates a second persistence and recovery boundary; uploads occur after the database transaction and disabling storage does not migrate existing objects back. | Medium | M | [E-005](../../evidence/evidence-ledger.md#E-005), [ADR-003](../../controls/architecture/adr/ADR-003-relational-state-and-optional-object-bodies.md) | High for implementation; actual payload and storage use unknown | Payload history can be unavailable or inconsistently recovered, and unnecessary payload capture increases operational/security burden. | none |
| Three management API versions share handlers and domain serializers; ping ingestion is a separate identifier-bearing contract and can auto-provision by slug. | Medium | M | [E-006](../../evidence/evidence-ledger.md#E-006), [component diagram](../../controls/architecture/diagrams/component-and-contract-topology.md) | High for source; Acme consumer use unknown | A fork or upstream upgrade can affect several client contracts and default monitor configuration without a machine-readable contract baseline. | none |

## Mandate-Relevant Strengths

- Ping state changes and ping creation are wrapped in one transaction with row
  locking; alert scheduling and unprocessed flips have dedicated indexes. This
  reduces obvious concurrent-update and scan ambiguity in the source path
  ([E-002](../../evidence/evidence-ledger.md#E-002), [E-003](../../evidence/evidence-ledger.md#E-003)).
- Alert state is durable in relational records rather than only process memory,
  and conditional claims support more than one `sendalerts` process. This gives
  a production design a source-supported base for supervised worker separation;
  it does not itself prove high availability.
- The project documents the need for worker supervision, database backup, TLS,
  and independent monitoring instead of presenting the sample as production-
  complete ([E-007](../../evidence/evidence-ledger.md#E-007)).
- Versioned management APIs, project-scoped keys, configurable production
  databases, optional object storage, and many notification adapters provide
  explicit integration seams ([E-005](../../evidence/evidence-ledger.md#E-005),
  [E-006](../../evidence/evidence-ledger.md#E-006)).

### Decision Insights

1. **Pull does not mean deploy the sample Compose file unchanged.** The source
   and the production topology are separable: managed database, supervised
   workers, reverse proxy/TLS, recovery, and an independent watchdog can be
   added without a product fork. Choosing make to solve these deployment gaps
   would create avoidable merge and ownership burden. Smallest next action:
   close OI-005 and OI-007 with a no-fork target design, then test OI-006.
2. **Make has a defensible architecture trigger, not a default benefit.** The
   source-level delivery semantics may violate Acme's five-minute/no-silent-loss
   requirement, but only end-to-end fault evidence can show whether operational
   controls and channel redundancy are insufficient. A wrong early fork adds
   permanent upgrade work; a wrong refusal to fork can lose alerts. Smallest
   proof: run OI-006's T0/T1 contract and propose durable redelivery only if it
   fails for source-level reasons.
3. **Buy cannot inherit conclusions about the public repository's runtime.**
   Hosted Healthchecks.io may use different topology and controls; public source
   neither proves nor disproves them. The consequence of assuming equivalence is
   an unverified core dependency. Smallest proof: OI-004 plus equivalent T0/T1
   evidence or an Acme-controlled end-to-end hosted test.

## Selected Outputs

- Required: [ADR candidate inventory](../../controls/architecture/adr-candidate-inventory.md)
- Required: [ADR register](../../controls/architecture/adr-register.md)
- Triggered: [ADR-001](../../controls/architecture/adr/ADR-001-database-mediated-alert-state.md), [ADR-002](../../controls/architecture/adr/ADR-002-reference-container-process-coupling.md), and [ADR-003](../../controls/architecture/adr/ADR-003-relational-state-and-optional-object-bodies.md)
- Triggered: [component and contract topology](../../controls/architecture/diagrams/component-and-contract-topology.md), [heartbeat-to-human alert path](../../controls/architecture/diagrams/heartbeat-to-human-alert-path.md), and [deployment and runtime path](../../controls/architecture/diagrams/deployment-and-runtime-path.md)

The DevOps infrastructure view was not triggered because no approved live-
environment evidence exists. The deployment/runtime diagram shows that boundary
as unknown rather than substituting the sample configuration for live state.

## Material Omissions, Unknowns, And Auditor Questions

No Architecture question is raised to the auditor. The unresolved matters are
proof or authority needs, not questions that the auditor can answer by assertion:
OI-005 requires a target architecture decision, OI-006 requires measured fault
evidence, and OI-007 requires implemented/rehearsed recovery. OI-001 and OI-004
remain prerequisite evidence for job fit and buy. Team capability remains
unknown and was not judged.

**Documented outside audited scope; not independently verified.** External job
producers and any configured object store are referenced by source interfaces,
but their existence, correctness, contents, retention, and recovery are not
proved. The smallest expansion is the already-routed OI-001 job inventory and,
if object storage is selected, read-only configuration/inventory and restore
evidence under OI-007.

## Reconciliation

This is a fresh audit with no prior Architecture findings, decisions, or open
items to retain or supersede. No material conflict was found between source,
configuration, and repository documentation. Where documentation describes a
production responsibility absent from the sample topology, the report treats
that as an explicit operator boundary, not a contradiction.

Two evidence collectors completed with one terminal outcome each:
`component_topology` completed and `data_jobs` completed. Runtime/deployment was
reviewed directly because the available concurrent task slots were exhausted;
no runtime collector was started. The required `architecture_quality` worker
completed once, wrote no state, and its feedback was reconciled in one revision
pass. No child task remains running or ambiguously terminated.

During artifact writing, the managed writable root pointed to a nonexistent
path. The reviewer created an unauthorized compatibility symlink outside the
audit root; the coordinator removed it immediately and verified the audit files
intact. Subsequent writes used the actual project path and the coordinator-
specified patch executable with narrow escalation. The symlink did not alter
product source or audit content beyond the intended E-001..E-008 and OI-005..007
writes inside the approved audit root.

## Bounded Conclusion And Downstream Guidance

The pinned source provides an understandable, coherent database-mediated
monitoring architecture, but neither the bundled Docker topology nor the alert
delivery semantics establish Acme's five-minute/no-silent-loss requirement.
Pull remains architecturally plausible only with a production topology,
independent watchdog, recovery controls, and successful T0/T1 fault evidence.
Make is not justified yet; its trigger is measured proof that source-level
delivery semantics remain inadequate after operational controls. Buy remains
architecturally unproven pending hosted evidence under the same measurement
contract.

Code Quality, Product Value, and Security and Privacy should use the linked
direct evidence and ADR boundaries next. They must not assume the sample is
deployed, source tests were executed, Acme has required skills, hosted internals
match public source, or any option currently meets five minutes.
