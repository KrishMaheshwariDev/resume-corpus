#!/usr/bin/env python3
"""Explainable heuristic scorecard for the resume corpus.

This is not a proprietary ATS replica. It produces deterministic indicators for:
- parse/structure proxy,
- general-market keyword coverage,
- evidence placement,
- human-review proxy,
- composite fit.

JD-specific semantic evaluation still requires the resume-optimizer workflow.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


CRITICAL = {
    "Java": [r"\bJava\b"],
    "Spring": [r"\bSpring Boot\b", r"\bSpring Framework\b"],
    "API": [r"\bREST", r"\bSOAP", r"\bJAX-WS\b"],
    "SQL": [r"\bSQL\b", r"\bOracle\b", r"\bDB2\b", r"\bPostgreSQL\b"],
    "Backend": [r"\bBackend\b", r"\bmicroservices?\b", r"\bSOA\b"],
}

COMMON = {
    "Persistence": [r"\bJPA\b", r"\bHibernate\b", r"\bJDBC\b", r"\bHQL\b"],
    "Testing": [r"\bJUnit\b", r"\bUnit Testing\b", r"\bIntegration Testing\b"],
    "CI/CD": [r"\bCI/CD\b", r"\bJenkins\b", r"\bAzure DevOps\b", r"\bGitLab CI/CD\b"],
    "Cloud": [r"\bAWS\b", r"\bAzure\b"],
    "Build": [r"\bMaven\b", r"\bGradle\b", r"\bGit\b"],
    "Production": [r"\bProduction Support\b", r"\bproduction\b", r"\bSLA\b"],
}

HIGH_VALUE_PROOFS = [
    r"50K\+",
    r"99\.99",
    r"60\+\s*sec",
    r"10.?20\s*sec",
    r"Log4j2",
    r"correlation",
    r"WebSphere",
    r"WebLogic",
]


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def present(text: str, patterns: list[str]) -> bool:
    return any(re.search(p, text, re.IGNORECASE) for p in patterns)


def section(text: str, start: str, end_markers: list[str]) -> str:
    idx = text.find(start)
    if idx < 0:
        return ""
    tail = text[idx:]
    end_positions = [tail.find(x, len(start)) for x in end_markers if tail.find(x, len(start)) >= 0]
    end = min(end_positions) if end_positions else len(tail)
    return tail[:end]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--resume", default="resume.tex")
    args = parser.parse_args()

    path = Path(args.resume)
    if not path.exists():
        print(json.dumps({"status": "FAIL", "error": "resume not found"}, indent=2))
        return 2

    text = load_text(path)
    experience = section(text, r"\ressection{Work Experience}", [r"\ressection{Projects}", r"\ressection{Education}"])
    summary = section(text, r"\ressection{Summary}", [r"\ressection{Technical Skills}", r"\ressection{Work Experience}"])

    critical_hits = {k: present(text, v) for k, v in CRITICAL.items()}
    common_hits = {k: present(text, v) for k, v in COMMON.items()}

    critical_score = 100 * sum(critical_hits.values()) / len(critical_hits)
    common_score = 100 * sum(common_hits.values()) / len(common_hits)
    market_coverage = round(0.7 * critical_score + 0.3 * common_score, 1)

    evidence_hits = 0
    evidence_total = 0
    for _, patterns in {**CRITICAL, **COMMON}.items():
        evidence_total += 1
        if present(experience, patterns):
            evidence_hits += 1
    evidence_strength = round(100 * evidence_hits / evidence_total, 1)

    parse_safety = 100.0
    if re.search(r"\\begin\{(?:multicols|paracol)\}|\\twocolumn", text):
        parse_safety -= 30
    if re.search(r"\\begin\{(?:tabular|tabularx|longtable)\}", text):
        parse_safety -= 15
    margin = re.search(r"margin\s*=\s*([0-9.]+)in", text)
    if margin and float(margin.group(1)) < 0.5:
        parse_safety -= 10
    font = re.search(r"\\fontsize\{([0-9.]+)\}", text)
    if font and float(font.group(1)) < 10:
        parse_safety -= 10
    parse_safety = max(parse_safety, 0)

    human = 50.0
    if re.search(r"Java\s+(?:Backend|/Spring)", summary, re.IGNORECASE):
        human += 12
    proof_count = sum(1 for p in HIGH_VALUE_PROOFS if re.search(p, text, re.IGNORECASE))
    human += min(proof_count * 4, 24)
    weak_openers = len(re.findall(r"\\item\s+(?:Responsible for|Worked on|Helped|Involved in|Assisted)", text, re.IGNORECASE))
    human -= weak_openers * 5
    long_bullets = [b for b in re.findall(r"\\item\s+(.+)", text) if len(b) > 360]
    human -= min(len(long_bullets) * 3, 12)
    human_review = round(max(0, min(100, human)), 1)

    composite = round(
        0.35 * market_coverage
        + 0.25 * evidence_strength
        + 0.20 * parse_safety
        + 0.20 * human_review,
        1,
    )

    stuffing = {}
    for term in ["Java", "Spring Boot", "AWS", "Azure", "SQL", "Kafka", "Kubernetes"]:
        count = len(re.findall(re.escape(term), text, re.IGNORECASE))
        if count >= 5:
            stuffing[term] = count

    report = {
        "scorecard": "resume-corpus explainable heuristic",
        "proprietary_ats_replica": False,
        "resume": str(path),
        "scores": {
            "parse_safety": round(parse_safety, 1),
            "general_market_coverage": market_coverage,
            "evidence_strength_proxy": evidence_strength,
            "human_review_proxy": human_review,
            "composite_fit_proxy": composite,
        },
        "critical_market_hits": critical_hits,
        "common_market_hits": common_hits,
        "high_value_proof_count": proof_count,
        "keyword_saturation_warnings": stuffing,
        "notes": [
            "JD-specific hard requirements and semantic responsibility match require the resume-optimizer workflow.",
            "A score >=80 is a repository target, not a universal ATS guarantee.",
            "Truthfulness/evidence overlays override any score incentive.",
        ],
    }
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
