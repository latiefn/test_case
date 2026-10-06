import openpyxl
from openpyxl import Workbook

HEADER = ['Key','Summary','Description','Requirement Keys','Test Type','Automation Content',
          'Epic Key','Fix Versions','Status','Priority','Assignee','Reporter','Labels',
          'Test Category','Components','Precondition','Folder','Step Description','Step Data','Expected Result']

TICKET = 'PLM-1005'
EPIC = 'Linking-Unlinking Process Benefit Management'
REPORTER = 'Latief'
FOLDER = '2026/2026 Sprint 20/PLM-1005'
REQ = 'PLM-1005'

# Each case: meta dict + list of steps (step_desc, step_data, expected)
cases = []

cases.append({
    'summary': '[TC][PLM-1005] Verify automatic linking succeeds and member is linked to existing Assigned Plan when eligibility status is valid and plan combination exists',
    'description': 'Validate the valid happy path: card routed to Meditap (AGG-0006), Member Eligibility is called, existing Assigned Plan combination is reused, and the member is created and linked with details mapped from the API. Coverage: REQ-001/003/004/005/006/007/008/012.',
    'priority': 'High',
    'precondition': 'Channel Management toggle routes the card number to AGG-0006 (Meditap, Production). An Assigned Plan already exists for the combination Aggregator=Meditap (AGG-0006) + Payor=insurance + Corporate=policyHolderName (matched case-insensitive) returned by the API. Meditap API Member Eligibility By Card Number is reachable and returns response.code=0000, data.status=valid.',
    'steps': [
        ('User/Partner from the plugin sends the linking request to the System.', 'Body: {cardNo:<valid member code>, planCode:<TM/OP>, birthDate:<DOB>}', 'Request is accepted and processed by the System.'),
        ('System determines the card number belongs to AGG-0006 (Meditap, Production) based on the Channel Management toggle and calls Meditap API Member Eligibility By Card Number.', '<valid cardNo>', 'System routes to AGG-0006 and calls the Member Eligibility By Card Number API; API returns response.code=0000, data.status=valid.'),
        ('System checks the Assigned Plan combination Aggregator=Meditap (AGG-0006) + Payor=insurance + Corporate=policyHolderName (case-insensitive) and finds an existing match.', 'Payor=insurance (from API), Corporate=policyHolderName (from API)', 'Existing Assigned Plan with the matching combination is identified; no new Assigned Plan is created.'),
        ('System creates the member, attaches the matched Assigned Plan, and populates member details from the API response.', 'Full Name=name, Gender=gender, Additional Policy/Card Number=policyNo, Policy Coverage Start Date=member creation date, Policy Coverage End Date=empty', 'Member is created and linked to the existing Assigned Plan with the mapped fields; Policy Coverage End Date is empty.'),
        ('Observe the linking result returned to the user.', '', 'Success message is displayed to the user.'),
    ],
})

cases.append({
    'summary': '[TC][PLM-1005] Verify Assigned Plan is auto-created from Template with correct naming and defaults when valid status and plan combination does not exist',
    'description': 'Validate the valid path where the Assigned Plan combination does not exist: System creates an Assigned Plan from the Template Assigned Plan, applies the Plan naming format and default field values, then creates the member. Coverage: REQ-002/009/010/011.',
    'priority': 'High',
    'precondition': 'Channel Management toggle routes the card to AGG-0006 (Meditap, Production). No Assigned Plan exists yet for the combination Aggregator=Meditap (AGG-0006) + Payor=insurance + Corporate=policyHolderName returned by the API. A Template Assigned Plan is configured. Meditap Member Eligibility returns response.code=0000, data.status=valid.',
    'steps': [
        ('Send the linking request for a card whose plan combination is not yet present on any Assigned Plan.', 'Body: {cardNo:<valid member code>, planCode:<TM/OP>, birthDate:<DOB>}', 'System calls Member Eligibility; API returns data.status=valid.'),
        ('System checks the Assigned Plan combination (Meditap AGG-0006 + Payor + Corporate) and finds no match, then rechecks the Template Assigned Plan.', 'Payor=insurance, Corporate=policyHolderName', 'No existing Assigned Plan combination is found; System proceeds to create from the Template Assigned Plan.'),
        ('System creates a Plan using the naming format Plan_<Aggregator>_<Payment Model>_<Coshare covered on benefit>_<Benefit names covered>, applying default Payment Mode PPU and benefit renames (Prescription->Rx, Delivery Fee->Delivery).', 'Example expected form: Plan_Meditap_PPU_80%_GP SP Rx Delivery', 'Plan is created with the documented naming format and default Payment Mode PPU; Prescription is shown as Rx and Delivery Fee as Delivery.'),
        ('System creates the Assigned Plan from the newly created Plan with the documented defaults.', 'Contract Start Date=Assigned Plan creation date, Contract End Date=empty, Care Model=Standard', 'Assigned Plan is created with Contract Start Date=creation date, Contract End Date empty, and Care Model=Standard.'),
        ('System creates the member and attaches the newly created Assigned Plan.', 'Member details mapped from API response', 'Member is created and linked to the new Assigned Plan; success message is displayed.'),
    ],
})

cases.append({
    'summary': '[TC][PLM-1005] Verify Member Type and relationship are mapped correctly from membership value during linking',
    'description': 'Validate equivalence mapping of API membership to Member Type/Relationship on member creation during a valid linking. Coverage: REQ-013.',
    'priority': 'High',
    'precondition': 'A valid linking is in progress (data.status=valid) with a resolved Assigned Plan. The API returns a membership value for the member.',
    'steps': [
        ('Perform linking where API membership = KARYAWAN.', 'membership=KARYAWAN', 'Member is created with Member Type=Principal.'),
        ('Perform linking where API membership = SUAMI/ISTRI KARYAWAN.', 'membership=SUAMI/ISTRI KARYAWAN', 'Member is created with Member Type=Dependant, Relationship=Spouse, Principal Member Code=empty.'),
        ('Perform linking where API membership = ANAK KARYAWAN.', 'membership=ANAK KARYAWAN', 'Member is created with Member Type=Dependant, Relationship=Child, Principal Member Code=empty.'),
        ('Perform linking where API membership is any other value.', 'membership=<other value>', 'Member is created with Member Type=Principal (default/else branch).'),
    ],
})

cases.append({
    'summary': '[TC][PLM-1005] Verify Member Invalid Message is displayed for invalid, memberNotFound, and birthdayInvalid statuses',
    'description': 'Validate the error path producing the Member Invalid Message. Coverage: REQ-014/026/027.',
    'priority': 'Medium',
    'precondition': 'Channel Management toggle routes the card to AGG-0006 (Meditap, Production); Meditap Member Eligibility is reachable and returns response.code=0000 with the status under test.',
    'steps': [
        ('Send a linking request where Member Eligibility returns data.status=Invalid.', 'data.status=Invalid', 'System displays the error Member Invalid Message; no member or Assigned Plan is created.'),
        ('Send a linking request where Member Eligibility returns data.status=memberNotFound.', 'data.status=memberNotFound', 'System displays the Member Invalid Message.'),
        ('Send a linking request where Member Eligibility returns data.status=birthdayInvalid.', 'data.status=birthdayInvalid', 'System displays the Member Invalid Message.'),
    ],
})

cases.append({
    'summary': '[TC][PLM-1005] Verify Member Inactive Message is displayed when eligibility status is Inactive',
    'description': 'Validate the error path for inactive member. Coverage: REQ-015.',
    'priority': 'Medium',
    'precondition': 'Channel Management toggle routes the card to AGG-0006; Meditap Member Eligibility returns response.code=0000, data.status=Inactive.',
    'steps': [
        ('Send a linking request where Member Eligibility returns data.status=Inactive.', 'data.status=Inactive', 'System displays the error Member Inactive Message; no member or Assigned Plan is created.'),
    ],
})

cases.append({
    'summary': '[TC][PLM-1005] Verify Member Expired Message is displayed for policyPeriodInvalid, memberPeriodInvalid, and benefitLimitExpired statuses',
    'description': 'Validate the error path producing the Member Expired Message. Coverage: REQ-016/017/024.',
    'priority': 'Medium',
    'precondition': 'Channel Management toggle routes the card to AGG-0006; Meditap Member Eligibility returns response.code=0000 with the status under test.',
    'steps': [
        ('Send a linking request where Member Eligibility returns data.status=policyPeriodInvalid.', 'data.status=policyPeriodInvalid', 'System displays the error Member Expired Message.'),
        ('Send a linking request where Member Eligibility returns data.status=memberPeriodInvalid.', 'data.status=memberPeriodInvalid', 'System displays the error Member Expired Message.'),
        ('Send a linking request where Member Eligibility returns data.status=benefitLimitExpired.', 'data.status=benefitLimitExpired', 'System displays the error Member Expired Message.'),
    ],
})

cases.append({
    'summary': '[TC][PLM-1005] Verify There is no benefit Message is displayed for planOnlyAcceptReimbursee, underAdministrationProcess, validBpjsFirst, and memberHaveNoBenefit statuses',
    'description': 'Validate the error path producing the There is no benefit Message. Coverage: REQ-019/021/022/023.',
    'priority': 'Medium',
    'precondition': 'Channel Management toggle routes the card to AGG-0006; Meditap Member Eligibility returns response.code=0000 with the status under test.',
    'steps': [
        ('Send a linking request where Member Eligibility returns data.status=planOnlyAcceptReimbursee.', 'data.status=planOnlyAcceptReimbursee', 'System displays the There is no benefit Message.'),
        ('Send a linking request where Member Eligibility returns data.status=underAdministrationProcess.', 'data.status=underAdministrationProcess', 'System displays the There is no benefit Message.'),
        ('Send a linking request where Member Eligibility returns data.status=validBpjsFirst.', 'data.status=validBpjsFirst', 'System displays the There is no benefit Message.'),
        ('Send a linking request where Member Eligibility returns data.status=memberHaveNoBenefit.', 'data.status=memberHaveNoBenefit', 'System displays the There is no benefit Message.'),
    ],
})

cases.append({
    'summary': '[TC][PLM-1005] Verify Member cannot use this Provider Message is displayed when status is providerInvalid',
    'description': 'Validate the error path for provider invalid. Coverage: REQ-020.',
    'priority': 'Medium',
    'precondition': 'Channel Management toggle routes the card to AGG-0006; Meditap Member Eligibility returns response.code=0000, data.status=providerInvalid.',
    'steps': [
        ('Send a linking request where Member Eligibility returns data.status=providerInvalid.', 'data.status=providerInvalid', 'System displays the error Member cannot use this Provider Message.'),
    ],
})

cases.append({
    'summary': '[TC][PLM-1005] Verify MMV validation request is created when alreadyRegistered/alreadyHaveSettlement and treatment list contains code OP or RJ',
    'description': 'Validate the nested branch: on alreadyRegistered or alreadyHaveSettlement, System calls Treatment List by Card Number and, when a treatment with code OP or RJ exists, creates an MMV request for admin validation. Coverage: REQ-018/025 (OP/RJ branch).',
    'priority': 'High',
    'precondition': 'Channel Management toggle routes the card to AGG-0006; Meditap Member Eligibility returns the status under test; Treatment List by Card Number is reachable and returns at least one treatment with code OP or RJ.',
    'steps': [
        ('Send a linking request where Member Eligibility returns data.status=alreadyRegistered.', 'data.status=alreadyRegistered', 'System calls Treatment List by Card Number.'),
        ('System evaluates the treatment list and finds a treatment with code OP or RJ.', 'Treatment list contains code=OP or code=RJ', 'System creates a request to MMV for an admin to validate.'),
        ('Repeat the linking request where Member Eligibility returns data.status=alreadyHaveSettlement with a treatment list containing code OP or RJ.', 'data.status=alreadyHaveSettlement; treatment code=OP or RJ', 'System calls Treatment List and creates a request to MMV for admin validation (same behavior as alreadyRegistered).'),
    ],
})

cases.append({
    'summary': '[TC][PLM-1005] Verify There is no Benefit Message is displayed when alreadyRegistered/alreadyHaveSettlement and treatment list has no code OP or RJ',
    'description': 'Validate the nested branch: on alreadyRegistered or alreadyHaveSettlement, when Treatment List contains no treatment with code OP or RJ, System displays the There is no Benefit Message. Coverage: REQ-018/025 (no OP/RJ branch).',
    'priority': 'Medium',
    'precondition': 'Channel Management toggle routes the card to AGG-0006; Meditap Member Eligibility returns the status under test; Treatment List by Card Number is reachable and returns no treatment with code OP or RJ.',
    'steps': [
        ('Send a linking request where Member Eligibility returns data.status=alreadyRegistered.', 'data.status=alreadyRegistered', 'System calls Treatment List by Card Number.'),
        ('System evaluates the treatment list and finds no treatment with code OP or RJ.', 'Treatment list has no code=OP and no code=RJ', 'System displays the There is no Benefit Message.'),
        ('Repeat the linking request where Member Eligibility returns data.status=alreadyHaveSettlement with a treatment list containing no code OP or RJ.', 'data.status=alreadyHaveSettlement; no treatment code OP/RJ', 'System displays the There is no Benefit Message (same behavior as alreadyRegistered).'),
    ],
})

wb = Workbook()
ws = wb.active
ws.title = 'Tests'
ws.append(HEADER)

def row_for(meta, step, first):
    r = [None]*20
    if first:
        r[1] = meta['summary']
        r[2] = meta['description']
        r[3] = REQ
        r[6] = EPIC
        r[9] = meta['priority']
        r[11] = REPORTER
        r[13] = 'Manual'
        r[15] = meta['precondition']
        r[16] = FOLDER
    r[17] = step[0]
    r[18] = step[1] if step[1] else None
    r[19] = step[2]
    return r

for meta in cases:
    for i, step in enumerate(meta['steps']):
        ws.append(row_for(meta, step, i == 0))

import os
os.makedirs('output', exist_ok=True)
wb.save('output/PLM-1005.xlsx')
print('Saved output/PLM-1005.xlsx with', len(cases), 'cases')
