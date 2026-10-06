# Template Rules

## 1. Authority and Scope

`template/Test Case template.xlsx` is authoritative for the **physical XLSX import structure**: worksheet, current columns, column order, and explicit allowed-value notes. It is not a source of product behavior.

Apply the source-of-truth order in `AGENTS.md`. A current user instruction may intentionally override the template; report the deviation and validate against the requested target.

## 2. Current Template Structure

At the time this rule was updated, the current template has:
- Sheet name: `Tests`
- Row 1: 20 column headers
- No merged cells
- Multi-step test cases spanning consecutive rows

Inspect the actual workbook on every generation run. Fail fast if its structure differs from the documented contract; do not silently generate from a stale hardcoded header.

### Column List (20 Columns)

| # | Column | Notes |
|---|---|---|
| 1 | Key | Jira issue key; empty for new test cases |
| 2 | Summary | Test case title |
| 3 | Description | Purpose plus internal coverage IDs |
| 4 | Requirement Keys | Existing PRD/Jira ticket ID |
| 5 | Test Type | `Manual` / `Automated`; optional |
| 6 | Automation Content | Only when Test Type = `Automated`; optional |
| 7 | Epic Key | Jira epic; optional |
| 8 | Fix Versions | Comma-separated; optional |
| 9 | Status | Leave empty for new cases |
| 10 | Priority | `High` / `Medium` / `Low` |
| 11 | Assignee | Optional |
| 12 | Reporter | Author name or valid Jira identity |
| 13 | Labels | Comma-separated, no spaces within labels; optional |
| 14 | Test Category | Current template allows `Manual` / `Automated` |
| 15 | Components | Comma-separated; optional |
| 16 | Precondition | State/setup required before execution |
| 17 | Folder | Organizational path |
| 18 | Step Description | Test-step action |
| 19 | Step Data | Input data; optional |
| 20 | Expected Result | Observable expected outcome |

The template's rows 2 and later are instructional/sample records. Never copy them into generated output. Use them only to understand import notes and permitted values.

## 3. Multi-Step Row Layout

When a test case has multiple steps:
- **Step 1 row**: populate applicable metadata plus Step Description, Step Data, and Expected Result.
- **Step 2+ rows**: populate only Step Description, Step Data, and Expected Result. All metadata cells must be truly empty.

A new test case starts when `Summary` is non-empty.

## 4. Preserve Current Structure

Do not rename, reorder, remove, or add columns unless explicitly instructed. In particular, do not copy the older 18-column structure from `PLM-659.xlsx`; the current template includes `Test Type` and `Automation Content`.

## 5. Field Mapping

Map the logical schema to the inspected current template. Leave a field empty when it is optional and no authoritative value exists. Do not fabricate metadata merely to fill a column.

Use values accepted by the current template/project configuration:
- `Test Type`: `Manual` or `Automated` when populated.
- `Test Category`: `Manual` or `Automated` under the current template contract.
- Do not use the older reference value `Functional` unless the user confirms that the target Jira project accepts it.

## 6. Reference File Boundary

`template/PLM-659.xlsx` is an older 18-column artifact. Use it only for content patterns such as descriptive summaries, precise preconditions, observable expected results, coherent multi-step layout, and scenario granularity.

Do not copy from the reference:
- its header or column count;
- old field values that conflict with the current template;
- its folder whitespace;
- its ticket-specific behavior as if it were a general product rule.

## 7. Folder and Missing Metadata

Folder format is `{Year}/{Year} Sprint {N}/{TICKET}` with no extra space after `/`.

Year, sprint, reporter, Jira identities, versions, components, and other project metadata must come from the user or stable project context. If a required value is unavailable, ask for it or report the output as blocked; do not choose a “reasonable default.”

## 8. Runtime Conflict Check

Before writing output, compare:
1. actual current-template headers and import notes;
2. documented schema/rules;
3. requested target project conventions.

Report conflicts before generation. Current-template structure wins over the older reference unless the user explicitly targets another format.
