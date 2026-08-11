# Resume Corpus Agent Contract

## Mission

This repository is Kunal Maheshwari's evidence-driven resume optimization system.

Optimize resumes for:
1. truthful role fit,
2. reliable ATS/AI parsing and retrieval,
3. fast recruiter comprehension,
4. deeper hiring-manager credibility,
5. moderate, readable information density.

Do not optimize for a fictional universal ATS score. Use the repository's explainable scorecards and evidence rules.

## Canonical artifacts

- `resume.tex` — canonical general-market resume source.
- `Resume.pdf` — compiled canonical artifact; it is valid only when rebuilt from the current `resume.tex`.
- `profiles/` — factual and evidence sources.
- `kb/` — optimization, role, market, writing, scoring, and human-review policy.
- `.agents/skills/` — reusable Codex workflows.
- `scripts/` — deterministic validation/scoring helpers.
- `evals/` — regression cases for resume behavior.
- `resumes/tailored/` — JD-specific variants. Do not overwrite the canonical general resume for a one-off JD unless the user explicitly asks.

## Evidence precedence

Before changing a resume, use this precedence:

1. explicit user confirmation in the active conversation;
2. `profiles/WORK_EXPERIENCE_EVIDENCE_OVERLAY_2026-08-11.md`;
3. `profiles/PROJECT_EVIDENCE_OVERLAY_2026-08-11.md`;
4. `profiles/EVIDENCE_FACT_OVERLAY_2026-08-11.yml`;
5. current repo resume source;
6. `profiles/MASTER_PROFILE_V2.md` and `profiles/PROFILE_FACT_MATRIX_V2.yml`;
7. archive/export evidence and current project repositories;
8. older resume variants.

Never silently resolve HR title, employment-date, contact, final GPA, or work-authorization conflicts unless a higher-priority source explicitly resolves them.

## Mandatory preflight

For any resume edit, optimization, score, or tailored variant, load:

1. `kb/optimization_run_protocol.md`
2. `kb/optimization_run_checklist.yml`
3. `profiles/MASTER_PROFILE_V2.md`
4. `profiles/PROFILE_FACT_MATRIX_V2.yml`
5. `profiles/ARCHIVE_RESUME_CORPUS_AUDIT.md`
6. `profiles/WORK_EXPERIENCE_EVIDENCE_OVERLAY_2026-08-11.md`
7. `profiles/PROJECT_EVIDENCE_OVERLAY_2026-08-11.md`
8. `profiles/EVIDENCE_FACT_OVERLAY_2026-08-11.yml`
9. `profiles/UNRESOLVED_SOURCES.md`
10. `profiles/RESUME_POSITIONING_V1.yml`
11. `kb/resume_optimization_knowledge_base.md`
12. `kb/human_review/resume_perception_knowledge_base.md`
13. `kb/scoring/weights.yml`
14. `kb/scoring/human_review_weights.yml`
15. `kb/skills/java_backend_taxonomy.yml`
16. `kb/roles/java_backend_engineer.yml`
17. `kb/market/india_java_backend.yml` for general India Java/backend work
18. `kb/writing/bullet_semantics.yml`
19. `kb/writing/action_verbs_java_backend.yml`
20. `kb/resume_output_requirements.yml`

Do not edit from model memory alone.

## Default positioning

Primary role family:
- Java Backend Engineer
- Backend Software Engineer
- Java/Spring Backend Engineer
- Software Engineer II / SDE II
- Senior Java Developer where seniority requirements are credible

Primary differentiators:
- enterprise Java/Spring/SOAP/REST integration experience;
- healthcare and automotive domain systems;
- 50K+ daily-request production scale and 99.99% SLA context;
- hybrid integration/messaging and enterprise middleware;
- production troubleshooting, observability, release validation, and modernization;
- direct Capgemini VIN API latency reduction from ~60+ seconds to ~10–20 seconds;
- project-backed AWS/Terraform/Spark/React breadth.

Do not over-position Kunal as a production Kafka specialist, Kubernetes/platform engineer, Java 17 production engineer, pure frontend engineer, pure data engineer, or senior AI engineer unless new verified evidence supports it.

## Optimization modes

Use `.agents/skills/resume-optimizer/SKILL.md`.

Supported modes:
- general optimization;
- JD-specific tailoring;
- one-page compression;
- two-page expansion;
- ATS/AI parse and retrieval audit;
- recruiter/hiring-manager review;
- resume build and validation.

For current-market research or benchmark refresh, use `.agents/skills/market-benchmark-refresh/SKILL.md`. Do not browse the market on every normal edit.

## Page-length policy

Default to the shortest version that preserves material evidence and remains easy to read.

- Allowed: 1–2 pages.
- One page is preferred when the candidate's strongest relevant evidence fits naturally.
- Two pages are allowed when page two adds material role-relevant evidence, architecture depth, or projects required for the target.
- Page two must earn its existence.
- Never add filler to reach two pages.
- Never remove material evidence merely to satisfy one page.
- Do not shrink normal body text below 10 pt or margins below 0.5 in merely to fit content unless the user explicitly requests a denser format.
- Prefer deleting redundancy before tightening layout.

## Content-selection rule

A resume is a relevance-ranked evidence document, not a career archive.

Every line should contribute at least one of:
- target-role relevance;
- technical capability;
- ownership;
- system/domain context;
- scale or constraint;
- measurable outcome;
- credibility;
- differentiated evidence.

Remove or compress filler, generic responsibilities, repeated tools, and weak self-description.

Do not delete skills from the factual corpus just because they are omitted from a tailored resume. A tailored resume may omit low-relevance skills while preserving them in profile/KB sources.

## Evidence and claim rules

Classify claims mentally as:
- P1 — verified professional/production evidence;
- P2 — verified project evidence;
- P3 — verified academic/training evidence;
- P4 — certification/knowledge/exposure;
- P5 — unresolved or unsupported.

P1 can support strong employment bullets.
P2 belongs in projects unless directly tied to employment.
P3 must remain clearly academic/training.
P4 can appear in skills/certifications with appropriate restraint.
P5 must not be promoted without user confirmation.

Special current boundaries:
- `50K+ daily requests` and `99.99% SLA` are safe conservative NTT signals.
- Log4j2 migration has strong ownership; the older `20% issue-resolution` number is source-dependent and should not be the default.
- Capgemini VIN latency has direct evidence: ~60+ sec to ~10–20 sec. Prefer this over the older broad `~90%` claim.
- AWS Spark project's `40% runtime improvement` is source-dependent until its comparison baseline is reconstructed.
- AWS Spark currently uses local-mode Spark inside the ECS container. Do not claim multi-node Spark execution.
- Checkpointing does not prove end-to-end exactly-once JDBC/PostgreSQL writes.
- Kafka and Kubernetes must not be represented as production ownership without separate evidence.
- FHIR is PoC/exposure unless stronger evidence is added.
- API Gateway authentication was owned by another team; describe the security boundary accurately.
- Production deployment execution at NTT was handled by a deployment team; Kunal supported artifacts, validation, go/no-go/rollback recommendations, and smoke/business checks.

## Bullet-writing policy

Prefer one dominant idea per bullet.

Use varied structures based on the strongest signal:
- action-first;
- impact-first;
- scale-first;
- architecture-first;
- modernization-first.

Strong engineering bullets usually contain 3–5 dimensions:
`action/ownership + technology/method + system/domain + scale/constraint + outcome`

Do not force a metric into every bullet.
Do not use a single formula mechanically.
Avoid weak openers such as `Responsible for`, `Worked on`, `Helped with`, or `Involved in`.
Avoid promotional adjectives when evidence can do the work.

## Section and scan policy

For general Java/backend resumes, default order:
1. Name/contact
2. Summary
3. Technical Skills
4. Work Experience
5. Projects
6. Education
7. Certifications

For a JD-specific resume, reorder lower sections only when it materially improves relevance.

The first screen/top quarter should establish:
- Java/backend identity;
- experience level;
- Spring/API/database/cloud/integration fit;
- one or more memorable proof points.

The first bullet under each employer must be the strongest role-relevant evidence.

## Scoring and release gates

Use repository scores as explainable heuristics, not proprietary ATS replicas.

Report separately:
- Parse Safety
- Requirement/Market Coverage
- Evidence Strength
- Human Review
- Composite Fit

Default target when truthfully achievable:
- Truthfulness: PASS
- Parse Safety: >= 95
- Human Review: >= 82
- Composite Fit: >= 80
- no hidden failed critical requirement;
- no keyword stuffing;
- no unsupported ownership/metrics.

If a target role cannot credibly reach 80 because of a real skill/seniority gap, report the maximum credible fit and the gap. Never invent experience to hit a threshold.

## General-market optimization

When there is no JD:
- use `kb/roles/java_backend_engineer.yml`;
- use `kb/market/india_java_backend.yml`;
- use `profiles/RESUME_POSITIONING_V1.yml`;
- optimize for broad 3–7 year Java/backend hiring;
- favor durable evidence over trendy unsupported tools.

## JD-specific variants

When given a JD:
1. parse mandatory, preferred, responsibility, seniority, domain, and technology requirements;
2. map each important requirement to evidence;
3. mark exact/alias/semantic/weak/missing;
4. identify hard gaps before writing;
5. tailor wording and section emphasis without fabricating;
6. save a variant under `resumes/tailored/<company-role-date>/` unless the user explicitly wants to replace `resume.tex`;
7. preserve the canonical general resume.

## Build and validation

A source edit is not complete until the output is checked.

Preferred workflow:
1. compile the LaTeX source;
2. confirm a PDF is produced;
3. check page count;
4. extract PDF text;
5. verify standard headings and contact text survive;
6. check font/margin/page policy;
7. check for obvious keyword regression;
8. compare current source claims against evidence boundaries;
9. re-score after edits.

Use:
- existing `build-resume.ps1` / `build-resume.cmd` when appropriate;
- `python scripts/validate_resume.py --tex resume.tex --pdf Resume.pdf`;
- `python scripts/score_resume.py --resume resume.tex`.

If a validation tool is unavailable, report the limitation rather than claiming it passed.

## Regression discipline

Before finalizing an optimization:
- compare before/after high-value signals;
- preserve or intentionally replace the strongest evidence;
- reject an edit that improves prose but materially damages retrieval or truthfulness;
- use `evals/resume_optimizer_cases.yml` as behavioral regression guidance.

## Output report

Every material optimization should report:
- mode;
- source resume;
- target role/JD;
- files loaded;
- page count;
- Parse Safety;
- Requirement/Market Coverage;
- Evidence Strength;
- Human Review;
- Composite Fit;
- hard gaps;
- strongest retained evidence;
- edits made;
- claims intentionally not used and why;
- unresolved source conflicts;
- validation results;
- files changed.

## Repository hygiene

- Do not commit LaTeX auxiliary/build clutter unless explicitly intended.
- Do not rewrite legacy/archive files just to make them consistent.
- Record generated optimization reports under `runs/` only when useful.
- Keep market research timestamped and distinguish observed market patterns from candidate facts.
- Keep `AGENTS.md` orchestration-focused. Put detailed domain knowledge in `profiles/` and `kb/`, and repeat only non-negotiable guardrails here.
