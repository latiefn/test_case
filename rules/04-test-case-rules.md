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

Write role and starting state as short lines; separate multiple conditions with real newlines, not literal `\n` text.

## 5. Steps

Each step should be:
- executable;
- sequential;
- clear enough to reproduce;
- one action where practical.

Use the smallest number of steps that still makes the scenario reproducible and diagnosable.

A coherent flow may contain several actions in one test case when they prove one primary behavior.

Write step descriptions in imperative voice — "Open…", "Click…", "Fill…", "Input…", "Observe…".

## 6. Expected Result

Write an observable, objective result for each relevant step.

Preserve exact source text, values, status, or messages when explicitly specified.

Keep expected results outcome-focused. Put multiple assertions on separate lines (real newlines), quote actual UI copy verbatim, and use `-` bullets when listing displayed UI elements.

Never invent an expected result that the source does not support.

## 7. Test Case Granularity (One Outcome, One Reason to Fail)

This is the canonical granularity rule. Other files reference it.

A test case verifies **one observable outcome** and should fail for **one reason**. A FAIL in Xray must tell the reader what broke without opening the steps, and a failure must not hide whether other, independent conditions work.

### Split into separate test cases when
- the expected outcome differs (e.g. column shown vs hidden, save succeeds vs fails);
- the trigger is an alternative path with its own failure mode (e.g. check button vs Enter key, cross button vs Escape key);
- a later condition could still be tested on its own if an earlier step failed (independence test: "if step N fails, can step N+1 still be meaningfully verified?" → if yes, split);
- the precondition or actor differs (e.g. Store Admin vs Vendor Admin viewing as store);
- the risk or priority differs.

### Keep in one test case when
- the steps form one dependent chain that proves a single outcome (e.g. edit → save → reload → value persisted);
- the steps are data variants of the same outcome, one step per variant, so the failing variant is visible from the step result (e.g. status Connected and Pending both show the column);
- the setup is expensive and the assertions are effects of one trigger (e.g. one forced sync failure → banner on the list and CTA on the dashboard).

### Do not
- split a coherent chain merely because it has many UI actions;
- merge independent conditions only to reduce the case count;
- create a case that has no distinct outcome or no traceable condition.

Test count is a result of this rule, never a target in either direction.

## 8. Test Data

Use source-defined data where available.

Format step data as `Field : value`, one field per line. Leave it empty when the step needs no input.

Otherwise use descriptive placeholders such as `<valid_email>` or `<eligible_user>`.

Do not fabricate production-like values that could be mistaken for real business data.

When a documented constraint has an explicit limit (max/min characters, numeric range, size), supply concrete boundary data that actually exercises the limit rather than a placeholder — for example a real string longer than a 64-character title cap, or a value one unit past a numeric bound. Keep such filler data obviously synthetic (e.g. `Lorem ipsum …`) so it is not mistaken for real business data.

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

## 12. Language

Write all test case content in **English only** — Summary, Description, Precondition, Step Description, Step Data, and Expected Result.

This applies regardless of the language the user chats in or the language of the PRD/requirement source. If a source (e.g., a Jira ticket or Figma copy) is in another language, translate the testable intent into English for the test case text.

Exception: when a specific literal string must be asserted verbatim (an exact UI message, label, status, or error text defined by the source), preserve that string in its original language inside quotes, and keep the surrounding step/expected wording in English. Example: `Expected: System displays the error message "Masa berlaku kartu asuransi kamu habis".`
