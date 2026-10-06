# Test Case Writing Rules

A well-written test case is specific, traceable, executable, and useful when it fails.

## 1. Summary

Format:
`[TC][{TICKET}] {Specific behavior}`

State the feature and condition/outcome being verified. Avoid generic titles such as `Test feature` or `Verify works`.

## 2. Description

State the test objective and, when useful, the logical coverage IDs.

Keep it concise. Do not repeat the entire requirement.

## 3. Requirement Keys

Use the official PRD/Jira ticket ID.

Do not replace it with an internal requirement ID.

## 4. Preconditions

Describe the required state/data/actor/configuration before execution.

Do not place execution actions in preconditions.

Use the minimum state needed for the scenario.

## 5. Steps

Each step should be:
- executable;
- sequential;
- clear enough to reproduce;
- one action where practical.

Use the smallest number of steps that still makes the scenario reproducible and diagnosable.

A coherent flow may contain several actions in one test case when they prove one primary behavior.

## 6. Expected Result

Write an observable, objective result for each relevant step.

Preserve exact source text, values, status, or messages when explicitly specified.

Never invent an expected result that the source does not support.

## 7. One Primary Behavior

Keep one primary behavior/condition per test case.

Do not split a coherent flow merely because it has many UI actions.

Split when failure mode, precondition, expected outcome, or risk materially differs.

## 8. Test Data

Use source-defined data where available.

Otherwise use descriptive placeholders such as `<valid_email>` or `<eligible_user>`.

Do not fabricate production-like values that could be mistaken for real business data.

## 9. Priority

Use the definitions in `rules/06-priority-rules.md`.

## 10. Template-Specific Metadata

Follow the current template and `rules/07-template-rules.md` for:
- Test Type;
- Automation Content;
- Reporter;
- Test Category;
- Folder;
- optional metadata.

Do not invent identities, versions, labels, components, or other Jira metadata.

## 11. Writing Reference

`template/PLM-659.xlsx` is historical reference material only.

Use it only when writing style is unclear after applying these rules and the current examples.

It must never override current template structure, field constraints, or project rules.
