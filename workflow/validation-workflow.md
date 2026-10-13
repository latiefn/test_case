# Test Case Validation Workflow

Validation is a separate quality gate. Prefer deterministic checks where possible.

## Step 1 — Load

Read:
- `schemas/test-case-schema.md`
- relevant validation rules
- current XLSX template
- `work/{TICKET}/coverage.md`
- generated `output/{TICKET}.xlsx`

Load the full generation context only when a semantic dispute cannot be resolved from these artifacts.

## Step 2 — Structural Validation

Re-open the saved `output/{TICKET}.xlsx` and confirm:
- the file opens successfully and the ZIP is intact;
- the sheet name is `Tests`;
- the header row matches the current 20-column template exactly, including fill and wrap;
- column widths carried over from the template;
- no leftover sample/instruction data from the template remains;
- required fields are populated (Requirement Keys, Priority, Reporter, Test Category, Precondition, Folder on every test case);
- the multi-step row convention is correct — metadata appears only on each test case's first row; continuation rows carry only Step Description, Step Data, and Expected Result;
- every step row has both a Step Description and an Expected Result;
- the test-case count and per-test-case step counts match the approved set;
- text values are preserved (IDs/codes kept as text).

## Step 3 — Semantic Validation

Check every test case for:
- traceability;
- unsupported behavior;
- executable steps;
- observable expected results;
- valid priority/category;
- coherent preconditions;
- useful test data.

## Step 4 — Duplicate Validation

Detect exact and semantic duplicates. Remove or consolidate only when behavior, outcome, state, and risk are materially equivalent.

## Step 5 — Conditional Coverage Validation

Re-check only the techniques that were activated during generation:
- boundaries;
- decision tables;
- state transitions;
- pairwise reduction;
- lifecycle;
- regression/non-impact;
- integration;
- concurrency/idempotency.

Do not re-run every coverage dimension for every ticket.

## Step 6 — Hallucination / Contradiction Check

Flag unsupported:
- limits;
- messages;
- statuses;
- roles;
- UI elements;
- system behaviors.

Also check whether expected results conflict with the authoritative requirements.

## Step 7 — Decision

`PASS` — no critical issue.

`PASS WITH WARNINGS` — supported output exists with non-critical ambiguity/gaps.

`FAIL` — critical traceability, hallucination, schema, corruption, or material coverage failure.

## Step 8 — Remediation

Repair only affected cases where possible. Do not regenerate the entire suite unless the defect is systemic.

Write final result to `work/{TICKET}/validation.md`.

## Step 9 — Report and Cleanup

Report a pass/fail summary. If any value in the saved file differs from what was approved, flag it explicitly rather than glossing over it.

Clean up temporary throwaway scripts when finished (keep the `work/{TICKET}/generate.py` artifact), and give the user the **exact absolute file path** of the generated workbook.
