# Security and Privacy

## Audit Question, Depth, And Evidence Boundary

This detailed review asks whether identity, authorization, bearer identifiers,
credentials, payloads, privacy, edge/runtime defaults, dependencies, release
provenance, and product-abuse controls make Healthchecks supportable as Acme's
core job monitor across pull, make, and buy. The cutoff is 2026-08-19. Evidence
is bounded to `HC-CODE-001` commit
`fafac59eeb00cfdc87166242544fa071ecad1723`, directly relevant repository
documentation/configuration, local read-only tool results, and current public
Healthchecks.io privacy, legal, and API documentation. Reusable evidence is
[E-020 through E-026](../../evidence/evidence-ledger.md).

This was a source and public-material review, not penetration testing,
certification, a live configuration assessment, or proof of non-compromise. No
Acme deployment, identity provider, network, logs, secret metadata, payloads,
staff capability, vendor agreement, or hosted internals were observed.

## Coverage And Material Gaps

The review traced account authentication, WebAuthn/TOTP, project roles, API-key
validation, ping capability routes, proxy-auth headers, notification/integration
configuration, logging, relational/object body storage, retention/deletion,
callback and SMTP surfaces, outbound-request restrictions, Docker/runtime
defaults, dependencies, CI/image publication, SBOM production, and public
hosted data-use terms.

The material proof routes are [OI-004](../../controls/open-items.md#OI-004) for
hosted controls and terms, [OI-010](../../controls/open-items.md#OI-010) for a
deployed self-host baseline, and [OI-011](../../controls/open-items.md#OI-011)
for capability, payload, and offboarding lifecycle. OI-008 remains the immutable
release/trust-anchor consumer gate. Live DNS/TLS/WAF/reachability evidence was
unavailable, so no live edge exposure view was created.

### Executed Checks

| Working directory | Command/tool | Intended coverage | Result | Dependency/installation state | Bounded conclusion |
|---|---|---|---|---|---|
| `HC-CODE-001:./` | Existing-tool inventory across eight named security tools | Available security tooling | Pass: pip-audit 2.10.0 present; seven unavailable | No installation authorized | Scanner coverage is incomplete. |
| `HC-CODE-001:./` | Four `pip-audit` invocations detailed in the tooling view | Direct dependency advisories | One bounded pass: no known vulnerabilities in direct production pins; three errors | Development set unpinned; transitive resolution disabled; one restricted-network failure | Not a clean transitive, development, image, or exploitability result. |
| `HC-CODE-001:./` | Git pin and signature display | Source identity and local signer verification | Pin passed; local signature verification unavailable | Isolated environment lacked a usable GPG keybox | Commit identity is proven; signer trust is not. |
| Audit root | `python3 core:scripts/validate_audit_structure.py <audit-root>` | Artifact shape and references | Pass: 0 errors, 0 warnings | Existing Python; no installation | Required structure, IDs, table schemas, handoff headings, and portable-path rules passed; conclusions remain evidence-bounded. |

Security-tool totals are five checks: one inventory plus four pip-audit
invocations. Provenance-tool total is one. Project test execution did not start:
0 passed, 0 failed, 0 errors, and 0 skipped. Exact commands and limits are in
the [tooling view](../../controls/security/supply-chain-and-tooling.md).

## Key Findings

| Finding | Severity | Effort | Evidence links | Confidence and limitation | Consequence | Taxonomy |
|---|---|---|---|---|---|---|
| Ping UUIDs and project ping-key/slug paths are bearer capabilities that can submit success, failure, start, log, or exit status without a user/API session. UUIDs do not rotate independently; a project ping key expands blast radius and slug mode can auto-create checks. | High | M | [E-021](../../evidence/evidence-ledger.md#E-021), [boundary view](../../controls/security/identity-secret-and-data-boundaries.md) | High for source semantics; no Acme leak or abuse observed | Exposure can suppress a real outage with forged success, trigger false alerts, or create misleading monitors. | project-control:capability-secret |
| Enabling optional shell integration gives a regular read/write project member the ability to store an arbitrary command executed as the application OS user. It is disabled by default. | High | S | [E-023](../../evidence/evidence-ledger.md#E-023) | High for the conditional source path; Acme configuration unknown | A member or compromised session can execute commands with application data/environment access. | CWE-78 |
| The reference deployment is not secure-by-default for production: source defaults include debug/open registration, the sample secret is a placeholder, the sample exposes HTTP port 8000 without TLS, and source does not set a complete secure-cookie/HSTS/CSP baseline. Proxy identity/scheme/IP controls depend on a correctly stripping sole proxy. | High | M | [E-023](../../evidence/evidence-ledger.md#E-023), [OI-010](../../controls/open-items.md#OI-010) | High for defaults/docs; live Acme edge/config unknown | Deploying the sample as-is can expose administrative/data surfaces, weaken session transport, or allow forged proxy identity/metadata. | OWASP ASVS V14 |
| Ping bodies, metadata, integration credentials, TOTP material, and provider diagnostics cross database, log, notification, backup, and optional object-store boundaries. Source-level field encryption and a general application-log retention policy were not found; object deletion needs a separate prune step. | High | M | [E-022](../../evidence/evidence-ledger.md#E-022), [boundary view](../../controls/security/identity-secret-and-data-boundaries.md) | High is driven by stored integration credentials/TOTP verifier material plus potentially sensitive bodies; actual storage encryption and payload classes are unknown, and this does not assert every Acme ping is sensitive | A DB, backup, log, or broad project-view compromise can expose credentials or customer/job data; deletion can be incomplete. | CWE-312 |
| Buy changes rather than removes the visibility boundary: public hosted material discloses collection of check/account/log metadata, notification credentials and client IPs, named processors, international processing, and backup retention up to two months; standard terms disclaim uninterrupted, secure, or available service. | High | M | [E-026](../../evidence/evidence-ledger.md#E-026), [OI-004](../../controls/open-items.md#OI-004) | High for public terms; negotiated Acme agreement and hosted controls unknown | Without minimization/vendor review, a core monitor can reveal operational cadence, job identity, payload, and credentials without an evidenced service/security commitment. | none |
| The delivery-status callback accepts a recent notification UUID without a provider signature; possession of that opaque one-hour identifier can record an error and optionally disable the channel. | Medium | S | [E-021](../../evidence/evidence-ledger.md#E-021) | High for source verifier absence; reachability/identifier disclosure unknown | A leaked callback identifier can disable an alert route when it is needed. | CWE-345 |
| Dependency/build inputs are not reproducibly trust-bound: direct Python packages are pinned but unhashed, development pins incomplete, Actions/base images use mutable tags, and SBOM production has no located Acme consuming verifier. | Medium | M | [E-024](../../evidence/evidence-ledger.md#E-024), [E-025](../../evidence/evidence-ledger.md#E-025), [tooling view](../../controls/security/supply-chain-and-tooling.md) | High for repository declarations; live GitHub/registry and transitive/image advisories unknown | Pull can admit an unintended build; make increases exposure on every upstream merge and Acme release. | SLSA: build integrity |
| Self-host ping ingress has a body limit by default, but no source rate limiter was found for public ping or optional unauthenticated SMTP ingestion; unlimited bodies and enabling SMTP/private-reach modes broaden resource and SSRF exposure. | Medium | M | [E-021](../../evidence/evidence-ledger.md#E-021), [E-023](../../evidence/evidence-ledger.md#E-023) | High for source paths; edge limits/enabled features unknown | Floods can consume storage/worker capacity and increase false or delayed monitoring; bypass modes can reach unintended networks. | CWE-400 |

## Vulnerability-Class Checklist Verdicts

These are source-review verdicts, not penetration-test or certification results.

| Class | Verdict | Locator and rationale |
|---|---|---|
| Canonicalization | finding | Forwarded IP/scheme and optional remote-user headers are consumed as trust inputs; stripping is delegated to the proxy (`HC-CODE-001:hc/api/views.py:197-211`; `HC-CODE-001:hc/accounts/middleware.py:30-84`). |
| Injection sinks | finding | ORM/templates use framework encoding in sampled paths, but enabled shell integration intentionally reaches `os.system` with a project-member command (`HC-CODE-001:hc/integrations/shell/transport.py:13-52`; CWE-78). |
| Redirect or forward targets | verified | Login `next` is restricted to a relative known route and generic HTTP requests constrain protocols; redirect sockets retain private-IP checks (`HC-CODE-001:hc/accounts/views.py:59-73`; `HC-CODE-001:hc/lib/curl.py:51-206`). |
| Deserialization and parsing | finding | Ping bodies default to a 10,000-byte bound but can be unlimited; optional SMTP accepts message bytes without an evidenced application size/depth limit (`HC-CODE-001:hc/settings.py:270-276`; `HC-CODE-001:hc/api/management/commands/smtpd.py:110-165`; CWE-400). |
| Verifier correctness | finding | WebAuthn/TOTP and timestamped magic links use verifier helpers, but notification status callbacks use only a recent opaque UUID and no provider signature (`HC-CODE-001:hc/api/views.py:819-857`). |
| Key lifecycle | finding | Project API/ping keys can rotate, but per-check UUIDs are immutable and legacy plaintext API keys remain accepted (`HC-CODE-001:hc/accounts/models.py:400-440,538-593`; `HC-CODE-001:hc/api/models.py:191-197`). |
| Authorization placement | verified | Reviewed management handlers apply project-scoped read-only/read-write checks and role permissions (`HC-CODE-001:hc/api/decorators.py:33-118`; `HC-CODE-001:hc/accounts/models.py:601-625`). Capability ping routes are public-by-design. |
| Response headers | finding | Django clickjacking/content-type middleware is present, but no repository production baseline was found for CSP, HSTS, secure session/CSRF cookies, or referrer policy (`HC-CODE-001:hc/settings.py:138-149`). |
| CORS | verified | API/ping responses permit wildcard origins but do not enable credentialed-cookie CORS; management handlers still require a bearer API key. Browser-held keys remain outside the safe client model (`HC-CODE-001:hc/api/views.py:179-244,462-477`; `HC-CODE-001:hc/api/decorators.py:33-93`). |
| Cache and CDN behavior | unknown | No approved live CDN/cache policy exists. Effective proxy/CDN behavior cannot be established from the repository. |
| Request construction | finding | Generic pycurl restricts protocols, redirects, TLS, and private IPs by default, but Apprise can bypass the private-IP guard and shell is a command sink when enabled (`HC-CODE-001:hc/lib/curl.py:51-206`; `HC-CODE-001:hc/api/apps.py:73-80`). |
| Data minimization | finding | Full ping bodies/metadata can be persisted and forwarded; hosted public material discloses additional account/log/processor data. No Acme payload contract exists ([E-022](../../evidence/evidence-ledger.md#E-022), [E-026](../../evidence/evidence-ledger.md#E-026)). |
| Secrets in motion | finding | Ping capabilities are URL paths; API keys may be accepted in POST JSON; webhooks may use HTTP and carry headers/bodies (`HC-CODE-001:hc/api/decorators.py:33-93`; `HC-CODE-001:hc/integrations/webhook/forms.py`; `HC-CODE-001:hc/integrations/webhook/transport.py:13-93`). |
| Protection claims | unknown | Public hosted descriptions are not evidence of hosted control operation; self-host storage, backup, deletion, and TLS depend on an unobserved deployment. |
| Fail posture | finding | Security-relevant source defaults include debug/open registration and a placeholder secret; private-IP protection and dangerous integrations are configurable, while proxy safety is external ([E-023](../../evidence/evidence-ledger.md#E-023)). |
| Trust-anchor consumption | finding | Release SBOM output and public signature presentation have no located Acme consuming verifier; local signature trust could not be verified ([tooling view](../../controls/security/supply-chain-and-tooling.md)). |
| Diagnostic surfaces | finding | Admin/status routes are registered, metrics is key-guarded, and debug defaults on in source; production exposure/config is unknown (`HC-CODE-001:hc/urls.py:15-20`; `HC-CODE-001:hc/api/views.py:860-883`; `HC-CODE-001:hc/settings.py:68-75`). |
| Dependency and build integrity | finding | Requirements lack hashes/transitive lock, Actions/base images use mutable tags, and the available audit covered only direct production pins ([E-024](../../evidence/evidence-ledger.md#E-024), [E-025](../../evidence/evidence-ledger.md#E-025)). |
| Product-class abuse | finding | Dominant paths are forged/suppressed heartbeats, alert floods, slug auto-provisioning, body/storage exhaustion, callback channel disablement, integration SSRF, and optional shell execution. Existing controls are partial and do not close OI-010/OI-011. |

## Mandate-Relevant Strengths

- Project-scoped authorization is consistently applied to reviewed management
  handlers, new API keys use prefix plus HMAC digest, Argon2 is first, and
  WebAuthn/TOTP plus sudo confirmation provide a sound authentication base
  ([E-020](../../evidence/evidence-ledger.md#E-020)).
- Generic integration HTTP uses TLS verification, HTTP(S)-only protocols,
  bounded redirects, and a socket-level private-IP block by default. Shell and
  Apprise are disabled by default, and the container runs non-root
  ([E-023](../../evidence/evidence-ledger.md#E-023)).
- Source search found no automatic update mechanism or general analytics
  exporter; optional StatsD is configuration-driven. This is bounded to the
  approved tree and does not establish hosted telemetry.
- Upstream CI at the pin is broad and green, requests an SBOM, and public release
  metadata presents signed commits. These are useful inputs once Acme builds a
  verifier/promotion gate; they are not that gate.

### Decision Insights

1. **Pull is the security-default candidate, but only as a hardened deployment,
   not the sample.** The highest-impact gaps—TLS/proxy discipline, feature-off
   policy, secret storage, minimization, membership control, and immutable
   promotion—can be implemented without a fork. Smallest action: close
   OI-010/OI-011 and OI-008 against pinned upstream source/image.
2. **Make needs a demonstrated source-level requirement.** Defensible triggers
   include narrower key/integration roles, field-level encryption, independent
   per-check rotation, signed callbacks, or a bounded ingress guard unavailable
   operationally. Test each control against pull; fork only the failing control.
3. **Buy is reviewable only under an explicit data contract.** Removing bodies
   is the strongest low-cost visibility reduction, but the vendor still sees
   timing, client IP, account/check metadata, and hosted integration credentials.
   Define no-body/opaque-name/scoped-relay rules, then close OI-004.
4. **Capability lifecycle is common to every option.** A leaked UUID can falsify
   monitoring regardless of host. Use one UUID per job, no critical slug
   auto-provisioning, path redaction, and tested recreate/migrate after exposure.

## Selected Outputs

- Triggered: [identity, secret, and data boundaries](../../controls/security/identity-secret-and-data-boundaries.md)
- Triggered: [supply-chain and tooling results](../../controls/security/supply-chain-and-tooling.md)
- Required: vulnerability-class verdicts in this report

The named edge exposure view was not created because its trigger requires
approved live DNS, TLS, ingress, WAF, certificate, or reachability evidence.
The source-bounded flow shows the unknown edge without substituting repository
defaults for live state.

## Material Omissions, Unknowns, And Auditor Questions

No Security and Privacy question is raised to the auditor. The unknowns require
verification rather than executive assertion: OI-004 owns hosted security,
privacy, and contract evidence; OI-010 owns selected self-host edge,
configuration, storage, and secret controls; OI-011 owns job payload and
capability lifecycle. Team capability remains intentionally untested.

**Documented outside audited scope; not independently verified.** Public hosted
privacy/breach-policy pages name processors and processes, but agreements,
audit reports, control operation, production architecture, and Acme-negotiated
terms were not approved sources. The smallest expansion is OI-004's bounded
vendor review.

## Reconciliation

There was no prior Security and Privacy report. No material contradiction was
found between source and repository documentation. Public hosted terms describe
a separately operated service and are not proof about self-host source or vice
versa.

Two collectors each reached one terminal `completed` outcome and wrote no audit
state: `identity_boundaries` returned identity/secret/data evidence and
`edge_runtime` returned source-only edge/runtime evidence after a transient
execution-backend failure. Supply chain was reviewed directly. The single
required `security_quality` worker reached one terminal `completed` outcome,
wrote no state, and its feedback was applied in one revision pass. OI-004 was
raised from P2 to P1 because it is a buy production gate. After revision, the
canonical structural validator passed with 0 errors and 0 warnings. No child
task remains running, multiply terminated, or ambiguously correlated.

## Bounded Conclusion And Downstream Guidance

Healthchecks has a credible security base—project authorization, strong password
hashing/MFA options, hashed new API keys, outbound private-network blocking, and
dangerous features off by default—but none of the three options is
security-approved from current evidence. Pull is preferable to make unless a
source-level gap is demonstrated; it still requires production hardening,
data/capability controls, and immutable promotion. Make inherits every control
plus fork-security ownership. Buy reduces hosting work but adds an unverified
vendor/processor/contract boundary and does not remove capability-URL risk.

Business Continuity should use credential/control-transfer and hosted-dependency
findings; Expense Exposure and Maintenance Cost should price OI-004, OI-008,
OI-010, and OI-011. They must not infer live exposure, acceptable hosted
controls, zero vulnerabilities, absence of leakage, or team readiness.
