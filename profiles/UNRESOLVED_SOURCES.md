# Unresolved Profile Sources and Verification Checklist

Last updated: 2026-08-11

This file tracks profile sources and facts that remain unresolved after parsing the repo, uploaded ZIP archive, LinkedIn PDF export, academic history, degree plan, portfolio, GitHub-accessible repositories, and detailed interview-preparation reconstruction of professional work.

The 2026-08-11 overlays add high-confidence architecture/ownership detail but intentionally do not resolve HR/contact/date conflicts unless explicitly confirmed.

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

Status: Mostly superseded by uploaded ZIP and connector directory fetches, but still relevant for future repo-only runs.

If future resume files are added under unknown filenames, maintain a manifest or inspect repository contents before assuming a source does not exist.

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

Accessible search did not return usable profile stats. Needed from user only if LeetCode metrics become relevant:

- total solved,
- easy/medium/hard solved,
- contest rating,
- badges,
- current streak,
- preferred languages,
- screenshot or copied text.

## 5. Work authorization

Status: Needs confirmation for U.S.-market resumes.

Evidence:

- Multiple U.S.-market resume variants mention OPT-EAD and full-time work authorization.
- Prior context also says OPT-EAD was in hand.

Still needed from user:

- current authorization status,
- expiry year,
- whether U.S. resumes should mention it,
- whether sponsorship is required.

## 6. Current location and contact details

Status: Needs confirmation before final resume use when the latest resume block is not explicitly selected.

Conflict summary:

- Current root resume uses India-market contact/location details.
- Archive U.S. resumes use Mount Pleasant, MI positioning.
- Archive India-tailored resumes and current root resume do not fully agree on the India phone/contact set.
- Job-board context also includes New Delhi and multiple India target locations.

Needed from user when not already clear from the chosen resume source:

- preferred India resume location,
- preferred U.S. resume location, if applicable,
- preferred email for resumes,
- correct phone for India resumes,
- correct phone for U.S. resumes, if applicable,
- whether the portfolio URL should be included given prior Gmail flagging concerns.

## 7. Education conflicts

Status: Needs confirmation before background-check-sensitive output if the latest resume is not explicitly authoritative.

Conflicts:

- CMU GPA: 3.76 from academic history and older resumes, 3.85 from `Resume.docx`, 3.87 from current root resume and later resume variants.
- CMU completion/date: Dec 2025 vs May 2026 vs completed.
- LPU degree wording: B.Tech CSE vs B.Tech CSE with specialization in Data Science.

Needed from user:

- final GPA,
- official graduation/completion date,
- exact degree wording.

## 8. Professional title/date conflicts

Status: Still unresolved for HR/background-check precision.

NTT DATA:

- Current/root/later resume title: Software Developer.
- LinkedIn/older resume title and prior interview context: Software Development Analyst.
- Date variants: Aug 2022 - Jul 2024 vs Aug 2022 - Aug 2024.
- Detailed 2026 interview-prep reconstruction strongly enriched the work content but did **not** explicitly settle the HR title/date conflict.

Capgemini:

- Some resumes group Senior Analyst / Analyst.
- LinkedIn and older resumes split Senior Analyst, Analyst, and Trainee.
- Detailed interview-prep reconstruction confirms the Mercedes/Daimler Vans work and mentoring details but does not settle whether final resume display should group or split titles.

Needed from user for background-check-sensitive resumes:

- exact HR title and dates,
- whether resume should group or split Capgemini roles.

## 9. Skill-depth conflicts

Status: Partially clarified by 2026-08-11 evidence overlays.

### Spring Boot / Spring

Clarified:

- NTT detailed work reconstruction confirms Spring Framework in later JAX-WS services.
- Capgemini Mercedes production application is confirmed as Java EE/J2EE, EJB, JSF, Hibernate, WebLogic, and DB2.
- Capgemini training confirms Spring Framework/Spring MVC + Angular + PostgreSQL.

Still unresolved:

- Which exact NTT production service(s), if any, should be used as primary evidence for a strong `Spring Boot` production claim.

Rule:

- Do not automatically claim professional Spring Boot at both NTT and Capgemini solely from older resume variants.
- Spring Boot may remain in Skills where supported by other current resume/project evidence, but project/employment bullets should map it to a specific truthfully supported context.

### Kafka

Clarified:

- Small project/hands-on project experience is supported by prior context.
- Production Kafka ownership is not confirmed.

Rule: use `project experience` / skills-list wording, not production Kafka leadership.

### Kubernetes

Clarified:

- Knowledge/hands-on learning/project exposure is supported by prior context.
- Production Kubernetes ownership is not confirmed.

Rule: do not claim production Kubernetes deployment ownership without another source.

### PL/SQL

Clarified:

- At NTT, Java services consumed Oracle views and PL/SQL procedures through OJDBC.
- Separate DB team generally owned PL/SQL implementation.

Rule: position as Oracle/PLSQL integration and database coordination unless direct procedure-authoring evidence is separately available.

### Other skills still needing depth verification before prominent use

- Scala.
- GCP Pub/Sub.
- OpenAPI/Swagger.
- Redis.
- Celery.

## 10. Metric confidence checks

Status: Updated after detailed work reconstruction.

### High-confidence / reconstructed

- NTT: `50K+ daily API requests` — safe conservative aggregate; detailed discussion suggests roughly 55–65K+ across CAQH v2/v4 and other services.
- NTT: `99.99% SLA uptime/availability` — formal SLA context confirmed.
- Capgemini VIN feature: approximately `60+ seconds -> 10–20 seconds` after HQL/DB2 optimization; implies roughly 67–83% reduction for a 60-second baseline.
- AWS taxi project: `8GB+ dataset` remains supported by project/resume evidence.

### Source-dependent / verify before prominent use

- NTT: `20% issue-resolution time reduction` — older resume evidence exists, but detailed Log4j2 reconstruction did not establish the measurement basis. Prefer qualitative debugging/traceability improvement unless intentionally retaining the sourced metric.
- NTT: `50% faster delivery cycles / EDX delivery improvement` — older resume evidence exists; user contribution to Edifecs/upgrade analysis is supported, but exact metric attribution needs confirmation.
- Capgemini: `99%+ uptime` — present in older/current resume evidence but not independently reconstructed during interview prep.
- Capgemini: `10% query performance improvement` — source exists in older variants; exact feature/context not reconstructed.
- AWS Spark: `40% runtime/processing improvement` — repository does not establish the comparison baseline. Verify before prominent use.

### Downgraded / do not automatically use

- Capgemini: blanket `90% performance improvement` should not automatically be attached to the VIN feature. Direct reconstructed timings support ~67–83% for that specific feature.
- Capgemini: `99% code coverage` remains unverified.
- Lamprey: `99.9% uptime` remains unverified.
- Lamprey: `10GB video data daily` remains unverified.
- `30-member Agile training program` remains source-dependent unless retained from an explicit training source.

## 11. NTT production incident unknowns

Status: Important claim-boundary checklist.

Confirmed incident pattern is documented in `WORK_EXPERIENCE_EVIDENCE_OVERLAY_2026-08-11.md`.

Still unknown and must not be guessed:

- exact REST client library used for Tufts integration,
- exact leaked class/client API,
- exact JVM argument used for the temporary Jackson-buffer mitigation,
- whether formal memory-watch/load testing was added afterward,
- exact CVE associated with the Log4j migration,
- final production outcome of the FHIR proof of concept.

Ownership rule:

- User supported root-cause investigation and remediation strategy for the memory incident but was not the primary final-fix implementer.
- Do not write `fixed the memory leak` as a sole-ownership claim.

## 12. Capgemini / Mercedes implementation unknowns

Status: Important claim-boundary checklist.

Confirmed architecture and feature details are documented in `WORK_EXPERIENCE_EVIDENCE_OVERLAY_2026-08-11.md`.

Still unknown and must not be guessed:

- exact JSF component framework,
- exact EAR module structure,
- exact JTA/EJB transaction configuration,
- exact Python callback async implementation detail,
- exact downstream Mercedes central-ordering protocol,
- exact table names/status codes,
- exact nightly invalid-configuration remediation action,
- exact number of junior developers mentored.

Model terminology conflict:

- Older resume variants say `Python decision tree`.
- Current recollection says `hierarchical model`.
- Safest resume wording is `Python prediction service/model` until model type is reconfirmed.

## 13. AWS Spark implementation boundaries

Status: Clarified from repository code.

Confirmed:

- S3 -> Lambda -> EFS -> Spark Structured Streaming -> PostgreSQL/RDS.
- Atomic `.part -> .csv` staging.
- EFS checkpointing.
- Terraform-based infrastructure.

Important boundaries:

- Current Spark code uses `master("local")`; do not describe current implementation as a multi-node distributed Spark cluster.
- Checkpointing does not prove end-to-end exactly-once JDBC persistence; append-mode `foreachBatch` can require an idempotent sink strategy.
- Database credentials are not currently evidenced as Secrets Manager-backed.
- 40% runtime metric baseline remains unresolved.

## 14. Salary/job-board details

Status: Private planning data, not resume content.

Usage rule:

- Do not include salary data in resumes.
- Use only for job-search strategy if the user explicitly asks.

## 15. Overlay files added 2026-08-11

Future resume runs must read these after the V2 baseline profile:

- `profiles/WORK_EXPERIENCE_EVIDENCE_OVERLAY_2026-08-11.md`
- `profiles/PROJECT_EVIDENCE_OVERLAY_2026-08-11.md`
- `profiles/EVIDENCE_FACT_OVERLAY_2026-08-11.yml`

They are the preferred source for detailed architecture, ownership boundaries, skill-depth corrections, direct timing evidence, and project implementation limits.

## 16. AI product and AI-assisted engineering boundaries (2026-08-15)

Confirmed by the user and repository evidence:

- runtime-AI project work retained in the AI corpus covers AI Email Client, CodingHelper, and Article Voice Desk;
- Codex and GitHub Copilot AI-assisted-delivery attribution is limited to Resume Corpus and Portfolio, with human direction, review, tests, runtime checks, and acceptance;
- AWS Automated Spark Pipeline is a master's coursework project and is not AI-assisted-delivery evidence;
- Ollama, llama.cpp, and LM Studio were installed/configured and executed for local-inference comparison and integration evaluation;
- Ollama has direct application-integration evidence through CodingHelper.

Still unresolved or unsupported and therefore prohibited from promotion:

- exact llama.cpp/LM Studio model names, quantization formats, hardware, tokens/second, memory, quality, or latency comparisons;
- direct llama.cpp or LM Studio application integration beyond evaluation;
- production traffic, user counts, adoption, SLA, security certification, or commercial deployment for the personal AI projects;
- measured productivity improvement attributable to Codex or GitHub Copilot;
- employer authorization or production use of AI coding tools/local runtimes;
- autonomous agent acceptance, deployment, application submission, or final decision-making;
- formal correctness/security guarantees from CodingHelper's bounded tests;
- GitHub Models, Cursor, Claude Code, or Microsoft Copilot hands-on experience.

Rule: use the ownership formulation `directed, reviewed, tested, and validated AI-assisted delivery`; preserve P2/P3/P4 depth and never convert these claims to P1 without separate professional evidence.
