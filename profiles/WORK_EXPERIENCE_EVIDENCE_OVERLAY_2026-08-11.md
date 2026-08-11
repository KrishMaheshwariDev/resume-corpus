# Work Experience Evidence Overlay — 2026-08-11

Status: High-priority user-confirmed overlay for resume optimization.

Purpose: Capture detailed employment/project evidence elicited during interview preparation after `MASTER_PROFILE_V2.md` / `PROFILE_FACT_MATRIX_V2.yml` were created. When this file conflicts with older resume variants or archive-derived assumptions, prefer this file for **scope, ownership, architecture, implementation detail, and metric confidence**. Do not use it to silently resolve HR title/date/contact conflicts unless explicitly marked resolved.

## Evidence labels

- **CONFIRMED** — explicitly described by Kunal in interview-prep conversation or directly supported by current project/repository evidence.
- **RESUME-SAFE** — can be used in a resume if relevant and space permits.
- **INTERVIEW-SAFE** — useful for interviews but usually too detailed for a resume.
- **QUALIFY OWNERSHIP** — user contributed materially but was not sole/primary implementer.
- **UNRESOLVED** — do not convert into a strong claim without confirmation.
- **DO NOT CLAIM** — wording known to overstate or misrepresent the work.

---

# 1. NTT DATA — Point32Health / Harvard Pilgrim / Tufts Health Plan

## Business/domain context

**CONFIRMED**

- Client environment: Point32Health, formed from Harvard Pilgrim Health Care and Tufts Health Plan.
- The team originally supported Harvard Pilgrim services; after the combination/acquisition, Tufts traffic and projects increasingly integrated into the same service landscape.
- Services consolidated healthcare-member/patient, provider, insurance, and dependent data for internal and external consumers.
- Data handling was subject to healthcare/HIPAA-oriented controls and client governance.
- Core system was an established enterprise SOA environment rather than a greenfield microservice platform.

### Resume positioning

Strong domain keywords when relevant:

`healthcare payer`, `enterprise integration`, `member/provider data`, `SOA`, `SOAP`, `REST`, `Oracle`, `high availability`, `production support`, `regulated data`, `API integration`.

Do not claim formal HIPAA compliance ownership unless the target resume merely states healthcare/HIPAA-regulated context.

---

## Core service architecture

**CONFIRMED**

- Core services were SOAP-based and hosted on IBM WebSphere in company-leased datacenter infrastructure.
- Older services used Maven, JAX-WS, XML configuration, generated WSDL request/response classes, and Java service logic.
- Later services combined Spring Framework with JAX-WS, but JAX-WS remained dominant in the user-described services.
- Typical parent project contained two components:
  - a bean/model project generating WSDL/request/response classes;
  - a service project containing implementation/listener/business logic.
- Maven built the bean component before the service component.
- Deployable artifacts were JARs deployed to WebSphere.
- Multiple independent services ran on WebSphere rather than one monolithic application.

### Environment topology

**CONFIRMED**

- SIT: 2 load-balanced servers.
- Production: 4 load-balanced servers.
- Development: 4 servers that were not interconnected in the same way.
- Each server had an isolated WebSphere instance.
- Shared dependencies could reside in WebSphere or the internal Maven repository.
- Datacenter/server-infrastructure ownership was outside the user's developer scope.

### Resume-safe phrasing

- `Developed and maintained Java/JAX-WS SOAP services on IBM WebSphere in a load-balanced enterprise SOA environment.`
- `Integrated Spring Framework components into established JAX-WS service architecture while preserving existing SOAP contracts.`

### Claim boundary

**DO NOT CLAIM** that the user designed the datacenter, load balancers, or WebSphere topology.

---

## Oracle / PL/SQL / data access

**CONFIRMED**

- Services accessed Oracle through OJDBC.
- Java primarily consumed existing Oracle views, PL/SQL procedures, and SQL statements.
- A separate database team generally owned SQL/PLSQL implementation; application developers integrated those database contracts and applied business rules in Java.
- Java-layer decisions included whether dependent/additional member information should be returned.

### Resume-safe phrasing

- `Integrated Java services with Oracle through OJDBC, consuming established views and PL/SQL procedures while applying service-layer business rules.`

### Claim boundary

Do not present the user as the principal PL/SQL/database-schema owner for this engagement.

---

## Internal/external security boundary

**CONFIRMED**

- Internal services were accessible only within a restricted network and did not perform application-level authentication on every internal service call.
- External hospital/clinic/client traffic entered through an API Gateway owned by another team.
- Gateway authentication was outside the user's team's ownership.
- Downstream services received identity/user information and could validate whether a user was active/authorized for the specific service/framework.

### Resume-safe phrasing

- `Worked behind an enterprise API Gateway security boundary, consuming authenticated caller identity and enforcing service-level authorization rules.`

### Claim boundary

Do not claim ownership of the API Gateway authentication implementation.

---

## CAQH v2 / v4 service work

**CONFIRMED, terminology should remain cautious**

- User refers to internal service generations as CAQH v2/v4 according to the client's framework/versioning.
- CAQH v2 used conventional SOAP request/response without MIME.
- CAQH v4 supported MIME request/response as well as raw XML depending on request type.
- Service logic parsed requests and formatted output to the expected client/framework specification.
- Gateway handled authentication; the service received username/identity and performed service/framework-level active-user checks.
- After the Point32Health combination, CAQH flows also integrated Tufts REST services.
- For Tufts-origin data there was no Harvard-side local copy; requests were routed synchronously to Tufts REST services, with Tufts remaining the data holder.
- Partial downstream failures could be represented as partial/failure outcomes; timeouts propagated as timeout responses to the caller.

### Traffic

**CONFIRMED approximate operational volumes**

- CAQH v2: approximately 35K requests/day.
- CAQH v4: 10K+ requests/day.
- Other services: approximately 10–20K/day.
- Aggregate environment: roughly 55–65K+ requests/day.
- Existing resume figure `50K+ daily requests` is intentionally conservative and safe.

### Resume-safe phrasing

- `Supported healthcare integration services processing 50K+ daily requests across SOAP and REST workflows.`
- `Integrated synchronous downstream REST calls into existing SOAP service flows with explicit timeout and partial-failure handling.`

### Standards note

CAQH CORE operating/connectivity rules and HL7 FHIR are separate standards. Do not imply that CAQH v2/v4 is FHIR versioning.

---

## CI/CD and deployment ownership

**CONFIRMED**

### Non-production

- Jenkins coordinated the build/deploy workflow.
- Jenkins built the service JAR and pushed it to a deployment location.
- IBM UrbanCode Deploy retrieved the selected artifact and deployed it to WebSphere.
- Developers owned build/test readiness and non-production validation.

### Production

- A dedicated deployment team executed scheduled production deployments and server downtime/restart activities.
- Developers supplied the tested JAR, change log, and test evidence.
- Developers executed post-deployment smoke/liveness/business validation and provided go/no-go or rollback recommendations.
- Failed releases could require RCA and reporting/escalation to client and leadership.

### Resume-safe phrasing

- `Supported Jenkins/Maven/IBM UrbanCode deployment workflows and production release validation for WebSphere services.`
- `Performed post-deployment smoke and business-flow validation and contributed go/no-go/rollback recommendations.`

### Claim boundary

Do not claim sole production deployment ownership.

---

## Testing

**CONFIRMED**

- User personally wrote/executed JUnit tests.
- Integration testing in development used SoapUI for response format and success/failure cases.
- A separate testing team owned broader regression, response-time, correctness, and SIT metrics.
- Developers performed production smoke testing after deployment.

### Resume-safe phrasing

- `Validated service behavior with JUnit and SoapUI and supported production smoke testing after releases.`

---

## Shared service-monitoring JAR

**CONFIRMED; strong observability/integration story**

- A shared monitoring JAR was included as a dependency by services.
- The user's team maintained/integrated the dependency JAR; the user personally worked with it.
- The library used AOP interception around service requests.
- A correlation/transaction ID supplied by the caller/source was propagated across services.
- Captured metadata included success/failure, request/response metadata, execution time/latency, and volume.
- Monitoring events were batched/queued to a separate central monitoring application.
- The central application consolidated monitoring events, persisted data, and exposed tabular/UI views.
- The central monitoring application itself was owned by another team.

### Resume-safe phrasing

- `Integrated and maintained an AOP-based service-monitoring library that propagated correlation IDs and captured latency, success/failure, and request-volume telemetry across services.`

### Claim boundary

Describe this as correlation-ID-based tracing/service monitoring; do not claim OpenTelemetry-style distributed tracing unless separately implemented.

---

## Production memory/resource incident

**INTERVIEW-SAFE; use carefully on resume**

### Situation

- A new Tufts synchronous REST integration plus JSON-to-XML processing introduced a memory/resource-retention issue.
- The WebSphere JVM could crash approximately every two hours.
- Production operations manually restarted JVMs while a permanent fix was prepared.
- The incident occurred around the Christmas period when normal deployment support availability was limited.

### Investigation and ownership

**QUALIFY OWNERSHIP**

- User supported root-cause investigation but was not the primary developer of the original change or the final correction.
- User reviewed the integration path/code and helped strategize remediation with the implementing developer.
- Higher management engaged Oracle support to analyze heap dumps.
- Oracle support confirmed a resource-retention pattern.
- User remembers REST-client/resource lifecycle and Jackson buffer recycling as involved but does not recall the exact leaked class/API; do not invent it.

### Mitigation

- An exact JVM argument related to Jackson buffer recycling is not recalled.
- The mitigation extended the crash interval from approximately two hours to approximately six hours.
- Four production nodes were restarted in rotation while the load balancer routed traffic to remaining nodes.
- Some in-flight read requests could fail during a node restart; the platform did not automatically retry them and clients could re-run the request.
- The 99.99% SLA was not considered broken because service remained available through the load-balanced nodes.

### Permanent correction

- Final code changes correctly managed/closed the relevant REST and Jackson/XML resources.
- Another developer was the primary implementer; user contributed analysis, strategy, and support.
- After deployment the repeated JVM crashes stopped.

### Resume-safe possibilities

Only use when a JD values production troubleshooting/Java performance, and preserve ownership:

- `Supported root-cause analysis of a WebSphere memory/resource-retention incident, contributing code-path review, mitigation strategy, and rolling-restart validation while maintaining service availability.`

### DO NOT CLAIM

- `I fixed the memory leak`.
- Exact leaking class/API.
- Exact JVM flag.
- Formal load/memory test additions unless independently confirmed.

---

## Log4j 1.x -> Log4j2 migration

**CONFIRMED; strongest NTT ownership/leadership story**

### Trigger

- Log4j 1.x had reached end of life/support.
- A client security review raised potential CVE/security exposure and requested upgrade.
- Exact CVE is not recalled.
- **Do not identify this as Log4Shell unless independently verified.**

### Original state

- Individual services carried their own logging `.properties` files inside JARs.
- At least one service had XML configuration; some services had Java code-based logging configuration.
- Older SLF4J dependencies/fallback behavior existed in some projects.
- Logs were written to server locations according to existing business/operations requirements.

### User ownership

- User was solely responsible for the initial proof of concept.
- Selected a difficult representative service/configuration.
- Migrated/standardized configuration on Log4j2 properties.
- Removed old SLF4J dependencies where the project permitted; remaining incompatible code was deprecated rather than hidden.
- Removed code-based logging configuration where applicable.
- Preserved existing output format, rolling behavior, filenames, and locations to minimize production change risk.
- Added granular log-level control and improved dependency logging within service logs.
- Implemented, tested, and deployed the PoC.
- Documented changes, dependency requirements, issues, limitations, and repeatable migration steps.
- After approval, distributed migration work among team developers, reviewed/approved changes, tracked rollout, and reported progress to the team lead.
- Other teams reused the documentation and occasionally asked for support.

### Outcome

- Project services were migrated away from Log4j 1.x.
- Logging configuration became reproducible and more consistent at service level.
- Dependency/service logs became easier to collect in development/SIT.
- Log size/history management and transaction-ID investigation became easier.
- No production regression was reported in the conversation.

### Resume-safe phrasing

- `Led a project-wide Log4j2 migration, owning the initial PoC, preserving production log contracts, documenting a repeatable upgrade path, and reviewing team rollout across services.`
- `Standardized service-level logging configuration and dependency logging, improving transaction-ID-based production troubleshooting.`

### Metric confidence

The older `20% issue-resolution time reduction` metric is **not independently substantiated by the interview-prep evidence**. Prefer qualitative wording such as `improved evidence collection/debugging` unless a source for 20% is retained and intentionally used.

### Technical nuance

Removing SLF4J was a project-specific compatibility choice, not a universal architecture recommendation. In a modern system, SLF4J may remain as an abstraction with a proper Log4j2 binding.

---

## Edifecs upgrade/integration support

**CONFIRMED; limited ownership**

- Existing platform used selected Edifecs capabilities wrapped by internal domain/industry logic rather than treating Edifecs as the entire application platform.
- Upgrade introduced new vendor JARs that were incompatible with internal JARs relying on older Edifecs classes/behavior.
- The broader upgrade had been delayed for months while teams worked through compatibility/integration issues.
- User joined temporarily as Java/integration support.
- Responsibilities included tracing requests through internal code and vendor JARs, inspecting/decompiling vendor JARs when source was unavailable, testing failure paths, identifying dependencies, and producing a technical roadmap for required internal-JAR changes.
- User did not own the vendor platform or the final production implementation.

### Resume-safe phrasing

- `Supported a complex Edifecs vendor-library upgrade by tracing request flows, analyzing binary/JAR dependencies, isolating compatibility failures, and documenting required internal-code changes.`

### Claim boundary

Describe decompilation as authorized internal vendor-integration analysis, not as a reverse-engineering achievement.

---

## FHIR

**CONFIRMED but limited**

- User worked on a FHIR migration proof of concept near the end of NTT tenure.
- Final implementation/outcome is not known.

### Resume rule

Use `FHIR PoC/exposure` rather than production FHIR migration ownership unless another source supports production delivery.

---

# 2. Capgemini — Mercedes/Daimler Vans

## Business context

**CONFIRMED**

- Client: Mercedes/Daimler, specifically vans.
- Application supported dealer/supplier/showroom vehicle configuration, recommendation, and ordering workflows.
- Vans had large option/package spaces and dealerships faced inventory risk when stocking configurations that might not sell.
- A predictive model generated commercially relevant configurations while the Java application remained authoritative for deterministic validation.
- Dealers could lock selected options/model and request recommendations or build a custom configuration for customer demand.

### Domain model

- Option: individual feature/part identified by code and price (for example engine, seats, lights, color).
- Some options were mandatory; others optional.
- Package: group of options sold together with package pricing.
- Avoid overclaiming exact vehicle-pricing calculation mechanics.

---

## Production architecture

**CONFIRMED**

- Java EE/J2EE monolithic application packaged as an EAR and deployed on Oracle WebLogic.
- DB2 database.
- JSF UI with AJAX.
- Logical layers included JSF/UI, service, DAO, and DTO layers.
- Hibernate/HQL used for persistence/querying; HQL is specifically confirmed for the VIN optimization.
- Separate Python prediction service existed outside the Java application.
- User did not build/train/deploy the prediction model but understood the integration sufficiently to debug cross-system issues using logs and data.

### Resume-safe phrasing

- `Developed and supported a Java EE/JSF/Hibernate enterprise application on WebLogic with DB2 for Mercedes-Benz Vans dealer configuration workflows.`

### Claim boundary

Do not guess the exact JSF component library or EAR module structure.

---

## Python prediction workflow

**CONFIRMED**

1. Dealer selected a vehicle model/options; some could be locked.
2. Java created/owned a unique run ID/record.
3. Java called the Python service through HTTP with the run/configuration request.
4. Python acknowledged the request.
5. Python asynchronously generated candidate configurations and wrote results to the database.
6. Python called a Java callback with the run ID when processing completed.
7. The callback was an HTTP GET with `runId`; Java returned success/accepted and triggered validation processing.
8. Java applied established deterministic rules to each generated configuration: mandatory options, expired options, package/combination validity, incompatible options, etc.
9. Individual configurations were accepted/rejected; the run was not necessarily rejected as a whole.
10. Valid configurations were presented to the UI, ordered by relevance.
11. Selected order information was delegated to the broader Mercedes central ordering ecosystem, which was outside the user's ownership.

### Architecture insight

Strong transfer story: an upstream predictive/non-authoritative system proposes results, while the Java service remains authoritative for deterministic domain validation.

### Modernization insight

The legacy callback uses GET despite triggering processing. For a new design, prefer POST or an event/message because GET should be safe/idempotent from an HTTP semantics perspective.

### Resume-safe phrasing

- `Integrated a Python-based vehicle-configuration prediction workflow with Java services, then enforced deterministic option/package validation before recommendations were exposed to dealers.`

### Claim boundary

The user now recalls the model as `hierarchical`; older resumes call it a `decision tree`. Avoid naming the model type unless needed and reconfirmed. `Python prediction service` is safest.

---

## VIN repeat-configuration feature — strongest Capgemini personal feature

**CONFIRMED; strong ownership**

### Business problem

- Existing customers could request a same/similar configuration to a previously purchased van by supplying its VIN.
- Supplier invoked an API rather than using the dealer UI.
- System retrieved the historical configuration, mapped legacy/expired option codes to current equivalents, validated whether an equivalent configuration was still available, and returned a usable current configuration.

### Original performance

- Caller experienced a long-running synchronous endpoint.
- Typical execution could take approximately 60 seconds or more.
- Hard timeout was approximately 120 seconds.
- Mapping logic originally ran in Java after data retrieval, and multiple-VIN processing was slow.

### User implementation

- User traced the bottleneck and moved deterministic code mappings from Java into an HQL query executed against DB2.
- Used HQL/DB2 `CASE` expressions for stable mapping transformations.
- Multiple VINs could be handled in a single/batched query/request path; exact maximum batch size is not recalled.
- Core business validation remained in Java.
- Timing was checked locally with Postman and in production logs.
- User implemented the query change, tested it, and supported the production rollout.

### Result

- Before: approximately 60+ seconds.
- After: approximately 10–20 seconds.
- For a 60-second baseline this is approximately a **67–83% latency reduction**.
- The older resume's `90% performance improvement` is not fully substantiated by the reconstructed timings and should not automatically be used for this feature.

### Resume-safe phrasing

- `Reduced VIN repeat-configuration API latency from ~60+ seconds to ~10–20 seconds by moving stable option-code mapping into set-based HQL/DB2 CASE expressions while retaining business validation in Java.`
- `Optimized multi-VIN configuration retrieval by consolidating deterministic mapping into database-side set processing, cutting synchronous response time by roughly two-thirds or more.`

### Interview design follow-up

If redesigning today, consider an asynchronous `202 Accepted + request ID/status` workflow for truly long-running requests where the external contract permits it.

---

## Nightly validation jobs

**CONFIRMED**

- WebLogic-scheduled background jobs checked that active configurations did not contain expired options.
- Exact remediation/status action after detecting invalid configurations is not recalled.

### Resume rule

Can support keywords such as `scheduled batch validation`, `WebLogic scheduler`, `reference-data validation`; do not invent the exact failure/remediation state.

---

## Production debugging / data-quality pattern

**CONFIRMED**

- Many production/local run issues were reference-data problems rather than defects in the core deterministic rule engine.
- Typical investigation path:
  - inspect Python logs to see whether a configuration was generated;
  - inspect Java logs for validation/invalidation behavior;
  - inspect DB2 state/reference data;
  - identify expired/bad option data or runtime validation failures.
- User recalls that a large majority of issues were data-related, but `90% of bugs were data-related` should be treated as conversational approximation, not a formal metric.

### Resume-safe phrasing

- `Diagnosed cross-system configuration failures across Python model output, Java validation logs, and DB2 reference data.`

---

## Mentoring

**CONFIRMED**

- User onboarded junior developers.
- Assigned contained day-to-day defects and small production changes.
- Explained codebase and business flow.
- Supported blockers.
- Reviewed code and tested/deployed work when appropriate.
- Used incremental tasks to help juniors learn the system progressively.

### Resume-safe phrasing

- `Mentored junior developers through incremental production defects/features, codebase walkthroughs, debugging support, and code reviews.`

### Claim boundary

Do not invent team size, number of mentees, or a specific quantified mentoring result.

---

# 3. Professional skill-depth corrections

These entries supersede overly broad older assumptions unless another primary source is explicitly chosen.

## Spring / Spring Boot

- **NTT production:** Spring Framework is confirmed in later JAX-WS services. Spring Boot appears in resume variants, but the detailed Point32Health interrogation did not establish a clear Spring Boot-specific production service.
- **Capgemini production:** Java EE/J2EE, EJB, JSF, Hibernate, WebLogic, and DB2 are confirmed for the Mercedes application.
- **Capgemini training:** Spring Framework/Spring MVC + Angular + PostgreSQL are confirmed.

Resume generator should not automatically say `Spring Boot production at both NTT and Capgemini` merely because the keyword appears in older resumes. Use Spring Boot where a separate resume/project source supports it, but do not anchor the Mercedes production story on Spring Boot.

## Kafka

- Project/small hands-on experience is supported by prior context.
- Production Kafka ownership is **not confirmed**.
- Safe labels: `project experience`, `hands-on project`, or skills-list keyword if relevant.

## Kubernetes

- Knowledge/hands-on learning/project exposure is supported by prior context.
- Production Kubernetes ownership is **not confirmed**.
- Avoid `deployed production workloads to Kubernetes` unless separately evidenced.

## PL/SQL

- NTT application work consumed Oracle PL/SQL procedures/views through OJDBC; database team generally owned procedure implementation.
- User understands SQL/PLSQL concepts, but the corpus should distinguish integration/consumption from database-team ownership.

---

# 4. Metric confidence corrections

## High confidence / safe

- NTT: 50K+ daily requests (conservative aggregate).
- NTT: 99.99% formal SLA/availability target.
- NTT CAQH traffic breakdown: ~35K/day v2; 10K+/day v4; ~10–20K/day other services (interview evidence, use aggregate on resume).
- Capgemini VIN feature: ~60+ sec -> ~10–20 sec, approximately 67–83% reduction for a 60-second baseline.

## Medium / source-dependent

- NTT: `20% issue-resolution time reduction` exists in older resume evidence but was not independently substantiated during detailed interrogation.
- NTT: `50% faster delivery cycles / EDX delivery improvement` exists in older resume evidence; user involvement in EDX/Edifecs analysis is supported, but the exact metric-to-contribution mapping should be verified before prominent use.
- Capgemini: `99%+ uptime` appears in resume sources; not challenged in detailed discussion but not independently reconstructed.
- Capgemini: `10% query improvement` exists in older sources; exact feature/context unresolved.

## Downgrade / verify before use

- Capgemini: blanket `90% performance improvement` should not automatically be attached to the VIN feature. Reconstructed timings support ~67–83% for that specific optimization.
- `99% code coverage` remains unverified.

---

# 5. Ownership-safe resume bullet library

Use these as source material, not mandatory final wording.

## NTT DATA

1. `Developed and maintained Java/JAX-WS healthcare integration services on IBM WebSphere, supporting 50K+ daily SOAP/REST requests under a 99.99% availability SLA.`
2. `Integrated Oracle views and PL/SQL procedures through OJDBC and applied service-layer member/provider business rules across healthcare data workflows.`
3. `Led the initial PoC and coordinated rollout for a Log4j2 migration, standardizing service logging while preserving existing production log formats, rolling policies, filenames, and locations.`
4. `Integrated an AOP-based monitoring dependency that propagated correlation IDs and captured latency, success/failure, and volume telemetry across services.`
5. `Supported root-cause analysis of a WebSphere resource-retention incident, contributing code-path review, mitigation strategy, and rolling-restart validation while maintaining platform availability.`
6. `Supported a complex Edifecs library upgrade by tracing request flows, analyzing JAR dependencies, isolating compatibility failures, and documenting required internal changes.`
7. `Supported Jenkins/Maven/IBM UrbanCode release workflows, executing post-deployment smoke/business validation and contributing go/no-go or rollback recommendations.`

## Capgemini / Mercedes-Benz Vans

1. `Developed and supported a Java EE/JSF/Hibernate application on WebLogic and DB2 for Mercedes-Benz Vans vehicle-configuration workflows.`
2. `Integrated a Python prediction workflow with Java services and enforced deterministic option/package validation before recommendations were exposed to dealers.`
3. `Reduced VIN repeat-configuration API latency from ~60+ seconds to ~10–20 seconds by moving stable mapping transformations into set-based HQL/DB2 CASE expressions while retaining business rules in Java.`
4. `Diagnosed cross-system configuration failures using Python-service logs, Java validation traces, and DB2 reference data.`
5. `Mentored junior developers through incremental production defects/features, codebase walkthroughs, debugging support, and code reviews.`

---

# 6. Interview-only / contextual details that can improve resume wording indirectly

These facts are useful for generating stronger but truthful bullets even when not quoted directly:

- NTT systems were mature enterprise services with separate infrastructure, DB, API-gateway, testing, and deployment teams; cross-team coordination was part of the work.
- Production rollout accountability mattered: failed releases could trigger RCA/client escalation.
- Point32Health migration introduced synchronous cross-system REST dependencies into an older SOAP/SOA environment, creating realistic timeout/partial-failure/resource-lifecycle concerns.
- Mercedes model integration deliberately separated probabilistic recommendation generation from authoritative deterministic validation.
- Mercedes VIN optimization is a concrete example of choosing the database for stable set-based transformation while keeping volatile domain rules in Java.

---

# 7. Explicit unknowns — never reconstruct from guesswork

## NTT

- Exact REST client implementation/library used for Tufts calls.
- Exact leaked class/client API in the memory incident.
- Exact JVM mitigation flag.
- Exact CVE that triggered the Log4j migration.
- Whether memory-watch/load testing was formally added after the incident.
- Final outcome of the FHIR proof of concept.

## Capgemini

- Exact JSF component framework.
- Exact EAR module breakdown.
- Exact transaction/JTA/EJB configuration.
- Exact Python callback async implementation details.
- Exact downstream order protocol into Mercedes central ordering.
- Exact table names/status values.
- Exact nightly-invalid-configuration remediation action.
- Exact number of junior developers mentored.

---

# 8. Resume generation rule from this overlay

When tailoring a resume:

1. Prefer **Log4j2 migration** for ownership/leadership/migration/security-maintenance roles.
2. Prefer **VIN optimization** for SQL/Hibernate/performance roles.
3. Prefer **Point32Health service architecture + 50K+/99.99%** for Java backend/enterprise integration/reliability roles.
4. Prefer **monitoring JAR + correlation IDs** for observability/production support roles.
5. Prefer **Tufts SOAP-to-REST integration** for integration/distributed-system/API roles.
6. Prefer **Edifecs analysis** for vendor integration/migration/legacy-modernization roles.
7. Prefer **Mercedes prediction + deterministic validation** for rule-engine/integration/decision-system roles.
8. Never convert supporting participation into sole implementation ownership.
9. Prefer reconstructed direct timings over broader historical percentages when the two conflict.
10. Keep skills such as Kafka/Kubernetes clearly labeled by actual depth.
