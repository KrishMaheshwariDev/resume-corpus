# Unresolved Profile Sources and Verification Checklist

Last updated: 2026-07-05

This file tracks profile sources and facts that remain unresolved after parsing the repo, uploaded ZIP archive, LinkedIn PDF export, academic history, degree plan, portfolio, and GitHub-accessible repositories.

## 1. Uploaded ZIP/archive

Status: Resolved.

What changed:

- `temp.zip` was located in the active runtime.
- The archive was unzipped and parsed.
- Total files found: 55.
- Profile/resume-relevant files parsed: 42.
- Parsed archive audit file: `profiles/ARCHIVE_RESUME_CORPUS_AUDIT.md`.
- Archive-refreshed master profile: `profiles/MASTER_PROFILE_V2.md`.
- Archive-refreshed fact matrix: `profiles/PROFILE_FACT_MATRIX_V2.yml`.

## 2. GitHub directory listing limitation

Status: Mostly superseded by uploaded ZIP, but still relevant for future repo-only runs.

The available GitHub connector can fetch known file paths and search text. It does not currently expose a direct directory-tree listing action. If future resume files are added to the repo under unknown filenames, provide exact paths or maintain a manifest.

Recommended manifest path:

```text
RESUME_FILES.md
```

## 3. LinkedIn

Status: Partially resolved.

Direct public LinkedIn access was not reliable, but `Profile_linkedin.pdf` from the uploaded archive was parsed.

Resolved from LinkedIn PDF export:

- Headline: `Java Developer | Spring Boot | REST APIs | SQL | Backend Engineering`.
- LinkedIn location signal: Mount Pleasant, Michigan, United States.
- Top skills shown: PEFT, Local LLMs, LoRA.
- Languages shown: Hindi (Native or Bilingual), English (Limited Working).
- Certifications shown: workshop on ethical hacking, Microsoft Certified: Azure Fundamentals, introduction to Linux, Agile Software Development.
- Experience timeline for NTT DATA and Capgemini.
- Education timeline for CMU, LPU, and St. Paul's Senior Secondary School.

Still needed from user if exact live LinkedIn is required:

- Updated LinkedIn PDF export, or copied profile text, if the live profile has changed after the archived export.

## 4. LeetCode

Status: Not resolved.

URL provided by user:

```text
https://leetcode.com/u/preferablehuman/
```

Accessible search did not return usable profile stats. Needed from user:

- total solved,
- easy/medium/hard solved,
- contest rating,
- badges,
- current streak,
- preferred languages,
- screenshot or copied text.

## 5. Work authorization

Status: Needs confirmation.

Evidence:

- Multiple U.S.-market resume variants mention OPT-EAD and full-time work authorization.
- Prior context also says OPT-EAD was in hand.

Still needed from user:

- current authorization status,
- expiry year,
- whether U.S. resumes should mention it,
- whether sponsorship is required.

## 6. Current location and contact details

Status: Needs confirmation before final resume use.

Conflict summary:

- Current root resume uses India-market contact/location details.
- Archive U.S. resumes use Mount Pleasant, MI positioning.
- Archive India-tailored resumes and current root resume do not fully agree on the India phone/contact set.
- Job-board context also includes New Delhi and multiple India target locations.

Needed from user:

- preferred India resume location,
- preferred U.S. resume location, if applicable,
- preferred email for resumes,
- correct phone for India resumes,
- correct phone for U.S. resumes, if applicable,
- whether the portfolio URL should be included given prior Gmail flagging concerns.

## 7. Education conflicts

Status: Needs confirmation.

Conflicts:

- CMU GPA: 3.76 from academic history and older resumes, 3.85 from `Resume.docx`, 3.87 from current root resume and later resume variants.
- CMU completion/date: Dec 2025 vs May 2026 vs completed.
- LPU degree wording: B.Tech CSE vs B.Tech CSE with specialization in Data Science.

Needed from user:

- final GPA,
- official graduation/completion date,
- exact degree wording.

## 8. Professional title/date conflicts

Status: Needs confirmation.

NTT DATA:

- Current/root/later resume title: Software Developer.
- LinkedIn/older resume title: Software Development Analyst.
- Date variants: Aug 2022 - Jul 2024 vs Aug 2022 - Aug 2024.

Capgemini:

- Some resumes group Senior Analyst / Analyst.
- LinkedIn and older resumes split Senior Analyst, Analyst, and Trainee.

Needed from user:

- exact HR/background-check title and dates,
- whether resume should group or split Capgemini roles.

## 9. Skill-depth conflicts

Status: Needs confirmation before strong claims.

Skills to label carefully:

- Kafka: appears in some targeted variants and prior context, but production depth is not confirmed.
- Kubernetes: appears in many variants, but production depth is not confirmed.
- Scala: appears in some tailored summaries but lacks independent evidence.
- Spring Boot: strong target skill and repeatedly listed; confirm whether production work used Spring Boot directly or broader Spring/Spring MVC/Spring Framework.
- GCP Pub/Sub: prior-context only; verify before listing prominently.
- OpenAPI/Swagger: prior-context only; verify before listing prominently.
- Redis/Celery: verify project evidence before using in a final resume.

## 10. Metric confidence checks

Status: Some require confirmation.

High-confidence/repeated:

- 50K+ daily API requests.
- 99.99% SLA uptime/availability.
- 20% issue-resolution time reduction.
- 50% faster delivery cycles / EDX delivery improvement.
- 90% performance improvement.
- 99%+ uptime.
- 8GB+ taxi dataset.
- 40% Spark/runtime improvement.

Needs verification before prominent use:

- 10% query performance improvement.
- 99% code coverage.
- Lamprey 99.9% uptime.
- Lamprey 10GB video data daily.
- 30-member Agile training program.

## 11. Salary/job-board details

Status: Private planning data, not resume content.

Usage rule:

- Do not include salary data in resumes.
- Use only for job-search strategy if the user explicitly asks.
