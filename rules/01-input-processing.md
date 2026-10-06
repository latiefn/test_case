# Input Processing Rules

## 1. General

Inspect all provided requirement sources before finalizing test design.

Use structured extraction first. Do not repeatedly reread the same source unless a contradiction, ambiguity, or visual detail requires it.

For large documents, extract text/tables programmatically when possible and inspect only pages/images that add functional evidence.

## 2. Source Types

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
