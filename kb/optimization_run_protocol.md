# Resume Optimization Run Protocol

Last updated: 2026-08-12  
Repository: `resume-corpus`

## Purpose

Mandatory protocol for every resume optimization run.

The workflow is evidence-first and optimizes for:
1. truthful role fit,
2. ATS/AI parse and retrieval,
3. recruiter/hiring-manager comprehension,
4. technical credibility,
5. readable 1–2 page output, with readability taking priority over compactness.

No resume source file should be edited before the required profile and knowledge-base files are loaded.

Each run is an isolated document optimization. Application outcomes, recruiter responses, outreach history, funnel metrics, and rejection stages are outside this protocol and must not influence resume scoring or edits.

## Agent routing

Start with root `AGENTS.md`.

For resume work, use:
- `.agents/skills/resume-optimizer/SKILL.md`

For current-market benchmark research only, use:
- `.agents/skills/market-benchmark-refresh/SKILL.md`

## Mandatory preflight reads

### Candidate baseline and evidence

1. `profiles/MASTER_PROFILE_V2.md`
2. `profiles/PROFILE_FACT_MATRIX_V2.yml`
3. `profiles/ARCHIVE_RESUME_CORPUS_AUDIT.md`
4. `profiles/WORK_EXPERIENCE_EVIDENCE_OVERLAY_2026-08-27.md`
5. `profiles/PROJECT_EVIDENCE_OVERLAY_2026-08-27.md`
6. `profiles/AI_ASSISTED_ENGINEERING_EVIDENCE_OVERLAY_2026-08-27.md`
7. `profiles/EVIDENCE_FACT_OVERLAY_2026-08-27.yml`
8. `profiles/UNRESOLVED_SOURCES.md`
9. `profiles/RESUME_POSITIONING_V1.yml`

Apply the active dated overlays after the V2 baseline. On conflicts involving implementation detail, architecture, ownership, skill depth, or metric confidence, prefer the overlays.

Do not silently resolve HR title/date/contact/final-GPA/work-authorization conflicts unless explicitly marked resolved.

### Optimization knowledge

10. `kb/resume_optimization_knowledge_base.md`
11. `kb/human_review/resume_perception_knowledge_base.md`
12. `kb/scoring/weights.yml`
13. `kb/scoring/human_review_weights.yml`
14. `kb/skills/java_backend_taxonomy.yml`
15. `kb/skills/ai_assisted_engineering.yml`
16. `kb/roles/java_backend_engineer.yml`
17. `kb/writing/bullet_semantics.yml`
18. `kb/writing/action_verbs_java_backend.yml`
19. `kb/resume_output_requirements.yml`

For a general India Java/backend run also load:
20. `kb/market/india_java_backend.yml`

For the research rationale, consult `kb/research/resume_research_2026.md` when needed; it is not required on every edit.

If a JD-specific role profile exists later, load it after the baseline role profile.

## Source precedence

Unless the active user explicitly chooses a different source of truth:

1. explicit user confirmation in the active conversation;
2. 2026-08-11 evidence overlays;
3. current repo resume source;
4. V2 profile/fact matrix;
5. archive audit and exported source documents;
6. current project repositories;
7. older resume variants.

Repository code may outrank older project-resume wording when code reveals a more precise implementation boundary.

## Supported run types

### General optimization
No JD required.

Use:
- `profiles/RESUME_POSITIONING_V1.yml`
- `kb/roles/java_backend_engineer.yml`
- `kb/market/india_java_backend.yml`

Goal: broad Java/backend market relevance without becoming generic.

### JD-specific tailoring
JD required.

Focus:
- hard requirement gate;
- exact/alias/semantic match;
- responsibility alignment;
- seniority;
- evidence depth;
- truthful gap reporting.

### One-page compression
Use only when the content fits naturally. Compress without sacrificing material evidence, whitespace, scanability, or readability.

### Two-page expansion
Use only when page two adds material role-relevant evidence or architecture/seniority depth.

### Human-review pass
Focus on first-pass clarity, top-half strength, evidence density, skimmability, credibility, and memorability.

### ATS/AI pass
Focus on parse safety, relevant terminology, role/requirement coverage, semantic evidence, and keyword saturation risk.

### Build/validation
Compile and verify output after source changes.

## Phase 1: Intake

Resolve:
- source resume;
- run type;
- target role;
- JD if available;
- target market/location;
- output path;
- page preference if explicitly requested;
- whether canonical or tailored resume should change.

Do not overwrite the canonical root resume for a one-off JD unless the user explicitly asks.

For every optimization run that creates or edits a tailored variant, first run `scripts/archive-tailored-resumes.ps1`. The archive preflight must move all root-level tailored variant directories dated before the current local date into `resumes/tailored/old/DD-MM.YYYY/`, preserving each complete variant folder. Current-day variants remain at the tailored root. Never overwrite an existing destination or guess the date of an undated directory.

## Phase 2: Baseline review

Evaluate:
- structure/parse safety;
- page count;
- summary/role identity;
- skills coverage;
- top-half signal;
- experience evidence;
- projects;
- readability;
- source-dependent or ambiguous claims.

Capture baseline scores when practical.

## Phase 3: Evidence reconciliation

Before scoring or rewriting:
- map material claims to evidence;
- apply ownership qualifiers;
- distinguish P1 professional, P2 project, P3 academic/training, P4 knowledge/exposure, P5 unresolved;
- prefer direct measurements over broad historical percentages when they conflict;
- preserve unresolved HR/contact/date conflicts.

Build a cross-section evidence map for the actual resume content:

`Summary/Skills claim -> visible Work Experience or Project proof -> P1/P2/P3/P4 depth`

Every material Summary claim and prominent technology/skill family must have visible contextual proof in Work Experience or Projects. Clear semantic aliases are acceptable; loose thematic similarity is not. Professional claims should map to professional bullets, while project-backed claims must remain mapped to and qualified by Projects. A relevant P4 item may remain only when explicitly labeled as knowledge, exposure, training, or certification. The fact being present elsewhere in the corpus does not satisfy this resume-level alignment check.

Current examples:
- Project metrics require a direct implementation source or explicit user confirmation.
- In-development projects must distinguish current code from planned scope.
- Project evidence must not be upgraded to employment, internship, or production ownership.
- Foundational skills must remain qualified when the evidence depth is limited.

## Phase 4: Requirement / market analysis

JD-specific:
- hard requirements;
- preferred requirements;
- responsibilities;
- title/seniority;
- domain;
- technology;
- architecture/operational expectations.

General:
- durable C++/software-engineering intern and fresher capability clusters;
- current India-market benchmark;
- candidate differentiators and gaps.

## Phase 5: Human-review analysis

Evaluate:
- role clarity;
- top-quarter signal;
- evidence density;
- strongest first bullet;
- skimmability;
- credibility/restraint;
- sentence variety;
- section ordering;
- space cost of each line.

## Phase 6: Truthfulness gate

Reject/downgrade any suggestion that introduces:
- invented technology;
- inflated years;
- unsupported metric;
- exaggerated leadership;
- fake production exposure;
- project-only skill as employment experience;
- ownership of systems managed by another team;
- guessed implementation detail;
- unsupported reliability/distributed-system guarantee.

## Phase 7: Edit strategy

Rank edits by:

`role relevance + retrieval value + evidence strength + human signal + differentiation - space cost - redundancy - credibility risk`

Prioritize:
1. verified high-value evidence;
2. strong ownership stories;
3. role clarity;
4. truthful exact target terms;
5. context/impact improvement;
6. top-half scan value;
7. removal of filler/repetition;
8. parse safety;
9. readable page fit.

## Phase 8: Source edit

Bullet rules:
- one dominant idea;
- 3–5 useful evidence dimensions when appropriate;
- varied action/impact/scale/architecture/modernization structures;
- no forced metric;
- no generic promotional adjectives.

Emphasis rules:
- use restrained bolding for important technologies, verified metrics, ownership signals, and outcomes;
- bold short phrases, not complete bullets;
- avoid dense or repetitive emphasis that harms parsing or visual rhythm.

Pagination and spacing rules:
- allow content to flow naturally across pages; never insert a forced break that creates a large avoidable blank area;
- prevent orphaned section headings by keeping each heading with several lines of following content;
- do not repeat the candidate identity header on later pages unless explicitly requested;
- maintain visible separation between section headings, employer/project titles, subtitles or metadata, and body text.

Skills:
- preserve truthful search coverage;
- targeted resumes may omit low-relevance skills;
- omission does not delete skills from factual corpus;
- label limited/project skills when unqualified presentation would mislead.
- remove, qualify, or contextually demonstrate material technologies that would otherwise be orphaned in the Skills section.

Projects:
- use to demonstrate modern capabilities or close truthful gaps;
- do not displace stronger professional evidence for ordinary backend roles.

## Phase 9: Build and validation

After source changes:
1. compile;
2. confirm PDF;
3. check 1–2 page policy;
4. extract PDF text;
5. verify headings/contact/content;
6. check body font/margins;
7. check keyword saturation/regression;
8. re-check evidence boundaries.
9. verify every material Summary and Technical Skills claim against visible Work Experience or Project evidence, and resolve all material orphans.

Preferred helpers:

```bash
python scripts/validate_resume.py --tex resume.tex --pdf Resume.pdf
python scripts/score_resume.py --resume resume.tex
```

Scripts are heuristic/local QA, not ATS replicas.

## Phase 10: Re-score and compare

Report separately:
- Parse Safety;
- Requirement/Market Coverage;
- Evidence Strength;
- Human Review;
- Composite Fit.

Default release targets when truthfully achievable:
- Truthfulness: PASS
- Parse Safety: >=95
- Human Review: >=82
- Composite Fit: >=80
- no hidden critical-requirement failure
- no keyword stuffing
- no unsupported ownership/metrics

If real gaps prevent >=80, report the maximum credible fit instead of fabricating.

## Phase 11: Output report

Every material run should report:

```text
Run type:
Source resume:
Target role/JD:
Market:
Files loaded:
Page count:
Parse Safety:
Requirement/Market Coverage:
Evidence Strength:
Human Review:
Composite Fit:
Hard requirements/gaps:
Top evidence retained/promoted:
Weak/missing areas:
Edits made:
Truthfulness risks:
Source-confidence/metric risks:
Ownership qualifiers:
Claims intentionally excluded:
Parse/readability risks:
Validation:
Files changed:
Commit SHA, if pushed:
```

## Terminal boundary

The optimization run ends after the validated resume and report are delivered. Do not perform contact research, outreach drafting, message queueing, application logging, or external sending from an optimization request. Those actions require a separate explicit user request and remain outside resume scoring.

## Consistency rule

If context is lost, reload `AGENTS.md`, this protocol, checklist, V2 baseline, August 11 overlays, unresolved sources, positioning, and relevant KB before making resume changes.

## Non-negotiable rule

Do not edit resume files directly from memory alone.
