# Feature-Level Contribution Value Evidence Packet

## Scope And Evidence Boundary

- **Reader question:** Which contributors have source-supported, outcome-relevant feature value, and how concentrated is that value across the project lifetime and consecutive cutoff-anchored 12-month periods?
- **Evidence cutoff:** 2026-08-19.
- **Approved sources and actions:** Complete public Git history and tags for `HC-CODE-001` at `fafac59eeb00cfdc87166242544fa071ecad1723`; repository changelog; linked public issues, pull requests, and commits; completed Product Value and Business Continuity evidence only for outcome context.
- **Exclusions and sensitivity:** No personnel sources, private data, unrelated repositories, performance inference, or CodeGraph. Pull-request review/comment metadata was unavailable. Outcomes are implemented, not demonstrated or Acme-approved.

## Observations

| Observation | Source type and exact locator | Observed/effective time | What it establishes | Limitation |
|---|---|---|---|---|
| Complete local history | `HC-CODE-001` Git history, root `00cdc313eca85a5a2bc68e77fc7dcef5f72eadfc`, cutoff `fafac59eeb00cfdc87166242544fa071ecad1723` | 2015-06-11 through 2026-08-19 | The fetched public history contains 3,913 commits and spans every required annual window. | Commit volume is history coverage, not value or performance. |
| Supported feature-level set | [Contribution-value assessment](../../controls/contributors/contribution-value.md#featurechange-units) | Assessed 2026-08-19 | Twenty-three coherent units, each with outcome, magnitude, quality, direct contribution, and confidence, total 118 within-audit feature-value units. | Deliberately selective evidence set; not an exhaustive project catalog. |
| Lifetime supported concentration | [Lifetime table](../../controls/contributors/contribution-value.md#project-lifetime-top-80-contributors) | Assessed 2026-08-19 | Pēteris Caune has 69/118 supported units (58.5%). Six contributors are needed to cross 80%; a six-way tie makes the last four names non-unique. | The result ranks supported units, not people or all project work. |
| Consecutive annual coverage | [Annual tables](../../controls/contributors/contribution-value.md#cutoff-anchored-12-month-periods) | Assessed 2026-08-19 | Every full cutoff-anchored 12-month window and the founding partial window contains supported maintainer-authored value plus material external units where evidence supports them. | Two sampled units per full window make annual long-tail totals unsuitable as project-wide estimates. |
| External value exists | PRs/issues #9, #86, #140, #272, #370, #484, #722, #901, #990, #1177 and linked commits in the assessment | 2015-2026 | External contributors delivered material alert concurrency, configuration, webhook, integration, API, role, run-correlation, and notification-group changes, often with tests. | Episodic feature delivery does not establish ongoing stewardship or successor capacity. |

## Material Unknowns And Access Limits

- Review approvals, private design work, issue authorship, co-authorship, operational work, and uncredited work are unavailable.
- Git identity normalization is limited. Pēteris Caune's two historical emails were collapsed based on exact name and repository continuity; Git has no `.mailmap`.
- Direct public API access failed for the collector. The reviewer separately obtained public repository and contributor-index responses, used only as identity/history corroboration.
- The SMTP implicit-TLS unit and founding range have no recovered PR/issue association; commit/range evidence is retained without inventing one.
- Product and continuity evidence does not show that any contributed unit delivers Acme's five-minute human-alert, 30-minute RTO, or five-minute RPO targets.

## Reuse Guidance

Use this packet to establish that long-lived direct-maintainer concentration and material episodic external contribution coexist. Do not call the values performance, infer a bus factor from commit counts, claim exhaustive project-wide top-80 coverage, or conclude that community history proves Acme can maintain a fork.
