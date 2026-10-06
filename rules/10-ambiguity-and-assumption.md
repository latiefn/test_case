# Ambiguity and Assumption Rules

## 1. Principle

Do not invent missing product behavior.

## 2. Ambiguity Types

- `MISSING_REQUIREMENT` — required behavior is absent.
- `AMBIGUOUS_REQUIREMENT` — multiple reasonable interpretations exist.
- `CONFLICTING_REQUIREMENT` — sources disagree.
- `UNDEFINED_BOUNDARY` — a limit is referenced but not defined.
- `UNDEFINED_EXPECTED_RESULT` — action is described without an observable oracle.
- `UNDEFINED_ERROR_BEHAVIOR` — failure is possible but response is unspecified.

## 3. Handling

Create a local blocker for the affected requirement/condition.

Continue generating all independent supported cases.

Do not stop the entire ticket because one requirement is blocked unless the blocker prevents the core flow or the output contract.

## 4. Assumptions

Use assumptions only when the user or an explicit project rule permits them.

Label assumptions clearly and never write them as product facts.

## 5. Clarification Questions

Ask only questions that change:
- expected behavior;
- testability;
- coverage closure; or
- output validity.

Do not ask for information that does not affect generated cases.
