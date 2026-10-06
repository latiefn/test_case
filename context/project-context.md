# Project Context

## Purpose

This file contains stable project-specific conventions.

It is intentionally separate from general QA methodology.

## Current Scope

The system generates software test cases from PRD (Product Requirement Documents) using Senior QA expertise.

PRD inputs may include:
- PDF;
- images / screenshots;
- XML;
- Markdown;
- plain text.

PRD files are stored under `prd/{TICKET}/`.

Output template:
- `template/Test Case template.xlsx` (20-column Jira import format)

Writing style reference:
- `template/PLM-659.xlsx`

Primary output:
- XLSX (saved to `output/{TICKET}.xlsx`)

## Current Generation Philosophy

The project prioritizes (in order):
1. **Complete scope coverage** — every requirement dimension is tested.
2. Requirement traceability — every test case links to a PRD ticket.
3. Meaningful functional coverage — no fake or redundant tests.
4. Executable, verifiable test cases.
5. Systematic coverage using decision tables, data isolation, backward compatibility, and non-impact verification.
6. Low redundancy.
7. Machine-readable output compatible with Jira import.

## Senior QA Coverage Expectations

Complete scope coverage is demonstrated through the artifacts and closure gate in `rules/11-scope-model-and-coverage-closure.md`, not by a fixed test count.

Every generation run must assess these dimensions and record `APPLICABLE`, `NOT APPLICABLE`, or `BLOCKED` with evidence:

| Dimension | Typical trigger |
|---|---|
| Functional and alternate behavior | Explicit action/outcome or acceptance criterion |
| Configuration and persistence | Configurable values, inheritance, overrides, or toggles |
| State combinations and transitions | Multiple conditions/states affect behavior |
| Negative, validation, and ineligibility | Explicit constraint, prohibition, or rejection behavior |
| Data isolation and lifecycle | Parallel entities, persistent data, usage/consumption, or migration |
| Roles and authorization | Documented actors or permission boundaries |
| Workflows and interruption | Sequential, cancellable, retryable, or resumable behavior |
| Interfaces and integrations | UI/API/service/file/queue/third-party contract |
| Compatibility and non-impact | Existing behavior changes or explicit “unchanged” promise |
| Boundaries and combinations | Explicit limits or interacting factors |
| Concurrency and idempotency | Repeated/parallel actions, callbacks, retries, or shared resources |
| Quality attributes | Explicit security, privacy, accessibility, performance, reliability, localization, or compliance requirement |

A dimension may not be silently omitted. Do not generate tests for a dimension whose expected behavior has no supported oracle.

## AI Behavior

AI agents must reload persistent context and must:
1. build atomic requirements and test conditions before writing cases;
2. use decision tables/state models when outcomes depend on combinations or transitions;
3. map every feasible row and documented transition to a test case;
4. preserve bidirectional requirement/condition/test traceability;
5. use reduction techniques only with documented rationale;
6. report ambiguities, blockers, assumptions, and exclusions;
7. write precise preconditions, executable steps, and observable expected results;
8. semantically deduplicate without hiding distinct failure risks;
9. pass an independent/adversarial coverage and XLSX validation pass.

## Project-Specific Conventions

### Ticket ID Format
PRD tickets follow `PLM-{number}`.

### Test Case Summary Format
`[TC][{TICKET}] {Descriptive title}`

### Requirement Keys
Set to the official PRD/Jira ticket ID. Put internal requirement and condition IDs in Description.

### Reporter
Use a user-supplied or stable known project identity. Ask if required and unavailable.

### Test Type and Test Category
The current template permits `Manual` and `Automated`. Use `Automated` only with authoritative automation evidence/content. `Functional` appears in the older reference but must not be used unless the target Jira project explicitly accepts it.

### Priority Values
`High`, `Medium`, `Low`. Priority must have a risk basis; do not default all cases to one value.

### Folder Path Convention
`{Year}/{Year} Sprint {N}/{TICKET}`

Example: `2026/2026 Sprint 16/PLM-659`

There is no space after the final `/`. Ask for a required year or sprint when unavailable; do not invent it.

### Multi-Step Layout
Step 1 contains applicable metadata and the first step. Continuation rows contain only Step Description, Step Data, and Expected Result.

### Output Location
Generated test case files are saved to `output/{TICKET}.xlsx`.

### Template Columns (20)
Key, Summary, Description, Requirement Keys, Test Type, Automation Content, Epic Key, Fix Versions, Status, Priority, Assignee, Reporter, Labels, Test Category, Components, Precondition, Folder, Step Description, Step Data, Expected Result

## Change Management

When a convention changes, update this file or the appropriate rule file rather than relying on conversation history.

Do not store temporary task-specific information here.
Do not store secrets, API keys, credentials, or personal data here.
