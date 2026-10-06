# Logical Test Case Schema

This schema describes a logical test case before it is mapped to the physical XLSX template.

## XLSX Template Columns (Physical)

The current template (`template/Test Case template.xlsx`) defines these 20 columns. Inspect it at run time and stop if it has changed.

| # | Column | Required by this project | Description |
|---|---|---|---|
| 1 | Key | No | Jira issue key for updating an existing case; empty for a new case. |
| 2 | Summary | **Yes** | `[TC][{TICKET}] {Description}`. |
| 3 | Description | **Yes** | Objective plus internal coverage IDs, for example `Coverage: REQ-001 / COND-003`. |
| 4 | Requirement Keys | **Yes** | Existing official PRD/Jira ticket ID. |
| 5 | Test Type | No | `Manual` or `Automated`. |
| 6 | Automation Content | Conditional | Required only when the target import requires it for an `Automated` case. |
| 7 | Epic Key | No | Existing Jira epic key when supplied. |
| 8 | Fix Versions | No | Existing version value(s) when supplied. |
| 9 | Status | No | Empty for new cases unless explicitly requested. |
| 10 | Priority | **Yes** | `High`, `Medium`, or `Low`. |
| 11 | Assignee | No | Existing Jira identity when supplied. |
| 12 | Reporter | **Yes** | Known author/Jira identity. |
| 13 | Labels | No | Comma-separated labels without spaces inside each label. |
| 14 | Test Category | **Yes** | `Manual` or `Automated` under the current template contract. |
| 15 | Components | No | Existing Jira components when supplied. |
| 16 | Precondition | **Yes** | Required system/data state, not execution actions. |
| 17 | Folder | **Yes** | `{Year}/{Year} Sprint {N}/{TICKET}`. |
| 18 | Step Description | **Yes** | One executable action per step where practical. |
| 19 | Step Data | No | Specific input or descriptive placeholder. |
| 20 | Expected Result | **Yes** | Observable outcome backed by a test oracle. |

The generic workbook note says only Summary is universally required by the importer. This repository intentionally defines additional quality-required fields above. Target Jira custom-field requirements may add further obligations and must be confirmed rather than invented.

## Multi-Step Row Layout

Each test case may span multiple XLSX rows:

```text
Row N   (Step 1): Applicable metadata + Step Description + Step Data + Expected Result
Row N+1 (Step 2): Only Step Description + Step Data + Expected Result
Row N+2 (Step 3): Only Step Description + Step Data + Expected Result
...
```

A new case starts when `Summary` is non-empty. Continuation-row metadata cells must be truly empty.

## Logical Test Case Fields

### test_case_id
Internal generation identifier. Do not write it to XLSX `Key` for a new test case.

### summary
`[TC][{TICKET}] {specific behavior, context, and expected direction}`.

### description
State the objective and atomic traceability, including `Coverage: <requirement ID(s)> / <condition ID(s)>`. If a case consolidates multiple conditions, list all IDs.

### requirement_keys
The official PRD/Jira ticket ID. Internal `REQ-###` IDs belong in Description and the coverage matrix, not this field.

### test_type
Optional `Manual` or `Automated`. Do not mark a case automated without actual automation evidence/content.

### automation_content
Automation script, path, or link only for an automated case and only when supplied or created as part of the task.

### priority
Risk-based `High`, `Medium`, or `Low` with evidence in the internal risk assessment; High cases require a clear basis.

### reporter
Known test-case author/Jira identity. Do not invent one.

### test_category
`Manual` or `Automated` under the current template contract. An older reference value such as `Functional` requires explicit target-project confirmation.

### precondition
The actor, data, configuration, and system state required before execution. Do not place imperative actions here.

### folder
Exact target path `{Year}/{Year} Sprint {N}/{TICKET}` with no extra space after `/`. Do not invent the year or sprint.

### steps[]
Ordered steps containing:
- `step_description` — executable action;
- `step_data` — specific input when applicable;
- `expected_result` — observable result supported by an oracle.

## Optional Fields

Depending on project needs:
- Key
- Test Type
- Automation Content
- Epic Key
- Fix Versions
- Status
- Assignee
- Labels
- Components

## Mapping Principle

The logical schema is independent of the physical output template.

Never change QA semantics merely because a template uses different column names.

Map the logical fields to the template during output generation.
