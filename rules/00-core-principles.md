# Core QA Principles

## 1. Requirement First

Every test case must originate from an explicit requirement, acceptance criterion, business rule, documented UI/API behavior, documented constraint, or explicit project rule.

## 2. Never Invent Behavior

Do not invent:
- business rules;
- limits or default values;
- validation messages;
- roles or permissions;
- API responses/status codes;
- navigation behavior;
- database/integration behavior;
- timing or timeout values.

When information is missing, follow `10-ambiguity-and-assumption.md`.

## 3. Senior QA Means Selective Depth

Think beyond the happy path, but activate deeper analysis only when evidence supports it.

Use this order:
1. explicit behavior;
2. directly derived test conditions;
3. documented risk;
4. only then optional experience-based checks.

Experience-based checks must not invent product behavior.

## 4. Coverage Over Quantity

Generate enough cases to cover meaningful behavior and material risk.

Do not use fixed case-count targets.

Remove cases that duplicate another case's behavior, outcome, failure mode, and data/state condition.

Do not merge independent conditions into one case to reduce the count. One case = one observable outcome, one reason to fail. See `rules/04-test-case-rules.md` §7.

## 5. Observable Oracles

Expected results must be observable and objectively verifiable.

Do not write vague outcomes such as `works correctly` or `system behaves properly`.

## 6. Atomic but Cohesive

A test case has one observable outcome and one reason to fail.

A multi-step flow is valid when every step is part of one dependent chain toward that outcome, such as configure → save → reopen → verify persistence. Independent conditions belong in separate cases.

## 7. Independence

Avoid unnecessary dependency between cases. Put required state/data in the precondition instead of relying on another test case unless the dependency is itself the behavior under test.

## 8. Traceability

Maintain:
`Requirement → Condition → Test Case`

## 9. Regression Restraint

Add regression cases only when the requirement changes existing behavior/data/interface, explicitly promises non-impact, or project context documents a concrete dependency/risk.

Do not create broad regression suites from generic possibility.

## 10. No Fake Coverage

Do not create cases only to satisfy a checklist.

A dimension with no evidence or trigger should be treated as not applicable, not filled with generic tests.
