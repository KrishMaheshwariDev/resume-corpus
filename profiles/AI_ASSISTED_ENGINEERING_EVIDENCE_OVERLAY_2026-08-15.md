# AI Product and AI-Assisted Engineering Evidence Overlay

Date recorded: 2026-08-15  
Evidence scope: explicit user confirmation, current GitHub repositories, repository documentation/tests, and existing profile evidence.  
Evidence precedence: this overlay supplements the work/project overlays; it never converts personal/project evidence into employer production evidence.

## Evidence model

- **AI product engineering (P2/P3):** models, retrieval, inference, evaluation, or AI APIs implemented inside an application.
- **AI-assisted engineering (P2 workflow):** Kunal directed, reviewed, tested, and accepted work produced with Codex or GitHub Copilot. This does not imply manual authorship of every line or autonomous acceptance/deployment.
- **Local-model R&D (P3):** hands-on installation, configuration, execution, comparison, and integration evaluation of Ollama, llama.cpp, and LM Studio.
- **Tool exposure (P4):** use only for a relevant tool without implementation evidence. No P4 item may be presented as delivered production capability.

All evidence below is project/personal evidence unless a separate professional source explicitly proves employer use.

## Runtime-AI project matrix

| Project | Purpose | AI role and models/tools | Engineering work | Verification | Class / maturity | Claim boundary |
|---|---|---|---|---|---|---|
| **AI Email Client** | Privacy-oriented email summarization, classification, and reply support | PyTorch, Hugging Face Transformers, T5, PEFT/LoRA, ROUGE | FastAPI model service; per-user adapter loading/lifecycle; MinIO artifacts; Prometheus diagnostics; React/TypeScript client | Model/evaluation workflow and repository/profile evidence; recorded ROUGE results remain source-backed project metrics | P2/P3, graduate capstone / implemented prototype | Do not claim production users, formal privacy compliance, foundation-model training, or enterprise scale |
| **CodingHelper** | Teach coding/DSA through generated, executable solution ladders | LangChain gateway, Ollama, `qwen2.5-coder:7b`, RAG, Qdrant | React/TypeScript + FastAPI; PostgreSQL source of truth; retrieval routes; isolated Java/Python execution; repair/reject/promotion gates | Generated implementations run against bounded asserting tests before display/reuse; repository includes automated tests | P2, implemented project | Bounded tests are not formal correctness; do not claim unrestricted sandbox security or production scale |
| **Article Voice Desk** | Local-first narration and image-aware reading for large documents | SmolVLM-256M-Instruct vision; Supertonic 3 ONNX TTS | Electron; shared prioritized inference worker; local model packaging; streaming parsers; SQLite persistence; bounded audio/reader windows; OS/HTTP fallbacks | Parser, queue, inference, buffering, progress, packaging, and resume tests; Windows/macOS release gates | P2, implemented desktop application | Do not infer OCR support, cloud model serving, user/adoption scale, or accessibility certification |

## Local-model R&D

Explicitly confirmed hands-on runtimes:

- **Ollama:** installed/configured and executed; integrated through CodingHelper's provider-neutral gateway.
- **llama.cpp:** installed/configured and executed for local-inference comparison and integration evaluation.
- **LM Studio:** installed/configured and executed for local-inference comparison and integration evaluation.

Safe description: `Compared local-model inference and integration workflows across Ollama, llama.cpp, and LM Studio, including setup, model execution, runtime behavior, and application-integration options.`

Do not claim a direct llama.cpp or LM Studio application integration, custom runtime modification, benchmark result, GPU optimization, production deployment, or distributed serving until code or measurements verify it.

## AI-assisted delivery across recent projects

Kunal explicitly confirmed sustained use of **Codex** and **GitHub Copilot** across recent projects. The safe ownership model is: Kunal directed architecture and implementation work, reviewed generated changes, debugged failures, and accepted changes only after relevant builds, tests, and runtime checks.

| Project | Delivered system | Direction-and-validation evidence |
|---|---|---|
| Resume Corpus | Evidence-ranked resume optimization and validation system | Evidence overlays, deterministic validators/scorers, regression cases, build and parse checks |
| Portfolio | React/TypeScript evidence portfolio | Case-study structure, lint/build checks, GitHub Pages workflow |

This attribution may extend to other recent repositories only after their repository purpose and validation signals are inspected. It is evidence of AI-assisted software delivery, not evidence that Codex/Copilot operated autonomously.

## Retrieval-safe claims

- `Hands-on AI product engineering across local LLM/RAG, transformer fine-tuning, local vision, and ONNX TTS projects.`
- `Directs and validates AI-assisted development with Codex and GitHub Copilot across recent software projects.`
- `Reviews generated changes and requires appropriate builds, automated tests, execution checks, and runtime validation before acceptance.`
- `Compared Ollama, llama.cpp, and LM Studio for local-model execution and integration; integrated Ollama into CodingHelper.`
- `Implemented human-in-the-loop and verification-gated handling of AI-generated code and evidence-constrained resume output.`

## Prohibited inferences

- employer-authorized or employer-production use of Codex, GitHub Copilot, or local-model runtimes;
- GitHub Models, Cursor, Claude Code, or Microsoft Copilot experience;
- autonomous agents that independently accept, deploy, apply, or make final decisions;
- measured productivity gains from AI tools;
- production/adoption scale for personal projects;
- formal correctness or security guarantees from bounded tests;
- direct llama.cpp/LM Studio application integration or custom runtime engineering;
- senior AI/ML engineer positioning based on these projects alone.

## Resume selection guidance

- General Java/backend resumes may include a concise Codex/Copilot or CodingHelper signal only when it improves target fit; the full AI inventory belongs in the corpus, not every resume.
- AI-enabled backend roles should lead with CodingHelper and AI Email Client, then select Article Voice Desk when local inference, desktop, or streaming evidence is relevant.
- AI-assisted-development JDs may use the direction-and-validation workflow plus the most relevant downstream project proof.
- Every AI skill named in a resume must map to a visible project bullet and retain its P2/P3 qualification.
