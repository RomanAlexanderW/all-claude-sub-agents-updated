#!/usr/bin/env python3
"""
Claude Flow v2.7.0 Agent Converter
Batch converts 610+ agents to new YAML frontmatter format
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime

# Color palette by agent type
COLORS = {
    "developer": "#4CAF50",
    "tester": "#2196F3",
    "coordinator": "#9C27B0",
    "analyzer": "#FF9800",
    "security": "#F44336",
    "synchronizer": "#00BCD4",
    "reviewer": "#795548",
    "planner": "#607D8B",
    "researcher": "#3F51B5",
    "specialist": "#E91E63",
    "optimizer": "#009688",
    "manager": "#673AB7",
    "engineer": "#FF5722",
    "architect": "#8BC34A",
    "documenter": "#CDDC39"
}

# Type detection based on agent name/content keywords
TYPE_KEYWORDS = {
    "tester": ["test", "qa", "validation", "tdd", "bdd", "atdd", "jest", "cypress", "playwright", "quality-assurance"],
    "security": ["security", "vulnerability", "threat", "compliance", "audit", "penetration", "owasp", "encryption"],
    "coordinator": ["coordinator", "orchestrat", "manager", "swarm", "hive", "queen", "coordination"],
    "analyzer": ["analy", "monitor", "benchmark", "performance", "metric", "diagnos", "profil"],
    "researcher": ["research", "insight", "intelligence", "trend", "discovery", "mining", "market"],
    "planner": ["plan", "strateg", "architect", "design", "roadmap", "blueprint"],
    "reviewer": ["review", "audit", "quality", "code-review", "inspection"],
    "synchronizer": ["sync", "crdt", "replica", "distributed", "consensus"],
    "optimizer": ["optim", "enhance", "improve", "tuning", "refinement", "performance"],
    "engineer": ["engineer", "devops", "cicd", "pipeline", "infrastructure", "deployment"],
    "documenter": ["doc", "api-doc", "openapi", "swagger", "documentation"],
    "architect": ["architect", "system-design", "microservice", "architecture"]
}

# Category mapping based on old directory structure
CATEGORY_MAP = {
    "software-development-and-engineering/frontend-development": "frontend",
    "software-development-and-engineering/backend-development": "backend",
    "software-development-and-engineering/devops-and-infrastructure": "devops",
    "software-development-and-engineering/testing-and-qa": "testing",
    "software-development-and-engineering/mobile-development": "mobile",
    "data-and-analytics/machine-learning-and-ai": "ml-ai",
    "data-and-analytics/data-science-and-analytics": "data",
    "data-and-analytics/data-engineering": "data",
    "security-and-compliance/application-security": "security/application",
    "security-and-compliance/compliance-and-governance": "security/compliance",
    "security-and-compliance/infrastructure-security": "security/infrastructure",
    "business-and-operations/marketing-and-sales": "business/marketing-sales",
    "business-and-operations/operations-and-process": "business/operations",
    "business-and-operations/finance-and-analytics": "business/finance",
    "business-and-operations/strategy-and-growth": "business/strategy",
    "business-and-operations/customer-success": "business/customer-success",
    "personal-and-professional-development/relationships-and-communication": "personal/relationships",
    "personal-and-professional-development/learning-and-skills": "personal/learning",
    "personal-and-professional-development/career-development": "personal/career",
    "personal-and-professional-development/health-and-wellness": "personal/health",
    "personal-and-professional-development/life-planning": "personal/life-planning",
    "creative-and-design/visual-design": "creative/visual-design",
    "creative-and-design/content-creation": "creative/content-creation",
    "creative-and-design/innovation-and-creativity": "creative/innovation",
    "specialized-domains/simulation-and-modeling": "specialized/simulation",
    "specialized-domains/industry-specific": "specialized/industry",
    "specialized-domains/advanced-technologies": "specialized/advanced-tech"
}

# Priority detection
PRIORITY_KEYWORDS = {
    "critical": ["critical", "security", "production", "enterprise", "essential"],
    "high": ["core", "primary", "main", "key", "important"],
    "medium": ["standard", "common", "general", "regular"],
    "low": ["optional", "experimental", "helper", "utility"]
}

def detect_type(name: str, content: str) -> str:
    """Detect agent type from name and content"""
    text = (name + " " + content).lower()
    for agent_type, keywords in TYPE_KEYWORDS.items():
        if any(kw in text for kw in keywords):
            return agent_type
    return "developer"  # default

def detect_priority(name: str, content: str) -> str:
    """Detect priority level"""
    text = (name + " " + content).lower()
    for priority, keywords in PRIORITY_KEYWORDS.items():
        if any(kw in text for kw in keywords):
            return priority
    return "medium"  # default

def extract_capabilities(content: str, name: str) -> list:
    """Extract capabilities from markdown content"""
    capabilities = []

    # Look for capabilities section
    cap_match = re.search(r'##\s*(?:Capabilities|Core Competencies|Features)\s*\n((?:[-*]\s*.+\n?)+)', content, re.IGNORECASE)
    if cap_match:
        lines = cap_match.group(1).strip().split('\n')
        for line in lines[:10]:  # Max 10 from this section
            clean = re.sub(r'^[-*]\s*\*?\*?', '', line).strip()
            clean = re.sub(r'\*\*', '', clean)  # Remove bold
            if clean and len(clean) > 3:
                # Convert to snake_case
                cap = re.sub(r'[^a-zA-Z0-9\s]', '', clean)
                cap = cap.lower().replace(' ', '_')[:50]
                if cap and cap not in capabilities:
                    capabilities.append(cap)

    # Fallback: extract from first meaningful paragraphs
    if len(capabilities) < 3:
        # Extract action words from content
        words = content.lower().split()
        action_words = ["generation", "analysis", "optimization", "testing", "review",
                       "planning", "research", "coordination", "monitoring", "automation"]
        for word in action_words:
            if word in content.lower() and word not in capabilities:
                capabilities.append(word)
                if len(capabilities) >= 5:
                    break

    # Ultimate fallback
    if not capabilities:
        capabilities = ["specialized_task_execution", "agent_orchestration", "workflow_automation"]

    return capabilities[:8]  # Max 8 capabilities

def parse_yaml_frontmatter(content: str) -> tuple:
    """Parse existing YAML frontmatter"""
    yaml_match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
    if yaml_match:
        yaml_content = yaml_match.group(1)
        remaining_content = yaml_match.group(2)

        # Extract name and description from old format
        name_match = re.search(r'name:\s*(.+)', yaml_content)
        desc_match = re.search(r'description:\s*(.+?)(?:\n|$)', yaml_content, re.DOTALL)

        name = name_match.group(1).strip() if name_match else ""
        description = desc_match.group(1).strip() if desc_match else ""

        # Clean up description (remove newlines, extra spaces)
        description = ' '.join(description.split())

        return name, description, remaining_content

    return "", "", content

def extract_description(content: str, old_desc: str = "") -> str:
    """Extract first meaningful paragraph as description"""
    if old_desc and len(old_desc) > 20:
        return old_desc[:200]

    # Skip the title and get first paragraph
    lines = content.split('\n')
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#') and not line.startswith('Principle') and len(line) > 20:
            # Clean and truncate
            desc = re.sub(r'\[.*?\]\(.*?\)', '', line)  # Remove links
            desc = re.sub(r'[*_`]', '', desc)  # Remove formatting
            return desc[:200]
    return "Specialized AI agent for Claude Flow swarm orchestration"

def get_new_category(old_path: str, agent_name: str) -> str:
    """Map old category path to new v2.7.0 category"""
    old_path_normalized = old_path.replace('\\', '/')

    for old_cat, new_cat in CATEGORY_MAP.items():
        if old_cat in old_path_normalized:
            return new_cat

    # Fallback based on agent name
    name_lower = agent_name.lower()
    if 'test' in name_lower or 'qa' in name_lower:
        return "testing"
    elif 'security' in name_lower:
        return "security/application"
    elif 'frontend' in name_lower or 'ui' in name_lower or 'react' in name_lower:
        return "frontend"
    elif 'backend' in name_lower or 'api' in name_lower:
        return "backend"
    elif 'devops' in name_lower or 'cicd' in name_lower:
        return "devops"
    elif 'data' in name_lower or 'analytics' in name_lower:
        return "data"
    elif 'ml' in name_lower or 'ai' in name_lower or 'machine-learning' in name_lower:
        return "ml-ai"

    return "specialized"  # default

def convert_agent(old_path: Path, base_old: Path) -> tuple:
    """Convert a single agent file to v2.7.0 format"""

    with open(old_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse existing YAML if present
    old_name, old_desc, body_content = parse_yaml_frontmatter(content)

    # Extract agent name from filename or YAML
    if old_name:
        agent_name = old_name
    else:
        agent_name = old_path.stem.lower().replace('_', '-').replace(' ', '-')

    # Ensure kebab-case
    agent_name = re.sub(r'[^a-z0-9-]', '-', agent_name.lower())
    agent_name = re.sub(r'-+', '-', agent_name).strip('-')

    # Detect properties
    full_content = content if not body_content else body_content
    agent_type = detect_type(agent_name, full_content)
    color = COLORS.get(agent_type, "#607D8B")
    priority = detect_priority(agent_name, full_content)
    capabilities = extract_capabilities(full_content, agent_name)
    description = extract_description(full_content, old_desc)

    # Determine new category
    rel_path = str(old_path.relative_to(base_old))
    new_category = get_new_category(rel_path, agent_name)

    # Build YAML frontmatter
    yaml_front = f'''---
name: {agent_name}
type: {agent_type}
color: "{color}"
description: {description}
capabilities:
'''
    for cap in capabilities:
        yaml_front += f"  - {cap}\n"

    yaml_front += f'''priority: {priority}
hooks:
  pre: |
    echo "Initializing {agent_name}"
  post: |
    echo "Completed {agent_name} execution"
---

'''

    # Clean body content (remove old Principle 0 if too long, keep if short)
    body_lines = body_content.split('\n')
    cleaned_body = []
    skip_principle = False
    principle_line_count = 0

    for line in body_lines:
        if 'Principle 0' in line or 'ABSOLUTE TRUTHFULNESS' in line:
            skip_principle = True
            principle_line_count = 0

        if skip_principle:
            principle_line_count += 1
            if principle_line_count > 100:  # Skip long principle sections
                skip_principle = False
            continue

        if '###' in line and 'SUBAGENT' in line.upper():
            skip_principle = False
            continue

        cleaned_body.append(line)

    body_content = '\n'.join(cleaned_body).strip()

    # Add usage section to content
    usage_section = f'''

## Usage Example

```bash
# Single agent deployment
Task("{description[:50]}...", "detailed instructions here", "{agent_name}")
```

## Swarm Deployment

```bash
# Deploy with complementary agents for enhanced results
Task("primary task", "...", "{agent_name}")
Task("supporting task", "...", "related-agent")
```
'''

    # Combine: YAML + cleaned content + usage
    new_content = yaml_front + body_content + usage_section

    return new_category, agent_name, new_content

def main():
    """Main conversion process"""

    old_agents_dir = Path("agents")
    new_agents_dir = Path(".claude/agents")

    if not old_agents_dir.exists():
        print("ERROR: agents/ directory not found!")
        return

    # Ensure new directory exists
    new_agents_dir.mkdir(parents=True, exist_ok=True)

    converted = 0
    errors = []
    category_counts = {}

    print("=" * 60)
    print("Claude Flow v2.7.0 Agent Converter")
    print("=" * 60)
    print(f"Source: {old_agents_dir}")
    print(f"Target: {new_agents_dir}")
    print()

    # Find all .md files in old agents directory
    md_files = list(old_agents_dir.rglob("*.md"))
    total = len(md_files)

    print(f"Found {total} agent files to convert...")
    print()

    for idx, md_file in enumerate(md_files, 1):
        try:
            new_category, agent_name, new_content = convert_agent(md_file, old_agents_dir)

            # Create category directory
            new_cat_dir = new_agents_dir / new_category
            new_cat_dir.mkdir(parents=True, exist_ok=True)

            # Write new agent file
            new_file = new_cat_dir / f"{agent_name}.md"
            with open(new_file, 'w', encoding='utf-8') as f:
                f.write(new_content)

            converted += 1
            category_counts[new_category] = category_counts.get(new_category, 0) + 1

            if converted % 50 == 0:
                print(f"Progress: {converted}/{total} agents converted ({converted*100//total}%)")

        except Exception as e:
            errors.append((str(md_file), str(e)))
            print(f"ERROR converting {md_file.name}: {e}")

    print()
    print("=" * 60)
    print("CONVERSION COMPLETE")
    print("=" * 60)
    print(f"Total converted: {converted}/{total}")
    print(f"Success rate: {converted*100//total}%")
    print(f"Errors: {len(errors)}")
    print()

    print("Agents by category:")
    for cat in sorted(category_counts.keys()):
        print(f"  {cat:40s} {category_counts[cat]:4d} agents")
    print()

    if errors:
        print("Errors encountered:")
        for path, err in errors[:10]:
            print(f"  - {path}: {err}")
        if len(errors) > 10:
            print(f"  ... and {len(errors) - 10} more errors")
        print()

    # Generate manifest
    manifest = {
        "version": "2.7.0",
        "converted_at": datetime.now().isoformat(),
        "total_agents": converted,
        "categories": sorted(category_counts.keys()),
        "category_counts": category_counts,
        "conversion_errors": len(errors)
    }

    manifest_file = new_agents_dir / "manifest.json"
    with open(manifest_file, 'w') as f:
        json.dump(manifest, f, indent=2)

    print(f"Manifest written to {manifest_file}")
    print()
    print("=" * 60)
    print("Next steps:")
    print("1. Review converted agents in .claude/agents/")
    print("2. Run: find .claude/agents -name '*.md' | wc -l")
    print("3. Commit changes: git add -A && git commit -m 'feat: migrate to v2.7.0'")
    print("=" * 60)

if __name__ == "__main__":
    main()
