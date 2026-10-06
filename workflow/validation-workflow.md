# Test Case Validation Workflow

Validation is a separate quality gate.

## Step 1 — Load Context

Read:
- `AGENTS.md`;
- `README.md`;
- relevant rules;
- `schemas/test-case-schema.md`;
- `context/project-context.md`;
- `template/Test Case template.xlsx` (for column structure);
- `template/PLM-659.xlsx` (for writing style reference).

## Step 2 — Load Generated Test Cases

Read the generated XLSX from `output/{TICKET}.xlsx`.

## Step 3 — Validate Schema

Check:
- Sheet name is `Tests`;
- Header row contains all 20 template columns in order;
- Required fields are populated for each test case;
- Multi-step row convention is correct (metadata only on step 1 rows).

## Step 4 — Validate Field Format

Check:
- Summary follows `[TC][{TICKET}] ...` format;
- Requirement Keys contains the PRD ticket ID;
- Priority is `High`, `Medium`, or `Low`;
- Test Category is a valid value;
- Folder follows the organizational path convention.

## Step 5 — Validate Traceability

For every test case:
- identify its requirement;
- verify the requirement exists in the PRD;
- verify the scenario is relevant.

## Step 6 — Validate Logic

Check:
- preconditions are valid (not actions);
- test steps are executable;
- expected results are observable;
- step data is appropriate;
- priority matches risk assessment.

## Step 7 — Detect Hallucinations

Flag:
- unsupported limits;
- unsupported messages;
- unsupported statuses;
- unsupported UI elements;
- unsupported roles;
- unsupported behavior.

## Step 8 — Detect Duplicates

Identify exact and semantic duplicates.

## Step 9 — Validate Coverage

Check applicable test design dimensions.

## Step 10 — Validate Contradictions

Find expected results that conflict with requirements or with other test cases.

## Step 11 — Validate XLSX

Open and verify:
- the workbook opens without corruption;
- the header row matches the template exactly;
- row lengths and column alignment;
- multi-step grouping is correct;
- field integrity (no misaligned or truncated cells);
- text cells were not converted to numbers or dates.

## Step 12 — Decision

Possible outcomes:

### PASS
No critical issues.

### PASS WITH WARNINGS
No critical issues, but ambiguities or non-critical gaps exist.

### FAIL
Critical issue exists and output should not be treated as production-ready.

## Step 13 — Remediation

For every failure:
- identify the exact test case;
- identify the violated rule;
- explain the correction;
- regenerate only affected cases where possible.

Do not rewrite the entire test suite unnecessarily.

## Enforced Validation Evidence

Validation requires these inputs in addition to the XLSX:
- source inventory;
- atomic requirement catalog with evidence;
- scope/applicability matrix;
- test-condition inventory;
- decision tables and state models when applicable;
- bidirectional coverage matrix;
- ambiguity/assumption/blocker log;
- deduplication register.

If these artifacts are absent, coverage completeness cannot be verified and the result is `FAIL`.

## Scope-Closure Validation Procedure

1. Re-extract a sample and all high-risk source sections independently to detect missed requirements.
2. Confirm every explicit requirement and acceptance criterion has `COVERED`, `CONSOLIDATED`, `BLOCKED`, or `NOT APPLICABLE` disposition with evidence.
3. Challenge every `NOT APPLICABLE` and `BLOCKED` decision; reject unsupported rationales.
4. Confirm every applicable coverage dimension has test conditions and mapped test cases.
5. Count feasible decision-table rows and verify each row is mapped; inspect evidence for impossible rows.
6. Verify every documented state and valid transition is mapped.
7. Verify every test Description lists the internal requirement/condition IDs it covers.
8. Trace each expected result to an explicit/derived oracle or approved assumption.
9. Compare semantic signatures, not titles, for duplicate detection.
10. Confirm all High priorities have risk evidence.
11. Confirm explicit compatibility, migration, unchanged/non-impact, negative, and integration-error statements have direct coverage.

## Current Template Validation

Validate against `template/Test Case template.xlsx`, not the older PLM-659 header:
- `Tests` sheet and exact current 20-column order;
- `Test Type` and `Automation Content` retained;
- `Test Type` and `Test Category` use current allowed values when populated;
- no template sample rows;
- no metadata on continuation rows;
- one consistent Folder value per ticket unless the user requested multiple target folders;
- no extra space after the final folder `/`;
- no `Functional` category copied from the old reference without confirmed target-project support.

## Decision Rules

`PASS` requires complete supported scope, valid oracles, no unexplained matrix gaps, no critical ambiguity, and a valid workbook.

`PASS WITH WARNINGS` is allowed only when all executable supported scope is covered and remaining limitations are explicitly source-blocked and non-critical.

`FAIL` applies when evidence artifacts are absent; an explicit testable requirement, feasible decision row, documented valid transition, or applicable dimension is missing; a test is unsupported; a critical oracle is unknown; or the XLSX contract is invalid.
