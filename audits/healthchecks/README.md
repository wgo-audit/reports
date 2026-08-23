# healthchecks

Point-in-time audits of Healthchecks, newest first. Each row is a frozen snapshot; read across the columns below to see how the situation changes over time.

| Evidence cutoff | Audit |
|---|---|
| [2026-08-19](2026-08-19/index.md) | Pull make buy technical and operational audit (deep) |

## Conclusions over time

| Question | 2026-08-19 |
|---|---|
| Conduct a technical, operational, security, strategic, and cost audit enabling Acme to choose pull, make, or buy for Healthchecks. | Compare buy and pull through parallel bounded due diligence; consider make only for a demonstrated source-change need; no option has production approval. |
| Select an option Acme can depend on over time, or identify the smallest unresolved evidence preventing a responsible choice. | The evidence does not support an all-in burden ranking between buy and pull; comparable Acme-specific vendor, topology, alert, ownership, cost, and exit evidence is required. |
| Determine whether each option can deliver an actionable human alert within five minutes of a critical job missing expected completion. | No option has T0-to-actionable-human evidence at or below 300 seconds with no silent loss. |
| Do not recommend an option whose monitoring or notification path can fail silently without a reasonable independent safeguard. | The conditional recommendation requires an Acme-controlled independent watchdog and alert route. |
| Do not recommend self-hosting or a fork that Acme cannot sustainably operate, maintain, recover, and upgrade. | Pull and buy both require measured Acme-specific ownership evidence; make additionally requires a demonstrated source-change need and accepted fork stewardship. |
| Identify required skills and ownership without treating unavailable team evidence as proof of capability or incapability. | Required roles and skills are mapped; Acme team ability remains intentionally unassessed. |
| Assess slightly fewer than 100 jobs today and reasonable growth without inventing unavailable workload metrics. | Source mechanisms and commercial tiers are known, but production capacity and growth headroom require measured workload evidence. |
| Assess heartbeat and cron semantics, grace periods, schedule edge cases, overlapping runs, exit status, duration measurement, and practical Windows Scheduled Task support. | Fit is strong for known-schedule passive monitoring; business-output, overlap, and Windows operating contracts remain incomplete. |
| Identify material risks, mitigations, stop conditions, and independent safeguards for pull, make, and buy. | Option-specific risks and stop conditions are documented; every option retains Acme-owned alert and continuity duties. |
| Estimate initial and recurring engineering and operational effort for pull and make, including upgrades, security patches, backup, recovery, cleanup, and host monitoring. | Exact effort and an all-in buy-versus-pull burden ranking are unsupported; measured option-specific routine and surge work is required. |
| Estimate setup, recurring infrastructure or vendor expense, labor effort, and uncertainty separately for every option. | Hosted list price is known; all-in TCO and monetized opportunity cost remain unknown for every option. |
| Determine whether Healthchecks.io data visibility and exposure can be acceptably controlled through security review and minimal architecture changes. | Data minimization can reduce exposure, but vendor/security/contract acceptance remains open. |
| Assess sensitive ping payload, captured-log, environment-variable, credential, retention, pruning, and external-object-storage exposure. | Material storage/provider boundaries are mapped; no-body-by-default and lifecycle controls are required. |
| Assess enterprise identity, reverse-proxy SSO, WebAuthn, team isolation, credential storage, brute-force defenses, and supply-chain controls. | Useful source controls exist, but proxy trust, bearer capabilities, privileges, credential lifecycle, and deployed supply-chain acceptance remain open. |
| Assess rate limits, request sizes up to 100 kB, concurrency, database and storage growth, retention, pruning, and realistic compute footprint from source and operator evidence. | Mechanisms are established; CPU, RAM, storage, burst, and queue capacity are not production-proven. |
| Assess license obligations, primary-maintainer concentration, community health, issue and pull-request handling, release continuity, and integration of outside contributions. | BSD rights and active history preserve options, but upstream/vendor concentration and Acme succession remain material. |
| Do not treat missing scaling, reliability, team, or hosted-service evidence as positive or negative evidence; classify it by decision relevance. | Normally private and Acme-specific unknowns are neutral unless a decision requires them; direct source findings are reported separately. |
