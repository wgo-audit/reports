# Contributor Value Assessment

## Evidence Boundary And Attribution Rules

- **Audit cutoff:** 2026-08-20 at onboarding start, America/Toronto.
- **Included source types:** cutoff-bounded Git commit identity/date/message data, exact selected commit bodies and changed-file/test paths, repository changelog, and Product Value records. See [E-052](../../evidence/evidence-ledger.md#e-052).
- **Excluded/inaccessible source types:** hosted pull-request descriptions, reviews, approvals, issue/discussion activity, contributor profiles, private delivery records, staff evidence, and undocumented work. Some old blobs required a post-cutoff read-only fetch; that action validates already dated commits and does not add post-cutoff work.
- **Feature grouping rule:** eleven coherent, mandate-relevant source change units were selected across the repository lifetime. Related commits are grouped only where release/source context shows one outcome. This is a supported sample, not an exhaustive product history.
- **Attribution rule:** credit follows documented commit authorship or explicit co-authorship plus an evidenced material part of the unit. Shares are bounded reviewer judgements about the selected unit, never commit/PR/line counts. Unsupported review, design, triage, operations, or follow-up credit is excluded rather than guessed.
- **Identity rule:** case-only variants for Uku Taht are consolidated. `Adam Rutkowski` and `hq1` share a source-recorded address but not a stable displayed identity, so the primary lifetime view labels them one ambiguous alias set and shows the alternate result. No email addresses are reproduced.

The bands are only within-audit ordering aids: `critical = 8`, `high = 5`, `meaningful = 3`, `bounded = 2`, `minor = 1`. They do not measure productivity, hours, employment performance, acceptance, ownership, or total project value.

## Feature/Change Units

| Unit | Outcome and value band | Task magnitude | Delivery quality | Credited contributors and share | Evidence | Confidence/limit |
|---|---|---|---|---|---|---|
| Initial analytical foundation | **critical = 8**: initial tracker, pageview/storage/query, and dashboard surfaces form the product foundation on which the reviewed reporting chain depends. | Cross-stack foundation | Implementation is present; no contemporaneous release or test result was inspected. | Uku Taht 100% | [commit `779d64e`](https://github.com/plausible/analytics/commit/779d64e19a26a4e4944d4f0d7d9e280a27fbc6e5); `primary-code:assets/js/plausible.js`; `primary-code:assets/js/stats/index.js`; `primary-code:lib/plausible/tracking.ex`; `primary-code:lib/plausible/stats/query.ex` | Medium; initial snapshot authorship is direct, but the outcome is source-only and uncredited prior/design work is unknowable. |
| Event context and realtime measurement | **meaningful = 3**: event metadata, automatic outbound-link tracking, browser/OS context, and realtime conversion display expand service discovery/interaction measurement. | Multi-surface feature set | Implementation and release notes are present; complete contemporary tests were not available. | Uku 80%; Vignesh Joglekar 20% | [PR #381](https://github.com/plausible/analytics/pull/381), [commit `40900c76`](https://github.com/plausible/analytics/commit/40900c7653684d36135b4955b0a0ccfa6b7a304c); [PR #389](https://github.com/plausible/analytics/pull/389), [commit `f0cbf33d`](https://github.com/plausible/analytics/commit/f0cbf33d7c39216d07051c9fac11862cc4a25457); [PR #500](https://github.com/plausible/analytics/pull/500), [commit `f776c6bb`](https://github.com/plausible/analytics/commit/f776c6bb30a0ee339a86a7997942f70e655133df); `primary-code:CHANGELOG.md:623-638` | Medium; PR URLs come from explicit merged-commit titles, not retrieved PR discussions. |
| Reusable reporting and sharing | **high = 5**: Stats API/API keys, entry/exit-page reporting, and an embeddable dashboard underpin reusable outputs. | Cross-backend/dashboard/API feature set | Direct API/query/controller tests are present. | Uku 75%; Vignesh 25% | [PR #679](https://github.com/plausible/analytics/pull/679), [commit `5acb5b70`](https://github.com/plausible/analytics/commit/5acb5b7039a9cf103a8bb29d6c458405af3ffb0c); [PR #712](https://github.com/plausible/analytics/pull/712), [commit `ff32218b`](https://github.com/plausible/analytics/commit/ff32218bd030f28b0d9ee80dc39952a190d8faab); [PR #812](https://github.com/plausible/analytics/pull/812), [commit `844af698`](https://github.com/plausible/analytics/commit/844af698ce138d31d91207d27447743d593032e1); `primary-code:test/plausible/stats/query_test.exs`; `primary-code:test/plausible_web/controllers/api/external_stats_controller/` | High for source implementation; low for deployed use or acceptance. |
| Analysis controls and role-restricted access | **high = 5**: API/CSV metrics, wildcard/exclusion filters, site-role invitations, and conversion-rate reporting support the source-level reporting/access model. | Cross-feature reporting and access change | Tests are present for the metric, filter, and invitation changes; live assignments remain unknown. | Uku 40%; Vignesh 35%; Ro Savage 25% | [PR #952](https://github.com/plausible/analytics/pull/952), [commit `b1077177`](https://github.com/plausible/analytics/commit/b107717774a83a0449f6eb0ccc9c863eb3f88baf); [PR #1067](https://github.com/plausible/analytics/pull/1067), [commit `b6eeb404`](https://github.com/plausible/analytics/commit/b6eeb40472db77dbb17bb3131222f6d01ec6f841); [PR #1122](https://github.com/plausible/analytics/pull/1122), [commit `e71de6dc`](https://github.com/plausible/analytics/commit/e71de6dc1f0c9a70a743d633dc7b254a7f4f1958); [PR #1299](https://github.com/plausible/analytics/pull/1299), [commit `b3bc796d`](https://github.com/plausible/analytics/commit/b3bc796d504f7fa5607aca33873f32547162189c); [PDR-005](../product/pdr/PDR-005-role-based-dashboard-access.md) | High for source. This unit crosses a 12-month boundary; period allocation uses the dated contributor subcomponents, not an undated split. |
| Historical continuity, graph intervals, and session refresh | **high = 5**: graph intervals, GA import, and a session-cache-store change expand historical/contextual reporting and ingestion continuity. | Broad query/import/session change | Some direct graph and session tests are visible; import breadth is source-evidenced but not runtime-proven. | Uku 50%; Vignesh 35%; Vini Brasil 15% | [PR #1574](https://github.com/plausible/analytics/pull/1574), [commit `497a52c1`](https://github.com/plausible/analytics/commit/497a52c10a38e06b3b3731e03d4ea38f76cf2e24); [PR #1753](https://github.com/plausible/analytics/pull/1753), [commit `e27734ed`](https://github.com/plausible/analytics/commit/e27734ed797b776581e37ec2d22efe88f5b1bca7); [PR #1934](https://github.com/plausible/analytics/pull/1934), [commit `3e569540`](https://github.com/plausible/analytics/commit/3e5695408af74dca9baab77af60c229a36f7b845); `primary-code:CHANGELOG.md:470-511,541-543` | Medium-high. This unit crosses a period; the dated Uku subcomponent is assigned to 2021–22 and the dated Vignesh/Vini subcomponent to 2022–23. Other co-authored import work remains unquantified. |
| Query/import and conversion continuity | **high = 5**: Search Console filtering and a CE imported-data migration improve historical/query usefulness. | Query plus data-migration change | Merged source and release notes are present; complete PR review and all historic test context were unavailable. | Uku 60%; Ruslandoga 40% | [PR #4077](https://github.com/plausible/analytics/pull/4077), [commit `06e8118d`](https://github.com/plausible/analytics/commit/06e8118dab1d202016c353d24871ac19ccc1cd8d); [PR #4155](https://github.com/plausible/analytics/pull/4155), [commit `dc7243ff`](https://github.com/plausible/analytics/commit/dc7243ff2ebcf802b19d58c6b383b3c4ee9de20b); `primary-code:CHANGELOG.md:296-337` | Medium. |
| Multi-site teams, saved segments, and billing role | **high = 5**: membership/invitation actions, segment gating, and a billing role materially extend the multi-site role model. | Cross-domain authorization/product change | Direct controller, LiveView, authorization, and migration tests are present. | Adrian Gruntkowski 45%; Artur Pata 40%; `hq1` 15% | [PR #4977](https://github.com/plausible/analytics/pull/4977), [commit `a45bc1c9`](https://github.com/plausible/analytics/commit/a45bc1c963d06be076298ee4241358c99c307d58); [PR #5129](https://github.com/plausible/analytics/pull/5129), [commit `47b8553c`](https://github.com/plausible/analytics/commit/47b8553ca11903a6109b02c5c34d4bb22e5893fe); [PR #5171](https://github.com/plausible/analytics/pull/5171), [commit `841abf5e`](https://github.com/plausible/analytics/commit/841abf5e538352f7fd3ba7bcf8e3bcd930e8cafa); [PDR-005](../product/pdr/PDR-005-role-based-dashboard-access.md) | High for source; `hq1`/Adam alias status is ambiguous. |
| Automatic form-submission tracking | **meaningful = 3**: tracker collection and goal synchronization add a concrete registration-journey measurement path. | Tracker plus goal integration | Direct tracker form-submission tests are present. | Artur 100% | [PR #5381](https://github.com/plausible/analytics/pull/5381), [commit `9be01236`](https://github.com/plausible/analytics/commit/9be012362c2d12588ed32c93884914b37c390dd2); [PR #5545](https://github.com/plausible/analytics/pull/5545), [commit `3c6db4ef`](https://github.com/plausible/analytics/commit/3c6db4efebaf5d9313e33938689dffcf2ad855eb); `primary-code:tracker/src/` | High for implementation; library instrumentation is unverified. |
| Strict-order funnels, EE-bound | **high = 5**: strict-order schema, settings, computation, and tests implement ordered analysis, but Product Value establishes that this path is not a CE Run outcome. | Cross-stack premium feature | Direct funnel and LiveView tests are present. | Adam Rutkowski 100% | [PR #6237](https://github.com/plausible/analytics/pull/6237), [commit `ea3d23d8`](https://github.com/plausible/analytics/commit/ea3d23d879810ffeb4f4ab1216dcafb390486e9c); `primary-code:extra/lib/plausible/funnel.ex`; `primary-code:extra/lib/plausible/stats/funnel.ex`; [PDR-003](../product/pdr/PDR-003-edition-bounded-journey-analysis.md) | High for EE source; no credit to Run or hosted entitlement. |
| Dashboard annotations | **meaningful = 3**: backend/API, UI, gating, and tests add reporting context. | Backend/frontend/migration feature | Direct annotation API/frontend tests are present. | Artur 90%; Sanne de Vries 10% | [PR #6478](https://github.com/plausible/analytics/pull/6478), [commit `3d135c9a`](https://github.com/plausible/analytics/commit/3d135c9a5345197893ef051ab34ffcabada66573); [PR #6481](https://github.com/plausible/analytics/pull/6481), [commit `a3a2f312`](https://github.com/plausible/analytics/commit/a3a2f3126fc8c1e63d2ad7196e42b5c1a12ea20f); [PR #6482](https://github.com/plausible/analytics/pull/6482), [commit `354e47ce`](https://github.com/plausible/analytics/commit/354e47ce36700d8e88b157bac875190062f6942f); `primary-code:CHANGELOG.md:5-20` | High confidence in Artur's bounded Git/change attribution; medium confidence in Sanne's bounded attribution because the evidence is an earlier UI iteration. This is not a quality or performance judgement. |
| Replayed-event ingestion | **meaningful = 3**: request, session, and ClickHouse event/session paths support controlled event replay. | Ingestion/session/storage change | Direct ingestion, request, session-cache, and gatekeeper tests are present. | Adrian 100% | [PR #6491](https://github.com/plausible/analytics/pull/6491), [commit `17cfe6d9`](https://github.com/plausible/analytics/commit/17cfe6d98faa9d424acb27742af21309d3770e94); `primary-code:lib/plausible/ingestion/request.ex`; `primary-code:lib/plausible/session/cache_store.ex`; `primary-code:test/plausible/ingestion/request_test.exs` | High for source; this is EE-bound and not evidence of a CE or hosted control outcome. |

## Project-Lifetime Top-80% Contributors

The supported total is **50 feature-value units**, not 4,362 commits or all project value. On the conservative alias-set view, the following is the smallest set that reaches approximately 80%.

| Contributor | Attributed feature-value units | Share of supported total | Material feature/change units | Evidence and confidence |
|---|---:|---:|---|---|
| Uku Taht | 21.65 | 43.3% | Foundation; event/realtime; reporting/sharing; analysis/access; historical continuity; query/import | Direct authored history; mixed medium-to-high unit confidence. |
| Artur Pata | 7.70 | 15.4% | Multi-site teams/segments; form tracking; annotations | Direct authored history; high source confidence. |
| Adam Rutkowski / `hq1` alias set | 5.75 | 11.5% | Strict-order funnels; billing-role portion | Same source-recorded address supports the alias set, but displayed identity is not stable; no current role is inferred. |
| Vignesh Joglekar | 5.35 | 10.7% | Event/realtime; reporting/sharing; analysis controls; graph intervals | Direct authorship/co-authorship; medium-to-high source confidence. |

This set totals **40.45 units (80.9%)**. The supported long tail is **9.55 units (19.1%)**: Adrian Gruntkowski 5.25 (10.5%), Ruslandoga 2.00 (4.0%), Ro Savage 1.25 (2.5%), Vini Brasil 0.75 (1.5%), and Sanne de Vries 0.30 (0.6%). If Adam and `hq1` are not consolidated, the approximately-80% set changes to Uku, Artur, Vignesh, and Adrian (39.95 units; 79.9%); therefore the exact membership is identity-sensitive.

## Cutoff-Anchored 12-Month Periods

Two grouped lifetime units cross period boundaries. They are apportioned here only because exact author/commit dates identify their subcomponents: the analysis/access unit assigns 3.75 points to 2020–21 and Ro's 1.25 points to 2021–22; the historical-continuity unit assigns Uku's 2.50 points to 2021–22 and Vignesh/Vini's 2.50 points to 2022–23. No undated share is moved across a period.

### 2019-09-02 to 2020-08-19 (partial first period)

| Contributor | Attributed feature-value units | Share of supported period total | Material feature/change units | Evidence and confidence |
|---|---:|---:|---|---|
| Uku Taht | 8.00 | 100% | Initial foundation | Medium; one selected foundational unit. |

Long tail: 0 within the supported sample.

### 2020-08-20 to 2021-08-19

| Contributor | Attributed feature-value units | Share of supported period total | Material feature/change units | Evidence and confidence |
|---|---:|---:|---|---|
| Uku Taht | 8.15 | 69.4% | Event/realtime; reporting/sharing; dated analysis/access subcomponents | Medium-high. |
| Vignesh Joglekar | 3.60 | 30.6% | Event/realtime; reporting/sharing; dated filter subcomponent | Medium-high. |

Smallest approximately-80% set: both contributors, 11.75 units (100%). Long tail: 0 within the supported sample.

### 2021-08-20 to 2022-08-19

| Contributor | Attributed feature-value units | Share of supported period total | Material feature/change units | Evidence and confidence |
|---|---:|---:|---|---|
| Uku Taht | 2.50 | 66.7% | Dated GA-import/session subcomponent | Medium-high; other co-authored import work is unquantified. |
| Ro Savage | 1.25 | 33.3% | Dated conversion-rate subcomponent | High for authorship. |

Smallest approximately-80% set: both contributors, 3.75 units (100%). Long tail: 0 within the supported sample.

### 2022-08-20 to 2023-08-19

| Contributor | Attributed feature-value units | Share of supported period total | Material feature/change units | Evidence and confidence |
|---|---:|---:|---|---|
| Vignesh Joglekar | 1.75 | 70.0% | Dated graph-interval subcomponent | Medium-high. |
| Vini Brasil | 0.75 | 30.0% | Explicit co-author on dated graph-interval change | Medium; differentiated role is unavailable. |

Smallest approximately-80% set: both contributors, 2.50 units (100%). Long tail: 0 within the supported sample.

### 2023-08-20 to 2024-08-19

| Contributor | Attributed feature-value units | Share of supported period total | Material feature/change units | Evidence and confidence |
|---|---:|---:|---|---|
| Uku Taht | 3.00 | 60.0% | Query/filter contribution | Medium. |
| Ruslandoga | 2.00 | 40.0% | CE imported-data migration | Medium. |

Smallest approximately-80% set: both contributors, 5.00 units (100%). Long tail: 0 within the supported sample.

### 2024-08-20 to 2025-08-19

| Contributor | Attributed feature-value units | Share of supported period total | Material feature/change units | Evidence and confidence |
|---|---:|---:|---|---|
| Artur Pata | 5.00 | 62.5% | Segments and form-submission tracking | High for source. |
| Adrian Gruntkowski | 2.25 | 28.1% | Team-member/invitation actions | High for source. |

Smallest approximately-80% set: Artur and Adrian, 7.25 units (90.6%). Long tail: `hq1`, 0.75 units (9.4%).

### 2025-08-20 to 2026-08-20

| Contributor | Attributed feature-value units | Share of supported period total | Material feature/change units | Evidence and confidence |
|---|---:|---:|---|---|
| Adam Rutkowski | 5.00 | 45.5% | Strict-order funnels | High for EE source. |
| Adrian Gruntkowski | 3.00 | 27.3% | Event replay | High for source. |
| Artur Pata | 2.70 | 24.5% | Dashboard annotations | High for source. |

Smallest approximately-80% set: Adam, Adrian, and Artur, 10.70 units (97.3%). Long tail: Sanne de Vries, 0.30 units (2.7%).

## Material Unknowns And Closure Routes

- The lists describe only the eleven supported units. They must not be presented as the people who supplied 80% of Plausible's total value, nor used for staff/vendor performance, workload, payment, procurement, or blame.
- Git history does not identify current maintainers, release approvers, support staff, employment, availability, or successor authority. [OI-015](../open-items.md#oi-015) owns option accountability; [OI-020](../open-items.md#oi-020) owns a library successor exercise.
- Run receives meaningful upstream source and release value, but CE support remains community-only and its deployment repository is outside scope. Verify the consumed artifact/release through [OI-005](../open-items.md#oi-005) and the operating/upgrade route through [OI-004](../open-items.md#oi-004).
- Subscribe may buy direct vendor operation/support, but public terms and contribution history do not prove the library's support outcome, SLA, vendor continuity, entitlement, or exit. Close those through [OI-015](../open-items.md#oi-015) and [OI-017](../open-items.md#oi-017).
- Replace has no candidate, contributor history, vendor evidence, or successor model in scope. Reuse the attribution, ownership, support, release, licence, portability, and exit questions in a funded future shortlist.
