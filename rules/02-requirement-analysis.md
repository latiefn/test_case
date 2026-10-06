# Requirement Analysis Rules

## 1. Normalize

Convert each independent behavior into a stable requirement unit.

Use, when available:
- official ID;
- actor;
- precondition/trigger;
- action/event;
- input/data;
- rule/constraint;
- expected outcome;
- dependency;
- source reference.

Create `REQ-###` only when the source has no official ID.

## 2. Split Only Independent Behavior

Split a compound requirement only when its behaviors have different:
- outcomes;
- failure modes;
- prerequisites; or
- test conditions.

Do not split a coherent business flow merely because it contains several UI actions.

## 3. Requirement Classification

Classify only categories evidenced by the source:
- Functional
- Business Rule
- Validation
- UI/Navigation
- Data/Lifecycle
- API/Integration
- Authentication/Authorization
- State Transition
- Error Handling
- Backward Compatibility
- Non-Impact
- Non-Functional

Do not force every requirement into every category.

## 4. Trigger Analysis

For each requirement identify whether any of these triggers exist:
- explicit limit/range/format;
- multiple input classes with different outcomes;
- multiple conditions controlling an outcome;
- documented state or transition;
- role/permission rule;
- persisted/consumed/updated data;
- external/internal integration;
- changed existing behavior or data;
- repeated/parallel/asynchronous action;
- explicit NFR.

Only triggered dimensions require deeper test design.

## 5. Cross-Feature Impact

Assess regression scope only from concrete evidence:
- changed shared entity/data;
- changed workflow/interface;
- documented dependency;
- explicit non-impact statement;
- known project risk.

Do not expand scope from generic possibilities.

## 6. Testability

For each requirement, determine whether setup, action, and observable outcome are defined.

If outcome is missing, classify the affected requirement as `BLOCKED` rather than inventing an oracle.

## 7. Output of Analysis

The working analysis should answer only:
1. What must be tested?
2. What conditions change the behavior?
3. What risks justify additional depth?
4. What is ambiguous or blocked?

Avoid long narrative analysis that does not change the resulting test suite.
