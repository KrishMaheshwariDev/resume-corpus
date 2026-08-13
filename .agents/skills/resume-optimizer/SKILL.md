---
name: resume-optimizer
description: Evidence-driven resume optimization for Kunal Maheshwari. Use when asked to optimize, tailor, audit, score, compress, expand, build, or generate a resume from this repository.
---

# Resume Optimizer

## Objective

Produce the strongest truthful, readable 1–2 page resume for the requested role while optimizing both machine retrieval and human review.

Do not treat keyword count as the objective. The goal is high-relevance, high-evidence, low-friction communication.

## Inputs

Resolve from the request or repository:
- run mode;
- source resume;
- target role;
- JD, if any;
- target market/location;
- requested output path;
- requested page preference, if any.

If the user does not provide a JD, use the general Java/backend market baseline.

## Required preflight

Read root `AGENTS.md`, then follow its mandatory preflight list.

Do not skip the August 11 evidence overlays.

## Run-mode selection

### General optimization
Use:
- `profiles/RESUME_POSITIONING_V1.yml`
- `kb/roles/java_backend_engineer.yml`
- `kb/market/india_java_backend.yml`

Goal: a durable Java/backend resume suitable for broad India-market applications.

### JD-specific tailoring
Parse:
- hard requirements;
- preferred requirements;
- responsibilities;
- title/seniority;
- domain;
- architecture/platform expectations;
- likely recruiter search terms.

Map each to verified evidence before rewriting.

### One-page compression
Compress in this order:
1. repeated wording;
2. generic responsibilities;
3. duplicate skills;
4. low-relevance project detail;
5. lower-value optional sections.

Do not remove material evidence, crowd the page, or reduce body text below the repository readability floor merely to hit one page.

### Two-page expansion
Use only when a second page materially improves fit.
Add deeper verified architecture/ownership/project evidence before adding any generic content.

### Audit
Do not edit until the user asks for edits.
Report parse, coverage, evidence, human-review, and truthfulness findings.

## Baseline analysis

Before editing, capture:
- current page count if PDF exists;
- current summary positioning;
- current skill coverage;
- top-half strength;
- current strongest evidence;
- weak/generic bullets;
- source-dependent metrics;
- unsupported or ambiguous claims;
- candidate/role gaps.

If scripts are available, run the deterministic checks. Treat script scores as aids, not truth.

## Evidence map

For every material new or rewritten claim, identify its evidence class:
- P1 professional/production;
- P2 project;
- P3 academic/training;
- P4 knowledge/certification/exposure;
- P5 unresolved.

Reject P5 claims.
Do not convert P2/P3/P4 into P1.

## Editing strategy

Rank candidate edits by expected value:

`role relevance + retrieval value + evidence strength + human signal + differentiation - space cost - redundancy - credibility risk`

Prefer edits with strong evidence and high first-pass value.

### Top-of-resume
The first quarter should answer:
1. What role is Kunal?
2. What scale/complexity has he handled?
3. What makes him different from a generic Java developer?
4. Is there enough credible evidence to continue reading?

### Summary
Use the canonical skimmable capability-summary pattern for all general and tailored resumes unless the user explicitly requests another format:
1. identity, experience depth, and product/domain context;
2. **Delivery scope:** what Kunal can carry from requirements through implementation, testing, release validation, and production support;
3. **Engineering approach:** how he handles performance, reliability, observability, integrations, data, and business-rule boundaries;
4. **Working style:** how he collaborates, communicates, documents, reviews, and mentors.

Write for a recruiter's first-pass scan. Keep these labels visually distinct, use short evidence-backed phrases, and make the bold anchors sufficient to reconstruct the intended value proposition. Retain searchable technologies and discussion hooks, but keep detailed metrics and proof in the experience section. Adapt technologies and emphasis to the target JD without changing the four-part structure or fabricating capability.

### Experience bullets
For each employer:
- strongest target-role evidence first;
- one dominant idea per bullet;
- technology in context, not only in Skills;
- use direct, measured language;
- favor direct timings/scale over reconstructed marketing percentages.

### Skills
Preserve truthful parser/search coverage.
For targeted resumes, omit low-value skills if necessary, but never delete them from the profile corpus.
Label project/knowledge-only areas when the unqualified term would create a misleading production impression.

### Projects
Projects exist to:
- demonstrate modern capabilities absent from employment;
- close truthful role gaps;
- show architecture depth.

Do not let projects displace stronger production evidence for ordinary Java/backend roles.

### Cross-section alignment gate

Before editing, and again before release, build a compact cross-section evidence map:

`Summary capability or skill -> Work Experience/Project proof -> evidence class and depth`

Rules:
- every material Summary promise must have visible downstream proof;
- every prominent technology or skill family must be used in context in Work Experience or Projects, using exact wording or a clear semantic alias;
- professional skills map to Work Experience; project skills map to Projects and retain project qualification;
- P4 knowledge/exposure/certification may appear without a delivery bullet only when explicitly labeled and relevant;
- an underlying corpus fact is not enough to justify an orphaned resume keyword;
- remove, qualify, or add concise verified context for every material orphan;
- confirm that relevant differentiated downstream proof is represented in the top half rather than hidden.

Treat unresolved material orphans as a failed release gate, not a cosmetic warning.

## Current candidate-specific safeguards

Prefer:
- NTT: 50K+ daily requests, 99.99% SLA, Java/JAX-WS/Spring, WebSphere, healthcare payer integration, hybrid/service integration, Log4j2 migration ownership, monitoring/correlation IDs, release validation.
- Capgemini: Java EE/JSF/Hibernate/WebLogic/DB2, Python prediction integration with deterministic Java validation, VIN latency ~60+ sec to ~10–20 sec, cross-system debugging, mentoring.
- AWS project: S3 -> Lambda -> EFS -> Spark Structured Streaming -> PostgreSQL/RDS, Terraform, Docker, checkpoints, 8GB+ dataset.
- Portfolio: React/TypeScript/Vite/Tailwind, skill-evidence search, case studies, GitHub Pages.

Avoid as default:
- NTT 20% issue-resolution metric unless intentionally sourced;
- Capgemini broad ~90% metric when VIN timing is the actual evidence;
- AWS 40% metric without baseline;
- production Kafka/Kubernetes;
- multi-node Spark;
- exactly-once PostgreSQL;
- production FHIR ownership;
- API Gateway authentication ownership;
- sole production deployment ownership.

## Scoring loop

Use a scored improvement loop:

1. baseline;
2. identify highest-value weaknesses;
3. propose edits;
4. truthfulness gate;
5. apply edits;
6. build;
7. validate;
8. re-score;
9. compare before/after;
10. keep only net-positive credible changes.

Stop when:
- release gates are met; or
- no material truthful improvement remains; or
- further improvement would require unsupported experience.

Do not iterate merely to inflate a heuristic number.

## Build/QA

Preferred commands:

```bash
python scripts/validate_resume.py --tex resume.tex --pdf Resume.pdf
python scripts/score_resume.py --resume resume.tex
```

If `Resume.pdf` is stale, rebuild it before claiming final validation.

Check:
- 1–2 pages;
- body font >=11pt (hard floor; never reduce below it to meet a page target);
- margins >=0.5in unless explicitly overridden;
- readable line spacing and section separation;
- restrained bold emphasis on high-value technologies, metrics, and outcomes;
- no forced page break that creates a large avoidable blank region;
- no repeated identity header on page two unless explicitly requested;
- section headings kept with following content;
- visible spacing between headings, titles/subtitles, and body text;
- single-column/readable text;
- standard headings;
- no bullet overflow/splitting where avoidable;
- PDF extraction;
- high-value term regression;
- evidence boundary compliance.
- Summary/Skills-to-Experience/Projects alignment, with no material orphaned claims or unqualified technologies.

## Variant storage

Before starting any optimization that creates or edits a tailored variant, run:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/archive-tailored-resumes.ps1
```

This is the daily tailored-file preflight. It moves every dated variant older than the current local date from `resumes/tailored/` to `resumes/tailored/old/DD-MM.YYYY/`, preserving the full variant directory. It must run before the new current-day variant is created. Do not overwrite collisions or infer dates for undated directories.

General baseline:
- `resume.tex`
- `Resume.pdf`

JD-specific:
- `resumes/tailored/<company-role-YYYY-MM-DD>/resume.tex`
- corresponding PDF if generated;
- `jd.txt` or `jd.md`;
- optional `optimization_report.yml`.

Archived JD-specific:
- `resumes/tailored/old/DD-MM.YYYY/<company-role-YYYY-MM-DD>/`

Do not overwrite `resume.tex` for a one-off JD unless the user explicitly asks.

## Final report

Return:
- run mode;
- target;
- baseline vs final scores;
- page count;
- strongest evidence retained/promoted;
- key edits;
- hard gaps;
- claims excluded for truthfulness;
- validation status;
- changed files.
