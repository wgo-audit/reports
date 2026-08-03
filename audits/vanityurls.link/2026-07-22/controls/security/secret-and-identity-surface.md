# Secret, Identity, And Privacy Surface

## Evidence Boundary

This view uses cutoff-pinned public source and documentation through July 22, 2026. It records variable names and redacted roles only. No secret values, authenticated account settings, history-wide secret scanner, token validation, provider console, revocation, offboarding, or privacy/compliance assessment was approved. A bounded common credential-pattern search of the approved working-tree source returned no matches; this is not proof that repository history or external systems are free of secrets.

## Surface Map

| Surface | Data/credential role | Declared control | Owner/custody evidence | Offboarding/recovery evidence | Position |
|---|---|---|---|---|---|
| GitHub repositories/organization | Admin, merge, workflow, release, ruleset authority | CODEOWNERS, maintainer declarations, least workflow permissions, desired branch/tag rules | Named maintainers only; actual owners/admins unknown | Unknown | Transfer-critical external identity surface |
| Release signing | Trusted release identity and signed tags | Two pinned signer identities; manual gitsign procedure | Declared identities; current access/recovery unknown | Unknown | Trust design exists; successor continuity unproved |
| Cloudflare account/zone/Worker | DNS, deploy, logs, WAF, Access, secrets | Terraform intent, Wrangler config, least-privilege token guidance | Actual owners/admins/tokens unknown | Unknown | Transfer-critical external control plane |
| Access audience/team/JWKS | Private stats/tests authentication | Audience stored as Worker secret; team domain non-secret; JWT signature/audience/claims verification and fail-closed behavior | Secret value and allowed identities excluded; role owner unknown | Key refresh implemented; account recovery/offboarding unknown | Strong source control; live effectiveness unknown |
| Terraform state/variables | Resource identity, imports, account-bound values, maintainer allow-list | Ignored from Git; environment token; provider lock | Backend/state/token custodian unknown | Restore/rotation unknown | Public code is insufficient for takeover |
| Domain registrar/DNS | Existing public service identity and routing | Cloudflare authoritative DNS documented | Owner, renewal, recovery, transfer unknown | Unknown | Highest community-continuity dependency |
| Analytics collection | Optional URL/referrer/UA, slug/target host, state/schedule, country/colo/correlation; optional IP mode | Disabled by default; asynchronous send; truncated/none guidance; provider credentials separated | Reference instance declares disabled; provider account owners unknown | Retention/deletion/rotation unknown | Baseline minimizes exposure; enabling adds a separate privacy boundary |
| Public operator/contact metadata | Legal/operator/security/privacy/abuse contacts | Generated configuration/public pages and `security.txt` | Values are intentionally public; ongoing consent/monitoring unknown | Replacement procedure only partly documented | Necessary accountability with PII/contact-staleness risk |
| Local `.dev.vars` and helper credentials | Development/provider secrets | Git-ignored; installer says it does not read/write/log secrets; diagnostic authorization redaction declared | Workstation custody unknown | Rotation/deletion unknown | Good repository boundary; no operational proof |

## Material Control Gaps

- OI-002/OI-006: prove redacted ownership, least privilege, successor access, recovery, revocation, and state custody.
- OI-003: create the governed transfer/offboarding/incident procedure after synthesis approval.
- OI-010: enforce signed-upgrade verification before executing refreshed upstream code and correct conflicting security documentation.
- OI-004: validate Access fail-closed, analytics-disabled, rollback, and successor paths in an isolated environment.
