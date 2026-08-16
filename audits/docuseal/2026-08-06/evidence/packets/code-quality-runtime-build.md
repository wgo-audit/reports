# Code Quality Evidence Packet — Ruby/Rails Runtime And Build Surfaces

## Scope And Evidence Boundary

Pinned source: `docuseal/` tag `3.1.7`, commit `a2d8b855491793870b7b4acf176d2d95ae95ff83`. Observed 2026-08-06. This packet covers Ruby/Rails/native/build change safety; it does not prove runtime reliability or production operation.

## Observations

### Test Inventory And Execution Boundary

Static inventory found 41 RSpec files and 247 declared examples: 13 job files / 64 examples; 1 library file / 5 examples; 5 request files / 38 examples; and 22 system files / 140 examples. No disabled `xit`/`xdescribe`/`pending`/`skip` declaration was found by targeted search. These are source counts, not executed pass counts. Local execution was blocked by absent dependencies and runtime mismatch; the hosted pinned RSpec job passed but exposed no example or coverage counts in the approved packet.

The product surface contains 89 `lib/**/*.rb` files, 34 models, 126 controllers, and 21 jobs. Direct specs cover 13 jobs, five API request areas, one library validator, and browser workflows; no model-spec directory and no migration specs were found. Raw file ratios are navigation signals only, not coverage percentages.

### Mandate-Critical Paths

| Path | Credible change-safety evidence | Material boundary |
|---|---|---|
| Signer UI to completion enqueue | Cuprite system spec fills and signs a form and observes `ProcessSubmitterCompletionJob` enqueue (`spec/system/signing_form_spec.rb:1142-1159`). | Does not execute the async completion/artifact path in the system scenario. |
| Completion result generation | `ProcessSubmitterCompletionJob` spec uses a generated certificate, executes the job, asserts completed records, and checks that `CompletedDocument.sha256` is present and equals production-populated attachment metadata (`spec/jobs/process_submitter_completion_job_spec.rb:3-50`; production call chain at `app/jobs/process_submitter_completion_job.rb:9-50`). | It does not recompute the digest or assert an audit artifact. Only three examples; no independent PDF signature/PAdES/TSA/LTV verification, unsigned path, audit-content integrity, multi-signer ordering, retry/fail/concurrency, or recovery assertions. |
| Audit/signature verification | Production can sign or write unsigned audit PDFs (`lib/submissions/generate_audit_trail.rb:33-69`) and exposes upload verification (`app/controllers/verify_pdf_signature_controller.rb:3-18`). | No direct spec for `EnsureAuditGenerated`, `GenerateAuditTrail`, `GenerateResultAttachments`, or the verification controller; UI-render-only test is not conformance evidence. |
| Webhook event delivery | Eleven event job families have tests for payload dispatch/retry; the submission-created spec covers secret header, HMAC round-trip, HTTP error requeue and maximum attempts (`spec/jobs/send_submission_created_webhook_request_job_spec.rb:15-117`). | Expected payloads call the same production serializers, and HMAC is verified with the same production verifier, so contract/cryptographic vectors are production-generated rather than independent. No release-bound external consumer contract is validated. |
| REST API | Five request-spec files exercise submissions, submitters, templates, tools, and forms, including production/test-account separation. | No check binds routes/serializers to `docs/openapi.json`; Architecture observed documented/implemented edition/path divergence. |
| Migrations/build | Hosted RSpec job creates/migrates PostgreSQL 14 and precompiles assets (`ci.yml:111-179`); tag container build succeeded. | No upgrade-from-prior-version, rollback, pooled-connection, multi-node, data-migration recovery, image runtime/smoke, or post-publish verification gate. |

### Fixture And Oracle Provenance

- FactoryBot database records and field structures are **production-generated from test-authored synthetic inputs** because they execute production persistence/processors; they are not independent conformance oracles.
- The PKCS material in completion/webhook specs is **production-generated** through `GenerateCertificate.call` (`spec/jobs/process_submitter_completion_job_spec.rb:10-13`; `spec/jobs/send_submission_created_webhook_request_job_spec.rb:10-13`). No independent certificate chain, trusted external verifier, TSA response, or known-answer signature vector is used.
- Webhook payload expected values are **production-generated** by the same serializer used by implementation; HMAC is checked by the same production verifier (`spec/jobs/send_submission_created_webhook_request_job_spec.rb:24-75`). These tests detect wiring regressions but not shared serializer/verifier drift.
- Binary document fixtures have **unknown** provenance; repository history establishes when they appeared, not how they were produced or whether they represent organization documents, KYC inputs, malformed files, adversarial PDFs, or jurisdiction-specific evidence cases.

### Contract And Failure Boundaries

No source-visible gate validates `docs/openapi.json` or the Markdown webhook schemas against routes/serializers. No mutation, property-based, fuzz, malformed-document, independent artifact-verification, or database upgrade/rollback suite is declared. This does not mean those techniques are mandatory for every change; it means critical regulated-onboarding claims currently depend on green broad tests without measured coverage or independent conformance oracles.

## Material Unknowns And Access Limits

Target `ProcessSubmitterCompletionJob`, `Submissions::EnsureResultGenerated`, `Submissions::GenerateResultAttachments`, `Submissions::EnsureAuditGenerated`, `Submissions::GenerateAuditTrail`, `VerifyPdfSignatureController`, `SendWebhookRequest`, `WebhookUrls::Signatures`, and migration/boot scripts when change rationale matters.

## Reuse Guidance

Reviewers may reuse the source and bounded test observations with their recorded limitations. Counts, hosted success, and production-generated fixtures must not be treated as coverage percentages, independent conformance evidence, runtime reliability, or production acceptance.
