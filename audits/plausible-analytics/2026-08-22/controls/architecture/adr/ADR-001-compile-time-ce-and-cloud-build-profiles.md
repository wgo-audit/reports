# ADR-001: Compile-Time CE and Cloud Build Profiles

- Status: observed
- Evidence cutoff: 2026-08-22 22:08:28 EDT

## Decision Statement

`[Verified fact]` One Phoenix/OTP monorepo produces Community Edition and cloud/EE builds through Mix environments, compile-time `on_ce`/`on_ee` macros, `extra/lib` source inclusion, and build-specific assets/images. [E-001](../../../evidence/evidence-ledger.md#e-001) [E-011](../../../evidence/evidence-ledger.md#e-011)

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | `test`/`prod` include `extra/lib`; CE profiles omit it and compile different branches/assets. Ninety-eight Elixir files contain CE/EE conditionals. | E-001, E-011 | Count is breadth, not defect evidence. |
| Runtime/live state | `[Unknown]` Which profiles, versions, and feature combinations run in each environment. | [OI-004](../../open-items.md#oi-004) | No live inventory. |
| Rationale | `[Public claim]` The same code supports managed cloud and CE while premium/infrastructure responsibilities differ. | E-011 | Marketing claim, not an internal decision record. |
| Approval | `[Unknown]` | [OI-005](../../open-items.md#oi-005) | Merge history does not prove approval authority. |

## Constraints, Options, And Tradeoffs

`[Reasoned inference]` Shared code reduces duplication and supports rapid cross-edition fixes, but compile-time branching and tracker variants enlarge the configuration matrix. Existing CE/cloud CI and artifact workflows reduce, but do not eliminate, edition-specific risk.

## Impacts And Boundaries

The Phoenix endpoint, repositories, jobs, router, and many feature paths remain one deployable application. This record does not establish Community Edition packaging or upgrades: `Documented outside audited scope; not independently verified.` The smallest expansion would be the specifically referenced `plausible/community-edition` release/upgrade corpus, which the auditor excluded.

## Change, Reversal, And Follow-Up

Map supported combinations and owners before changing the build boundary; close [OI-004](../../open-items.md#oi-004). Validate approval/rationale through [OI-005](../../open-items.md#oi-005).
