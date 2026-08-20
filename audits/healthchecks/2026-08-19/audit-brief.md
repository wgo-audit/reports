# Audit Brief

| Field | Confirmed value |
|---|---|
| Onboarding start date, mode, and audit root | 2026-08-19; `improve` first audit; `_whats-going-on-20260819` |
| Baseline audit root and access (`none`, `read-only`, or `hidden`) | None; `none` |
| Audit platform/model and catalog platform/model | Codex; active session model (exact identifier unavailable); Codex `gpt-5.6-terra` at high reasoning for the documentation catalog |
| Reviewer-version comparison and auditor acceptance | First audit; no baseline versions. All selected core packages validated at version `0.2`; auditor approved the complete configuration on 2026-08-19. |
| Company and product | Acme Inc.; Healthchecks |
| Audience and business context | Acme CTO is the primary working audience. Acme CEO is the executive audience when findings or the recommendation require escalation. Acme is a small SaaS business serving a few thousand customers daily. Healthchecks would become core to daily operations. |
| Mandate and decision enabled | Determine whether Acme should pull upstream Healthchecks and self-host, maintain a security/reliability fork and self-host, or buy Healthchecks.io. Recommend an option or identify the smallest unresolved evidence preventing a responsible decision. |
| Detailed standard and cutoff | Detailed; onboarding start on 2026-08-19 |
| Current-folder repository scope | Entire current project folder, excluding audit roots |
| Primary code repository (source ID, URL/origin, ref, portable locator) | `HC-CODE-001`; `https://github.com/healthchecks/healthchecks`; `master`; resolved commit `fafac59eeb00cfdc87166242544fa071ecad1723`; `HC-CODE-001:./` |
| Supporting code repositories (source ID, URL, ref, portable locator) | None approved |
| Automatic GitHub code repository sources | Read-only accessible issues, pull requests, Projects, Actions, releases, and history for `HC-CODE-001`, bounded by the cutoff |
| Evidence and documentation sources (source ID, portable locator or GitHub URL/ref) | `HC-CODE-001` repository documentation; `HC-WEB-001` public Healthchecks and Healthchecks.io documentation rooted at `https://healthchecks.io`; no Acme internal sources approved |
| Source limits | No team interviews or requested team metrics. No Acme infrastructure, cloud-rate, labor-rate, on-call, job-inventory, payload-classification, or security-standard evidence. No live load test or hosted-service internals. Public evidence cannot prove hosted live state. After reviewing documentation coverage signals, the auditor declined to add sources on 2026-08-19. |
| Selected reviewer packages (ID, version, core/external, portable package locator) | `architecture` 0.2 core `core:references/reviewers/architecture/reviewer.md`; `business-continuity` 0.2 core `core:references/reviewers/business-continuity/reviewer.md`; `code-quality` 0.2 core `core:references/reviewers/code-quality/reviewer.md`; `contributor-vendor-value` 0.2 core `core:references/reviewers/contributor-vendor-value/reviewer.md`; `expense-exposure` 0.2 core `core:references/reviewers/expense-exposure/reviewer.md`; `maintenance-cost` 0.2 core `core:references/reviewers/maintenance-cost/reviewer.md`; `product-value` 0.2 core `core:references/reviewers/product-value/reviewer.md`; `project-health` 0.2 core `core:references/reviewers/project-health/reviewer.md`; `revenue-risk` 0.2 core `core:references/reviewers/revenue-risk/reviewer.md`; `scalability` 0.2 core `core:references/reviewers/scalability/reviewer.md`; `security-privacy` 0.2 core `core:references/reviewers/security-privacy/reviewer.md` |
| Approved substitutions and resolved dependency waves | No substitutions. Wave 1: Architecture. Wave 2: Code Quality, Product Value, Security and Privacy. Wave 3: Business Continuity, Expense Exposure, Scalability. Wave 4: Contributor and Vendor Value, Maintenance Cost, Revenue Risk. Wave 5: Project Health. |
| Reviewer run disposition (`fresh`, `complete-missing`, or `rerun-all`) | `fresh` |
| Material auditor answers and success boundaries | Slightly fewer than 100 jobs today with expected growth. For a critical job, an actionable alert must reach a responsible human within five minutes of missed expected completion. Monitoring-service RTO is 30 minutes and RPO is 5 minutes; the independent five-minute human-alert requirement still applies during service recovery. Cost comparisons use a 36-month horizon. Engineering time is opportunity cost rather than cash spend, and no Acme application-architecture-change effort is assigned to pull or make; deployment, hardening, testing, recovery, and operational work remain in scope. Team ability is unknown by design and must not be inferred. The audit must not alarm or involve the team. No additional sources were approved after the documentation coverage review. |
| Major known unknowns | Job schedules, payload sensitivity, criticality distribution, failure frequency, alert channels, escalation ownership, Acme infrastructure and security standards, cloud/provider rates, any requested opportunity-cost conversion rate, team skill coverage, hosted-service internals, and live capacity. |
| Success criteria | Recommend pull, make, or buy or isolate the minimum decision-blocking evidence; assess the five-minute alert boundary; identify risks, mitigations, stop conditions, and independent safeguards; separate setup effort, recurring maintenance, infrastructure/vendor cost, and uncertainty; define required skills without judging the team; assess whether hosted exposure is controllable; produce CTO-level analysis and a CEO-ready summary. |

## Decision Scenarios

- **Pull:** deploy the upstream Healthchecks project without maintaining a product fork, adding only necessary deployment and operational controls.
- **Make:** maintain a fork with evidence-justified security or reliability changes and accept the resulting ownership and upgrade burden.
- **Buy:** use Healthchecks.io, subject to security review, cloud-visibility concerns, and required architecture changes.

This audit does not perform a general commercial-vendor market scan. Healthchecks.io is the approved buy case.

## Business Concerns

| ID | Type | Approved statement |
|---|---|---|
| acme-pull-make-buy | mandate | Conduct a technical, operational, security, strategic, and cost audit enabling Acme to choose pull, make, or buy for Healthchecks. |
| select-sustainable-option | decision | Select an option Acme can depend on over time, or identify the smallest unresolved evidence preventing a responsible choice. |
| five-minute-critical-alert | concern | Determine whether each option can deliver an actionable human alert within five minutes of a critical job missing expected completion. |
| silent-monitor-failure | failure-mode | Do not recommend an option whose monitoring or notification path can fail silently without a reasonable independent safeguard. |
| unsustainable-ownership | failure-mode | Do not recommend self-hosting or a fork that Acme cannot sustainably operate, maintain, recover, and upgrade. |
| team-readiness-unknown | concern | Identify required skills and ownership without treating unavailable team evidence as proof of capability or incapability. |
| workload-growth-envelope | question | Assess slightly fewer than 100 jobs today and reasonable growth without inventing unavailable workload metrics. |
| job-monitoring-fit | question | Assess heartbeat and cron semantics, grace periods, schedule edge cases, overlapping runs, exit status, duration measurement, and practical Windows Scheduled Task support. |
| pull-make-buy-risk | question | Identify material risks, mitigations, stop conditions, and independent safeguards for pull, make, and buy. |
| maintenance-love | question | Estimate initial and recurring engineering and operational effort for pull and make, including upgrades, security patches, backup, recovery, cleanup, and host monitoring. |
| option-cost | question | Estimate setup, recurring infrastructure or vendor expense, labor effort, and uncertainty separately for every option. |
| hosted-cloud-visibility | concern | Determine whether Healthchecks.io data visibility and exposure can be acceptably controlled through security review and minimal architecture changes. |
| payload-data-exposure | concern | Assess sensitive ping payload, captured-log, environment-variable, credential, retention, pruning, and external-object-storage exposure. |
| identity-access-security | question | Assess enterprise identity, reverse-proxy SSO, WebAuthn, team isolation, credential storage, brute-force defenses, and supply-chain controls. |
| capacity-retention-footprint | question | Assess rate limits, request sizes up to 100 kB, concurrency, database and storage growth, retention, pruning, and realistic compute footprint from source and operator evidence. |
| upstream-continuity | concern | Assess license obligations, primary-maintainer concentration, community health, issue and pull-request handling, release continuity, and integration of outside contributions. |
| assessment-absence-guard | failure-mode | Do not treat missing scaling, reliability, team, or hosted-service evidence as reassuring evidence; preserve it as an explicit limit or verification. |

## Fixed Audit Boundaries

- The review is detailed and covers the full current project folder plus `HC-CODE-001`.
- Shared collectors are available internally and will be used only when a selected reviewer needs one.
- Public and existing-session GitHub access is read-only.
- Reviewer order is coordinator-owned through the approved dependency waves.
- The audit will not deploy, mutate, load test, install dependencies, change billing, or involve Acme staff.
- Implementation, live state, observed behavior, approval, readiness, ownership, cost, and future intent remain distinct.
