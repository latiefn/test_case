# Test Case Validation Rules

Validation must be treated as a separate quality gate from generation.

## 1. Requirement Validation

Check:
- Is every test case traceable via Requirement Keys?
- Is the referenced requirement (PRD ticket) real?
- Does the case actually test the requirement?
- Was unsupported behavior introduced?

## 2. Test Case Validation

For every case:
- Summary follows `[TC][{TICKET}] ...` format;
- Description is specific;
- Preconditions are valid (not actions);
- Steps are executable;
- Expected results are observable;
- Step data is appropriate;
- Priority follows project rules (`High`/`Medium`/`Low`);
- No unrelated behavior is combined;
- Reporter is populated;
- Test Category is populated;
- Folder follows convention.

## 3. Multi-Step Validation

For multi-step test cases:
- Step 1 row has every project-required metadata value and any applicable optional metadata;
- Step 2+ rows have ONLY Step Description, Step Data, Expected Result;
- No metadata is duplicated on step 2+ rows;
- Steps are in logical sequence;
- A continuation row never appears before a Summary row.

## 4. Duplicate Validation

Identify duplicates and near-duplicates based on:
- same requirement;
- same condition;
- same action;
- same expected result.

Remove redundant cases unless there is a documented reason to keep them.

## 5. Coverage Validation

Check applicable:
- positive;
- negative;
- boundary;
- equivalence classes;
- decision combinations;
- state transitions;
- roles/permissions;
- error handling;
- integrations.

## 6. Hallucination Detection

Flag any test case containing:
- undocumented error message;
- undocumented limit;
- undocumented role;
- undocumented API status;
- undocumented UI element;
- undocumented default;
- undocumented behavior.

Such cases must be corrected or removed.

## 7. Contradiction Detection

Look for test cases whose expected results conflict with each other.

If the conflict originates in requirements, mark the source requirement conflict rather than choosing an interpretation silently.

## 8. Template Validation

Check:
- Sheet name is `Tests`;
- Exact 20-column header;
- Exact column order;
- Required fields populated;
- Allowed values;
- Multi-step convention followed.

## 9. XLSX Validation

Open the final XLSX and verify:
- the workbook opens without corruption;
- the header row matches the template exactly;
- every row aligns to the correct columns;
- no row is misaligned or truncated;
- text-formatted cells were not silently converted to numbers or dates;
- multi-step grouping is correct.

## 10. Quality Gate

Do not declare generation complete if critical validation failures remain.

Critical failures include:
- untraceable test cases;
- invented product behavior;
- corrupt or malformed XLSX;
- missing required template fields;
- major requirement gaps;
- wrong Summary format;
- metadata on step 2+ rows.

## 11. Validation Output

If the user requests only the final XLSX, keep validation details outside the XLSX unless the template explicitly provides a validation field.

If the user requests analysis, provide:
- coverage gaps;
- ambiguities;
- duplicate removals;
- validation failures;
- assumptions.

## 12. Mandatory Coverage Evidence

Validate using the artifacts in `11-scope-model-and-coverage-closure.md`. A ticket-level Requirement Keys value alone is not sufficient atomic traceability.

Check:
- every source and atomic requirement has a disposition;
- every test Description contains mapped requirement/condition IDs;
- every feasible decision row and documented valid transition is covered;
- every applicable dimension is covered;
- `NOT APPLICABLE`, `BLOCKED`, impossible-row, and reduction decisions include evidence;
- every expected result has an authoritative or explicitly approved oracle;
- every case traces back to evidence in the reverse direction.

Missing mandatory evidence is a validation failure, not an optional documentation issue.

## 13. Semantic Duplicate Validation

Use the normalized signature from Rule 11. Similar titles may cover different risks; different titles may be duplicates. Consolidation is valid only when retained steps and expected results visibly prove every mapped condition.

## 14. Critical Scope Failures

In addition to Section 10, classify these as critical:
- explicit testable requirement or acceptance criterion has no disposition;
- applicable coverage dimension has no condition/case;
- feasible outcome-distinct decision row is unmapped;
- documented valid transition is unmapped;
- explicit non-impact, migration, compatibility, or defined error behavior is missed;
- test expectation has no oracle or contains an unauthorized assumption;
- orphan test has no supported source;
- unresolved contradiction causes mutually incompatible expected results;
- current-template structure is replaced by the old reference structure.

## 15. Current Template and Metadata Checks

The current template has 20 columns. Treat PLM-659 as an older 18-column content reference only.

Verify:
- current header includes `Test Type` and `Automation Content`;
- `Test Category` is `Manual` or `Automated` unless target-project support for another value is confirmed;
- `Functional` was not copied merely from PLM-659;
- required year, sprint, reporter, Jira keys, versions, components, or identities were not invented;
- Folder is internally consistent and follows `{Year}/{Year} Sprint {N}/{TICKET}` without an extra space;
- template instructional/sample rows are absent.

## 16. Independent Review Mindset

Validation must challenge the generator's interpretation. Revisit source evidence instead of validating only internal consistency. Search specifically for missed tables, footnotes, screenshot states, exceptions, precedence rules, and “existing/retain/unchanged/not affected” statements.
