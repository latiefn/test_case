# test_case_md_v2_corrected

This archive is the corrected replacement pack for the lean QA test-case generation rules discussed in the conversation.

## Replaced / revised files

- `AGENTS.md`
- `README.md`
- `rules/00-core-principles.md`
- `rules/01-input-processing.md`
- `rules/02-requirement-analysis.md`
- `rules/03-test-design-techniques.md`
- `rules/04-test-case-rules.md`
- `rules/05-coverage-rules.md`
- `rules/07-template-rules.md`
- `rules/08-output-xlsx-rules.md`
- `rules/09-validation-rules.md`
- `rules/10-ambiguity-and-assumption.md`
- `rules/11-scope-model-and-coverage-closure.md`
- `workflow/generation-workflow.md`
- `workflow/validation-workflow.md`
- `examples/good-test-case.md`

## Included unchanged reference files

- `rules/06-priority-rules.md`
- `schemas/test-case-schema.md`
- `examples/bad-test-case.md`

## Intent

The revised rules use adaptive test-design triggers instead of forcing every ticket through every QA coverage dimension. Detailed coverage analysis is reserved for conditions where the requirement or project risk actually activates it.

This pack is an overlay for the existing repository. It does not include XLSX templates, project-specific context, source PRDs, or generated output files.
