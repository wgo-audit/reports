# Code Quality

## Audit Question, Depth, And Evidence Boundary

This detailed review asks which code-level risks materially affect correctness, delivery, maintainability, security, or product promises. It covers `primary-code` at commit `9cc669b97ece3ecd37fcb3950791cb3873d7944d`, declared gates, direct test/source inspection, and targeted public GitHub issues, PRs, reviews, and Actions effective by the 2026-08-22 22:08:28 EDT cutoff. Post-cutoff API access is used only to validate cutoff-bounded records. No dependencies were installed, no live control was exercised, and production, private repository settings, internal defects/incidents, and deployment evidence remain excluded.

## Coverage And Material Gaps

The review inventoried Elixir EE/CE, application E2E, dashboard/Jest, tracker/multi-browser, migration, spelling, aggregate, and Checkly-definition gates ([E-013](../../evidence/evidence-ledger.md#e-013)); inspected source-level test breadth and fixture construction ([E-014](../../evidence/evidence-ledger.md#e-014)); and reconciled pinned-SHA hosted outcomes ([E-015](../../evidence/evidence-ledger.md#e-015)).

Coverage position is **`blocked`**: coverage tools exist, but no declared CI coverage command, threshold, or accessible report was found, and local dependencies/toolchains were absent. Fixture provenance is predominantly **`independently-built`**; production-generated fixture use is **`unknown`**. Case-level outcomes, retry/flakiness history, branch/ruleset enforcement, a real tracker-to-persistence-to-dashboard journey, and production release/migration behavior remain [OI-008](../../controls/open-items.md#oi-008), [OI-003](../../controls/open-items.md#oi-003), and [OI-004](../../controls/open-items.md#oi-004).

## Key Findings

| Finding | Severity | Effort | Evidence links | Confidence and limitation | Consequence | Taxonomy |
|---|---|---|---|---|---|---|
| The pinned source can classify a CE local-import cleanup failure as an import failure and invoke imported-stat deletion; issue #6515 reports realized loss, while its scoped fix remained unmerged/unreviewed. | Critical | S | [E-016](../../evidence/evidence-ledger.md#e-016); [OI-006](../../controls/open-items.md#oi-006) | High for code path; issue impact is a public claim; deployed/affected versions and frequency are unknown. S covers the guard and regression test, not release discovery/recovery. | A cleanup permission failure can become analytics-data deletion and delayed misleading status for operators. | none |
| The public Stats API breakdown action raises on invalid `page`; negative coverage is absent, issue #6500 reports HTTP 500, and two fixes remained open. | Medium | S | [E-017](../../evidence/evidence-ledger.md#e-017); [OI-007](../../controls/open-items.md#oi-007) | High for exception path; 500 and volume are issue-reported/unverified live behavior. | Avoidable server errors degrade API reliability, consume error budget, and undermine boundary-validation confidence. | none |
| The full cloud safe-change gate is unproved: the pinned merge gate was green, but a master static job failed at dependency retrieval while the private image build succeeded independently. | High | M | [E-007](../../evidence/evidence-ledger.md#e-007); [E-015](../../evidence/evidence-ledger.md#e-015); [OI-003](../../controls/open-items.md#oi-003) | High for public workflow/run topology; branch rules, promotion, deployment, and runtime image are inaccessible. | An incoming CTO cannot establish that only fully validated artifacts reach production or that rollback/migration controls bound a bad change. | none |
| Public evidence shows broad tests but no measured coverage, case-level history, retry rates, fixture-lineage assurance, or one real end-to-end analytics journey. | High | M | [E-013](../../evidence/evidence-ledger.md#e-013); [E-014](../../evidence/evidence-ledger.md#e-014); [E-015](../../evidence/evidence-ledger.md#e-015); [OI-008](../../controls/open-items.md#oi-008) | High for absence within approved public source; private/internal quality evidence may exist. | Test volume can create false confidence while destructive cross-worker, API-boundary, contract-drift, and deployment defects escape. | none |
| Tracker change safety spans three engines, but known conditional flaky skips, CI retries, path-only execution, and no supported variant/browser matrix leave compatibility risk unquantified. | Medium | M | [E-006](../../evidence/evidence-ledger.md#e-006); [E-018](../../evidence/evidence-ledger.md#e-018); [OI-004](../../controls/open-items.md#oi-004) | Medium; source shows mechanisms and one reviewed change, not production usage or browser-market outcomes. | A tracker regression can affect data collection or page performance across legacy integrations without a clear stop boundary. | none |

## Mandate-Relevant Strengths

- The source contains substantial automated breadth: 307 ExUnit files, 33 Jest files, 25 tracker Playwright files, and 12 application E2E files, with separate EE/CE partitions and database-backed integration jobs ([E-014](../../evidence/evidence-ledger.md#e-014)). Counts are inventory, not executed coverage.
- The pinned merge group completed 16/16 Elixir jobs successfully; NPM, spelling, and aggregate workflows also succeeded. This is useful change evidence even though it is not production proof ([E-015](../../evidence/evidence-ledger.md#e-015)).
- Specific review histories show defects receiving targeted tests and changes-requested review before approval, including the ingestion buffer and cross-store deletion work ([E-002](../../evidence/evidence-ledger.md#e-002), [E-005](../../evidence/evidence-ledger.md#e-005)).
- Tracker CI spans Chromium, Firefox, and WebKit, and source-visible release automation checks buildability, script size, versioning, labels, and changelog discipline ([E-006](../../evidence/evidence-ledger.md#e-006), [E-013](../../evidence/evidence-ledger.md#e-013)).

### Decision Insights

1. **Positive role signal and onboarding question:** broad green public CI, specialized gates, and substantive review are credible evidence of engineering rigor. Image promotion is private and should be learned through [OI-003](../../controls/open-items.md#oi-003) after joining; its public absence does not imply an unsafe release path or justify conditioning the offer.
2. **Immediate inheritance priority:** identify CE releases containing the cleanup misclassification path and either prevent that cleanup execution or deploy and verify the scoped fix before representing local-import retention as safe. The source-proven destructive path plus issue-reported loss makes this a pre-normalization stop condition; close [OI-006](../../controls/open-items.md#oi-006).
3. **Quality-investment decision:** prioritize risk-weighted proof over a generic test-count or coverage target. The smallest next move is case-level/coverage/retry evidence plus missing import-failure, API-boundary, contract-drift, full-journey, and release/migration tests in [OI-008](../../controls/open-items.md#oi-008).

## Selected Outputs

- Triggered [Code Quality Change-Safety Matrix](../../controls/quality/change-safety-matrix.md), including declared gates, hosted outcomes, critical paths, coverage/fixture position, exact executed/unexecuted boundaries, and defect routes.

## Material Omissions, Unknowns, And Auditor Questions

No local application test ran: **passed 0, failed 0, errors 0, skipped 0**. Dependency-free checks completed **73 passed, 0 failed, 0 errors, 0 skipped**: 69 Node syntax parses, one pinned-commit whitespace check, and three package-manifest parses ([E-019](../../evidence/evidence-ledger.md#e-019)). `mix test`, compile/format/CreDo/Dialyzer/coverage, Jest/type/lint/format/generated types, both Playwright suites, tracker compilation, Terraform, migrations, load, release, and deployment checks were not run because dependencies/toolchains/services/access were absent and installation/live-control authorization was not granted.

GitHub public API job-log access returned 403; case counts, retry history, coverage, and reports remain unavailable under the recorded [source-access limit](../../evidence/source-access-register.md). No material question is routed to the auditor: remaining needs are internal verification/action, not mandate facts the auditor can answer by assertion.

## Reconciliation

No prior Code Quality output existed. No material source conflict was found, but three evidence tensions are preserved: green merge-group CI versus a failing master static job and independently successful image build; broad test inventory versus source-confirmed escaped defects; and multi-browser tracker tests versus unmeasured variant/browser support. Issue-reported impacts are kept separate from source-proven paths, and open PRs are proposals rather than merged behavior. The one required quality worker completed, returned one terminal outcome, and the selected artifact was revised once.

## Bounded Conclusion And Downstream Guidance

The repository has a serious, broad, and recently green source-visible quality system, but the pinned code also contains one potentially destructive CE import path and one public-API exception path, while coverage, fixture drift, flakiness, enforcement, and release safety remain unproved. Code Quality is complete with open verification/action through OI-003, OI-004, and OI-006–OI-008. Application Security may use the declared gate and input-boundary evidence; Maintenance Cost and Project Health may use the escaped-defect and quality-baseline burden. They must not assume production deployment, live impact frequency, coverage percentage, team performance, or branch protection.
