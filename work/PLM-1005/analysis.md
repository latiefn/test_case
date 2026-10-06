# PLM-1005 — Analysis

## Source Inventory
- `prd/PLM-1005/PLM-1005.xml` — Jira Story export (PRIMARY requirement source).
- `prd/PLM-1005/[#PLM-1005] Automatic Linking via API Meditap version 2.0.pdf` — same ticket PDF (overlaps XML; not re-read, XML is machine-readable).
- Attachments referenced but not available as text: API Documentation PDF, Figma, Google Sheet sample. Message screenshots referenced only by image.

## Ticket Metadata
- Key: PLM-1005 | Type: Story | Parent: PLM-1002 | Epic: "Linking-Unlinking Process Benefit Management"
- Priority (ticket): Medium | Status: Backlog | Sprint: Platform Sprint 20 | Reporter: Adam Graphiandana | Assignee: Daffa Zaky
- Year: 2026 | Folder: `2026/2026 Sprint 20/PLM-1005`

## Feature Summary
Automatic member linking via Meditap API v2.0. User/Partner (plugin) requests linking with body {cardNo, planCode (TM/OP, hardcoded TBC), birthDate}. System routes card to AGG-0006 (Meditap, Production) via Channel Management toggle, then calls Meditap API `Member Eligibility By Card Number`. System reacts to `data.status`.

## Atomic Requirement Catalog
| ID | Requirement | Source | Evidence |
|---|---|---|---|
| REQ-001 | DoD: user can link automatically via API Meditap | DoD #1 | EXPLICIT |
| REQ-002 | DoD: system creates new Assigned Plan from Assigned Plan Template automatically during linking | DoD #2 | EXPLICIT |
| REQ-003 | Linking request body = {cardNo, planCode<TM/OP>, birthDate} | Scenario body | EXPLICIT (planCode hardcoded TBC) |
| REQ-004 | System routes card to AGG-0006 (Meditap, Production), determined by Channel Management toggle | System Flow #2 | EXPLICIT |
| REQ-005 | System calls Meditap API `Member Eligibility By Card Number` | System Flow #3 | EXPLICIT |
| REQ-006 | status=valid: happy path — assigned plan resolution + member creation | Use Case table row valid | EXPLICIT |
| REQ-007 | Assigned Plan combination check = Aggregator(Meditap AGG-0006) + Payor(insurance, case-insensitive) + Corporate(policyHolderName, case-insensitive) | Use Case valid #1 | EXPLICIT |
| REQ-008 | If combination exists on Assigned Plan → proceed to member creation | Use Case valid #2 | EXPLICIT |
| REQ-009 | If combination not exist → recheck Template Assigned Plan, create Assigned Plan from Template | Use Case valid #3 | EXPLICIT |
| REQ-010 | Plan naming format: Plan_<Aggregator>_<PaymentModel>_<Coshare>_<Benefits>; default Payment Mode PPU; Prescription→Rx; Delivery Fee→Delivery; example Plan_Meditap_PPU_80%_GP SP Rx Delivery | Use Case valid #3.b | EXPLICIT |
| REQ-011 | Created Assigned Plan defaults: Contract Start = creation date, Contract End = empty, Care Model = Standard | Use Case valid #3.c | EXPLICIT |
| REQ-012 | Member creation field mapping: Full Name=name, Gender=gender, Additional Policy/Card No=policyNo, Policy Coverage Start=creation member date, Policy Coverage End=empty | Use Case valid #4 | EXPLICIT |
| REQ-013 | Member Type by membership: KARYAWAN→Principal; SUAMI/ISTRI KARYAWAN→Dependant/Spouse/PrincipalCode empty; ANAK KARYAWAN→Dependant/Child/PrincipalCode empty; Else→Principal | Use Case valid #4.f | EXPLICIT |
| REQ-014 | status=Invalid → Display error Member Invalid Message | Use Case table | EXPLICIT |
| REQ-015 | status=Inactive → Display error Member Inactive Message | Use Case table | EXPLICIT |
| REQ-016 | status=policyPeriodInvalid → Display error Member Expired Message | Use Case table | EXPLICIT |
| REQ-017 | status=memberPeriodInvalid → Display error Member Expired Message | Use Case table | EXPLICIT |
| REQ-018 | status=alreadyRegistered → call Treatment List by Card Number; if code OP or RJ → create MMV request for admin to validate; else → Display There is no Benefit Message | Use Case table | EXPLICIT |
| REQ-019 | status=planOnlyAcceptReimbursee → Display There is no benefit Message | Use Case table | EXPLICIT |
| REQ-020 | status=providerInvalid → Display error Member cannot use this Provider Message | Use Case table | EXPLICIT |
| REQ-021 | status=underAdministrationProcess → Display There is no benefit Message | Use Case table | EXPLICIT |
| REQ-022 | status=validBpjsFirst → Display There is no benefit Message | Use Case table | EXPLICIT |
| REQ-023 | status=memberHaveNoBenefit → Display There is no benefit Message | Use Case table | EXPLICIT |
| REQ-024 | status=benefitLimitExpired → Display error Member Expired Message | Use Case table | EXPLICIT |
| REQ-025 | status=alreadyHaveSettlement → call Treatment List by Card Number; if code OP or RJ → create MMV request; else → Display There is no Benefit Message | Use Case table | EXPLICIT |
| REQ-026 | status=memberNotFound → Display Member Invalid Message | Use Case table | EXPLICIT |
| REQ-027 | status=birthdayInvalid → Display Member Invalid Message | Use Case table | EXPLICIT |

Note: all rows carry response.code = 0000; branching is driven by `data.status`.

## Trigger Analysis
- Decision table / multi-condition outcome: YES — `data.status` enum (15 values) + nested branching for alreadyRegistered/alreadyHaveSettlement (treatment code OP/RJ). PRIMARY driver.
- Equivalence partitioning: YES — membership classes → Member Type mapping (4 classes).
- Business rule / data creation: YES — Assigned Plan existence check + Template-based creation + naming format + defaults.
- Data lifecycle/persistence: YES — member + assigned plan creation and field mapping.
- Integration: YES — Meditap API Member Eligibility + Treatment List; routing via Channel Management toggle (AGG-0006).
- Boundary: NO explicit numeric limits/ranges defined.
- Role/permission: Partial — "admin to validate" via MMV, but admin role behavior not defined here → out of scope for this ticket's oracle.
- State transition: NO explicit state machine beyond status→outcome mapping (covered by decision table).

## Complexity
HIGH — large interacting condition space (15 status enum + nested treatment-code branch + membership classes + plan existence branch + template creation), integration dependency, data creation lifecycle.

## Risk Notes
- Happy path (valid): HIGH — core business flow, creates persistent member + assigned plan; data integrity + downstream benefit validation (the whole initiative's purpose).
- Assigned Plan creation + naming + defaults: HIGH — data integrity, downstream benefit mapping; error-prone formatting.
- Member Type mapping: HIGH — determines Principal/Dependant relationship; data integrity.
- Routing to AGG-0006 via toggle: Medium — integration precondition.
- Error status mappings: Medium — explicit user-facing messages; distinct diagnosis per outcome but several share same message.
- Treatment-list nested branch (alreadyRegistered / alreadyHaveSettlement): High — MMV request creation, secondary integration + conditional outcome.

## Ambiguity / Blocker Log
- AMB-001 (planCode TM/OP "Hardcoded, TBC (?)"): behavior of planCode on outcome is undefined. Not a testable oracle on its own → documented as not-covered input note; linking outcome driven by API status, not planCode. NOT A CORE BLOCKER.
- AMB-002: exact message text/strings are provided only as Figma screenshots (images), not as text in XML. Oracle = message identity by name ("Member Invalid Message", "Member Inactive Message", "Member Expired Message", "There is no benefit Message", "Member cannot use this Provider Message", success message). Tests assert the named message/outcome, not verbatim string → acceptable oracle; verbatim text BLOCKED where it would require the image.
- AMB-003: "Expected Outcome to User [WIP]" column header flagged WIP — the user-facing outcomes for valid and most error rows ARE provided in the table; WIP noted but does not remove the explicit mappings.
- AMB-004: Channel Management toggle setup is a precondition; its own config UI is out of scope (covered as precondition only).
- AMB-005: MMV request internal structure / admin validation flow not defined in this ticket (PLM-1006 action item) → assert "MMV request created for admin validation" as outcome; deeper MMV behavior NOT APPLICABLE here.
- AMB-006: "Principal Member Code: empty" for dependants looks unusual (dependant normally references a principal) but is stated explicitly → test asserts as documented; flagged as a possible PRD inconsistency, not invented.
