# Code Quality

## Audit Question, Depth, And Evidence Boundary

This detailed review asks which code-level risks materially affect correctness, delivery, maintainability, security, product promises, and successor change safety. It uses cutoff-pinned source, a CodeGraph preflight, package/workflow declarations, test source, Architecture/Product/Project Health handoffs, and public hosted records through July 22, 2026. `node_modules/` was absent in `code`, `v8s-link`, and `website`; `.terraform/` was absent in `v8s-config`. Installation and executable checks were not approved, so no local build, lint, test, validation, coverage, Terraform, deploy, or runtime command ran.

## Coverage And Material Gaps

The review covers Worker behavior, build/registry/link/policy code, setup/detach/upgrade, CLI/Git operations, public-page generation, complexity, dependencies, Terraform, and website quality. The product repository contains 14 declared test scripts and a broad integrated check. Material gaps are executed evidence for the pinned state, coverage measurement, non-creator end-to-end checks, non-blocking complexity limits, absent infrastructure/instance CI, and weak website reproducibility.

## Key Findings

| Finding | Evidence links | Confidence and limitation | Consequence |
|---|---|---|---|
| The product repository has substantial source-level change-safety coverage across critical behavior, including a 1,741-line Worker test and focused build/install/detach/upgrade/registry/policy tests. | [Change-safety matrix](../../controls/quality/change-safety-matrix.md), `package.json`, test source | High for source presence/coverage areas; nothing was executed and no coverage percentage exists. | A new maintainer inherits meaningful regression intent, reducing—but not eliminating—change risk. |
| One `npm run check` composes formatting, build, hygiene/complexity lint, and 14 test scripts; hosted checks have succeeded for exact cutoff-eligible records. | [E-011](../../evidence/evidence-ledger.md), [delivery packet](../../evidence/packets/delivery-and-quality.md) | High for declaration and named runs; latest-100 sample, not pinned-local verification or production proof. | The product has a credible quality gate, but takeover acceptance still needs a clean successor-run result. |
| Complexity risk is explicitly recognized, yet all budgets are warnings and critical orchestrators remain large: Worker 1,822 lines, build 849, setup 816, upgrade 574. | `eslint.config.js`; `docs/adr/0016-adopt-complexity-budget.md`; [matrix](../../controls/quality/change-safety-matrix.md) | High for source/raw line counts; warning counts were not executed. | Knowledge concentration inside long orchestration files raises modification and review cost, especially after maintainer departure. |
| The most operationally sensitive repositories have the weakest executed/public quality evidence. | [E-010](../../evidence/evidence-ledger.md), [matrix](../../controls/quality/change-safety-matrix.md) | High for public records; external/private automation unknown. | Terraform or live-instance changes can bypass the product repository’s strong test discipline. |
| Website/documentation quality is materially weaker than product-code quality: no npm lockfile, no hosted package checks, and inconsistent version manifests. | [E-012](../../evidence/evidence-ledger.md), [delivery packet](../../evidence/packets/delivery-and-quality.md) | High for cutoff source; no build executed. | The primary onboarding/operations source can drift or fail even while hosted workflows stay green. |
| The public instance snapshot is on 3.6.3 while latest cutoff product release is 3.7.0 and its upgrade-nudge workflow is inactive. | `v8s-link/package.json`; [E-009/E-010](../../evidence/evidence-ledger.md); recovery packet | High for pinned source; no live deployment equivalence. | The reference instance can diverge from the product and mislead maintainers unless upgrade state is actively verified. |

### Decision Insights

- **Use the product check as a takeover prerequisite, not as readiness proof from source alone.** Its breadth is a strength, but missing dependency state and no clean successor run leave the harmful onboarding question unanswered. Smallest proof: OI-004 with exact pass/fail/error/skip and tool versions.
- **Extend existing quality discipline to `v8s-config`, `v8s-link`, and `website` before adding new product tests.** Current risk is cross-repository asymmetry, not absence of product test source. Smallest action: OI-007/OI-008.
- **Make complexity reduction an incremental ratchet, not a rewrite.** Critical behavior already has broad tests, and ADR 0016 explicitly supports decomposition when modules are touched. A large rewrite would increase handover risk. Smallest action: OI-009, converting selected budgets from warnings after focused extraction.

## Selected Outputs

The material regression and safe-change question triggered the [change-safety matrix](../../controls/quality/change-safety-matrix.md), including explicit execution accounting and cross-repository gaps.

## Material Omissions, Unknowns, And Stakeholder Questions

- Exact local results, tool versions, duration, coverage, and flaky-test behavior: not available because dependencies were absent and execution/installation was not approved.
- Whether public hosted checks were required for merge and whether the pinned main release commit passed the complete gate: authenticated enforcement and complete population evidence are unavailable.
- Whether `lnk` commit/push behavior, Terraform changes, website builds, and instance upgrades work on a clean non-creator machine: OI-004/OI-007/OI-008.
- Whether the 3.6.3 reference snapshot was deployed or intentionally held behind 3.7.0: unknown.

## Reconciliation

The product’s large files are not treated as defects solely because of size; the repository itself records complexity as a recognized warning-level budget. Broad test source and hosted successes reduce confidence in a “poor code quality” claim, while absence of execution and cross-repository gates prevents a “proven safe” claim. Hosted run statuses are not converted into test counts.

## Bounded Conclusion And Downstream Guidance

The core product code is thoughtfully tested and has a credible integrated quality design. Its largest weakness is not careless code; it is uneven enforcement and evidence across the whole operating system, plus concentrated complexity in critical orchestration. Security and Scalability may use tested-behavior areas as source evidence; Business Continuity and Maintenance Cost may use execution, complexity, and cross-repository gaps. No downstream reviewer may claim tests passed locally, coverage exceeded any threshold, production is correct, or operational repositories are safe.
