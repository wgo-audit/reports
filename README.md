<p align="center">
  <img src=".github/assets/wgo_banner.png" alt="WGO Reports" width="100%">
</p>

<!-- BADGES:START -->
<a href="#reports"><img alt="Reports" src="https://img.shields.io/badge/Reports-3-2DD4BF?style=flat-square&labelColor=111827"></a>
<a href="https://github.com/wgo-audit/reports/commits/main"><img alt="Last commit" src="https://img.shields.io/github/last-commit/wgo-audit/reports?style=flat-square&labelColor=111827&color=2DD4BF&label=Last%20commit"></a>
<a href="LICENSE.md"><img alt="License" src="https://img.shields.io/github/license/wgo-audit/reports?style=flat-square&labelColor=111827&color=2DD4BF"></a>
<!-- BADGES:END -->

Each report is a deep, public-evidence audit of a real asset that the core team publishes
to demonstrate what the tool produces.

Reports are **immutable**: once published, a report is never edited. Re-auditing an asset
later adds a new dated report alongside the old one, so you can watch how a project's
situation evolves over time.

## What a report answers

- **Continuity** — can the project survive its current maintainers leaving or losing interest?
- **Third-party operability** — could an independent successor build, run, and recover it without the creators?
- **Evidence** — every finding traces to a pinned commit or public source, frozen at a stated cutoff date.

## Reports

<!-- REPORTS:START -->
| Asset | Evidence cutoff | Audit |
|---|---|---|
| [docuseal](audits/docuseal/README.md) | [2026-08-06](audits/docuseal/2026-08-06/index.md) | Regulated esignature readiness (deep) |
| [healthchecks](audits/healthchecks/README.md) | [2026-08-19](audits/healthchecks/2026-08-19/index.md) | Pull make buy technical and operational audit (deep) |
| [vanityurls.link](audits/vanityurls.link/README.md) | [2026-07-22](audits/vanityurls.link/2026-07-22/index.md) | Continuity & third-party operability (deep) |
<!-- REPORTS:END -->

### Layout

Every report folder follows the same shape, open **`index.md`** to start reading:

```
audits/
└── <asset>/                        # the audited asset name
    └── <evidence-cutoff>/          # date the evidence was frozen (e.g., cutoff)
        ├── index.md                # START HERE — THE REPORT'S ENTRYPOINT
        ├── manifest.json           # machine-readable metadata
        ├── executive-summary.md    # the reconciled assessment and 30–90 day plan
        ├── controls/               # control-by-control analysis of each safeguard
        ├── evidence/               # evidence ledger and supporting packets
        ├── reviewer-reports/       # findings by review discipline
        └── operator-aids/          # how-to guides for a new operator to rebuild, recover, and monitor
```

See [CONTRIBUTING](.github/CONTRIBUTING.md) for the folder conventions and how to add a report.
