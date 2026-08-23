# ADR-003: Asynchronous Pluggable Ingestion Persistence

- Status: observed
- Evidence cutoff: 2026-08-22 22:08:28 EDT

## Decision Statement

`[Verified fact]` The event pipeline supports embedded, remote, and embedded-with-relay persistence, deterministic percentage rollout, in-memory session state, and asynchronous event/session write buffers before ClickHouse insertion. [E-002](../../../evidence/evidence-ledger.md#e-002) [E-003](../../../evidence/evidence-ledger.md#e-003)

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | `[Verified fact]` Embedded mode casts encoded rows into buffers with five-second/100,000-byte defaults; remote mode calls a configured HTTP/2 service; relay mode preserves embedded authority during transition. | [E-002](../../../evidence/evidence-ledger.md#e-002), [E-003](../../../evidence/evidence-ledger.md#e-003) | Runtime values/backend unknown. |
| Runtime/live state | `[Unknown]` Current backend, traffic percentage, remote implementation, drop rate, buffer loss, and session-handoff effectiveness. | [OI-001](../../open-items.md#oi-001) | No production telemetry/config. |
| Rationale | `[Verified fact]` PR #5653 describes a dedicated persistence service and transitional load testing; #5700 adds progressive percentage routing. | [E-003](../../../evidence/evidence-ledger.md#e-003) | PR rationale is not proof of current intent. |
| Approval | `[Unknown]` | [OI-005](../../open-items.md#oi-005) | Merge does not establish decision authority. |

## Constraints, Options, And Tradeoffs

`[Reasoned inference]` In-process buffers favor throughput and bounded ClickHouse write amplification; progressive backend selection reduces migration blast radius. The public `202` contract and cast-based buffer make confirmed durability distinct from request acceptance. A known `EXIT` crash was fixed after issue/PR review, but the complete failure/loss envelope is not public.

## Impacts And Boundaries

`[Verified fact]` Session processing uses local sharding/cache state and optional cross-deployment transfer. `[Reasoned inference]` Remote persistence is a material service/trust boundary. `[Unknown]` Its implementation and live operation are not in the approved evidence. Source does not prove data loss; it proves a durability boundary requiring measurement.

## Change, Reversal, And Follow-Up

Close [OI-001](../../open-items.md#oi-001) before changing acceptance semantics or persistor selection. Preserve deterministic rollout and rollback proof.
