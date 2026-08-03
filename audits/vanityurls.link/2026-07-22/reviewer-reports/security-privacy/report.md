# Security And Privacy

## Audit Question, Depth, And Evidence Boundary

This detailed review asks what material identity, credential, public/private route, supply-chain, privacy, PII, and operating-control risks are evidenced. It uses cutoff-pinned source/configuration, Worker tests as source intent, Terraform/Wrangler declarations, public documentation, governance/release records, and Architecture/Code Quality/Product handoffs through July 22, 2026. No secret values, authentication, live DNS/TLS/WAF/Access inspection, penetration test, dependency vulnerability scan, history-wide secret scan, compliance assessment, or credential action was performed.

## Coverage And Material Gaps

Coverage includes redirect validation, public lookup, private stats/tests, raw runtime assets, CSP/headers/CORS, Access JWT verification, WAF/rate limits, secrets/config variables, GitHub/release identity, upgrade supply chain, Terraform state, public contacts, analytics payloads/IP modes, and incident intake. Material gaps are live control effectiveness, ownership/offboarding/recovery, domain and state custody, alert routing, provider retention, specialist privacy/security acceptance, and verified signed-upgrade enforcement.

## Key Findings

| Finding | Evidence links | Confidence and limitation | Consequence |
|---|---|---|---|
| The source security model is deliberate and defense-in-depth: build-time target validation, runtime protocol/credential/path guards, strict product CSP, sandboxed custom HTML, hidden runtime files, Access-protected operations, and intended edge controls. | [Edge view](../../controls/security/diagrams/edge-exposure-view.md), [PDR-005/PDR-007](../../controls/product/pdr-register.md), Worker/header/Terraform source | High for implementation and intended configuration; no live effectiveness or penetration test. | A successor inherits clear control boundaries rather than an ad hoc redirect script. |
| Access verification fails closed and tests cover malformed, wrong-audience, invalid-claim/signature, cached-key, and key-rotation cases. | Worker/test source; [change-safety matrix](../../controls/quality/change-safety-matrix.md), [E-014](../../evidence/evidence-ledger.md) | High for source test intent; tests not executed and applied policy/secret unknown. | Private operational surfaces are designed safely, but takeover still depends on external identity and secret control. |
| Sensitive runtime/state material is intentionally outside public Git; a bounded common credential-pattern working-tree search found no matches. | [Secret/identity surface](../../controls/security/secret-and-identity-surface.md), `.gitignore`, setup/security docs | Moderate: pattern search was bounded, not history-wide or a specialist scanner; external custody unknown. | Public source avoids obvious credential embedding, but continuity cannot be inferred because the required private custody inventory is absent. |
| Analytics is off in the reference instance and optional by design; enabling it can transmit URL/referrer/UA, event metadata, and—by operator choice—truncated, omitted, or full IP data. | [PDR-007](../../controls/product/pdr/PDR-007-private-operations-and-optional-analytics.md), analytics docs/source, `v8s-link/wrangler.toml` | High for source contract; provider configuration, retention, deletion, and live events unknown. | The baseline is privacy-minimizing; each operator who enables analytics assumes a separate privacy and vendor-governance obligation. |
| Release tags are intended to be signed, but the upgrade tool resolves/fetches a stable tag and does not itself verify its signature before refreshed code can run; an older security-model page incorrectly says the default is a mutable branch. | `scripts/upgrade.mjs`; `scripts/lib/upgrade-source.mjs`; source ADR 0015; website security-model/upgrading docs; [ADR-005](../../controls/architecture/adr/ADR-005-release-and-delivery-trust-chain.md) | High for source/doc conflict; actual tag protection/signatures not verified. | A compromised upstream/tag-control path could affect instances; successor operators may misunderstand the present trust guarantee. |
| Incident intake is email/contact based, but public evidence has no responder roster, severity/escalation model, monitored-contact proof, or offboarding path. | [E-015](../../evidence/evidence-ledger.md), [recovery packet](../../evidence/packets/recovery-and-operations.md) | High for public declarations; private process may exist. | Sudden maintainer departure can turn technically sound controls into unowned security and privacy obligations. |

### Decision Insights

- **Make signed-upgrade verification a stop condition, not only a release aspiration.** Stable tags reduce mutability but do not authenticate themselves; the upgrade may run refreshed code. Smallest action: OI-010 with automated or mandatory manual verification before bootstrap/check execution.
- **Prioritize identity/offboarding proof over adding more edge rules.** Source already has layered controls; the harmful continuity risk is unknown ownership and recovery for GitHub, Cloudflare, domain, Access, signer, state, and contacts. Smallest proof: OI-002/OI-006.
- **Keep analytics disabled in the successor baseline.** It is not required for redirects and creates provider/privacy/retention dependencies. Enable only after an operator records purpose, fields, IP mode, retention, owner, and deletion route.

## Selected Outputs

- Triggered [secret, identity, and privacy surface](../../controls/security/secret-and-identity-surface.md).
- Triggered [edge exposure view](../../controls/security/diagrams/edge-exposure-view.md), because source-bounded ingress, WAF, Access, and route evidence materially clarify the public/private boundary. Unknown live edges are explicit.

The ephemeral artifact-quality review retained both artifacts because one answers custody/offboarding and the other answers exposure/data flow. The diagram was revised so no DNS, TLS, WAF, Access, analytics, or alert edge can be read as live proof.

## Material Omissions, Unknowns, And Stakeholder Questions

- Actual account owners/admins, least privilege, recovery factors, token/secret rotation, successor access, revocation, and monitored contacts: OI-002/OI-006.
- Applied DNS/TLS/WAF/rate-limit/Access settings, Worker secret metadata, logs, alerts, and response evidence: OI-006.
- Signed-tag verification before upgrade execution and correction of conflicting public guidance: OI-010.
- Provider retention/deletion and privacy/legal/accessibility sign-off for enabled analytics and generated public claims: not established; keep optional features disabled until owned.

## Reconciliation

The security-model documentation says the default upgrade source is a mutable branch, while current upgrade code, upgrading docs, and ADR 0015 say the default resolves the latest stable tag. The latter three align with implementation; the security-model statement is stale. However, ADR 0015 also describes automatic signature verification as future hardening, so “stable tag” is not reconciled into “verified signed upgrade.” Terraform/WAF/Access files are treated as intended controls only, consistent with their incomplete live-discovery note.

## Bounded Conclusion And Downstream Guidance

The source posture is a project strength: small runtime dependency surface, strong validation/headers, fail-closed private routes, explicit edge layers, and opt-in analytics. The project is not security-operable by a successor on public evidence alone because identity, secret/state custody, offboarding, live effectiveness, alerts, and incident ownership are unproved. Scalability may use public/third-party paths; Business Continuity must use custody/response gaps; Revenue Risk may use claim boundaries. None may claim certification, absence of vulnerabilities/secrets, live protection, compromise, or privacy compliance.
