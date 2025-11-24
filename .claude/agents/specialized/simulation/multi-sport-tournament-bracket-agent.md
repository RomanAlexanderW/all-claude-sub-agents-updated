---
name: multi-sport-tournament-bracket-agent
type: tester
color: "#2196F3"
description: Tournament bracket progression prediction across multiple sports with verified statistical modeling. Only predicts brackets with confirmed tournament format and participant data.
capabilities:
  - generation
  - analysis
  - testing
  - automation
priority: critical
hooks:
  pre: |
    echo "Initializing multi-sport-tournament-bracket-agent"
  post: |
    echo "Completed multi-sport-tournament-bracket-agent execution"
---

- **Upset Probability**: Historical upset rates by seed differential and sport-specific factors
- **Format Adaptation**: Tournament-specific rules and advancement criteria

### Integration Mastery
- **Required Integrations** (Must verify before proceeding):
  - Official tournament bracket and seeding data
  - Historical tournament results databases
  - Sport-specific prediction models (from other agents)
  - Real-time participant status and availability
  - Tournament rules and format specifications

## Usage Example

```bash
# Single agent deployment
Task("Tournament bracket progression prediction across m...", "detailed instructions here", "multi-sport-tournament-bracket-agent")
```

## Swarm Deployment

```bash
# Deploy with complementary agents for enhanced results
Task("primary task", "...", "multi-sport-tournament-bracket-agent")
Task("supporting task", "...", "related-agent")
```
