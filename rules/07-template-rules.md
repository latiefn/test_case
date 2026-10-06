# Template Rules

`template/Test Case template.xlsx` is the authoritative physical XLSX contract.

## Runtime Inspection

Inspect the current workbook at generation time.

If sheet name, column count, order, or allowed values differ from this repository documentation, use the actual template as authority and report the deviation.

## Current Contract

The current template uses sheet `Tests` with 20 columns:

`Key | Summary | Description | Requirement Keys | Test Type | Automation Content | Epic Key | Fix Versions | Status | Priority | Assignee | Reporter | Labels | Test Category | Components | Precondition | Folder | Step Description | Step Data | Expected Result`

## Multi-Step Convention

- Step 1 row contains case metadata plus step fields.
- Step 2+ rows contain only Step Description, Step Data, and Expected Result.
- A new test case starts at a non-empty Summary cell.

Never use the older `PLM-659.xlsx` header as the current structure.
