# Capacity Envelope

## Purpose And Evidence Boundary

This view separates source-known work from the workload and live measurements needed to approve Acme's slightly-below-100-job deployment. It uses [E-031 through E-035](../../evidence/evidence-ledger.md). Source and public operator reports do not prove production capacity. No benchmark, deployment, provider quota, runtime metric, or Acme job inventory was available.

## Workload Variables And Source-Bounded Arithmetic

| Variable | Meaning | Known value | Decision use |
|---|---|---|---|
| `N` | Monitored jobs/checks | Slightly below 100 today; growth expected | Hosted 100-check tier leaves little growth headroom; self-host source permits a much higher default account limit but capacity is unproved. |
| `fᵢ` | Runs per second for job `i` | unknown | Completion-only ping rate is `Σfᵢ`; start-plus-completion instrumentation approximately doubles requests. |
| `R` | Aggregate ping requests per second | unknown | If 100 jobs each run once per minute, arithmetic is 1.67 requests/s completion-only or 3.33 start-plus-completion; this is not an Acme assumption or capacity claim. |
| `Burst` | Events aligned in a short interval | unknown | Average rate cannot protect against synchronized schedules or dependency outages. |
| `B` | Retained bytes per ping body | default cap 10,000 bytes; 100 kB requires configuration | The view reads the full HTTP body before slicing retained bytes. With S3, bodies over 100 bytes add synchronous object upload to ping response time. |
| `L` | Retained ping count per check | default 100 | On successful pruning, rows per active check can reach `L + 99` between 100-ping prune points. |
| `C` | Enabled channels per flip | unknown | Channels for one flip are sequential; provider latency sums. |
| `W` | Alert workers | configurable; default 1 | Queue dwell depends on `W`, `C`, burst size, and channel service time. |

For a 100-check arithmetic boundary, once every check has at least `L` retained rows and pruning succeeds, a fully populated set contains about 10,000 rows immediately after each check's prune and fewer than 19,900 before the next per-check prunes; newer or sparse checks can be lower. If every retained body is exactly at the configured cap, raw body bytes at those occupancy points are about 0.10-<0.199 GB at 10 kB or 1.0-<1.99 GB at 100 kB. These are conditional decimal byte counts, not expected occupancy or disk requirements. With object storage, only retained pings whose bodies exceed 100 bytes create body objects; object/version/orphan/backup overhead remains unbounded.

## Decision Envelope

| Dimension | Source-known boundary/control | Approved workload conclusion | Required proof / stop condition |
|---|---|---|---|
| Ping ingress | Four single-threaded uWSGI processes by default; configurable; 10-second harakiri; no source ping limiter found | Job count is not a request-rate or burst envelope | Stop pull/make approval until OI-014 measures peak/burst latency and errors behind selected edge limits. |
| Same-check overlap | Each ping takes a database row lock | Different checks use separate rows; same-check events serialize | Test maximum expected overlap, including start/success/fail races. |
| 100 kB bodies | Requires increasing `PING_BODY_LIMIT`; request is read before truncation | Source can retain 100 kB, but safe rate, memory, and storage are unproved | Require a business need under OI-011; otherwise send no body. If needed, include 100 kB in OI-014. |
| Relational retention | Default `L=100`; prune every 100th ping; flips at least 93 days | Count-based pruning limits active-check history but does not size disk | Monitor prune success, row/index/dead-tuple growth, query latency, and backup size. |
| Object storage | Bodies >100 bytes offload; upload synchronous; read circuit after repeated errors; delete threaded | Reduces DB body bytes while adding latency, object-count, and recovery boundaries | Test timeout/outage behavior and preserve OI-006. |
| Alert delivery | Due checks one at a time; `W` workers; channels sequential; generic HTTP up to 90 seconds/channel | Synchronized misses have no proven five-minute queue margin | OI-006 governs T0/T1; OI-014 supplies production-shaped burst/resource evidence. |
| Hosted plan/provider | Public plans distinguish 100 and 1,000 checks; internals/quotas unknown | Current count is close to 100-check boundary | OI-004 confirms limits/commitments; Expense Exposure prices tier transition. |

## Intake Estimate Verdicts

| Intake claim | Verdict | Why |
|---|---|---|
| 1-2 vCPU | unsupported | No benchmark, peak rate, database topology, worker count, or availability topology exists. |
| 1-2 GB RAM | unsupported | No measurement exists. One maintainer reproduction said an 8 GB MariaDB buffer improved a much larger dataset; it is not transferable. |
| 10-20 GB SSD | unsupported | Disk depends on rows, indexes, dead tuples, flips, notifications, logs, backups, objects, and cleanup failures. |
| S3 for bodies up to 100 kB | mechanism confirmed; sizing unsupported | Offload threshold is 100 bytes when enabled, not 100 kB, and upload is synchronous. Capacity, latency, recovery, and quotas are unknown. |

The 2-5 setup-day and 4-8-hour/month estimates are left to Maintenance Cost and Expense Exposure. Scalability adds OI-014 measurement, alarms, and periodic growth review not evidenced in those figures.

## Growth Gates

1. Establish OI-001 inputs without broad team interviews: schedule, event multiplicity, peak alignment, body size/class, retention, channels, and one-year growth.
2. Select pull/make topology under OI-005 or complete hosted review under OI-004.
3. Execute OI-014 at 2x approved peak and expected one-year check count, then apply a measured margin. The multiplier is a proposed gate, not a supported capacity claim.
4. Pass OI-006 under synchronized misses and degraded provider/database/object storage with independent observation.
5. Re-run when retention, body limit, worker/channel count, database, provider, or check tier changes materially.
