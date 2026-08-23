# Supply Chain And Tooling Results

## Purpose And Evidence Boundary

This view records dependency, build, release, SBOM, trust-anchor, and local
security-tool evidence for `HC-CODE-001` at the pinned commit. It does not claim
a complete vulnerability scan, secret scan, release attestation, or Acme
promotion control. No package was installed and source was not modified.

## Dependency And Build Integrity

- `requirements.txt` has 15 exact direct pins but no hashes. Development
  requirements include unpinned typing packages. No complete transitive lock or
  hash-verified installation contract was found in the approved tree.
- CI installs with `pip` and references GitHub Actions by mutable major tags.
  The release workflow requests an SBOM, but no repository-side policy or Acme
  consumer that verifies an SBOM, checksum, signature, attestation, or immutable
  image digest was found.
- The Docker build starts from a mutable Python image tag and installs unpinned
  OS packages; the sample database uses a mutable major-version tag.
- Local commit signature verification could not complete because the isolated
  environment had no usable GPG keybox. Public GitHub release UI reports signed
  release commits; that presentation is not an Acme consuming verifier.

This extends [OI-008](../open-items.md#OI-008): promotion must identify an
immutable source/image digest and verify the evidence Acme chooses to trust.
Generating an SBOM without consuming it does not reduce release risk.

## Executed And Blocked Checks

Working directory: `HC-CODE-001:./`. `pip-audit` was version 2.10.0.
Installation was not authorized. Totals: five security-tool checks and one
provenance check. Of eight named security tools, one was present and seven were
unavailable.

| Exact command | Intended coverage | Outcome | Dependency state and bounded conclusion |
|---|---|---|---|
| `for t in scorecard osv-scanner gitleaks trivy grype pip-audit bandit semgrep; do command -v "$t" || true; done` | Existing scanner inventory | Pass: `pip-audit` present; seven tools unavailable | No installation. Absence of scanner output is not a clean result. |
| `pip-audit -r requirements.txt -r requirements-dev.txt --disable-pip --progress-spinner off` | Production and development advisories | Error before audit: `--disable-pip` requires a hash-complete/no-dependency mode | No dependency conclusion. |
| `pip-audit -r requirements.txt -r requirements-dev.txt --no-deps --disable-pip --progress-spinner off` | Direct production and development advisories | Error in restricted run: network/DNS unavailable | Retried through approved read-only network access. |
| `pip-audit -r requirements.txt -r requirements-dev.txt --no-deps --disable-pip --progress-spinner off` | Direct production and development advisories | Error: unpinned `types-Markdown` prevents the mode | Development set was not audited; no clean claim. |
| `pip-audit -r requirements.txt --no-deps --disable-pip --progress-spinner off` | Direct production dependency advisories | Pass: no known vulnerabilities reported | Direct pins only; transitive resolution omitted, advisory coverage time-bound, not exploitability analysis. |
| `git rev-parse HEAD && git show -s --format=fuller --show-signature HEAD` | Pin and local signature-verification capability | Mixed: pin matched; signature verification could not complete | Commit identity established; signer trust not locally verified. |

No project tests were executed for this security review: 0 passed, 0 failed,
0 errors, and 0 skipped because execution was not started. Existing hosted test
and CodeQL results remain bounded by [E-010](../../evidence/evidence-ledger.md#E-010).

## Required Consumer Controls

1. Promote only a reviewed immutable commit and image digest.
2. Archive an SBOM with the release and make an Acme gate consume it for
   policy/advisory review. Record verifier, trust root, failure behavior, and
   exception owner.
3. Use a hash-complete dependency resolution or equivalent reproducible build,
   pin Actions by immutable commit, minimize workflow permissions, and record
   base-image provenance.
4. Run an authorized secret scanner, complete dependency/SBOM scan, and image
   scan at every promoted release. A fork must also scan every upstream merge.
5. Treat public badges and a generated SBOM as inputs, not release approval.

## Limitations And Follow-Up

Scorecard, OSV-Scanner, secret scanners, source analyzers, and image scanners
were unavailable and were not installed. The direct production audit reported
no known advisories but did not resolve transitive dependencies. No image was
pulled, built, or scanned. No live CI permissions, branch protection, release
approval, registry retention, signature policy, or Acme consumer was observed.
