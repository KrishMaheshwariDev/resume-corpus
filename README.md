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
8. bullet-level rewrite recommendations.

## Initial structure

```text
kb/
  resume_optimization_knowledge_base.md
  scoring/weights.yml
  skills/java_backend_taxonomy.yml
  roles/java_backend_engineer.yml
```

## Operating rule

When using this repository for future resume work, first read `kb/resume_optimization_knowledge_base.md`, then apply the YAML score and taxonomy files before editing resume source files.
