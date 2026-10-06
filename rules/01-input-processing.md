# Input Processing Rules

## 1. General

Inspect every provided PRD source before generating test cases.

When multiple sources are provided, treat them as potentially related and resolve their relationships before generation.

A Senior QA reads ALL sources completely before writing a single test case.

## 2. PDF

Extract:
- headings;
- paragraphs;
- tables;
- lists;
- acceptance criteria;
- diagrams when functional;
- embedded images containing requirements.

Preserve page or section references when available.

Do not treat decorative content as a requirement.

## 3. Images / Screenshots

Extract only information that is reliably observable:
- visible text;
- labels;
- buttons;
- fields;
- UI states;
- validation messages;
- navigation clues;
- diagrams;
- data structures shown in UI;
- setting names and their visible states (enabled/disabled, checked/unchecked).

Do not infer hidden behavior from appearance alone.

If text is unreadable, mark it as uncertain rather than inventing it.

**Senior QA tip**: Screenshots often reveal implicit requirements that the text PRD missed — field ordering, validation placement, toggle groupings, navigation paths.

## 4. XML

Parse:
- elements;
- attributes;
- values;
- hierarchy;
- metadata relevant to behavior;
- enumeration values;
- data types;
- relationships between elements.

Do not interpret technical metadata as a business rule unless the source establishes that relationship.

**Senior QA tip**: XML PRDs often contain structured requirement data. Pay attention to element hierarchies — they reveal entity relationships and data structures that drive test design.

## 5. Markdown / Plain Text

Extract:
- headings;
- tables;
- lists;
- acceptance criteria;
- examples;
- business rules;
- constraints;
- explicit expected behavior;
- state definitions;
- entity descriptions.

## 6. Multiple Sources

When sources overlap:
- identify duplicate requirements;
- preserve the most precise wording;
- retain source traceability;
- detect contradictions.

Do not merge conflicting requirements into one invented interpretation.

**Senior QA tip**: Cross-reference text PRDs with screenshots. The screenshots may show features not mentioned in the text, and vice versa. Both are requirements.

## 7. Source Evidence

Every normalized requirement should retain:
- source name;
- location if available;
- original wording or a faithful summary.

This enables later traceability and validation.

## 8. Extraction Confidence

Distinguish:
- explicit requirement;
- clearly inferred relationship;
- uncertain interpretation.

Only explicit requirements may directly establish product behavior.

A derived test scenario is acceptable only when the derivation follows a standard test-design technique from an explicit rule, without inventing product behavior.

## 9. Comprehensive Extraction Checklist

A Senior QA extracts ALL of the following from every PRD:

- [ ] Functional requirements (what the system does)
- [ ] Business rules (conditional logic, calculations, routing)
- [ ] UI elements (fields, buttons, labels, toggles, states)
- [ ] Validation rules (input constraints, format rules)
- [ ] Error conditions (what can go wrong, error responses)
- [ ] User roles and permissions
- [ ] Data constraints (types, ranges, required fields)
- [ ] Integration points (what connects to what)
- [ ] State definitions (ON/OFF, active/inactive, enabled/disabled)
- [ ] Configuration settings (what can be configured, valid values)
- [ ] Workflows (multi-step processes, sequences)
- [ ] Backward compatibility requirements (migration, preservation)
- [ ] Non-impact statements (what should NOT change)
- [ ] Data lifecycle rules (creation, storage, consumption, update)
- [ ] Eligibility/qualification criteria
- [ ] Routing rules (which path/benefit applies in which context)
