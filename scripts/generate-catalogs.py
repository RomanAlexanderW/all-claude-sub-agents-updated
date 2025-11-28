#!/usr/bin/env python3
"""
Generate Markdown catalogs, LLM.txt, and JSON files for the agent repository.
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime

AGENTS_DIR = Path("agents")
CATALOGS_DIR = Path("Agents-Catalogs")

# Category mapping
CATEGORIES = {
    "01-software-engineering": {
        "name": "Software Engineering",
        "subcategories": ["frontend", "backend", "devops", "testing", "mobile", "architecture"]
    },
    "02-data-and-ai": {
        "name": "Data & AI",
        "subcategories": ["data-engineering", "data-science", "machine-learning", "analytics"]
    },
    "03-business": {
        "name": "Business",
        "subcategories": ["marketing", "sales", "customer-success", "finance", "operations", "strategy"]
    },
    "04-security-compliance": {
        "name": "Security & Compliance",
        "subcategories": ["application-security", "infrastructure-security", "compliance-governance"]
    },
    "05-predictions-forecasting": {
        "name": "Predictions & Forecasting",
        "subcategories": ["sports", "market-financial", "social-political", "technology", "entertainment"]
    },
    "06-personal-development": {
        "name": "Personal Development",
        "subcategories": ["career", "skills", "communication", "wellness", "relationships"]
    },
    "07-specialized-domains": {
        "name": "Specialized Domains",
        "subcategories": ["simulations", "industry-verticals", "emerging-tech"]
    }
}


def parse_agent_file(filepath):
    """Parse an agent markdown file and extract metadata."""
    try:
        content = filepath.read_text(encoding='utf-8')
        name_match = re.search(r'^name:\s*(.+)$', content, re.MULTILINE)
        desc_match = re.search(r'^description:\s*(.+)$', content, re.MULTILINE)

        name = name_match.group(1).strip() if name_match else filepath.stem
        description = desc_match.group(1).strip() if desc_match else ""

        # Clean up name
        display_name = name.replace('-', ' ').replace('_', ' ').title()

        return {
            "filename": filepath.name,
            "name": name,
            "display_name": display_name,
            "description": description[:200] + "..." if len(description) > 200 else description,
            "path": str(filepath.relative_to(AGENTS_DIR))
        }
    except Exception as e:
        return None


def get_agents_in_category(category_path):
    """Get all agents in a category directory."""
    agents = []
    for md_file in category_path.rglob("*.md"):
        if md_file.name in ["README.md", "CLAUDE.md"]:
            continue
        agent = parse_agent_file(md_file)
        if agent:
            agents.append(agent)
    return sorted(agents, key=lambda x: x["name"])


def generate_category_catalog(category_id, category_info):
    """Generate markdown catalog for a category."""
    category_path = AGENTS_DIR / category_id
    if not category_path.exists():
        return None

    agents = get_agents_in_category(category_path)

    md_content = f"""# {category_info['name']} Agents Catalog

> **{len(agents)} specialized AI agents** for {category_info['name'].lower()}

---

## Overview

| Metric | Value |
|--------|-------|
| **Total Agents** | {len(agents)} |
| **Category** | {category_info['name']} |
| **Path** | `agents/{category_id}/` |

---

## Agents by Sub-Category

"""

    # Group agents by subcategory
    subcats = defaultdict(list)
    for agent in agents:
        parts = agent["path"].split("/")
        if len(parts) >= 2:
            subcat = parts[1] if len(parts) > 2 else "general"
        else:
            subcat = "general"
        subcats[subcat].append(agent)

    for subcat in sorted(subcats.keys()):
        subcat_agents = subcats[subcat]
        md_content += f"\n### {subcat.replace('-', ' ').title()} ({len(subcat_agents)} agents)\n\n"
        md_content += "| Agent | Description |\n"
        md_content += "|-------|-------------|\n"
        for agent in subcat_agents:
            desc = agent["description"][:100] + "..." if len(agent["description"]) > 100 else agent["description"]
            md_content += f"| `{agent['name']}` | {desc} |\n"

    md_content += f"""
---

## All Agents List

| Agent Name | Path | Description |
|------------|------|-------------|
"""

    for agent in agents:
        desc = agent["description"][:80] + "..." if len(agent["description"]) > 80 else agent["description"]
        md_content += f"| {agent['display_name']} | `{agent['path']}` | {desc} |\n"

    md_content += f"\n---\n\n*Generated: {datetime.now().strftime('%Y-%m-%d')}*\n"

    return md_content, agents


def generate_llm_txt():
    """Generate LLM.txt for the entire repository."""
    all_agents = []
    category_counts = {}

    for category_id in CATEGORIES:
        category_path = AGENTS_DIR / category_id
        if category_path.exists():
            agents = get_agents_in_category(category_path)
            all_agents.extend(agents)
            category_counts[category_id] = len(agents)

    llm_content = """# AI Agent Repository - LLM Context File

## Purpose
This file provides a concise summary of the 607+ AI agent prompts in this repository for LLM consumption.

## Repository Structure

```
agents/
├── 01-software-engineering/  (274 agents) - Development, DevOps, Testing
├── 02-data-and-ai/           (94 agents)  - ML, Data Science, Analytics
├── 03-business/              (66 agents)  - Marketing, Sales, Payments
├── 04-security-compliance/   (69 agents)  - AppSec, Compliance
├── 05-predictions-forecasting/ (44 agents) - Sports, Financial, Tech Predictions
├── 06-personal-development/  (56 agents)  - Career, Skills, Wellness
└── 07-specialized-domains/   (4 agents)   - Simulations, Emerging Tech
```

## Key Agent Categories

### Software Engineering (274 agents)
- Frontend: React, Vue, Angular, Svelte, Next.js specialists
- Backend: Python, Java, Go, Rust, Node.js specialists
- DevOps: Docker, Kubernetes, AWS, Terraform specialists
- Testing: Jest, Cypress, Playwright, TDD specialists

### Data & AI (94 agents)
- Machine Learning: PyTorch, TensorFlow specialists
- Data Science: Analysis, visualization, statistics

### Business (66 agents)
- Marketing & Sales specialists
- **Payment Integration**: 17 agents (Stripe, PayPal, Apple Pay, etc.)

### Predictions & Forecasting (44 agents)
- Sports: Baseball, basketball, football, tennis predictions
- Financial: Stock, crypto, economic forecasts
- Technology: AI development, climate, trends

## Agent Format
Each agent is a markdown file with:
- name: Agent identifier
- description: Agent capabilities and use cases
- Full system prompt for the specialized agent

## Usage
1. Navigate to the appropriate category folder
2. Find the agent matching your use case
3. Copy the agent prompt for use with any LLM

## Search
Use `python scripts/agents-search.py --query "your search"` to find agents.

"""

    # Add agent list
    llm_content += "\n## All Agents (Summary)\n\n"
    for category_id, info in CATEGORIES.items():
        llm_content += f"\n### {info['name']}\n"
        category_path = AGENTS_DIR / category_id
        if category_path.exists():
            agents = get_agents_in_category(category_path)
            for agent in agents[:20]:  # Limit to top 20 per category for token efficiency
                llm_content += f"- {agent['name']}: {agent['description'][:60]}...\n"
            if len(agents) > 20:
                llm_content += f"- ... and {len(agents) - 20} more agents\n"

    return llm_content, all_agents


def generate_json_catalog():
    """Generate JSON catalog for the entire repository."""
    all_agents = []
    category_stats = {}

    for category_id, info in CATEGORIES.items():
        category_path = AGENTS_DIR / category_id
        if category_path.exists():
            agents = get_agents_in_category(category_path)
            all_agents.extend(agents)
            category_stats[category_id] = {
                "name": info["name"],
                "count": len(agents),
                "subcategories": info["subcategories"]
            }

    return {
        "version": "3.0.0",
        "generated": datetime.now().isoformat(),
        "total_agents": len(all_agents),
        "categories": category_stats,
        "agents": all_agents
    }


def main():
    # Generate category catalogs
    for category_id, info in CATEGORIES.items():
        result = generate_category_catalog(category_id, info)
        if result:
            md_content, agents = result
            output_path = CATALOGS_DIR / category_id / "README.md"
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(md_content, encoding='utf-8')
            print(f"Generated: {output_path} ({len(agents)} agents)")

    # Generate LLM.txt
    llm_content, all_agents = generate_llm_txt()
    llm_path = CATALOGS_DIR / "LLM.txt"
    llm_path.write_text(llm_content, encoding='utf-8')
    print(f"Generated: {llm_path}")

    # Generate JSON catalog
    json_data = generate_json_catalog()
    json_path = CATALOGS_DIR / "agents-catalog.json"
    json_path.write_text(json.dumps(json_data, indent=2), encoding='utf-8')
    print(f"Generated: {json_path}")

    # Generate repo-level LLM.txt
    repo_llm_path = Path("LLM.txt")
    repo_llm_path.write_text(llm_content, encoding='utf-8')
    print(f"Generated: {repo_llm_path}")

    # Generate repo-level JSON
    repo_json_path = Path("agents-catalog.json")
    repo_json_path.write_text(json.dumps(json_data, indent=2), encoding='utf-8')
    print(f"Generated: {repo_json_path}")

    print(f"\nTotal agents processed: {len(all_agents)}")


if __name__ == "__main__":
    main()
