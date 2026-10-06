# XLSX Output Rules

## 1. Format

The primary output is an XLSX workbook (`.xlsx`).

Write a single worksheet named `Tests`.

## 2. Output File Naming

Output file: `output/{TICKET}.xlsx`

Example: `output/PLM-1003.xlsx`

## 3. Header

Row 1 must contain the exact template header columns in order:

`Key | Summary | Description | Requirement Keys | Test Type | Automation Content | Epic Key | Fix Versions | Status | Priority | Assignee | Reporter | Labels | Test Category | Components | Precondition | Folder | Step Description | Step Data | Expected Result`

Use all 20 columns from the template, even if some columns are left empty for all rows.

## 4. Multi-Step Row Convention

Each test case occupies one or more consecutive rows:

- **Step 1 row**: Populate metadata columns (Summary, Description, Requirement Keys, Priority, Reporter, Test Category, Precondition, Folder) and the first step (Step Description, Step Data, Expected Result).
- **Step 2+ rows**: Populate ONLY Step Description, Step Data, and Expected Result. Leave all metadata columns empty.

A new test case is identified by a non-empty `Summary` cell.

## 5. Cell Values

Write each field into its own cell.

Because XLSX stores values in discrete cells, no delimiter, field separator, or quoting is required or applied.

## 6. Text and Line Breaks

Preserve text exactly as written, including commas and quotation marks, without escaping.

If a field must contain multiple lines, store the line breaks within the single cell rather than splitting across columns.

## 7. Data Types

Preserve values that must remain textual (for example, ticket IDs or codes with leading characters) as text cells so they are not reformatted as numbers or dates.

## 8. No Markdown or Analysis

The XLSX file must not contain:
- Markdown tables;
- code fences;
- explanatory paragraphs;
- analysis text.

## 9. Column Consistency

Every data row must align to the same columns as the header. Do not shift values into the wrong column.

## 10. Empty Values

Leave a cell empty when there is no applicable value.

Do not use arbitrary strings such as:
- N/A;
- Unknown;
- TBD;

unless the template or project rules explicitly allow them.

## 11. Columns Left Empty for New Test Cases

For newly generated test cases, leave these columns empty:
- Key (no existing Jira key)
- Test Type (unless specified)
- Automation Content (unless automated)
- Epic Key (unless specified by user)
- Fix Versions (unless specified by user)
- Status (filled during execution)
- Assignee (unless specified by user)
- Labels (unless specified by user)
- Components (unless specified by user)

## 12. XLSX Generation

Use a workbook library that preserves text values and styles reliably; `openpyxl` is the default supported implementation.

Before writing:
- inspect `template/Test Case template.xlsx` at run time;
- assert sheet `Tests` and the exact current 20-column header;
- discard all instructional/sample rows from the template;
- do not copy the older 18-column header from `PLM-659.xlsx`.

For generated cases:
- use Arial 10pt to follow the reference's verified text style;
- use wrap text and practical column widths when they improve readability (these are output formatting choices, not verified PLM-659 structural requirements);
- set `Test Category` to `Manual` or `Automated` under the current template contract;
- keep `Test Type` empty unless known, or match it to the authoritative manual/automated designation;
- include internal `REQ-###` / `COND-###` coverage IDs in Description;
- use one canonical output path, `output/{TICKET}.xlsx`; do not create suffixed variants unless explicitly requested.

## 13. Final Integrity Check

Before declaring completion:
- reopen the generated XLSX;
- verify the header against the actual current template;
- verify every row and test grouping;
- verify continuation rows contain no metadata;
- verify required project fields and current allowed values;
- verify text values were not converted to numbers or dates;
- verify no template sample/instruction row was copied;
- verify the workbook contains exactly the cases approved by the coverage matrix.
