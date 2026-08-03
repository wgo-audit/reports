# Replacement Maintainer Transition Aid

- Status: untested
- Selected precursor: [Executive Summary](../executive-summary.md), [Continuity And Transfer Matrix](../controls/continuity/continuity-and-transfer-matrix.md), [Successor Time-To-Safety Map](../controls/maintenance/time-to-safety.md), and [OI-001–OI-005](../controls/open-items.md)

## Purpose And Evidence Boundary

This aid answers one operator question: **what must be accepted and evidenced before a non-creator can become a vanityURLs maintainer without depending on creator-only knowledge or access?**

It applies separately to:

1. **Independent-fork maintainership:** accepting responsibility for a separately controlled fork and instance.
2. **Canonical maintainership:** accepting responsibility for the existing `vanityURLs` repositories, release trust, public documentation, `v8s.link` domain, and demo service.

The first is technically plausible from public source. The second is not transfer-ready on evidence through July 22, 2026. No successor appointment, access transfer, build, release, deployment, recovery, or offboarding procedure was executed during the audit. Current appointing authority, accepted successor, exercise date, assistance threshold, and canonical continuity scope are **UNKNOWN**.

This aid contains no credentials and grants no authority. Use the [IAM And Credential Control Aid](iam-and-credential-control.md) for access; the [Recovery Aid](recovery.md) for service recovery; the [Observability Aid](observability.md) for response ownership; and the [Isolated Rebuild Aid](isolated-rebuild.md) for independent technical acceptance.

## Existing Runbook And Coverage

No existing document provides a complete cross-repository maintainer handover.

Applicable partial sources are:

- [`.github/GOVERNANCE.md`](../../.github/GOVERNANCE.md) defines users, contributors, maintainers, decision-making, and invitation to maintainership. It does not define nomination criteria, approval authority, probation, cross-repository scope, access transfer, conflict handling, revocation, or offboarding. It also contradicts its own two-person roster by saying the project is maintained by one individual.
- [`.github/MAINTAINERS.md`](../../.github/MAINTAINERS.md) lists product maintainers and trusted release signers. It is not a cross-repository owner or successor register.
- [`.github/repository-rules.md`](../../.github/repository-rules.md) defines desired product-repository protections. It explicitly says administrative application and exported rulesets remain external.
- [`RELEASE_WORKFLOW.md`](../../RELEASE_WORKFLOW.md) is the primary product release procedure. It covers review, checks, signed tags, release publication, deployment, and rollback; it does not transfer signer or administrative authority.
- The [Quickstart](../documentation/tmp/website/content/docs/setup/quickstart.en.md) and [`docs/README.md`](../../docs/README.md) are the primary independent-instance setup and everyday-operation procedures.

This transition aid complements those sources with acceptance, authority, and stop conditions. It does not reproduce their commands.

## Authority And Preconditions

Do not begin access transfer until the following record exists:

| Precondition | Required state | Current evidence |
|---|---|---|
| Continuity scope | Community-visible decision distinguishing independent fork from canonical continuity | **UNKNOWN**; [OI-001](../controls/open-items.md) |
| Appointing authority | Named role authorized to appoint and remove maintainers for each repository and service asset | **UNKNOWN** |
| Candidate | Named successor who has explicitly accepted the proposed scope and volunteer obligations | **UNKNOWN** |
| Sponsor/observer | Current maintainer or community-approved observer accountable for the transition record | **UNKNOWN** |
| Repository scope | `code`, `website`, `v8s-config`, `v8s-link`, and any additional canonical repository listed with role expectations | Four audited repositories known; final canonical scope **UNKNOWN** |
| External asset scope | GitHub, release signing, Cloudflare, Access, DNS/domain, Terraform state, deployment, contacts, alerts, and renewals mapped to accountable roles | **UNKNOWN**; [OI-002](../controls/open-items.md), [OI-006](../controls/open-items.md), [OI-013](../controls/open-items.md) |
| Security baseline | Least privilege, phishing-resistant authentication for privileged roles, recoverable second administrator, and offboarding authority | Declared intent; applied state **UNKNOWN** |
| Acceptance environment | Isolated account/domain/repository or explicitly authorized existing-service environment | **UNKNOWN** |
| Success criteria | Maximum creator assistance, required checks, release/deploy/recovery evidence, observation period, and stop authority | **UNKNOWN** |

The candidate must receive links to the [audit index](../index.md), [Technical Lead Notes](../technical-lead-notes.md), [cross-repository boundary](../controls/architecture/diagrams/cross-repository-control-boundary.md), [open-item register](../controls/open-items.md), and all five operator aids before accepting operational responsibility.

## Procedure And Stop Conditions

### 1. Record the appointment boundary

- State whether the appointment covers an independent fork, the canonical project, or both.
- List every repository, service, domain, release identity, contact, and vendor surface in scope.
- Name who can approve the appointment, who can revoke it, and who resolves conflicts.
- Publish the non-sensitive role decision where contributors can find it.

**Stop** if continuity scope or appointing authority is **UNKNOWN**. A candidate may continue an independent fork, but must not be described as the canonical maintainer without a valid authority decision.

### 2. Complete evidence orientation

The candidate reviews the four-repository map, ADR/PDR registers, product check design, release workflow, security model, instance workflow, Terraform intent, public documentation workflow, and canonical open items. Record:

- questions answered directly by source;
- questions requiring creator explanation;
- undocumented dependencies;
- contradictions or stale links;
- areas the candidate declines to own.

**Stop** if a material behavior, public promise, or control cannot be traced to source or assigned to an accountable owner. Route the gap to the existing [open-item register](../controls/open-items.md); do not create a private parallel backlog.

### 3. Grant and verify least-privilege authority

Use the [IAM And Credential Control Aid](iam-and-credential-control.md). Grant only the role needed for the agreed scope, then verify:

- repository read/review/merge/admin abilities as applicable;
- branch/tag protection visibility and change authority;
- release-signing eligibility and recovery;
- cloud, Access, DNS/domain, Terraform-state, deployment, contact, alert, and renewal access where canonical service operation is in scope;
- ability to remove or disable the candidate through a separate authorized path.

Use redacted role and recovery records; never copy secret values into this packet.

**Stop** if one person is the sole recoverable administrator for a transfer-critical surface, if a departed person cannot be revoked, or if the candidate must use another person’s identity or credential.

### 4. Demonstrate technical maintainership

For an independent fork, use the [Isolated Rebuild Aid](isolated-rebuild.md). For canonical maintainership, add a reviewed product change and release rehearsal using the primary [`RELEASE_WORKFLOW.md`](../../RELEASE_WORKFLOW.md).

At minimum, record whether the candidate can:

- explain source ownership and generated artifacts;
- run the declared check and report pass, fail, error, and skipped counts;
- review a representative pull request across product and documentation;
- identify which operational changes belong in `v8s-config` and `v8s-link`;
- verify release provenance before using upstream code;
- produce or rehearse a signed release without moving an existing tag;
- deploy only to an approved isolated target;
- smoke, observe, roll back, and recover through the linked aids.

The exact candidate change, fixture, tool versions, acceptable assistance, and acceptance threshold are **UNKNOWN** until an exercise is approved.

**Stop** before any release or upgrade that cannot authenticate its source. [OI-010](../controls/open-items.md) remains open.

### 5. Demonstrate operational ownership

Using the [Recovery Aid](recovery.md) and [Observability Aid](observability.md), the candidate must show that:

- an incident can reach two independent recipients;
- a responder with authority can identify the affected layer;
- a last-known-good commit/deployment and source registry can be identified;
- rollback and recovery can be authorized without creator-only action;
- domain renewal, public contacts, and security intake remain owned;
- communications have an accountable publisher.

**Stop** canonical-service acceptance if Terraform state/import coverage, deployed-commit equivalence, domain/renewal custody, alert delivery, or recovery authority remains **UNKNOWN**.

### 6. Accept, limit, or reject the role

The candidate and appointing authority record one outcome:

- `accepted-independent-fork`;
- `accepted-canonical-project`;
- `accepted-with-explicit-exclusions`;
- `not-accepted`.

An acceptance with exclusions must identify the accountable owner for every excluded critical surface. Do not label an unexecuted procedure or incomplete access transfer as successful.

## Expected Evidence And Records

Retain one redacted transition record containing:

- approved continuity scope and appointment authority;
- candidate acceptance and exclusions;
- cross-repository role map;
- redacted access/administrator/recovery matrix;
- evidence-orientation questions and creator assistance log;
- build/check results with pass, fail, error, and skipped counts;
- reviewed change and release rehearsal record;
- isolated deployment, smoke, rollback, recovery, and alert exercise links;
- current public contact, incident, renewal, and communication owners;
- unresolved stop conditions linked to canonical open items;
- final decision and review/expiry date.

Record location, retention period, reviewer, and next review date are **UNKNOWN**.

## Escalation, Recovery, And Unknowns

- If appointment authority is disputed, stop canonical transfer and resolve [OI-001](../controls/open-items.md) publicly.
- If access cannot be recovered or revoked, stop and use [OI-002](../controls/open-items.md) plus the [IAM And Credential Control Aid](iam-and-credential-control.md).
- If live state or deployed source cannot be reconciled, stop and use [OI-006](../controls/open-items.md) plus the [Recovery Aid](recovery.md).
- If alerts or public intake are unowned, stop operational acceptance and use [OI-012](../controls/open-items.md) plus the [Observability Aid](observability.md).
- If a clean non-creator exercise has not completed, retain the project status “plausible, not proven easy”; use [OI-004](../controls/open-items.md) and the [Isolated Rebuild Aid](isolated-rebuild.md).

Current successor, appointing authority, canonical asset scope, access owners, exercise owner, time-to-safety, assistance threshold, and acceptance date remain **UNKNOWN**.
