# Resume Corpus

Private repository for resume source files, resume optimization knowledge base, role profiles, scoring rules, source audits, archive-derived profile data, interview-validated work evidence, project implementation evidence, and future job-description-specific resume variants.

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
9. profile consistency and truthfulness,
10. source confidence and conflict handling,
11. bullet-level rewrite recommendations.

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

profiles/
  MASTER_PROFILE_V2.md
  PROFILE_FACT_MATRIX_V2.yml
  WORK_EXPERIENCE_EVIDENCE_OVERLAY_2026-08-11.md
  PROJECT_EVIDENCE_OVERLAY_2026-08-11.md
  EVIDENCE_FACT_OVERLAY_2026-08-11.yml
  ARCHIVE_RESUME_CORPUS_AUDIT.md
  UNRESOLVED_SOURCES.md
  MASTER_PROFILE.md
  PROFILE_FACT_MATRIX.yml
```

## Operating rule

Every resume optimization run must start with the mandatory run protocol and checklist:

1. `kb/optimization_run_protocol.md`
2. `kb/optimization_run_checklist.yml`

Then read the archive-refreshed baseline profile files:

3. `profiles/MASTER_PROFILE_V2.md`
4. `profiles/PROFILE_FACT_MATRIX_V2.yml`
5. `profiles/ARCHIVE_RESUME_CORPUS_AUDIT.md`

Then apply the newer high-priority evidence overlays **after** the V2 baseline:

6. `profiles/WORK_EXPERIENCE_EVIDENCE_OVERLAY_2026-08-11.md`
7. `profiles/PROJECT_EVIDENCE_OVERLAY_2026-08-11.md`
8. `profiles/EVIDENCE_FACT_OVERLAY_2026-08-11.yml`
9. `profiles/UNRESOLVED_SOURCES.md`

Overlay rule:

- For conflicts involving implementation detail, architecture, ownership, skill depth, or metric confidence, prefer the 2026-08-11 evidence overlays.
- Do not use the overlays to silently resolve HR title/date/contact conflicts unless explicitly marked resolved.
- Preserve `UNRESOLVED_SOURCES.md` as the final guardrail for remaining conflicts.

Then read the core knowledge-base files:

10. `kb/resume_optimization_knowledge_base.md`
11. `kb/human_review/resume_perception_knowledge_base.md`
12. `kb/scoring/weights.yml`
13. `kb/scoring/human_review_weights.yml`
14. `kb/skills/java_backend_taxonomy.yml`
15. `kb/roles/java_backend_engineer.yml`
16. `kb/writing/bullet_semantics.yml`
17. `kb/writing/action_verbs_java_backend.yml`

Then inspect or edit resume source files. Resume edits must preserve truthfulness, avoid inflated claims, and optimize for both ATS retrieval and human reviewer comprehension.

## Evidence precedence

Use this source order for resume facts unless a task explicitly chooses a different primary source:

1. explicit user confirmation in the current conversation,
2. 2026-08-11 evidence overlays,
3. current repo resume source,
4. V2 master profile / fact matrix,
5. archive audit and LinkedIn/academic exports,
6. current project repositories,
7. older resume variants.

For project implementation facts, repository code can outrank older resume wording when it reveals a technical limitation or more precise architecture.

## Legacy profile files

`profiles/MASTER_PROFILE.md` and `profiles/PROFILE_FACT_MATRIX.yml` are retained for audit/history. Prefer the V2 files plus the 2026-08-11 overlays for future resume work because they incorporate the uploaded resume archive, LinkedIn PDF export, academic history, degree-plan evidence, detailed interview-prep work reconstruction, and current repository validation.

## Non-negotiable rule

Do not edit resume files directly from memory alone. Reload the protocol, checklist, V2 baseline profile, 2026-08-11 evidence overlays, archive audit, unresolved-source checklist, and knowledge base first.
