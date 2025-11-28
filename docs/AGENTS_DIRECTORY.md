# Agents Directory

**Comprehensive catalog of 607+ Enterprise AI Agents organized by domain and functionality**

---

## Overview Statistics

| Metric | Count |
|--------|-------|
| **Total Agents** | 607 |
| **Main Categories** | 7 |
| **Sub-Categories** | 36 |
| **All Agents Categorized** | Yes |

---

## Directory Structure

```
agents/
├── 01-software-engineering/     (274 agents)
│   ├── frontend/
│   │   ├── frameworks/          (119 agents)
│   │   ├── styling/
│   │   └── ui-components/
│   ├── backend/
│   │   ├── languages/           (12 agents)
│   │   ├── frameworks/          (45 agents)
│   │   ├── databases/           (5 agents)
│   │   └── apis-integrations/
│   ├── devops/
│   │   ├── ci-cd/
│   │   ├── containers/
│   │   ├── infrastructure/      (28 agents)
│   │   └── monitoring/
│   ├── testing/
│   │   └── unit-testing/        (37 agents)
│   ├── mobile/                  (12 agents)
│   └── architecture/            (9 agents)
│
├── 02-data-and-ai/              (94 agents)
│   ├── data-engineering/        (3 agents)
│   ├── data-science/            (12 agents)
│   ├── machine-learning/        (80 agents)
│   └── analytics/
│
├── 03-business/                 (66 agents)
│   ├── marketing/               (13 agents)
│   ├── sales/
│   ├── customer-success/        (3 agents)
│   ├── finance/
│   │   └── payments/            (17 agents) - ALL payment integrations here
│   ├── operations/              (13 agents)
│   └── strategy/                (15 agents)
│
├── 04-security-compliance/      (69 agents)
│   ├── application-security/    (34 agents)
│   ├── infrastructure-security/ (4 agents)
│   └── compliance-governance/   (31 agents)
│
├── 05-predictions-forecasting/  (44 agents) - ALL prediction agents here
│   ├── sports/                  (10 agents)
│   ├── market-financial/        (9 agents)
│   ├── social-political/        (6 agents)
│   ├── technology/              (10 agents)
│   └── entertainment/           (9 agents)
│
├── 06-personal-development/     (56 agents)
│   ├── career/                  (14 agents)
│   ├── skills/                  (16 agents)
│   ├── communication/           (8 agents)
│   ├── wellness/                (9 agents)
│   └── relationships/           (9 agents)
│
└── 07-specialized-domains/      (4 agents)
    ├── simulations/             (2 agents)
    ├── industry-verticals/
    └── emerging-tech/           (2 agents)
```

---

## Category Descriptions

### 01 - Software Engineering

All agents related to building software, including:
- **Frontend**: React, Vue, Angular, Svelte, CSS, Tailwind specialists
- **Backend**: Python, Java, Go, Rust, Node.js, Django, Spring specialists
- **DevOps**: Docker, Kubernetes, CI/CD, Terraform, cloud infrastructure
- **Testing**: TDD, unit testing, integration testing, E2E testing
- **Mobile**: iOS, Android, Flutter, React Native specialists
- **Architecture**: System design, patterns, code analysis

### 02 - Data and AI

Data science, machine learning, and analytics agents:
- **Data Engineering**: ETL, pipelines, data architecture
- **Data Science**: Analysis, visualization, statistics
- **Machine Learning**: Models, training, MLOps
- **Analytics**: BI, reporting, insights

### 03 - Business

Business operations and growth agents:
- **Marketing**: Campaigns, SEO, content strategy
- **Sales**: Enablement, CRM, lead generation
- **Customer Success**: Retention, onboarding, support
- **Finance/Payments**: ALL payment integration agents (Stripe, PayPal, etc.)
- **Operations**: Process optimization, workflow
- **Strategy**: Planning, competitive analysis, growth

### 04 - Security and Compliance

Security and compliance agents:
- **Application Security**: Code security, vulnerability scanning
- **Infrastructure Security**: Network, cloud security
- **Compliance Governance**: GDPR, HIPAA, auditing, policies

### 05 - Predictions and Forecasting

ALL prediction and forecasting agents consolidated here:
- **Sports**: Baseball, basketball, football, tennis predictions
- **Market/Financial**: Stock, crypto, economic forecasts
- **Social/Political**: Elections, social movements, demographics
- **Technology**: Tech adoption, AI development, climate
- **Entertainment**: Viral content, movie/music success

### 06 - Personal Development

Personal and professional growth agents:
- **Career**: Job search, transitions, leadership
- **Skills**: Learning, mastery, education
- **Communication**: Public speaking, writing, influence
- **Wellness**: Health, stress, work-life balance
- **Relationships**: Networking, conflict resolution

### 07 - Specialized Domains

Domain-specific and emerging technology agents:
- **Simulations**: Monte Carlo, agent-based, digital twins
- **Industry Verticals**: Healthcare, legal, real estate
- **Emerging Tech**: Quantum, blockchain innovations

---

## Search Options

Use the `agents-search.py` tool to find agents:

```bash
# Search by category
python scripts/agents-search.py --category "backend"
python scripts/agents-search.py --category "predictions"
python scripts/agents-search.py --category "payments"

# Full-text search
python scripts/agents-search.py --query "payment stripe"
python scripts/agents-search.py --query "react testing"

# Show statistics
python scripts/agents-search.py --stats

# List all categories
python scripts/agents-search.py --list-categories

# Generate JSON index
python scripts/agents-search.py --generate-index
```

---

## Key Consolidations

### All Prediction Agents (44 total)
Previously scattered across 8+ folders, now consolidated in:
- `agents/05-predictions-forecasting/`

### All Payment Integration Agents (17 total)
Previously scattered across 5+ folders, now consolidated in:
- `agents/03-business/finance/payments/`

---

## Finding the Right Agent

Use the "First Look Test": Ask yourself "Where would 80% of users look FIRST for this agent?"

| Looking for... | Go to... |
|---------------|----------|
| Payment processing (Stripe, PayPal) | `03-business/finance/payments/` |
| Sports predictions | `05-predictions-forecasting/sports/` |
| Stock/crypto forecasting | `05-predictions-forecasting/market-financial/` |
| React/Vue/Angular | `01-software-engineering/frontend/frameworks/` |
| Docker/Kubernetes | `01-software-engineering/devops/` |
| Security scanning | `04-security-compliance/application-security/` |
| Machine learning models | `02-data-and-ai/machine-learning/` |
| Career development | `06-personal-development/career/` |

---

## Quick Reference

| Category | Path | Agent Count |
|----------|------|-------------|
| Software Engineering | `01-software-engineering/` | 274 |
| Data & AI | `02-data-and-ai/` | 94 |
| Business | `03-business/` | 66 |
| Security & Compliance | `04-security-compliance/` | 69 |
| Predictions & Forecasting | `05-predictions-forecasting/` | 44 |
| Personal Development | `06-personal-development/` | 56 |
| Specialized Domains | `07-specialized-domains/` | 4 |

---

*Reorganized from previous Haiku categorization to fix misclassifications and improve discoverability.*
