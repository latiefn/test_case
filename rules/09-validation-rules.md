# Test Case Validation Rules

Validation is a separate quality gate from generation.

## 1. Always Validate

Check:
- traceability;
- unsupported/invented behavior;
- executable steps;
- observable expected results;
- English-only test case text (except source-defined literal strings quoted verbatim);
- duplicate cases;
- priority validity;
- required template fields;
- XLSX structure;
- multi-step row convention.

## 2. Conditional Validation

Re-check the following only when the generation used them:
- decision-table closure;
- state-transition closure;
- pairwise reduction;
- lifecycle coverage;
- regression/non-impact coverage;
- integration-specific claims;
- ambiguity resolution.

## 3. Hallucination Detection

Flag:
- unsupported limits;
- unsupported messages;
- unsupported status codes;
- unsupported UI elements;
- unsupported roles/permissions;
- unsupported behavior.

## 4. Duplicate Detection

Detect:
- exact duplicates;
- same scenario with wording changes;
- same behavior/outcome with equivalent conditions.

Keep separate only when risk, state, outcome, or failure diagnosis materially differs.

## 4a. Granularity Check

Flag any case that verifies more than one independent outcome — for example a case whose steps test cancel, save, and sync as separate conditions. Apply the independence test from `rules/04-test-case-rules.md` §7: if a later step remains meaningfully testable after an earlier step fails, the case must be split.

## 5. Requirement Coverage

Every requirement must be `COVERED`, `CONSOLIDATED`, `BLOCKED`, or `NOT APPLICABLE`.

A blocked local requirement does not fail the whole ticket unless it affects the core flow or required output contract.

## 6. XLSX Validation

Verify:
- workbook opens;
- sheet is `Tests`;
- current template header/order match;
- row alignment is correct;
- required fields are populated;
- step 2+ rows contain only step fields;
- text values are preserved.

## 7. Quality Gate

`PASS` — no critical issues.

`PASS WITH WARNINGS` — supported output exists but ambiguity/non-critical gaps remain.

`FAIL` — critical traceability, hallucination, schema, corruption, or major coverage issue remains.

When fixing failures, repair only affected cases where possible.
