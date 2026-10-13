---
inclusion: auto
name: jira-figma-to-tricentis-test-cases
description: Reusable workflow for turning a Jira ticket (plus its linked PRD and Figma designs) into detailed English test cases delivered as an .xlsx file that matches the team's Tricentis/Xray-style Excel template. Use when asked to create, generate, or write test cases from a Jira ticket, Jira issue key, PRD, or Figma design, or to produce a test case Excel file.
---

# Jira + Figma → Test Case Excel Workflow

Reusable process for producing test cases from a Jira ticket and its design
references, delivered in the team's Excel template format.

## Reference template

Use the team's existing test case workbook as the structural reference:

```
/Users/cahya.reza/Documents/GDT - Test Cases/[TC][Fast Reply Template] Global Configuration Fast Reply Template.xlsx
```

Treat it as read-only. Never overwrite it, and never overwrite previously
generated output workbooks. Always write to a new file.

`.xlsx` is a binary ZIP of XML, so it cannot be read with plain text tools.
Read it with `openpyxl` (see Phase 5) or by unzipping and parsing
`xl/worksheets/sheet1.xml` against `xl/sharedStrings.xml`.

---

## Phase 1 — Read the Jira ticket

- Read the issue with `mcp_atlassian_read_jira_issue` using the ticket key.
- Capture: summary, description, acceptance criteria, status, issue type,
  priority, labels, components, epic/parent, comments, attachments, and links.
- If a call fails with an undefined/missing field error, retry with a narrower
  `expand` (for example `fields,comment,attachment,issuelinks`).
- Sanity-check the connection first with `mcp_atlassian_get_jira_current_user`
  if reads fail. A response lacking `accountId` / `displayName`, or showing a
  placeholder domain, means the integration is not authenticated. Report that
  to the user instead of guessing at ticket content.
- Many tickets carry little detail in the description itself and instead link
  out to a PRD. Follow those links.

## Phase 2 — Read the linked PRD or documentation

- Read linked Confluence pages with `mcp_atlassian_read_confluence_page`
  (`format: markdown` is easiest to scan).
- Locate the section that corresponds to the specific ticket. A PRD often
  covers an entire epic across multiple phases and user stories, so scope the
  reading to the one user story under test.
- Extract the user story, acceptance criteria, business rules, permissions/roles,
  and anything explicitly marked out of scope or deferred to a later phase.
- Note what belongs to sibling stories. Do not test another story's behavior.

## Phase 3 — Analyze the Figma design

- Collect Figma URLs from the ticket and the PRD section.
- Read structure with `mcp_figma_get_figma_data`, passing `fileKey` and the
  `nodeId` from the URL's `node-id` parameter (convert `1-70` style to `1:70`).
- Acceptance criteria are often written as annotation frames inside a Figma
  section (frequently in GIVEN/WHEN/THEN form). Harvest that text verbatim; it
  is usually the most precise specification available.
- The annotation section and the actual UI mockups are commonly separate.
  Explore the canvas (`depth: 1` then drill in) to find the screen frames,
  dialogs, snackbars, and empty/loading/error states.
- Render frames to images with `mcp_figma_download_figma_images` and read them
  to confirm on-screen copy: labels, column headers, dialog titles and body
  text, button labels, toast/snackbar messages, and status values. Use an
  absolute `localPath`, and render individual frames (scale 2) rather than a
  whole huge section, so text stays legible.
- Record exact UI strings. Expected results should quote real copy, not
  paraphrase.

## Phase 4 — Derive scenarios, then confirm before building

Identify scenarios across these categories, but only where the sources support
them:

- **Positive / happy path** — the primary flow completes successfully.
- **Negative** — cancel, dismiss, or abort paths, and unavailable actions.
- **Validation** — required fields, character limits, enable/disable rules.
- **State-based** — behavior per entity state, per role, and per permission,
  including list/table and empty-state presentation.

Then:

1. Present the full set of test cases as a table or structured text for review
   **before** generating any file.
2. Call out scenarios you deliberately skipped because no source supports them.
3. Wait for approval, then build the workbook.

## Phase 5 — Author test cases in the template format

### Column structure (A:R, exact order)

| Col | Header | Notes |
|-----|--------|-------|
| A | Key | Leave empty; populated on Jira/Xray import |
| B | Summary | Test title |
| C | Description | One sentence on the test's purpose |
| D | Requirement Keys | The Jira ticket key under test |
| E | Epic Key | Epic/parent key when known |
| F | Fix Versions | Usually empty |
| G | Status | Usually empty |
| H | Priority | e.g. `Medium` |
| I | Assignee | Confirm with the user |
| J | Reporter | Confirm with the user |
| K | Labels | Usually empty |
| L | Test Category | Usually empty |
| M | Components | Usually empty |
| N | Precondition | Role + starting state |
| O | Folder | Test repository path |
| P | Step Description | The action to perform |
| Q | Step Data | Input data; empty when not needed |
| R | Expected Result | Expected outcome |

### Multi-step row structure

- Each test case begins on a row carrying the full metadata in columns B–O.
- That same row also holds **step 1** in P/Q/R.
- Every additional step is its own row with **B–O left blank** and only
  P, Q, R populated. This is the standard one-row-per-step layout.
- Keep empty-by-design columns empty rather than inserting placeholders.

### Writing style

- **Summary:** `[TC][<Feature/Story Name>] <what is verified>`, typically
  starting with "Verify".
- **Description:** a single sentence — "Ensures…", "Confirms…", "Validates…".
- **Precondition:** short lines for role and starting state, multiple
  conditions separated by real newlines (`\n`), not literal `\n` text.
- **Step Description:** imperative voice — "Open…", "Click…", "Fill…",
  "Observe…", "Input…".
- **Step Data:** `Field : value`, one field per line.
- **Expected Result:** outcome-focused; multiple assertions on separate lines;
  quote actual UI copy; `-` bullets for listing displayed elements.
- Write everything in English unless the user asks otherwise.
- Match the template's own punctuation habits (it mixes straight and curly
  quotes; either is acceptable).

### Guardrails

- Never invent requirements, UI behavior, copy, validation rules, error states,
  sprint numbers, or folder paths. Every assertion must trace back to Jira, the
  PRD, or Figma.
- If the **sprint or folder path** cannot be confirmed from Jira or the PRD,
  **ask the user before generating the final Excel file.** Folder paths in this
  team follow a `<year>/<year> Sprint <n>/<Feature>/<Story>` pattern, and the
  sprint is rarely derivable from the ticket.
- Confirm Assignee, Reporter, and Epic Key with the user when they are not
  stated in the ticket.
- Exclude behavior owned by a different user story, and behavior the PRD marks
  out of scope.

## Phase 6 — Generate the .xlsx

Prefer `openpyxl` over hand-building XLSX XML. If `openpyxl` is unavailable,
tell the user and offer options before proceeding — do not silently fall back
to CSV when Excel was requested.

Set up an isolated environment with a pinned version:

```bash
python3 -m venv ~/.venv-tc-xlsx
~/.venv-tc-xlsx/bin/python -m pip install "openpyxl==3.1.5"
```

A venv avoids the PEP 668 "externally managed environment" error that blocks
installing into a Homebrew Python, and leaves the system interpreter untouched.
Mention that the venv can be removed afterwards.

Generation approach that preserves formatting:

1. `shutil.copyfile(template, destination)` — inherits column widths, header
   fill, fonts, and wrap settings.
2. Load the copy, then clear values from row 2 down while leaving styling
   intact (set `cell.value = None`; do not delete rows).
3. Write the new rows, applying the template's body style: Calibri 11,
   `wrap_text=True`, `vertical='center'` (the Precondition column also uses
   `horizontal='left'`).
4. Save to a new filename, for example
   `[TC][<Feature>] <Story Name>.xlsx`.

## Phase 7 — Verify before reporting

Re-open the saved file and confirm:

- The file opens successfully and the ZIP is intact; the expected sheet
  (e.g. `Tests`) is present.
- Header row A1:R1 matches the template exactly, including fill and wrap.
- Column widths carried over from the template.
- No leftover example data from the template.
- Test case count and per-test-case step counts match the approved set.
- Metadata appears only on each test case's first row; continuation rows carry
  only P/Q/R.
- Requirement Keys, Epic Key, Priority, Assignee, and Reporter are populated on
  every test case.
- Every step row has both a Step Description and an Expected Result.

Report a pass/fail summary. If any value in the saved file differs from what
was approved, flag it explicitly rather than glossing over it.

Clean up temporary scripts when finished, and give the user the **exact
absolute file path** of the generated workbook.
