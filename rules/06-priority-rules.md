# Test Case Priority Rules

## Priority Levels

Use only the priority values supported by the template. If the template uses High/Medium/Low, apply the following definitions.

### High

Use when failure could affect:
- critical business flow;
- authentication;
- authorization;
- financial/transactional behavior;
- data integrity;
- security-sensitive functionality;
- regulatory/compliance requirements;
- critical integration;
- primary user journey.

### Medium

Use for:
- important secondary functionality;
- standard business validation;
- alternate workflows;
- non-critical integrations;
- meaningful negative scenarios.

### Low

Use for:
- low-impact edge cases;
- minor secondary behavior;
- low-risk scenarios.

## Rules

Priority must be based on business or technical risk, not on:
- test-case position;
- ease of testing;
- personal preference;
- number of steps.

Do not assign High merely because a feature sounds important.

If risk information is absent, use the documented project convention. If no convention exists, avoid pretending that risk is known.

## Risk Evidence

Record the basis for priority in the internal risk assessment. Consider documented impact, exposure/likelihood, data or financial integrity, security/privacy/compliance, integration complexity, blast radius, and recoverability.

Every `High` priority test must cite a clear risk basis in its Description or linked internal condition. Do not default all cases to `Medium`, inflate all cases to `High`, or infer business criticality from ticket wording alone.

Risk controls test depth and ordering, but it never permits an explicit testable requirement to be omitted.
