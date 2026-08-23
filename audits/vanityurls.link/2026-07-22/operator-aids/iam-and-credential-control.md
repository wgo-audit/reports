# IAM And Credential Control Transition Aid

- Status: untested
- Selected precursor: [Secret, Identity, And Privacy Surface](../controls/security/secret-and-identity-surface.md), [Vendor, Ownership, And Commercial Packet](../evidence/packets/vendor-ownership-commercial.md), [Security/Privacy Report](../reviewer-reports/security-privacy/report.md), and [OI-002/OI-006](../controls/open-items.md)

## Purpose And Evidence Boundary

This aid answers one operator question: **how should a successor inventory, receive, verify, review, recover, and relinquish the identities and credentials needed to maintain vanityURLs without exposing secret values or inheriting creator-only access?**

It covers roles and recovery paths for GitHub, release signing, Cloudflare, Workers/deployment, Access/identity providers, DNS/domain registrar, Terraform state/backend, public contacts, alerts, and optional analytics. It does not contain credentials or authorize access.

Public source documents variable names, desired controls, two release-signer identities, and secret-storage boundaries. Actual owners, administrators, tokens, keys, recovery factors, Terraform state custodian, registrar account, deployment connection, Access allow list, provider plans, and offboarding state are **UNKNOWN**. No authentication, invitation, privilege change, rotation, revocation, recovery, or secret validation was executed.

## Existing Runbook And Coverage

No existing document provides a complete joiner/mover/leaver, recovery, and cross-provider credential-control procedure.

Use these sources as primary for their narrower questions:

- [Access control](../documentation/tmp/website/content/docs/customize/access-control.en.md) covers Cloudflare Access setup, identity-provider choices, audience-secret storage, allowed/denied tests, and protected paths.
- [Cloudflare Access operations](../documentation/tmp/website/content/blog/operating-cloudflare-access-for-a-short-link-domain.en.md) covers review triggers when a maintainer, domain/account, team domain, provider, or exposed value changes.
- [Setup prerequisites](../documentation/tmp/website/content/docs/setup/_index.en.md) requires operational secrets and recovery information outside Git.
- `product-code:.github/repository-rules.md` defines desired GitHub least privilege, phishing-resistant authentication, branch/tag rules, Actions permissions, secret scanning, and owner expectations. Applied settings are external.
- `product-code:RELEASE_WORKFLOW.md`, `product-code:.github/release-signers.json`, and `product-code:.github/MAINTAINERS.md` define the release-signing procedure and trusted identities. Recovery and successor enrollment are not defined.
- `terraform-source:README.md` defines least-permission Cloudflare token intent and notes that the observed DNSControl token lacked Access permissions.

This aid complements those sources with a redacted control inventory and lifecycle. It does not reproduce provider-specific setup or secret commands.

## Authority And Preconditions

Before any access change, record:

| Precondition | Required state | Current evidence |
|---|---|---|
| Continuity scope | Independent fork or canonical asset/service continuity | **UNKNOWN**; [OI-001](../controls/open-items.md) |
| Access approver | Current authorized owner for each provider/asset | **UNKNOWN** |
| Successor identity | Unique personal identity; no shared login | **UNKNOWN** |
| Role requirement | Documented task and least privilege | **UNKNOWN** |
| Removal authority | Separate recoverable administrator able to revoke access | **UNKNOWN** |
| Authentication baseline | Phishing-resistant MFA for privileged roles and protected recovery factors | Declared intent; applied state **UNKNOWN** |
| Secret store | Approved password/secret manager and recovery-owner policy | **UNKNOWN** |
| Evidence store | Redacted access decision and review log | **UNKNOWN** |
| Emergency authority | Approved break-glass owner, conditions, expiry, and review | **UNKNOWN** |
| Offboarding trigger | Role end/change communicated to every surface owner | **UNKNOWN** |

Never record a token, private key, recovery code, password, payment method, or secret value in this aid, Git, an issue, a pull request, or an audit artifact.

## Procedure And Stop Conditions

### 1. Create the redacted control inventory

For each surface, record provider/asset, role needed, current accountable owner, backup owner, recovery route, secret locator, grant/revoke authority, review date, and expiry. Use `UNKNOWN` rather than guessing.

| Surface | Minimum roles to account for | Current position |
|---|---|---|
| GitHub repositories/organization | Owner/admin, merge/review, Actions/environment, ruleset/security administration | Actual assignments **UNKNOWN** |
| Release trust | Trusted signer, signer-list approver, tag-rule administrator, recovery path | Two declared signer identities; custody/recovery **UNKNOWN** |
| Cloudflare account/zone | Account/zone admin, DNS, Workers, Access/Zero Trust, WAF/rules, analytics/logs, billing/plan | Actual assignments **UNKNOWN** |
| Deployment connection | GitHub application/integration, environment approval, deploy/rollback operator | **UNKNOWN** |
| Domain registrar | Registrant/admin/technical contacts, renewal/payment owner, transfer/recovery authority | **UNKNOWN** |
| Terraform | Backend/state administrator, provider-token custodian, import/apply reviewer | **UNKNOWN** |
| Worker secrets | Secret owner, runtime setter, recovery/rotation owner | Variable roles known; custody **UNKNOWN** |
| Public contacts/alerts | Security, abuse, privacy, operations, renewal, incident communication | Public values exist; monitoring/backup **UNKNOWN** |
| Optional analytics | Provider admin, collection configuration, management token, privacy/retention owner | Disabled baseline; external roles **UNKNOWN** |

**Stop** if an asset has no identifiable authorized owner, if one person is the only recoverable administrator, or if ownership is inferred from a public commit/email rather than provider evidence.

### 2. Verify recovery before adding responsibility

For every transfer-critical surface:

- verify two independent recovery paths where the provider permits;
- verify each privileged identity uses an individual account;
- verify MFA and protected recovery factors;
- verify the backup can recover without the primary;
- verify provider/domain notifications reach owned destinations;
- verify access and audit logs are available to an authorized reviewer.

Use safe provider-supported verification or an isolated exercise. Exact identities, factors, test method, and acceptance criteria are **UNKNOWN**.

**Stop** if verification would reveal a secret, lock out the sole owner, alter production, or depend on an unowned personal account.

### 3. Joiner or role expansion

- Approve the task and minimum role.
- Grant access through the provider’s supported individual/team mechanism.
- Require the authentication baseline before privileged use.
- Test only the minimum allowed action in a safe target.
- Record grant, approver, role, scope, test evidence, review/expiry date, and removal owner.
- For release signing, follow the primary release procedure and signer-list approval; do not move or recreate an existing tag.
- For Access, follow the primary [Access control](../documentation/tmp/website/content/docs/customize/access-control.en.md) procedure and test allowed and denied identities.

**Stop** if a shared credential is proposed, if the approver is not authoritative, or if the role exceeds the agreed task.

### 4. Mover or periodic review

Review access when a maintainer’s role changes, at a scheduled interval, after an incident, after account/domain migration, after provider/IdP changes, or when an operational value may have been exposed.

- Compare current provider roles with the redacted inventory.
- Remove obsolete roles and stale identities.
- Reconfirm backup recovery, public contacts, alerts, and renewal ownership.
- Reconcile GitHub rules, Cloudflare Access, Terraform state access, deploy integrations, and secret locators.
- Keep analytics disabled unless its owner, purpose, fields, IP mode, retention, deletion, and cost/quota are approved.

Review interval and accountable reviewer are **UNKNOWN**.

### 5. Leaver or emergency revocation

An authorized owner should:

- revoke provider sessions, memberships, roles, application grants, deploy access, and alert/contact access;
- remove the person from Access policies/groups and any trusted-signer list through reviewed change;
- rotate only credentials that were shared, exposed, or solely controlled by the leaver;
- transfer registrar, renewal, billing-notification, Terraform-state, public-contact, and incident responsibilities;
- preserve redacted audit evidence;
- verify that the remaining backup can administer and recover each surface.

Do not rotate blindly. Provider, credential identity, impact, rollback, owner, and validation method must be established first.

**Stop** if revocation would remove the last recoverable administrator or interrupt the domain/service without an approved recovery path. Escalate to the continuity authority and use the [Recovery Aid](recovery.md).

### 6. Break-glass and secret recovery

A break-glass path is acceptable only when an authorized owner has documented:

- exact provider/asset scope;
- protected storage locator;
- two-person retrieval or equivalent control;
- permitted emergency conditions;
- expiry and rotation;
- access logging and after-action review;
- tested recovery that does not expose secret values.

No such path is publicly evidenced; its existence, location, owners, and test result are **UNKNOWN**.

## Expected Evidence And Records

Retain only redacted records:

- current/backup owner and role per critical surface;
- approver, grant, verification, review, expiry, and revoke decisions;
- authentication and recovery-path confirmation without factor values;
- signer-list and immutable-tag control evidence;
- GitHub ruleset/security and deploy-environment evidence;
- Cloudflare/Access/domain/Terraform/deployment role evidence;
- secret name/purpose/storage locator/custodian/rotation date, never value;
- joiner/mover/leaver and emergency exercise results;
- public contact, alert, renewal, and communication ownership;
- unresolved gaps linked to [OI-002](../controls/open-items.md), [OI-006](../controls/open-items.md), [OI-010](../controls/open-items.md), [OI-012](../controls/open-items.md), and [OI-013](../controls/open-items.md).

Canonical record location, access policy, retention, review interval, and accountable reviewer are **UNKNOWN**.

## Escalation, Recovery, And Unknowns

- If scope or appointment authority is unclear, stop and use [OI-001](../controls/open-items.md) plus the [Replacement Maintainer Aid](replacement-maintainer.md).
- If an owner or recovery path is missing, do not assume access is transferable; close [OI-002](../controls/open-items.md).
- If Cloudflare/Terraform/deployed state cannot be reconciled, stop live changes and use [OI-006](../controls/open-items.md) plus the [Recovery Aid](recovery.md).
- If revocation or recovery affects detection/response, coordinate through the [Observability Aid](observability.md).
- If any secret appears in Git or a public record, preserve evidence without spreading the value, follow the confidential security route, revoke/rotate under authorized provider procedure, and review downstream exposure.

Actual provider owners, backup administrators, MFA/recovery state, secret manager, break-glass path, Terraform-state custodian, registrar control, alert/contact owners, offboarding history, and exercise result remain **UNKNOWN**.
