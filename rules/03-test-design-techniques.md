# Test Design Techniques

Techniques are triggered by requirement structure. Do not apply them mechanically.

## 1. Equivalence Partitioning

Use when different input classes can produce different behavior.

Create one representative per behaviorally distinct class. Add more only when the behavior or risk differs.

## 2. Boundary Value Analysis

Use only for explicit or authoritative limits.

Default coverage:
- lower boundary;
- upper boundary;
- one invalid class outside the range.

Expand to just-inside/just-outside values only when the boundary behavior is business-critical or known to be error-prone.

Never invent limits.

## 3. Decision Tables

Use only when at least two independent conditions jointly influence an outcome, or when explicit precedence/exclusion rules exist.

Procedure:
1. identify conditions;
2. identify feasible states;
3. remove impossible rows;
4. group rows with identical observable outcomes when safe;
5. create one case per outcome-distinct row or consolidated group.

Do not create a decision table for a simple single-condition flow.

## 4. State Transition

Use when the source defines states and transitions.

Cover documented states and valid transitions. Test invalid transitions only when their prohibition or outcome is documented.

## 5. Pairwise / Combinatorial

Use when multiple independent factors create a large combination space.

Prefer:
- exhaustive coverage for small, interacting spaces;
- outcome/rule coverage plus pairwise coverage for larger independent spaces;
- targeted high-risk combinations.

Record any deliberate reduction.

## 6. Role / Permission

Use only for explicitly defined roles/permissions.

Cover allowed and prohibited actions when both are supported by requirements.

Do not invent roles.

## 7. Negative Testing

Generate negative cases only when supported by:
- explicit rejection behavior;
- documented constraint;
- documented invalid state;
- authorization rule;
- documented error path; or
- concrete project risk.

Do not create generic empty/null/special-character/SQL-injection cases solely because a field exists.

## 8. Error Handling

When an error condition is specified, verify the trigger, documented response, resulting state, and recovery behavior when specified.

Never invent error messages.

## 9. Workflow / End-to-End

For a multi-step business process, cover:
- primary valid flow;
- meaningful alternate flow if it changes outcome;
- meaningful failure/recovery flow if documented.

Do not create a separate case for every click.
