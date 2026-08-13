# Resume / ATS / Human-Review Research Digest — 2026

Last updated: 2026-08-12

## Purpose

Persistent research layer for the resume optimizer.

This file records externally researched principles. It does not contain candidate facts and must not override `profiles/` evidence.

## Core conclusion

A strong technical resume must work for three stages:

1. **machine retrieval and matching** — clean parsing, relevant titles/skills, semantic evidence;
2. **rapid human triage** — role clarity, recent experience, recognizable technologies, scale and outcomes;
3. **deeper technical review** — credible architecture, ownership, constraints, trade-offs, troubleshooting and measurable results.

Optimizing only one stage creates a weaker resume.

## Modern ATS / AI matching findings

### Greenhouse

Greenhouse Talent Matching documentation describes matching using structured candidate information such as:
- skills;
- titles;
- years of experience;
- companies/employment context;
- recruiter-selected and weighted requirements.

Its matching system can use semantic similarity rather than only exact literal keyword matches. It also exposes matched/missing evidence to human reviewers.

Implication:
- exact terminology matters for retrieval;
- contextual evidence matters;
- adding more repeated keywords is not the same as adding stronger evidence.

Source:
- Greenhouse Support, Talent Matching / data processing documentation.
- https://support.greenhouse.io/

### Workday

Workday recruiting documentation indicates machine-learning matching can use information across the resume, including experience, education, certificates, and other extracted content.

Implication:
- technologies should be demonstrated in experience/projects, not isolated only in the Skills section.

Source:
- Workday Admin Guide, Recruiting / candidate matching documentation.
- https://doc.workday.com/

### LinkedIn Recruiter

LinkedIn Recruiter can use:
- explicit listed skills;
- skills inferred from position descriptions and profile text;
- titles;
- years/seniority;
- companies;
- resume-derived information.

Implication:
- `skill -> context -> evidence` is stronger than keyword-only listing;
- resume and LinkedIn should share the same factual evidence model even though LinkedIn can be more expansive.

Source:
- LinkedIn Recruiter Help.
- https://www.linkedin.com/help/recruiter/

## Parsing and formatting findings

Mainstream ATS guidance consistently favors:
- text-based documents;
- standard section headings;
- conventional chronology;
- simple single-column structure;
- readable dates/titles;
- no reliance on graphics, icons, text boxes, or multi-column tables for critical information.

Greenhouse specifically warns that complex graphics, tables, headers/footers, text boxes, columns, unclear sections, and incomplete titles can interfere with parsing.

Resume implication:
- design through typography, spacing, hierarchy, and content;
- do not make the parser decode a visual design system.

## Human review findings

### Harvard career guidance

Current Harvard resume guidance emphasizes:
- specific rather than general;
- active rather than passive;
- fact-based rather than subjective;
- quantified/qualified results where useful;
- concise and easy to scan;
- accomplishments rather than generic duties.

Implication:
- evidence and outcomes should replace promotional adjectives.

Source:
- Harvard Mignone Center for Career Success, Create a Strong Resume.
- https://careerservices.fas.harvard.edu/

### MIT career guidance

MIT guidance emphasizes:
- familiar formatting;
- action verbs;
- specificity;
- accomplishments;
- technologies in context;
- quantification where appropriate;
- readable typography/margins;
- PAR-style thinking (problem/project, action, result).

Current MIT guidance does not support shrinking a resume aggressively merely to force one page.

Implication:
- page count is subordinate to readability and material evidence;
- concise one page is good when natural; two pages are acceptable when the second page adds real value.

Source:
- MIT Career Advising & Professional Development.
- https://capd.mit.edu/

### Scanning / information design

Human readers scan before deep reading. Information-carrying words at the start of bullets, clear headings, visible numerals, and predictable structure lower cognitive effort.

Do not treat the popular "6-second recruiter rule" as a precise scientific constant. Treat it as a reminder that the first pass is fast.

Implication:
- strongest role signal and strongest evidence must be visible early;
- the resume should reward deeper reading rather than require it to discover basic fit.

## Sentence / bullet research synthesis

Do not force every bullet into one formula.

Preferred engineering bullet shapes:
- action-first;
- impact-first;
- scale-first;
- architecture-first;
- modernization-first.

A high-value bullet usually contains several of:
- ownership/action;
- technology/method;
- system/domain;
- scale/constraint;
- outcome.

A metric is useful when it is reliable. A precise architectural or ownership fact may be stronger than an unsupported percentage.

## Page-length synthesis

Use 1–2 pages.

One page:
- preferred when material evidence fits comfortably;
- especially useful for general recruiting portals and rapid screening.

Two pages:
- justified when architecture, seniority, role breadth, or project evidence materially increases fit;
- never justified by filler.

Readability floors:
- normal body text must remain >=11 pt under the repository's current readability policy;
- margins should generally remain >=0.5 in;
- reduce redundancy before tightening typography.

## Skills-section synthesis

The Skills section has search/retrieval value, but it is not proof.

Evidence hierarchy:
1. skill used in professional achievement;
2. skill used in contextual professional responsibility;
3. skill used in project/academic evidence;
4. skill listed only;
5. unsupported/missing.

Resume optimization should reward levels 1–3 more than raw frequency.

## Current Java/backend market synthesis

For 3–7 year India Java/backend roles, recurring durable clusters observed in current postings include:
- Java;
- Spring/Spring Boot;
- REST APIs / microservices;
- SQL / relational persistence;
- JPA/Hibernate/JDBC;
- testing;
- Git/Maven/build/release tooling;
- CI/CD;
- debugging/performance/production ownership.

Frequently differentiating, role-dependent clusters include:
- AWS/Azure;
- Docker/Kubernetes;
- Kafka/event-driven systems;
- security/OAuth/JWT;
- observability;
- system design/distributed-systems thinking.

Market importance never grants permission to claim experience.

## Codex design findings

OpenAI Codex supports:
- repository-level `AGENTS.md` instructions;
- nested instruction layering;
- reusable Skills under `.agents/skills`;
- focused skills with progressive disclosure;
- eval/scored improvement workflows.

Architecture implication:
- keep `AGENTS.md` orchestration-focused;
- keep detailed candidate facts in `profiles/`;
- keep reusable domain/scoring rules in `kb/`;
- put repeatable execution workflow in a Skill;
- put deterministic checks in scripts;
- use evals to prevent regressions.

Official sources:
- OpenAI Codex AGENTS.md / agent configuration documentation.
- OpenAI Codex Skills documentation.
- OpenAI Codex use cases / scored improvement loop guidance.
- https://developers.openai.com/codex/
- https://learn.chatgpt.com/codex/

## Resume optimizer principles derived from research

1. Optimize for evidence-backed relevance, not keyword count.
2. Put exact high-value terms where truthful.
3. Demonstrate important terms in experience/project context.
4. Make the first quarter of the resume useful without reading the rest.
5. Use metrics only when confidence is sufficient.
6. Prefer direct measurements to reconstructed percentages.
7. Preserve machine-readable simplicity.
8. Keep one dominant idea per bullet.
9. Use 1–2 pages based on material evidence, not dogma.
10. Make every line justify its page cost.
11. Separate candidate facts from market observations.
12. Never compensate for a genuine gap with fabricated experience.

## Research limitations

- There is no universal proprietary ATS score.
- Individual employers configure ATS/recruiter filters differently.
- Current job samples are snapshots, not the full market.
- Human review behavior varies by recruiter, company, role, seniority, and referral context.
- Market benchmarks must be timestamped and periodically refreshed.
