# Architecture: Approved Public Deployment Documentation

## Boundary

- Approved source: `https://www.docuseal.com` only.
- Observed: 2026-08-06, the audit cutoff.
- These dynamic pages are public documentation/marketing, not release-pinned implementation, live-environment evidence, contractual commitments, or proof of control effectiveness.

## Source-Bounded Observations

| Observation | Exact source | Status and limitation | Architecture route |
|---|---|---|---|
| The server-requirements guide gives approximate CPU, RAM, and disk examples for 10,000 signed documents across document-size/template-reuse/signer-count scenarios. It recommends PostgreSQL for production API/embedding use above 1,000 documents/year and calls SQLite/MySQL partially compatible. | [On-premises server requirements](https://www.docuseal.com/docs/on-premises-server-requirements), “Requirements,” “Database requirements,” and “Additional recommendations” | Documented estimate; not a benchmark or capacity commitment for the target workload, which is unknown. | Capacity/cost candidate and verification input; PostgreSQL production data-authority decision. |
| The environment guide exposes database and application secret configuration, optional TLS enforcement and host name, SMTP credentials, S3/GCS/Azure storage credentials, `WEB_CONCURRENCY` (default one process), long-lived session/presigned/file URL defaults, and an optional Pro Gotenberg integration. | [Configuring with environment variables](https://www.docuseal.com/docs/configuring-docuseal-via-environment-variables), “General Configuration,” storage sections, and “Misc (optional)” | Configuration documentation; it does not establish how the organization stores/rotates secrets, terminates TLS, or configures a live deployment. Page is not version-bound to `3.1.7`. | Identity/secrets, storage, runtime concurrency, and Pro boundary candidates. |
| The Docker update guide tells operators to pull an unqualified `docuseal/docuseal` image and recreate the container, or force-recreate with Compose. It does not identify an immutable digest, pre-upgrade backup, migration rehearsal, rollback, or post-deploy verification in the retrieved body. | [Update DocuSeal to the latest version in Docker](https://www.docuseal.com/docs/update-docuseal-to-the-latest-version), “Using basic Docker commands” and “Using Docker-Compose” | Bounded absence claim for this approved page only. Published registry contents and deployment templates are outside the approved corpus. | Release/deployment decision; operations verification and rollback design. |
| The on-premises page presents Docker/PaaS deployment and local/S3/GCS/Azure storage. It labels roles, SMS identity verification, SSO/SAML, HTML/tag APIs, and embedded signing/form builder as Pro features. | [On-Premises](https://www.docuseal.com/on-premises), “Features” and “Pro Features” | Dynamic product/edition statement, not Pro implementation evidence or a release-specific entitlement contract. | Community/Pro integration and trust-boundary decision dependency. |

## Outside-Scope Pointers

- The README/public site point to deployment-template repositories and Docker Hub artifacts. **Documented outside audited scope; not independently verified.** Those sources could establish version/digest/template assumptions, but were not approved as supporting code/artifact sources.
- No approved live environment, DNS, cloud account, datastore instance, secret manager, image digest, deployment record, or runtime telemetry was supplied. Live topology and control effectiveness are unknown.
