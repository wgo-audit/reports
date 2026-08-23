# Isolated Rebuild Acceptance Aid

- Status: untested
- Selected precursor: [Quickstart](../documentation/tmp/website/content/docs/setup/quickstart.en.md), [Delivery And Quality Packet](../evidence/packets/delivery-and-quality.md), [Build, Deploy, And Request Path](../controls/architecture/diagrams/build-deploy-request-path.md), and [OI-004](../controls/open-items.md)

## Purpose And Evidence Boundary

This optional aid answers one operator question: **can a non-creator reconstruct and operate a new vanityURLs instance in independently controlled infrastructure with measured assistance and without touching the existing project/domain/demo?**

A successful exercise proves independent-fork operability only. It does not prove transfer of canonical GitHub repositories, release trust, `v8s.link`, Cloudflare accounts, Terraform state, public contacts, or community identity.

No clean checkout, dependency installation, check, build, deploy, smoke, rollback, recovery, or timing exercise was performed during the audit. Exercise owner, independent operator, isolated account/domain/repository, budget, fixture, tool versions, maximum assistance, expected outputs, timing thresholds, and cleanup authority are **UNKNOWN**.

## Existing Runbook And Coverage

The [Quickstart](../documentation/tmp/website/content/docs/setup/quickstart.en.md) is the primary rebuild procedure. It covers prerequisites, clone/detach, tools, dependencies, setup, Git publication, Cloudflare deployment connection, Access, edge protection, validation, and deployed smoke paths. Do not reproduce or silently alter it during the exercise.

Use these supporting sources:

- [Setup prerequisites](../documentation/tmp/website/content/docs/setup/_index.en.md) defines the required domain, GitHub, Cloudflare, workstation, and secret-storage boundaries.
- [Setup flowcharts](../documentation/tmp/website/content/docs/setup/flowcharts.en.md) explains installer branches and written files.
- [Repository layout](../documentation/tmp/website/content/docs/reference/repository-layout.en.md) defines product-owned, instance-owned, and generated paths.
- `product-code:docs/README.md` covers everyday operation after detachment.
- [Access control](../documentation/tmp/website/content/docs/customize/access-control.en.md), [Network protection](../documentation/tmp/website/content/docs/customize/network-protection.en.md), and the `product-code:RELEASE_WORKFLOW.md` deployment/rollback checklist cover the security and verification boundaries.

The Quickstart does not define an independent observer, creator-assistance budget, pass/fail record, isolated rollback/recovery exercise, canonical-versus-fork acceptance boundary, or cleanup evidence. This aid adds those controls without copying the procedure.

## Authority And Preconditions

Approve and record:

| Precondition | Required state | Current evidence |
|---|---|---|
| Exercise owner | Authorizes isolated resources, budget, stop, and cleanup | **UNKNOWN** |
| Independent operator | Has not relied on creator-only access or undocumented steps | **UNKNOWN** |
| Observer | Records assistance, failures, timing, and evidence without doing the work | **UNKNOWN** |
| Source pin | Cutoff/release commit or tag and verification policy | Audit pin exists; exercise source **UNKNOWN** |
| Isolated GitHub target | New repository/account boundary with no canonical secrets | **UNKNOWN** |
| Isolated Cloudflare target | New account/zone/Worker/Access boundary or approved sandbox | **UNKNOWN** |
| Isolated domain | Disposable or approved test hostname with no production traffic | **UNKNOWN** |
| Secret boundary | Exercise-only credentials stored outside Git | **UNKNOWN** |
| Fixture | Representative links, states, schedule/policy, localization, and protected paths | **UNKNOWN** |
| Toolchain | Exact OS, Git, Node.js, npm, jq, Terraform if used, Wrangler, and provider versions | **UNKNOWN** |
| Acceptance criteria | Required checks, behaviors, rollback/recovery, assistance/time limits | **UNKNOWN** |
| Cleanup/retention | What is retained as evidence and who removes isolated resources | **UNKNOWN** |

Never reuse production secrets, domain control, Terraform state, provider tokens, contact addresses, analytics accounts, or deployment connections. Keep analytics disabled for the baseline.

## Procedure And Stop Conditions

### 1. Establish the exercise record

Record operator, observer, source pin, environment boundary, start time, approved budget, fixture, acceptance criteria, allowed assistance, stop authority, and evidence location.

Classify help as:

- documentation link;
- clarification of public source;
- workaround discovered by operator;
- creator-only instruction;
- creator-performed action.

The last two prevent a “minimal creator involvement” pass unless the acceptance criteria explicitly permit them.

**Stop** if the environment could route production traffic, if a credential/domain/account belongs to the canonical service, or if the operator/observer cannot distinguish isolated and production targets.

### 2. Follow the primary Quickstart from a clean environment

The operator follows the [Quickstart](../documentation/tmp/website/content/docs/setup/quickstart.en.md) as written, using independently controlled resources. The observer records:

- each prerequisite and how it was discovered;
- every command outcome without copying secrets;
- unclear, stale, missing, or contradictory guidance;
- time spent and assistance category;
- files created or changed;
- source ownership and generated-artifact understanding.

Do not patch source or documentation during the measured run. Record a blocker first; any later correction begins a separately identified retry.

**Stop** if dependency installation is not approved, source provenance cannot be authenticated, setup requests production values, or a secret would enter Git/log evidence. [OI-010](../controls/open-items.md) remains a supply-chain stop condition.

### 3. Execute declared quality gates

Use the commands and groupings in `product-code:package.json` and `product-code:docs/README.md`. Record:

- exact command and source commit;
- tool/dependency versions and lockfile state;
- pass, fail, error, and skipped test counts;
- format/build/lint/complexity output;
- generated release-manifest identity and hashes;
- whether target reachability validation was enabled;
- unexpected working-tree changes.

This audit has no local result to use as an expected pass baseline. Expected counts and acceptable warnings are **UNKNOWN** until maintainers approve the acceptance record.

**Stop** on a failed required gate, unexplained generated change, unauthenticated source, or mismatch between instance-owned and generated paths.

### 4. Deploy only to the isolated target

Follow the Quickstart, [Access control](../documentation/tmp/website/content/docs/customize/access-control.en.md), [Network protection](../documentation/tmp/website/content/docs/customize/network-protection.en.md), and the existing deployment checklist. Record repository/deployment connection, target account/zone/hostname, deployment identifier, intended edge controls, and log evidence.

If Terraform is included, use the public `terraform-source:README.md` only as reference. Create an exercise-specific state/backend; never import or target canonical resources.

**Stop** if account, zone, hostname, state backend, deployment target, or rollback path is ambiguous.

### 5. Verify representative behavior

Use the primary Quickstart and release checklist to verify the approved fixture across:

- active redirect and expected status/target;
- missing or hidden slug;
- representative lifecycle state;
- generated registry/source timestamp or manifest;
- public home/lookup/status pages;
- raw runtime assets remaining inaccessible;
- Access protection for localized stats/tests with allowed and denied identities;
- Cloudflare custom domain and unintended preview/`workers.dev` exposure;
- edge security evidence;
- analytics remaining disabled.

Exact URLs, expected statuses, schedule time, language set, threshold, and evidence screenshots/logs are **UNKNOWN** until the fixture is approved.

**Stop** if a protected path is public, a runtime asset is exposed, an unexpected target is returned, or the deployed artifact cannot be traced to the exercise source.

### 6. Exercise rollback and reconstruction

In the isolated environment only:

- identify the current and previous deployment/commit;
- follow the existing rollback checklist;
- repeat the same smoke fixture;
- demonstrate reconstruction of generated output from human-authored Git source;
- verify that no production resource or credential was touched.

Exercise scenario and failure injection are **UNKNOWN**. Use a safe planned change or tabletop event; do not create a real outage or destructive state loss.

**Stop** if rollback cannot be performed without creator action, if the last-known-good artifact is unclear, or if the operator would need canonical Terraform state/secrets.

### 7. Evaluate the result

Record one result:

- `pass-independent-instance`;
- `pass-with-documented-assistance`;
- `blocked-documentation`;
- `blocked-source-or-tooling`;
- `blocked-provider-or-authority`;
- `failed`.

Do not convert a pass into evidence of canonical takeover. The [Replacement Maintainer Aid](replacement-maintainer.md), [IAM And Credential Control Aid](iam-and-credential-control.md), [Recovery Aid](recovery.md), and [Observability Aid](observability.md) govern that broader outcome.

## Expected Evidence And Records

Retain:

- approved exercise charter and isolation proof;
- operator/observer identities and independence statement;
- source pin and release-verification result;
- exact tool/provider versions;
- prerequisite, timing, and assistance log;
- commands and pass/fail/error/skipped results;
- generated-manifest provenance;
- isolated repository, deployment, domain, Access, and edge evidence;
- smoke fixture and actual results;
- rollback/reconstruction result;
- evidence that analytics and production credentials/resources were not used;
- documentation defects and retries;
- final result, exclusions, and owner acceptance;
- links to [OI-004](../controls/open-items.md), [OI-007](../controls/open-items.md), [OI-010](../controls/open-items.md), and [OI-011](../controls/open-items.md) where gaps remain.

Evidence location, retention, acceptable assistance, time threshold, test counts, and approving owner are **UNKNOWN**.

## Escalation, Recovery, And Unknowns

- If a procedure needs creator-only information, record the exact gap and classify the exercise as blocked or assisted; do not hide the dependency.
- If source verification fails, stop and close [OI-010](../controls/open-items.md) before executing refreshed code.
- If deployment or rollback fails, preserve evidence and use the [Recovery Aid](recovery.md) only within the isolated boundary.
- If access or secret handling is unclear, stop and use the [IAM And Credential Control Aid](iam-and-credential-control.md).
- If signals or alert routing cannot be tested, use the [Observability Aid](observability.md); do not claim operational readiness.

Exercise owner, operator, observer, isolated resources, fixture, toolchain, expected outputs, thresholds, cleanup plan, measured assistance, and execution result remain **UNKNOWN**.
