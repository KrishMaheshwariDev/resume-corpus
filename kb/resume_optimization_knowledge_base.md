# Resume Optimization Knowledge Base

Last updated: 2026-07-05
Repository: `preferablehuman/resume-corpus`

## Purpose

This file is the durable working knowledge base for resume optimization. Future resume edits should begin by reading this file before modifying resume source files. The goal is not to chase a fake universal ATS percentage. The goal is to improve resume-job alignment through parse-safe formatting, truthful skill coverage, evidence-backed bullets, and hybrid lexical-semantic scoring.

## Core principle

There is no single universal applicant tracking system score. Employer hiring stacks vary by ATS vendor, recruiter configuration, job-specific filters, parsing quality, search queries, knockout questions, and human review. A useful optimizer should therefore produce an explainable scorecard instead of claiming to reproduce Workday, Greenhouse, Lever, iCIMS, Taleo, SmartRecruiters, Ashby, LinkedIn, Indeed, or any proprietary model exactly.

## How ATS and recruiting systems generally work

A typical hiring workflow is:

1. Candidate submits resume and application form.
2. Resume file is parsed into text and structured fields.
3. Contact details, skills, education, experience, dates, titles, employers, and certifications are extracted.
4. Knockout questions and structured form fields are evaluated.
5. Candidate profile is stored in a searchable database.
6. Recruiters search, filter, shortlist, rank, tag, or manually review candidates.
7. Interview scorecards, notes, communication history, and pipeline stages are managed inside the ATS or connected tools.

Important implication: resume appearance is secondary to extraction quality. A visually strong PDF can fail if the text extraction order is broken or if headings, tables, columns, icons, or text boxes cause parser loss.

## Matching layers

Use these layers when scoring a resume against a job description.

### 1. Hard requirement gate

These are pass/fail or near-pass/fail criteria. They should be reported separately from similarity scoring.

Examples:

- work authorization,
- location,
- relocation requirement,
- hybrid/on-site availability,
- minimum years of experience,
- degree requirement,
- required certification,
- required technology experience,
- domain requirement,
- application form knockout questions.

A resume can score highly on keywords and still fail because a hard requirement is missing.

### 2. Exact keyword and phrase coverage

Exact terms still matter because many recruiter searches and older ATS workflows use Boolean or keyword search. Exact JD terms should be included when truthful.

Examples for Java backend roles:

- Java,
- Java 8,
- Java 11,
- Spring Boot,
- REST API,
- microservices,
- SQL,
- JPA,
- Hibernate,
- AWS,
- Azure,
- CI/CD,
- Jenkins,
- Maven,
- Docker,
- Kafka,
- JMS.

Rule: high-value terms should appear at least once exactly as written in the JD when they are truthful.

### 3. Weighted lexical relevance

Use TF-IDF and BM25-style scoring for lexical relevance. BM25 is preferable to simple keyword counting because it accounts for term frequency saturation and document length normalization. Repeating a term excessively should not produce unlimited gains.

Implementation guidance:

- score JD requirements against resume bullets,
- score required skills separately from preferred skills,
- discount repeated terms with no evidence,
- prioritize exact phrase matches over isolated token matches,
- avoid rewarding keyword stuffing.

### 4. Taxonomy and alias normalization

Normalize aliases and variants before scoring.

Examples:

- `SpringBoot` -> `Spring Boot`,
- `RESTful services` -> `REST API`,
- `CI CD` -> `CI/CD`,
- `Amazon Web Services` -> `AWS`,
- `Java Enterprise Edition` -> `J2EE` / `Java EE`,
- `object oriented programming` -> `OOP`,
- `message queue` -> `messaging`,
- `WebSphere JMS` -> `JMS`.

Use canonical skills, aliases, related skills, and evidence patterns instead of flat keyword lists.

### 5. Semantic responsibility alignment

Use embeddings or transformer-based sentence similarity to compare JD responsibility statements to resume bullets. Whole-document similarity is insufficient because it hides missing requirements. The optimizer should map each important JD requirement to the best matching resume evidence.

Example mapping:

JD: "Design and implement secure, maintainable Spring Boot microservices."
Resume bullet: "Developed Java 8/Spring Boot REST APIs for healthcare payer integrations, supporting certificate-based authentication and 50K daily requests."

This should score higher than a resume that only lists "Spring Boot" in the skills section.

### 6. Evidence strength grading

A skill is stronger when it is attached to real work, project context, metrics, ownership, or production constraints.

Evidence levels:

- Level 0: missing.
- Level 1: keyword appears only in skills list.
- Level 2: keyword appears in a generic bullet.
- Level 3: keyword appears with project or responsibility context.
- Level 4: keyword appears with production, scale, metric, reliability, security, or business impact.

Example:

- Weak: "Skills: Kafka."
- Moderate: "Built Kafka-based event processing pipeline."
- Strong: "Implemented Kafka-based asynchronous processing for order events, reducing downstream latency by 35% and improving retry reliability."

### 7. Human review readiness

ATS optimization alone is insufficient. A resume must also satisfy recruiter and hiring-manager review.

Strong bullets should include:

- action verb,
- technology or method,
- business or system context,
- measurable impact where truthful,
- ownership signal,
- production or scale signal when available.

Preferred bullet pattern:

`Action + technology/method + system/domain context + measurable result`

Example:

"Developed Java 8/Spring Boot REST APIs for healthcare payer integrations, supporting 50K daily requests and 99.99% SLA availability."

## Recommended local scoring model

Use a scorecard instead of one opaque ATS score.

Suggested default weights:

- required skill coverage: 25%,
- preferred skill coverage: 15%,
- role title and seniority match: 15%,
- responsibility semantic match: 15%,
- domain and project match: 10%,
- experience depth match: 10%,
- education and certification match: 5%,
- parse quality and format safety: 5%.

Final report should include:

1. hard requirement status,
2. required skills: matched / weak / missing / synonym-matched,
3. preferred skills: matched / missing / optional,
4. semantic alignment table,
5. evidence strength by skill,
6. parse and formatting risk,
7. bullet-level edits.

## Parse quality rules

Prefer:

- single-column layout,
- standard headings,
- text-based PDF generated from source,
- no icons for contact info,
- no tables for core experience content,
- no images of text,
- no text boxes,
- consistent date format,
- standard section order.

Standard section headers:

- Summary,
- Skills,
- Experience,
- Projects,
- Education,
- Certifications.

Risky patterns:

- multi-column layouts,
- decorative section labels,
- excessive icons,
- charts,
- skill bars,
- tables,
- hidden text,
- white-font keyword stuffing,
- headers/footers containing important content,
- PDF generated from screenshots.

Validation step:

1. Generate final PDF.
2. Extract text from PDF.
3. Verify contact info, section headings, employers, titles, dates, skills, and bullets are readable in correct order.
4. Compare extracted text against source text.
5. Flag missing or reordered content.

## Technical architecture for local optimizer

Recommended pipeline:

1. Ingest resume and job description.
2. Extract text from source files.
3. Normalize text and aliases.
4. Split resume into sections and bullets.
5. Split JD into required skills, preferred skills, responsibilities, qualifications, and domain signals.
6. Apply hard requirement checks.
7. Run exact keyword and phrase matching.
8. Run TF-IDF and BM25 lexical scoring.
9. Run semantic similarity from JD chunks to resume bullets.
10. Apply evidence grading rules.
11. Generate scorecard and missing/weak/matched reports.
12. Suggest bullet-level edits.
13. Preserve truthfulness and avoid invented experience.
14. Regenerate resume source.
15. Validate final PDF extraction.

Recommended local libraries and tools:

- Apache Tika: broad document text extraction.
- PyMuPDF or pdfplumber: PDF fallback extraction.
- python-docx: DOCX extraction.
- pylatexenc or custom parser: LaTeX source handling.
- regex: deterministic normalization and pattern checks.
- spaCy: tokenization, phrase matching, entity ruler, custom NLP pipeline.
- scikit-learn: TF-IDF and cosine similarity.
- rank-bm25 or BM25S: local BM25 scoring.
- sentence-transformers: local dense embeddings.
- cross-encoder reranker: optional second-stage semantic reranking.
- SQLite or YAML/JSON: lightweight knowledge base storage.
- PostgreSQL: later option if KB grows.

## Knowledge base schema

Canonical skill object:

```yaml
canonical_skill: Spring Boot
category: backend_framework
aliases:
  - SpringBoot
  - Spring Framework Boot
  - Spring
related_skills:
  - Java
  - REST API
  - Microservices
  - JPA
  - Hibernate
strong_context_terms:
  - developed
  - implemented
  - secured
  - deployed
  - optimized
weak_context_terms:
  - familiar
  - exposure
  - basic knowledge
evidence_patterns:
  - Spring Boot REST API
  - Spring Boot microservice
  - Spring Boot application deployed
seniority_weight: 0.9
ats_exact_match_priority: true
```

## Java backend optimization priorities

For Java backend roles, optimize around these clusters:

### Core Java

Java 8, Java 11, OOP, Collections, Streams, Lambdas, Exception Handling, Concurrency, Multithreading, JVM, Memory Management.

### Spring and backend APIs

Spring Boot, Spring MVC, Spring Security, Spring Data JPA, REST API, Dependency Injection, Bean, Configuration, Transaction Management, OpenAPI/Swagger.

### Microservices and distributed systems

Microservices, service boundaries, API Gateway, inter-service communication, resilience, distributed tracing, circuit breaker, service discovery, data consistency.

### Database and persistence

SQL, Oracle, PostgreSQL, DB2, JDBC, JPA, Hibernate, query optimization, indexes, transactions.

### Cloud and integration

AWS EC2, S3, RDS, Lambda, ECS, Azure Functions, Azure Service Bus, Azure Relay, Azure DevOps.

### Messaging and async processing

JMS, IBM WebSphere JMS, Azure Service Bus, Kafka, queues, topics, event-driven architecture, retry, dead-letter queue.

### DevOps and release engineering

Jenkins, Maven, Git, SVN, Docker, Kubernetes, CI/CD, IBM UrbanCode Deploy, Azure DevOps pipelines.

### Testing and quality

JUnit, Mockito, unit testing, integration testing, code coverage, TDD, static analysis, quality gates.

### Enterprise and healthcare domain

SOAP, REST, SOA, CAQH, FHIR, API Gateway, certificate authentication, SLA, production support, payer integrations.

## Truthfulness rule

Do not invent technologies, metrics, domains, ownership, scale, certifications, or production exposure. The optimizer may improve wording, consolidate keywords, and surface existing evidence, but it must not manufacture experience.

Use these labels for weak or uncertain items:

- production experience,
- project experience,
- academic experience,
- local project experience,
- exposure,
- familiar with,
- currently learning.

## Resume edit strategy

When tailoring a resume to a JD:

1. Extract must-have skills from JD.
2. Confirm which must-have skills are truthfully supported by the profile.
3. Place exact must-have terms in Skills section.
4. Add or adjust evidence bullets where truthful.
5. Prefer bullets that combine technology + responsibility + impact.
6. Remove weak filler if space is constrained.
7. Preserve high-signal metrics.
8. Validate one-page or two-page target after edit.
9. Validate PDF text extraction.
10. Produce a change summary.

## Anti-patterns

Avoid:

- keyword stuffing,
- hidden keywords,
- fake experience,
- inflated years of experience,
- vague bullets,
- bullets with tools but no outcome,
- unsupported cloud/Kubernetes/Kafka claims,
- removing strong metrics to add weak keywords,
- overfitting to one JD while damaging general backend positioning.

## Output format for future optimization runs

Every JD-resume analysis should produce:

```text
Overall fit: High / Medium / Low
Hard requirements: PASS / WEAK / FAIL
Required skill coverage: X/Y
Preferred skill coverage: X/Y
Top matched evidence:
  - ...
Missing or weak areas:
  - ...
Recommended edits:
  - section/path/bullet-level suggestion
Risks:
  - parse, truthfulness, seniority, location, authorization, etc.
```

## Initial implementation priority

Build deterministic scoring first, then add LLM-based rewrite assistance.

Order:

1. YAML taxonomy and aliases.
2. Resume/JD parser.
3. Keyword and phrase matching.
4. Hard requirement extractor.
5. Evidence grader.
6. BM25 and TF-IDF scoring.
7. Semantic bullet-to-JD mapping.
8. Report generator.
9. LaTeX patch generator.
10. PDF extraction validation.

This keeps the system explainable and prevents the LLM from becoming an unreliable black-box scorer.
