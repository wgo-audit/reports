# Change-Safety Matrix

## Evidence Boundary

Evidence is cutoff-pinned source plus public hosted records through July 22, 2026. Local dependency directories were absent and installation/execution was not approved. No test, build, lint, format, Terraform, deploy, coverage, mutation, load, or runtime command was run.

## Declared And Observed Quality Position

| Change area | Source-declared safety evidence | Public hosted evidence | Material limitation | Change-safety position |
|---|---|---|---|---|
| Worker routing, headers, Access, lifecycle, schedules, analytics | `scripts/workers/worker.test.mjs` is 1,741 lines and exercises response, header, registry, schedule, Access, lookup, CORS, and analytics cases | Included in `npm run check`; exact successful check runs exist for named commits/PR heads | No local run, line/branch coverage, production request, or audited-commit run result | Strong source test intent; executed correctness not established |
| Registry, links, policy, targets | Registry, first-party links, target normalizer/checker, and policy-related assertions across focused scripts | Included in product check workflow | Network target checks have external variability; no current execution or coverage result | Credible unit/integration-oriented source coverage; effectiveness unmeasured |
| Setup, install, detach, upgrade | Dedicated install/core, detach, upgrade-source, upstream-release, and maintenance test scripts | Included in product check workflow | No clean-machine/non-creator execution; upgrade may install dependencies and execute refreshed code | Material continuity paths have source tests but need an isolated successor exercise |
| Build, HTML, localized/public pages | Build-site-core/build-html-core/install/maintenance tests plus build within `check` | Included in product check workflow | `scripts/build.mjs` is 849 lines; rendered output/accessibility not independently accepted | Good regression surface, with concentrated orchestration risk |
| CLI/Git write workflow | CLI libraries share validators; check-target/maintenance paths are tested | Broad check exists | No dedicated end-to-end `lnk` add/replace/commit/push exercise found; external Git credentials/rollback untested | Operator-critical write path remains only partly evidenced |
| Complexity/maintainability | ESLint/Sonar budgets for complexity, depth, file/function length, parameters; ADR 0016 | Runs under product `lint`/`check` | All budgets are warnings; 1,822-line Worker, 849-line build, 816-line setup, 574-line upgrade exceed the 400-line budget by raw line count | Risk is visible but non-blocking and concentrated in critical orchestrators |
| Product repository dependencies | npm lockfile v3 with 102 package entries; Dependabot and dependency-review workflow | Selected dependency-review runs succeeded | No local restore, vulnerability result, SBOM, or complete-run review | Reproducible dependency intent; current risk not independently measured |
| `v8s-link` instance | Same 14-part declared suite and lockfile as product snapshot | No public Actions/PR/release history | Snapshot is 3.6.3 while latest cutoff product release is 3.7.0; no active upgrade nudge or check | Runtime instance change safety is not publicly demonstrated |
| Terraform control plane | Version/provider constraints, provider lock, README commands | No public Actions/PR/release history | No test fixtures/modules, format/validate/plan result, applied-state comparison, or policy check | Critical infrastructure changes lack public automated evidence |
| Website/documentation | Declared build, Worker test, format, Markdown/YAML/spell/link checks | Hosted workflows do not run package quality commands | No npm lockfile; no hosted quality gate; manifest/package versions differ | Operator source of truth has weak reproducibility/change safety |

## Execution Accounting

| Scope | Pass | Fail | Error | Skipped | Boundary |
|---|---:|---:|---:|---:|---|
| Local checks/tests | 0 | 0 | 0 | 0 | Not executed; missing dependency directories and no installation/execution approval |
| Hosted samples | Not aggregated as test cases | Not aggregated as test cases | Not aggregated as test cases | Not available | Workflow-run conclusions remain in [delivery packet](../../evidence/packets/delivery-and-quality.md); run status is not a test-case count |

## Closure Routes

- OI-004: clean non-creator setup/check/change/upgrade/deploy/rollback exercise with exact results.
- OI-007: automated review/validation for Terraform and instance repositories.
- OI-008: locked, hosted website quality gate.
- OI-009: enforce a complexity ratchet and decompose critical orchestration when touched.
