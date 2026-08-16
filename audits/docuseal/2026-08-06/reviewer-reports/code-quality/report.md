# Code Quality

## Audit Question, Depth, And Evidence Boundary

Which code-level risks in pinned DocuSeal Community `3.1.7` materially affect correctness, delivery, maintainability, security, or product promises for regulated web/mobile onboarding? This detailed review is cutoff at 2026-08-06 and uses direct source at `a2d8b855491793870b7b4acf176d2d95ae95ff83`, the [CI/test/release packet](../../evidence/packets/code-quality-ci-test-release.md), [Ruby/runtime packet](../../evidence/packets/code-quality-runtime-build.md), [JavaScript/UI packet](../../evidence/packets/code-quality-typescript-ui.md), [shared GitHub packet](../../evidence/packets/github-history-and-hosted-ci.md), and Architecture’s linked source evidence.

Excluded: package installation/restoration, remediation, Pro/external package implementation, penetration/load testing, target/live-environment execution, legal/regulatory acceptance, and production approval. Source tests and hosted green jobs do not prove production correctness or control effectiveness.

## Coverage And Material Gaps

The review inventoried every declared gate; inspected RSpec, frontend, Ruby/Rails/native/container and release surfaces; classified material fixture/oracle provenance; traced signer completion, document/audit generation, verification, API/webhook contracts, migrations and publication; and compared `3.1.6..3.1.7` change evidence.

All five declared CI jobs and the separate Docker publication job passed for the pinned tag. The source contains 41 RSpec files and 247 declared examples, including 140 browser/system examples. Local quality execution remained blocked without installation: the host has Ruby 2.6.10 instead of 4.0.5, no locked Bundler 4.0.3, no Yarn, and no installed gem or Node dependency trees. No install/restore was authorized. Coverage is **unmeasured**; exact RSpec pass/fail/error/pending counts were not available from the approved hosted packet.

Material gaps are independent signed-document/audit conformance, completion failure/recovery tests, release/edition contract validation, mobile/browser/accessibility/Vue gates, representative upgrade tests, measurable coverage/results, and CI-bound immutable artifact promotion. Coordinator serialization merged the acceptance suite into OI-006 and registered OI-007–OI-008; Architecture OI-003–OI-005 remain applicable.

## Key Findings

| Finding | Severity | Effort | Evidence links | Confidence and limitation | Consequence |
|---|---|---|---|---|---|
| The signer-to-completion path has useful browser and job tests, but signed/unsigned PDFs, audit artifacts, trust-chain/TSA/LTV behavior, tamper detection, and uploaded-signature verification lack independent conformance or failure-path oracles. Stored SHA-256 metadata is compared to production-populated metadata rather than recomputed; no audit artifact assertion exists. | High | L | [runtime packet §Mandate-Critical Paths](../../evidence/packets/code-quality-runtime-build.md); [test health](../../controls/quality/test-health.md); Architecture [E-015](../../evidence/evidence-ledger.md) | High for test/source shape; cryptographic and specialist acceptance intentionally untested | A green suite can coexist with an unusable or incorrectly interpreted signed agreement/audit record, directly affecting regulated onboarding evidence. |
| Tag image publication is a separate workflow with no source-visible dependency on CI and no runtime smoke, vulnerability, SBOM, signature, attestation, digest-promotion or post-publish gate. | High | M | [CI packet §Declared Gate Inventory](../../evidence/packets/code-quality-ci-test-release.md); [shared run evidence](../../evidence/packets/github-history-and-hosted-ci.md); Architecture [ADR-011](../../controls/architecture/adr/ADR-011-release-image-provenance-and-promotion.md) | High for workflow definition; protected settings and registry/deployed digest unavailable | A reviewed source tag can publish or promote an artifact whose quality/provenance is not bound to the passed source gates. |
| API, webhook, template and signer payloads are parallel implicit contracts without a release/edition-bound conformance gate; webhook expectations and HMAC round-trip reuse production serializers/verifier. | High | M | [change-safety matrix](../../controls/quality/change-safety-matrix.md); [Architecture component packet §3–7](../../evidence/packets/architecture-component-api-ui-contracts.md); [runtime packet §Fixture And Oracle Provenance](../../evidence/packets/code-quality-runtime-build.md) | High for source/test topology; external consumer and Pro contracts unavailable | Organization web/mobile clients can drift from Community/Pro endpoints or payloads while repository tests remain green. |
| Release `3.1.7` changed 90 files, including 73 frontend-facing files and broad mobile/signer/builder work, with no spec-file changes; system tests use a fixed 1200×800 viewport, CI omits all 70 Vue files from ESLint, and no component/mobile/accessibility matrix is declared. | High | M | [UI packet §Release 3.1.7 Change-Safety Signal](../../evidence/packets/code-quality-typescript-ui.md); [test health §Release-Delta Signal](../../controls/quality/test-health.md) | High for diff/configuration; the aggregate hosted RSpec/assets job passed, so no defect is inferred | Mobile onboarding, payment/phone, navigation or accessibility regressions can escape gates despite all-new-customer/revenue exposure. |
| The workflow exports `COVERAGE=true`, but source only requires SimpleCov after Rails application load and declares no start, threshold, refuse-drop rule or retained artifact; local reproduction and exact RSpec counts were unavailable. | Medium | M | [CI packet §Coverage Configuration](../../evidence/packets/code-quality-ci-test-release.md); [test health](../../controls/quality/test-health.md) | High for source and available packet; a private artifact outside scope could exist | Decision-makers cannot quantify which critical paths are exercised or detect coverage regression; “green” must remain job-scoped. |
| CI/container inputs include mutable action tags, `setup-chrome@latest`, unpinned Bundler installation, non-frozen Yarn installs, and several unchecked build downloads. | Medium | M | [CI packet §Release Reproducibility Boundary](../../evidence/packets/code-quality-ci-test-release.md); `docuseal/Dockerfile:1-45` | High for declarations; no claim that the successful pinned run actually resolved malicious/different inputs | Re-running the same source can produce different test/build behavior, weakening reproducible review and incident reconstruction. |

## Mandate-Relevant Strengths

- The assessed snapshot is reproducibly pinned, and all five configured CI jobs plus the multi-architecture publication job passed at that commit.
- The 247-example source suite has substantial browser-level breadth: signer, builder, upload, API, settings, authorization and webhook flows are represented; targeted source search found no disabled/pending example declarations.
- Completion tests execute production document generation and record result metadata; webhook job tests cover dispatch, error requeue/max-attempt behavior, secret headers and one HMAC round-trip. These are meaningful wiring/regression signals even though they are not independent conformance evidence.
- Test configuration blocks non-localhost network calls, uses verified partial doubles and transactional fixtures, reducing accidental external coupling and some mock drift (`spec/rails_helper.rb:14-18,48-81`; `spec/spec_helper.rb:3-12`).

### Decision Insights

- **Require an organization-owned acceptance layer before production approval.** Repository tests optimize upstream regression detection, while the mandate needs independent artifact validity, target failure/recovery, and release/edition contract evidence. A wrong assumption can make signed evidence or onboarding state unusable. Smallest next action: OI-006 with specialist-approved known-answer artifacts and target-topology failures.
- **Treat upstream green CI and a promotable production artifact as separate decisions.** The workflows can succeed independently, and publication lacks immutable provenance/runtime gates. Promoting by tag can invalidate every source-based conclusion. Smallest next action: extend OI-004 so digest promotion depends on passed CI, SBOM/provenance/vulnerability and runtime-smoke evidence.
- **Make the `3.1.7` mobile surface a focused evaluation target.** Broad mobile/UI change, fixed desktop tests and absent Vue lint create a release-specific evidence gap without proving a defect. Smallest next action: OI-008 across supported mobile browsers/webviews, accessibility and critical signer/payment/phone paths.

## Selected Outputs

- Triggered [test health assessment](../../controls/quality/test-health.md).
- Triggered [change-safety matrix](../../controls/quality/change-safety-matrix.md).
- Supporting [CI/test/release](../../evidence/packets/code-quality-ci-test-release.md), [Ruby/runtime/build](../../evidence/packets/code-quality-runtime-build.md), and [JavaScript/UI](../../evidence/packets/code-quality-typescript-ui.md) packets.
- No defect register was created: this review identified material evidence/control gaps, not a confirmed product defect from executed failing behavior.

## Material Omissions, Unknowns, And Auditor Questions

Open items after coordinator serialization:

| Placeholder | Type | Priority | Item and consequence | Owner | Closure route |
|---|---|---|---|---|---|
| OI-006 (expanded) | verification | P1 | Establish an independent regulated-onboarding acceptance suite; without it, signed/audit artifacts, contracts and completion failure/recovery cannot support production approval. | VP Software Engineering, CISO, IT Operations Director, Product Manager with legal/compliance specialists | Use specialist-approved known-answer signed/unsigned/tampered artifacts and independent verification; add multi-signer, audit content, webhook/API consumer, retry/concurrency/crash/reconciliation and target-store recovery cases. |
| OI-007 | verification | P2 | Produce reproducible pinned-suite results with exact example outcomes and actual coverage; current job success cannot be converted into test/coverage percentages. | VP Software Engineering | In an approved matching toolchain, run the non-mutating gates, retain machine-readable pass/fail/error/pending counts and coverage artifacts, then set risk-based critical-path thresholds. |
| OI-008 | action | P1 | Add Vue/mobile/browser/webview/accessibility and release-delta gates; target-channel regressions can otherwise affect all new customers. | VP Software Engineering, Product Manager | Add non-mutating Vue lint and supported-device/viewport/accessibility tests for signer completion, payment/phone, navigation/modal/filter and builder paths. |

Architecture OI-003–OI-006 remain the routes for target topology/recovery, controlled release/migrations, versioned integration contracts and evidence lifecycle verification. Pro packages/repositories are **Documented outside audited scope; not independently verified.** No qualifying mandate, acceptable-outcome, priority or auditor-authority question emerged.

Structural validation not run: the canonical validator is absent from the active audit root.

## Reconciliation

No baseline or prior Code Quality items exist. The apparent coverage signal (`COVERAGE=true`) was reconciled against the absence of a source-visible SimpleCov start/threshold/artifact and is reported as unmeasured, not zero. The package script’s JS/Vue scope was reconciled against the actual hosted CI glob, which covers JS only; the green ESLint job is not generalized to Vue. Hosted job success is separated from unavailable RSpec example counts and local non-execution. No GitHub issue/PR assertion was promoted to a defect, and no other material evidence conflict was found.

## Bounded Conclusion And Downstream Guidance

Code Quality supports **continue conditionally** into vendor/specialist discussions and target-owned evaluation, not production approval. The pinned repository has a meaningful green CI and browser/API/job regression baseline, but it does not independently establish signed/audit artifact correctness, mobile change safety, release/edition contract compatibility, failure/recovery behavior, measured coverage, upgrade safety or deployable artifact provenance.

Maintenance Cost should price the acceptance/gate burden and must not treat upstream green CI as eliminating target test ownership. Product Value should use the contract/artifact gaps without inferring product incorrectness or Pro defects. Project Health may use gate breadth and release-delta evidence but must not infer review quality, coverage or defect rate from job status.
