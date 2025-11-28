# Repository Update Instructions

**Purpose**: This document provides precise instructions for updating all dependent files when changes are made to the agents folder structure. Following these instructions ensures consistency across all documentation and prevents outdated references.

**Last Updated**: 2025-11-28
**Applies To**: Agent additions, removals, reorganizations, and category changes

---

## Quick Reference: Files That Need Updates

| File | Location | Update Trigger | Priority |
|------|----------|----------------|----------|
| `agents-index.json` | `/agents-index.json` | ANY agent change | **CRITICAL** |
| `agents-catalog.json` | `/agents-catalog.json` | ANY agent change | **CRITICAL** |
| `LLM.txt` | `/LLM.txt` | ANY agent change | **CRITICAL** |
| `agents-quickref.md` | `/agents-quickref.md` | Agent add/remove, count changes | HIGH |
| `AGENTS_DIRECTORY.md` | `/AGENTS_DIRECTORY.md` | Structure/count changes | HIGH |
| `README.md` (root) | `/README.md` | Structure/count changes | HIGH |
| `docs/INDEX.md` | `/docs/INDEX.md` | Total agent count changes | HIGH |
| `agents/README.md` | `/agents/README.md` | Category structure changes | MEDIUM |
| `agents/CLAUDE.md` | `/agents/CLAUDE.md` | Category structure changes | MEDIUM |
| `Agents-Catalogs/*/README.md` | `/Agents-Catalogs/` | Category-specific changes | MEDIUM |
| `Agents-Catalogs/LLM.txt` | `/Agents-Catalogs/LLM.txt` | ANY agent change | MEDIUM |
| `Agents-Catalogs/agents-catalog.json` | `/Agents-Catalogs/agents-catalog.json` | ANY agent change | MEDIUM |

---

## Automation Scripts Available

### Primary Script: `scripts/generate-catalogs.py`

**What it does**: Automatically regenerates ALL catalog files, LLM.txt, and JSON files based on current agent folder contents.

**Usage**:
```bash
python3 scripts/generate-catalogs.py
```

**Files it generates/updates**:
- `Agents-Catalogs/01-software-engineering/README.md`
- `Agents-Catalogs/02-data-and-ai/README.md`
- `Agents-Catalogs/03-business/README.md`
- `Agents-Catalogs/04-security-compliance/README.md`
- `Agents-Catalogs/05-predictions-forecasting/README.md`
- `Agents-Catalogs/06-personal-development/README.md`
- `Agents-Catalogs/07-specialized-domains/README.md`
- `Agents-Catalogs/LLM.txt`
- `Agents-Catalogs/agents-catalog.json`
- `LLM.txt` (root)
- `agents-catalog.json` (root)

**IMPORTANT**: This script does NOT update:
- `README.md` (root) - Manual update required
- `docs/INDEX.md` - Manual update required
- `AGENTS_DIRECTORY.md` - Manual update required
- `agents-quickref.md` - Manual update required
- `agents-index.json` - Manual update required

### Secondary Script: `scripts/agents-search.py`

**What it does**: Searches for agents by name, description, or category.

**Usage**:
```bash
python3 scripts/agents-search.py --query "search term"
python3 scripts/agents-search.py --category "01-software-engineering"
python3 scripts/agents-search.py --list-all --json > agents-index.json
```

---

## Update Scenarios & Checklists

### Scenario 1: Adding a Single Agent

**Trigger**: New `.md` agent file added to any category folder

**Checklist**:
- [ ] 1. Add agent file to correct category folder (e.g., `agents/01-software-engineering/backend/`)
- [ ] 2. Run `python3 scripts/generate-catalogs.py`
- [ ] 3. Update `agents-index.json` (add new entry)
- [ ] 4. Update `agents-quickref.md` (add to correct category section)
- [ ] 5. If notable agent, consider adding to "Top 20 Most Versatile Agents" in `agents-quickref.md`
- [ ] 6. Update total count in:
   - `/README.md` line ~1 (title badge)
   - `/README.md` line ~1961 (Directory Statistics table)
   - `/docs/INDEX.md` line ~5, ~48, ~605 (agent counts)
   - `/AGENTS_DIRECTORY.md` line ~11 (Total Agents)

### Scenario 2: Removing an Agent

**Trigger**: Agent `.md` file deleted from any category folder

**Checklist**:
- [ ] 1. Delete agent file from category folder
- [ ] 2. Run `python3 scripts/generate-catalogs.py`
- [ ] 3. Update `agents-index.json` (remove entry)
- [ ] 4. Update `agents-quickref.md` (remove from category section)
- [ ] 5. If was in "Top 20", update that section in `agents-quickref.md`
- [ ] 6. Update total count in all files (same as Scenario 1, step 6)

### Scenario 3: Moving Agents Between Categories

**Trigger**: Agents moved from one category folder to another

**Checklist**:
- [ ] 1. Move agent files to new category folder
- [ ] 2. Run `python3 scripts/generate-catalogs.py`
- [ ] 3. Update `agents-index.json` (update category for moved agents)
- [ ] 4. Update `agents-quickref.md` (move entries to correct sections)
- [ ] 5. Update category counts in:
   - `/README.md` "Organized Agents Directory" section (~lines 1890-1948)
   - `/AGENTS_DIRECTORY.md` directory tree section
   - `/agents/README.md` category overview

### Scenario 4: Creating New Category/Subcategory

**Trigger**: New category folder created (e.g., `agents/08-new-category/`)

**Checklist**:
- [ ] 1. Create folder structure under `agents/`
- [ ] 2. Create `README.md` in new category folder
- [ ] 3. Update `scripts/generate-catalogs.py` CATEGORIES dict to include new category
- [ ] 4. Run `python3 scripts/generate-catalogs.py`
- [ ] 5. Create new catalog folder: `Agents-Catalogs/08-new-category/`
- [ ] 6. Update `AGENTS_DIRECTORY.md` (add new category to tree)
- [ ] 7. Update `/README.md` "Organized Agents Directory" section (add new category)
- [ ] 8. Update `/agents/README.md` (add new category)
- [ ] 9. Update `/agents/CLAUDE.md` (add new category)
- [ ] 10. Update `agents-quickref.md` (add new category section)
- [ ] 11. Update Main Categories count in statistics tables

### Scenario 5: Mass Reorganization (Like Today's Update)

**Trigger**: Major restructuring of agents folder

**Full Checklist**:
- [ ] 1. Plan new structure before making changes
- [ ] 2. Create all new folders first
- [ ] 3. Move all agents to new locations
- [ ] 4. Update `scripts/generate-catalogs.py` if category structure changed
- [ ] 5. Run `python3 scripts/generate-catalogs.py`
- [ ] 6. Regenerate `agents-index.json` using search script
- [ ] 7. Completely rewrite `agents-quickref.md` with new structure
- [ ] 8. Completely rewrite `AGENTS_DIRECTORY.md` with new tree
- [ ] 9. Update `/README.md`:
   - Title and badges (if count changed)
   - "Organized Agents Directory" section (lines ~1884-1977)
   - Directory Statistics table
- [ ] 10. Update `/docs/INDEX.md`:
   - All agent count references (search for "specialized agents")
- [ ] 11. Update `/agents/README.md` with new category structure
- [ ] 12. Update `/agents/CLAUDE.md` with new category structure
- [ ] 13. Scan ALL other docs for outdated references (see "Files That Reference Agents" below)
- [ ] 14. Commit all changes
- [ ] 15. Push to remote

---

## Detailed File Reference

### 1. `/README.md` (Root)

**Purpose**: Main repository readme, public-facing documentation

**Locations requiring updates**:

| Line Range | Content | Update When |
|------------|---------|-------------|
| ~1 | Title "610+ AI Agents" | Total count changes |
| ~6 | Badge `Agents-610%2B` | Total count changes |
| ~16 | "610+ specialized AI agents" | Total count changes |
| ~20 | "610+ Pre-built Agents" | Total count changes |
| ~151 | "610+ categorized AI agents" | Total count changes |
| ~1884-1977 | "Organized Agents Directory" section | Any structure change |
| ~1959-1964 | Directory Statistics table | Any count/structure change |
| ~1966-1975 | Quick Navigation table | Category paths change |

**Search patterns for outdated references**:
```bash
grep -n "610\|54\+" README.md
grep -n "agents/" README.md
```

### 2. `/docs/INDEX.md`

**Purpose**: Documentation hub for Claude Flow

**Locations requiring updates**:

| Line | Content | Update When |
|------|---------|-------------|
| ~5 | "607 specialized agents" | Total count changes |
| ~48 | "AI Agent Ecosystem (607 Agents)" | Total count changes |
| ~605 | "607 Specialized Agents" | Total count changes |

**Search pattern**:
```bash
grep -n "specialized agents\|Agents)" docs/INDEX.md
```

### 3. `/AGENTS_DIRECTORY.md`

**Purpose**: Complete directory listing of all agents

**Sections requiring updates**:

| Section | Lines | Update When |
|---------|-------|-------------|
| Overview Statistics table | ~9-15 | Any count/structure change |
| Directory Structure tree | ~20-80 | Any folder structure change |
| Category Descriptions | ~84+ | Category content changes |
| Full Agent Listings | Varies | Agent add/remove |

### 4. `/agents-quickref.md`

**Purpose**: Quick navigation reference for all agents

**Sections requiring updates**:

| Section | Update When |
|---------|-------------|
| Header statistics | Total count changes |
| Top 20 Most Versatile Agents | Notable agent changes |
| Quick Navigation by Category | Category structure changes |
| Category tables (01-07) | Agent add/remove in category |

### 5. `/agents/README.md`

**Purpose**: Overview of agents folder structure

**Update entirely when**: Category structure changes

### 6. `/agents/CLAUDE.md`

**Purpose**: AI instructions for working with agents folder

**Update when**: Category structure, navigation paths, or agent usage patterns change

---

## Files That Reference Agents (May Need Checking)

These files reference agents by NAME (not path), so they usually don't need updates for structural changes, but should be checked during major reorganizations:

| File | References | Usually Safe |
|------|------------|--------------|
| `swarm-combinations.md` | Agent names in swarm configs | Yes |
| `workflow-automation-scripts.md` | Agent names in YAML workflows | Yes |
| `troubleshooting.md` | Agent names in examples | Yes |
| `prompt-templates.md` | Agent names in templates | Yes |
| `agent-chaining-patterns.md` | Agent names in patterns | Yes |
| `tutorial.md` | Agent usage examples | Check |
| `flowstrats.md` | Agent coordination strategies | Check |

**Safe pattern**: Files that use agent names like `market-user-research` without paths don't need updates when folder structure changes.

**Needs update**: Files that use paths like `agents/software-development-and-engineering/` need updates.

---

## Verification Checklist

After completing any update scenario, verify:

- [ ] `python3 scripts/generate-catalogs.py` runs without errors
- [ ] `python3 scripts/agents-search.py --list-all` returns expected count
- [ ] All category counts in README.md sum to total
- [ ] No broken links in markdown files
- [ ] Git status shows only expected changes
- [ ] Commit message describes what was changed

**Quick verification commands**:
```bash
# Check total agent count
find agents -name "*.md" -type f | wc -l

# Verify catalog generation
python3 scripts/generate-catalogs.py 2>&1 | tail -1

# Check for "54+" (old count) references
grep -r "54+" --include="*.md" .

# Check for old path references
grep -r "software-development-and-engineering" --include="*.md" .
grep -r "data-and-analytics" --include="*.md" .
grep -r "security-and-compliance" --include="*.md" .
grep -r "business-and-operations" --include="*.md" .
grep -r "personal-and-professional-development" --include="*.md" .
grep -r "creative-and-design" --include="*.md" .
grep -r "specialized-domains/" --include="*.md" . | grep -v "07-specialized"
```

---

## Current Repository Structure (as of 2025-11-28)

```
agents/
├── 01-software-engineering/     (274 agents)
│   ├── frontend/
│   │   ├── frameworks/
│   │   ├── styling/
│   │   └── ui-components/
│   ├── backend/
│   │   ├── languages/
│   │   ├── frameworks/
│   │   ├── databases/
│   │   └── apis-integrations/
│   ├── devops/
│   │   ├── ci-cd/
│   │   ├── containers/
│   │   ├── infrastructure/
│   │   └── monitoring/
│   ├── testing/
│   │   └── unit-testing/
│   ├── mobile/
│   └── architecture/
│
├── 02-data-and-ai/              (94 agents)
│   ├── data-engineering/
│   ├── data-science/
│   ├── machine-learning/
│   └── analytics/
│
├── 03-business/                 (66 agents)
│   ├── marketing/
│   ├── sales/
│   ├── customer-success/
│   ├── finance/
│   │   └── payments/            ← ALL 17 payment agents
│   ├── operations/
│   └── strategy/
│
├── 04-security-compliance/      (69 agents)
│   ├── application-security/
│   ├── infrastructure-security/
│   └── compliance-governance/
│
├── 05-predictions-forecasting/  (44 agents) ← ALL prediction agents
│   ├── sports/
│   ├── market-financial/
│   ├── social-political/
│   ├── technology/
│   └── entertainment/
│
├── 06-personal-development/     (56 agents)
│   ├── career/
│   ├── skills/
│   ├── communication/
│   ├── wellness/
│   └── relationships/
│
└── 07-specialized-domains/      (4 agents)
    ├── simulations/
    ├── industry-verticals/
    └── emerging-tech/
```

**Total**: 607 agents across 7 main categories and 36 subcategories

---

## Change Log

| Date | Change | Files Updated |
|------|--------|---------------|
| 2025-11-28 | Initial creation of this document | N/A |
| 2025-11-28 | Complete reorganization from scattered to 7-category structure | All documentation files |

---

## Notes for Future Updates

1. **Always run the catalog generator first** - It handles most of the heavy lifting
2. **Search for hardcoded counts** - Use grep to find "607", "610", "54+" etc.
3. **Check path references** - Old paths like `software-development-and-engineering` should not exist
4. **Statistics tables are in multiple files** - Update all of them for consistency
5. **When in doubt, regenerate** - It's faster to regenerate than to manually edit
6. **Commit incrementally** - For large changes, commit after each major file update
