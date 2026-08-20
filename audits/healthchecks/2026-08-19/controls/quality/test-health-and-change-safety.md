# Test Health And Change-Safety Assessment

## Scope And Evidence Boundary

This control evaluates the declared quality gates and the change-safety evidence
for `HC-CODE-001` commit `fafac59eeb00cfdc87166242544fa071ecad1723`.
It separates upstream hosted results, source inspection, and local execution.
None of these proves an Acme deployment, a live notification provider, a
responsible human receiving an alert, or the five-minute outcome.

Evidence: E-009 through E-013 in the
[evidence ledger](../../evidence/evidence-ledger.md).

## Quality-Control Inventory

| Control | Type, declaration, and trigger | Intended coverage | Observed result at pinned commit | Enforcement and limit |
|---|---|---|---|---|
| Django test matrix | Repository-declared CI gate: `HC-CODE-001:.github/workflows/tests.yml`; push and pull request to `master`; SQLite, PostgreSQL, MySQL, and MariaDB across Python 3.12, 3.13, and 3.14 | Python application, database compatibility, API/UI server behavior, integrations | 12 of 12 hosted jobs passed; each ran 1,750 tests: 21,000 passed, 0 failed, 0 errors, 0 skipped | Workflows run on push as well as pull request. Public evidence did not establish that a successful run is required before `master` or release publication. |
| Coverage | Repository-declared CI gate: `HC-CODE-001:.github/workflows/coverage.yml`; push and pull request to `master`; Python 3.12 and default SQLite | Statement coverage for `hc`, excluding tests and migrations | One hosted run passed 1,750 tests and submitted coverage. With `master` still at the pinned commit, Coveralls reported 92% `hc` statement coverage, excluding migrations. Totals: 1,750 passed, 0 failed, 0 errors, 0 skipped | The workflow has no configured minimum threshold and its log does not retain a numeric report; the badge is externally served. Coverage does not express path, fault, or requirement coverage. |
| Strict mypy | Repository-declared CI gate: `HC-CODE-001:.github/workflows/mypy.yml`; push and pull request to `master`; Python 3.12 | Static typing for `hc` | Hosted job passed: no issues in 652 source files | No evidence that it blocks direct pushes or releases. Type success is not behavior evidence. |
| Ruff style | Manual contributor control: `HC-CODE-001:CONTRIBUTING.md:20-27` | Python formatting and, by commit convention, lint warnings | Local Ruff 0.9.4: `ruff check .` found 2 violations; `ruff format --check .` found 648 formatted files and 5 that would be reformatted | No Ruff version, rule/config file, canonical command, dependency declaration, or CI job is present. Result is not reproducible enough to be an authoritative upstream gate. |
| Documentation generation | Manual contributor control: `HC-CODE-001:CONTRIBUTING.md:29-37`; `./manage.py render_docs` | Keep Markdown source and committed HTML fragments synchronized | Not executed: Django dependencies are absent and installation is not authorized | No CI drift check was found. The generated fragments and instrumentation examples can diverge from source documentation. |
| Docker publication | Repository-declared release control: `HC-CODE-001:.github/workflows/publish_docker_image.yml`; release publication or manual dispatch | Configured to build and push `linux/amd64`, `linux/arm/v7`, and `linux/arm64/v8` images and request an SBOM when triggered | No run was triggered for the pinned non-release commit; 0 build jobs passed, failed, errored, or skipped | The workflow does not explicitly depend on the Tests, Coverage, or Mypy workflows. It publishes when independently triggered; source-visible enforcement is absent. |
| CodeQL default setup | GitHub-hosted dynamic control, not stored in the pinned tree | Static analysis of Python, Actions, and JavaScript/TypeScript | 3 of 3 hosted jobs passed | A successful analysis job does not mean no alert exists; alert inventory belongs to Security and Privacy. |

## Executed And Blocked Checks

| Execution context | Command and tool version | Exact outcome | Dependency and authorization state | Bounded conclusion |
|---|---|---|---|---|
| GitHub Actions at the pinned commit | `python manage.py test`; workflow-provisioned Python 3.12/3.13/3.14 and pinned project requirements | Matrix: 21,000 passed, 0 failed, 0 errors, 0 skipped across 12 jobs. Coverage duplicate: 1,750 passed, 0 failed, 0 errors, 0 skipped. Combined hosted test executions: 22,750 passed, 0 failed, 0 errors, 0 skipped. | Dependencies installed by the historical hosted runs | Strong regression evidence for the independently built upstream fixtures and four database engines; not live Acme or provider evidence. |
| GitHub Actions at the pinned commit | `mypy --strict --show-traceback hc`; workflow installed mypy 2.3.1 from `requirements-dev.txt` | 652 source files checked; 0 issues; job passed | Dependencies installed by hosted run | Static type gate was green at the pinned source. |
| Local approved checkout `HC-CODE-001:./` | `/usr/bin/env SECRET_KEY=dummy-key python3 manage.py test`; Python 3.14.6 | Execution did not start: `ModuleNotFoundError: django`. Test totals: 0 passed, 0 failed, 0 errors, 0 skipped. | Django absent; installing/restoring dependencies was not authorized | No local behavior result. |
| Local approved checkout `HC-CODE-001:./` | `coverage run --omit=*/tests/*,*/migrations/* --source=hc manage.py test`; Coverage.py 7.13.2, Python 3.13.11 | Execution did not start: `ModuleNotFoundError: django`; no data collected. Test totals: 0 passed, 0 failed, 0 errors, 0 skipped. | Django absent; installing/restoring dependencies was not authorized | Local numeric coverage is blocked. Hosted measurement is separately reported. |
| Local approved checkout `HC-CODE-001:./` | `mypy --strict --show-traceback hc`; mypy 1.19.1 | Checking did not start: missing `mypy_django_plugin`; 0 source files checked, 1 invocation/configuration error | django-stubs plugin absent; installing dependencies was not authorized | No local type result; hosted mypy is separate evidence. |
| Local approved checkout `HC-CODE-001:./` | `ruff check .`; Ruff 0.9.4 | Failed with 2 findings: E741 and F403 | Tool already present; project does not pin Ruff or its rule set | Demonstrates non-reproducible contributor guidance, not a proven regression. |
| Local approved checkout `HC-CODE-001:./` | `ruff format --check .`; Ruff 0.9.4 | Failed: 648 files formatted, 5 would reformat, 0 errors, 0 skipped | Tool already present; project does not pin Ruff | Demonstrates non-reproducible contributor guidance, not authoritative style status. |
| Local approved checkout `HC-CODE-001:./` | CodeGraph 1.5.0 `status`, `query`, `impact`, and `affected` with the required absolute root/`--path` | Index pass: 701 files, 7,177 nodes, 19,074 edges. `process_one_flip` traced to one direct test; `sendalerts.py` mapped to two test files. | Existing up-to-date index; no installation | Critical source and test relationships are traceable; this does not execute them. |

## Fixture Provenance And Critical-Path Coverage

Fixture provenance is **independently-built**. `HC-CODE-001:hc/test.py` creates
synthetic users, projects, keys, and membership data; transport tests construct
synthetic checks/flips and mock network calls. No production-generated fixture
or Acme job corpus was found in the approved source. Acme fixture provenance is
therefore **unknown**.

The green suite credibly covers schedule and grace calculations, ping handling,
database-backed state, API/UI server behavior, notification payload creation,
transport retry/error handling, and four database engines. The pinned commit's
one-file webhook change maps to a dedicated webhook test file, and the full
matrix passed.

The green suite does not cover a worker crash after `Flip.processed` is set,
durable alert redelivery/requeue, concurrent failure bursts and queue dwell,
live provider delivery, end-to-end human receipt, Acme job wrappers, Windows
Task Scheduler behavior, restore/rollback from a prior production-shaped
database, or the `T1 - T0 <= 300 seconds` measurement contract. The source
defaults to one worker, processes a flip's channels sequentially, and permits
up to three 30-second attempts for one HTTP channel. Those proven mechanics
consume and can queue within the 300-second budget; they do not prove an
observed miss. OI-006 fault/T0-T1 evidence is therefore a production stop
condition. Tests duplicate
transport request/response shapes as synthetic dictionaries and mocks; live
provider contract drift remains outside their evidence boundary.

## Change-Safety Matrix

| Change surface | Existing evidence | Material gap | Pull implication | Make implication | Required control |
|---|---|---|---|---|---|
| Ping, schedule, and state calculation | Dense Django tests; four-database matrix; Coveralls-reported 92% `hc` statement coverage, excluding migrations | No Acme schedule/job corpus or Windows acceptance test | Pin a reviewed release and run Acme-owned contract cases before promotion | Fork changes require upstream suite plus the same Acme contract pack | OI-001 and OI-008 in the [open-items register](../open-items.md) |
| Alert claim and notification dispatch | Unit/functional tests verify flip creation, processed marking, channel failure metrics, and mocked transport retries | No crash-after-claim, durable redelivery, burst, live-provider, or human-receipt test | Do not treat upstream green CI as five-minute/no-silent-loss proof; OI-006 is a production stop condition | A fork is justified only after operational controls fail measured acceptance and the source defect is isolated | OI-006 and OI-008 in the [open-items register](../open-items.md) |
| Database migrations and upgrades | Fresh test databases are created across four engines | Coverage excludes migrations; no prior-release data upgrade, rollback, or restored-backup rehearsal | Gate every selected release through migration/recovery rehearsal | Every fork merge increases the migration compatibility matrix | OI-007 and OI-008 in the [open-items register](../open-items.md) |
| Browser-side configuration UI | Django view/template tests and hosted JavaScript CodeQL | No JavaScript test/build manifest or browser behavior gate was found for 35 tracked root JavaScript files | If Acme uses the UI operationally, include critical monitor-configuration browser flows in acceptance tests | Forked UI changes create a new test-harness obligation if Acme relies on those flows | OI-008 in the [open-items register](../open-items.md) |
| Release artifact | Release-triggered workflow configured for multi-architecture images and an SBOM request | No source-visible dependency on green tests/type/coverage; branch enforcement was not established | Promote immutable image digests only after Acme-owned gates pass | Fork owner must implement and operate the complete promotion gate | OI-008 in the [open-items register](../open-items.md) |
| Documentation and job snippets | Markdown and committed generated fragments; manual render command | No automated drift gate; client examples are not Acme wrapper acceptance tests | Validate Acme's supported wrapper separately; do not rely on snippets as tests | Fork owner must prevent doc/generated-fragment drift | OI-008 in the [open-items register](../open-items.md) |

## Decision Boundary

The evidence supports **pull before make** for code ownership: upstream has a
broad, green regression base and the pinned change has a mapped test surface.
It does not support direct production promotion. Pull requires an Acme-owned
acceptance/promotion gate plus OI-006 and OI-007. Make adds responsibility for
the full matrix, browser/doc gaps, provider contract maintenance, migration
compatibility, and upstream merge validation. Buy is not covered by these
source tests; hosted runtime and five-minute evidence remain separate.
