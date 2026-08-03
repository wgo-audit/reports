# Product Decision Register

## Records

| ID | Statement | Domain | Status | Evidence confidence | Record link |
|---|---|---|---|---|---|
| PDR-001 | Operators host source-controlled exact/splat redirects on their own domain. | Core capability | observed | High implementation; no independent live acceptance | [Record](pdr/PDR-001-self-hosted-short-links-as-code.md) |
| PDR-002 | Setup/detach creates an independent instance and stable-release upgrades preserve local ownership. | Setup/upgrade | accepted | High source intent; unexecuted | [Record](pdr/PDR-002-instance-setup-detach-and-upgrade.md) |
| PDR-003 | Link changes are human-authored/CLI-managed, checked, and committed through Git. | Operator workflow | observed | High implementation; operator usability unobserved | [Record](pdr/PDR-003-git-reviewed-link-management.md) |
| PDR-004 | Lifecycle and schedule rules determine temporary targets and status outcomes. | Lifecycle | observed | High implementation; transition behavior unobserved | [Record](pdr/PDR-004-link-lifecycle-and-schedules.md) |
| PDR-005 | Destination policy and generated blocklists constrain unsafe targets. | Trust/configuration | observed | High implementation; policy efficacy/sign-off unknown | [Record](pdr/PDR-005-destination-policy-and-blocking.md) |
| PDR-006 | Localized public/trust/status pages are generated and operator-customizable. | Output/acceptance | observed | High implementation; rendered/live output unobserved | [Record](pdr/PDR-006-localized-public-and-trust-pages.md) |
| PDR-007 | Operational views are private and analytics is optional/non-blocking. | Governance/dependency/privacy | observed | High source intent; live controls/provider behavior unknown | [Record](pdr/PDR-007-private-operations-and-optional-analytics.md) |

## Coverage And Disposition

| Domain | Candidates | Records | Other dispositions | Limitation |
|---|---:|---:|---|---|
| Users/maturity/promise | 2 | 1 | 1 blocked | No adoption, live demo, or independent acceptance evidence. |
| Setup/lifecycle/upgrades | 4 | 3 | 1 merged | Commands and lifecycle transitions were not executed. |
| Redirect/configuration/output | 4 | 3 | 1 merged | Generated and deployed output was not observed. |
| Trust/governance/dependencies | 3 | 2 | 3 cross-domain merges included | No live Access/provider evidence or trust-and-safety specialist sign-off. |
