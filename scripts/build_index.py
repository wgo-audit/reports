#!/usr/bin/env python3
"""Regenerate the report index from manifest.json files.

Reads every audits/<asset>/<cutoff>/manifest.json and rewrites, idempotently:
  - the BADGES and REPORTS blocks in README.md (between HTML-comment markers)
  - audits/<asset>/README.md   (per-asset timeline + conclusions-over-time matrix)
  - audits/index.json          (machine-readable catalog)

Run it after adding or editing a report, then commit the result. CI runs the
same script and fails if anything is out of date (see .github/workflows/reindex.yml).

Standard library only — no third-party dependencies.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AUDITS = ROOT / "audits"
README = ROOT / "README.md"
REPO = "wgo-audit/reports"
SCHEMA_VERSION = "1.0.0"

AUDIT_LABELS = {
    "continuity-and-third-party-operability": "Continuity & third-party operability",
    "regulated-esignature-readiness": "Regulated eSignature readiness",
}


def load_reports() -> list[dict]:
    reports = []
    for manifest in sorted(AUDITS.glob("*/*/manifest.json")):
        data = json.loads(manifest.read_text(encoding="utf-8"))
        data["_dir"] = manifest.parent.relative_to(ROOT).as_posix()
        data["_asset"] = manifest.parent.parent.name
        data["_cutoff"] = manifest.parent.name
        validate_manifest(data, manifest)
        reports.append(data)
    return reports


def esc(value) -> str:
    return str(value).replace("|", "\\|")


def manifest_version(report: dict) -> str | None:
    return report.get("schemaVersion")


def subject_id(report: dict) -> str:
    if manifest_version(report) == SCHEMA_VERSION:
        return report["subject"]["id"]
    return report.get("asset") or report["_asset"]


def subject_name(report: dict) -> str:
    if manifest_version(report) == SCHEMA_VERSION:
        return report["subject"].get("name") or subject_id(report)
    return report.get("asset") or report["_asset"]


def subject_url(report: dict) -> str | None:
    if manifest_version(report) == SCHEMA_VERSION:
        return report["subject"].get("canonicalUrl")
    return report.get("assetUrl")


def evidence_cutoff(report: dict) -> str:
    if manifest_version(report) == SCHEMA_VERSION:
        return report["evidence"]["cutoff"]
    return report.get("evidenceCutoff") or report["_cutoff"]


def report_title(report: dict) -> str:
    if manifest_version(report) == SCHEMA_VERSION:
        return report["report"]["title"]
    return report.get("title") or label(report)


def generated_at(report: dict):
    if manifest_version(report) == SCHEMA_VERSION:
        return report["report"].get("generatedAt")
    return report.get("generatedAt")


def entrypoint(report: dict) -> str:
    if manifest_version(report) == SCHEMA_VERSION:
        return report["report"]["entrypoint"]
    return report.get("entrypoint", "index.md")


def headline(report: dict) -> dict | None:
    if manifest_version(report) == SCHEMA_VERSION:
        value = report["report"].get("headline")
        return value if isinstance(value, dict) else None
    text = report.get("headline")
    if text:
        return {"rating": None, "statement": text}
    return None


def audit_label_from_type(audit_type: str) -> str:
    if audit_type in AUDIT_LABELS:
        return AUDIT_LABELS[audit_type]
    words = audit_type.replace("_", "-").split("-")
    if not words:
        return "Audit"
    rendered = []
    for i, word in enumerate(words):
        if word == "and":
            rendered.append("&")
        elif i == 0:
            rendered.append(word.capitalize())
        else:
            rendered.append(word)
    return " ".join(rendered)


def label(report: dict) -> str:
    if manifest_version(report) == SCHEMA_VERSION:
        audit = report["audit"]
        kind = audit_label_from_type(audit["type"])
        depth = audit.get("depth")
        return f"{kind} ({depth})" if depth else kind
    if report.get("label"):
        return report["label"]
    kind = str(report.get("auditType", "audit")).replace("-", " ")
    depth = report.get("depth")
    return f"{kind} ({depth})" if depth else kind


def conclusions(report: dict) -> dict[str, str]:
    if manifest_version(report) == SCHEMA_VERSION:
        out = {}
        for concern in report.get("businessConcerns") or []:
            conclusion = concern.get("conclusion") or {}
            out[concern["statement"]] = conclusion.get("statement", "")
        return out
    return report.get("conclusions") or {}


def highlights(report: dict) -> list[str]:
    if manifest_version(report) == SCHEMA_VERSION:
        value = headline(report)
        return [value["statement"]] if value and value.get("statement") else []
    return report.get("highlights", [])


def validate_manifest(report: dict, manifest: Path) -> None:
    if manifest_version(report) != SCHEMA_VERSION:
        return

    rel = manifest.relative_to(ROOT).as_posix()
    report_root = manifest.parent
    if subject_id(report) != report["_asset"]:
        raise SystemExit(
            f"{rel}: subject.id must match audits/<subject>; "
            f"got {subject_id(report)!r}, expected {report['_asset']!r}"
        )
    if evidence_cutoff(report) != report["_cutoff"]:
        raise SystemExit(
            f"{rel}: evidence.cutoff must match the report directory; "
            f"got {evidence_cutoff(report)!r}, expected {report['_cutoff']!r}"
        )
    entry = report_root / entrypoint(report)
    if not entry.is_file():
        raise SystemExit(f"{rel}: report.entrypoint does not exist: {entrypoint(report)}")

    ids = [c.get("id") for c in report.get("businessConcerns") or []]
    if len(ids) != len(set(ids)):
        raise SystemExit(f"{rel}: businessConcerns ids must be unique")

    for source in report.get("evidence", {}).get("sources") or []:
        commit = source.get("commit")
        if commit and not re.fullmatch(r"[0-9a-fA-F]{40}", commit):
            raise SystemExit(
                f"{rel}: evidence source {source.get('id')!r} has a non-full SHA: {commit}"
            )

    for concern in report.get("businessConcerns") or []:
        source = (concern.get("conclusion") or {}).get("source")
        if source and not (report_root / source).is_file():
            raise SystemExit(
                f"{rel}: business concern {concern.get('id')!r} references "
                f"a missing conclusion source: {source}"
            )

    cost_source = (
        report.get("execution", {})
        .get("costEstimate", {})
        .get("source")
    )
    if cost_source and not (report_root / cost_source).is_file():
        raise SystemExit(f"{rel}: execution.costEstimate.source does not exist: {cost_source}")


def group_by_asset(reports: list[dict]) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = {}
    for report in reports:
        grouped.setdefault(subject_id(report), []).append(report)
    for rs in grouped.values():
        rs.sort(key=evidence_cutoff, reverse=True)
    return grouped


def reports_section(reports: list[dict]) -> str:
    if not reports:
        return "_No reports published yet._\n"
    rs = sorted(reports, key=evidence_cutoff, reverse=True)
    rs = sorted(rs, key=subject_id)
    out = ["| Asset | Evidence cutoff | Audit |", "|---|---|---|"]
    for r in rs:
        asset_link = f'[{subject_id(r)}](audits/{subject_id(r)}/README.md)'
        cutoff_link = f'[{evidence_cutoff(r)}]({r["_dir"]}/{entrypoint(r)})'
        out.append(f'| {asset_link} | {cutoff_link} | {esc(label(r))} |')
    return "\n".join(out).rstrip() + "\n"


def badges_block(reports: list[dict]) -> str:
    # Raw HTML (not markdown, which wouldn't parse next to the banner block),
    # left-aligned, matching the org profile's flat-square + dark-label + teal.
    n = len(reports)
    style = "style=flat-square&labelColor=111827"
    accent = "2DD4BF"
    return (
        f'<a href="#reports"><img alt="Reports" '
        f'src="https://img.shields.io/badge/Reports-{n}-{accent}?{style}"></a>\n'
        f'<a href="https://github.com/{REPO}/commits/main"><img alt="Last commit" '
        f'src="https://img.shields.io/github/last-commit/{REPO}?{style}&color={accent}&label=Last%20commit"></a>\n'
        f'<a href="LICENSE.md"><img alt="License" '
        f'src="https://img.shields.io/github/license/{REPO}?{style}&color={accent}"></a>\n'
    )


def replace_block(text: str, name: str, content: str) -> str:
    start, end = f"<!-- {name}:START -->", f"<!-- {name}:END -->"
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    if not pattern.search(text):
        raise SystemExit(f"marker <!-- {name} --> not found in README.md")
    return pattern.sub(f"{start}\n{content}{end}", text)


def per_asset_readme(asset: str, rs: list[dict]) -> str:
    asset_url = next((subject_url(r) for r in rs if subject_url(r)), None)
    name = next((subject_name(r) for r in rs if subject_name(r)), asset)
    asset_ref = f"[{name}]({asset_url})" if asset_url else name
    out = [
        f"# {asset}",
        "",
        f"Point-in-time audits of {asset_ref}, newest first. Each row is a frozen "
        "snapshot; read across the columns below to see how the situation changes "
        "over time.",
        "",
        "| Evidence cutoff | Audit |",
        "|---|---|",
    ]
    for r in rs:
        link = f'[{evidence_cutoff(r)}]({r["_cutoff"]}/{entrypoint(r)})'
        out.append(f'| {link} | {esc(label(r))} |')
    out.append("")

    keys: list[str] = []
    for r in rs:
        for key in conclusions(r):
            if key not in keys:
                keys.append(key)
    current_highlights = highlights(rs[0]) if rs else []
    if keys or current_highlights:
        out.append("## Conclusions over time")
        out.append("")
        for item in current_highlights:
            out.append(f"- {item}")
        if current_highlights:
            out.append("")
        if keys:
            out.append("| Question | " + " | ".join(evidence_cutoff(r) for r in rs) + " |")
            out.append("|" + "---|" * (len(rs) + 1))
            for key in keys:
                cells = [esc(key)]
                for r in rs:
                    cells.append(esc(conclusions(r).get(key, "—")))
                out.append("| " + " | ".join(cells) + " |")
            out.append("")
    return "\n".join(out).rstrip() + "\n"


def index_json(reports: list[dict]) -> dict:
    items = []
    for r in sorted(reports, key=lambda r: (subject_id(r), evidence_cutoff(r)), reverse=True):
        head = headline(r)
        items.append({
            "reportId": r.get("report", {}).get("id") if manifest_version(r) == SCHEMA_VERSION else None,
            "subject": subject_id(r),
            "subjectName": subject_name(r),
            "evidenceCutoff": evidence_cutoff(r),
            "path": r["_dir"],
            "entrypoint": entrypoint(r),
            "title": report_title(r),
            "label": label(r),
            "headline": head,
            "generatedAt": generated_at(r),
        })
    return {"count": len(items), "reports": items}


def main() -> None:
    reports = load_reports()

    text = README.read_text(encoding="utf-8")
    text = replace_block(text, "BADGES", badges_block(reports))
    text = replace_block(text, "REPORTS", reports_section(reports))
    README.write_text(text, encoding="utf-8")

    for asset, rs in group_by_asset(reports).items():
        (AUDITS / asset / "README.md").write_text(
            per_asset_readme(asset, rs), encoding="utf-8"
        )

    (AUDITS / "index.json").write_text(
        json.dumps(index_json(reports), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(f"indexed {len(reports)} report(s)")


if __name__ == "__main__":
    main()
