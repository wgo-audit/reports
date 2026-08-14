# Contributing to WGO Reports

This repository is a **core-team showcase**: it publishes reports produced by the
[wgo-audit](https://github.com/wgo-audit/code) engine to demonstrate the tool. It is not a
place for external code contributions. The one recurring task is **adding a generated
report**, covered below.

## Rules

- **Reports are immutable.** Once a report is committed, never edit its contents. A
  re-audit is a **new** folder under a new evidence cutoff.
- **Never commit build junk** — dependency clones, rendered site output, a `tmp/` copy of
  the audited project, or an audited project's `.git/`.
- **Keep each folder self-contained** — `index.md` is always the entrypoint and
  `manifest.json` is always present.
- **Never fabricate or revise a manifest during upload.** WGO creates it after the
  executive summary is final; report ingestion only verifies and packages it.

### manifest.json

Every report folder carries the final `manifest.json` produced by its audit. Its
`$schema` identifies the contract. The top-level fields are:

| Field | Purpose |
|---|---|
| `$schema`, `schemaVersion` | Exact machine-readable contract. |
| `report` | Stable report identity, title, entrypoint, and optional headline. |
| `subject` | Stable identity of the audited subject. |
| `audit` | Audit type, mode, and depth. |
| `businessConcerns` | Approved concerns paired one-to-one with conclusions. |
| `evidence` | Cutoff, pinned sources, access boundary, and limitations. |
| `execution` | Generator, platform, and reviewer-version provenance. |
| `relationships` | Previous, baseline, comparison, and supersession links. |

Reject a bundle whose manifest is absent, invalid, contains unresolved placeholders, or
uses the legacy flat `asset`, `evidenceCutoff`, or question-keyed `conclusions` format.

## Layout

Every report is a self-contained bundle at `audits/<asset>/<evidence-cutoff>/`:

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

- **`<asset>`** — one directory per audited asset; it groups every audit of that asset so
  the situation can be compared over time.
- **`<evidence-cutoff>`** — the ISO date the evidence was frozen (the "situation" the report
  describes). Compare along this axis, not the generation date; both are recorded in
  `manifest.json`.

## Adding a report

Submit the complete report bundle in a pull request at
`audits/<subject.id>/<evidence.cutoff>/`. Refuse to overwrite an existing report. Before
review, confirm that:

1. `manifest.json` is valid JSON and its entrypoint exists;
2. `subject.id` and `evidence.cutoff` match the destination path;
3. every Git source uses its full resolved commit when known;
4. every selected WGO reviewer records its ID, version, and status; and
5. build junk, local paths, credentials, session IDs, and unresolved placeholders are
   absent.

The pull request may update repository-level discovery files when needed, but it must
not derive a replacement manifest from report prose or an older schema.
