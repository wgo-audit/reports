# Capability Contract Matrix

## Evidence Boundary

This source-bounded matrix traces the pinned implementation and repository
documentation. It does not claim a deployed Acme configuration, hosted parity,
job correctness, provider delivery, or human receipt. See [E-014..E-019](../../evidence/evidence-ledger.md).

| Capability | Entry point/input | Material rule/configuration | Runtime consumer | Product output | Pull | Make | Buy | Five-minute implication | Unknown/closure |
|---|---|---|---|---|---|---|---|---|---|
| Passive completion heartbeat | UUID/slug success ping | Simple period or Cron/OnCalendar + timezone + grace | `Check.ping`, `get_grace_start`, `sendalerts` | Up/Late/Down, event, notification | Source-backed | Same unless fork changes it | Expected, not independently proven | Grace consumes the budget before delivery begins | OI-006/OI-009 |
| Active execution outcome | `/start`, base success, `/fail`, `/<exit-status>` | Exit 0 succeeds; 1-255 fails; start overrun uses grace | Ping view/model | Started indicator, duration, Down/Up flip | Source-backed | Same unless changed | Expected, not independently proven | Explicit failure can alert earlier than waiting for lateness | OI-009 |
| Overlapping runs | Signals with optional `rid` UUID | RID pairs displayed duration; latest start alone governs overrun timer | `Check.ping`, `Ping.duration` | Per-event durations; incomplete all-run protection | Source-backed limit | Could change only with justified fork work | Hosted behavior unproven | A hung non-latest run can escape duration alerting | OI-009 |
| Content-derived status | HTTP/email payload | Case-sensitive failure→success→start precedence; unmatched ignored or failed | Ping/SMTP classifiers | Classified or Ignored event, possible flip | Source-backed | Same unless changed | Expected, not proven | Misclassification can suppress or accelerate alerting | OI-009 |
| Pause/resume | UI/API and incoming ping | Normal pause may be cleared by ping; sticky pause ignores all pings | Ping state transition | Paused or resumed state | Source-backed | Same unless changed | Expected, not proven | A forgotten sticky pause suppresses monitoring indefinitely | OI-009 |
| Notification routing | Down/up flip | Enabled project channels; sequential per flip; provider-specific retry/no-op | `sendalerts`, channel transports | Provider request, notification/error record | Must operate providers/workers | Adds fork ownership without fixing provider receipt by itself | Vendor operates service; provider/human path still needs proof | Remaining budget includes queue, retries, provider, escalation | OI-006 |
| Diagnostic event/log | POST body or `/log` | Default body cap 10,000 bytes; `/log` does not change state | Ping persistence/body retrieval | Event metadata and bounded payload | Acme controls storage | Same plus fork delta risk | Vendor visibility/retention unresolved | Adds context but must not delay or be required for detection | OI-004/OI-009 |
| Auto-provisioning | Slug ping with `create=1` | One-day period, one-hour grace, all channels; temporary 2x account limit | Slug ping view | New check + first event | Source-backed but unsafe by default for critical jobs | Same unless changed | Plan/limit behavior needs hosted verification | Default grace alone violates 300 seconds | OI-009 |
| Project governance | UI/API/project membership | Owner, Manager, Team Member, Read-only; project-scoped keys/channels | Accounts/project views/models | Access and configuration boundary | Acme operates identity | Same plus fork ownership | Hosted identity/control needs vendor review | Wrong ownership can make an alert non-actionable | OI-004/OI-009 |
| Windows scheduled task | Source-documented PowerShell/C# HTTP request | No in-corpus Task Scheduler wrapper or failure/overlap contract | Generic ping endpoints | Server-side events are source-backed; Windows behavior is unobserved | Protocol compatibility plausible; client procedure absent | Fork does not supply missing client operations | Protocol and hosted behavior unproven | Basic success ping cannot prove exit failure or five-minute receipt | OI-009 |

## Option-Level Capability Difference

- **Pull** provides the reviewed product contract without carrying a fork; production
  value still depends on Acme configuration, client instrumentation, and OI-006/OI-009.
- **Make** has no additional evidenced product value today. A fork is justified only
  by a measured, source-level gap that cannot be closed operationally.
- **Buy** may transfer service operation, but source parity, hosted controls, limits,
  availability, and delivery behavior remain unknown under OI-004 and OI-006.
