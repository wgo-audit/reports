# Product Decision Candidate Inventory

## Coverage Domains

| Domain | Evidence boundary | Candidate count | Limitation/closure |
|---|---|---:|---|
| Users, maturity, and public promise | README, website docs, demo-instance source, public GitHub releases | 2 | No approved user research, adoption, service telemetry, acceptance, or independent demo exercise. |
| Setup, lifecycle, and upgrades | Installer/detach/upgrade source, CLI, guides, source ADRs | 4 | Commands were not executed and no non-creator walkthrough was observed. |
| Redirect, configuration, and output behavior | Build/Worker source, configuration schemas, reference docs | 4 | Runtime requests and generated outputs were not observed. |
| Trust, governance, and dependencies | Policy, Access, analytics, public pages, governance docs | 3 | Live control effectiveness, operator acceptance, provider state, and specialist sign-off are unknown. |

## Decision Candidates

| Candidate ID | Decision or durable behavior | Domain | Evidence | Observed/approved status | Disposition | Record or closure |
|---|---|---|---|---|---|---|
| PROD-DC-001 | Offer a source-controlled, self-hosted short-link redirector on an operator’s own domain. | User/promise | `README.md`; website setup/reference docs; Worker and Wrangler source | Public promise and implementation observed; adoption unknown | `record-created` | [PDR-001](pdr/PDR-001-self-hosted-short-links-as-code.md) |
| PROD-DC-002 | Use an idempotent setup, repository detachment, and stable-release upgrade path that preserves instance-owned files. | Setup/upgrade | `scripts/setup.mjs`; `scripts/detach-instance.mjs`; `scripts/upgrade.mjs`; quickstart; source ADR 0004 | Implemented/documented; execution unobserved | `record-created` | [PDR-002](pdr/PDR-002-instance-setup-detach-and-upgrade.md) |
| PROD-DC-003 | Make `custom/v8s-links.txt` the human-authored link source and provide a CLI that validates and commits successful changes. | Operator workflow | `docs/README.md`; `scripts/lnk`; `scripts/blocklist-cli.mjs`; LNK docs | Implemented/documented; operator acceptance unknown | `record-created` | [PDR-003](pdr/PDR-003-git-reviewed-link-management.md) |
| PROD-DC-004 | Support exact and splat redirects, including remainder substitution for splats. | Redirect contract | Registry/Worker source; link-format docs | Implemented/documented; live behavior unobserved | `merged-into` | [PDR-001](pdr/PDR-001-self-hosted-short-links-as-code.md) |
| PROD-DC-005 | Support link lifecycle states, expirations, maintenance/disabled pages, and ordered timezone-aware scheduled targets. | Lifecycle | Links parser, Worker state/schedule logic, public-page/schedule docs | Implemented/documented; boundary transitions unobserved | `record-created` | [PDR-004](pdr/PDR-004-link-lifecycle-and-schedules.md) |
| PROD-DC-006 | Validate destinations and apply default or instance-replacement policy/blocklists with narrowly scoped allow rules. | Trust/configuration | Policy/build/check source; blocklist docs | Implemented/documented; specialist sign-off and live efficacy unknown | `record-created` | [PDR-005](pdr/PDR-005-destination-policy-and-blocking.md) |
| PROD-DC-007 | Generate localized public, lookup, trust/legal, missing-link, and lifecycle pages with operator configuration and override support. | Output/acceptance | Build/site-core source; public-pages/i18n/jurisdiction docs | Implemented/documented; rendered output unobserved | `record-created` | [PDR-006](pdr/PDR-006-localized-public-and-trust-pages.md) |
| PROD-DC-008 | Protect statistics/test surfaces with Cloudflare Access and keep runtime data files non-public. | Governance/operator | Worker source; Access Terraform; security docs | Intended/implemented; live Access and acceptance unknown | `record-created` | [PDR-007](pdr/PDR-007-private-operations-and-optional-analytics.md) |
| PROD-DC-009 | Keep analytics disabled by default and send optional provider events asynchronously without blocking redirects. | Dependency/privacy | Worker analytics source; `wrangler.toml`; analytics docs | Implemented/documented; provider behavior unobserved | `merged-into` | [PDR-007](pdr/PDR-007-private-operations-and-optional-analytics.md) |
| PROD-DC-010 | Publish releases and allow detached instances to upgrade from stable signed tags while retaining local choices. | Upgrade/trust | Upgrade source; source ADRs 0001, 0004, 0015; release docs | Implemented/documented; signature/upgrade exercise unobserved | `merged-into` | [PDR-002](pdr/PDR-002-instance-setup-detach-and-upgrade.md) |
| PROD-DC-011 | Avoid upstream phone-home behavior; the upgrade nudge is opt-in and pull-based. | Public promise/privacy | `docs/README.md`; upgrade-nudge workflow template | Documented and source-observed | `merged-into` | [PDR-007](pdr/PDR-007-private-operations-and-optional-analytics.md) |
| PROD-DC-012 | Provide `v8s.link` as an official behavior reference/demo. | Maturity/demonstration | Website docs and `v8s-link` source | Public promise/source observed; live demonstration not cutoff-observed | `blocked` | OI-004: independently observe representative behavior and record assistance/results. |
| PROD-DC-013 | Generate readable random slugs with global, tag, and command-specific length precedence. | Operator workflow/configuration | CLI source/docs; source ADR 0006 | Implemented/documented | `merged-into` | [PDR-003](pdr/PDR-003-git-reviewed-link-management.md) |
