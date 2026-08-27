#!/usr/bin/env python3
"""Deterministic structural validation for the resume corpus.

This is intentionally conservative. It does not claim to reproduce an ATS.
It checks build/output facts that can be measured locally.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path


STANDARD_HEADINGS = [
    "Technical Skills",
    "Projects",
    "Education",
    "Activities",
]


def run(cmd: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, check=False)
    except OSError as exc:
        return subprocess.CompletedProcess(cmd, 127, "", str(exc))


def parse_tex_layout(tex: str) -> dict:
    result = {
        "margin_inches": None,
        "body_font_pt": None,
        "line_height_pt": None,
        "single_column_proxy": True,
        "table_warning": False,
    }

    margin = re.search(r"margin\s*=\s*([0-9.]+)in", tex)
    if margin:
        result["margin_inches"] = float(margin.group(1))

    font = re.search(r"\\fontsize\{([0-9.]+)\}\{([0-9.]+)\}", tex)
    if font:
        result["body_font_pt"] = float(font.group(1))
        result["line_height_pt"] = float(font.group(2))
    else:
        class_font = re.search(r"\\documentclass\[([0-9.]+)pt", tex)
        if class_font:
            result["body_font_pt"] = float(class_font.group(1))

    if re.search(r"\\begin\{(?:multicols|paracol)\}|\\twocolumn", tex):
        result["single_column_proxy"] = False

    if re.search(r"\\begin\{(?:tabular|tabularx|longtable)\}", tex):
        result["table_warning"] = True

    return result


def pdf_page_count(pdf: Path) -> tuple[int | None, str | None]:
    if shutil.which("pdfinfo"):
        proc = run(["pdfinfo", str(pdf)])
        if proc.returncode == 0:
            m = re.search(r"^Pages:\s+(\d+)", proc.stdout, re.MULTILINE)
            if m:
                return int(m.group(1)), None
        return None, proc.stderr.strip() or "pdfinfo failed"
    return None, "pdfinfo not installed"


def extract_pdf_text(pdf: Path) -> tuple[str | None, str | None]:
    if not shutil.which("pdftotext"):
        return None, "pdftotext not installed"
    proc = run(["pdftotext", "-layout", str(pdf), "-"])
    if proc.returncode != 0:
        return None, proc.stderr.strip() or "pdftotext failed"
    return proc.stdout, None


def build_pdf(tex_path: Path) -> tuple[bool, list[str]]:
    if not shutil.which("pdflatex"):
        return False, ["pdflatex not installed"]

    messages: list[str] = []
    for _ in range(2):
        proc = run(
            ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", tex_path.name],
            cwd=tex_path.parent,
        )
        if proc.returncode != 0:
            messages.append(proc.stdout[-4000:])
            messages.append(proc.stderr[-2000:])
            return False, messages
    return True, messages


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tex", default="resume.tex")
    parser.add_argument("--pdf", default="Resume.pdf")
    parser.add_argument("--build", action="store_true")
    args = parser.parse_args()

    tex_path = Path(args.tex)
    pdf_path = Path(args.pdf)

    report = {
        "validator": "resume-corpus structural validator",
        "ats_replica": False,
        "tex": str(tex_path),
        "pdf": str(pdf_path),
        "checks": {},
        "warnings": [],
        "errors": [],
    }

    if not tex_path.exists():
        report["errors"].append("TeX source not found")
        print(json.dumps(report, indent=2))
        return 2

    tex = tex_path.read_text(encoding="utf-8", errors="replace")
    layout = parse_tex_layout(tex)
    report["checks"]["layout"] = layout

    if layout["margin_inches"] is not None and layout["margin_inches"] < 0.5:
        report["errors"].append("Margins are below the 0.5in readability floor.")
    if layout["body_font_pt"] is not None and layout["body_font_pt"] < 11:
        report["errors"].append("Body font is below the 11pt readability floor.")
    if not layout["single_column_proxy"]:
        report["errors"].append("Multi-column layout detected.")
    if layout["table_warning"]:
        report["warnings"].append("Table environment detected; inspect ATS parse safety.")

    source_headings = [h for h in STANDARD_HEADINGS if h in tex]
    report["checks"]["source_headings_found"] = source_headings

    if args.build:
        ok, messages = build_pdf(tex_path)
        report["checks"]["build_ok"] = ok
        if not ok:
            report["errors"].extend(messages)

        generated = tex_path.with_suffix(".pdf")
        if ok and generated.exists() and generated.resolve() != pdf_path.resolve():
            pdf_path.write_bytes(generated.read_bytes())

    if not pdf_path.exists():
        report["warnings"].append("PDF not found; PDF-level checks skipped.")
    else:
        pages, err = pdf_page_count(pdf_path)
        report["checks"]["page_count"] = pages
        if err:
            report["warnings"].append(err)
        if pages is not None and not (1 <= pages <= 2):
            report["errors"].append(f"Page count {pages} is outside the allowed 1–2 page range.")

        text, err = extract_pdf_text(pdf_path)
        if err:
            report["warnings"].append(err)
        elif text is not None:
            report["checks"]["pdf_text_chars"] = len(text.strip())
            report["checks"]["pdf_headings_found"] = [h for h in STANDARD_HEADINGS if h in text]
            if len(text.strip()) < 500:
                report["errors"].append("Extracted PDF text is unexpectedly sparse.")
            missing = [h for h in source_headings if h not in text]
            if missing:
                report["warnings"].append(
                    "Headings present in source but absent in extracted PDF text: " + ", ".join(missing)
                )

    report["status"] = "PASS" if not report["errors"] else "FAIL"
    print(json.dumps(report, indent=2))
    return 0 if not report["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
