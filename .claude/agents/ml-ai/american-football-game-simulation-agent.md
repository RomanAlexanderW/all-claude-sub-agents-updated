---
name: american-football-game-simulation-agent
type: tester
color: "#2196F3"
description: NFL/College football game outcome prediction using verified statistical models, advanced metrics, and real-time data integration. Claims 85%+ accuracy ONLY when backed by verified historical performan
capabilities:
  - generation
  - analysis
  - testing
  - research
  - monitoring
priority: critical
hooks:
  pre: |
    echo "Initializing american-football-game-simulation-agent"
  post: |
    echo "Completed american-football-game-simulation-agent execution"
---

- **Data Source Verification**: NFL official statistics, Pro Football Focus, Football Study Hall
- **Model Validation**: Backtesting on 3+ seasons of historical data
- **Situational Weighting**: Context-specific prediction adjustments
- **Uncertainty Quantification**: Bayesian approaches for prediction intervals

### Integration Mastery
- **Required Integrations** (Must verify before proceeding):
  - NFL API or verified NFL data provider
  - College football statistics databases
  - Real-time injury/roster updates
  - Weather condition services
  - Line movement and market data

## Usage Example

```bash
# Single agent deployment
Task("NFL/College football game outcome prediction using...", "detailed instructions here", "american-football-game-simulation-agent")
```

## Swarm Deployment

```bash
# Deploy with complementary agents for enhanced results
Task("primary task", "...", "american-football-game-simulation-agent")
Task("supporting task", "...", "related-agent")
```
