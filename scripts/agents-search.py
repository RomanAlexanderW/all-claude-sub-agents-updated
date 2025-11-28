#!/usr/bin/env python3
"""
Agent Search Tool - Search and filter the agent repository by categories, tags, and keywords.

Usage:
    python agents-search.py --category "backend"
    python agents-search.py --tags python api --mode AND
    python agents-search.py --query "payment integration"
    python agents-search.py --generate-index
"""

import os
import re
import json
import argparse
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, field
from collections import defaultdict


@dataclass
class AgentMetadata:
    """Represents metadata for a single agent."""
    filename: str
    name: str
    description: str
    primary_path: str
    primary_weight: float = 1.0
    secondary_categories: Dict[str, float] = field(default_factory=dict)
    tags: Dict[str, List[str]] = field(default_factory=dict)
    keywords: List[str] = field(default_factory=list)


class AgentSearcher:
    """Search engine for the agent repository."""

    def __init__(self, agents_dir: str = "agents"):
        self.agents_dir = Path(agents_dir)
        self.agents: List[AgentMetadata] = []
        self.index: Dict[str, List[AgentMetadata]] = defaultdict(list)
        self._load_agents()
        self._build_index()

    def _load_agents(self):
        """Load all agent metadata from markdown files."""
        for md_file in self.agents_dir.rglob("*.md"):
            # Skip non-agent files
            if md_file.name in ["README.md", "CLAUDE.md", "MIGRATION_SUMMARY.md"]:
                continue
            metadata = self._parse_agent_file(md_file)
            if metadata:
                self.agents.append(metadata)

    def _parse_agent_file(self, filepath: Path) -> Optional[AgentMetadata]:
        """Parse an agent markdown file and extract metadata."""
        try:
            content = filepath.read_text(encoding='utf-8')

            # Extract YAML frontmatter
            name_match = re.search(r'^name:\s*(.+)$', content, re.MULTILINE)
            desc_match = re.search(r'^description:\s*(.+)$', content, re.MULTILINE)

            name = name_match.group(1).strip() if name_match else filepath.stem
            description = desc_match.group(1).strip() if desc_match else ""

            # Get relative path as primary category
            relative_path = filepath.parent.relative_to(self.agents_dir)

            # Extract categorization metadata if present
            secondary_cats = {}
            tags = {}
            keywords = []

            # Parse Secondary Categories table
            sec_cat_match = re.search(
                r'### Secondary Categories\n\|.*\n\|.*\n((?:\|.*\n)*)',
                content
            )
            if sec_cat_match:
                for line in sec_cat_match.group(1).strip().split('\n'):
                    parts = [p.strip() for p in line.split('|')[1:-1]]
                    if len(parts) >= 2:
                        cat = parts[0].strip('`')
                        try:
                            weight = float(parts[1])
                            secondary_cats[cat] = weight
                        except ValueError:
                            pass

            # Parse Tags table
            tags_match = re.search(
                r'### Tags\n\|.*\n\|.*\n((?:\|.*\n)*)',
                content
            )
            if tags_match:
                for line in tags_match.group(1).strip().split('\n'):
                    parts = [p.strip() for p in line.split('|')[1:-1]]
                    if len(parts) >= 2:
                        tag_type = parts[0].strip('*').lower()
                        tag_values = [t.strip() for t in parts[1].split(',')]
                        tags[tag_type] = tag_values

            # Parse Keywords
            kw_match = re.search(r'### Search Keywords\n`([^`]+)`', content)
            if kw_match:
                keywords = [k.strip() for k in kw_match.group(1).split(',')]

            # Extract keywords from description if no explicit keywords
            if not keywords and description:
                # Extract significant words from description
                words = re.findall(r'\b[a-zA-Z]{4,}\b', description.lower())
                keywords = list(set(words))[:10]

            return AgentMetadata(
                filename=filepath.name,
                name=name,
                description=description,
                primary_path=str(relative_path),
                primary_weight=1.0,
                secondary_categories=secondary_cats,
                tags=tags,
                keywords=keywords
            )
        except Exception as e:
            print(f"Warning: Could not parse {filepath}: {e}")
            return None

    def _build_index(self):
        """Build search indexes for fast lookup."""
        for agent in self.agents:
            # Index by primary path
            self.index[f"path:{agent.primary_path}"].append(agent)

            # Index by path components
            for part in agent.primary_path.split('/'):
                self.index[f"path_part:{part.lower()}"].append(agent)

            # Index by secondary categories
            for cat in agent.secondary_categories:
                self.index[f"path:{cat}"].append(agent)

            # Index by tags
            for tag_type, tag_values in agent.tags.items():
                for tag in tag_values:
                    self.index[f"tag:{tag.lower()}"].append(agent)
                    self.index[f"{tag_type}:{tag.lower()}"].append(agent)

            # Index by keywords
            for kw in agent.keywords:
                self.index[f"keyword:{kw.lower()}"].append(agent)

            # Index by name words
            name_words = agent.name.replace('-', ' ').replace('_', ' ').split()
            for word in name_words:
                self.index[f"name:{word.lower()}"].append(agent)

    def search_by_category(self, category: str) -> List[Tuple[AgentMetadata, float]]:
        """Search agents by category path."""
        results = []
        category_lower = category.lower()

        for agent in self.agents:
            if category_lower in agent.primary_path.lower():
                results.append((agent, 1.0))
            else:
                for cat, weight in agent.secondary_categories.items():
                    if category_lower in cat.lower():
                        results.append((agent, weight))
                        break

        # Sort by weight descending
        results.sort(key=lambda x: x[1], reverse=True)
        return results

    def search_by_tags(self, tags: List[str], mode: str = "OR") -> List[AgentMetadata]:
        """Search agents by tags. Mode can be 'AND' or 'OR'."""
        tag_sets = [set(self.index.get(f"tag:{t.lower()}", [])) for t in tags]

        if mode.upper() == "AND":
            if not tag_sets:
                return []
            result_set = tag_sets[0]
            for ts in tag_sets[1:]:
                result_set &= ts
        else:  # OR
            result_set = set()
            for ts in tag_sets:
                result_set |= ts

        return list(result_set)

    def search_by_query(self, query: str) -> List[Tuple[AgentMetadata, int]]:
        """Full-text search in names, descriptions and keywords."""
        query_lower = query.lower()
        query_words = query_lower.split()
        results = []

        for agent in self.agents:
            score = 0

            # Check name (highest priority)
            for word in query_words:
                if word in agent.name.lower():
                    score += 5

            # Exact name match bonus
            if query_lower in agent.name.lower():
                score += 10

            # Check description
            for word in query_words:
                if word in agent.description.lower():
                    score += 2

            # Exact phrase in description bonus
            if query_lower in agent.description.lower():
                score += 5

            # Check keywords
            for kw in agent.keywords:
                for word in query_words:
                    if word in kw.lower():
                        score += 1

            # Check path
            for word in query_words:
                if word in agent.primary_path.lower():
                    score += 1

            if score > 0:
                results.append((agent, score))

        results.sort(key=lambda x: x[1], reverse=True)
        return results

    def list_categories(self) -> Dict[str, int]:
        """List all categories with agent counts."""
        categories = defaultdict(int)
        for agent in self.agents:
            categories[agent.primary_path] += 1
        return dict(sorted(categories.items()))

    def get_stats(self) -> Dict[str, any]:
        """Get repository statistics."""
        categories = self.list_categories()
        main_cats = defaultdict(int)

        for path, count in categories.items():
            main_cat = path.split('/')[0] if '/' in path else path
            main_cats[main_cat] += count

        return {
            "total_agents": len(self.agents),
            "total_categories": len(categories),
            "main_categories": dict(main_cats),
            "detailed_categories": categories
        }

    def generate_index_json(self, output_path: str = "agents-index.json"):
        """Generate a JSON index file for external tools."""
        index_data = {
            "total_agents": len(self.agents),
            "generated_by": "agents-search.py",
            "agents": [
                {
                    "filename": a.filename,
                    "name": a.name,
                    "description": a.description[:200] + "..." if len(a.description) > 200 else a.description,
                    "primary_path": a.primary_path,
                    "secondary_categories": a.secondary_categories,
                    "tags": a.tags,
                    "keywords": a.keywords[:10] if a.keywords else []
                }
                for a in sorted(self.agents, key=lambda x: x.primary_path)
            ],
            "categories": self.list_categories()
        }

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(index_data, f, indent=2)

        print(f"Index saved to {output_path}")
        print(f"Total agents indexed: {len(self.agents)}")


def print_results(results: List, title: str, limit: int = 20):
    """Pretty print search results."""
    print(f"\n{title}\n{'=' * len(title)}\n")

    if not results:
        print("  No agents found matching your criteria.\n")
        return

    displayed = 0
    for item in results[:limit]:
        if isinstance(item, tuple):
            agent, score = item
            score_str = f" (score: {score})" if isinstance(score, (int, float)) else ""
        else:
            agent = item
            score_str = ""

        print(f"  {agent.name}{score_str}")
        print(f"     Path: {agent.primary_path}")
        desc = agent.description[:80] + "..." if len(agent.description) > 80 else agent.description
        print(f"     Desc: {desc}")
        print()
        displayed += 1

    if len(results) > limit:
        print(f"  ... and {len(results) - limit} more results")

    print(f"  Total: {len(results)} agents found\n")


def main():
    parser = argparse.ArgumentParser(
        description="Search the agent repository",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --category "backend"           # Find all backend agents
  %(prog)s --category "predictions"       # Find all prediction agents
  %(prog)s --tags python api --mode AND   # Find agents with both tags
  %(prog)s --query "payment stripe"       # Full-text search
  %(prog)s --stats                        # Show repository statistics
  %(prog)s --list-categories              # List all categories
  %(prog)s --generate-index               # Generate JSON index file
        """
    )
    parser.add_argument("--category", "-c", help="Search by category path")
    parser.add_argument("--tags", "-t", nargs="+", help="Search by tags")
    parser.add_argument("--mode", "-m", default="OR", choices=["AND", "OR"],
                        help="Tag search mode (default: OR)")
    parser.add_argument("--query", "-q", help="Full-text search query")
    parser.add_argument("--stats", "-s", action="store_true",
                        help="Show repository statistics")
    parser.add_argument("--list-categories", "-l", action="store_true",
                        help="List all categories with counts")
    parser.add_argument("--generate-index", action="store_true",
                        help="Generate JSON index file")
    parser.add_argument("--agents-dir", default="agents",
                        help="Path to agents directory (default: agents)")
    parser.add_argument("--limit", type=int, default=20,
                        help="Maximum results to display (default: 20)")

    args = parser.parse_args()

    # Find agents directory
    agents_dir = args.agents_dir
    if not os.path.isdir(agents_dir):
        # Try parent directory
        parent_agents = os.path.join(os.path.dirname(os.path.dirname(__file__)), "agents")
        if os.path.isdir(parent_agents):
            agents_dir = parent_agents
        else:
            print(f"Error: Could not find agents directory at {agents_dir}")
            return 1

    print(f"Loading agents from: {agents_dir}")
    searcher = AgentSearcher(agents_dir)
    print(f"Loaded {len(searcher.agents)} agents\n")

    if args.generate_index:
        output_path = os.path.join(os.path.dirname(agents_dir), "agents-index.json")
        searcher.generate_index_json(output_path)
        return 0

    if args.stats:
        stats = searcher.get_stats()
        print("Repository Statistics")
        print("=" * 40)
        print(f"  Total Agents: {stats['total_agents']}")
        print(f"  Total Categories: {stats['total_categories']}")
        print("\n  Main Categories:")
        for cat, count in sorted(stats['main_categories'].items()):
            print(f"    {cat}: {count} agents")
        return 0

    if args.list_categories:
        categories = searcher.list_categories()
        print("All Categories")
        print("=" * 40)
        for cat, count in categories.items():
            print(f"  {cat}: {count}")
        return 0

    if args.category:
        results = searcher.search_by_category(args.category)
        print_results(results, f"Agents in category '{args.category}'", args.limit)
    elif args.tags:
        results = searcher.search_by_tags(args.tags, args.mode)
        print_results([(r, 0) for r in results],
                     f"Agents with tags {args.tags} ({args.mode})", args.limit)
    elif args.query:
        results = searcher.search_by_query(args.query)
        print_results(results, f"Search results for '{args.query}'", args.limit)
    else:
        parser.print_help()

    return 0


if __name__ == "__main__":
    exit(main())
