# XLSX Output Rules

## Output

Write one workbook to:
`output/{TICKET}.xlsx`

Use sheet `Tests` and the exact current template columns/order.

## Multi-Step Rows

Step 1:
- populate applicable metadata;
- populate the first step.

Step 2+:
- populate only Step Description, Step Data, Expected Result;
- leave metadata empty.

## Values

Preserve textual IDs/codes as text.

Leave non-applicable optional fields empty. Do not insert arbitrary `N/A`, `TBD`, or `Unknown` unless the template/project explicitly permits them.

Do not copy sample/instruction rows from the template.

## Generation

Use a reliable workbook library such as `openpyxl`.

Validate the workbook after saving.
