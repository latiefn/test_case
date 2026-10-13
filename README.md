# QA Test Case Generation System

This repository is the persistent source of truth for AI-assisted test-case generation.

Pipeline:

`Input Sources → PRD → Extraction → Requirement Analysis → Trigger-Based Test Design → Coverage Closure → XLSX → Validation`

Input sources feeding the PRD stage:
- local files under `prd/{TICKET}/` (PDF, image, XML, Markdown, plain text);
- a Jira ticket read via the Atlassian MCP, then cached to `prd/{TICKET}/{TICKET}.md`;
- a referenced Figma design read once via the Figma MCP, then cached to `prd/{TICKET}/figma-content.md`.

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
- `work/{TICKET}/` — compact persistent generation artifacts (`analysis.md`, `coverage.md`, `validation.md`, and the `generate.py` used to build the XLSX)
- `prd/{TICKET}/` — requirement sources: local files plus MCP caches (`{TICKET}.md` from Jira, `figma-content.md` from Figma)
- `output/` — generated XLSX (`output/{TICKET}.xlsx`)

## Input Sources (MCP)

Tickets and designs can be pulled on demand and cached so later runs do not re-call the MCP:

- **Jira (Atlassian MCP):** read the issue when no local PRD exists; save the extracted requirement to `prd/{TICKET}/{TICKET}.md` and treat it as a PRD source. Resolve the cloudId once per session and reuse it.
- **Figma MCP:** fetch a referenced design once and cache the extracted content to `prd/{TICKET}/figma-content.md`. Capture three layers per screen so the cache supports UI-shape test cases, not only text: message copy; UI elements (fields, buttons/CTAs, icons, states/variants); and flow hints (steppers, arrows, connectors, cross-flow links — design indications, not guaranteed test steps). Reuse that file instead of calling Figma again — MCP access is rate-limited (a View/Collab seat allows only ~20 calls/month). Record file key, node id, URL, and fetch date; the cache is enough for functional UI test cases, and only pure visual checks (color/pixel/layout) need a re-fetch for a screenshot.

Never invent fields a source did not return.

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
