# Resume Corpus Agent Contract — Krish Maheshwari

## Mission

This repository is Krish Maheshwari's evidence-driven resume optimization system for C++ and software-engineering intern/fresher applications.

Optimize resumes for:
1. truthful role fit,
2. reliable ATS/AI parsing and retrieval,
3. fast recruiter comprehension,
4. deeper hiring-manager credibility,
5. moderate, readable information density.

Do not optimize for a fictional universal ATS score. Use the repository's explainable scorecards and evidence rules.

Treat every optimization as an isolated document evaluation. Do not use application outcomes, recruiter-response history, outreach activity, conversion metrics, or prior rejection stages to score, position, or rewrite a resume.

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
4. `profiles/AI_ASSISTED_ENGINEERING_EVIDENCE_OVERLAY_2026-08-15.md`;
5. `profiles/EVIDENCE_FACT_OVERLAY_2026-08-11.yml`;
6. current repo resume source;
7. `profiles/MASTER_PROFILE_V2.md` and `profiles/PROFILE_FACT_MATRIX_V2.yml`;
8. archive/export evidence and current project repositories;
9. older resume variants.

Never silently resolve HR title, employment-date, contact, final GPA, or work-authorization conflicts unless a higher-priority source explicitly resolves them.

## Mandatory preflight

For any resume edit, optimization, score, or tailored variant, load:

1. `kb/optimization_run_protocol.md`
2. `kb/optimization_run_checklist.yml`
3. `profiles/MASTER_PROFILE_V2.md`
4. `profiles/PROFILE_FACT_MATRIX_V2.yml`
5. `profiles/ARCHIVE_RESUME_CORPUS_AUDIT.md`
6. `profiles/WORK_EXPERIENCE_EVIDENCE_OVERLAY_2026-08-27.md`
7. `profiles/PROJECT_EVIDENCE_OVERLAY_2026-08-27.md`
8. `profiles/AI_ASSISTED_ENGINEERING_EVIDENCE_OVERLAY_2026-08-27.md`
9. `profiles/EVIDENCE_FACT_OVERLAY_2026-08-27.yml`
10. `profiles/UNRESOLVED_SOURCES.md`
11. `profiles/RESUME_POSITIONING_V1.yml`
12. `kb/resume_optimization_knowledge_base.md`
13. `kb/human_review/resume_perception_knowledge_base.md`
14. `kb/scoring/weights.yml`
15. `kb/scoring/human_review_weights.yml`
16. `kb/writing/bullet_semantics.yml`
17. `kb/writing/action_verbs_java_backend.yml`
18. `kb/resume_output_requirements.yml`

Do not edit from model memory alone.

## Default positioning

Primary role family:
- C++ Developer Intern
- Software Developer Intern
- Software Engineer Intern
- Backend Developer Intern
- Entry-level software-engineering roles consistent with a 2027 graduation.

Primary differentiators:
- modern C++20, CMake, graphics, and performance-oriented projects;
- bitboard data representation and rendering architecture;
- project-backed file tooling, document retrieval, SQL, Python, and React breadth;
- demonstrated debugging, DSA, OOP, and systems fundamentals.

Do not present project work as professional employment, internship, production ownership, or team leadership. Keep OpenChess and Get-My-Doc visibly marked in development.

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

Resume work is self-contained. An optimization request never authorizes or triggers contact research, outreach drafting, message queueing, application tracking, or external sending. Finish after the validated resume and optimization report unless the user makes a separate explicit request for another workflow.

For current-market research or benchmark refresh, use `.agents/skills/market-benchmark-refresh/SKILL.md`. Do not browse the market on every normal edit.

## Page-length policy

Default to the most readable version that preserves material evidence. Compactness is secondary to comprehension.

- Allowed: 1–2 pages.
- One page is acceptable when the candidate's strongest relevant evidence fits naturally without crowding.
- Two pages are allowed when page two adds material role-relevant evidence, architecture depth, or projects required for the target.
- Page two must earn its existence.
- Never add filler to reach two pages.
- Never remove material evidence merely to satisfy one page.
- Prefer readable spacing, line length, and visual separation over forcing a one-page result.
- Never reduce normal resume body text below 11 pt. This is a hard readability floor for canonical, general, and tailored resumes, including when the user requests a denser format; reduce or reprioritize content instead. Do not reduce margins below 0.5 in merely to fit content.
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

## Cross-section evidence alignment

The Summary and Technical Skills sections are promises that the Work Experience and Projects sections must substantiate.

- Every material capability, work-area, domain, delivery-scope, engineering-approach, or working-style claim in the Summary must map to at least one visible Work Experience or Project bullet.
- Every prominently listed technology or skill family must appear in a contextual Work Experience or Project bullet. Exact repetition is not required when an unambiguous alias or parent/child technology mapping carries the same meaning.
- A P4 knowledge, exposure, or certification item may remain without a delivery bullet only when it is clearly labeled as `knowledge`, `exposure`, `training`, or `certification`, is relevant to the target, and is not presented as hands-on delivery.
- Do not use the Skills section as an inventory dump. If a term has no visible evidence and is not a necessary qualified P4 item, omit it from that resume while preserving it in the factual corpus.
- Project-backed technologies must map to Projects and must not be made to look employment-backed. Professional capabilities should normally map to Work Experience.
- Validate alignment in both directions before release: top-of-resume claims must have downstream proof, and the strongest downstream proof should be represented appropriately in the Summary or Skills when relevant to the target.
- A resume with material orphaned summary claims or orphaned unqualified technologies fails the optimization release gate even when the underlying fact exists elsewhere in the corpus.

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
- Krish has no verified employment or internship experience.
- All project claims are P2 and must remain visibly project-backed.
- OpenChess and Get-My-Doc are in development; do not describe planned features as delivered.
- C and Java are foundational/basic.
- Use supplied benchmark figures only with project context and only while the implementation supports them.
- LogWhisperer may be described as project-based LLM-assisted incident reporting, not professional AI delivery.

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

For general intern/fresher resumes, default order:
1. Name/contact
2. Technical Skills
3. Projects
4. Education
5. Activities

For a JD-specific resume, reorder lower sections only when it materially improves relevance.

The first screen/top quarter should establish C++/software-engineering identity, intern/fresher career stage, and one or more concrete project proof points.

The first bullet under each project must be the strongest role-relevant evidence.

Use restrained bold emphasis to improve scanning. Bold section labels and a small number of high-value technologies, verified metrics, ownership signals, or outcomes. Do not bold entire bullets, create dense patches of bold text, or use bolding as keyword stuffing.

Formatting continuity rules:
- Never force a page break that leaves a large avoidable blank region on the preceding page.
- Do not repeat the candidate name, role, or contact header on page two unless the user explicitly requests a running header.
- Keep each section heading with enough following content to prevent an orphaned heading at the bottom of a page.
- Preserve visible spacing between section headings, employer/project titles, subtitles or metadata, and the text or bullets that follow.

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
- use `profiles/RESUME_POSITIONING_V1.yml`;
- optimize for C++/software-engineering internships and fresher roles in India;
- favor durable project evidence over broad unsupported tool lists.

## JD-specific variants

When given a JD:
1. before creating or editing a variant, run `scripts/archive-tailored-resumes.ps1` so every dated variant older than the current local date is moved from the root of `resumes/tailored/` into `resumes/tailored/old/DD-MM.YYYY/`, preserving the complete variant folder;
2. parse mandatory, preferred, responsibility, seniority, domain, and technology requirements;
3. map each important requirement to evidence;
4. mark exact/alias/semantic/weak/missing;
5. identify hard gaps before writing;
6. tailor wording and section emphasis without fabricating;
7. save a variant under `resumes/tailored/<company-role-YYYY-MM-DD>/` unless the user explicitly wants to replace `resume.tex`;
8. preserve the canonical general resume.

Tailored archive rules:
- Only current-day variant folders remain directly under `resumes/tailored/`.
- Archive folders use the exact date structure `resumes/tailored/old/DD-MM.YYYY/`.
- Move each complete variant directory as-is; do not flatten, rename, or split its contents.
- Determine archive date from the terminal `YYYY-MM-DD` suffix in the variant directory name.
- Skip `old/` and any undated directory; report undated directories for manual review rather than guessing.
- Archiving must be idempotent and must never overwrite an existing destination. Stop and report a collision.
- Run the archive step once at the beginning of every future resume optimization request, before creating the new current-day variant.

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
- build a Summary/Skills-to-Evidence map and resolve material orphaned claims or technologies;
- use `evals/resume_optimizer_cases.yml` as behavioral regression guidance.
- verify that the run created no application/outreach records and initiated no external contact.

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
