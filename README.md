# QA Test Case Generation System

This repository is the persistent source of truth for AI-assisted test-case generation.

Pipeline:

`PRD → Extraction → Requirement Analysis → Trigger-Based Test Design → Coverage Closure → XLSX → Validation`

## Design Goal

Optimize for:

`Meaningful Coverage + Traceability + Executability + Risk Coverage - Redundancy - Unnecessary Analysis`

The system must not treat test-case count or analysis volume as a quality metric.

## Repository Structure

- `AGENTS.md` — routing and global behavior
- `rules/` — focused QA rules
- `workflow/` — generation and validation sequence
- `schemas/` — logical/physical output contract
- `template/` — current XLSX template and historical writing reference
- `context/` — project-specific facts/conventions
- `examples/` — writing examples and failure examples
- `work/{TICKET}/` — compact persistent generation artifacts
- `prd/{TICKET}/` — requirement sources
- `output/` — generated XLSX

## Core Principle

Do not apply every testing dimension to every requirement.

Activate deeper techniques only when the requirement contains the relevant trigger or the project provides concrete risk evidence.

Examples:
- explicit range → boundary testing;
- 2+ conditions jointly determine outcome → decision table;
- explicit state model → transition testing;
- explicit roles → permission testing;
- changed existing data/behavior → regression/compatibility testing;
- large independent combination space → constrained pairwise/high-risk coverage.

## Traceability

Every test case must trace to an authoritative requirement/condition.

Every requirement/condition must end as `COVERED`, `CONSOLIDATED`, `BLOCKED`, or `NOT APPLICABLE`.

## Historical Reference

`template/PLM-659.xlsx` is a writing-style reference only. The current XLSX template always wins for structure and import format.
