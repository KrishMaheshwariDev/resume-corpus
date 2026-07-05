# Resume Corpus

Private repository for resume source files, resume optimization knowledge base, role profiles, scoring rules, and future job-description-specific resume variants.

## Current purpose

This repository is intended to support a local, evidence-driven resume optimization workflow. The system should not pretend to reproduce one proprietary ATS score. Instead, it should evaluate resume-job fit through a hybrid scorecard:

1. parse quality,
2. hard requirement coverage,
3. exact keyword and phrase coverage,
4. weighted lexical relevance,
5. taxonomy and alias normalization,
6. semantic responsibility alignment,
7. evidence strength,
8. human-review readability and perception,
9. bullet-level rewrite recommendations.

## Current structure

```text
kb/
  resume_optimization_knowledge_base.md
  human_review/resume_perception_knowledge_base.md
  scoring/weights.yml
  scoring/human_review_weights.yml
  skills/java_backend_taxonomy.yml
  roles/java_backend_engineer.yml
  writing/bullet_semantics.yml
  writing/action_verbs_java_backend.yml
```

## Operating rule

When using this repository for future resume work, first read:

1. `kb/resume_optimization_knowledge_base.md`
2. `kb/human_review/resume_perception_knowledge_base.md`
3. `kb/scoring/weights.yml`
4. `kb/scoring/human_review_weights.yml`
5. `kb/skills/java_backend_taxonomy.yml`
6. `kb/roles/java_backend_engineer.yml`
7. `kb/writing/bullet_semantics.yml`
8. `kb/writing/action_verbs_java_backend.yml`

Then inspect or edit resume source files. Resume edits must preserve truthfulness, avoid inflated claims, and optimize for both ATS retrieval and human reviewer comprehension.
