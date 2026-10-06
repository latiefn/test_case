# Good Test Case Examples

These examples demonstrate Senior QA test-case quality and content patterns inspired by `template/PLM-659.xlsx`. PLM-659 is an older 18-column reference; the metadata below follows the current template. The examples are illustrative and do not replace source-based traceability for a live ticket.

---

## Pattern 1: Configuration Test

### Source Requirement
> Template Assigned Plan must support both Standard Prescription and Specialist Prescription with independent configuration.

### Test Case

| Field | Value |
|---|---|
| Summary | `[TC][PLM-659] Verify Standard and Specialist Prescription are independently configurable on Template Assigned Plan` |
| Description | `Validate that Template Assigned Plan supports both prescription benefit types with the same applicable fields and independent values. Coverage: REQ-001 / COND-001.` |
| Requirement Keys | `PLM-659` |
| Test Type | `Manual` |
| Priority | `Medium` |
| Reporter | `Latief` |
| Test Category | `Manual` |
| Precondition | `Admin can edit an existing Template Assigned Plan.` |
| Folder | `2026/2026 Sprint 16/PLM-659` |

| Step | Step Description | Step Data | Expected Result |
|---|---|---|---|
| 1 | Open Template Assigned Plan configuration. | | Configuration page is displayed. |
| 2 | Locate prescription benefits. | | Standard Prescription and Specialist Prescription are displayed. |
| 3 | Enable Standard Prescription and Specialist Prescription. | | Both prescription benefits can be activated independently. |
| 4 | Enter different valid values for applicable fields. | Standard set A; Specialist set B | Both benefits accept independent values. |
| 5 | Save, reopen, and review the plan. | | Both active states and values persist without cross-overwrite. |

### Why This Is Good
- Tests configuration independence (two features, same interface, different values)
- Verifies persistence (save → reopen → verify)
- Step data makes isolation explicit ("Standard set A; Specialist set B")
- Precondition is a state, not an action

---

## Pattern 2: State Combination Test (Decision Table Row)

### Source Requirement
> GP checkout should use Standard Prescription benefit when applicable.

### Test Case

| Field | Value |
|---|---|
| Summary | `[TC][PLM-659] Verify GP checkout uses Standard Prescription when Standard is active and Specialist is inactive` |
| Description | `Validate source-based routing for GP when only Standard Prescription is active.` |
| Requirement Keys | `PLM-659` |
| Priority | `Medium` |
| Precondition | `Standard Prescription is ON with configured quota, coverage, limit, frequency, and fee values. Specialist Prescription is OFF. Eligible GP consultation data exists.` |

| Step | Step Description | Step Data | Expected Result |
|---|---|---|---|
| 1 | Initiate GP prescription checkout. | | Checkout process starts. |
| 2 | Verify prescription benefit applied. | | GP checkout applies Standard Prescription quota, coverage, limit, and fee values. |
| 3 | Verify prescription benefit source label. | | Prescription benefit is identified as Standard Prescription. |
| 4 | Complete checkout and verify transaction. | | Transaction completes using Standard Prescription configuration. |

### Why This Is Good
- Tests one specific row of the decision table (Standard ON, Specialist OFF, GP context)
- Precondition precisely describes the ON/OFF state of BOTH features
- Expected results are specific about WHICH benefit's values are applied
- Part of a systematic set covering all state combinations

---

## Pattern 3: Negative / Ineligibility Test

### Source Requirement
> When a prescription benefit is inactive, it should not be available for the corresponding consultation type.

### Test Case

| Field | Value |
|---|---|
| Summary | `[TC][PLM-659] Verify SP prescription is not eligible when Standard is active and Specialist is inactive` |
| Description | `Validate that Standard Prescription is not a fallback for SP consultation.` |
| Requirement Keys | `PLM-659` |
| Priority | `Medium` |
| Precondition | `Standard Prescription is ON. Specialist Prescription is OFF. SP consultation data exists.` |

| Step | Step Description | Step Data | Expected Result |
|---|---|---|---|
| 1 | Initiate SP prescription checkout. | | System evaluates prescription eligibility. |
| 2 | Verify prescription benefit availability. | | SP prescription benefit is not eligible (Specialist Prescription is inactive). |
| 3 | Verify no fallback to Standard Prescription. | | Standard Prescription is not applied as a substitute for Specialist Prescription. |

### Why This Is Good
- Tests the NEGATIVE case — what should NOT happen
- Explicitly verifies no cross-fallback between benefit types
- Precondition states both features' states clearly
- Expected result describes the absence of behavior (not eligible), not just "it fails"

---

## Pattern 4: Data Isolation Test

### Source Requirement
> Standard and Specialist Prescription quotas and frequencies must be stored and consumed independently.

### Test Case

| Field | Value |
|---|---|
| Summary | `[TC][PLM-659] Verify Standard and Specialist Prescription quota and frequency are stored and consumed independently` |
| Description | `Validate data isolation for quota and frequency across both benefit types.` |
| Requirement Keys | `PLM-659` |
| Priority | `Medium` |
| Precondition | `Both benefits are ON and configured with distinct quota and/or frequency values. User is eligible for both prescription benefit types before execution.` |

| Step | Step Description | Step Data | Expected Result |
|---|---|---|---|
| 1 | Record initial quota and frequency for both benefits. | | Both benefits show their independently configured quota and frequency values. |
| 2 | Consume a GP prescription (using Standard Prescription). | | Standard Prescription quota is decremented. |
| 3 | Verify Specialist Prescription quota. | | Specialist Prescription quota remains unchanged. |
| 4 | Consume an SP prescription (using Specialist Prescription). | | Specialist Prescription quota is decremented independently. |

### Why This Is Good
- Tests data isolation explicitly — consuming one benefit does NOT affect the other
- Verifies independence at the data level, not just configuration
- Step 3 is the critical assertion: verifying the OTHER feature was NOT affected

---

## Pattern 5: Backward Compatibility Test

### Source Requirement
> Existing plans with the former Prescription benefit must retain their configuration as Standard Prescription.

### Test Case

| Field | Value |
|---|---|
| Summary | `[TC][PLM-659] Verify existing Prescription benefit is retained as Standard Prescription after enhancement` |
| Description | `Validate backward compatibility for plans created before the feature.` |
| Requirement Keys | `PLM-659` |
| Priority | `Medium` |
| Precondition | `An existing pre-enhancement plan has the former Prescription benefit enabled and configured.` |

| Step | Step Description | Step Data | Expected Result |
|---|---|---|---|
| 1 | Open the pre-enhancement plan. | | Plan configuration is displayed. |
| 2 | Verify prescription benefit mapping. | | Former Prescription benefit is retained as Standard Prescription with original values preserved. |
| 3 | Verify plan functionality. | | Plan continues to function correctly with the mapped Standard Prescription. |

### Why This Is Good
- Explicitly verifies backward compatibility — existing data survives the enhancement
- Verifies data mapping (old → new structure)
- Verifies functional continuity (plan still works)

---

## Pattern 6: Non-Impact Verification Test

### Source Requirement
> Telemedicine Benefit behavior remains unchanged.

### Test Case

| Field | Value |
|---|---|
| Summary | `[TC][PLM-659] Verify Telemedicine Benefit behavior remains unchanged` |
| Description | `Validate explicit non-impact requirement.` |
| Requirement Keys | `PLM-659` |
| Priority | `Medium` |
| Precondition | `An existing Telemedicine Benefit configuration and eligible test data are available.` |

| Step | Step Description | Step Data | Expected Result |
|---|---|---|---|
| 1 | Open Telemedicine Benefit configuration. | | Configuration is accessible and displays existing values. |
| 2 | Verify Telemedicine Benefit settings. | | All settings match the pre-enhancement configuration. |
| 3 | Execute a Telemedicine flow. | | Telemedicine Benefit functions as before. |
| 4 | Verify no prescription-related side effects. | | Telemedicine flow does not reference or affect prescription benefits. |

### Why This Is Good
- Verifies the PRD's explicit promise that this feature is NOT affected
- Step 4 checks for cross-contamination from the new feature
- A Senior QA always verifies non-impact guarantees

---

## Summary: Senior QA Coverage Pattern

A complete Senior QA test suite for a feature like PLM-659 covers ALL of these dimensions:

| # | Pattern | Test Cases | Purpose |
|---|---|---|---|
| 1 | Configuration | 1-2 | Can each feature be set up independently? |
| 2 | State Combinations | 6-8 | All ON/OFF × context combinations |
| 3 | Negative/Ineligibility | 2-4 | What should NOT work? |
| 4 | Data Isolation | 1-2 | Do parallel features stay independent? |
| 5 | Backward Compatibility | 1-2 | Does old data survive the change? |
| 6 | Non-Impact | 1-2 | Are unaffected features truly unaffected? |

This produces approximately 12-20 focused test cases with **complete scope coverage** and **zero redundancy**.
