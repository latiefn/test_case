# Input Processing Rules

## 1. General

Inspect all provided requirement sources before finalizing test design.

Use structured extraction first. Do not repeatedly reread the same source unless a contradiction, ambiguity, or visual detail requires it.

For large documents, extract text/tables programmatically when possible and inspect only pages/images that add functional evidence.

## 2. Source Types

### Jira (via MCP) — read ticket directly, cache to prd/{TICKET}/
A ticket's requirement can be read directly from Jira through the Atlassian MCP, even when no file exists under `prd/{TICKET}/` yet.

Procedure:
1. Resolve the Atlassian cloudId once per session (cache it), then read the issue with `mcp_atlassian_read_jira_issue` using the ticket key (summary, description, acceptance criteria, status, issue type, priority, labels, components, epic/parent, sprint, reporter/assignee, attachments list, issue links, subtasks, comments).
2. Persist the extracted requirement to `prd/{TICKET}/{TICKET}.md` so later runs do not need another Jira call. Treat this file as a PRD source.
3. Record the ticket key, type, project, sprint, reporter, and fetch context in the saved file.

Execution notes:
- If a read fails with an undefined/missing-field error, retry with a narrower `expand` (for example `fields,comment,attachment,issuelinks`).
- If reads keep failing, sanity-check the connection first with `mcp_atlassian_get_jira_current_user`. A response lacking `accountId` / `displayName`, or showing a placeholder domain, means the integration is not authenticated — report that to the user instead of guessing at ticket content.
- Many tickets carry little detail in the description itself and link out to a PRD (Confluence or elsewhere). Follow those links and scope the reading to the one user story under test; do not test behavior owned by a sibling story or marked out of scope.

Use Jira read for: fetching the ticket when the user names a key but no local PRD exists; confirming metadata (sprint → Folder, reporter); and discovering linked designs/attachments. Do not invent fields Jira did not return. If the ticket references a Figma design, follow the Figma caching rule below. Prefer reading the issue once and reusing the saved `.md`; re-read only to refresh a changed ticket.

### PDF
Extract:
- headings;
- requirement statements;
- acceptance criteria;
- tables/lists;
- functional diagrams;
- screenshots containing functional information.

Preserve page/section references when available.

### Image / Screenshot
Capture only reliably observable:
- visible text;
- labels;
- fields/buttons/toggles;
- visible states;
- validation messages;
- navigation clues;
- data shown in the UI.

Do not infer hidden behavior from appearance alone.

### XML
Extract relevant elements, attributes, values, hierarchy, enums, relationships, and explicit metadata.

### Markdown / Plain Text
Extract requirement statements, acceptance criteria, rules, constraints, states, workflows, examples, and explicit expected behavior.

### Figma (via MCP) — fetch once, cache to Markdown
Figma MCP access is rate-limited (e.g., a View/Collab seat allows only ~20 tool calls/month). To conserve quota:
1. Fetch a Figma file/node from the MCP **only once**.
2. Immediately persist the extracted content to `prd/{TICKET}/figma-content.md`.
3. On later runs, read `prd/{TICKET}/figma-content.md` instead of calling Figma again.

Execution notes:
- Collect Figma URLs from the ticket and the PRD section.
- Read structure with `mcp_figma_get_figma_data`, passing `fileKey` and the `nodeId` from the URL's `node-id` parameter. Convert the URL's `1-70` style to the API's `1:70` style.
- Acceptance criteria are often written as annotation frames inside a Figma section (frequently in GIVEN/WHEN/THEN form). Harvest that text verbatim; it is usually the most precise specification available. The annotation section and the actual UI mockups are commonly separate — explore the canvas (`depth: 1`, then drill in) to find screen frames, dialogs, snackbars, and empty/loading/error states.
- When on-screen copy must be confirmed and the structured node data is not enough, render individual frames to images with `mcp_figma_download_figma_images` (use an absolute `localPath`, render individual frames at scale 2 rather than a whole huge section so text stays legible) and read them. Record exact UI strings; expected results must quote real copy, not paraphrase. Treat an image render as a Figma call that counts against quota — only do it when the structured cache is insufficient.

The Figma response is structured node data, not just text — so the cache MUST capture enough to build UI-shape test cases, not only message strings. Record, per screen/section:
- **Message copy** — titles, body, labels, button/CTA text (EN and any other locale present), with verbatim strings quoted.
- **UI elements** — fields/inputs, buttons/CTAs, icons, toggles, and visible states/variants (e.g., error vs success, 1st/2nd time, iOS/Android, enabled/disabled).
- **Flow hints** — in-screen steppers, navigation arrows, connector lines, and cross-flow links that indicate transitions between screens. Mark these as design indications, NOT guaranteed sequential test steps — do not invent a complete flow the design does not show.

The cache file MUST also record: file name, file key, node id, URL, "Fetched at" date, and the referencing ticket. Treat it as part of the PRD source (same priority as other `prd/{TICKET}/` content).

The cached Markdown is sufficient for functional UI test cases (which elements exist, what text shows, which buttons/states appear, how screens transition). Only pure visual verification (exact color, pixel spacing, font rendering) needs a rendered image — download a PNG/SVG (one new call) to `prd/{TICKET}/` only when such visual checking is explicitly required.

Refresh (one new fetch) only when: the design changed, the cache is missing required detail, or a screenshot is explicitly needed. Prefer fetching specific node ids over whole files, and batch needs into a single call. A stale cache (design changed) must be re-fetched and the "Fetched at" date updated.

## 3. Multiple Sources

When sources overlap:
- identify duplicates;
- retain the most precise wording;
- preserve all source references;
- detect contradictions.

Do not merge conflicting behavior into an invented interpretation.

## 4. Evidence Classes

Classify source evidence as:
- `EXPLICIT` — directly stated;
- `DERIVED` — produced by a recognized test-design technique from explicit behavior;
- `ASSUMPTION` — allowed only if explicitly approved;
- `UNKNOWN` — insufficient evidence.

Only `EXPLICIT` and valid `DERIVED` evidence may directly create normal test conditions.

## 5. Efficient Extraction

Build one compact source inventory and one normalized requirement catalog.

Do not create separate prose analyses that repeat the same source content.

Record only information that can affect scope, test design, expected results, priority, or traceability.
