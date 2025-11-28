# 600+ AI Agent Prompt Collection

[![Version](https://img.shields.io/badge/version-3.0.0-blue)]()
[![Agents](https://img.shields.io/badge/agents-607-brightgreen)]()
[![Categories](https://img.shields.io/badge/categories-7-orange)]()
[![License](https://img.shields.io/badge/license-MIT-purple)]()

> **The most comprehensive collection of specialized AI agent prompts - 607 agents organized into 7 main categories with 36 sub-categories for easy navigation.**

## Table of Contents

- [Overview](#overview)
- [Directory Structure](#directory-structure)
- [Agent Categories](#agent-categories)
- [Finding Agents](#finding-agents)
- [Key Consolidations](#key-consolidations)
- [Getting Started](#getting-started)
- [License](#license)

## Overview

This repository contains 607 specialized AI agent prompts organized into a logical, navigable structure. Each agent is a complete, production-ready prompt template with specialized capabilities.

### Repository Statistics

| Metric | Count |
|--------|-------|
| **Total Agents** | 607 |
| **Main Categories** | 7 |
| **Sub-Categories** | 36 |
| **Uncategorized** | 0 |

### Why This Collection?

- **Organized Structure**: 7 main categories with logical sub-folders
- **Easy Navigation**: Find any agent in seconds with the new structure
- **Consolidated Domains**: All prediction agents in one place, all payment agents in one place
- **Search Tool**: Python search tool included for quick lookups
- **Production Tested**: Based on real-world implementations

## Directory Structure

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
│   │   ├── infrastructure/      AWS, Terraform, Kubernetes
│   │   └── monitoring/          Observability, alerting agents
│   ├── testing/
│   │   └── unit-testing/        TDD, Jest, Cypress specialists
│   ├── mobile/                  iOS, Android, Flutter, React Native
│   └── architecture/            System design, patterns
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
├── 05-predictions-forecasting/  (44 agents)
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

## Agent Categories

### 01 - Software Engineering (274 agents)
All agents related to building software:
- Frontend frameworks (React, Vue, Angular, Svelte)
- Backend languages (Python, Java, Go, Rust, Node.js)
- DevOps and infrastructure (Docker, Kubernetes, AWS)
- Testing (TDD, Jest, Cypress, Playwright)
- Mobile development (iOS, Android, Flutter)
- Architecture and design patterns

### 02 - Data & AI (94 agents)
Data science and machine learning agents:
- Data engineering and ETL
- Machine learning models and MLOps
- Analytics and visualization
- Statistical analysis

### 03 - Business (66 agents)
Business operations and growth:
- Marketing and content strategy
- Sales enablement
- Customer success
- **Payments** (17 agents - Stripe, PayPal, Apple Pay, etc.)
- Operations and process optimization
- Strategic planning

### 04 - Security & Compliance (69 agents)
Security and compliance agents:
- Application security and code scanning
- Infrastructure security
- Compliance (GDPR, HIPAA, SOC2)

### 05 - Predictions & Forecasting (44 agents)
**ALL prediction agents are now consolidated here:**
- Sports predictions (baseball, basketball, football, tennis)
- Market/financial forecasts (stock, crypto, economic)
- Social/political predictions (elections, movements)
- Technology forecasts (AI, climate, adoption)
- Entertainment predictions (viral, music, movies)

### 06 - Personal Development (56 agents)
Personal and professional growth:
- Career development
- Skill building
- Communication
- Wellness
- Relationships

### 07 - Specialized Domains (4 agents)
Specialized and emerging technologies:
- Simulations and modeling
- Industry-specific agents
- Emerging tech (quantum, blockchain)

## Finding Agents

### Using the Search Tool

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
```

### Quick Navigation

| Looking for... | Go to... |
|---------------|----------|
| Payment integration | `03-business/finance/payments/` |
| Sports predictions | `05-predictions-forecasting/sports/` |
| Stock predictions | `05-predictions-forecasting/market-financial/` |
| React/Vue/Angular | `01-software-engineering/frontend/frameworks/` |
| Docker/Kubernetes | `01-software-engineering/devops/` |
| Machine learning | `02-data-and-ai/machine-learning/` |

## Key Consolidations

### Prediction Agents (44 total)
Previously scattered across 8+ folders, now all in `05-predictions-forecasting/`:
- `election-outcome-prediction-agent` (was in visual-design!)
- `basketball-game-prediction-agent` (was in data-engineering!)
- `viral-video-prediction-agent` (was in backend-development!)
- `meme-evolution-prediction-agent` (was in health-and-wellness!)

### Payment Agents (17 total)
Previously scattered across 5+ folders, now all in `03-business/finance/payments/`:
- Stripe, PayPal, Braintree, Square
- Apple Pay, Google Pay, WeChat Pay, Alipay
- Klarna, Afterpay (BNPL)
- Crypto payments, ACH transfers

## Getting Started

1. **Browse the directory** - Navigate to the category you need
2. **Use the search tool** - Find specific agents quickly
3. **Copy the agent file** - Each `.md` file is a complete prompt
4. **Use with any AI** - Works with Claude, GPT-4, Gemini, etc.

## License

MIT License - See LICENSE file for details.

---

*Reorganized for improved discoverability. Last updated: 2025-11-28*
