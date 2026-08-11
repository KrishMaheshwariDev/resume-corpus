# Project Evidence Overlay — 2026-08-11

Status: High-priority repository-validated overlay for project claims.

Purpose: Capture implementation facts verified from current GitHub repositories during interview preparation. When this file conflicts with older resume language, prefer the implementation evidence here for technical precision.

---

# 1. AWS Automated Spark Pipeline / NYU Taxi Platform

Repository: `preferablehuman/AWS-automated-spark-pipeline`

## Confirmed architecture

- S3 is the durable ingestion boundary.
- S3 `ObjectCreated` events trigger Lambda.
- Lambda stages uploaded CSVs into EFS.
- Lambda uses a `.part -> .csv` rename pattern so Spark does not discover a partially copied file.
- Spark Structured Streaming continuously watches the EFS input path.
- New files are processed as micro-batches.
- Spark enforces an explicit schema and derives fields including trip length and day of week.
- `foreachBatch` writes each micro-batch to PostgreSQL/RDS over JDBC in append mode.
- Spark checkpoint data is persisted on EFS so stream progress can survive container/process restarts.
- Terraform provisions networking and AWS resources including VPC/subnets/NAT, security groups, IAM, S3 notifications, Lambda, EFS, ECS, RDS, and CloudWatch-related resources.
- Docker packages the Spark workload.

## Resume-safe architecture statement

`Built an event-driven AWS data pipeline where S3 uploads trigger Lambda staging to EFS, Spark Structured Streaming processes files in micro-batches, and transformed data is persisted to PostgreSQL/RDS; provisioned the cloud environment with Terraform.`

## Important implementation boundary: Spark runtime

The current Spark job explicitly uses `SparkSession.builder.master("local")`.

Therefore:

- The project is containerized and deployed on ECS, but the current code is **not a multi-node distributed Spark cluster**.
- Do not claim executor scaling across multiple Spark worker nodes based on this repository.
- Safe description: `Spark Structured Streaming workload containerized on ECS`.
- If discussing future scale, say that a production-scale version could move to EMR, Glue, EKS/Spark Operator, or another distributed Spark runtime.

## Important delivery-semantics boundary

The README's broad exactly-once wording should not automatically become a resume claim.

Current sink behavior:

- Structured Streaming uses checkpoints for progress recovery.
- `foreachBatch` writes to PostgreSQL with `mode("append")` over JDBC.
- An external JDBC append sink can duplicate rows if the database commit succeeds but Spark fails before recording batch completion.

Therefore:

- Checkpointing provides recoverable stream progress.
- End-to-end exactly-once persistence to PostgreSQL is **not proven** by the current implementation.
- For true idempotent/exactly-once-style persistence, use stable record/batch keys, unique constraints, upsert/MERGE semantics, or an idempotent sink contract.

Resume-safe wording:

`Persisted Structured Streaming checkpoints on EFS for restart recovery; designed the pipeline with explicit file-staging and failure visibility.`

Avoid: `guaranteed exactly-once writes to PostgreSQL`.

## Performance/implementation note

The `foreachBatch` path calls `batch_df.count()` for logging before performing the JDBC write. Because both are Spark actions, the batch may be computed more than once unless cached/persisted.

This is useful as an interview optimization discussion but is not necessary on the resume.

## Security improvement boundary

- Database URL is injected through environment configuration.
- Database username/password are present in application configuration in the current repo.
- For stronger production architecture, credentials should move to AWS Secrets Manager or SSM Parameter Store and be injected through ECS task-role/runtime configuration.

Do not claim that Secrets Manager is already implemented unless the repository changes.

## 40% runtime improvement metric

Existing resume variants contain `40% runtime/processing improvement` for the 8GB+ taxi workload.

Current repository does **not** establish the comparison baseline.

Until the baseline is reconstructed, mark this metric as **source-dependent / verify before prominent use**.

Safer fallback:

`Processed an 8GB+ taxi dataset using Spark/PySpark in an automated AWS pipeline.`

## Strong interview themes

- Why S3 as durable ingestion boundary.
- Why Lambda only for lightweight event/staging work, not Spark execution.
- Why EFS for filesystem-based streaming and persistent checkpoints.
- Atomic `.part -> .csv` staging.
- Structured Streaming micro-batches and `maxFilesPerTrigger` rate control.
- Checkpointing vs sink idempotency.
- Failure behavior when PostgreSQL is unavailable.
- Terraform reproducibility.
- Migration path from local-mode Spark in ECS to managed/distributed Spark.

---

# 2. Interactive Portfolio System

Repository: `preferablehuman/portfolio`

## Confirmed stack

- React
- TypeScript
- Vite
- Tailwind CSS
- Motion for React
- Lucide React
- GitHub Pages
- GitHub Actions

## Confirmed functionality

- Recruiter-facing single-page application.
- Dedicated Overview, About, Experience, Projects, Skills, Education, and Contact views.
- Project case studies with structured evidence.
- Skill search/evidence views and deep links.
- Persisted dark/light theme preference.
- Resume preview/download workflow.
- GitHub Pages deployment with SPA deep-link fallback.

## Deep-link implementation detail

GitHub Pages is a static host and does not natively perform application-style SPA rewrites for arbitrary routes. The deployment copies the built `index.html` to `404.html`, allowing direct routes such as `/portfolio/projects` to fall back to the SPA shell.

Resume-safe wording:

`Built and deployed a recruiter-facing React/TypeScript SPA on GitHub Pages with searchable skill evidence, project case studies, persisted theming, and deep-link fallback support.`

## Maintainability boundary

The current `App.tsx` is large and centralizes significant page composition. It works, but it should not be presented as an ideal modular architecture.

If asked how to improve it:

- split page-level components;
- extract reusable feature components and hooks;
- keep content in typed data modules;
- consider routing/library-level separation as complexity grows.

---

# 3. Project skill-depth rules

## AWS / Spark / Terraform

Strong project evidence exists for:

- AWS S3, Lambda, EFS, ECS/Fargate, RDS, VPC/IAM/networking concepts;
- Terraform IaC;
- Docker;
- Spark/PySpark/Structured Streaming;
- PostgreSQL/JDBC;
- event-driven file ingestion.

## Kubernetes

Do not infer production Kubernetes from the AWS Spark repository. Kubernetes remains separate project/knowledge exposure unless another repository/source supports stronger use.

## Kafka

Do not infer Kafka from this pipeline. Kafka is separate small-project/hands-on experience from prior context, not production evidence from this repository.

---

# 4. Resume generation rule from this overlay

1. Use the AWS pipeline for cloud/data/event-driven/IaC roles.
2. Prefer exact architecture facts over broad distributed-systems buzzwords.
3. Do not claim multi-node distributed Spark from the current ECS/local-mode implementation.
4. Do not claim end-to-end exactly-once PostgreSQL delivery from checkpointing alone.
5. Verify the baseline before using the 40% runtime metric.
6. Use the portfolio for frontend/full-stack evidence, not as a primary Java-backend story unless the JD values React/TypeScript.
