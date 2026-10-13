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

Prefer `openpyxl` over hand-building XLSX XML. If `openpyxl` is unavailable, tell the user and offer options before proceeding — do not silently fall back to CSV when Excel was requested.

### Isolated environment (pinned version)

Set up a venv with a pinned openpyxl so the build is reproducible and the system interpreter is untouched:

```bash
python3 -m venv ~/.venv-tc-xlsx
~/.venv-tc-xlsx/bin/python -m pip install "openpyxl==3.1.5"
```

A venv avoids the PEP 668 "externally managed environment" error that blocks installing into a Homebrew Python. Mention that the venv can be removed afterwards.

### Formatting-preserving approach

Build from the current template so column widths, header fill, fonts, and wrap settings are inherited rather than reconstructed:

1. `shutil.copyfile(template, destination)` — copy `template/Test Case template.xlsx` to `output/{TICKET}.xlsx`, inheriting all styling.
2. Load the copy, then clear values from row 2 downward while leaving styling intact (`cell.value = None`; do **not** delete rows). Do not copy sample/instruction rows from the template.
3. Write the new rows, applying the template's body style: Calibri 11, `wrap_text=True`, `vertical='center'` (the Precondition column also uses `horizontal='left'`).
4. Save to `output/{TICKET}.xlsx`.

Keep the `generate.py` used for the build under `work/{TICKET}/` as a working artifact, and clean up any temporary throwaway scripts when finished.

Validate the workbook after saving (see `workflow/validation-workflow.md`).
