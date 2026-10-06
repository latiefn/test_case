# PLM-1005 — Coverage & Decision Table

## Decision Table: data.status → System behavior / Outcome (response.code=0000)

| Row | data.status | System action | Observable outcome | Diagnosis distinct? |
|---|---|---|---|---|
| D1 | valid + combination EXISTS | resolve existing Assigned Plan, create member | Success message; member created & linked | YES (happy, no plan creation) |
| D2 | valid + combination NOT EXIST | create Assigned Plan from Template, then member | Success message; new Assigned Plan + member created | YES (plan creation path) |
| D3 | Invalid | — | Member Invalid Message | YES |
| D4 | Inactive | — | Member Inactive Message | YES |
| D5 | policyPeriodInvalid | — | Member Expired Message | shares msg w/ D6,D13 |
| D6 | memberPeriodInvalid | — | Member Expired Message | shares msg |
| D7 | alreadyRegistered + treatment code OP/RJ | call Treatment List; create MMV request | MMV request created for admin validation | YES (nested branch) |
| D8 | alreadyRegistered + no OP/RJ | call Treatment List | There is no Benefit Message | YES |
| D9 | planOnlyAcceptReimbursee | — | There is no benefit Message | shares msg |
| D10 | providerInvalid | — | Member cannot use this Provider Message | YES |
| D11 | underAdministrationProcess | — | There is no benefit Message | shares msg |
| D12 | validBpjsFirst | — | There is no benefit Message | shares msg |
| D13 | memberHaveNoBenefit | — | There is no benefit Message | shares msg |
| D14 | benefitLimitExpired | — | Member Expired Message | shares msg |
| D15 | alreadyHaveSettlement + treatment code OP/RJ | call Treatment List; create MMV request | MMV request created for admin validation | same behavior as D7 |
| D16 | alreadyHaveSettlement + no OP/RJ | call Treatment List | There is no Benefit Message | same behavior as D8 |
| D17 | memberNotFound | — | Member Invalid Message | shares msg w/ D3 |
| D18 | birthdayInvalid | — | Member Invalid Message | shares msg w/ D3 |

## Consolidation decisions (same behavior + same outcome + simple passive mapping)
- Simple error statuses that just display a static message with NO system action are consolidated into message-group cases, but EACH status is still exercised as a data-driven step/row so every enum value is proven and individually diagnosable:
  - TC-ERR-INVALID: Invalid, memberNotFound, birthdayInvalid → "Member Invalid Message"
  - TC-ERR-EXPIRED: policyPeriodInvalid, memberPeriodInvalid, benefitLimitExpired → "Member Expired Message"
  - TC-ERR-NOBENEFIT: planOnlyAcceptReimbursee, underAdministrationProcess, validBpjsFirst, memberHaveNoBenefit → "There is no benefit Message"
  - TC-ERR-INACTIVE: Inactive → "Member Inactive Message" (unique)
  - TC-ERR-PROVIDER: providerInvalid → "Member cannot use this Provider Message" (unique)
- alreadyRegistered and alreadyHaveSettlement share identical nested behavior (Treatment List → OP/RJ → MMV vs no-benefit). Consolidated into the treatment-branch cases but both triggering statuses exercised:
  - TC-TREAT-MMV: (alreadyRegistered | alreadyHaveSettlement) + code OP/RJ → MMV request
  - TC-TREAT-NOBENEFIT: (alreadyRegistered | alreadyHaveSettlement) + no OP/RJ → no benefit message
- Membership→MemberType is a separate equivalence set, exercised on the valid happy path (data-driven across 4 classes).

## Test Case Plan
| TC | Covers | Priority | Basis |
|---|---|---|---|
| TC-01 | REQ-001,003,004,005,006,007,008,012 — valid, combination EXISTS → member linked (happy, routing + eligibility call) | High | core business flow, data integrity |
| TC-02 | REQ-002,009,010,011 — valid, combination NOT EXIST → Assigned Plan created from Template w/ naming + defaults | High | data integrity, downstream benefit mapping |
| TC-03 | REQ-013 — Member Type mapping across membership classes (KARYAWAN, SUAMI/ISTRI, ANAK, other) | High | relationship/data integrity |
| TC-04 | REQ-014,026,027 — Member Invalid Message group | Medium | explicit error path |
| TC-05 | REQ-015 — Member Inactive Message | Medium | explicit error path |
| TC-06 | REQ-016,017,024 — Member Expired Message group | Medium | explicit error path |
| TC-07 | REQ-019,021,022,023 — There is no benefit Message group | Medium | explicit error path |
| TC-08 | REQ-020 — provider invalid message | Medium | explicit error path |
| TC-09 | REQ-018,025 (OP/RJ) — Treatment List → MMV request created | High | secondary integration + conditional, MMV creation |
| TC-10 | REQ-018,025 (no OP/RJ) — Treatment List → no benefit message | Medium | conditional branch |

## Coverage Status
- REQ-001 COVERED (TC-01)
- REQ-002 COVERED (TC-02)
- REQ-003 COVERED (TC-01 precondition/step; planCode value AMB-001 noted)
- REQ-004 COVERED (TC-01)
- REQ-005 COVERED (TC-01)
- REQ-006 COVERED (TC-01)
- REQ-007 COVERED (TC-01, TC-02 — combination definition)
- REQ-008 COVERED (TC-01)
- REQ-009 COVERED (TC-02)
- REQ-010 COVERED (TC-02)
- REQ-011 COVERED (TC-02)
- REQ-012 COVERED (TC-01)
- REQ-013 COVERED (TC-03)
- REQ-014 COVERED (TC-04)
- REQ-015 COVERED (TC-05)
- REQ-016 COVERED (TC-06)
- REQ-017 COVERED (TC-06)
- REQ-018 COVERED (TC-09, TC-10)
- REQ-019 COVERED (TC-07)
- REQ-020 COVERED (TC-08)
- REQ-021 COVERED (TC-07)
- REQ-022 COVERED (TC-07)
- REQ-023 COVERED (TC-07)
- REQ-024 COVERED (TC-06)
- REQ-025 COVERED (TC-09, TC-10)
- REQ-026 COVERED (TC-04)
- REQ-027 COVERED (TC-04)

All 15 status enum values exercised. planCode exact behavior = BLOCKED/AMB (not a standalone oracle). Verbatim message strings = asserted by named identity (image-only text).
Reduction method: message-group + behavior-group consolidation with each enum value exercised as data-driven condition. No exhaustive status×membership cross-product (independent factors; membership only meaningful on valid path).
