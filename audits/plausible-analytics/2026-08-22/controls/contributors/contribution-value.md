# Contributor Value Assessment

## Evidence Boundary And Attribution Rules

- Audit cutoff: 2026-08-22 22:08:28 EDT.
- Included source types: `primary-code` Git history through `9cc669b97ece3ecd37fcb3950791cb3873d7944d`; targeted public PR, review, commit, source, and test records in the approved `plausible/analytics` repository; Product Value evidence only for outcome context.
- Excluded/inaccessible source types: private design, support, incident, account, staffing, contract, acceptance, customer-outcome, vendor, and production records; separately referenced repositories. Public metadata was accessible for the selected PRs. No source-visible test was executed for this reviewer.
- Feature grouping rule: fifteen deliberately selected coherent change units span all seven consecutive cutoff-anchored periods. Linked PRs are grouped only when they implement one bounded capability in the same period. This is a feature-level sample, not an inventory of all project work.
- Attribution rule: the PR author receives implementation/testing credit; a reviewer receives a bounded share only where a changes-requested record and author-confirmed revision show material effect. Approval, merge, comment, PR count, commit count, and line volume earn no credit by themselves. Composite shares reflect documented functional responsibility, not time or performance. GitHub handles are identifiers only; legal identity, employment/vendor status, account control, ownership, and off-platform contribution remain unknown.

Value bands are `critical = 8`, `high = 5`, `meaningful = 3`, `bounded = 2`, and `minor = 1`. They order source-visible product outcomes inside this audit; they are not universal productivity scores. Confidence is high for dates, authors, paths, and the two credited review records, and medium for outcome band and functional-share judgments because no live/customer evidence was approved ([E-073–E-076](../../evidence/evidence-ledger.md)). Evidence/open-item links in these outputs intentionally open the canonical table file because table rows do not provide Markdown anchors; the link label identifies the exact row.

## Feature/Change Units

| Unit | Outcome and value band | Task magnitude | Delivery quality | Credited contributors and share | Evidence | Confidence/limit |
|---|---|---|---|---|---|---|
| CV-01 — Realtime dashboard (2019-09-02–2020-08-22 available history) | Implemented current-visitor/realtime dashboard and stats-query path; **high = 5** | M | Merged source and query/controller tests | `ukutaht` 100% implementation/testing | [PR #212](https://github.com/plausible/analytics/pull/212), `232298d3`; `primary-code:assets/js/dashboard/realtime.js`; `primary-code:lib/plausible/stats/query.ex`; stats controller tests; [E-074](../../evidence/evidence-ledger.md) | High identity/change confidence; no runtime or user-outcome proof |
| CV-02 — Self-hosted support (same period) | Implemented hosting/configuration, release, auth, billing, and stats improvements; **meaningful = 3** | M | Merged source plus controller/domain tests | `tckb` 100% implementation/testing; merge commit records Chandra Tungathurthi as author | [PR #209](https://github.com/plausible/analytics/pull/209), `f7b37fe9`; historical `HOSTING.md`, `config/releases.exs`, `lib/plausible_release.ex`; [E-074](../../evidence/evidence-ledger.md) | High PR↔commit confidence; not a complete CE capability or acceptance record |
| CV-03 — Advanced dashboard filtering (2020-08-23–2021-08-22) | Implemented manual/editable/suggested, negated/glob path filters and filter groups; **high = 5** | M | Merged source/tests; one substantive changes-requested review altered product/UI/request behavior before merge | `Vigasaurus` 54% implementation; `ukutaht` 40% filter-group implementation and 6% evidenced review/design | [PR #1121](https://github.com/plausible/analytics/pull/1121), [review](https://github.com/plausible/analytics/pull/1121#pullrequestreview-681781219), `30ac9011`; [PR #1167](https://github.com/plausible/analytics/pull/1167), `0de89bad`; filter and suggestions source/tests; [E-074](../../evidence/evidence-ledger.md) | High direct-credit confidence; share between linked responsibilities is a medium-confidence audit judgment |
| CV-04 — Google Analytics import refactor (2021-08-23–2022-08-22) | Refactored import API, buffering, report processing, and imported-site behavior; **high = 5** | M | Merged API/buffer/VCR/imported-data tests | `vinibrsl` 100% implementation/testing | [PR #2046](https://github.com/plausible/analytics/pull/2046), `4b9032d8`; `primary-code:lib/plausible/google/api.ex`; historical buffer/report/imported-site source and tests; [E-074](../../evidence/evidence-ledger.md) | High source-history confidence; imported outcome and customer value not observed |
| CV-05 — Stats API breakdown semantics (same period) | Improved public Stats API breakdown behavior; **meaningful = 3** | S | Merged controller test | `RobertJoonas` 100% implementation/testing | [PR #1759](https://github.com/plausible/analytics/pull/1759), `e5cf800d`; historical Stats base/breakdown and external controller tests; [E-074](../../evidence/evidence-ledger.md) | High direct-credit confidence; bounded API unit, not whole API ownership |
| CV-06 — Custom-property revenue/report/export work (2022-08-23–2023-08-22) | Implemented private value lookup, revenue/property reporting, and CSV output; **high = 5** | M | Merged controller/CSV tests; one substantive change request produced an author-confirmed revision | `RobertJoonas` 80% implementation/testing; `vinibrsl` 15% revenue-breakdown implementation/testing; `aerosol` 5% evidenced review | [#3111](https://github.com/plausible/analytics/pull/3111), [review](https://github.com/plausible/analytics/pull/3111#pullrequestreview-1525665679), [revision discussion](https://github.com/plausible/analytics/pull/3111#discussion_r1262887593); [#3140](https://github.com/plausible/analytics/pull/3140); [#3167](https://github.com/plausible/analytics/pull/3167); [#3209](https://github.com/plausible/analytics/pull/3209); [#3261](https://github.com/plausible/analytics/pull/3261); corresponding source/tests; [E-075](../../evidence/evidence-ledger.md) | High direct-credit confidence; medium functional-share judgment |
| CV-07 — Stats API intervals (same period) | Implemented interval support across query/timeseries/imported paths; **meaningful = 3** | M | Merged interval/imported/query/timeseries/controller tests | `vinibrsl` 100% implementation/testing | [PR #2417](https://github.com/plausible/analytics/pull/2417), `9c98a3f2`; historical interval/query/timeseries source and tests; [E-075](../../evidence/evidence-ledger.md) | High source-history confidence; runtime semantics not exercised here |
| CV-08 — Plugins API foundation (2023-08-23–2024-08-22) | Implemented token schema/authorization plus shared-link and goal resources/specification; **high = 5** | M | Merged domain, plug, controller, schema, and spec tests | `aerosol` 100% implementation/testing | [#3370](https://github.com/plausible/analytics/pull/3370), [#3373](https://github.com/plausible/analytics/pull/3373), [#3378](https://github.com/plausible/analytics/pull/3378), [#3396](https://github.com/plausible/analytics/pull/3396); `primary-code:lib/plausible/plugins/api/`; [E-075](../../evidence/evidence-ledger.md) | High direct-credit confidence; does not establish live use or whole-API ownership |
| CV-09 — Public Stats/Sites API expansion (same period) | Added conversion-rate semantics, invalid-filter rejection, imported-data warning, and authorization refactor; **high = 5** | M | Merged external API and authorization tests | `RobertJoonas` 40%; `macobo` 30%; `zoldar` 30% for distinct documented responsibilities | [#3739](https://github.com/plausible/analytics/pull/3739), [#3986](https://github.com/plausible/analytics/pull/3986), [#4116](https://github.com/plausible/analytics/pull/4116), [#4297](https://github.com/plausible/analytics/pull/4297); `primary-code:lib/plausible_web/controllers/api/external_stats_controller.ex`; [E-075](../../evidence/evidence-ledger.md) | High direct-credit confidence; medium functional-share judgment; no API outcome observation |
| CV-10 — Tracker Script v2 support (2024-08-23–2025-08-22) | Implemented installation diagnostics, configurable API, package distribution, and EE cache behavior; **high = 5** | M | Merged backend, tracker, and Playwright-oriented tests | `apata` 60% verification/configuration/diagnostics; `macobo` 40% cache/distribution | [#5572](https://github.com/plausible/analytics/pull/5572), [#5607](https://github.com/plausible/analytics/pull/5607), [#5620](https://github.com/plausible/analytics/pull/5620), [#5627](https://github.com/plausible/analytics/pull/5627), [#5648](https://github.com/plausible/analytics/pull/5648); tracker/config/cache source and tests; [E-076](../../evidence/evidence-ledger.md) | High direct-credit confidence; medium functional-share judgment; package publication/uptake unproved |
| CV-11 — SSO audit trail (same period) | Implemented persisted/listed SSO audit entries; **meaningful = 3** | M | Merged audit, SSO, domain, and worker tests | `aerosol` 100% implementation/testing | [PR #5560](https://github.com/plausible/analytics/pull/5560), `adf39ca7`; `primary-code:extra/lib/plausible/audit.ex`; `primary-code:extra/lib/plausible/auth/sso.ex`; tests; [E-076](../../evidence/evidence-ledger.md) | High source-history confidence; retention/live assurance not established |
| CV-12 — Dashboard annotations (2025-08-23–2026-08-22) | Implemented feature-gated schema, CRUD/permission backend, React UI, and E2E coverage; **high = 5** | M | Merged backend, JS, controller, and E2E tests | `apata` 100% implementation/testing | [#6478](https://github.com/plausible/analytics/pull/6478), [#6481](https://github.com/plausible/analytics/pull/6481), [#6482](https://github.com/plausible/analytics/pull/6482); `primary-code:lib/plausible/annotations/annotations.ex`; UI/E2E source; [E-076](../../evidence/evidence-ledger.md) | High direct-credit confidence; deployment, entitlement, and customer use unknown |
| CV-13 — Event replay (same period) | Implemented replay-session fields through ingestion, ClickHouse event/session, cache, and gatekeeper paths; **meaningful = 3** | M | Merged ingestion/cache/gatekeeper tests | `zoldar` 100% implementation/testing | [PR #6491](https://github.com/plausible/analytics/pull/6491), `17cfe6d9`; `primary-code:lib/plausible/ingestion/event.ex`; event/session source and tests; [E-076](../../evidence/evidence-ledger.md) | High source-history confidence; replay operation and recovery outcome unobserved |
| CV-14 — Dashboard CSV export v2 (same period) | Implemented new dashboard CSV export surface; **bounded = 2** | M | Merged React, controller CSV, and E2E tests | `RobertJoonas` 100% implementation/testing | [PR #6436](https://github.com/plausible/analytics/pull/6436), `ba238ad3`; `primary-code:assets/js/dashboard/stats/csv-export/csv-export.tsx`; `primary-code:lib/plausible/stats/dashboard/csv_export.ex`; tests; [E-076](../../evidence/evidence-ledger.md) | High source-history confidence; bounded because this is a v2 surface within a larger export contract |

The table contains fourteen rows because CV-06 and CV-08–CV-10 are coherent multi-PR units; the underlying selected history contains thirty-one PR merge records. The supported total is 57 feature-value points. This number measures only this source-bounded sample.

## Project-Lifetime Top-80% Contributors

| Contributor | Attributed feature-value units | Share of supported total | Material feature/change units | Evidence and confidence |
|---|---:|---:|---|---|
| `RobertJoonas` | 11.00 | 19.3% | CV-05, CV-06, CV-09, CV-14 | Direct PR/commit identity high; share judgments medium |
| `vinibrsl` | 8.75 | 15.4% | CV-04, CV-06, CV-07 | Direct PR/commit identity high; composite share medium |
| `aerosol` | 8.25 | 14.5% | CV-06 review, CV-08, CV-11 | Direct PR/review evidence high; review allocation medium |
| `apata` | 8.00 | 14.0% | CV-10, CV-12 | Direct PR/commit identity high; composite share medium |
| `ukutaht` | 7.30 | 12.8% | CV-01, CV-03 implementation/review | Direct PR/review evidence high; composite share medium |
| `zoldar` | 4.50 | 7.9% | CV-09, CV-13 | Direct PR/commit identity high; composite share medium |

This is the smallest set reaching approximately 80%: 47.80 of 57 supported points, or 83.9%. The long tail is `macobo` 3.50, `tckb` 3.00, and `Vigasaurus` 2.70: 9.20 points, or 16.1%. It does not mean these accounts are the top contributors to the whole project or that omitted work has zero value.

## Cutoff-Anchored 12-Month Periods

### 2025-08-23 to 2026-08-22

| Contributor | Attributed feature-value units | Share of supported period total | Material feature/change units | Evidence and confidence |
|---|---:|---:|---|---|
| `apata` | 5.00 | 50.0% | CV-12 | Direct PR/commit identity high |
| `zoldar` | 3.00 | 30.0% | CV-13 | Direct PR/commit identity high |

Smallest set reaches exactly 80% of 10 supported points. Long tail: `RobertJoonas` 2.00 (20.0%), CV-14.

### 2024-08-23 to 2025-08-22

| Contributor | Attributed feature-value units | Share of supported period total | Material feature/change units | Evidence and confidence |
|---|---:|---:|---|---|
| `apata` | 3.00 | 37.5% | CV-10 | Direct PR identity high; composite share medium |
| `aerosol` | 3.00 | 37.5% | CV-11 | Direct PR identity high |
| `macobo` | 2.00 | 25.0% | CV-10 | Direct PR identity high; composite share medium |

All three are required to cross 80% of 8 supported points; there is no remaining long-tail value in this sample.

### 2023-08-23 to 2024-08-22

| Contributor | Attributed feature-value units | Share of supported period total | Material feature/change units | Evidence and confidence |
|---|---:|---:|---|---|
| `aerosol` | 5.00 | 50.0% | CV-08 | Direct PR identity high |
| `RobertJoonas` | 2.00 | 20.0% | CV-09 | Direct PR identity high; composite share medium |
| `macobo` | 1.50 | 15.0% | CV-09 | Direct PR identity high; composite share medium |

Smallest set reaches 85% of 10 supported points. Long tail: `zoldar` 1.50 (15.0%), CV-09.

### 2022-08-23 to 2023-08-22

| Contributor | Attributed feature-value units | Share of supported period total | Material feature/change units | Evidence and confidence |
|---|---:|---:|---|---|
| `RobertJoonas` | 4.00 | 50.0% | CV-06 | Direct PR identity high; composite share medium |
| `vinibrsl` | 3.75 | 46.9% | CV-06, CV-07 | Direct PR identity high; composite share medium |

Smallest set reaches 96.9% of 8 supported points. Long tail: `aerosol` 0.25 (3.1%), evidenced CV-06 review.

### 2021-08-23 to 2022-08-22

| Contributor | Attributed feature-value units | Share of supported period total | Material feature/change units | Evidence and confidence |
|---|---:|---:|---|---|
| `vinibrsl` | 5.00 | 62.5% | CV-04 | Direct PR identity high |
| `RobertJoonas` | 3.00 | 37.5% | CV-05 | Direct PR identity high |

Both are required to cross 80% of 8 supported points; there is no remaining long-tail value in this sample.

### 2020-08-23 to 2021-08-22

| Contributor | Attributed feature-value units | Share of supported period total | Material feature/change units | Evidence and confidence |
|---|---:|---:|---|---|
| `Vigasaurus` | 2.70 | 54.0% | CV-03 | Direct PR identity high; composite share medium |
| `ukutaht` | 2.30 | 46.0% | CV-03 implementation/review | Direct PR/review evidence high; composite share medium |

Both are required to cross 80% of 5 supported points; there is no remaining long-tail value in this sample.

### 2019-08-23 to 2020-08-22 (partial available history)

Repository history starts 2019-09-02, so 2019-08-23 through 2019-09-01 has no approved repository history.

| Contributor | Attributed feature-value units | Share of supported period total | Material feature/change units | Evidence and confidence |
|---|---:|---:|---|---|
| `ukutaht` | 5.00 | 62.5% | CV-01 | Direct PR identity high |
| `tckb` | 3.00 | 37.5% | CV-02 | Direct PR↔merge identity high |

Both are required to cross 80% of 8 supported points; there is no remaining long-tail value in this sample.

No selected unit crosses a period boundary, so no cross-period apportionment was made.

## Material Unknowns And Closure Routes

- The sample cannot reveal uncredited pair work, design, product direction, support, incident response, operations, documentation outside the approved monorepo, rejected work, or work that never became a linked PR. Do not use the numeric aggregation for performance, staffing, compensation, vendor renewal, or blame.
- GitHub handles/display names are not verified identities, roles, employment/vendor classifications, or account-control evidence. Resolve only the minimum role/knowledge mapping needed for succession, with consent and an accountable source; do not retrospectively score people.
- Source-visible tests accompany every unit, but none ran for this reviewer; other reviewers own test and live-outcome conclusions.
- Period lists show concentration inside the supported sample. They are a reason to verify primary/backup knowledge and access, not proof that any person is indispensable. Use [ownership/successor view](ownership-and-successor.md) and close [OI-022](../open-items.md).
- Actual cost, contract, acceptance, renewal, and vendor value remain unknown. Contributor history is not cost evidence; obtain those facts through [OI-025](../open-items.md) before any vendor or staffing value decision.
