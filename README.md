# QA Test Case Generation System

## 1. Purpose

This repository defines the persistent QA methodology for generating software test cases from PRD (Product Requirement Documents).

The target pipeline is:

`PRD → Requirement Extraction → Requirement Analysis → Test Design → Test Case Generation → Validation → XLSX`

The system is designed for AI agents that may operate without access to previous conversations.

## 2. Repository Structure

```text
.
├── AGENTS.md
├── README.md
├── rules/
│   ├── 00-core-principles.md
│   ├── 01-input-processing.md
│   ├── 02-requirement-analysis.md
│   ├── 03-test-design-techniques.md
│   ├── 04-test-case-rules.md
│   ├── 05-coverage-rules.md
│   ├── 06-priority-rules.md
│   ├── 07-template-rules.md
│   ├── 08-output-xlsx-rules.md
│   ├── 09-validation-rules.md
│   ├── 10-ambiguity-and-assumption.md
│   └── 11-scope-model-and-coverage-closure.md
├── workflow/
│   ├── generation-workflow.md
│   └── validation-workflow.md
├── schemas/
│   └── test-case-schema.md
├── template/
│   ├── Test Case template.xlsx    ← Current XLSX structure / import contract
│   └── PLM-659.xlsx               ← Older content and writing-style reference
├── context/
│   └── project-context.md
├── examples/
│   ├── good-test-case.md
│   └── bad-test-case.md
├── prd/
│   └── <TICKET>/                  ← PRD input files per ticket
└── output/
    └── <TICKET>.xlsx              ← Generated test case output
```

## 3. Rule Files

| File | Responsibility |
|---|---|
| `00-core-principles.md` | Fundamental QA rules |
| `01-input-processing.md` | Reading and extracting PRD sources |
| `02-requirement-analysis.md` | Requirement normalization and traceability |
| `03-test-design-techniques.md` | Test design methods |
| `04-test-case-rules.md` | Test-case writing standards |
| `05-coverage-rules.md` | Coverage model |
| `06-priority-rules.md` | Priority classification |
| `07-template-rules.md` | XLSX template handling |
| `08-output-xlsx-rules.md` | XLSX output requirements |
| `09-validation-rules.md` | Final quality validation |
| `10-ambiguity-and-assumption.md` | Missing/conflicting requirement handling |
| `11-scope-model-and-coverage-closure.md` | Scope model, traceability, reduction, deduplication, and completion gate |

## 4. Template Files

`template/Test Case template.xlsx` is the current import contract. Its `Tests` sheet has 20 columns, including `Test Type` and `Automation Content`. Always inspect the workbook at run time rather than relying only on this description.

`template/PLM-659.xlsx` is an older 18-column reference. Use its test-case content for writing patterns only. It must not override the current template's columns, order, field constraints, or current project instructions.

## 5. Workflow Files

`workflow/generation-workflow.md` defines the end-to-end generation process from PRD to XLSX.

`workflow/validation-workflow.md` defines independent validation of generated test cases.

## 6. Schema

`schemas/test-case-schema.md` defines the logical structure of a test case and its mapping to the physical XLSX template columns.

## 7. Project Context

`context/project-context.md` contains project-specific conventions. It must not be used to invent product behavior that is absent from current requirements.

## 8. Examples

The examples demonstrate the expected quality level and common failure modes.

## 9. Core Philosophy

The system optimizes for:

`Meaningful Coverage + Traceability + Executability + Risk Coverage - Redundancy`

The number of generated test cases is not a quality metric by itself.

A smaller, well-designed test suite is preferable to a large set of repetitive or speculative cases.

## 10. Persistent Context

The repository is the source of truth for QA generation methodology.

Do not assume information from previous sessions remains available.

Always reload the relevant files before performing substantive QA generation work.
