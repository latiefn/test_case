# Ambiguity and Assumption Rules

## 1. Principle

When the requirement is incomplete, ambiguous, or contradictory, do not invent the missing behavior.

## 2. Ambiguity Types

Classify ambiguity as:

### Missing Requirement
Required behavior is not specified.

### Ambiguous Requirement
The wording permits multiple reasonable interpretations.

### Conflicting Requirement
Two sources specify different behavior.

### Undefined Boundary
A limit is referenced but its value is absent.

### Undefined Expected Result
An action is described but the expected outcome is not defined.

### Undefined Error Behavior
Failure is possible but the system response is unspecified.

## 3. Assumptions

Do not convert assumptions into product facts.

If assumptions are permitted by the user:
- label them explicitly;
- explain their source;
- avoid making them look like requirements.

## 4. Clarification

If clarification is necessary for correct test generation, identify the exact question.

Bad:
`Requirement unclear.`

Good:
`Should an input value of exactly 60 be accepted, rejected, or is the upper boundary unspecified?`

## 5. Test Case Generation Under Ambiguity

Generate only the portion that is supported by the requirement.

Do not generate expected results based on common industry behavior unless the user explicitly asks for assumption-based test design.

## 6. Conflicting Sources

Record:
- source A;
- source B;
- conflicting statements;
- impact on test design.

Do not silently select one.

## 7. Assumption Tracking

If the project permits assumptions, maintain:

`ASSUMPTION-001`

with:
- assumption;
- affected requirement;
- affected test cases;
- reason.

## 8. Final Behavior

A test case must never disguise an assumption as an explicit requirement.

## 9. Mandatory Ambiguity and Blocker Log

Maintain an entry for every unresolved issue:

`ID | Type | Source/location | Affected requirement/condition | Competing interpretations or missing fact | Test impact | Exact clarification question | Status`

Use stable IDs such as `AMB-001`, `CONFLICT-001`, and `BLOCKER-001`.

## 10. Mandatory Disclosure

Unresolved ambiguities, conflicts, blockers, assumptions, unreadable source areas, and intentionally excluded combinations must always be disclosed in the final response, even when the user requests only the XLSX. They must never exist only in private reasoning.

Do not claim complete coverage when a critical condition lacks an oracle. Use the closure status rules in `11-scope-model-and-coverage-closure.md`.

## 11. Clarification Timing

Ask before generation when the missing answer changes a critical expected result, scope boundary, required metadata, or combination model. If supported work can continue independently, generate only that supported portion and clearly mark the blocked conditions; do not wait silently or fill the gap with assumptions.
