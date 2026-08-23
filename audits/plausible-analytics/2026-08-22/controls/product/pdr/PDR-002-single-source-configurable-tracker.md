# PDR-002: Single-Source Configurable Tracker

- Status: observed
- Evidence cutoff: 2026-08-22 22:08:28 EDT

## Decision Statement

Observed product position (not evidence of approval): one tracker source is compiled into web, npm, installation-support, and legacy variants, with site-specific settings applied at serving or client initialization.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Official scripts and browser-only npm integration support configurable event capture. | [E-020](../../../evidence/evidence-ledger.md#e-020) | Customer/browser compatibility not demonstrated. |
| Implementation | Compiler variants, serving/interpolation, and npm config share one source tree. | [E-006](../../../evidence/evidence-ledger.md#e-006) | Supported live variant set is unknown. |
| Runtime/demonstration | unknown | [OI-004](../../open-items.md#oi-004), [E-018](../../../evidence/evidence-ledger.md#e-018) | Public tests/history are not live coverage. |
| Approval/specialist sign-off | Tracker architecture states design goals; formal approval unknown. | [E-020](../../../evidence/evidence-ledger.md#e-020) | No decision owner. |

## Constraints, Options, And Tradeoffs

Shared source reduces semantic drift and bundle duplication, but expands compatibility and regression combinations across browsers, modes, and legacy variants.

## Impacts And Boundaries

Tracker changes can affect every collection channel and downstream statistic. Browser, SSR, opt-out, outbound/form/file, and custom-property behaviors require explicit matrix coverage.

## Change, Reversal, And Follow-Up

Map production-critical variants and retirement rules under [OI-004](../../open-items.md#oi-004) before a major tracker refactor.
