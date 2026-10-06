# Test Design Techniques

A Senior QA selects the right technique for each requirement. Techniques are tools, not checklists — apply them where they provide value.

## 1. Equivalence Partitioning

Divide input space into behaviorally equivalent classes.

Example:

Age must be 18–60.

Classes:
- below 18;
- 18–60;
- above 60.

Do not create multiple cases within the same class unless behavior differs.

## 2. Boundary Value Analysis

For explicit limits, consider:
- below minimum;
- minimum;
- just above minimum;
- representative valid value;
- just below maximum;
- maximum;
- above maximum.

Do not fabricate limits.

## 3. Decision Tables

Use when multiple conditions determine an outcome. **This is the most powerful technique for PRDs that introduce multiple independent settings or states.**

Steps:
1. Identify all independent conditions/settings.
2. Identify all possible states for each condition.
3. Enumerate meaningful combinations.
4. Remove impossible or redundant combinations.
5. For each combination, identify the expected outcome.
6. Generate one test case per meaningful combination.

### Example: PLM-659 Pattern

Conditions:
- Standard Prescription: ON / OFF
- Specialist Prescription: ON / OFF
- Consultation Type: GP / SP

Decision table:

| Standard | Specialist | Consult | Expected Behavior |
|---|---|---|---|
| ON | OFF | GP | Uses Standard Prescription |
| ON | OFF | SP | SP prescription not eligible |
| OFF | ON | GP | GP prescription not eligible |
| OFF | ON | SP | Uses Specialist Prescription |
| ON | ON | GP | Uses Standard Prescription |
| ON | ON | SP | Uses Specialist Prescription |
| OFF | OFF | GP | No prescription eligible |
| OFF | OFF | SP | No prescription eligible |

This produces 8 focused test cases that cover all meaningful combinations systematically.

## 4. State Transition

Use when the requirement defines states and transitions.

Model:

`Current State + Trigger → New State`

Consider:
- valid transitions;
- invalid transitions;
- state-specific actions;
- recovery transitions;
- data persistence across state changes;
- side effects of state changes on related features.

Only use states documented or directly established by the requirement.

## 5. Role / Permission Analysis

For explicitly defined roles:
- verify allowed actions;
- verify prohibited actions;
- verify authentication boundaries.

Do not invent roles.

## 6. Negative Testing

Consider:
- invalid input;
- missing required input;
- malformed data;
- unauthorized action;
- invalid state;
- unsupported action;
- ineligible scenario (e.g., benefit not active for this context).

Negative testing must still be grounded in a meaningful constraint or behavior.

## 7. Error Handling

When an error condition is specified, verify:
- trigger;
- system response;
- message if specified;
- resulting state;
- recovery path if specified.

Never invent an error message.

## 8. Workflow / End-to-End

For multi-step business flows, cover:
- primary flow;
- meaningful alternate flow;
- meaningful failure/recovery flow.

Do not split every click into a separate test case unless the template or requirement requires that granularity.

## 9. Data Isolation Testing

When two features share a similar structure or interface, verify isolation:
- Configuring feature A does not affect feature B's values.
- Consuming feature A's quota does not deplete feature B's quota.
- Disabling feature A does not disable feature B.
- Values for both features persist independently after save.

This technique is critical for features like PLM-659 where Standard and Specialist Prescription must be independently configurable.

## 10. Backward Compatibility Testing

When a PRD enhances an existing feature:
- Verify data created before the enhancement is retained correctly.
- Verify the old data maps to the new structure (e.g., old Prescription → Standard Prescription).
- Verify existing workflows continue to function.

## 11. Non-Impact Verification

When a PRD explicitly states that a feature is NOT affected:
- Create a dedicated test case that exercises the unaffected feature.
- Verify its behavior, data, and configuration remain unchanged.
- This is NOT optional — the PRD made a promise, and a Senior QA verifies promises.

## 12. Configuration Persistence Testing

For any configurable feature:
- Configure → Save → Reopen → Verify values persist.
- Configure → Save → Modify → Save → Reopen → Verify updated values persist.
- Configure → Save → Change related setting → Verify no cross-overwrite.

## 13. Technique Selection

Do not mechanically apply every technique to every requirement.

Select techniques based on the structure and risk of the requirement:

| Requirement Pattern | Recommended Techniques |
|---|---|
| Multiple independent ON/OFF settings | Decision Tables, Data Isolation |
| Numeric input with limits | Boundary Value Analysis, Equivalence Partitioning |
| Multi-state entity | State Transition |
| Feature enhancement | Backward Compatibility, Non-Impact Verification |
| Configurable settings | Configuration Persistence |
| Multi-role access | Role/Permission Analysis |
| Sequential workflow | End-to-End, State Transition |
| Similar parallel features | Data Isolation |

## 14. Cause-Effect and Rule Precedence Analysis

Use cause-effect analysis when several inputs or business rules contribute to an outcome. Identify each cause, effect, logical relationship, exclusion, and precedence rule before converting it to a decision table. Cover every distinct documented outcome and precedence branch.

## 15. Pairwise and Constrained Combinatorial Testing

Use pairwise or higher-strength combinations when many independent factors make exhaustive testing impractical and not every full combination creates a distinct outcome.

Before reducing combinations:
1. identify prohibited/impossible combinations from source evidence;
2. fully cover every documented rule, outcome, boundary, and high-risk interaction;
3. select a representative baseline;
4. generate pairwise coverage for remaining factors;
5. add targeted combinations for known dependencies and high-impact failures;
6. document that coverage is reduced rather than exhaustive.

Do not use pairwise to remove feasible rows from a small decision table whose rows produce different outcomes.

## 16. Workflow, Sequence, and Interruption Testing

For documented multi-step flows, model the allowed sequence and applicable alternatives. Consider cancellation, retry, resumption, repeated submission, out-of-order actions, timeout, and partial completion only when the source or system contract establishes those states or risks. Verify intermediate state and final state when both are observable requirements.

## 17. Persistent Data and CRUD Analysis

For each persistent entity, determine which of create, read, update, delete/archive, search/list, history/audit, and downstream consumption are actually in scope. Test identity, relationships, persistence, isolation, and lifecycle transitions supported by the requirements. Do not assume delete, audit, or history behavior exists merely because data is persistent.

## 18. Concurrency, Ordering, Replay, and Idempotency

Apply when requirements include asynchronous processing, callbacks, retries, duplicate submissions, shared limits/inventory, or concurrent actors. Identify the authoritative ordering and duplicate-handling oracle before generating a case. If behavior under concurrency is important but unspecified, record a clarification blocker rather than choosing last-write-wins or another policy.

## 19. Technique Evidence

Record the selected technique on each test condition in the internal inventory. Every generated condition must be explainable by its requirement structure and risk. Follow the reduction and closure requirements in `11-scope-model-and-coverage-closure.md`.
