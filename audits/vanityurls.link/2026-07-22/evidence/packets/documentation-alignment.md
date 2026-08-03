# Documentation Alignment Evidence Packet

## Scope And Evidence Boundary

- Reader question: Does the public documentation corpus align across repositories and cover the information a successor maintainer or independent operator needs?
- Evidence cutoff: July 22, 2026.
- Approved sources and actions: `docs/` in the `code` repository; `content/docs/` plus relevant public repository governance files in the approved `website` clone; the approved `v8s-config` and `v8s-link` repository snapshots; the 97-entry WGO documentation catalog.
- Exclusions and sensitivity: No private handover material, internal notes, live-console walkthrough, stakeholder interview, or observed third-party exercise was approved.

## Observations

| Observation | Source type and exact locator | Observed/effective time | What it establishes | Limitation |
|---|---|---|---|---|
| The product README designates the public website documentation as the source of truth for setup and operation. | `README.md:12` at `bc4a75d28340eadd31ecbf43923c2062ccc62166` | Repository state through 2026-06-16 | Establishes the intended documentation authority and cross-repository boundary. | Does not prove every repository-local instruction is synchronized with the website. |
| The approved corpus contains 97 catalogued documentation records, including English/French operator guidance and 19 architecture decision records in `code/docs/adr/`. | `_whats-going-on/documentation/catalog.md`; `docs/adr/`; website `content/docs/` | Catalogued 2026-07-24 from cutoff-eligible commits | The project has broad public coverage of setup, customization, reference, operations, troubleshooting, privacy/security topics, and recorded technical decisions. | Catalog presence does not prove correctness, currency, discoverability, or successful use by an independent operator. |
| Website documentation describes prerequisites, setup, build/deployment, customization ownership, testing, Access, network protection, analytics, upgrades, and troubleshooting. | Website `content/docs/setup/`, `content/docs/customize/`, `content/docs/operations/`, `content/docs/reference/`, and `content/docs/troubleshooting/` at `c2d735b494a36bc3a8cd340c324012b1e8fb00bb` | Repository state through 2026-07-20 | A prospective instance operator has a substantial public task-oriented guide. | No approved evidence shows a new operator completed the golden path without creator help or captured time, errors, and recovery outcomes. |
| The product repository documents the upstream-versus-instance ownership boundary and a detailed release process with local checks, release-please, signed tags, deployment verification, and rollback considerations. | `docs/README.md`; `RELEASE_WORKFLOW.md`; `docs/adr/0001-use-release-please-and-semantic-versioning.md`; `docs/adr/0015-require-signed-release-tags.md` | Repository state through 2026-06-16 | Important contribution, upgrade, and release design intent is documented. | It does not prove GitHub rules are applied, signer access is recoverable, or a successor has exercised the workflow. |
| The current `code` contribution guide points issue discussion to the prior personal-repository URL rather than the current organization repository. | `.github/CONTRIBUTING.md:7` | Repository state through 2026-06-16 | A contributor-facing navigation defect exists in the current public guide. | The current GitHub repository still exposes an Issues tab; impact on actual contributors was not observed. |
| The `code` governance file names two maintainers but also states that the project is currently maintained by a single individual. | `.github/GOVERNANCE.md`; `.github/MAINTAINERS.md`; `.github/CODEOWNERS` | Repository state through 2026-06-16 | Public maintainer-role documentation is internally inconsistent. | Public files do not establish which statement controls or the real access model. |
| Maintainer declarations differ by repository: two for `code`, one for `website`, and none found in `v8s-config` or `v8s-link`. | `.github/MAINTAINERS.md`; `_whats-going-on/documentation/tmp/website/.github/MAINTAINERS.md`; complete file inventories of the two operational repositories | Repository states through 2026-07-20 | Cross-repository responsibility is not documented as one coherent maintenance map. | Organization-level roles or private practices may exist outside the approved source set. |
| `v8s-config` describes Terraform ownership and migration/import rules, while also recording incomplete live discovery due to insufficient token permission. | `tmp_debug/wgo-sources/v8s-config/README.md` | Repository state through 2026-06-16 | The repository discloses both intended infrastructure authority and a verification limitation. | The note is not a dated live-state attestation and no approved state/plan/apply evidence closes the gap. |
| No dedicated public maintainer-onboarding, succession, repository/account-transfer, credential-custody, registrar-recovery, Terraform-state-recovery, or whole-system disaster-recovery runbook was found in the approved corpus. | `_whats-going-on/documentation/catalog.md`; bounded search of all four cutoff-eligible repository snapshots | Search performed 2026-07-24 over evidence eligible through 2026-07-22 | These named continuity topics are not covered as dedicated public procedures within scope. | Sensitive details should not be public; a public process can still identify roles, inventories, prerequisites, and redacted evidence. Private documents may exist but were not approved. |

## Material Unknowns And Access Limits

- Whether any prospective contributor, successor maintainer, or third-party operator has completed the documented paths without creator assistance is unknown.
- Whether private handover, account inventory, recovery, and succession material exists is unknown.
- Documentation-to-live-state alignment is unknown because no authenticated GitHub or Cloudflare settings and no deployed-runtime observation were approved.
- The requested website path was `context/docs/`; it did not exist. The catalog and this packet use the verified repository path `content/docs/`, as recorded in the source access register.

## Reuse Guidance

- Product Value, Architecture, Code Quality, Security, Scalability, and Maintenance Cost may reuse the documented behavior and source-of-truth boundaries, but must independently verify implementation before treating prose as code fact.
- Project Health, Contributor/Vendor Value, and Business Continuity may reuse governance inconsistencies and missing public continuity procedures.
- No reviewer may convert documentation breadth into proof of low-touch onboarding or third-party operability without an observed exercise or equivalent authoritative evidence.
