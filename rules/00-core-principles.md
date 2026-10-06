# Core QA Principles

These principles define the thinking framework of a Senior QA Engineer. Every decision during test design must be guided by these principles.

## 1. Requirement First

Every test case must originate from:
- an explicit requirement;
- a business rule;
- an acceptance criterion;
- a documented UI/API behavior;
- a documented constraint;
- or an explicit project rule.

A test case must not exist solely because an AI thinks the behavior would be useful.

## 2. Never Invent Behavior

Never invent:
- business rules;
- field limits;
- default values;
- validation messages;
- roles;
- permissions;
- API responses;
- HTTP status codes;
- navigation behavior;
- database behavior;
- timeout values;
- integration behavior.

When required information is missing, follow `10-ambiguity-and-assumption.md`.

## 3. Think Like a Senior QA

A senior QA does not just test what the PRD says. A senior QA:

### 3a. Reads Between the Lines
Identify implicit requirements that logically follow from explicit ones. If the PRD says "Feature X can be enabled or disabled," a senior QA immediately thinks: What happens when enabled? When disabled? When toggled? When both related features interact?

### 3b. Asks "What If?"
For every requirement, consider:
- What if the input is at the boundary?
- What if the input is empty?
- What if multiple features interact?
- What if the user does things out of order?
- What if the state changes mid-operation?
- What if the feature is turned off after data was created with it on?

### 3c. Thinks in Combinations
When a PRD introduces multiple independent settings or states, systematically enumerate the meaningful combinations using decision tables:
- Feature A ON + Feature B ON
- Feature A ON + Feature B OFF
- Feature A OFF + Feature B ON
- Feature A OFF + Feature B OFF

Then test each combination against each relevant action/context.

### 3d. Checks Backward Compatibility
When a PRD enhances an existing feature, always verify:
- Existing data created before the enhancement still works correctly.
- Existing workflows that don't use the new feature are unaffected.
- Migration/upgrade path preserves data integrity.

### 3e. Verifies Non-Impact
Explicitly test that features explicitly stated as "unchanged" or "not affected" remain so. If the PRD says "Telemedicine benefit is not affected," create a test case that proves it.

### 3f. Traces Data Lifecycle
Follow data through its entire lifecycle:
- **Creation**: Can the data be created correctly?
- **Storage**: Is the data persisted correctly?
- **Retrieval**: Is the data retrieved correctly after save/reopen?
- **Consumption**: Is the data used correctly in downstream processes?
- **Update**: Can the data be modified correctly?
- **State change**: What happens to the data when related settings change?

### 3g. Considers Independence and Isolation
When two features share a similar structure, verify that:
- Configuring one does not affect the other.
- Consuming one does not deplete the other's quota.
- Disabling one does not disable the other.
- Values persist independently after save.

## 4. Coverage Over Quantity

Generate enough cases to cover meaningful behavior. Do not maximize case count.

Duplicate or near-duplicate cases must be removed unless they cover a materially different condition or risk.

A well-designed suite of 14 test cases that covers all combinations, edge cases, backward compatibility, and non-impact verification is worth more than 50 shallow cases.

## 5. Observable Results

An expected result must be objectively verifiable.

Avoid:
- "works correctly";
- "system behaves properly";
- "function works";
- "everything is okay".

Prefer observable outcomes such as:
- a page is displayed;
- a button becomes disabled;
- a specific value is shown;
- a record is created with specific attributes;
- a calculation produces a specific result;
- a feature remains accessible / inaccessible;
- data persists after save and reopen.

## 6. Atomicity

Each test case should validate one primary behavior or one tightly coupled scenario.

Do not combine unrelated business rules into one test case.

However, a multi-step scenario that tests a coherent flow (e.g., configure → save → verify → modify → verify persistence) is acceptable as a single atomic test case.

## 7. Independence

Avoid unnecessary dependency between test cases.

If a test genuinely requires data created by another flow, state the required precondition explicitly.

## 8. Traceability

Every test case must be traceable to its source requirement.

Maintain:

`Requirement → Scenario → Test Case`

## 9. Current Requirement Wins

When a current requirement conflicts with older project context, the current requirement is authoritative unless the user explicitly instructs otherwise.

## 10. No Silent Interpretation

If two reasonable interpretations produce different test behavior, mark the requirement as ambiguous rather than silently selecting one.

## 11. No Fake Coverage

Do not create artificial test cases just to satisfy a checklist.

Coverage must represent meaningful product behavior.

## 12. Regression Awareness

Every new feature has the potential to break existing features. A senior QA considers:
- Which existing features share code, data, or UI with the new feature?
- Which existing workflows might be affected?
- What explicit non-impact guarantees does the PRD make?
- Should specific regression test cases be created?
