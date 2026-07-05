# Resume Optimization Run Protocol

Last updated: 2026-07-05
Repository: `preferablehuman/resume-corpus`

## Purpose

This file defines the mandatory protocol for every resume optimization run. It exists to keep results consistent across sessions, job descriptions, resume versions, and future context resets.

No resume source file should be edited before the required knowledge base files are read and applied.

## Mandatory preflight reads

Before analyzing or editing any resume, read these files in order:

1. `kb/resume_optimization_knowledge_base.md`
2. `kb/human_review/resume_perception_knowledge_base.md`
3. `kb/scoring/weights.yml`
4. `kb/scoring/human_review_weights.yml`
5. `kb/skills/java_backend_taxonomy.yml`
6. `kb/roles/java_backend_engineer.yml`
7. `kb/writing/bullet_semantics.yml`
8. `kb/writing/action_verbs_java_backend.yml`

If a job-description-specific role profile is added later, read it after the baseline `java_backend_engineer.yml` file.

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

### Phase 3: ATS-oriented analysis

Apply:

- hard requirement gate,
- exact keyword and phrase coverage,
- taxonomy and alias normalization,
- required and preferred skill scoring,
- lexical relevance,
- semantic JD-resume alignment,
- evidence strength grading.

### Phase 4: Human-review analysis

Apply:

- first-pass role clarity,
- top-half signal strength,
- evidence density,
- skimmability,
- action language strength,
- relevance ordering,
- credibility and restraint,
- grammar and consistency.

### Phase 5: Truthfulness gate

Before writing edits, reject or downgrade any suggestion that would create:

- invented technology experience,
- inflated years of experience,
- unsupported metrics,
- exaggerated leadership,
- fake production exposure,
- project-only skills presented as professional production experience,
- misleading cloud/Kafka/Kubernetes claims.

Use labels where needed:

- production experience,
- project experience,
- academic experience,
- local project experience,
- exposure,
- familiar with,
- currently learning.

### Phase 6: Edit strategy

Prioritize edits in this order:

1. preserve truthful high-signal metrics,
2. improve role clarity,
3. add exact JD terms where truthful,
4. strengthen weak bullets using action + technology + context + outcome,
5. improve top-half scan value,
6. remove filler and weak repetitions,
7. preserve ATS parse safety,
8. keep page-limit constraints.

### Phase 7: Output report

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
Parse risks:
Files changed:
Commit SHA, if pushed:
```

### Phase 8: Post-edit validation

After editing, verify:

- no unsupported claims were introduced,
- no critical keywords were accidentally removed,
- high-signal metrics remain visible,
- section headings remain standard,
- formatting remains parse-safe,
- bullets remain readable and not over-compressed,
- final output still matches the target role.

If a PDF is generated later, validate extracted PDF text against the source.

## Consistency rule

Every future optimization run must explicitly use this protocol. If the assistant loses chat context, reload this file and the mandatory preflight files from the repository before making resume changes.

## Non-negotiable rule

Do not edit resume files directly from memory alone. Always reload the knowledge base first.
