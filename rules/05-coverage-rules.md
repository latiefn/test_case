# Coverage Rules

## 1. Coverage Objective

Coverage means closing the documented, testable scope and material risk with minimal redundancy.

There is no fixed test-case count target.

## 2. Requirement Closure

Every testable requirement must map to at least one test case or be explicitly marked:
- `CONSOLIDATED`;
- `BLOCKED`; or
- `NOT APPLICABLE` with rationale.

## 3. Adaptive Coverage Dimensions

Evaluate dimensions only when triggered by requirement evidence or concrete project risk.

| Dimension | Trigger |
|---|---|
| Functional | Always for in-scope behavior |
| Validation/Negative | Explicit constraints, rejection, invalid state, or risk |
| Boundary | Explicit limits/ranges |
| Decision table | 2+ conditions jointly affect outcome |
| State transition | Explicit states/transitions |
| Role/permission | Explicit roles or access rules |
| Data lifecycle | Data is persisted, retrieved, consumed, updated, or state-dependent |
| Data isolation | Parallel entities/configurations share structure or data |
| Integration | Explicit integration/dependency |
| Regression | Concrete impact or explicit non-impact statement |
| Concurrency/idempotency | Repeated, parallel, asynchronous, retry, or duplicate behavior is in scope |
| Non-functional | Explicit NFR or project rule |

## 4. Coverage Depth

Use the smallest depth that closes the triggered dimension:
- one representative case when one behavior class exists;
- multiple cases only for distinct outcomes/classes/states/risks;
- exhaustive combinations only when practical and outcome-distinct;
- pairwise or risk-based reduction for large independent spaces.

## 5. Consolidation

Consolidate cases when they have the same:
- primary behavior;
- precondition/state;
- observable outcome;
- failure mode.

Do not consolidate when diagnosis becomes ambiguous or materially different risks are hidden.

## 6. Bidirectional Mapping

Maintain:
`Requirement/Condition → Test Case`
and
`Test Case → Requirement/Condition`

No orphan test case is allowed.

## 7. Closure Status

Use exactly:
- `COVERED`
- `CONSOLIDATED`
- `BLOCKED`
- `NOT APPLICABLE`

Each non-covered status requires a concrete rationale.

## 8. Combination Reduction

When the combination space is large:
1. cover every distinct documented outcome/rule;
2. cover all critical interactions when feasible;
3. apply pairwise/constrained coverage to remaining independent factors;
4. add targeted high-risk combinations;
5. record the reduction method.

Never claim exhaustive coverage after reducing the space.

## 9. No Generic Closure

Do not add cases merely because a dimension exists in this file. A dimension without a trigger is `NOT APPLICABLE`.
