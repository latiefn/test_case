# Test Case Writing Rules

These rules define how a Senior QA writes test cases. Refer to `template/PLM-659.xlsx` as the reference for expected writing style.

A well-written test case is specific, traceable, executable, and catches a real bug when it fails.

## 1. Summary (Title)

Format: `[TC][{TICKET}] {Descriptive title}`

The title should describe the specific behavior being verified. A Senior QA writes titles that immediately tell the reader:
- What feature is being tested
- What specific scenario or condition is being verified
- What state/configuration applies

Good:
`[TC][PLM-659] Verify GP checkout uses Standard Prescription when Standard is active and Specialist is inactive`
`[TC][PLM-659] Verify existing Prescription benefit is retained as Standard Prescription after enhancement`

Bad:
`[TC][PLM-659] Test prescription`
`[TC][PLM-659] Verify prescription works`

## 2. Description

Provide a clear, specific description of what the test case validates. The description explains the *purpose* and *scope* of the test.

Good:
`Validate source-based routing for GP when only Standard Prescription is active.`
`Validate backward compatibility for plans created before the feature.`

Bad:
`Test the prescription feature.`
`Check if it works.`

## 3. Requirement Keys

Always set to the PRD ticket ID (e.g., `PLM-659`).

Every test case must be traceable to its source requirement.

## 4. Preconditions

Preconditions describe the **state** required before execution, not the **actions** to reach it.

A Senior QA writes preconditions that are precise about the system state, including:
- Which settings are ON/OFF
- What data must exist
- What user/role is required
- What configuration values are set

Good:
`Standard Prescription is ON with configured quota, coverage, limit, frequency, and fee values. Specialist Prescription is OFF. Eligible GP consultation data exists.`
`Both benefits are ON and have intentionally different quota, coverage, limit, frequency, and fee values. Eligible GP consultation data exists.`

Bad:
`Open the plan and click edit.` ← This is an action, not a precondition.
`User is logged in.` ← Too vague; what user? what role? what state?

## 5. Test Steps (Multi-Row)

Each step occupies its own XLSX row with:
- **Step Description**: One clear action per step.
- **Step Data**: Specific input data when relevant; leave empty if not applicable.
- **Expected Result**: Observable, verifiable outcome for that step.

Steps must:
- be sequential;
- be executable;
- contain one clear action per step where practical;
- avoid ambiguous verbs;
- build toward verifying the test case's primary objective.

A Senior QA designs steps that:
- Set up the specific scenario (navigate, configure)
- Execute the action under test
- Verify the expected outcome
- Verify persistence where applicable (save → reopen → check)

Good steps:
1. `Open Template Assigned Plan configuration.` → `Configuration page is displayed.`
2. `Locate prescription benefits.` → `Standard Prescription and Specialist Prescription are displayed.`
3. `Enable Standard Prescription and Specialist Prescription.` → `Both prescription benefits can be activated independently.`
4. `Enter different valid values for applicable fields.` → `Both benefits accept independent values.`
5. `Save, reopen, and review the plan.` → `Both active states and values persist without cross-overwrite.`

Bad steps:
- `Check whether prescription works.` ← Vague, not executable.
- `Do everything and verify.` ← Not atomic.

## 6. Expected Results

Expected results must be observable and objectively verifiable. A Senior QA writes expected results that would make a tester say "PASS" or "FAIL" with no ambiguity.

Good:
`Standard Prescription becomes inactive while Specialist Prescription configuration remains unchanged.`
`GP checkout applies Standard Prescription quota, coverage, limit, and fee values.`
`Both active states and values persist without cross-overwrite.`

Bad:
`It works.`
`Prescription is correct.`
`System behaves as expected.`

## 7. One Primary Behavior Per Test Case

A test case should test one primary behavior, condition, or scenario.

However, a multi-step flow that tests a coherent scenario (configure → save → verify → modify → verify persistence) counts as one primary behavior.

Split test cases when:
- Two behaviors have different failure modes.
- Two scenarios require different preconditions.
- Two conditions produce different expected outcomes.

## 8. Exact Requirement Text

When the requirement specifies exact:
- UI text;
- validation message;
- value;
- status;
- response;
- state;

preserve it accurately in the expected result.

## 9. Test Data

Use only data defined by the requirement or clearly representative values.

If exact data is not specified, use descriptive placeholders:
- `Standard set A; Specialist set B` ← Makes isolation clear.
- `<valid_email>`
- `<eligible_GP_consultation_data>`

Do not fabricate production data.

## 10. Priority

Assign priority based on business/technical risk:
- **High**: Core functionality, business-critical flows, security, data integrity, financial/transactional behavior
- **Medium**: Important secondary functionality, alternative flows, standard validation, configuration, state transitions
- **Low**: Cosmetic, minor edge cases, low-impact scenarios

## 11. Reporter

Set Reporter only to an author identity known to exist in the target project. If it is required but not provided by user or stable project context, ask; do not invent a person or account.

## 12. Test Type and Test Category

Follow the inspected current template:
- `Test Type` is optional and, when populated, is `Manual` or `Automated`.
- `Test Category` uses `Manual` or `Automated` under the current template contract.
- Use `Automated` only when actual automation content or an authoritative automation designation exists.
- Do not copy `Functional` from the older PLM-659 reference unless the user confirms that the target Jira project accepts it.

## 13. Folder

Use the exact folder convention:
`{Year}/{Year} Sprint {N}/{TICKET}`

Example: `2026/2026 Sprint 16/PLM-659`

There is no space after the final `/`. Year and sprint must come from the user or stable project context. If required but unavailable, ask; do not invent a default.

## 14. Avoid Implementation Details

Do not test:
- CSS selectors;
- internal class names;
- database tables;
- implementation-specific functions;

unless they are explicitly part of the requirement or test objective.

## 15. Duplicate Prevention

Before finalizing a test case, compare:
- requirement;
- precondition;
- input;
- action;
- expected result.

If another case provides equivalent coverage, do not create another case without a specific reason.

## 16. Reusability

Use stable language that remains valid if implementation details change.

## 17. Senior QA Writing Patterns

A Senior QA follows these patterns from the PLM-659 reference:

### Pattern 1: Configuration Test
- **Objective**: Verify a feature can be configured independently
- **Steps**: Open config → Locate feature → Enable/configure → Set values → Save → Reopen → Verify persistence

### Pattern 2: State Combination Test
- **Objective**: Verify behavior under a specific combination of ON/OFF states
- **Steps**: Set precondition state → Initiate action → Verify correct behavior based on state
- **Precondition**: Precisely describes which features are ON/OFF

### Pattern 3: Data Isolation Test
- **Objective**: Verify two similar features operate independently
- **Steps**: Configure both with distinct values → Execute actions on each → Verify no cross-contamination

### Pattern 4: Backward Compatibility Test
- **Objective**: Verify pre-enhancement data is preserved
- **Steps**: Open pre-enhancement data → Verify mapping to new structure → Verify functionality preserved

### Pattern 5: Non-Impact Test
- **Objective**: Verify explicitly unaffected feature remains unchanged
- **Steps**: Exercise the unaffected feature → Verify behavior/data/config unchanged
