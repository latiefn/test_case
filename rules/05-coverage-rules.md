# Coverage Rules

A Senior QA designs for complete, meaningful coverage — not just happy paths. The test suite must cover all dimensions of the requirement space.

## 1. Coverage Objective

Coverage means meaningful verification of documented behavior, not the number of test cases.

## 2. Requirement Coverage

Every testable requirement should map to at least one test case.

A requirement may map to multiple cases when it contains:
- multiple equivalence classes;
- boundaries;
- multiple roles;
- multiple states;
- multiple decision combinations;
- meaningful negative paths.

## 3. Coverage Dimensions

A Senior QA evaluates ALL applicable dimensions for every PRD:

### 3a. Functional Coverage
- Happy path: Does the feature work as described?
- Alternate path: Are there alternative valid ways to achieve the same result?

### 3b. Configuration Coverage
- Can all settings be configured independently?
- Do configured values persist after save?
- Do configured values persist after modification?

### 3c. State Combination Coverage
- All meaningful ON/OFF, active/inactive combinations tested?
- Use decision tables to systematically enumerate.

### 3d. Negative / Ineligibility Coverage
- What happens when the feature is disabled/inactive?
- What happens when the user/context is not eligible?
- What happens with invalid input?

### 3e. Data Isolation Coverage
- Do parallel/similar features operate independently?
- Does configuring one affect the other?
- Does consuming one affect the other's quota/limits?

### 3f. Data Lifecycle Coverage
- Creation, storage, retrieval, consumption, update, state-change scenarios.

### 3g. Backward Compatibility Coverage
- Do pre-existing data and configurations continue to work?
- Is migration/upgrade handled correctly?

### 3h. Non-Impact Coverage
- Are explicitly unaffected features verified as unchanged?

### 3i. Boundary Coverage
- Are explicit numeric/value limits tested at boundaries?

### 3j. Integration Coverage
- Do integration points work correctly in all relevant states?

### 3k. Error Handling Coverage
- Are documented error conditions tested?

## 4. Risk Coverage

Give additional attention to:
- core business flows;
- transactional behavior;
- authentication;
- authorization;
- data integrity;
- critical integrations;
- regulatory requirements;
- high-impact failure paths.

Risk classification must be based on documented business impact or explicit project context.

## 5. Coverage Matrix

Before generating test cases, build an internal coverage matrix:

| Requirement | Dimension | Scenario | Test Case | Status |
|---|---|---|---|---|
| REQ-001 | Configuration | Both benefits configurable | TC-001 | Covered |
| REQ-001 | State Combo | ON+OFF, GP context | TC-003 | Covered |
| REQ-001 | Data Isolation | Quota independence | TC-011 | Covered |
| REQ-001 | Backward Compat | Pre-enhancement data | TC-013 | Covered |
| REQ-001 | Non-Impact | Telemedicine unchanged | TC-014 | Covered |

Verify every cell is covered before finalizing.

## 6. Coverage Completeness Checklist

Before declaring the test suite complete, verify:

- [ ] All explicit requirements have at least one test case.
- [ ] All state combinations are covered (decision table complete).
- [ ] Negative/ineligibility scenarios are covered for each context.
- [ ] Data isolation is verified for parallel features.
- [ ] Configuration persistence is tested (save → reopen → verify).
- [ ] Backward compatibility is tested if the PRD modifies existing features.
- [ ] Non-impact verification is included if the PRD guarantees unchanged features.
- [ ] Boundary values are tested for explicit numeric limits.
- [ ] No duplicate test cases exist.
- [ ] No test case is untraceable.

## 7. Uncovered Requirements

If a requirement cannot be tested because required information is missing:
- identify it;
- explain the missing information;
- do not invent a test expectation.

## 8. Redundant Coverage

If multiple cases test the same equivalence class and produce the same observable behavior, consolidate them.

## 9. Coverage Summary

Before final output, internally determine:
- total testable requirements;
- covered requirements;
- uncovered requirements;
- ambiguous requirements;
- duplicate candidates removed;
- coverage dimensions addressed.

The summary does not necessarily need to be included in the XLSX unless the template provides a suitable field.

## 10. Applicability Matrix

For every feature or atomic requirement, assess each coverage dimension as:
- `APPLICABLE` — create conditions and map them to tests;
- `NOT APPLICABLE` — record why the dimension does not exist for this requirement;
- `BLOCKED` — identify the missing oracle, setup, data, or clarification.

A silent omission is a coverage gap. “When applicable” is not permission to skip analysis.

In addition to the dimensions above, assess documented roles/permissions, workflow sequencing, CRUD/lifecycle operations, interface contracts, concurrency/idempotency, and explicit quality attributes. These dimensions create tests only when supported by requirements or stable project context.

## 11. Bidirectional Traceability

The coverage matrix is mandatory, even when it is not included in the XLSX. It must map every atomic requirement and test condition to one or more test cases, and every test case back to supported evidence.

Use the dispositions and fields defined in `11-scope-model-and-coverage-closure.md`. Any explicit testable requirement with no disposition is a critical gap. Any case with no supported requirement or condition is an orphan and must be removed or justified by an explicit project rule.

Include internal IDs in each test Description using `Coverage: REQ-### / COND-###` while keeping `Requirement Keys` equal to the official ticket key.

## 12. Combination and Transition Closure

For each decision table:
- map every feasible, outcome-distinct row to at least one test case;
- mark impossible rows and cite the rule that excludes them;
- document any combinatorial reduction and never label reduced coverage as exhaustive.

For each state model, map every documented state and valid transition. Invalid-transition cases require a supported prohibition or outcome.

## 13. Duplicate Signature

Compare candidates using:

`requirement/condition | actor/context | state | input partition | trigger/action | expected outcome | risk`

Equivalent signatures are duplicates unless a material platform, boundary, transition, integration, or risk difference exists. Record consolidated candidates in the coverage matrix rather than silently deleting traceability.

## 14. Closure Decision

Apply the closure gate in `11-scope-model-and-coverage-closure.md`.

- `PASS`: all documented testable scope is covered and no critical gap remains.
- `PASS WITH WARNINGS`: supported scope is covered, but explicitly reported source ambiguity or unavailable setup blocks non-critical confirmation.
- `FAIL`: an explicit critical requirement, feasible decision row, applicable dimension, valid transition, oracle, or structural requirement is missing or unsupported.

Do not use raw test count as evidence. If multiple requirements map to one test, confirm that the test proves each result clearly and remains diagnosable.
