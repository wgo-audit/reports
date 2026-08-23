# Code Quality Change-Safety Matrix

## Boundary And Reading Rule

This artifact assesses source-visible test, defect, and change-safety controls for `primary-code` at commit `9cc669b97ece3ecd37fcb3950791cb3873d7944d`, bounded by the 2026-08-22 22:08:28 EDT cutoff. `[Fact]` is direct source/hosted evidence, `[Claim]` is a public issue or PR statement, `[Inference]` is a bounded consequence, and `[Unknown]` requires internal or executed proof. A green hosted job is not production readiness or deployment proof.

## Declared Gate Inventory

| Surface | Declared check | Trigger and scope | What it establishes | Material limit |
|---|---|---|---|---|
| Elixir application | 12 ExUnit jobs: EE/test and CE/test, six partitions each, PostgreSQL 18 and ClickHouse; slow/migrations included and MinIO included for EE | PR, `master`/`stable` push, merge group | `[Fact]` Source-visible compile and integration-test matrix ([E-013](../../evidence/evidence-ledger.md#e-013)) | `[Unknown]` Case-level results, coverage, flake history, branch enforcement, and production parity |
| Application browser E2E | Two Playwright shards; format and typecheck; Chromium | Same Elixir workflow | `[Fact]` Dashboard flows run against a test app with PostgreSQL/ClickHouse ([E-013](../../evidence/evidence-ledger.md#e-013), [E-014](../../evidence/evidence-ledger.md#e-014)) | Statistics are injected through a test-only endpoint; no Firefox/WebKit and no real tracker-to-ingestion full journey |
| Elixir static | Compile with warnings as errors; format; unused dependency check; generated country metadata diff; merge-base CreDo; Dialyzer | PR, push, merge group | `[Fact]` Declared type/style/generated-output checks ([E-013](../../evidence/evidence-ledger.md#e-013)) | CreDo is diff-scoped; no coverage or architecture threshold; master-push static failure does not stop the independent image build ([E-007](../../evidence/evidence-ledger.md#e-007)) |
| Dashboard assets | Generated API type diff; TypeScript; ESLint/stylelint; Prettier; Jest | PR, `master`/`stable` push, merge group | `[Fact]` Source-visible generated contract, unit/component, type, style, and format checks ([E-013](../../evidence/evidence-ledger.md#e-013)) | No declared coverage threshold; tests use independently built DOM/data fixtures ([E-014](../../evidence/evidence-ledger.md#e-014)) |
| Tracker build | ESLint, Prettier, compilation; version bump, size comparison, release label, changelog | NPM CI plus path-triggered tracker-update workflow | `[Fact]` Build and release metadata checks for tracker changes ([E-006](../../evidence/evidence-ledger.md#e-006), [E-013](../../evidence/evidence-ledger.md#e-013)) | No declared size stop threshold; required-label/review authority and deployment linkage are unknown |
| Tracker behavior | Four Playwright shards across Chromium, Firefox, and WebKit; installation-support tests Chromium-only | Tracker-path PR or manual dispatch | `[Fact]` Multi-browser behavior tests, with CI retries and known conditional skips ([E-014](../../evidence/evidence-ledger.md#e-014)) | Does not run on `master` push; retry outcomes and variant/browser completeness are unknown; see [OI-004](../open-items.md#oi-004) |
| Migration change shape | Reject selected app/config and PostgreSQL/ClickHouse migration changes in the same PR | Migration-path PR | `[Fact]` Change segregation check ([E-004](../../evidence/evidence-ledger.md#e-004)) | No migration correctness, compatibility, promotion, stop condition, or rollback proof; see [OI-003](../open-items.md#oi-003) |
| Aggregate/hygiene | Status-check waiter and codespell | PR/merge group; spelling also `master` | `[Fact]` Declared aggregation and spelling checks ([E-013](../../evidence/evidence-ledger.md#e-013)) | `[Unknown]` Actual required-check set and ruleset enforcement because protection metadata was inaccessible ([E-015](../../evidence/evidence-ledger.md#e-015)) |
| Checkly definition | Terraform format/init/validate/plan; master auto-apply for `test/e2e/*.tf` | Path PR/push | `[Fact]` Source-visible management path for synthetic endpoint definitions ([E-013](../../evidence/evidence-ledger.md#e-013)) | This is Checkly configuration, not product E2E; state, plan, applied checks, and credentials are outside the public corpus |

The PR template asks for either tests or a “does not require tests” selection but states no approval criteria. This is a workflow prompt, not an enforced policy ([E-013](../../evidence/evidence-ledger.md#e-013)).

## Hosted Cutoff-Bounded Outcome

Every row below is `[Fact; post-cutoff validation]` from public GitHub API metadata that validates runs completed before the cutoff ([E-015](../../evidence/evidence-ledger.md#e-015)).

| Run boundary | Pass | Fail | Error | Skip | Bounded conclusion |
|---|---:|---:|---:|---:|---|
| Merge-group Elixir jobs, run `32291476826` | 16 | 0 | 0 | 0 | All 12 EE/CE partitions, two Chromium E2E shards, static checks, and report merge completed successfully ([E-015](../../evidence/evidence-ledger.md#e-015)). |
| Merge-group NPM job, run `32291476808` | 1 | 0 | 0 | 0 | Generated types, types, lint, format, Jest, and tracker build steps succeeded ([E-015](../../evidence/evidence-ledger.md#e-015)). |
| Merge-group spelling and aggregate runs | 2 | 0 | 0 | 0 | Spelling and aggregate waiter succeeded; this does not expose the protected-branch ruleset ([E-015](../../evidence/evidence-ledger.md#e-015)). |
| Master-push Elixir jobs, run `32291854903` | 15 | 1 | 0 | 0 | All test/E2E jobs succeeded; the static job failed at dependency retrieval. The independent private-image build succeeded ([E-007](../../evidence/evidence-ledger.md#e-007), [E-015](../../evidence/evidence-ledger.md#e-015)). |
| Master-push NPM job, run `32291854879` | 1 | 0 | 0 | 0 | Declared JS checks succeeded ([E-015](../../evidence/evidence-ledger.md#e-015)). |

`[Unknown]` GitHub's public API did not expose test-case counts, retry counts, coverage, or retained reports; unauthenticated job-log access returned 403. Job counts above must not be represented as test counts.

## Critical-Path Change Safety

| Critical path | Credible evidence present | Missing or contradicted evidence | Safe-change position |
|---|---|---|---|
| Browser tracker behavior | Multi-browser tracker Playwright, compiled variants, size reports, tracker release metadata | Known conditional flaky skips; PR #6174 changed tracker behavior after local Chrome profiling without a test-file change and requested future compatibility proof ([E-018](../../evidence/evidence-ledger.md#e-018)) | `[Inference]` Local tracker changes have useful protection, but variant/browser support cannot be accepted without [OI-004](../open-items.md#oi-004). |
| Event acceptance and persistence | Controller/write-buffer tests and broad EE/CE ExUnit matrix ([E-002](../../evidence/evidence-ledger.md#e-002), [E-014](../../evidence/evidence-ledger.md#e-014)) | No public full journey from real tracker request through deployed persistor to dashboard; durability contract remains [OI-001](../open-items.md#oi-001) | Do not infer durable ingestion from green CI. |
| Dashboard queries and CSV export | Large ExUnit query suite, Jest components, Chromium dashboard E2E, generated API types ([E-014](../../evidence/evidence-ledger.md#e-014)) | `[Fact]` Fixtures are independently built and E2E uses a test-only population endpoint. `[Inference]` These duplicated contracts can drift; production-derived fixture use and drift measurement are unknown. | `[Inference]` Strong source-level breadth, but production correctness needs contract/fixture lineage proof in [OI-008](../open-items.md#oi-008). |
| CE local CSV import and cleanup | Import/cleaner tests exist separately | `[Fact]` Pinned error reporter does not distinguish importer from cleanup worker; the destructive cross-worker case is absent from current tests. `[Claim]` Issue #6515 reports completed imports purged after cleaner failure ([E-016](../../evidence/evidence-ledger.md#e-016)). | `[Inference]` A release containing this path can delete retained imported rows under the described failure. Identify such releases and either prevent cleanup execution or deploy and verify the scoped fix before representing local-import retention as safe; close [OI-006](../open-items.md#oi-006). |
| Public Stats API boundary | Extensive breakdown controller tests | `[Fact]` Pinned action raises on invalid `page`; the negative case is absent and two fixes remained open. `[Claim]` Issue #6500 reports an HTTP 500 response ([E-017](../../evidence/evidence-ledger.md#e-017)). | `[Fact]` The unhandled input-exception path remains; close [OI-007](../open-items.md#oi-007). |
| Schema/data migration | Partitioned EE/CE migrations and change-segregation workflow | No production sequence, compatibility window, data correctness, rollback, or recent release proof | Safe change requires [OI-003](../open-items.md#oi-003); source checks alone are insufficient. |
| Cross-store deletion | Targeted worker tests and reviewed PR history | Async mutation completion and reconciliation remain unproved | Safe change requires [OI-002](../open-items.md#oi-002). |
| Cloud promotion/release | Successful merge gate and independent image build are visible ([E-007](../../evidence/evidence-ledger.md#e-007), [E-015](../../evidence/evidence-ledger.md#e-015)) | Image publication is not gated by the Elixir workflow; branch rules, promotion, deploy, runtime image, and rollback are unknown | Do not equate published image, notification, or green merge group with production deployment; close [OI-003](../open-items.md#oi-003). |

## Coverage And Fixture Position

- **Coverage position: `blocked`.** ExCoveralls and Jest coverage support are configured, but no declared CI coverage command, threshold, public coverage artifact, or current measurement was found in the approved source. Local coverage could not be run without restoring absent dependencies, which was not authorized ([E-013](../../evidence/evidence-ledger.md#e-013), [E-019](../../evidence/evidence-ledger.md#e-019)). The audit therefore cannot confirm the requested 90% target.
- **Fixture provenance: predominantly `independently-built`.** ExMachina factories, synthetic ClickHouse events, HTML pages, expected CSVs, mocks, and a test-only E2E population endpoint dominate ([E-014](../../evidence/evidence-ledger.md#e-014)).
- **`unknown` exceptions:** production-generated fixtures were not established. The GeoLite2 test database cites MaxMind-DB without an exact version/checksum. Synthetic E2E/event builders and generated dashboard types duplicate production contracts; no drift result beyond the generated-type diff is visible.
- **Flakiness:** application and tracker Playwright retry twice on CI; tracker source marks at least two browser conditions as `flaky` and contains other conditional browser skips. Public metadata does not expose whether retries occurred ([E-014](../../evidence/evidence-ledger.md#e-014), [E-015](../../evidence/evidence-ledger.md#e-015)).

## Executed And Unexecuted Checks

Working directory for all local checks: `primary-code:.`. Dependency state: `deps`, `_build`, and all three `node_modules` directories absent; `mix`, Elixir, and Terraform unavailable; Node v25.3.0, npm 11.7.0, Docker 29.5.3, and Python 3 available. Installation/restoration authorization: **not granted**.

| Command | Intended coverage | Pass | Fail | Error | Skip | Conclusion |
|---|---|---:|---:|---:|---:|---|
| `node --check` over 69 repository JS/MJS files | Dependency-free JavaScript syntax parse | 69 | 0 | 0 | 0 | Syntax only; imports, behavior, TypeScript, and generated output not checked. |
| `git diff --check HEAD^ HEAD` | Whitespace errors in pinned commit diff | 1 | 0 | 0 | 0 | Does not assess broader correctness. |
| `npm --prefix <package> pkg get name scripts` for `assets`, `tracker`, and `e2e` | Parse three package manifests | 3 | 0 | 0 | 0 | Does not install or execute packages. |

No local application test ran: **tests passed 0, failed 0, errors 0, skipped 0**. The following declared commands were not executed, rather than silently skipped: `mix test` in EE/CE profiles and partitions; `mix compile`, format, CreDo, Dialyzer, migrations, and coverage; asset Jest/type/lint/format/generated-type checks; tracker and application Playwright; tracker compilation; Terraform format/init/validate/plan; and any release, migration, load, production, or deployment check. Reasons are absent dependencies/toolchains/services/access and the audit's no-install/no-live-control boundary ([E-019](../../evidence/evidence-ledger.md#e-019)).

## Defect Register And Required Next Moves

Severity is consequence-based; effort is the smallest immediate proof/correction, not the full recovery program. `Critical / S` for the cleanup path reflects possible imported-data deletion from a localized worker guard plus regression test, while affected-release discovery and recovery remain broader [OI-006](../open-items.md#oi-006) work. `Medium / S` reflects a contained public-API error path with a localized validation/test correction. `High / M` in the original specialist classification orders onboarding verification where public evidence stops; it is not an offer-stage negative or a claim that the private release process is weak.

| Defect/control gap | Classification | Status at cutoff | Required route |
|---|---|---|---|
| CE cleanup failure can be classified as import failure and invoke imported-stat deletion | Critical / S | `[Fact]` Destructive source path; `[Claim]` issue #6515 reports realized loss; PR #6547 unmerged and unreviewed | [OI-006](../open-items.md#oi-006) |
| Invalid public Stats API `page` raises; issue reporter states it returns 500 | Medium / S | `[Fact]` Exception path; `[Claim]` HTTP 500; issue #6500 and two regression-tested fixes remained open | [OI-007](../open-items.md#oi-007) |
| Coverage, case-level outcomes, retries, fixture lineage, branch enforcement, and one full analytics journey are unproved | High / M | Open verification | [OI-008](../open-items.md#oi-008) |
| CI-to-image/promotion gate is not established | High / M | Open verification inherited from Architecture | [OI-003](../open-items.md#oi-003) |

## Safe-Change Boundary

The repository demonstrates substantial automated test breadth and a successful cutoff-bounded merge-group gate. It does **not** establish production readiness, enforced branch rules, measured coverage, durable ingestion, release/promotion safety, or current live behavior. `[Fact]` The pinned source contains a path that can invoke imported-stat deletion after a cleanup-worker failure; `[Claim]` issue #6515 reports realized loss; `[Inference]` releases containing that path carry a data-loss risk under the described condition. The immediate stop condition is to identify those releases and either prevent the cleanup path from executing or deploy and verify the scoped fix before representing CE local-import retention as safe. Changes touching persistence, deletion, migrations, editions, tracker variants, or release controls require the linked proofs before an incoming CTO accepts the risk envelope.
