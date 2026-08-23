# Expense Exposure Handoff

## Confirmed Navigation

Expense Exposure is `completed-with-open-verification`. Canonical validation
passed with 0 errors and 0 warnings. Use the [report](report.md),
[E-036..E-038](../../evidence/evidence-ledger.md), [commercial packet](../../evidence/packets/vendor-ownership-commercial.md),
and [burn control](../../controls/expense/burn-and-renewal.md).

## Constraints And Conflicts

Hosted list price is evidenced; Acme TCO is not. Public annual pricing and
monthly-cycle standard terms leave annual order/renewal mechanics unestablished.
Source dependencies are not spend.

## Material Unknowns

The horizon is 36 months; engineering time is opportunity cost, and pull/make carry no application-architecture-change effort. Provider rates, topology, check growth, alert volume, taxes/FX, hosted agreement, and account control remain unknown. RTO is 30 minutes and RPO is 5 minutes. OI-003 and OI-015 own remaining cost and plan closure; OI-004/OI-006/OI-012/OI-014 remain gates.

## Downstream Use

Maintenance Cost may estimate labor after design choices. Revenue Risk may use
interruption mechanisms, not invent loss. Neither may assume buy is all-in
cheapest, pull is free, make has a justified delta, or quotas fit.
