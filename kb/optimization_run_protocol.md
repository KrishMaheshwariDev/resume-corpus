# Resume Optimization Run Protocol

Last updated: 2026-08-11
Repository: `preferablehuman/resume-corpus`

## Purpose

This file defines the mandatory protocol for every resume optimization run. It exists to keep results consistent across sessions, job descriptions, resume versions, and future context resets.

No resume source file should be edited before the required profile and knowledge-base files are read and applied.

## Mandatory preflight reads

Before analyzing or editing any resume, read these files in order:

### Profile baseline and evidence overlays

1. `profiles/MASTER_PROFILE_V2.md`
2. `profiles/PROFILE_FACT_MATRIX_V2.yml`
3. `profiles/ARCHIVE_RESUME_CORPUS_AUDIT.md`
4. `profiles/WORK_EXPERIENCE_EVIDENCE_OVERLAY_2026-08-11.md`
5. `profiles/PROJECT_EVIDENCE_OVERLAY_2026-08-11.md`
6. `profiles/EVIDENCE_FACT_OVERLAY_2026-08-11.yml`
7. `profiles/UNRESOLVED_SOURCES.md`

Apply the 2026-08-11 overlays after the V2 baseline. On conflicts involving implementation detail, architecture, ownership, skill depth, or metric confidence, prefer the overlays. Do not silently use them to resolve HR title/date/contact conflicts unless explicitly marked resolved.

### Resume optimization knowledge base

8. `kb/resume_optimization_knowledge_base.md`
9. `kb/human_review/resume_perception_knowledge_base.md`
10. `kb/scoring/weights.yml`
11. `kb/scoring/human_review_weights.yml`
12. `kb/skills/java_backend_taxonomy.yml`
13. `kb/roles/java_backend_engineer.yml`
14. `kb/writing/bullet_semantics.yml`
15. `kb/writing/action_verbs_java_backend.yml`

If a job-description-specific role profile is added later, read it after the baseline `java_backend_engineer.yml` file.

## Source precedence

Unless the user explicitly chooses a different source of truth, use:

1. explicit user confirmation in the active conversation,
2. 2026-08-11 evidence overlays,
3. current repo resume source,
4. V2 profile/fact matrix,
5. archive audit and exported source documents,
6. current project repositories,
7. older resume variants.

Repository code may outrank older project-resume wording when the code reveals a more precise implementation boundary, such as local-mode Spark, sink semantics, or unsupported scale claims.

## Optimization phases

### Phase 1: Intake

Collect or identify:

- resume source file path,
- target role,
- job description if available,
- page limit,
- output format,
- whether this is general optimization or JD-specific tailoring,
- truthfulness constraints and confirmed experience level.

### Phase 2: Parse and baseline review

Evaluate:

- resume structure,
- parse safety,
- section names,
- current skills coverage,
- current evidence quality,
- human-review first-pass clarity.

### Phase 3: Evidence reconciliation

Before scoring or rewriting:

- map each important resume claim to baseline/overlay evidence,
- apply ownership qualifiers,
- distinguish production vs project vs academic exposure,
- prefer direct timings/architecture facts over broad historical percentages when they conflict,
- downgrade source-dependent metrics when the underlying comparison cannot be reconstructed,
- preserve unresolved HR/contact/date conflicts.

Examples from the current overlays:

- NTT Log4j2 migration: strong ownership; exact CVE unknown; do not label as Log4Shell without proof.
- NTT memory incident: supporting investigator; do not say `I fixed the memory leak`.
- Capgemini VIN optimization: direct timing supports ~60+ sec to ~10–20 sec; do not automatically attach the older 90% claim.
- Kafka/Kubernetes: do not present as production ownership without separate evidence.
- AWS Spark: current code runs local-mode Spark inside the container; do not claim current multi-node Spark execution.
- JDBC sink: checkpointing does not alone prove end-to-end exactly-once PostgreSQL persistence.

### Phase 4: ATS-oriented analysis

Apply:

- hard requirement gate,
- exact keyword and phrase coverage,
- taxonomy and alias normalization,
- required and preferred skill scoring,
- lexical relevance,
- semantic JD-resume alignment,
- evidence strength grading.

### Phase 5: Human-review analysis

Apply:

- first-pass role clarity,
- top-half signal strength,
- evidence density,
- skimmability,
- action language strength,
- relevance ordering,
- credibility and restraint,
- grammar and consistency.

### Phase 6: Truthfulness gate

Before writing edits, reject or downgrade any suggestion that would create:

- invented technology experience,
- inflated years of experience,
- unsupported metrics,
- exaggerated leadership,
- fake production exposure,
- project-only skills presented as professional production experience,
- misleading cloud/Kafka/Kubernetes claims,
- inferred ownership of systems managed by another team,
- guessed implementation details for legacy systems or incidents.

Use labels where needed:

- production experience,
- project experience,
- academic experience,
- local project experience,
- exposure,
- familiar with,
- currently learning,
- supporting investigator,
- integration contributor,
- proof of concept.

### Phase 7: Edit strategy

Prioritize edits in this order:

1. preserve truthful high-signal metrics,
2. preserve strongest ownership stories,
3. improve role clarity,
4. add exact JD terms where truthful,
5. strengthen weak bullets using action + technology + context + outcome,
6. improve top-half scan value,
7. remove filler and weak repetitions,
8. preserve ATS parse safety,
9. keep page-limit constraints.

### Phase 8: Output report

Every optimization run should produce a report containing:

```text
Run type: General / JD-specific / One-page compression / Human-review pass / ATS pass
Knowledge base files loaded: Yes / No, with list
Resume source path:
Target role:
Overall fit: High / Medium / Low
ATS fit: High / Medium / Low
Human-review fit: High / Medium / Low
Hard requirements: PASS / WEAK / FAIL
Required skill coverage:
Preferred skill coverage:
Top matched evidence:
Weak or missing areas:
Recommended edits:
Truthfulness risks:
Metric confidence risks:
Ownership qualifiers applied:
Parse risks:
Files changed:
Commit SHA, if pushed:
```

### Phase 9: Post-edit validation

After editing, verify:

- no unsupported claims were introduced,
- no critical keywords were accidentally removed,
- high-signal metrics remain visible,
- source-dependent metrics were not promoted without evidence,
- ownership qualifiers remain accurate,
- production/project skill-depth distinctions remain accurate,
- section headings remain standard,
- formatting remains parse-safe,
- bullets remain readable and not over-compressed,
- final output still matches the target role.

If a PDF is generated later, validate extracted PDF text against the source.

## Consistency rule

Every future optimization run must explicitly use this protocol. If the assistant loses chat context, reload this file, the V2 baseline profile, the 2026-08-11 evidence overlays, unresolved-source file, and the mandatory knowledge-base files before making resume changes.

## Non-negotiable rule

Do not edit resume files directly from memory alone. Always reload the profile evidence and knowledge base first.
