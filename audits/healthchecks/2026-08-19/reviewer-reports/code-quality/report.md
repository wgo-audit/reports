# Code Quality

## Audit Question, Depth, And Evidence Boundary

This detailed review asks which test, defect, and change-safety evidence at
`HC-CODE-001` commit `fafac59eeb00cfdc87166242544fa071ecad1723` materially
changes Acme's pull/make/buy decision. It uses the pinned source, declared
workflows and contributor guidance, CodeGraph relationships, commit-specific
public GitHub Actions results, and only already-installed local tools. The
cutoff is 2026-08-19. Evidence is registered as
[E-009 through E-013](../../evidence/evidence-ledger.md).

No dependency was installed, no lockfile or product source was changed, and no
live service, provider, Acme job, browser, migration upgrade, recovery path, or
human response was tested. Hosted green checks prove only their recorded
source-bounded executions.

## Coverage And Material Gaps

The review inventoried every declared gate; inspected 1,750 static test
definitions, critical alert-path tests, synthetic fixture provenance, the
Python/database matrix, browser-side JavaScript, generated documentation, and
release publication; and traced critical source-to-test relationships with
CodeGraph. Detailed gate and execution totals are in the
[test-health and change-safety assessment](../../controls/quality/test-health-and-change-safety.md).

The pinned commit has strong hosted regression evidence: 12 database/Python
matrix jobs passed 21,000 test executions, a coverage job passed another 1,750,
strict mypy checked 652 files without issues, and CodeQL completed three
language jobs. Coveralls reported 92% `hc` statement coverage, excluding
migrations, while `master` still resolved to the pinned commit.

Local Django tests, coverage, and mypy could not start because Django and the
Django mypy plugin are absent; installation was not authorized. Their local
test totals are 0 passed, 0 failed, 0 errors, and 0 skipped. The hosted results
are direct public evidence, but no local reproduction claim is made.

Material gaps remain: no critical-path fault/burst/human-receipt test, no
Acme-owned acceptance corpus, no prior-release migration/rollback rehearsal, no
JavaScript behavior gate, no source-visible release dependency on green checks,
and no established branch-protection enforcement. OI-008 in the
[open-items register](../../controls/open-items.md) routes the Acme acceptance
and promotion control; OI-007 retains recovery, and OI-006 retains five-minute
fault proof.

## Key Findings

| Finding | Severity | Effort | Evidence links | Confidence and limitation | Consequence | Taxonomy |
|---|---|---|---|---|---|---|
| The alert-claim test expects `Flip.processed` to be set while notification is mocked; no reviewed test covers worker death after claim, durable requeue/redelivery, burst queue latency, live provider delivery, or human receipt. The source defaults to one worker, handles a flip's channels sequentially, and permits three 30-second HTTP attempts per channel. | High | M | E-011 in the [evidence ledger](../../evidence/evidence-ledger.md), [test-health assessment](../../controls/quality/test-health-and-change-safety.md#fixture-provenance-and-critical-path-coverage), OI-006 in the [open-items register](../../controls/open-items.md) | High for source/test coverage; no live fault execution | These mechanics consume and can queue within the 300-second budget; they do not prove an observed miss. OI-006 fault/T0-T1 evidence is a production stop condition. | none |
| Acme has no approved acceptance/promotion gate tying a reviewed immutable version to job contracts, critical browser flows, alert fault tests, and release acceptance. | High | M | E-009 and E-010 in the [evidence ledger](../../evidence/evidence-ledger.md), OI-008 in the [open-items register](../../controls/open-items.md) | High that no Acme evidence was approved; required cases depend on OI-001 | Pull could ingest an upstream regression; make would multiply the same gap across every merge; buy remains outside source-suite coverage. | none |
| The release workflow is configured to build and push on release/manual events but has no source-visible dependency on Tests, Coverage, or Mypy; required checks on `master` could not be established. | Medium | S | E-009 in the [evidence ledger](../../evidence/evidence-ledger.md), [source-access register](../../evidence/source-access-register.md), OI-008 in the [open-items register](../../controls/open-items.md) | High for workflow structure; protection returned HTTP 404 and rulesets returned an empty list, which does not test release/manual-dispatch control | A published artifact can be treated as acceptable without an evidenced promotion decision even when adjacent checks are not proved mandatory. | none |
| The four-database matrix creates fresh test databases and coverage excludes migrations; no reviewed gate upgrades representative prior-release data, restores backup, or tests rollback. | High | M | E-009 and E-012 in the [evidence ledger](../../evidence/evidence-ledger.md), OI-007 in the [open-items register](../../controls/open-items.md) | High for declared gates; no production-shaped database evidence | A nominally green upgrade can still make the monitoring system unavailable or irrecoverable. | none |
| Thirty-five tracked root JavaScript files have no package manifest or JavaScript behavior/build test; hosted CodeQL is static analysis, while Django tests do not execute browser behavior. | Medium | M | E-012 in the [evidence ledger](../../evidence/evidence-ledger.md), [change-safety matrix](../../controls/quality/test-health-and-change-safety.md#change-safety-matrix) | High for the pinned tree; browser use by Acme is unknown | If Acme uses these UI paths operationally, monitor configuration and incident UI behavior can regress without a targeted executable gate; a fork would own that gap. | none |
| Ruff guidance is not reproducible: no version, configuration, canonical command, dependency, or CI gate is declared; installed Ruff 0.9.4 found 2 lint violations and 5 files needing format. | Low | S | E-009 and E-013 in the [evidence ledger](../../evidence/evidence-ledger.md) | High for current source and installed tool; results may differ under another Ruff version/rule set | Contributors and a fork owner can get contradictory style outcomes, adding avoidable change friction. | none |

## Mandate-Relevant Strengths

- The hosted matrix executes 1,750 tests against four relational engines and
  three current Python versions; all 12 matrix jobs passed at the pinned commit.
- Separate coverage and strict-mypy workflows passed; Coveralls reported 92%
  `hc` statement coverage excluding migrations, and mypy reported no issues
  in 652 source files.
- Tests exercise ping ingestion, schedules/grace, API and UI server behavior,
  integration payloads, transient transport errors, and notification status.
  CodeGraph maps `sendalerts.py` to direct tests and maps the pinned webhook
  change to its dedicated test file.
- The Docker publication workflow is configured to build three architectures
  and request an SBOM when triggered. This can help artifact inspection,
  although no pinned-commit publication run occurred and it is not an
  acceptance gate.

### Decision Insights

1. **Prefer pull over make at the code-ownership stage, but only behind an
   Acme gate.** Upstream's broad green suite lowers ordinary regression risk;
   the untested gaps are primarily Acme-specific fault, migration, browser, and
   promotion acceptance. Forking before isolating a source defect would add a
   larger permanent test matrix without closing those gaps. Smallest action:
   implement OI-008, then use OI-006 evidence to decide whether source changes
   are actually required.
2. **A green upstream commit is necessary but not sufficient for a critical
   monitor.** The suite verifies the current claim-before-delivery design but
   does not challenge the exact silent-loss condition that drives Acme's
   mandate. Mistaking regression success for resilience proof could approve an
   option that misses the five-minute requirement. Smallest proof: execute
   OI-006 through the OI-008 acceptance gate.
3. **Upgrade safety is a release acceptance problem for pull and a compounding
   ownership problem for make.** Fresh-database tests do not establish upgrade
   or rollback behavior. A wrong pull decision risks upgrade outage; a wrong
   make decision adds fork migrations and merge combinations. Smallest action:
   close OI-007 with production-shaped migration, restore, and rollback tests.

## Selected Outputs

- Required and triggered: [Test health and change-safety assessment](../../controls/quality/test-health-and-change-safety.md), combining the declared-gate inventory, exact execution totals, fixture provenance, critical-path coverage, and pull/make implications.

A separate defect register was not created. The material alert-delivery behavior
is already registered by Architecture as [ADR-001](../../controls/architecture/adr/ADR-001-database-mediated-alert-state.md)
and routed to OI-006; Code Quality records the missing challenge tests without
reclassifying an observed design as a confirmed defect.

## Material Omissions, Unknowns, And Auditor Questions

No Code Quality question is raised to the auditor. The missing facts require
implementation or observed proof, not an answer by assertion.

- Coverage position: **measured upstream, locally blocked**. The hosted run
  instrumented `hc` excluding migrations and submitted successfully; Coveralls
  reported 92% `hc` statement coverage. Local numeric reproduction is blocked
  by absent dependencies, and no minimum threshold is declared.
- Fixture provenance: **independently-built** upstream and **unknown** for Acme.
  No production-generated or Acme job fixture was approved.
- Gate enforcement: the `master` protection endpoint returned HTTP 404 and the
  repository ruleset endpoint returned an empty list. This does not prove
  protection is absent or evaluate release/manual-dispatch control; required
  status-check enforcement on `master` was not established.
- Live provider contracts, JavaScript browser behavior, hosted-service runtime,
  prior-release data upgrades, and the five-minute T0/T1 path were not executed.

**Documented outside audited scope; not independently verified.** External
notification provider behavior and Acme job wrappers are referenced by the
implementation and tests, but their live contracts and failure behavior are
outside the approved source. The smallest expansions are the OI-001 job
inventory and the bounded OI-006/OI-008 acceptance evidence.

## Reconciliation

This is a fresh Code Quality review. Architecture's source finding that flips
are claimed before delivery is consistent with the tests: the direct test
asserts the processed timestamp and mocks notification. No material source/test
conflict was found.

No card-listed collector was started: the reviewer performed the gate, Python,
JavaScript, release, and hosted-CI slices directly because concurrent audit
slots were occupied. The required `code_quality_artifact_review` worker read
the quality rubric, returned one completed terminal outcome, wrote no state, and
its feedback was reconciled in this single revision pass. No child task remains
running or ambiguously terminated.

## Bounded Conclusion And Downstream Guidance

The pinned source has a broad, currently green upstream regression suite and a
credible code base for **pull**, but it does not prove Acme's five-minute or
no-silent-loss outcome and it is not an Acme release gate. Code Quality does not
justify **make**: a fork would inherit every upstream gate and add merge,
migration, browser, provider-contract, and release responsibilities. **Buy**
cannot inherit source-suite conclusions about hosted runtime.

Maintenance Cost and Project Health should use E-009..E-013 and the linked
control to price and assess the quality burden. They must not assume branch
gates are enforced, local tests ran, Acme fixtures exist, migrations are safe,
providers were exercised, or any option meets five minutes.
