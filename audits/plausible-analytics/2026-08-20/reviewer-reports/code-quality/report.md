# Code Quality

## Audit Question, Depth, And Evidence Boundary

This detailed review asks which code-level test, defect, and change-safety risks materially affect correctness, maintainability, and the Run/Subscribe/Replace decision. The cutoff is 2026-08-20 at onboarding start, America/Toronto. Evidence is the approved `primary-code` snapshot at commit `9cc669b97ece3ecd37fcb3950791cb3873d7944d`, public GitHub Actions/ruleset evidence effective by the cutoff, Architecture's linked source evidence, and narrow post-cutoff validation against the same snapshot. No dependency was installed or restored; no local product suite, migration, container, browser, load test, deployment, live traffic, private system, hosted runtime, or replacement code was inspected.

## Coverage And Material Gaps

The review inventoried Elixir/CE tests, application and tracker Playwright, Jest, type/lint/format/static analysis, generated-contract drift, migration isolation, aggregate merge control, image/package release automation, and supporting gates. It inspected critical tracker-ingestion-dashboard, migration, and fixture boundaries. The declared-gate and exact-check inventory is in the [change-safety matrix](../../controls/quality/change-safety-matrix.md); reconciled execution evidence is in the [delivery-and-quality packet](../../evidence/packets/delivery-and-quality.md).

Coverage is **blocked**, not measured: source configures ExCoveralls and Jest coverage but inspected CI does not collect/enforce it, no retained coverage artifact was available, and local measurement required prohibited dependency restore and services. Deployed release-to-image provenance is routed through [OI-005](../../controls/open-items.md#oi-005); the ingestion failure gap retains [OI-003](../../controls/open-items.md#oi-003).

## Key Findings

| Finding | Severity | Effort | Evidence links | Confidence and limitation | Consequence | Taxonomy |
|---|---|---|---|---|---|---|
| The source has no full observed tracker-to-public-ingestion-to-buffer-to-dashboard journey, and the critical accepted-before-durable interval lacks an abrupt-loss or datastore-failure reconciliation test. Backend helpers explicitly flush buffers; dashboard E2E injects stats through an EE-only test controller. | High | M | [E-004](../../evidence/evidence-ledger.md#e-004), [E-011](../../evidence/evidence-ledger.md#e-011), [matrix](../../controls/quality/change-safety-matrix.md#critical-path-and-fixture-provenance), [OI-003](../../controls/open-items.md#oi-003) | High source confidence; no claim that production data was lost. EE-only E2E is not CE Run evidence. | A green suite can coexist with unquantified event loss or contract drift across the exact journey used for search/registration measurement. | none |
| Code coverage is unmeasured: coverage tooling exists, but no inspected CI threshold/result or retained artifact establishes line, branch, or critical-path coverage. | Medium | M | [E-009](../../evidence/evidence-ledger.md#e-009), [E-010](../../evidence/evidence-ledger.md#e-010), [coverage position](../../controls/quality/change-safety-matrix.md#exact-executed-and-unexecuted-boundary) | High confidence for approved sources; a non-public report could exist. | The audit cannot quantify coverage or use test volume as a proxy for safe change. | none |
| Run release/upgrade provenance is not closed: tracker browser CI is PR/manual only, release workflows do not depend on quality workflows, the deployed CE tag/digest is unknown, and source tests do not prove the library's interwoven migration, backup, rollback, or recovery path. | Medium | L | [E-005](../../evidence/evidence-ledger.md#e-005), [E-009](../../evidence/evidence-ledger.md#e-009), [E-010](../../evidence/evidence-ledger.md#e-010), [E-012](../../evidence/evidence-ledger.md#e-012), [OI-004](../../controls/open-items.md#oi-004), [OI-005](../../controls/open-items.md#oi-005) | High source confidence; GitHub tag authority, library deployment, and recovery evidence unavailable. | Run could consume an artifact without proof that its exact source passed relevant gates or that the dual-store change can be safely recovered. | SLSA provenance |
| The exact audited commit passed the enforced merge-group gate, but its later master-push Elixir workflow errored during dependency resolution while the independently triggered private EE-image build succeeded. | Medium | S | [E-010](../../evidence/evidence-ledger.md#e-010), [packet](../../evidence/packets/delivery-and-quality.md#observations) | High confidence in public run logs; the failure occurred before static commands and is not a code-defect finding. The EE image is not CE Run evidence. | External dependency failure can leave a red default branch while artifact automation proceeds, complicating release confidence unless artifact-to-green-run linkage is verified. | none |
| Generated query types have a CI drift check, but material E2E event and expected-output fixtures are independently built or of unknown production provenance. | Low | M | [E-013](../../evidence/evidence-ledger.md#e-013), [matrix](../../controls/quality/change-safety-matrix.md#critical-path-and-fixture-provenance) | High confidence in inspected fixtures; no production data was requested or needed. | Manual contracts can lag implementation without a failing generation/conformance gate, reducing confidence in untested combinations. | none |

## Mandate-Relevant Strengths

- The active default-branch ruleset requires merge queue, one approval, strict status checks, linear history, and the aggregate `enforce-all-checks` status; the audited merge-group commit passed that control ([E-010](../../evidence/evidence-ledger.md#e-010)).
- The exact commit recorded 12,188 test-case passes, with zero observed failures/errors; 6,468 were EE backend, 5,148 CE backend, 67 EE-only application E2E, and 505 Jest. This is broad change evidence, not unique-test, CE dashboard, or coverage proof ([E-010](../../evidence/evidence-ledger.md#e-010)).
- CI explicitly includes slow and migration-tagged backend tests in both main variants, and source tests exercise interwoven migration ordering ([E-009](../../evidence/evidence-ledger.md#e-009), [E-011](../../evidence/evidence-ledger.md#e-011)).
- Query API TypeScript is generated from a repository JSON schema and CI fails on regeneration drift ([E-013](../../evidence/evidence-ledger.md#e-013)).
- Tracker tests cover three major browser engines and material pageview/custom-event/form/package/legacy behavior when applicable ([E-009](../../evidence/evidence-ledger.md#e-009)).

### Decision Insights

1. **Run upgrade acceptance must bind the deployed digest to source, green evidence, and recoverable dual-store change.** A protected `master` and one green merge-group run do not identify the library's deployed CE release or prove its migration/rollback path. Choosing Run without that chain risks inheriting unknown fixes, conditional-test gaps, or an unrecoverable partial migration. Close [OI-001](../../controls/open-items.md#oi-001), [OI-004](../../controls/open-items.md#oi-004), and [OI-005](../../controls/open-items.md#oi-005) before treating upstream quality as deployment quality.
2. **Measurement completeness needs one targeted failure/round-trip proof, not a larger generic test count.** Browser tracker, public ingestion, buffered persistence, and dashboard tests exist as pieces, but fixtures/forced flushes bypass the failure boundary. A wrong green-suite inference could overstate search/registration measurement completeness. Set tolerance through [OI-002](../../controls/open-items.md#oi-002), then execute [OI-003](../../controls/open-items.md#oi-003).
3. **Quality evidence is option-specific.** The CE repository can inform Run; it does not establish the hosted runtime for Subscribe, and no replacement source was approved. A wrong transfer would make the option comparison look more complete than it is. Require option-specific service/release evidence downstream.

## Selected Outputs

- [Test health and change-safety matrix](../../controls/quality/change-safety-matrix.md), including the declared-gate inventory, exact execution boundary, fixture provenance, critical-path coverage, and source-bounded release-flow diagram.
- [Delivery and quality evidence packet](../../evidence/packets/delivery-and-quality.md).

## Material Omissions, Unknowns, And Auditor Questions

No new material auditor question was raised. The unanswered service-loss/outage threshold remains routed through [OI-002](../../controls/open-items.md#oi-002); it changes acceptance for the test gap but does not require the Code Quality reviewer to invent a threshold. Exact deployed release/image, coverage, critical round-trip/failure behavior, and hosted/replacement quality are proof needs, not auditor questions.

## Reconciliation

Architecture's buffered-ingestion finding is reinforced, not duplicated: source tests cover forced flush and one linked-process regression but not abrupt acknowledged-event loss. Public CI adds a bounded strength unavailable to Architecture. The exact commit's merge-group success and later push failure are not contradictory: they are separate events, and the later failure occurred during dependency retrieval before static commands. No prior Code Quality finding existed. Both collectors reached one completed terminal outcome. The single artifact-quality worker returned `REVISE`; outputs were revised once to correct the CE/EE boundary, execution accounting, fixture terminology, release separation, citations, and Run upgrade proof.

## Bounded Conclusion And Downstream Guidance

The audited source shows mature, broad declared change controls and a successfully enforced merge-group run for the exact snapshot. It does not establish measured coverage, deployed-image provenance, the library's live correctness, the buffered-ingestion loss behavior, hosted-service quality, or a replacement product's quality. Product Value may use the covered goals/reports/dashboard paths but must not treat them as user acceptance; Application Security may use the gate/fixture boundaries but not infer security effectiveness; Maintenance Cost should treat the multi-service test matrix and release verification as ongoing Run effort.
