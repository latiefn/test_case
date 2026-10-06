# Requirement Analysis Rules

A Senior QA does not merely read requirements — they decompose, classify, cross-reference, and probe for gaps. This is the most critical phase: poor analysis leads to poor coverage.

## 1. Requirement Unit

Normalize each logical requirement into a discrete unit.

A requirement should contain, where available:
- Requirement ID;
- actor/role;
- precondition;
- action;
- input;
- business rule;
- expected behavior;
- constraint;
- dependency;
- source reference.

## 2. Split Compound Requirements

If one requirement contains multiple independent behaviors, split it logically.

Example:

"User can search products, filter by category, and sort by price."

Potential normalized requirements:
- product search;
- category filtering;
- price sorting.

## 3. Classification

Classify requirements to ensure coverage across all dimensions:
- Functional;
- Business Rule;
- Validation;
- UI;
- Navigation;
- Data;
- API;
- Integration;
- Authentication;
- Authorization;
- State Transition;
- Error Handling;
- Non-Functional;
- Backward Compatibility;
- Non-Impact (explicitly unaffected features).

## 4. Deep Analysis Checklist

For every PRD, systematically extract:

### 4a. Entities and Objects
- What objects/entities does the PRD introduce or modify?
- What are their attributes/fields?
- What are the relationships between them?

### 4b. States and Transitions
- What states can each entity be in? (active/inactive, enabled/disabled, on/off)
- What triggers state transitions?
- What happens when a state changes? (side effects, cascading changes)
- What state combinations exist across multiple entities?

### 4c. Configuration and Settings
- What settings are introduced?
- Are settings independent or interdependent?
- What are the valid values for each setting?
- What happens when settings are changed after initial configuration?

### 4d. Business Rules and Logic
- What conditional logic governs behavior? (if/then/else rules)
- What calculations or formulas apply?
- What are the eligibility/qualification criteria?
- What are the routing/selection rules? (e.g., which benefit applies to which context)

### 4e. Data Lifecycle
- How is data created?
- How is data stored and persisted?
- How is data retrieved and displayed?
- How is data consumed by downstream processes?
- How is data updated or modified?
- What happens to data when related settings change?

### 4f. User Actions
- What actions can the user perform?
- What preconditions are required for each action?
- What is the expected outcome of each action?
- What happens when the user performs an invalid action?

### 4g. Boundaries and Limits
- What explicit limits does the PRD define?
- What values are at the boundary of valid ranges?
- What happens at, below, and above boundaries?

### 4h. Integration Points
- What other systems or features interact with this feature?
- What data flows between systems?
- What happens when the integration point is unavailable?

### 4i. Backward Compatibility
- What existing features does this PRD enhance or modify?
- What happens to data created before this enhancement?
- What existing workflows must continue to work?

### 4j. Non-Impact Verification
- Does the PRD explicitly state that certain features are not affected?
- If so, these must be verified through dedicated test cases.

## 5. Actor and Role

Identify the actor when explicitly specified.

Do not invent additional roles.

## 6. Preconditions

Extract explicit prerequisites.

Do not turn test actions into preconditions.

## 7. Expected Behavior

Capture the exact documented outcome.

If the requirement only says an action is allowed but does not define the resulting UI or response, do not invent one.

## 8. Requirement Traceability

Create a stable internal identifier when the source does not provide one.

Suggested format:

`REQ-001`, `REQ-002`, etc.

Never replace an existing official requirement ID with an internally generated ID.

## 9. Conflicts

If sources contradict each other:
- record both;
- identify the conflicting source locations;
- do not silently choose a winner;
- mark the requirement as requiring clarification.

## 10. Requirement Completeness

Evaluate whether each requirement has enough information to produce an executable test.

Missing information should be classified using `10-ambiguity-and-assumption.md`.

## 11. Cross-Feature Impact Analysis

A Senior QA maps the "blast radius" of each requirement:
- Which existing features share data with the new/modified feature?
- Which existing workflows pass through the affected area?
- Which UI screens display or depend on the affected data?
- Which downstream processes consume the affected data?

This analysis identifies regression risks and drives non-impact test cases.

## 12. Requirement Evidence Record

Use the atomic requirement catalog defined in `11-scope-model-and-coverage-closure.md`. Each normalized unit must retain its source/location, basis (`EXPLICIT`, `DERIVED`, `ASSUMPTION`, or `UNKNOWN`), expected-result oracle, testability, risk evidence, and ambiguity references.

An acceptance criterion, business-rule table row, explicit exception, and explicit non-impact statement are separate coverage obligations even when they belong to one ticket.

## 13. Scope Boundary Analysis

Explicitly classify:
- in-scope behavior introduced or modified by the PRD;
- existing behavior that is in regression scope because it shares data, workflow, interface, or implementation impact identified by the sources;
- explicitly unchanged behavior requiring non-impact verification;
- explicitly out-of-scope behavior;
- unknown scope requiring clarification.

Do not expand regression scope based only on generic possibilities. Tie each impact to a changed entity, state, interface, rule, workflow, or documented project dependency.

## 14. Testability and Oracle Review

For each requirement, determine whether setup, action, and expected outcome are sufficiently defined. If an action is specified but the observable outcome is not, classify it as blocked rather than inventing an oracle. If only part of a requirement is testable, cover the supported portion and report the remainder.

## 15. Cross-Source Reconciliation

Create one evidence record when sources agree. When they differ, preserve each statement and apply the source-of-truth order in `AGENTS.md` only when the conflict is between source tiers. Conflicts within the same authoritative tier require clarification; do not silently choose the most convenient interpretation.
