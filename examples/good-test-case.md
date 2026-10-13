# Good Test Case Examples

These examples demonstrate writing quality and composition patterns only.

They are NOT quotas, minimum case counts, or mandatory coverage dimensions.

## Example 1 — Simple Functional Flow

**Summary**  
`[TC][PLM-100] Verify user can save a valid profile phone number`

**Description**  
Validate that a valid phone number can be saved and remains available after the profile is reopened.

**Precondition**  
User account exists and the profile is editable.

**Steps**
1. Open the profile edit page. → Profile edit page is displayed.
2. Enter `<valid_phone_number>` in the phone number field. → The value is accepted.
3. Save the profile. → The profile is saved successfully.
4. Reopen the profile. → The saved phone number is displayed.

## Example 2 — Boundary

Use only when the requirement explicitly defines a limit.

**Pattern**
- one valid boundary;
- one upper/lower boundary as applicable;
- one invalid class outside the limit.

Add just-inside/just-outside cases only when the boundary behavior or risk warrants them.

## Example 3 — Decision Table

Use only when multiple conditions jointly determine an outcome.

Do not infer a fixed number of combinations from this example.

## Writing Rules

- One observable outcome and one reason to fail per case (`rules/04-test-case-rules.md` §7).
- Multi-step flows are allowed when steps form one dependent chain toward that outcome.
- Expected results must be observable.
- Preserve exact source wording when the requirement specifies exact text/value/status.
- Use representative placeholders when exact data is not defined.
- Do not invent error messages, limits, or roles.
- Avoid shallow duplicate variants, but do not merge independent conditions to reduce the count.
