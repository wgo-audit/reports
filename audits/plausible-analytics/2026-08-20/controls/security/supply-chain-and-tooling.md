# Supply Chain And Tooling Results

## Evidence Boundary

This source-bounded view covers the approved `primary-code` snapshot, its lockfiles, Dependabot configuration, and release workflows. It uses [E-009](../../evidence/evidence-ledger.md#e-009), [E-010](../../evidence/evidence-ledger.md#e-010), [E-012](../../evidence/evidence-ledger.md#e-012), [E-028](../../evidence/evidence-ledger.md#e-028), and [E-029](../../evidence/evidence-ledger.md#e-029). No dependency restore, local scanner, registry inspection, SBOM validation, signing-key review, tag-authority review, deployment inspection, or separate Community Edition repository was authorized.

## Evidence Dimensions Used

Implementation and public exact-commit CI/ruleset evidence are present. Deployed artifact identity, release approval, registry policy, vulnerability state, scanner operation, and consuming verification are unknown.

## Current Source-Bounded Position

| Question | Verdict | Evidence | Limitation / consequence |
|---|---|---|---|
| Dependency pinning and update discovery | Partial control | Mix and three NPM lockfiles exist; NPM locks carry integrity metadata. Dependabot schedules daily Mix/Docker/NPM and weekly Actions updates ([E-028](../../evidence/evidence-ledger.md#e-028)). | No approved vulnerability result, remediation SLA, or proof that updates were merged/deployed. The source policy supports only the latest major.minor ([E-029](../../evidence/evidence-ledger.md#e-029)). |
| Workflow dependency trust | Source-verified strength | Inspected third-party GitHub Actions use full commit SHAs ([E-028](../../evidence/evidence-ledger.md#e-028)). | Action repository integrity and GitHub runtime controls were not independently assessed. |
| CE image trust-anchor production | Source-verified producer | Tagged builds publish per-platform content digests; the workflow consumes those digest filenames to assemble the multi-architecture manifest ([E-028](../../evidence/evidence-ledger.md#e-028)). | No SBOM, signature, or attestation production was found in the approved repository. Release workflows do not declare a dependency on quality workflows. |
| CE image trust-anchor consumption | Unknown | [E-028](../../evidence/evidence-ledger.md#e-028), [OI-005](../open-items.md#oi-005) | The library's deployed digest/tag and any pull-time policy are unknown. A produced digest is useful only if deployment pins/verifies it. |
| Tracker NPM publication | Partial control | Release workflow uses OIDC trusted publishing and a commit-pinned checkout action ([E-028](../../evidence/evidence-ledger.md#e-028)). | It runs `npm install` and publish steps independently of the tracker browser gate; no library consumption path or package-verification policy was inspected. |
| Hosted security claims | Public claim only | [E-030](../../evidence/evidence-ledger.md#e-030) says dependency scans run daily and vulnerability scans regularly. | Post-cutoff validation, not scanner output or control-effectiveness proof. Applies to hosted claims, not CE operation. |
| Secret scanning / SBOM / provenance | Unknown / not found in approved source | [E-028](../../evidence/evidence-ledger.md#e-028) | Bounded absence only. No active scan was run. Do not infer that dependencies or history are vulnerability-free. |

## Trust-Anchor Reconciliation

The CE workflow produces content digests and consumes them when creating its manifest. The next consuming verifier—the library deployment's digest pinning, admission rule, or equivalent—was not available. The NPM workflow uses GitHub OIDC to authenticate publication, but no downstream package-consumer verification was approved. No other signature, checksum, SBOM, or attestation producer requiring a source-visible verifier was found.

## Material Unknowns And Closure Routes

- Close artifact-to-source-to-green-run and deployed-digest verification through [OI-005](../open-items.md#oi-005), after [OI-001](../open-items.md#oi-001) identifies the deployment.
- Application Security owns dependency exploitability and deeper workflow attack paths. Cloud Security owns registry, deployment, admission, IAM, and runtime effectiveness.
- For Subscribe, obtain dated scanner summaries, vulnerability/patch handling evidence, and service-specific supply-chain assurances during security/procurement review; [E-030](../../evidence/evidence-ledger.md#e-030) is not sufficient control proof.
