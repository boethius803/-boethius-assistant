# Handoff Packets - Agent Handoff Protocol

When passing work to another agent or session, include:

```
1. Goal (one sentence)
2. Current state (what's already true)
3. Next action (the very next concrete step)
4. Constraints (hard rules, safety, deadlines)
5. Known unknowns (what to verify)
6. Artifacts/paths/links (where the work lives)
7. Stop conditions (when to halt + ask for help)
```

## Example

```
Goal: Complete Python scraper for e-commerce
Current state: HTML parsing done, need to extract price fields
Next action: Write price extraction regex for product cards
Constraints: Must handle missing prices gracefully, output CSV
Known unknowns: Whether site uses JavaScript for prices
Artifacts: /workspace/scraper/parser.py
Stop conditions: If 3 retries fail, ask for help
```
