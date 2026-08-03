# PDR-002: Instance Setup, Detach, And Upgrade

- Status: accepted
- Evidence cutoff: July 22, 2026

## Decision Statement

A new operator clones the product, detaches into an independent repository, runs idempotent setup, connects a Cloudflare deployment, and later upgrades product-owned files from stable upstream releases while retaining instance-owned configuration.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Quickstart promises a path from clone to first deployed redirect and upgrades that preserve local choices. | Website quickstart/upgrading docs | Assistance and completion time unobserved. |
| Implementation | Setup, detach, upgrade, source-selection, and verification scripts exist with tests declared. | `scripts/setup.mjs`; `detach-instance.mjs`; `upgrade.mjs`; package scripts | Commands/tests not run. |
| Runtime/demonstration | `v8s-link` is a detached instance at product version 3.6.3. | Instance source/history | Its creation/deployment was not independently observed. |
| Approval/specialist sign-off | Source ADR 0004 is accepted; release trust is documented. | `docs/adr/0004-*`, `0015-*` | Successor/operator acceptance unknown. |

## Constraints, Options, And Tradeoffs

Detachment gives owners independence but intentionally removes upstream maintainer material; upgrades execute refreshed scripts and therefore rely on release provenance and local review.

## Impacts And Boundaries

The mechanism supports third-party creation of new instances. It does not transfer existing repositories, domain, Cloudflare state, secrets, or release authority.

## Change, Reversal, And Follow-Up

Preserve source/instance boundaries and stable signed release defaults. Use OI-004 to observe a clean non-creator setup and upgrade; record every creator intervention.
