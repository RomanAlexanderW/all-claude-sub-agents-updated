# Claude Code Configuration - Agent Repository

## CRITICAL: CONCURRENT EXECUTION & FILE MANAGEMENT

**ABSOLUTE RULES**:
1. ALL operations MUST be concurrent/parallel in a single message
2. **NEVER save working files, text/mds and tests to the root folder**
3. ALWAYS organize files in appropriate subdirectories

### GOLDEN RULE: "1 MESSAGE = ALL RELATED OPERATIONS"

**MANDATORY PATTERNS:**
- **TodoWrite**: ALWAYS batch ALL todos in ONE call (5-10+ todos minimum)
- **Task tool**: ALWAYS spawn ALL agents in ONE message with full instructions
- **File operations**: ALWAYS batch ALL reads/writes/edits in ONE message
- **Bash commands**: ALWAYS batch ALL terminal operations in ONE message

### File Organization Rules

**NEVER save to root folder. Use these directories:**
- `/src` - Source code files
- `/tests` - Test files
- `/docs` - Documentation and markdown files
- `/config` - Configuration files
- `/scripts` - Utility scripts
- `/examples` - Example code

---

## Agent Repository Overview

**Total Agents**: 607
**Main Categories**: 7
**All Agents Categorized**: Yes

---

## Agent Directory Structure

```
agents/
├── 01-software-engineering/     (274 agents)
│   ├── frontend/
│   │   ├── frameworks/          React, Vue, Angular, Svelte specialists
│   │   ├── styling/             CSS, Tailwind, Sass specialists
│   │   └── ui-components/       Material-UI, design systems
│   ├── backend/
│   │   ├── languages/           Python, Java, Go, Rust specialists
│   │   ├── frameworks/          Django, Spring, Express specialists
│   │   ├── databases/           PostgreSQL, MongoDB, Redis specialists
│   │   └── apis-integrations/   REST, GraphQL integration agents
│   ├── devops/
│   │   ├── ci-cd/               Pipeline specialists
│   │   ├── containers/          Docker, Kubernetes specialists
│   │   ├── infrastructure/      AWS, Terraform specialists
│   │   └── monitoring/          Observability agents
│   ├── testing/
│   │   └── unit-testing/        TDD, Jest, Cypress specialists
│   ├── mobile/                  iOS, Android, Flutter, React Native
│   └── architecture/            System design, patterns, analysis
│
├── 02-data-and-ai/              (94 agents)
│   ├── data-engineering/        ETL, pipelines, data architecture
│   ├── data-science/            Analysis, visualization, statistics
│   ├── machine-learning/        Models, training, MLOps (80 agents)
│   └── analytics/               BI, reporting, insights
│
├── 03-business/                 (66 agents)
│   ├── marketing/               Campaigns, SEO, content strategy
│   ├── sales/                   Enablement, CRM, lead generation
│   ├── customer-success/        Retention, onboarding, support
│   ├── finance/
│   │   └── payments/            ALL 17 payment integration agents
│   ├── operations/              Process optimization, workflow
│   └── strategy/                Planning, competitive analysis
│
├── 04-security-compliance/      (69 agents)
│   ├── application-security/    Code security, vulnerability scanning
│   ├── infrastructure-security/ Network, cloud security
│   └── compliance-governance/   GDPR, HIPAA, auditing, policies
│
├── 05-predictions-forecasting/  (44 agents)  ← ALL prediction agents
│   ├── sports/                  Baseball, basketball, football, tennis
│   ├── market-financial/        Stock, crypto, economic forecasts
│   ├── social-political/        Elections, social movements
│   ├── technology/              AI development, climate, trends
│   └── entertainment/           Viral content, music, movies
│
├── 06-personal-development/     (56 agents)
│   ├── career/                  Job search, transitions, leadership
│   ├── skills/                  Learning, mastery, education
│   ├── communication/           Public speaking, writing, influence
│   ├── wellness/                Health, stress, work-life balance
│   └── relationships/           Networking, conflict resolution
│
└── 07-specialized-domains/      (4 agents)
    ├── simulations/             Monte Carlo, agent-based models
    ├── industry-verticals/      Healthcare, legal, real estate
    └── emerging-tech/           Quantum, blockchain innovations
```

---

## Key Agent Categories

### Most Used Development Agents
- `python-specialist` - Python 3.12+ development
- `react-19-specialist` - Modern React development
- `typescript-specialist` - Type-safe development
- `nodejs-specialist` - Server-side JavaScript
- `aws-cloud-architect` - Cloud infrastructure

### Payment Integration Agents (03-business/finance/payments/)
All payment agents consolidated in one location:
- `stripe-integration-agent`
- `paypal-integration-agent`
- `apple-pay-integration-agent`
- `google-pay-integration-agent`
- `square-integration-agent`
- `braintree-integration-agent`
- `klarna-bnpl-integration-agent`
- `afterpay-bnpl-integration-agent`
- And 9 more...

### Prediction Agents (05-predictions-forecasting/)
All prediction agents consolidated by domain:
- **Sports**: `baseball-outcome-forecasting-agent`, `basketball-game-prediction-agent`
- **Financial**: `stock-price-movement-predictor`, `cryptocurrency-volatility-agent`
- **Social**: `election-outcome-prediction-agent`, `social-movement-prediction-agent`
- **Tech**: `technology-adoption-prediction-agent`, `ai-development-timeline-agent`
- **Entertainment**: `viral-video-prediction-agent`, `music-hit-prediction-agent`

---

## Agent Search Tool

Use the search tool to find agents quickly:

```bash
# Search by category
python scripts/agents-search.py --category "backend"
python scripts/agents-search.py --category "predictions"
python scripts/agents-search.py --category "payments"

# Full-text search
python scripts/agents-search.py --query "payment stripe"

# Show statistics
python scripts/agents-search.py --stats

# List all categories
python scripts/agents-search.py --list-categories
```

---

## Claude Code vs MCP Tools

### Claude Code Handles ALL Execution:
- File operations (Read, Write, Edit, MultiEdit, Glob, Grep)
- Code generation and programming
- Bash commands and system operations
- Implementation work
- Project navigation and analysis
- TodoWrite and task management
- Git operations
- Package management
- Testing and debugging

### MCP Tools ONLY Coordinate:
- Swarm initialization (topology setup)
- Agent type definitions (coordination patterns)
- Task orchestration (high-level planning)
- Memory management
- Neural features
- Performance tracking

**KEY**: MCP coordinates the strategy, Claude Code's Task tool executes with real agents.

---

## Quick Setup

```bash
# Add Claude Flow MCP server
claude mcp add claude-flow npx claude-flow@alpha mcp start
```

---

## Support

- Documentation: https://github.com/ruvnet/claude-flow
- Issues: https://github.com/ruvnet/claude-flow/issues

---

Remember: **Claude Flow coordinates, Claude Code creates!**

# important-instruction-reminders
Do what has been asked; nothing more, nothing less.
NEVER create files unless they're absolutely necessary for achieving your goal.
ALWAYS prefer editing an existing file to creating a new one.
NEVER proactively create documentation files (*.md) or README files. Only create documentation files if explicitly requested by the User.
Never save working files, text/mds and tests to the root folder.
