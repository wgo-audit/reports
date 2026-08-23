# Architecture

## Audit Question, Depth, And Evidence Boundary

Is Plausible Analytics' current technical boundary and its material decisions understood well enough for safe change? This detailed, read-only review is bounded to `primary-code` at commit `9cc669b97ece3ecd37fcb3950791cb3873d7944d`, relevant public GitHub issues/PRs/reviews/Actions/history, and approved Plausible pages through 2026-08-22 22:08:28 EDT. It excludes production/cloud access, internal repositories, private operations, customers, contracts, and live testing. Source implementation does not prove deployment, approval, ownership, capacity, or control effectiveness.

## Coverage And Material Gaps

`[Verified audit observation]` Coverage includes component/build boundaries, Phoenix routes and dashboard contracts, supervision/runtime wiring, tracker compilation, PostgreSQL/ClickHouse authority and migrations, ingestion/session persistence, jobs, deletion handoff, images/release workflows, and source-configured observability. CodeGraph 1.5.0 was synced at the approved absolute Git root and queried for supported JS/TS/config topology; it indexed 346 files but not Elixir, which was traced directly. The executable checks were read-only: `codegraph status`, `codegraph sync`, `codegraph files`, `codegraph query`, and `codegraph explore`; no dependencies were installed and no dependency-requiring tests were authorized or run.

Material gaps are live persistence/durability ([OI-001](../../controls/open-items.md#oi-001)), cross-store deletion convergence ([OI-002](../../controls/open-items.md#oi-002)), cloud promotion/migration/rollback ([OI-003](../../controls/open-items.md#oi-003)), configuration-matrix coverage ([OI-004](../../controls/open-items.md#oi-004)), and approved decision ownership ([OI-005](../../controls/open-items.md#oi-005)).

## Key Findings

| Finding | Severity | Effort | Evidence links | Confidence and limitation | Consequence | Taxonomy |
|---|---|---|---|---|---|---|
| `[Verified fact]` The Events API returns `202` after embedded in-process buffering rather than confirmed ClickHouse insertion; remote/relay backends and percentage routing add a material runtime boundary. `[Unknown]` The production backend, loss envelope, and SLO. | High | M | [E-002](../../evidence/evidence-ledger.md#e-002), [E-003](../../evidence/evidence-ledger.md#e-003), [ADR-003](../../controls/architecture/adr/ADR-003-asynchronous-pluggable-ingestion-persistence.md) | High for source; low for live frequency/impact. Issue #6382 and PR #6454 prove one crash/fix path, not current loss. | A wrong durability assumption can undercount customer analytics and misstate acceptance semantics. | none |
| `[Verified fact]` PostgreSQL deletion intent is cleared after asynchronous ClickHouse delete issuance, not source-visible completion. Public review changed a flawed date-authority design but retained residual/race limits. | High | M | [E-005](../../evidence/evidence-ledger.md#e-005), [ADR-007](../../controls/architecture/adr/ADR-007-postgresql-worklist-for-clickhouse-site-deletion.md), [view](../../controls/architecture/diagrams/deletion-consistency-path.md) | High for implementation/history; unknown for deployed reconciliation, mutation alerts, or residual rows. | Failed or incomplete cross-store deletion can create lifecycle, customer-trust, privacy, and storage consequences. | none |
| `[Verified fact]` Container publication is independent of CI; at the pinned commit merge-group checks succeeded, the master image build succeeded, and a separate push CI static job failed at dependency retrieval. `[Unknown]` Promotion, branch rules, migration, live digest, and rollback. | Medium | M | [E-007](../../evidence/evidence-ledger.md#e-007), [deployment view](../../controls/architecture/diagrams/deployment-and-runtime-path.md), [access limit](../../evidence/source-access-register.md) | High for public workflow/run metadata; no evidence that a bad image deployed. | Without the hidden gate, an incoming CTO cannot judge release safety or exercise stop/rollback authority. | none |
| `[Verified fact]` CE/cloud compile-time branches occur across 98 Elixir files and one tracker source compiles many integration/legacy variants; CI tests CE and cloud profiles and tracker workflows enforce size/release metadata. | Medium | M | [E-006](../../evidence/evidence-ledger.md#e-006), [E-011](../../evidence/evidence-ledger.md#e-011), [ADR-001](../../controls/architecture/adr/ADR-001-compile-time-ce-and-cloud-build-profiles.md), [ADR-005](../../controls/architecture/adr/ADR-005-single-source-multi-variant-tracker.md) | High for source; unknown for supported combinations, live usage, and historical regressions. | Cross-cutting changes can have edition- or integration-specific blast radius that a partial matrix misses. | none |
| `[Verified audit observation]` No whole-system approved ADR set was located in the reviewed public corpus; material rationale is distributed across code, one tracker guide, PRs, and unavailable internal links. `[Unknown]` A private approved set may exist. | Medium | M | [inventory](../../controls/architecture/adr-candidate-inventory.md), [register](../../controls/architecture/adr-register.md), [source-access boundary](../../evidence/source-access-register.md) | High for the bounded public search; deliberately no global absence claim. | A successor may mistake observed implementation for an approved/current decision and reverse a constraint without its operating context. | none |

## Mandate-Relevant Strengths

- `[Verified fact]` The main runtime boundary is source-legible: supervision, routes, repositories, job queues, and build profiles are explicit. [E-001](../../evidence/evidence-ledger.md#e-001) [E-009](../../evidence/evidence-ledger.md#e-009)
- `[Verified fact]` Data-store responsibilities and migration ordering are deliberate: read, ingest, async-insert, and deletion ClickHouse paths are separated, and the migrator documents cross-store ordering. [E-004](../../evidence/evidence-ledger.md#e-004)
- `[Verified fact]` Specific public review loops materially improved architecture changes: PR #6591 received changes requested over convergence/data authority and was revised; issue #6382 led to the scoped, tested PR #6454. This is change evidence, not an inference about individual performance. [E-002](../../evidence/evidence-ledger.md#e-002) [E-005](../../evidence/evidence-ledger.md#e-005)
- `[Verified fact]` Merge-group CI covers cloud and CE tests, E2E, and static checks; tracker changes have specialized version/size/changelog gates; third-party Actions are commit-pinned. [E-006](../../evidence/evidence-ledger.md#e-006) [E-007](../../evidence/evidence-ledger.md#e-007) [E-012](../../evidence/evidence-ledger.md#e-012)

### Decision Insights

- **Positive role signal and onboarding question:** The core analytics design is legible and deliberate. Request-to-durable-event and PostgreSQL-to-ClickHouse deletion convergence should be understood with the team through [OI-001](../../controls/open-items.md#oi-001) and [OI-002](../../controls/open-items.md#oi-002), but their private deployed evidence is not an offer condition or an adverse finding. The smallest onboarding check is deployed configuration, existing tests/telemetry, and reconciliation output.
- **First-30-day sequence:** The public repository ends at image publication, so broad architectural change should follow—not precede—commit-to-live provenance, migration/rollback proof, and branch/promotion authority under [OI-003](../../controls/open-items.md#oi-003). Otherwise a correct source change can still be unsafe operationally.
- **Change-budget condition:** One codebase is a clear strength, but CE/EE and tracker variants make configuration coverage a material dependency. Before a platform split or major refactor, close [OI-004](../../controls/open-items.md#oi-004) and validate the observed ADR baseline under [OI-005](../../controls/open-items.md#oi-005).

## Selected Outputs

- Required [ADR candidate inventory](../../controls/architecture/adr-candidate-inventory.md) and [ADR register](../../controls/architecture/adr-register.md).
- Seven material observed ADRs are linked from the register.
- Triggered [system component/data-flow](../../controls/architecture/diagrams/system-component-and-data-flow.md), [deployment/runtime](../../controls/architecture/diagrams/deployment-and-runtime-path.md), and [deletion consistency](../../controls/architecture/diagrams/deletion-consistency-path.md) views.
- No DevOps infrastructure view was created: its trigger requires approved live-environment evidence, which was not available.

## Material Omissions, Unknowns, And Auditor Questions

No auditor question is needed: the remaining material questions require proof, authority held by Plausible, or implementation action, not an assertion from the auditor. `Documented outside audited scope; not independently verified.` This applies to the separately referenced `plausible/community-edition` installation/upgrade corpus and `plausible/docs` workflow links; the auditor declined to expand scope. Internal Basecamp rationale linked from PR #6591 and the cloud deploy/infrastructure system are also unavailable, so they cannot establish approval or live state.

No dependency-requiring tests, image builds, migrations, load tests, or live checks were run because the audit is read-only and installation/external-service authorization was not given.

## Reconciliation

No predecessor or prior architecture report existed. Direct source and hosted history were reconciled. The important apparent conflicts are bounded: the public `202 Accepted` description does not mean ClickHouse durability and explicitly permits dropped events; the private-image workflow's “Deploying” notification does not prove deployment; source-configured monitoring does not prove operation. Public PR #6591 records disagreement over the deletion design, subsequent revision, and final approval; this report preserves both the improvement and remaining completion unknown rather than treating either as conclusive live assurance.

The single delegated artifact-quality review completed and identified ambiguous diagram edges and claim labelling. The selected artifacts were revised once to separate embedded from remote ingestion, decouple CI from image publication, separate deletion completion from reconciliation, add direct evidence navigation, and state the safe-change boundary.

Structural validation ran with Python 3.13.11 using `python3 plugins/wgo/skills/wgo/scripts/validate_audit_structure.py _whats-going-on-20260822` from the project root and returned `0 error(s), 0 warning(s)`. This validates structure, not conclusions or live behavior.

## Bounded Conclusion And Downstream Guidance

`[Verified audit conclusion]` Plausible's source architecture is understandable enough for targeted code navigation and risk-directed verification, but not yet for unconditional safe change of ingestion durability, deletion lifecycle, or cloud release boundaries. The source shows a coherent Phoenix/OTP monorepo, explicit store/workload specialization, deliberate tracker/release automation, and substantive review history. It also exposes three incoming-CTO conditions: quantify the event durability contract, prove cross-store deletion convergence, and reconstruct the live promotion/migration/rollback gate.

Code Quality, Product Value, and Security/Privacy should use the linked direct evidence and ADRs next. They must not assume source topology proves production configuration, customer behavior, live controls, ownership, approval, data correctness, or compliance.
