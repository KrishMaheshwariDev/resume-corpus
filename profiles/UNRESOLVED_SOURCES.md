# Unresolved Profile Sources and Verification Checklist

Last updated: 2026-07-05

This file tracks sources that were requested or useful for the master profile but could not be fully accessed or verified in the current environment.

## 1. Uploaded ZIP/archive

Status: Not accessible.

What happened:

- User asked to unzip and parse an archive.
- `/mnt/data` contained no uploaded file at the time of checking.
- Recent File Library search did not surface a resume archive.

Needed from user:

- Upload the ZIP/archive again in the chat, or
- provide the exact GitHub repository path, or
- create a repo manifest listing all resume corpus files.

Suggested manifest path:

```text
RESUME_FILES.md
```

Suggested manifest content:

```text
resume.tex
resume.pdf
temp/<exact-file-name>.tex
temp/<exact-file-name>.pdf
archive/<exact-file-name>.zip
```

## 2. GitHub directory listing limitation

Status: Partially blocked.

The available GitHub connector can fetch known file paths and search text. It does not currently expose a direct directory-tree listing action. Because of that, common known paths were checked manually, but unknown filenames under root or `temp/` could not be discovered exhaustively.

Checked and not found:

- `temp/resume.tex`
- `resume.pdf`
- `temp/resume.pdf`
- `Kunal_Maheshwari_Resume.tex`
- `Kunal_Maheshwari_Resume.pdf`
- `temp/main.tex`

Found and parsed:

- `resume.tex`

Needed from user:

- exact filenames, or
- a file manifest, or
- a repo tree/ZIP upload.

## 3. LinkedIn

Status: Not directly accessible.

URL:

```text
https://www.linkedin.com/in/kunalmaheshwari26/
```

Known from indirect evidence:

- Root resume links this URL.
- Portfolio links this URL.
- Personal/job-search context indicates the headline: `Java Developer | Spring Boot | REST APIs | SQL | Backend Engineering`.
- Portfolio README says a LinkedIn PDF export was one source used to curate content.

Needed from user:

- LinkedIn PDF export, or
- copied LinkedIn profile text, or
- screenshots of About, Experience, Education, Skills, Licenses & Certifications, Projects.

## 4. LeetCode

Status: Not directly accessible.

URL:

```text
https://leetcode.com/u/preferablehuman/
```

Needed from user:

- total solved,
- easy/medium/hard solved,
- contest rating,
- badges,
- current streak,
- preferred languages,
- screenshot or copied text.

## 5. Work authorization

Status: Conflicting/stale.

Prior context says:

- F-1 OPT-EAD was in hand.
- OPT-EAD valid through January 31, but the year is not confirmed in the current profile evidence.
- U.S. full-time work eligibility was used in earlier application contexts.

Needed from user:

- current authorization status,
- expiry year,
- whether U.S. resumes should mention it,
- whether sponsorship is required.

## 6. Current location and contact details

Status: Conflicting by market/context.

Current root resume says:

- Haldwani, Uttarakhand, India
- 9258446350
- `work.kunal.maheshwari@gmail.com`

Prior U.S. context says:

- Mount Pleasant, MI, USA
- `+1 (989) 906-2108`
- `kunal.maheshwari.work@gmail.com`

Job-board context also suggests:

- New Delhi, India

Needed from user:

- which location/contact set to use for India resumes,
- which location/contact set to use for U.S. resumes,
- whether portfolio URL should appear, given prior Gmail flagging concern.

## 7. Education conflicts

Status: Needs confirmation.

Conflicts:

- CMU GPA: 3.87 vs 3.76
- CMU date/status: Dec 2025 vs May 2026 vs completed
- LPU degree: `B.Tech CSE` vs `B.Tech CSE with specialization in Data Science`

Needed from user:

- final GPA,
- official graduation/completion date,
- exact degree wording.

## 8. Professional title/date conflicts

Status: Needs confirmation.

NTT DATA:

- Current resume title: Software Developer
- Prior context: Software Development Analyst
- Current resume period: Aug 2022 - Aug 2024
- Prior context: Aug 2022 - Jul 2024

Capgemini:

- Current resume groups: Senior Analyst / Analyst, Jul 2020 - Aug 2022
- Prior context splits:
  - Analyst, Jul 2020 - Oct 2021
  - Senior Analyst, Oct 2021 - Aug 2022

Needed from user:

- exact HR/background-check title and dates,
- whether resume should group or split Capgemini roles.

## 9. Skill-depth conflicts

Status: Needs confirmation before strong resume claims.

Skills to label carefully:

- Kafka: small project/exposure unless confirmed otherwise.
- Kubernetes: listed in skills, but production experience not confirmed.
- Spring Boot: strong target skill and listed in summary/skills; current professional bullets emphasize Spring Framework/Spring MVC. Need confirm production Spring Boot depth.
- GCP Pub/Sub: prior context only; verify before listing.
- OpenAPI/Swagger: prior context only; verify before listing prominently.
- Redis/Celery: portfolio skill/context may mention; verify project evidence before using in resume.

## 10. Salary/job-board details

Status: Private planning data, not resume content.

Observed from job-search context:

- Current salary around INR 12.5 LPA
- Preferred salary around INR 15 LPA
- Current location New Delhi in Naukri context

Usage rule:

- Do not include salary data in resumes.
- Use only for job-search strategy if user explicitly asks.
