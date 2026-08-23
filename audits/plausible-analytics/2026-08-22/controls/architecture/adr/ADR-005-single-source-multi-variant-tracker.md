# ADR-005: Single-Source Multi-Variant Tracker

- Status: observed
- Evidence cutoff: 2026-08-22 22:08:28 EDT

## Decision Statement

`[Verified fact]` One tracker source tree compiles web, legacy, npm, and installation-support variants; Elixir serves compiled scripts and applies site-specific configuration. [E-006](../../../evidence/evidence-ledger.md#e-006)

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | Variant manifest and compile globals drive dead-code elimination; workflows enforce size reporting, release labels, changelog, and npm publication. | E-006 | Hosted publication/runtime compatibility not proven. |
| Runtime/live state | `[Unknown]` Variant use, CDN/cache state, npm adoption, and compatibility outcomes. | [OI-004](../../open-items.md#oi-004) | No customer/runtime inventory. |
| Rationale | `[Verified fact]` The tracker guide names small size, single-source maintenance, user configuration, and legacy support as design goals. | E-006 | No dated approval record. |
| Approval | `[Unknown]` | [OI-005](../../open-items.md#oi-005) | Guide authorship is not authority evidence. |

## Constraints, Options, And Tradeoffs

`[Reasoned inference]` One source limits divergent implementations and enables common browser tests; variant generation and legacy support increase the compatibility matrix and release coupling.

## Impacts And Boundaries

Tracker compilation produces both cloud-served script artifacts and npm package inputs. Product promises and compatibility policy belong to Product Value; live CDN/package state is not established here.

## Change, Reversal, And Follow-Up

Close [OI-004](../../open-items.md#oi-004) before pruning variants or splitting the tracker codebase.
