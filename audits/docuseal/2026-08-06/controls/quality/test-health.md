# Test Health — DocuSeal Community 3.1.7

## Boundary And Outcome

This assessment covers pinned source `a2d8b855491793870b7b4acf176d2d95ae95ff83`, the declared workflows, source-visible tests, and the shared pinned GitHub Actions results. It does not claim production correctness, legal validity, cryptographic acceptance, or target-environment readiness.

| Dimension | Evidence-backed position | Decision use |
|---|---|---|
| Hosted gates | RuboCop, ERB lint, ESLint, Brakeman, and RSpec/assets jobs passed on tag `3.1.7`; tag image build/push also passed. | Useful snapshot signal, bounded to configured jobs. |
| Local execution | No local quality gate ran: Ruby 2.6.10 versus required 4.0.5; Bundler 4.0.3, Yarn, gems, and `node_modules` absent. No install/restore authorized. Docker publication was not preflighted or attempted locally. | The five application gates were not runnable; local reproduction and exact test counts are blocked, not failed. |
| Source test inventory | 41 RSpec files / 247 declared examples: 64 job, 5 library, 38 request, 140 system. Targeted search found zero disabled/pending declarations. | Source inventory only; not an executed pass count. |
| Coverage | `COVERAGE=true` is exported, but source only requires SimpleCov after Rails load and has no `SimpleCov.start`, threshold, refuse-drop rule, or retained artifact. | Coverage is **unmeasured**; no percentage or 90% claim is available. |
| Frontend | 22 Cuprite system files exercise browser workflows at 1200×800. No standalone frontend unit/component tests, type checker, mobile viewport matrix, accessibility gate, or Vue lint in CI. | Desktop behavior has meaningful tests; mobile/component regression control is unresolved. |
| Fixture/oracle provenance | Factory records/artifacts are production-generated from test-authored synthetic inputs; PKCS and webhook expectations are production-generated; binary fixtures have unknown provenance. | Green tests can establish wiring but not independent artifact or contract conformance. |

## Declared Gates And Exact Execution Status

See the [CI/test/release packet](../../evidence/packets/code-quality-ci-test-release.md) for exact commands, working directory, tool states, run IDs, and results. Local quality checks: **0 executed, 0 passed, 0 failed, 0 errored**; five application gates were not runnable. Docker publication was not attempted locally. Hosted pinned jobs: **all 5 declared CI jobs passed, 0 failed, 0 errored**; RSpec example pass/fail/error/pending counts are unavailable. One separate Docker build/push job passed.

## Critical-Path Test Health

| Critical path | Present evidence | Health |
|---|---|---|
| Public signer UI | System tests exercise forms, signature drawing, verification steps, and completion enqueue. | Partial |
| Signed result PDF and audit trail | Completion job test executes result generation and checks that stored SHA-256 metadata is present/equal; it does not recompute the digest or assert an audit artifact. | Weak for mandate claim |
| Uploaded signature verification | UI render is tested. | Weak |
| Completion retries/concurrency/recovery | Production code has lock/retry/fail paths. | Weak |
| Webhook delivery | Event families test dispatch/error requeue; one family tests an HMAC round-trip with production code. | Moderate for wiring |
| API integration | Request specs cover five endpoint areas and production/test-account separation. | Partial |
| Database upgrade | CI creates and migrates a fresh PostgreSQL 14 database. | Weak for upgrade |
| Release image | Multi-architecture build/push succeeded. | Weak for deployable artifact |

The [change-safety matrix](change-safety-matrix.md) is the canonical route for each uncovered failure, consequence, and next proof/action.

## Release-Delta Signal

Tag `3.1.7` changed 90 files versus `3.1.6`, including 73 frontend-facing files, with no `spec/` changes. The aggregate hosted RSpec/assets job passed, so this is not a defect finding or evidence of release-delta-specific assertions. It is a change-safety gap for the release’s mobile/UI work because the system viewport is fixed at desktop size and CI omits Vue files from ESLint.

## Open Routes

- OI-006 — independent regulated-onboarding artifact/failure acceptance suite, merged into the evidence-lifecycle item.
- OI-007 — reproducible suite result with test counts, skip counts, and actual coverage measurement.
- OI-008 — Vue/mobile/browser/accessibility and release-delta frontend gates.
- Architecture OI-004 — controlled release/promotion, immutable artifact and migration gates.
- Architecture OI-005/OI-006 — versioned integration contracts and evidence lifecycle verification.
