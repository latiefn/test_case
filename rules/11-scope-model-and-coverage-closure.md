# Scope Model and Coverage Closure

This rule is the completion contract for Medium/High complexity generation and for any ticket with interacting conditions, states, or cross-feature impact.

## 1. Compact Working Artifacts

Use three files under `work/{TICKET}/`:
- `analysis.md`
- `coverage.md`
- `validation.md`

Do not create separate documents for every artifact unless the user requests them.

## 2. Analysis Record

`analysis.md` must contain:
- source inventory;
- atomic requirement catalog;
- trigger/applicability decisions;
- risk notes;
- ambiguity/blocker log.

## 3. Condition Record

Each meaningful test condition should capture:
`Condition ID | Requirement ID | Basis | Context/State | Trigger/Input | Expected Oracle | Technique | Risk`

## 4. Scope Status

Each requirement/condition ends in:
- `COVERED`
- `CONSOLIDATED`
- `BLOCKED`
- `NOT APPLICABLE`

## 5. Decision Closure

Use decision tables only when multiple conditions jointly determine an outcome.

Every feasible outcome-distinct row must map to a test case or a clearly equivalent consolidated case.

## 6. State Closure

When a documented state model exists, cover every documented state and valid transition.

Invalid transitions require an explicit prohibition or expected behavior.

## 7. Large Combination Spaces

Do not exhaustively enumerate large spaces by default.

Use:
- distinct documented outcomes;
- critical interactions;
- pairwise/constrained coverage for remaining independent factors;
- targeted high-risk combinations.

Record the reduction method and do not claim exhaustive coverage.

## 8. Risk Depth

Extra coverage must have evidence from:
- business/user impact;
- data/financial/security/compliance impact;
- exposure;
- change complexity;
- blast radius;
- documented defect history.

Do not infer risk solely from ticket wording.

## 9. Closure Gate

Do not export XLSX while a material requirement or applicable condition has an unexplained gap.

A local ambiguity can coexist with otherwise complete generation. Report it as `BLOCKED`.
