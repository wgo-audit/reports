# Recovery Transition Aid

- Status: untested
- Selected precursor: [Recovery And Operations Packet](../evidence/packets/recovery-and-operations.md), [Continuity And Transfer Matrix](../controls/continuity/continuity-and-transfer-matrix.md), [Business Continuity Report](../reviewer-reports/business-continuity/report.md), and [OI-002/OI-004/OI-006](../controls/open-items.md)

## Purpose And Evidence Boundary

This aid answers one operator question: **how should an authorized successor restore a vanityURLs instance or the existing `v8s.link` service without confusing public source reconstruction with proven control-plane recovery?**

The runtime is stateless and the human-authored link registry is Git-backed, so source reconstruction is favorable. The existing service still depends on external GitHub, Cloudflare, Terraform state, DNS/domain, secret, deployment, alert, and renewal controls. Their owners, back ends, recovery factors, deployed equivalence, last-known-good deployment, recovery objectives, and restore history are **UNKNOWN**.

No restore, rollback, deployment, Terraform action, DNS change, secret recovery, or domain operation was executed during the audit. This aid must not be used as authorization to act on production.

## Existing Runbook And Coverage

Use these existing procedures as primary:

- The deployment and rollback section of [`RELEASE_WORKFLOW.md`](../../RELEASE_WORKFLOW.md) covers a clean reviewed worktree, deployment-log observation, custom-domain and exposure checks, last-known-good rollback, smoke checks, registry validation, and incident recording.
- [Upgrading an instance](../documentation/tmp/website/content/docs/reference/upgrading.en.md) covers product-file refresh while preserving instance-owned source and secrets. It does not provide a full rollback or recovery process.
- [`docs/README.md`](../../docs/README.md) covers everyday link changes, checks, Git publication, Cloudflare deployment, and source ownership.
- [`v8s-config/README.md`](../../tmp_debug/wgo-sources/v8s-config/README.md) covers Terraform initialization, validation, planning, known discovery limitations, import addresses, and the rule that dashboard changes be reconciled into Terraform.
- The [Quickstart](../documentation/tmp/website/content/docs/setup/quickstart.en.md) is the primary first-deployment procedure for a new independent instance.

None covers whole-service disaster recovery, Terraform backend/state restoration, registrar recovery, secret reconstitution, alert ownership, RTO/RPO, or a tested canonical takeover. This aid complements those missing boundaries and does not repeat their commands.

## Authority And Preconditions

Before any recovery action, record:

| Precondition | Required state | Current evidence |
|---|---|---|
| Recovery scope | `independent-instance`, `canonical-source`, or `existing-v8s-link-service` | **UNKNOWN** for a future event |
| Incident/recovery commander | Named person authorized to approve recovery and rollback | **UNKNOWN** |
| Independent reviewer | Separate person who verifies target, scope, and evidence | **UNKNOWN** |
| Recovery objectives | Maximum data loss, maximum interruption, and acceptance threshold | RPO/RTO/threshold **UNKNOWN** |
| Source checkpoint | Pinned product, instance, infrastructure, and website commits/tags | Audit pins exist; operational last-known-good values **UNKNOWN** |
| Release provenance | Selected upstream source authenticated against an approved signer policy | Design exists; upgrade enforcement incomplete under [OI-010](../controls/open-items.md) |
| Git authority | Recoverable access to required repositories and protected branches/tags | **UNKNOWN** |
| Cloud authority | Recoverable account/zone/Worker/Access/DNS/deploy authority | **UNKNOWN** |
| Terraform control | Known backend, state version, imports, drift, provider version, and lock | **UNKNOWN** |
| Domain control | Registrar owner, renewal state, recovery contact, transfer authority | **UNKNOWN** |
| Secret references | Redacted inventory of required secrets and custodians, without values | **UNKNOWN** |
| Isolated target | Approved non-production account/domain for rehearsal when production authority is absent | **UNKNOWN** |
| Communication route | Accountable publisher and approved status/contact channel | **UNKNOWN** |

Use the [IAM And Credential Control Aid](iam-and-credential-control.md) before retrieving or changing any credential. Use the [Observability Aid](observability.md) to establish detection and verification sources.

## Procedure And Stop Conditions

### 1. Classify the recovery

Record the failed layer and intended outcome:

- source/history reconstruction;
- instance link/configuration reconstruction;
- release-trust recovery;
- Worker deployment rollback;
- Terraform/cloud control-plane recovery;
- DNS/domain recovery;
- Access/secret recovery;
- public website/contact recovery.

Separate “new independent instance” from “recover the existing identity and service.”

**Stop** if the target or authorizing owner is **UNKNOWN**, if two environments could be confused, or if recovery would overwrite unexamined live state.

### 2. Freeze and preserve evidence

- Record incident time, reporter, visible symptoms, affected hostnames/paths, and current public impact.
- Preserve redacted GitHub, Cloudflare, deployment, Access, DNS, registrar, and Terraform logs available to the authorized operator.
- Record current repository heads, deployed identifier if visible, Terraform state version/serial if authorized, DNS values, and last-known-good references.
- Do not copy tokens, private keys, payment data, or secret values into the recovery record.

**Stop** destructive or irreversible changes until evidence has an accountable custodian and a reviewer confirms the target.

### 3. Reconstruct source

Use Git as the source for:

- product files and history;
- instance-owned `custom/` source and `wrangler.toml`;
- Terraform declarations;
- website/documentation source.

Treat generated `build/`, `src/`, and compatibility output as disposable and rebuildable. Verify selected commits/tags and follow the existing release/upgrade procedures. Do not use a mutable or unauthenticated upgrade source for recovery.

**Stop** if the last-known-good commit, trusted release source, or instance source of truth cannot be established. Escalate to the recovery commander; do not guess from generated or deployed output.

### 4. Reconcile the control plane

For a new independent instance, follow the [Quickstart](../documentation/tmp/website/content/docs/setup/quickstart.en.md) in the approved isolated environment.

For the existing service:

- identify the Terraform backend and current state before initialization against the target;
- compare declared resources, imports, provider/lock versions, and authorized live discovery;
- identify dashboard-only controls, emergency drift, DNS/domain settings, Worker deployment connection, Access application, WAF/rate limits, secrets by locator, and current deployed artifact;
- use the primary [`v8s-config/README.md`](../../tmp_debug/wgo-sources/v8s-config/README.md) import guidance only after matching resources and authority are verified.

**Stop before `apply`, import, secret change, DNS change, or deployment** if backend/state/import coverage, target account/zone, drift, rollback path, or reviewer is **UNKNOWN**. Source presence is not proof that Terraform owns the live resource.

### 5. Restore access and secrets by reference

Use the [IAM And Credential Control Aid](iam-and-credential-control.md). Restore only the minimum roles and secret references required for the selected path. Validate that departed identities can be revoked and that a second recoverable administrator exists.

**Stop** if recovery requires impersonating another person, sharing a personal credential, placing a secret in Git, or using an unowned break-glass path.

### 6. Build, deploy, and verify

Use the existing [`RELEASE_WORKFLOW.md`](../../RELEASE_WORKFLOW.md) deployment/rollback checklist and instance [Quickstart](../documentation/tmp/website/content/docs/setup/quickstart.en.md). Record:

- tool and provider versions;
- exact source commits/tags;
- check results with pass, fail, error, and skipped counts;
- generated release-manifest provenance;
- deployment identifier and target;
- public redirect, missing/lifecycle page, raw-runtime-file, Access-protected path, and registry-timestamp checks;
- Cloudflare deployment/Worker/Security evidence;
- analytics state, which should remain disabled unless explicitly owned.

Exact fixture, expected outputs, timing thresholds, and approved target are **UNKNOWN** until the exercise is authorized.

**Stop** if checks fail, source differs unexpectedly, the protected paths do not fail closed, raw runtime assets are exposed, or the target cannot be rolled back.

### 7. Roll back or accept recovery

If verification fails, use the primary rollback checklist to return to the identified last-known-good Git commit or Cloudflare deployment. Re-run the same smoke checks and record the result.

Accept recovery only when the recovery commander and independent reviewer confirm:

- intended source and deployed artifact match;
- core redirects and lifecycle behavior meet the approved fixture;
- Access and edge controls meet the approved boundary;
- alerts and public contacts are owned;
- remaining drift and unknowns have explicit owners.

No current acceptance threshold or authorized signer is established; both are **UNKNOWN**.

## Expected Evidence And Records

Retain one redacted recovery record containing:

- scenario, impact, scope, commander, reviewer, and authorization;
- RTO/RPO target and measured result, or `UNKNOWN`;
- preserved pre-change evidence;
- source pins and release-verification result;
- Git, Terraform state/backend/import/drift, Cloudflare, DNS/domain, deployment, and secret-locator inventories;
- check totals and generated-manifest identity;
- deployment, smoke, Access, edge, registry, and rollback results;
- incident communications and public status/contact decisions;
- data loss or source divergence assessment;
- unresolved items linked to [OI-002](../controls/open-items.md), [OI-004](../controls/open-items.md), [OI-006](../controls/open-items.md), [OI-010](../controls/open-items.md), and [OI-012](../controls/open-items.md).

Record location, retention period, and evidence access policy are **UNKNOWN**.

## Escalation, Recovery, And Unknowns

- If canonical authority is unavailable, do not alter the existing service; reconstruct an isolated instance under [OI-004](../controls/open-items.md).
- If Terraform state or import coverage is unavailable, stop live control-plane changes and close [OI-006](../controls/open-items.md).
- If release source cannot be authenticated, stop the upgrade/release path and close [OI-010](../controls/open-items.md).
- If credentials or administrators cannot be recovered or revoked, use [OI-002](../controls/open-items.md) and the [IAM And Credential Control Aid](iam-and-credential-control.md).
- If alerts, response ownership, or communication are missing, use [OI-012](../controls/open-items.md) and the [Observability Aid](observability.md).

Current recovery commander, second reviewer, RTO, RPO, last-known-good deployment, Terraform backend/state, registrar recovery, secret custodians, alert routes, and canonical exercise result remain **UNKNOWN**.
