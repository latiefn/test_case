# Scope Model and Coverage Closure

This rule turns “complete coverage” into an inspectable QA contract. Complete coverage means coverage of the **documented and testable scope**, not every behavior that can be imagined.

## 1. Mandatory Analysis Artifacts

Before writing test cases, create these internal artifacts:

1. **Source inventory** — every input file, its purpose, extraction status, and unreadable areas.
2. **Atomic requirement catalog** — one record per requirement, acceptance criterion, business rule, constraint, or explicit non-impact statement.
3. **Scope model** — actors, entities, data, actions, states, rules, workflows, interfaces, configuration, and change impact.
4. **Test-condition inventory** — the distinct conditions that require verification.
5. **Decision tables / state models** — whenever outcomes depend on combinations or transitions.
6. **Risk assessment** — impact and likelihood evidence for prioritization and depth.
7. **Coverage matrix** — requirement and condition to test-case mapping, including disposition.
8. **Ambiguity log** — missing, conflicting, or untestable behavior and exact clarification questions.
9. **Deduplication register** — duplicate candidates removed or consolidated and why.
10. **Validation report** — final gate result and unresolved warnings.

These artifacts may remain working notes unless the user asks for them, but they must exist and be used. Unresolved ambiguities and coverage blockers must always be reported to the user.

## 2. Atomic Requirement Catalog

Each requirement record must contain, when available:

- stable ID: official ID or internal `REQ-###`;
- exact source and location;
- faithful source statement;
- basis: `EXPLICIT`, `DERIVED`, `ASSUMPTION`, or `UNKNOWN`;
- actor or system participant;
- preconditions and trigger;
- action or event;
- input/data and relevant partitions;
- business rule or constraint;
- expected outcome / test oracle;
- states and transitions;
- dependencies and affected interfaces;
- in-scope, out-of-scope, or explicitly unchanged status;
- risk evidence;
- testability status;
- ambiguity or conflict references.

Do not flatten multiple independent behaviors into one record. Do not lose acceptance criteria, table rows, footnotes, image annotations, examples that define behavior, or explicit “unchanged/not affected” statements.

## 3. Test-Basis Discipline

Use these basis types consistently:

### EXPLICIT
Behavior stated directly by the current requirement, accepted project rule, or authoritative source.

### DERIVED
A test condition produced from explicit behavior using a recognized technique, such as a documented boundary, an equivalence class, a feasible state combination, or a documented transition. A derived condition may vary input or state, but it must not invent a new product rule or expected outcome.

### ASSUMPTION
A proposed interpretation not guaranteed by the sources. Do not turn it into a test oracle unless the user explicitly authorizes assumption-based design. Track it using `ASSUMPTION-###`.

### UNKNOWN
The action, condition, or outcome cannot be established. Record a blocker and ask a precise clarification question. Do not disguise it as an executable test.

An implicit expectation is testable only when it follows necessarily from explicit rules. “Common behavior,” industry convention, or personal experience alone is not a sufficient oracle.

## 4. Scope Model

For every feature or change, inspect each axis and record what exists:

| Axis | Questions |
|---|---|
| Actors and permissions | Who may initiate, view, modify, approve, or consume the behavior? Which prohibitions are explicit? |
| Entities and fields | What is created or changed? Which attributes, relationships, required values, defaults, and uniqueness rules are documented? |
| Actions and triggers | Which user actions, events, schedules, callbacks, or system triggers start behavior? |
| States and transitions | What are the valid states, transition triggers, guards, side effects, and terminal/recovery states? |
| Rules and outcomes | Which conditions, calculations, precedence, eligibility, routing, and fallback rules determine the result? |
| Workflows and journeys | What are the primary, alternate, cancellation, interruption, retry, and resumption paths when documented? |
| Data lifecycle | How is data created, persisted, retrieved, updated, consumed, archived/deleted, migrated, and audited when applicable? |
| Configuration | Which scopes inherit or override values? Are settings independent? What happens after changes? |
| Interfaces and integrations | What crosses UI, API, service, file, queue, notification, or third-party boundaries? What failures are defined? |
| Compatibility and impact | What existing data, users, workflows, reports, and explicitly unaffected features could regress? |
| Quality attributes | Which security, privacy, accessibility, performance, reliability, localization, compatibility, or compliance obligations are explicit? |

Do not silently skip an axis. Mark it `APPLICABLE`, `NOT APPLICABLE`, or `BLOCKED`, with a short evidence-based reason.

## 5. Test-Condition Inventory

Create conditions before test cases. Each condition must state:

`Condition ID | Requirement ID(s) | Basis | Actor/context | Preconditions/state | Trigger/input partition | Expected outcome/oracle | Technique | Risk | Applicability disposition`

A condition is not a test case. Multiple conditions may be combined only when one executable flow proves them without hiding a distinct failure or making diagnosis ambiguous.

## 6. Technique Selection and Combination Coverage

Select techniques from the requirement structure:

- equivalence partitioning for behaviorally equivalent data classes;
- boundary value analysis only for explicit boundaries;
- decision tables / cause-effect analysis for conditional outcomes;
- state-transition testing for stateful behavior;
- use-case or sequence testing for workflows;
- pairwise or other constrained combinatorial testing for many interacting factors;
- CRUD and lifecycle analysis for persistent entities;
- role/permission matrices for documented access rules;
- syntax/format testing for documented structured input;
- backward-compatibility and migration testing for changed existing behavior;
- data-isolation testing for parallel entities or configurations;
- concurrency, replay, duplicate-submission, ordering, and idempotency analysis only when repeated/parallel actions or asynchronous processing are in scope;
- experience-based/error-guessing scenarios only when tied to a documented rule, known defect, architecture risk, or explicit project context.

### Decision-table closure

Every **feasible, outcome-distinct** decision-table row must map to at least one test case. Mark impossible rows and cite the rule that makes them impossible. Do not remove a row merely to reduce test count.

### Large combination spaces

When exhaustive combinations are impractical:

1. cover every documented outcome, rule, precedence branch, and single-factor constraint;
2. use full combinations for critical or strongly interacting factors when feasible;
3. apply pairwise/constrained coverage to remaining independent factors;
4. include a baseline and targeted high-risk combinations;
5. record the reduction method and every intentionally omitted class.

Never claim exhaustive coverage when a reduction method was used.

### State-model closure

Cover every documented state and valid transition. Cover invalid transitions only when prohibition or resulting behavior is supported. Include persistence and side effects across transitions when applicable.

## 7. Risk-Based Depth and Priority

Assess risk using source-supported evidence:

- business/user impact;
- probability or exposure frequency;
- data integrity, financial, security, privacy, or compliance impact;
- integration and change complexity;
- recoverability and blast radius;
- history of defects, if documented.

Risk changes **depth and priority**, not whether an explicit requirement is covered. Low-risk requirements still need traceability. Every `High` priority case must have a clear risk basis in its description or the internal risk assessment.

## 8. Test Oracle Rules

Each expected result must be traceable to an oracle in this order:

1. explicit acceptance criterion or business rule;
2. explicit UI/API/data contract;
3. explicit project rule or approved baseline;
4. logically necessary result derived from the above;
5. approved assumption.

If none exists, classify the expected result as unknown and block that condition. Verify all observable effects required by the oracle, including returned/displayed values, persisted state, downstream effects, and absence of prohibited side effects when specified.

Do not require a particular message, status code, control, storage implementation, timing threshold, or fallback unless an authoritative source defines it.

## 9. Traceability and Coverage Matrix

The mandatory coverage matrix must support both directions:

- requirement/condition → test case(s), proving no scope item is missed;
- test case → requirement/condition, proving no unsupported test exists.

Use:

`Requirement ID | Condition ID | Scope axis/dimension | Scenario | Risk | Test Case ID(s) | Disposition | Evidence/Reason`

Allowed dispositions:

- `COVERED` — mapped to an executable case;
- `CONSOLIDATED` — covered by a case shared with another condition; identify that case;
- `BLOCKED` — oracle/setup/information is missing; identify clarification;
- `NOT APPLICABLE` — the dimension does not apply; give reason.

Blank dispositions are forbidden. `NOT APPLICABLE` and `BLOCKED` must never be used without a reason.

The XLSX `Requirement Keys` field remains the official ticket key. Put internal requirement/condition IDs in the test Description using `Coverage: REQ-### / COND-###` so atomic traceability is not lost in the exported file.

## 10. Redundancy Control

Normalize every candidate to this semantic signature:

`requirement/condition | actor/context | precondition/state | input partition | action/trigger | expected outcome | risk addressed`

Candidates with equivalent signatures are duplicates unless they use a materially different platform, data partition, transition, integration boundary, or risk. Consolidate duplicates and record the decision. Different wording does not make a test unique.

Do not over-consolidate cases when doing so hides separate failure causes, requires contradictory preconditions, or makes the test difficult to execute and diagnose.

## 11. Coverage Closure Gate

A suite is complete only when all of the following are true:

- every source was processed or explicitly reported unreadable;
- every explicit testable requirement and acceptance criterion has a disposition;
- every applicable scope axis and coverage dimension has at least one mapped condition and case;
- every feasible decision-table row and documented state transition is mapped;
- every explicit negative, non-impact, compatibility, migration, and integration-error promise is covered;
- every test case maps back to supported source evidence;
- every expected result has a valid oracle;
- no unresolved duplicate or contradiction remains;
- blockers, assumptions, reductions, and exclusions are reported;
- the XLSX passes structural and content validation.

A suite with unresolved critical requirements or missing applicable coverage cannot receive `PASS`. Use `PASS WITH WARNINGS` only when executable supported scope is covered and the remaining limitation is explicitly blocked by missing/ambiguous source information. Otherwise use `FAIL`.

Test count is never the closure criterion. If the number of cases is smaller than the number of atomic requirements, verify that every many-to-one mapping is explicit and diagnostically sound.