# Code Quality Evidence Packet — CI, Test, And Release Gates

Pinned source: `docuseal/` tag `3.1.7`, commit `a2d8b855491793870b7b4acf176d2d95ae95ff83`. Observed 2026-08-06. This packet records declared gates and bounded hosted/local execution evidence; it does not establish production correctness or release approval.

## Declared Gate Inventory

| Gate | Exact declaration | Declared command / behavior | Pinned hosted result | Boundary |
|---|---|---|---|---|
| Ruby style/static lint | `docuseal/.github/workflows/ci.yml:6-29` | `bundle exec rubocop`, Ruby 4.0.5 | GitHub Actions tag run `30804591585`: successful | Hosted job success only; branch-protection/required-check state unavailable. |
| ERB lint | `docuseal/.github/workflows/ci.yml:31-54` | `bundle exec erb_lint ./app`, Ruby 4.0.5 | Successful | Does not execute rendered behavior or accessibility checks. |
| JavaScript lint | `docuseal/.github/workflows/ci.yml:56-81` | ESLint over `app/javascript/**/*.js`, Node 20.19.0 | Successful | The glob excludes all `.vue` files. The separate package script includes JS/Vue but uses `--fix` (`package.json:70-74`) and is not the CI gate. |
| Rails static security scan | `docuseal/.github/workflows/ci.yml:83-109`; `config/brakeman.ignore:1-28` | `bundle exec brakeman -q --exit-on-warn` with six committed ignores | Successful | Brakeman is not dependency, secret, container, dynamic, or penetration testing. Ignore rationales are concise assertions, not independently reviewed evidence. |
| Database/assets/spec suite | `docuseal/.github/workflows/ci.yml:111-179` | PostgreSQL 14; database create/migrate; assets precompile; RSpec; Chrome 125; `COVERAGE=true` | Successful | No example/pass count, coverage artifact/percentage, browser matrix, or runtime result was available in the shared packet. |
| Tag image publication | `docuseal/.github/workflows/docker.yml:1-49` | On `*.*.*`, build and push AMD64/ARM64 image | Run `30804590741`: successful | Workflow has no dependency on CI jobs and no visible test, vulnerability, signature, SBOM, attestation, or post-publish verification gate. |

The CI workflow runs on every push (`ci.yml:2-3`), while the image workflow separately runs on a matching tag (`docker.yml:3-6`). No `needs`, reusable workflow, environment approval, or other source-visible ordering binds image publication to successful CI. Repository branch rules and protected settings were inaccessible, so enforcement outside these files is unknown.

## Dependency State And Executable Checks

All commands below used exact working directory `/Users/patrick/Library/CloudStorage/OneDrive-Drolet/wip/wgo/wgo-docuseal/docuseal`. No installation or restore was authorized or attempted.

| Command | Intent | Tool/dependency state | Result | Counts / bounded conclusion |
|---|---|---|---|---|
| `ruby --version` | Check required runtime availability | Host Ruby available | Pass: `ruby 2.6.10p210` | Dependency preflight only; project requires Ruby 4.0.5 (`Gemfile`, `Gemfile.lock`, CI). |
| `bundle --version` | Check locked Bundler availability | `/usr/bin/bundle` present; locked Bundler 4.0.3 absent | Error: `Gem::GemNotFoundException` | Dependency preflight only. |
| `node --version` | Check frontend runtime availability | Host Node available | Pass: `v25.3.0` | Dependency preflight only; CI declares Node 20.19.0. |
| `yarn --version` | Check locked frontend installer availability | Yarn absent | Error: command not found | Dependency preflight only. |
| `bundle check` | Check installed Ruby dependency set without restoring | Bundler 4.0.3 absent; `vendor/bundle` and `.bundle` absent | Error: `Gem::GemNotFoundException` | Dependency preflight only. |

`node_modules`, `vendor/bundle`, `.bundle`, and `tmp/cache` were absent. Therefore local quality checks executed: **0**; passed: **0**; failed: **0**; errored: **0**. The five application CI gates (RuboCop, ERB lint, ESLint, Brakeman, and RSpec/assets) were not runnable with the available dependencies/runtimes. The Docker publication check was neither preflighted nor attempted locally and remains separate. Installation authorization: not granted. Coverage: **unmeasured**.

Hosted evidence is separate: all five declared CI jobs were visible and passed, and one Docker publication job passed for the pinned tag. The packet does not expose RSpec example pass/fail/error/pending counts or coverage. Hosted green status must not be generalized beyond those configured jobs.

## Coverage Configuration

The RSpec job exports `COVERAGE=true` (`ci.yml:169-179`), but `spec/rails_helper.rb:3-18` loads the Rails application before only requiring `simplecov`. No `SimpleCov.start`, minimum threshold, refuse-drop control, or coverage artifact/upload is present in the pinned source. Accordingly, the repository does not provide measured coverage evidence for this audit; the green job is not evidence of any percentage.

## Release Reproducibility Boundary

The CI jobs use action tags rather than immutable SHAs and use `browser-actions/setup-chrome@latest` (`ci.yml:11-17,36-42,61-69,88-94,131-148`). Dependency installation uses unpinned `gem install bundler` and `yarn install` without a frozen-lockfile gate (`ci.yml:23-27,76-81,100-107,156-168`). The container build also runs `yarn install` without a frozen-lockfile flag and downloads several build inputs without checksum validation (`Dockerfile:1-18,20-45`); PDFium is the exception, with architecture-specific SHA-256 checks at `Dockerfile:12-18`. These are observed reproducibility boundaries, not proof that the pinned successful build used altered inputs.

## History Target

For rationale and enforcement, target `.github/workflows/ci.yml`, `.github/workflows/docker.yml`, `spec/rails_helper.rb`, and `Dockerfile`; the shared GitHub packet preserves the exact pinned run identifiers and inaccessible branch/settings limitations.
