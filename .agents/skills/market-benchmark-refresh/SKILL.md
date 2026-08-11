---
name: market-benchmark-refresh
description: Refresh timestamped Java/backend hiring-market benchmarks used by the resume optimizer. Use when asked to research current market requirements, refresh role priorities, or update the general-market benchmark.
---

# Market Benchmark Refresh

## Purpose

Refresh market evidence without mixing external job-market observations with candidate facts.

Normal resume optimization should consume the existing market benchmark. Do not re-research the market on every edit.

## Scope

Default market:
- India
- Java/backend software engineering
- approximately 3–7 years of experience
- product, GCC, enterprise, consulting, and startup hiring

Expand to remote/international or another role family only when explicitly requested.

## Research method

Prefer:
1. current employer career pages / ATS postings;
2. major recruiter/job platforms for broader pattern checks;
3. reputable career/recruiting documentation;
4. secondary articles only for supporting context.

Use a varied sample across company types and locations.

Do not infer exact market-wide frequency from a small sample. Label frequencies as qualitative unless a reproducible count is available.

## Extract

For each sampled role, capture:
- title;
- company;
- location;
- experience band;
- mandatory technologies;
- preferred technologies;
- backend responsibilities;
- cloud/DevOps expectations;
- testing/quality expectations;
- system-design/distributed-systems expectations;
- domain-specific requirements.

Aggregate into:
- critical/durable;
- common;
- differentiating;
- emerging;
- lower-frequency/niche.

## Candidate mapping

After aggregating the market, map it to `profiles/RESUME_POSITIONING_V1.yml` and evidence sources:

- strong professional match;
- partial/professional adjacent;
- project-backed;
- knowledge/exposure;
- genuine gap.

Never upgrade a candidate claim just because the market values it.

## Outputs

Update:
- `kb/market/india_java_backend.yml`
- `benchmarks/java_backend/benchmark_manifest.yml`
- optionally `kb/research/resume_research_2026.md` when research methodology or ATS/human-review findings materially change.

Record:
- researched date;
- source types;
- sample size if actually counted;
- limitations;
- notable market changes.

Do not change resume files during a market-refresh run unless the user also asks for resume optimization.
