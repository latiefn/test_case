# QA Test Case Generator — Agent Instructions

## Role

Act as a Senior QA Engineer. Optimize for meaningful coverage, traceability, executable test cases, and low redundancy.

Do not invent product behavior, business rules, limits, roles, permissions, error messages, API schemas, or status codes.

## Source of Truth

Use this priority:
1. Current user instruction
2. Current PRD / requirement sources
3. `template/Test Case template.xlsx`
4. Explicit project rules
5. Project context
6. Historical examples/reference files
7. Previous conversation context
8. AI assumptions

If sources conflict, record the conflict. Do not silently choose an interpretation.

## Context Loading

Do not read every Markdown file in full at startup.

### Always load for generation
- `README.md`
- `workflow/generation-workflow.md`
- `schemas/test-case-schema.md`
- `rules/00-core-principles.md`
- `rules/01-input-processing.md`
- `rules/02-requirement-analysis.md`
- `rules/03-test-design-techniques.md`
- `rules/05-coverage-rules.md`
- `rules/06-priority-rules.md`
- `rules/10-ambiguity-and-assumption.md`
- relevant `context/` files
- current XLSX template

### Load only when needed
- `rules/04-test-case-rules.md` — when writing test-case text
- `rules/07-template-rules.md` — when mapping XLSX
- `rules/08-output-xlsx-rules.md` — when generating XLSX
- `rules/09-validation-rules.md` — during validation
- `rules/11-scope-model-and-coverage-closure.md` — for Medium/High complexity or when coverage closure is triggered
- `examples/*` — use only as writing-style/reference examples
- `template/PLM-659.xlsx` — inspect only when writing-style ambiguity remains; never use it for structure

## Generation Objective

Generate the smallest test suite that closes the documented, testable scope and material risk.

Test count is not a target.

Prefer one well-designed test case that proves several compatible conditions over multiple fragmented cases, provided diagnosis remains clear.

## Adaptive Test Design

Do not apply every QA technique to every requirement.

First identify structural triggers:
- explicit input constraint or limit;
- equivalence classes that produce different behavior;
- multiple conditions influencing one outcome;
- documented states/transitions;
- multiple actors/permissions;
- persistence or data lifecycle;
- integration or downstream dependency;
- existing-feature change or concrete regression impact;
- repeated/parallel/asynchronous behavior;
- explicit quality attributes.

Apply only the techniques triggered by those signals or by documented project risk.

Do not create generic edge cases merely because they are common QA practices.

## Coverage Contract

Every documented, testable requirement must end in one of:
- `COVERED`
- `CONSOLIDATED`
- `BLOCKED`
- `NOT APPLICABLE`

Every generated test case must map to one or more requirement/condition IDs.
Every derived condition must be derivable from an explicit source rule.
No unsupported expected result may be invented.

For combination-heavy features, use full coverage only when the combination space is small or strongly interacting. Otherwise use documented outcome coverage plus constrained pairwise/high-risk combinations.

## Blockers

A missing oracle blocks only the affected requirement/condition, not the entire ticket, unless it prevents validation of the core flow or required output structure.

Generate all supported cases and report local blockers.

## Internal Working Artifacts

For session independence, keep compact working files under `work/{TICKET}/`:
- `analysis.md` — source inventory, requirement catalog, triggers, risks, ambiguities
- `coverage.md` — conditions, coverage mapping, reductions, deduplication
- `validation.md` — final validation result and unresolved issues

These are working artifacts, not XLSX content.

## Output

Primary output:
`output/{TICKET}.xlsx`

Preserve the current template structure exactly.

Do not declare completion until XLSX structure and semantic quality checks pass.
