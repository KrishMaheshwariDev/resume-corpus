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
  optimization_run_protocol.md
  optimization_run_checklist.yml
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

Every resume optimization run must start with the mandatory run protocol and checklist:

1. `kb/optimization_run_protocol.md`
2. `kb/optimization_run_checklist.yml`

Then read the core knowledge-base files:

3. `kb/resume_optimization_knowledge_base.md`
4. `kb/human_review/resume_perception_knowledge_base.md`
5. `kb/scoring/weights.yml`
6. `kb/scoring/human_review_weights.yml`
7. `kb/skills/java_backend_taxonomy.yml`
8. `kb/roles/java_backend_engineer.yml`
9. `kb/writing/bullet_semantics.yml`
10. `kb/writing/action_verbs_java_backend.yml`

Then inspect or edit resume source files. Resume edits must preserve truthfulness, avoid inflated claims, and optimize for both ATS retrieval and human reviewer comprehension.

## Non-negotiable rule

Do not edit resume files directly from memory alone. Reload the protocol, checklist, and knowledge base first.
