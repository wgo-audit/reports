# Audit Brief

| Field | Confirmed value |
|---|---|
| Onboarding start date, mode, and audit root | 2026-08-06 (America/Toronto); `improve`; `_whats-going-on-20260806` |
| Baseline audit root and access (`none`, `read-only`, or `hidden`) | `none` |
| Audit platform/model and catalog platform/model | Codex/OpenAI active audit model; Codex/OpenAI inherited active model for the documentation catalog because `gpt-5.6-luna` is not exposed by this task's worker interface |
| Reviewer-version comparison and auditor acceptance | First audit; no baseline versions to compare |
| Company and product | Unnamed regulated SaaS provider evaluating self-hosted DocuSeal Community for an eSignature capability in web and mobile customer-onboarding applications; DocuSeal LLC is the upstream project/vendor |
| Audience and business context | CEO; IT Operations Director; VP Software Engineering; Product Manager; CISO. The capability affects all new customers and associated new revenue and is intended to operate within the organization's existing SOC 2 control boundary. |
| Mandate and decision enabled | Assess whether the pinned DocuSeal Community repository is a sound foundation for further technical evaluation and vendor discussions, identify conditions that must be resolved before any production-approval decision, and recommend `continue evaluation`, `continue conditionally`, or `stop` based only on available evidence. The recommendation is about readiness for vendor and specialist discussions, not production approval. |
| Detailed standard and cutoff | Detailed; full current-folder review; evidence cutoff is the onboarding start on 2026-08-06 in America/Toronto. Later evidence may be used only as labeled post-cutoff validation. |
| Current-folder repository scope | Entire current project folder, excluding audit roots. `docuseal/` is the sole product code root. Local WGO and launcher material is coordination tooling and is not evidence of DocuSeal behavior. |
| Primary code repository (source ID, URL/origin, ref, portable locator) | `primary-code`; `https://github.com/docusealco/docuseal`; release tag `3.1.7`; commit `a2d8b855491793870b7b4acf176d2d95ae95ff83`; `primary-code:.` |
| Supporting code repositories (URL, ref, local path) | None, confirmed by the auditor |
| Automatic GitHub code repository sources | Read-only accessible PRs, issues, Projects, Actions, releases, and history for `docusealco/docuseal`, bounded to the cutoff and existing session access |
| Evidence and documentation sources (source ID, portable locator or GitHub URL/ref) | Full pinned repository (`primary-code:.`); approved public source `https://www.docuseal.com`; auditor-supplied mandate at `auditor-input:pasted-text.txt` |
| Source limits | Community implementation and approved public sources only. No Pro implementation, hosted DocuSeal Cloud assessment, penetration testing, load testing, code remediation, legal determination, regulatory determination, or access to the organization's legal, compliance, security, or DocuSeal contacts. The documentation catalog identified referenced external assurance, status, artifact, deployment-template, component, wrapper, contract, and review records plus partial or missing operational documentation; on 2026-08-06 the auditor declined to add sources before audit start. Relevant pages within the already approved `docuseal.com` boundary remain readable, while external references remain outside the approved corpus. |
| Selected reviewer packages (ID, version, core/external, portable package locator) | See [Selected Reviewer Packages](#selected-reviewer-packages); all are core version `0.2` |
| Approved substitutions and resolved dependency waves | No substitutions. Wave 1: `architecture`. Wave 2: `code-quality`, `product-value`, `security-privacy`. Wave 3: `business-continuity`, `expense-exposure`, `scalability`. Wave 4: `contributor-vendor-value`, `maintenance-cost`, `revenue-risk`. Wave 5: `project-health`. |
| Reviewer run disposition (`fresh`, `complete-missing`, or `rerun-all`) | `fresh` |
| Material auditor answers and success boundaries | Preserve evidentiary independence; distinguish repository evidence from legal, compliance, security-specialist, vendor, live-state, and production-approval determinations; do not treat unavailable Pro implementation as a repository defect; do not let Pro gaps conceal assessable Community risks. The auditor approved the configuration and declined source expansion after reviewing catalog signals. On 2026-08-06 the auditor set monthly availability targets of 99.5% for signing and 99% for customer onboarding, a maximum data-loss/RPO target of two hours (with synchronous transactions preferred), and confirmed that all new onboarding may pause during an interruption. On 2026-08-07 the auditor approved authority-approved bounded low/base/high workload and service-level scenarios as the capacity acceptance oracle when exact forecasts are unavailable; actual scenario values still require named-owner approval and verification. The complete approved mandate appears below. |
| Major known unknowns | Actual workload volumes; detailed target architecture; jurisdiction-specific enforceability; KYC identity-binding sufficiency; privacy and data-residency determinations; Community-versus-Pro edition decision; unavailable Pro evidence; specialist/vendor answers; production ownership, capacity, recovery, security, maintenance, and cost decisions not proven by the repository. |
| Success criteria | Evidence-backed assessment; internally resolvable conditions; Pro/vendor evidence requests; specialist determination list; production requirements and target-architecture gaps; evidence-bounded recommendation to continue, continue conditionally, or stop. |

## Selected Reviewer Packages

| ID | Version | Source | Portable package locator |
|---|---|---|---|
| `architecture` | `0.2` | core | `core:references/reviewers/architecture/reviewer.md` |
| `business-continuity` | `0.2` | core | `core:references/reviewers/business-continuity/reviewer.md` |
| `code-quality` | `0.2` | core | `core:references/reviewers/code-quality/reviewer.md` |
| `contributor-vendor-value` | `0.2` | core | `core:references/reviewers/contributor-vendor-value/reviewer.md` |
| `expense-exposure` | `0.2` | core | `core:references/reviewers/expense-exposure/reviewer.md` |
| `maintenance-cost` | `0.2` | core | `core:references/reviewers/maintenance-cost/reviewer.md` |
| `product-value` | `0.2` | core | `core:references/reviewers/product-value/reviewer.md` |
| `project-health` | `0.2` | core | `core:references/reviewers/project-health/reviewer.md` |
| `revenue-risk` | `0.2` | core | `core:references/reviewers/revenue-risk/reviewer.md` |
| `scalability` | `0.2` | core | `core:references/reviewers/scalability/reviewer.md` |
| `security-privacy` | `0.2` | core | `core:references/reviewers/security-privacy/reviewer.md` |

## Fixed Audit Defaults

- Detailed review of the full current project folder and the confirmed product code root.
- Auditor instruction: do not load the project-documentation skill; use the completed documentation catalog for navigation and cite original sources for findings.
- Available shared collectors may be used when a selected reviewer needs them.
- Read-only public GitHub access and private GitHub data available through the existing session are authorized only for the named repository.
- WGO coordinates dependency waves; reviewers do not select their own run order.
- Audit work is read-only unless the auditor separately authorizes a state-changing action.

## Full Auditor Mandate (Verbatim)

```text
Background and context
The organization is a regulated SaaS provider, adding an eSignature capability to its web and mobile customer-onboarding applications to meet applicable regulatory requirements. The capability will affect all new customers and the associated new revenue. The organization intends to self-host DocuSeal within its existing SOC 2 control boundary. The system may process customer identity information, KYC documents, signed agreements, signer evidence, and audit records.

DocuSeal is distributed in a Community edition (open source, AGPL-3.0) and a proprietary Pro edition. This engagement assesses the community repository and approved public sources. The assessed repository version must be pinned to a specific commit or release tag at kickoff so the findings are reproducible.

Objectives
Assess whether the DocuSeal Community repository is a sound foundation for further technical evaluation and vendor discussions toward the organization’s eSignature capability and identify the conditions that must be resolved before any production-approval decision.

The assessment will:

●      evaluate the repository against defined technical, security, reliability, scalability, maintainability, and licensing criteria;
●      identify where the target architecture depends on capabilities not available in the Community edition (typically Pro), and specify the evidence to request from DocuSeal;
●      separate what the assessor can conclude from evidence from what requires a legal, compliance, or security specialist determination; and
●      not assert that DocuSeal or any future organization implementation satisfies any regulation.

3. Scope
3.1 In scope: the repository and approved public sources
Assessment is limited to implementation and evidence present in the pinned repository version and approved by public sources. The assessor will examine the following and support each finding with cited evidence:

●      Signature validity and integrity. Whether the community implementation produces cryptographically verifiable, tamper-evident signed documents (for example PKI or PAdES digital signatures) or visual representations supported by a separate audit record, and whether a completed document can be independently verified after the fact.
●      Signer evidence and audit records. What signer evidence is captured, how audit records are generated and stored, and whether their integrity can be established, for example through hashing or immutability of the record.
●      Authentication and access control. The access-control model is available in the community, given that SSO/SAML and role-based permissions are pro-features, and whether it is adequate to protect KYC and identity data at the organization’s scale.
●      Data handling. How identity documents and signed agreements are stored, encrypted in transit and at rest, retained, and deleted, and how secrets and signing keys are managed.
●      Security posture. Dependency and supply-chain health, known vulnerabilities, and the project’s security-response and patch cadence.
●      Reliability and scalability. Architectural evidence for horizontal scaling, background-job processing, and data-store behaviour under the stated load of all new customers, and the gaps that require dedicated load validation.
●      Maintainability and project health. Release cadence, contributor concentration, issue backlog, and documentation quality as indicators of maintenance risk.
●      Licensing. The obligations that AGPL-3.0 places on a commercial SaaS that self-hosts may modify, and serves DocuSeal over a network, including source-availability triggers, and the interaction between those obligations and the fact that API access, webhooks, and embedding, which organization’s architecture requires, are provided only under Pro.
●      Deployability within the SOC 2 boundary. Configuration, hardening, and operational assumptions for running the Community edition inside the organization’s existing control environment.

You will identify the pinned repository version for this assessment.
3.2 Deferred vendor validation: Pro and non-inspectable capabilities
When a required or useful capability is available only in DocuSeal Pro, or otherwise cannot be inspected, the assessor will:

●      identify the capability and why it may matter to the regulatory or business outcome;
●      classify it as deferred vendor validation;
●      specify the question or evidence to request from DocuSeal;
●      not assess the unavailable implementation, and not treat its absence from the repository as a defect or a failed review; and
●      report it as a decision dependency, not a confirmed blocker, until DocuSeal and the relevant specialist have responded.


Capabilities already known to fall here include API access and web hooks, embedding, SSO/SAML, role-based permissions, and SMS or phone-based signer identity verification.

3.3 Out of scope
●      Any assessment of the pro-implementation itself.
●      Legal or regulatory determinations (see Section 7).
●      Penetration testing, load testing, or code remediation, unless added by change control.
●      Assessment of DocuSeal’s hosted cloud service.

4. Independence and evidentiary standard
The assessor’s findings and recommendations are determined solely by the evidence available in the assessed sources. The organization will not direct, constrain, or edit the assessor’s conclusions, and this mandate does not instruct the assessor toward any particular recommendation. Each material finding will cite the file, artifact, or public source that supports it. Where evidence is insufficient, the assessor will state that the question is unresolved rather than resolve it by assumption.

4.1 Failures the assessment is designed to avoid
●      Concluding that DocuSeal or a future organization implementation satisfies a regulation. The assessment does not make that claim.
●      Rejecting DocuSeal only because Pro implementation details are not present in the public repository.
●      Characterizing as viable, secure, or compliant any capability that could not be assessed from available evidence.
●      Treating deployment inside the SOC 2 boundary as proof that the resulting service is compliant.
●      Allowing an unavailable Pro feature to hide a repository-level security, reliability, scalability, licensing, or maintenance issue that can be assessed independently.
5. Deliverables
1.    An evidence-backed assessment of the repository against the Section 4.1 criteria.
2.    The conditions that the organization can resolve internally.
3.    A separate list of Pro and vendor questions for DocuSeal, each with the specific evidence requested.
4.    A separate list of legal and compliance determinations required, routed to the appropriate specialist.
5.    Production requirements for capacity, recovery, security, maintenance, cost, and ownership, including the gap between the repository and the target architecture.
6.    A recommendation to continue evaluation, continue conditionally, or stop, based only on evidence actually available. The recommendation addresses readiness to proceed to vendor and specialist discussions, not production approval.
6. Client dependencies and specialist determinations
The following are outside the assessor’s authority and must be provided by the organization or its named specialists. The assessment identifies the questions but does not answer them:

●      legal validity and enforceability of the eSignature approach in each applicable jurisdiction, for example ESIGN, UETA, eIDAS, and any Quebec or Canadian requirements;
●      regulatory sufficiency of the binding between signer identity and KYC obligations;
●      data residency and privacy determinations for identity documents; and
●      Confirmation of the Community-versus-Pro edition decision, which materially affects both the licensing and capability findings.
●      The organization will not provide access to the relevant legal, compliance, and security contacts, or a point of contact for questions directed to DocuSeal.
```
