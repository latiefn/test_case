# Bad Test Case Examples

These examples illustrate patterns that must be avoided. A Senior QA recognizes and eliminates these patterns during review.

## 1. Invented Error Message

### Bad

**Expected Result:**
`System displays "Password must contain at least 8 characters".`

### Problem

The requirement only states that the password must contain at least 8 characters. It does not specify the exact error message.

The test may verify rejection, but the exact message must not be invented.

---

## 2. Vague Expected Result

### Bad

`Login works correctly.`
`Prescription is correct.`
`System behaves as expected.`

### Problem

Not objectively verifiable. A tester cannot determine PASS or FAIL.

**Senior QA fix**: `User is logged in and redirected to the dashboard.` / `GP checkout applies Standard Prescription quota, coverage, limit, and fee values.`

---

## 3. Multiple Unrelated Behaviors

### Bad

`Verify login, dashboard loading, profile editing, logout, and password reset.`

### Problem

Not atomic. If this test fails, which behavior broke? Split into individual test cases.

---

## 4. Invented Boundary

### Bad

Requirement:
`Username must be valid.`

Test:
`Verify username with exactly 20 characters.`

### Problem

The requirement does not specify a 20-character boundary. A Senior QA tests only documented boundaries.

---

## 5. Duplicate Test Cases

### Bad

TC-001:
`Verify invalid email is rejected.`

TC-002:
`Verify malformed email cannot be submitted.`

If both use the same input class and verify the same rejection behavior, they are redundant. Consolidate.

---

## 6. Unsupported Role

### Bad

Requirement:
`User can submit the form.`

Test:
`Verify administrator can submit the form.`

### Problem

No administrator role is specified. A Senior QA does not invent roles.

---

## 7. Implementation-Based Test

### Bad

`Verify CSS class .btn-primary is present.`

### Problem

Implementation detail, not a product requirement. Test observable behavior instead.

---

## 8. Wrong Summary Format

### Bad

`TC-001: Test prescription feature`
`Verify prescription`

### Problem

The summary must follow `[TC][{TICKET}] {Descriptive title}` format.

Correct: `[TC][PLM-659] Verify GP checkout uses Standard Prescription when Standard is active and Specialist is inactive`

---

## 9. Actions in Precondition

### Bad

**Precondition:** `Open the plan configuration page and click Edit.`

### Problem

Preconditions describe the required STATE, not ACTIONS. Actions belong in test steps.

Correct: `Admin can edit an existing Template Assigned Plan.`

---

## 10. Missing Requirement Keys

### Bad

A test case with empty Requirement Keys.

### Problem

Every test case must be linked to the official PRD/Jira ticket, and its Description must list the internal requirement/condition IDs used by the coverage matrix. A ticket key alone does not prove which atomic rule the case covers.

---

## 11. Vague Precondition

### Bad

**Precondition:** `User is logged in.`

### Problem

Doesn't specify WHICH user, what ROLE, what SYSTEM STATE.

**Senior QA fix**: `Standard Prescription is ON with configured quota, coverage, limit, frequency, and fee values. Specialist Prescription is OFF. Eligible GP consultation data exists.`

---

## 12. Missing State Combinations

### Bad

Only testing the happy path (both features ON) without testing:
- Feature A ON + Feature B OFF
- Feature A OFF + Feature B ON
- Feature A OFF + Feature B OFF

### Problem

Incomplete coverage. A Senior QA uses decision tables to systematically cover ALL meaningful state combinations.

---

## 13. Missing Negative Tests

### Bad

Only testing what SHOULD work, without testing what should NOT work.

### Problem

A Senior QA always verifies ineligibility: When a feature is OFF, the corresponding context should NOT have access to that benefit.

---

## 14. Missing Non-Impact Verification

### Bad

The PRD says "Telemedicine Benefit is not affected" but no test case verifies this.

### Problem

The PRD made a promise. A Senior QA verifies promises. Create a dedicated non-impact test case.

---

## 15. Missing Backward Compatibility

### Bad

The PRD enhances an existing feature but no test verifies that pre-enhancement data is preserved.

### Problem

Existing users depend on existing data. A Senior QA always tests that old data survives new features.
