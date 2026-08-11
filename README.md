# Resume Corpus

Evidence-driven resume optimization repository for Kunal Maheshwari.

The repository separates:
- candidate facts/evidence;
- market/role knowledge;
- scoring and writing policy;
- Codex orchestration/workflows;
- canonical and tailored resume artifacts;
- deterministic validation;
- behavioral eval cases.

The system must optimize for both machine retrieval and human review without pretending to reproduce one proprietary ATS score.

## Agent entry point

Codex should read:

1. `AGENTS.md`
2. `.agents/skills/resume-optimizer/SKILL.md` when doing resume work
3. `.agents/skills/market-benchmark-refresh/SKILL.md` only when current-market research/refresh is requested

`AGENTS.md` is the orchestration contract. Detailed facts stay in `profiles/` and detailed policy stays in `kb/`.

## Current structure

```text
AGENTS.md

.agents/
  skills/
    resume-optimizer/SKILL.md
    market-benchmark-refresh/SKILL.md

resume.tex
Resume.pdf

profiles/
  MASTER_PROFILE_V2.md
  PROFILE_FACT_MATRIX_V2.yml
  WORK_EXPERIENCE_EVIDENCE_OVERLAY_2026-08-11.md
  PROJECT_EVIDENCE_OVERLAY_2026-08-11.md
  EVIDENCE_FACT_OVERLAY_2026-08-11.yml
  ARCHIVE_RESUME_CORPUS_AUDIT.md
  UNRESOLVED_SOURCES.md
  RESUME_POSITIONING_V1.yml

kb/
  optimization_run_protocol.md
  optimization_run_checklist.yml
  resume_output_requirements.yml
  resume_optimization_knowledge_base.md
  research/resume_research_2026.md
  market/india_java_backend.yml
  human_review/resume_perception_knowledge_base.md
  scoring/weights.yml
  scoring/human_review_weights.yml
  skills/java_backend_taxonomy.yml
  roles/java_backend_engineer.yml
  writing/bullet_semantics.yml
  writing/action_verbs_java_backend.yml

benchmarks/
  java_backend/benchmark_manifest.yml

scripts/
  validate_resume.py
  score_resume.py

evals/
  resume_optimizer_cases.yml

resumes/
  README.md
  general/README.md
  tailored/README.md

runs/
  README.md
```

Legacy/archive files may remain elsewhere for audit/history.

## Core operating rule

Never edit a resume from memory alone.

For every optimization, follow:
- `AGENTS.md`;
- `kb/optimization_run_protocol.md`;
- `kb/optimization_run_checklist.yml`;
- V2 profile and August 11 evidence overlays;
- `profiles/RESUME_POSITIONING_V1.yml`;
- relevant role/market/scoring/writing policy.

## Evidence precedence

Unless the active user explicitly resolves something differently:

1. explicit user confirmation in the current conversation;
2. August 11 evidence overlays;
3. current repo resume source;
4. V2 master profile/fact matrix;
5. archive/export evidence;
6. current project repositories;
7. older resume variants.

For implementation boundaries, current repository code can outrank older resume wording.

Do not silently resolve HR title/date/contact conflicts.

## Resume philosophy

A resume is a relevance-ranked evidence document, not a career archive.

Optimize for:
1. parse/retrieval;
2. rapid recruiter comprehension;
3. deeper technical credibility.

Every line should contribute relevance, technical capability, ownership, context, scale/constraint, outcome, credibility, or differentiated evidence.

## Page policy

Use 1–2 pages.

- Prefer one page when material evidence fits naturally.
- Use two pages when the second page materially improves role fit.
- Never add filler.
- Never remove material evidence just to satisfy one page.
- Do not shrink below 10pt body text / 0.5in margins merely to force fit.

See `kb/resume_output_requirements.yml`.

## Scoring

Report separate:
- Parse Safety;
- Requirement/Market Coverage;
- Evidence Strength;
- Human Review;
- Composite Fit.

Target Composite Fit >=80 when truthfully achievable, but never fabricate experience to reach a number.

See `kb/scoring/weights.yml`.

## Canonical vs tailored resumes

Root:
- `resume.tex` = canonical general Java/backend source.
- `Resume.pdf` = canonical compiled output, valid only after rebuilding from the current source.

JD-specific variants belong under `resumes/tailored/` unless the user explicitly asks to replace the canonical resume.

## Validation

After material edits:

```bash
python scripts/validate_resume.py --tex resume.tex --pdf Resume.pdf
python scripts/score_resume.py --resume resume.tex
```

Use existing build scripts or `pdflatex` to rebuild the PDF first when needed.

The scripts are explainable local checks, not ATS replicas.

## Non-negotiable truthfulness rules

Do not invent:
- technologies;
- years;
- metrics;
- leadership;
- production exposure;
- ownership;
- distributed-system guarantees.

Current important boundaries include:
- prefer Capgemini VIN timing (~60+ sec -> ~10–20 sec) over the older ~90% claim;
- do not default to the older NTT 20% issue-resolution number;
- AWS 40% runtime metric is source-dependent;
- AWS Spark is local mode inside the ECS container in current code;
- checkpointing does not prove exactly-once JDBC persistence;
- Kafka/Kubernetes are not production ownership;
- FHIR is PoC/exposure unless newer evidence changes that.

See the August 11 overlays for the authoritative detail.
