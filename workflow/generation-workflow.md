# Test Case Generation Workflow

This workflow transforms a PRD into a validated XLSX file containing structured test cases designed by a Senior QA.

## Phase 0 — Context Loading

1. Read `AGENTS.md`.
2. Read `README.md`.
3. Read all applicable rules under `rules/`.
4. Read `schemas/test-case-schema.md`.
5. Read `context/project-context.md`.
6. Inspect the template: `template/Test Case template.xlsx`.
7. Study the reference: `template/PLM-659.xlsx`.
8. Identify the PRD files (under `prd/{TICKET}/`).

Do not start generation before context loading is complete.

## Phase 1 — Input Inventory

Create an internal inventory of all PRD sources:

| Source | Type | Purpose | Status |
|---|---|---|---|
| `prd/{TICKET}/{TICKET}.xml` | XML | Requirements | Available |
| `prd/{TICKET}/*.png` | Image | UI mockups / screenshots | Available |
| `prd/{TICKET}/add-info.xml` | XML | Additional requirements | Available |
| `template/Test Case template.xlsx` | XLSX | Output structure | Available |
| `template/PLM-659.xlsx` | XLSX | Writing style reference | Available |

Adapt the inventory to the actual files provided.

## Phase 2 — Extraction

Extract ALL requirements from ALL PRD sources.

Preserve source references.

Separate:
- explicit requirements;
- examples;
- explanatory content;
- assumptions;
- ambiguous content.

**Senior QA focus**: Don't just extract what's written. Note what's MISSING — gaps in error handling, undefined edge cases, unspecified interactions.

## Phase 3 — Normalization

Convert raw content into normalized requirement units.

Assign stable internal requirement IDs where official IDs are absent.

## Phase 4 — Deep Analysis (Senior QA)

This is the most critical phase. Apply the full analysis checklist from `rules/02-requirement-analysis.md`.

For each requirement identify:
- actor;
- preconditions;
- action;
- input;
- rules;
- expected result;
- constraints;
- dependencies;
- risk.

### 4a. Entity-State Mapping

Identify all entities and their possible states:

```text
Entity: Standard Prescription
  States: ON, OFF
  Attributes: quota, coverage, limit, frequency, fee

Entity: Specialist Prescription
  States: ON, OFF
  Attributes: quota, coverage, limit, frequency, fee

Context: Consultation Type
  Values: GP, SP
```

### 4b. Decision Table Construction

Build a decision table from all independent conditions:

| # | Condition 1 | Condition 2 | Context | Expected Behavior |
|---|---|---|---|---|
| 1 | ON | OFF | GP | ... |
| 2 | ON | OFF | SP | ... |
| ... | ... | ... | ... | ... |

### 4c. Cross-Feature Impact Map

Identify which existing features are affected and which are explicitly unaffected.

### 4d. Backward Compatibility Assessment

Determine if the PRD modifies existing features and what migration/preservation guarantees exist.

### 4e. Gap Identification

List requirements that are:
- ambiguous;
- incomplete;
- contradictory;
- missing error handling;
- missing boundary definition.

## Phase 5 — Test Design

Select applicable techniques based on the analysis:

| Requirement Pattern | Technique |
|---|---|
| Independent ON/OFF settings | Decision Tables |
| Numeric limits | Boundary Value Analysis |
| Parallel similar features | Data Isolation |
| Feature enhancement | Backward Compatibility |
| Unaffected features | Non-Impact Verification |
| Configurable settings | Configuration Persistence |
| Multi-step workflow | End-to-End |

Do not apply techniques mechanically. Select based on the structure and risk of each requirement.

## Phase 6 — Candidate Generation

Generate candidate test cases following the PLM-659 patterns.

Each candidate must contain:
- summary (title in `[TC][{TICKET}] ...` format);
- description;
- requirement keys (PRD ticket ID);
- precondition (precise state description);
- steps (each with step description, step data, expected result);
- priority;
- reporter;
- test category;
- folder.

### Coverage Targets

Ensure candidates cover ALL dimensions:
1. **Configuration**: Can each feature be configured independently?
2. **State combinations**: All meaningful ON/OFF × context combinations.
3. **Negative/ineligibility**: What happens when a feature is OFF for a given context?
4. **Data isolation**: Do parallel features operate independently?
5. **Data lifecycle**: Create → store → retrieve → consume → update → state-change.
6. **Backward compatibility**: Pre-enhancement data preserved?
7. **Non-impact**: Explicitly unaffected features verified?

## Phase 7 — Deduplication

Compare candidates.

Remove:
- exact duplicates;
- semantic duplicates;
- redundant cases covering the same condition and outcome.

Keep cases that cover materially different risks.

## Phase 8 — Coverage Review

Build the internal requirement-to-test matrix.

Verify the coverage completeness checklist from `rules/05-coverage-rules.md`.

Identify:
- covered requirements;
- uncovered requirements;
- ambiguous requirements;
- unsupported scenarios.

**If any coverage dimension is missing, go back to Phase 6 and add the missing test cases.**

## Phase 9 — Quality Validation

Apply `rules/09-validation-rules.md`.

Do not trust the generator's own claim that its output is correct.

## Phase 10 — Template Mapping

Map the logical test cases into the XLSX template:

1. Create sheet `Tests`.
2. Write the 20-column header row.
3. For each test case:
   a. Write Step 1 row with all metadata columns + step data.
   b. Write Step 2+ rows with only Step Description, Step Data, Expected Result.
4. Leave optional columns empty when not applicable.

## Phase 11 — XLSX Generation

Generate the XLSX file using `openpyxl`:

1. Create workbook with sheet `Tests`.
2. Write header row with all 20 columns.
3. Write test case rows following the multi-step convention.
4. Apply formatting (Arial 10pt, text wrapping, column widths).
5. Save to `output/{TICKET}.xlsx`.

## Phase 12 — XLSX Validation

Validate the generated XLSX:
- Open the file and verify it is not corrupt.
- Verify header matches template.
- Verify multi-step grouping is correct.
- Verify no misaligned or truncated rows.
- Verify text cells are not converted to numbers/dates.

## Phase 13 — Final Output

Return the generated XLSX file.

Provide a concise summary of:
- total test cases;
- total test steps;
- coverage dimensions addressed;
- coverage gaps (if any);
- ambiguities (if any);
- assumptions (if any);
- validation issues (if any).

Never put analysis into the XLSX itself.

## Mandatory Workflow Gates

The following gates apply to the phases above and take precedence over generic checklist wording.

### Gate A — Source and Requirement Completeness (after Phase 3)

Do not start test design until:
- every source is inventoried as processed, duplicate, superseded, unreadable, or conflicting;
- every atomic requirement, acceptance criterion, business-rule row, explicit exception, and non-impact statement has a stable ID and source evidence;
- each item is classified `EXPLICIT`, `DERIVED`, `ASSUMPTION`, or `UNKNOWN`;
- conflicts and unreadable content are recorded.

### Gate B — Scope and Test-Condition Readiness (after Phase 5)

Create the scope model, applicability matrix, test-condition inventory, risk assessment, and required decision/state models from `rules/11-scope-model-and-coverage-closure.md`.

For each dimension, record `APPLICABLE`, `NOT APPLICABLE`, or `BLOCKED` with rationale. For every condition, identify its requirement IDs, technique, risk, and expected-result oracle. Do not proceed with a condition whose oracle is unknown.

### Gate C — Combination Closure (before Phase 6)

Confirm that:
- every feasible, outcome-distinct decision-table row is selected;
- every documented state and valid transition is selected;
- impossible combinations cite source evidence;
- reduced combinatorial suites state the technique and do not claim exhaustive coverage;
- explicit compatibility, migration, non-impact, negative, and integration-error promises have conditions.

### Gate D — Candidate Traceability and Deduplication (Phases 6–8)

Each candidate Description must include `Coverage: <REQ IDs> / <COND IDs>`. Build the bidirectional coverage matrix and semantic signature defined in Rule 11.

A candidate may be consolidated only if the retained test clearly proves all mapped outcomes under compatible preconditions. Preserve all mapped condition IDs. Remove orphan cases that have no authoritative basis.

Do not map cases to XLSX while any requirement/condition has a blank disposition.

### Gate E — Adversarial Validation (Phases 9–12)

Review the suite independently from the generator's candidate list. Re-read source evidence and actively search for:
- missed requirements, table rows, footnotes, screenshot states, and exceptions;
- unsupported expected results;
- untested state/decision rows;
- silent `NOT APPLICABLE` claims;
- contradictory cases and semantic duplicates;
- missing continuation-row rules or stale reference columns.

Apply the validation workflow and closure decision. Fix failed cases or coverage gaps before writing the final workbook.

### Final Reporting Requirement

Always report, even when the user requests only XLSX:
- case and step counts;
- requirements/conditions covered;
- reduction methods and exclusions;
- unresolved ambiguities, blockers, conflicts, and assumptions;
- closure result: `PASS`, `PASS WITH WARNINGS`, or `FAIL`.

Do not describe a suite with blocked critical scope as complete.
