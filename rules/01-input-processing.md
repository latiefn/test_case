# Input Processing Rules

## 1. General

Inspect all provided requirement sources before finalizing test design.

Use structured extraction first. Do not repeatedly reread the same source unless a contradiction, ambiguity, or visual detail requires it.

For large documents, extract text/tables programmatically when possible and inspect only pages/images that add functional evidence.

## 2. Source Types

### Jira (via MCP) — read ticket directly, cache to prd/{TICKET}/
A ticket's requirement can be read directly from Jira through the Atlassian MCP, even when no file exists under `prd/{TICKET}/` yet.

Procedure:
1. Resolve the Atlassian cloudId once per session (cache it), then read the issue (summary, description, acceptance criteria, status, sprint, reporter/assignee, attachments list, issue links, subtasks).
2. Persist the extracted requirement to `prd/{TICKET}/{TICKET}.md` so later runs do not need another Jira call. Treat this file as a PRD source.
3. Record the ticket key, type, project, sprint, reporter, and fetch context in the saved file.

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
2. Immediately persist the extracted content (message copy, labels, states, structure) to `prd/{TICKET}/figma-content.md`.
3. On later runs, read `prd/{TICKET}/figma-content.md` instead of calling Figma again.

The cache file MUST record: file name, file key, node id, URL, "Fetched at" date, and the referencing ticket. Treat it as part of the PRD source (same priority as other `prd/{TICKET}/` content).

Refresh (one new fetch) only when: the design changed, the cache is missing required detail, or a PNG/SVG screenshot is explicitly needed. Prefer fetching specific node ids over whole files, and batch needs into a single call. A stale cache (design changed) must be re-fetched and the "Fetched at" date updated.

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
