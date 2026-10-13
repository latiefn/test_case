# Test Case Generation Workflow

## Objective

Transform PRD sources into a minimal, high-value, traceable XLSX test suite.

## Phase 0 — Fast Context Load

Read:
- `AGENTS.md`
- `README.md`
- `schemas/test-case-schema.md`
- core generation rules listed in `AGENTS.md`
- relevant project context
- current XLSX template

Do not load validation/template-detail rules before they are needed.

## Phase 1 — Source Extraction

1. Inventory all PRD files.
2. Extract all requirement-bearing content.
3. Preserve source locations.
4. Separate explicit requirements, examples, assumptions, and ambiguous content.
5. De-duplicate overlapping sources.
6. Record contradictions.

Create `work/{TICKET}/analysis.md`.

## Phase 2 — Requirement Analysis

For each atomic requirement:
1. identify actor/precondition/action/outcome;
2. identify constraints and dependencies;
3. detect design triggers;
4. assess concrete risk;
5. classify testability;
6. record blockers only where behavior cannot be determined.

Classify ticket complexity:

### LOW
Simple behavior with no interacting states, no meaningful combination space, and no significant cross-feature impact.

### MEDIUM
Multiple validations, state/data lifecycle, or limited interaction/decision logic.

### HIGH
Large or interacting condition spaces, integration/migration impact, substantial cross-feature impact, or high documented risk.

Load `rules/11-scope-model-and-coverage-closure.md` for MEDIUM/HIGH or when closure analysis is triggered.

## Phase 3 — Test Design and Generation

For each requirement, generate only the test conditions activated by its triggers.

Priority order:
1. core functional behavior;
2. distinct business-rule outcomes;
3. explicit validation/error paths;
4. explicit boundaries;
5. required state/role/integration coverage;
6. concrete regression/non-impact coverage;
7. targeted high-risk combinations.

Deduplicate during generation, not only after generating a large candidate set.

Do not use a fixed number of cases per requirement.

Update `work/{TICKET}/coverage.md` as cases are created.

## Phase 4 — Coverage Closure

Check both directions:
- requirement/condition → test case;
- test case → requirement/condition.

For each uncovered item decide:
- add case;
- consolidate with existing case;
- mark blocked;
- mark not applicable.

Do not create generic cases to close a dimension that has no trigger.

## Phase 4.5 — Pre-Build Approval Gate

Before writing any XLSX file:

1. Present the full set of proposed test cases as a table or structured text for review.
2. Call out scenarios deliberately skipped because no source supports them, and any local blockers.
3. Confirm with the user any required metadata that cannot be derived from Jira/PRD — in particular **Folder sprint path**, **Reporter**, **Assignee**, and **Epic Key**. Folder paths follow `{Year}/{Year} Sprint {N}/{TICKET}` and the sprint is rarely derivable from the ticket; ask rather than invent.
4. Wait for approval, then build the workbook.

Skip the wait only when the user has already explicitly authorized direct generation.

## Phase 5 — XLSX Mapping and Validation

Load:
- `rules/04-test-case-rules.md`
- `rules/07-template-rules.md`
- `rules/08-output-xlsx-rules.md`

Map logical cases into the current template.

Generate `output/{TICKET}.xlsx`.

Then run validation using `rules/09-validation-rules.md` and `workflow/validation-workflow.md`.

Create `work/{TICKET}/validation.md`.

## Final Output

Return the XLSX and a concise summary of:
- test-case count;
- blocked requirements;
- coverage reduction used, if any;
- warnings/validation issues.

Do not place analysis artifacts inside the XLSX.
