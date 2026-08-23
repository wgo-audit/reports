# Contributor Value Assessment

## Evidence Boundary And Attribution Rules

- **Audit cutoff:** 2026-08-19; `HC-CODE-001` pinned at `fafac59eeb00cfdc87166242544fa071ecad1723`.
- **Included source types:** Complete Git history and tags, repository `CHANGELOG.md`, linked public issues/PRs/commits, implementation, tests, and documentation. Product Value and Business Continuity establish outcome context only.
- **Excluded/inaccessible source types:** Private work, personnel records, review approvals/comments, uncredited work, hosted operations, and demonstrated Acme outcomes.
- **Feature grouping rule:** A unit is a coherent implemented outcome whose linked commits and files can be bounded. Twenty-three units were selected to cover every consecutive annual window; the sample is not exhaustive.
- **Attribution rule:** Credit only directly evidenced material implementation, tests, or documentation. Merge, comment, and raw activity volume are not credit. Units use `critical = 8`, `high = 5`, `meaningful = 3`, `bounded = 2`, and `minor = 1` only as within-audit ordering aids.

## Feature/Change Units

| Unit | Outcome and value band | Task magnitude | Delivery quality | Credited contributors and share | Evidence | Confidence/limit |
|---|---|---|---|---|---|---|
| 2026 notification downtime context | Alert context propagated across transports; `high = 5` | Cross-transport | Representative tests present | Pēteris Caune 100% | [#1309](https://github.com/healthchecks/healthchecks/issues/1309), [commit](https://github.com/healthchecks/healthchecks/commit/3cb1262745a11d202133b851c9f4ecb7ac7b5a92); `HC-CODE-001:hc/api/models.py`, `HC-CODE-001:hc/integrations/telegram/tests/test_notify.py` | High; delivery, receipt, and Acme approval unproved |
| 2026 Gotify priorities | Down/up priority control; `meaningful = 3` | Integration UI, transport, tests | Focused tests present | João F. 100% | [#990](https://github.com/healthchecks/healthchecks/issues/990), [commit](https://github.com/healthchecks/healthchecks/commit/7ed59c4d3e079e0bcbede143b99b32b7bd0fab5b); `HC-CODE-001:hc/integrations/gotify/` | High; implementation only |
| 2025 hashed project API keys | Reduces recoverable secret exposure; `high = 5` | Auth and migration | Focused tests present | Pēteris Caune 100% | [PR #1167](https://github.com/healthchecks/healthchecks/pull/1167), [commit](https://github.com/healthchecks/healthchecks/commit/d953c7b65cb33172dd5fddc7b42d39a88621e5db); `HC-CODE-001:hc/api/tests/test_auth.py` | High; deployed migration unproved |
| 2025 Docker IPv6 | Adds uWSGI IPv6 listening; `bounded = 2` | Deployment config | No same-unit test | Nico B 100% | [PR #1177](https://github.com/healthchecks/healthchecks/pull/1177), [commit](https://github.com/healthchecks/healthchecks/commit/b2185e3120811225081214d108ac42e99bbbfccf); `HC-CODE-001:docker/uwsgi.ini` | Medium quality; runtime unproved |
| 2024 serialized check updates | Protects core ping-state consistency; `high = 5` | Core ingestion | No same-unit test delta | Pēteris Caune 100% | [#1023](https://github.com/healthchecks/healthchecks/issues/1023), [commit](https://github.com/healthchecks/healthchecks/commit/bc8fb90fed6be42ffa746dbe2ae7b58d05b72aef); `HC-CODE-001:hc/api/models.py` | Medium quality; concurrency behavior not run here |
| 2023 notification groups | Adds grouped routing control; `high = 5` | Model, form, view, UI | Focused tests present | Florian Apolloner 100% | [PR #901](https://github.com/healthchecks/healthchecks/pull/901), [#894](https://github.com/healthchecks/healthchecks/issues/894), [commit](https://github.com/healthchecks/healthchecks/commit/7057f6d3a5fd052c307bf425624b98b0943f05a9); `HC-CODE-001:hc/api/tests/test_notify_group.py` | High; live routing unproved |
| 2023 OnCalendar | Adds systemd schedule semantics; `high = 5` | Model, parser, UI, docs | Focused tests present | Pēteris Caune 100% | [#919](https://github.com/healthchecks/healthchecks/issues/919), [commit](https://github.com/healthchecks/healthchecks/commit/d65f41d192e95b8e30c95768195739bdcf7a807d); `HC-CODE-001:hc/front/tests/test_oncalendar_preview.py` | High; Acme schedule fit unproved |
| 2022 run IDs | Correlates overlapping start/completion duration; `high = 5` | Migration, model, ingest, UI | Focused tests present | seidnerj 100% | [PR #722](https://github.com/healthchecks/healthchecks/pull/722), [commit](https://github.com/healthchecks/healthchecks/commit/b6027fa12650827705df40b5f54b58c0b9fd8b96); `HC-CODE-001:hc/api/tests/test_ping.py` | High; not every concurrent run is alerted |
| 2022 Gotify integration | Adds full notification channel; `high = 5` | Transport, forms, views | Focused tests present | Pēteris Caune 100% | [#270](https://github.com/healthchecks/healthchecks/issues/270), [commit](https://github.com/healthchecks/healthchecks/commit/b19ddab1bde31c33c8dc267e366815013640c1c9); historical `HC-CODE-001:hc/api/tests/test_notify_gotify.py` | High; provider delivery unproved |
| 2022 SMTP implicit TLS | Adds operator configuration; `meaningful = 3` | Settings and docs | No same-unit automated test | Facorazza 100% | [commit](https://github.com/healthchecks/healthchecks/commit/6f1900cfa32c74ecbc25e5838b3e533b8b36d7c2); `HC-CODE-001:hc/settings.py`, `HC-CODE-001:templates/docs/self_hosted_configuration.md` | Medium; no PR/issue association recovered |
| 2021 TOTP 2FA | Adds account credential control; `high = 5` | Model, forms, migration | Extensive focused tests | Pēteris Caune 100% | [#354](https://github.com/healthchecks/healthchecks/issues/354), [commit](https://github.com/healthchecks/healthchecks/commit/222722569ee275845e15e0c9286c7da5ff9bc33d); `HC-CODE-001:hc/accounts/tests/test_login_totp.py` | High; deployed control unproved |
| 2021 manager role | Adds project governance role; `high = 5` | Model, migration, forms, views | Focused tests present | swoga 100% | [#484](https://github.com/healthchecks/healthchecks/issues/484), [commit](https://github.com/healthchecks/healthchecks/commit/9640d2242f9e868f765ed8c6e1b05b86385f6aa1); `HC-CODE-001:hc/accounts/tests/test_project.py` | High; Acme role design unknown |
| 2020 phone-call integration | Adds notification channel; `high = 5` | Transport, routes, views | Focused tests present | Pēteris Caune 100% | [#403](https://github.com/healthchecks/healthchecks/issues/403), [commit](https://github.com/healthchecks/healthchecks/commit/ee9ac0ffefca6131192baf0b14ed2d497432755f); historical `HC-CODE-001:hc/front/tests/test_add_call.py` | High; provider behavior unproved |
| 2020 check-history API follow-through | Returns flip history; `high = 5` | API, model, docs | Focused tests present | James Kirsop 100% of bounded unit | [#370](https://github.com/healthchecks/healthchecks/issues/370), [commit](https://github.com/healthchecks/healthchecks/commit/368d7a4fec374f5cec57e485902191bc231c8a87); `HC-CODE-001:hc/api/tests/test_get_flips.py` | High; separate #371 work excluded |
| 2019 project model | Creates project-scoped ownership foundation; `critical = 8` | Cross-account/API migration | Broad affected tests | Pēteris Caune 100% | [#183](https://github.com/healthchecks/healthchecks/issues/183), [commit](https://github.com/healthchecks/healthchecks/commit/1c69cf7f8914730520f40d68fdef05c1ece62fdb); historical migrations `0017/0018` | High; live migration unproved |
| 2019 Apprise integration | Adds generalized notification integration; `high = 5` | Transport, settings, UI, docs | Focused tests present | Chris Caron 100% | [PR #272](https://github.com/healthchecks/healthchecks/pull/272), [commit](https://github.com/healthchecks/healthchecks/commit/c2b1d00422db971d4d1f758ef4191b65adfb1c9d); historical `HC-CODE-001:hc/front/tests/test_add_apprise.py` | High; third-party support outside scope |
| 2018 explicit fail pings | Adds failure-state semantics; `critical = 8` | Core state, API, migration, UI | Model and ping tests | Pēteris Caune 100% | [#151](https://github.com/healthchecks/healthchecks/issues/151), [commit](https://github.com/healthchecks/healthchecks/commit/3fc84ca0ffc1d4b8cd0285a38b50bafca0652c28); historical `HC-CODE-001:hc/api/tests/test_ping.py` | High; Acme job correctness unproved |
| 2017 webhook headers | Adds arbitrary headers and UI/storage; `high = 5` | Transport, form, view, JS | Focused tests present | someposer 100% | [PR #140](https://github.com/healthchecks/healthchecks/pull/140), [commit](https://github.com/healthchecks/healthchecks/commit/5781ddfe4dccc3cb05cf35413e7d7c3ce8efb1f5); historical `HC-CODE-001:hc/front/tests/test_add_webhook.py` | High; secret/data safety not inferred |
| 2017 last-ping body | Adds diagnostic payload retention; `high = 5` | Migration, model, API, UI | Model/ping tests | Pēteris Caune 100% | [#116](https://github.com/healthchecks/healthchecks/issues/116), [commit](https://github.com/healthchecks/healthchecks/commit/3862cd6b0658ef96a21619219d5fb84a6b1e7568); historical `HC-CODE-001:hc/front/tests/test_last_ping.py` | High; data classification remains unknown |
| 2016 site identity | Propagates configurable site name; `meaningful = 3` | Config/templates/tests | Affected tests adjusted | James Moore 100% | [PR #86](https://github.com/healthchecks/healthchecks/pull/86), [merge](https://github.com/healthchecks/healthchecks/commit/ac68df5bf5c223c523c41b5ee6309eec8d1db863); `HC-CODE-001:hc/settings.py` | High; historical source surface changed since |
| 2016 password accounts | Adds password-backed authentication; `high = 5` | Backend, forms, model, views | Affected tests present | Pēteris Caune 100% | [#6](https://github.com/healthchecks/healthchecks/issues/6), [commit](https://github.com/healthchecks/healthchecks/commit/1dacc8b797b18fcc3900a10b751408455a9980f4); historical `HC-CODE-001:hc/accounts/` | High; current auth evolved |
| 2015 concurrent sendalerts | Adds concurrent dispatch; `critical = 8` | Alert command/model/dependency | No focused same-unit test located | Di Wu 100% | [PR #9](https://github.com/healthchecks/healthchecks/pull/9), [merge](https://github.com/healthchecks/healthchecks/commit/4e53e064189611754006ba5630aebfaccf80d3e7); historical `HC-CODE-001:hc/api/management/commands/sendalerts.py` | Medium quality; implementation later changed |
| 2015 founding product | Establishes checks, ping ingest, alert worker/channels, and tests; `critical = 8` | Launch-scale | Tests added in range | Pēteris Caune 100% | [range](https://github.com/healthchecks/healthchecks/compare/00cdc313eca85a5a2bc68e77fc7dcef5f72eadfc...cee2b52d3ec5312715fc63900fc851d641b5f2e0); historical check/model/worker/tests | High authorship, medium historical quality; no founding PR/issue |

## Project-Lifetime Top-80% Contributors

The supported set totals 118 units. The deterministic table uses alphabetical order to break a six-way tie at five units; any four tied contributors with Pēteris Caune and Di Wu form an equally small six-person set at 97/118 (82.2%).

| Contributor | Attributed feature-value units | Share of supported total | Material feature/change units | Evidence and confidence |
|---|---:|---:|---|---|
| Pēteris Caune | 69 | 58.5% | Founding product; project model; fail pings; TOTP; schedule, integration, security, and consistency changes | Unit-linked evidence above; high attribution, selective-set limit |
| Di Wu | 8 | 6.8% | Concurrent `sendalerts` | PR #9 and merge; high identity, medium quality evidence |
| Chris Caron | 5 | 4.2% | Apprise integration | PR #272 and linked implementation/tests; high |
| Florian Apolloner | 5 | 4.2% | Notification groups | PR #901, issue #894, tests; high |
| James Kirsop | 5 | 4.2% | Check-history API follow-through | Issue #370, implementation/docs/tests; high |
| seidnerj | 5 | 4.2% | Run ID correlation | PR #722, implementation/tests; high |

Supported long tail: 21/118 (17.8%), including swoga and someposer at five each and five smaller-unit contributors. This is not a project-wide or personnel ranking.

## Cutoff-Anchored 12-Month Periods

Each full period deliberately contains two supported units, so its smallest set includes both contributors and its within-sample long tail is zero. That is a sampling property, not evidence that actual annual work had no long tail.

| Period | Contributor set reaching at least 80% | Supported units/share | Supported long tail | Confidence/limit |
|---|---|---:|---:|---|
| 2025-08-20 to 2026-08-19 | Pēteris Caune; João F. | 8/8, 100% | 0 | High attribution; selective two-unit sample |
| 2024-08-20 to 2025-08-19 | Pēteris Caune; Nico B | 7/7, 100% | 0 | High identity; mixed quality; selective sample |
| 2023-08-20 to 2024-08-19 | Pēteris Caune; Florian Apolloner | 10/10, 100% | 0 | High attribution; selective sample |
| 2022-08-20 to 2023-08-19 | Pēteris Caune; seidnerj | 10/10, 100% | 0 | High attribution; selective sample |
| 2021-08-20 to 2022-08-19 | Pēteris Caune; Facorazza | 8/8, 100% | 0 | Medium-high; selective sample |
| 2020-08-20 to 2021-08-19 | Pēteris Caune; swoga | 10/10, 100% | 0 | High attribution; selective sample |
| 2019-08-20 to 2020-08-19 | Pēteris Caune; James Kirsop | 10/10, 100% | 0 | High attribution; selective sample |
| 2018-08-20 to 2019-08-19 | Pēteris Caune; Chris Caron | 13/13, 100% | 0 | High attribution; selective sample |
| 2017-08-20 to 2018-08-19 | Pēteris Caune; someposer | 13/13, 100% | 0 | High attribution; selective sample |
| 2016-08-20 to 2017-08-19 | Pēteris Caune; James Moore | 8/8, 100% | 0 | High attribution; selective sample |
| 2015-08-20 to 2016-08-19 | Di Wu; Pēteris Caune | 13/13, 100% | 0 | Medium-high; selective sample |
| 2015-06-11 to 2015-08-19 (partial) | Pēteris Caune | 8/8, 100% | 0 | High authorship, medium historical quality |

## Material Unknowns And Closure Routes

- The 23-unit set supports bounded concentration findings, not an exhaustive project-wide top-80 claim. An exhaustive feature catalog would be required before using these numbers for any personnel or commercial allocation; this audit has no such need.
- Reviews, design, debugging, issue work, operations, and uncredited work are unavailable and excluded from numeric credit.
- Identity normalization is limited; no `.mailmap` exists.
- No contribution unit proves Acme's live reliability, recovery, security, or human-alert targets. OI-006, OI-013, and OI-014 retain those proof routes.
