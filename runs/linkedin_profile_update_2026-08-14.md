# LinkedIn Full-Profile Update - 2026-08-14

## Recommended positioning

Target: Java Backend Engineer / Backend Software Engineer / Java Application Developer roles in India.

## Live profile audit

Read-only audit completed against the signed-in LinkedIn profile on 2026-08-14. No edit form was opened and nothing was saved.

- Current headline: `Java Developer | Spring Boot | REST APIs | SQL | Backend Engineering`
- Current location: `Haldwani, Uttarakhand, India`
- Current NTT entry: `Software Engineer`, Aug 2022 - Aug 2024
- Current About section still uses the older software-developer/data-engineer positioning and says the MS is in progress.
- Current visible top skills: SQL, Software Development Life Cycle (SDLC), Core Java, Spring Framework, Web Services API.
- Current skills inventory contains useful backend terms mixed with low-priority or noisy entries such as Quantitative Models, Customer Service, Modeling Languages, WAMP, Front-end Engineering, and Storage Optimization.
- Current Capgemini descriptions still contain the broad 90% performance claim and unverified 99% code-coverage claim.
- No populated LinkedIn Projects detail page was found; the strongest verified projects should be added.
- Current certifications include Azure Fundamentals plus expired Azure Developer Associate and Azure Data Engineer Associate credentials, along with several older Coursera/training credentials.
- Current Open to Work preference is India with on-site, hybrid, and remote options.

## Headline

Java Backend Engineer | Java 8/11, Spring, REST/SOAP APIs, SQL & Hibernate | Enterprise Integration, Performance & Production Reliability

## About

I am a Java backend engineer with 4.6+ years of experience building, integrating, modernizing, and supporting enterprise applications across healthcare payer and automotive domains.

At NTT DATA, I developed and maintained Java 8/11, JAX-WS/Spring, and REST/SOAP healthcare integration services supporting 50K+ daily requests under a 99.99% availability SLA. My work spanned hybrid integrations using Azure Relay, Azure Service Bus, Azure Functions, and JMS; Oracle/OJDBC processing; production troubleshooting; release validation; and observability. I also led the initial PoC and coordinated the rollout of a project-wide Log4j2 migration while preserving existing production logging contracts.

At Capgemini, I developed and supported Java EE, JSF, Hibernate/HQL, WebLogic, and DB2 applications for vehicle configuration and recommendation workflows. I reduced a VIN repeat-configuration API's response time from about 60+ seconds to 10-20 seconds by moving stable option-code transformations into set-based HQL/DB2 processing while retaining authoritative business validation in Java. I also integrated a Python prediction workflow with Java services and mentored junior developers through codebase walkthroughs, debugging, incremental changes, and reviews.

My project work extends into AWS, Terraform, Docker, Spark Structured Streaming, PostgreSQL, React, TypeScript, and applied NLP. I enjoy tracing behavior across application, database, messaging, and downstream boundaries, then turning that understanding into measurable performance, reliability, and maintainability improvements.

Core areas: Java 8/11, Spring Framework, Spring MVC, Java EE, REST/SOAP APIs, JAX-WS, Hibernate/HQL, SQL/JDBC, Oracle, DB2, WebSphere, WebLogic, Azure integration, Jenkins/Maven CI/CD, JUnit, Log4j2, production support, performance tuning, and root-cause analysis.

Portfolio: https://preferablehuman.github.io/portfolio/

## Experience

### NTT DATA

Recommended title: retain the live LinkedIn title `Software Engineer`; do not change the title during this update.

Recommended dates: retain the live LinkedIn dates `Aug 2022 - Aug 2024`; do not change the dates during this update.

Description:

- Developed and maintained Java 8/11, JAX-WS/Spring, and REST/SOAP healthcare payer integration services on IBM WebSphere, supporting 50K+ daily requests under a 99.99% availability SLA.
- Integrated hybrid service flows across Azure Relay, Azure Service Bus, Azure Functions, and JMS, plus synchronous downstream REST calls and Oracle/OJDBC processing with timeout and partial-failure handling.
- Integrated Java services with established Oracle views and PL/SQL procedures through OJDBC while applying member and provider business rules in the service layer.
- Led the initial PoC and coordinated the rollout of a project-wide Log4j2 migration, preserving production log formats, filenames, locations, and rolling policies while documenting a repeatable upgrade path.
- Integrated an AOP-based monitoring library that propagated correlation IDs and captured latency, success/failure, and request-volume telemetry across services.
- Supported Jenkins, Maven, and IBM UrbanCode release workflows; executed JUnit/SoapUI and post-deployment validation and contributed go/no-go or rollback recommendations.
- Supported root-cause analysis of a WebSphere memory/resource-retention incident through code-path review, mitigation planning, and rolling-restart validation while maintaining availability.

### Capgemini - Senior Analyst / Analyst

Recommended dates: retain LinkedIn's split roles unless an HR record supports regrouping.

Senior Analyst description:

- Developed and supported a Java EE/J2EE, JSF, Hibernate/HQL enterprise application on Oracle WebLogic and DB2 for Mercedes-Benz Vans configuration, recommendation, and ordering workflows.
- Integrated a Python vehicle-configuration prediction workflow with Java services and enforced deterministic option/package validation before recommendations were exposed to dealer users.
- Reduced VIN repeat-configuration API latency from about 60+ seconds to 10-20 seconds by moving stable option-code mappings into set-based HQL/DB2 CASE expressions while retaining business validation in Java.
- Diagnosed cross-system failures using Python-service output, Java validation logs, and DB2 reference data; verified behavior and timing with Postman and production logs.
- Supported Jenkins/GitLab CI/CD, Git-based code reviews, JUnit4 testing, release validation, and production debugging.
- Mentored junior developers through codebase walkthroughs, incremental defects and features, debugging support, and code reviews.

Analyst description:

- Developed and maintained Java enterprise application features and REST-based integrations for automotive configuration workflows.
- Investigated application and reference-data issues across Java logs, Python prediction output, and DB2, supporting reliable production behavior.
- Contributed to Agile delivery through feature development, defect resolution, JUnit4 testing, code reviews, technical documentation, and release support.

### Capgemini - Trainee

Recommended dates: retain `Jan 2020 - May 2020` until the May/Jun 2020 conflict is resolved.

Description:

- Built Java, Spring/Spring MVC, Angular, and PostgreSQL modules for fitness-club and digital-wallet applications during a structured Agile training program.
- Implemented authentication, email/OTP login, CRUD operations, account balances, transactions, profile management, and image-upload workflows.

## Projects to add

### AWS Automated Spark Pipeline / NYU Taxi Platform

- Built an event-driven AWS pipeline where S3 uploads trigger Lambda staging to EFS, a Docker-packaged Spark Structured Streaming workload processes micro-batches on ECS, and transformed data persists to RDS PostgreSQL through JDBC.
- Provisioned VPC, subnets, NAT, IAM, S3 notifications, Lambda, EFS, ECS, RDS, security groups, and CloudWatch resources with Terraform.
- Processed an 8GB+ taxi dataset and persisted EFS checkpoints for restart recovery.

Link: https://github.com/preferablehuman/AWS-automated-spark-pipeline

### Privacy-Preserving AI Email Client

- Built a graduate capstone for privacy-oriented email summarization and classification using FastAPI, PyTorch, Hugging Face Transformers, T5, PEFT/LoRA, Docker, MinIO, Prometheus, React, and TypeScript.
- Implemented summarization, categorization, per-user adapter lifecycle, and diagnostics workflows; evaluated the model at ROUGE-1 F 53.04, ROUGE-2 F 44.90, and ROUGE-L F 45.90.

### Interactive Portfolio System

- Built and deployed a recruiter-facing React, TypeScript, Vite, and Tailwind CSS SPA with project case studies, searchable skill evidence, persisted theming, deep-link fallback, and GitHub Actions/GitHub Pages delivery.

Link: https://preferablehuman.github.io/portfolio/

## Skills priority

Pin these top three:

1. Java
2. Spring Framework
3. REST APIs

Prioritize next:

Java 8, Java 11, Spring MVC, Java EE, JAX-WS, SOAP APIs, SQL, Hibernate, HQL, JDBC, Oracle Database, IBM DB2, IBM WebSphere, Oracle WebLogic, Microservices, SOA, JMS, Azure Service Bus, Azure Functions, Jenkins, Maven, JUnit, Log4j2, Production Support, Performance Tuning, Root Cause Analysis, CI/CD, Git, Agile/Scrum.

Project-qualified skills:

AWS, Terraform, Docker, Apache Spark, PySpark, Spark Structured Streaming, PostgreSQL, React, TypeScript, FastAPI, PyTorch, Hugging Face Transformers, PEFT, LoRA.

Do not pin PEFT, Local LLMs, or LoRA for the general Java/backend profile. Do not present Kafka or Kubernetes as production expertise.

## Education and certifications

- Keep Central Michigan University MS in Computer Science, but confirm final graduation status and final GPA before adding or changing either.
- Keep Lovely Professional University BTech in Computer Science and Engineering.
- Remove St. Paul's broad `2000-2016` date range or correct it to the verified 10+2 period only if desired; it adds little value for an experienced profile.
- Retain Microsoft Certified: Azure Fundamentals as the active certification.
- Retain the Azure Developer Associate and Azure Data Engineer Associate entries with LinkedIn's visible expired status; do not present them as active credentials.
- De-emphasize or remove generic workshop/training certificates from the visible top set.

## Items requiring confirmation before live changes

- Location will remain `Haldwani, Uttarakhand, India`, matching the live profile.
- Contact information will not be changed because the live contact overlay did not expose a verifiable email or phone during the read-only audit.
- NTT title and dates will remain exactly as currently shown: `Software Engineer`, Aug 2022 - Aug 2024.
- Capgemini trainee end date: May 2020 versus June 2020.
- Final CMU graduation status/date and final GPA.
- Language proficiency will not be changed in this update.

## Silent-update controls

- Before editing, verify LinkedIn's network-sharing/profile-update setting is disabled when accessible.
- For every experience, education, or certification form, keep `Notify network` or its equivalent switched off.
- Never click `Create a post`, `Share`, `Post`, or any option that announces profile changes.
- After each save, verify only the intended profile field changed and no post was created.

## Claims intentionally removed or downgraded

- Removed the NTT 20% issue-resolution metric and 50% delivery metric because they remain source-dependent.
- Replaced the broad Capgemini 90% performance claim with the directly reconstructed 60+ seconds to 10-20 seconds VIN latency result.
- Removed the unverified 99% JUnit coverage claim.
- Kept FHIR as exposure rather than production ownership.
- Did not claim production Kafka or Kubernetes ownership.
- Did not claim multi-node Spark or exactly-once PostgreSQL writes.
