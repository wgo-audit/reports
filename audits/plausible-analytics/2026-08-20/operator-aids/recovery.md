# Recovery Decision And Evidence Guide

- Status: untested
- Selected precursor: [recovery and operations packet](../evidence/packets/recovery-and-operations.md), [recovery and control view](../controls/continuity/recovery-and-control-view.md), and [OI-002–OI-005](../controls/open-items.md#oi-002)

## Purpose And Evidence Boundary

Operator question: What must be true, observed, and retained before the library can call recovery of the selected Plausible option acceptable?

This is an untested decision and evidence guide, not authorization to restore, restart, migrate, fail over, or change a service. No library backup, topology, RPO/RTO, restore, rollback, incident, hosted control, or replacement candidate was inspected. Run recovery must coordinate PostgreSQL, ClickHouse, required persistent files, application/session state, and cross-store migrations. Subscribe recovery is vendor-operated but still requires library objectives, escalation, report reconciliation, account continuity, export, and contractual evidence.

## Existing Runbook And Coverage

No applicable production backup/restore or disaster-recovery runbook was found in the approved catalog or source. `primary-code:lib/plausible_release.ex:25-177` explains ordered cross-store up-migration and exposes pending/rollback mechanisms; `primary-code:rel/overlays/migrate.sh:1-6` and `primary-code:rel/overlays/rollback.sh:1-5` invoke them. `primary-code:rel/docker-entrypoint.sh:1-14` starts the application without automatically running migration. These are primary source mechanisms, not backup, restore, consistency, rollback, or recovery proof. The separate CE deployment repository is outside scope and must be reviewed at the deployed tag through [OI-004](../controls/open-items.md#oi-004) before adopting any of its procedures.

## Authority And Preconditions

Library IT/operations owns Run execution; the continuity authority approves the scenario and recovery objectives; the service owner accepts functional/reporting results; security/privacy approves test data and evidence handling. For Subscribe, procurement and the SaaS service owner additionally own vendor escalation and contractual evidence.

Do not schedule an exercise until all applicable prerequisites are recorded:

- selected option, non-production environment, fixture, exercise window, participants, communications route, and abort authority;
- approved normal and peak event-loss/reporting-outage limits from [OI-002](../controls/open-items.md#oi-002);
- exact Run topology, image digest, stores, volumes, queues, integrations, and health/telemetry boundary from [OI-001](../controls/open-items.md#oi-001), or accepted hosted responsibility/assurance evidence from [OI-015](../controls/open-items.md#oi-015);
- documented backup scope, timestamps, retention, encryption/custody, consistency method, restoration target, and rollback stop conditions under [OI-004](../controls/open-items.md#oi-004);
- artifact provenance under [OI-005](../controls/open-items.md#oi-005); and
- synthetic, non-identifying events and test identities approved under [OI-006](../controls/open-items.md#oi-006)/[OI-008](../controls/open-items.md#oi-008).

Any missing item remains `UNKNOWN`; this guide does not fill it with a default.

## Procedure And Stop Conditions

1. **Declare the scenario and success measures.** Record whether the bounded scenario is datastore unavailability/corruption, application restart/loss, migration failure, credential/account loss, mail/report failure, or hosted outage. Define expected recovery point, recovery time, acceptable measurement loss, reporting availability, and required data/output checks.
2. **Freeze identity and evidence.** Record the exact non-production release/digest, topology, datastore versions, pending migrations, configuration fingerprint, backup identifiers, and observation window. Do not record secrets. Confirm that production and live visitor traffic are outside the exercise.
3. **Review the recovery plan before action.** A second authorized operator checks backup completeness across PostgreSQL, ClickHouse, required persistent files and keys; source-to-artifact provenance; migration ordering; irreversible/non-atomic boundaries; rollback stop conditions; and the path back to the known pre-exercise state.
4. **Execute only under separate authorization.** This guide does not grant execution authority. For Run, the authorized procedure must restore into an isolated target, preserve cross-store consistency, start only after required migrations and configuration are reconciled, and avoid treating the generic rollback command as universally safe. For Subscribe, use the accepted vendor incident/escalation process and test only the library-controlled account, reporting, export, and communication boundaries permitted by contract.
5. **Verify service outcomes.** Reconcile datastore/application readiness with one synthetic search and registration journey, accepted-versus-stored event counts, session aggregates, goals, representative dashboard queries, CSV/API output, roles, monthly-report route, queue state, deletion/export state, and observable alerts. A green liveness response is insufficient.
6. **Measure and decide.** Compare actual loss, recovery time, report availability, inconsistencies, manual intervention, and unresolved alarms with the approved thresholds. Record `pass`, `fail`, or `inconclusive`; never turn an incomplete exercise into a pass.
7. **Return to the approved state.** Confirm the isolated target disposition, credential/access cleanup, alert closure, evidence retention, and next production-change decision. Production change requires a separate change record and approval.

Stop before or during any authorized exercise if the exact target or backup cannot be proven; production/live traffic could be affected; recovery would require an unreviewed irreversible or non-atomic migration; PostgreSQL/ClickHouse/persistent-file consistency cannot be established; required keys or owners are unavailable; unexpected visitor data appears; observed loss/outage exceeds the approved limit; or the rollback path would destroy the only usable copy. Preserve state and escalate.

## Expected Evidence And Records

Retain the approved scenario, authority record, exact non-production identity, redacted topology/configuration fingerprints, backup component identifiers and timestamps, restore/migration logs, start/stop times, accepted-versus-stored reconciliation, representative output checks, alerts/communications, deviations, final disposition, residual risk owner, and review date. Link the canonical record from [OI-003](../controls/open-items.md#oi-003) or [OI-004](../controls/open-items.md#oi-004); do not copy secrets, visitor data, or sensitive vendor evidence into the public audit.

`executed-successfully` is permitted only when an authorized canonical execution record demonstrates that every approved objective and stop condition was met. Source commands, vendor claims, backup completion, or a readiness response alone do not qualify.

## Escalation, Recovery, And Unknowns

Escalate tolerance decisions to the Director/continuity authority under OI-002; Run topology, artifact, backup, migration, and restore gaps to Library IT under OI-001/OI-004/OI-005; functional/reporting mismatches to Digital Services under OI-006/OI-014; and hosted recovery, support, or contract gaps to procurement and security under OI-015. If recovery fails or is inconclusive, keep the option conditional, preserve the last known usable state, remediate the smallest evidenced gap, and rerun only with renewed authority.

The current RPO/RTO, backup scope, restore target, runbook, owner roster, hosted recovery commitment, and verified exit copy are `UNKNOWN`.
