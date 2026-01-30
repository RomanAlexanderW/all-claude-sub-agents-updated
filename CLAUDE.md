# Claude Code Configuration - SPARC Development Environment (v3.0.0)

## 🚨 CRITICAL: CONCURRENT EXECUTION & FILE MANAGEMENT

**ABSOLUTE RULES**:
1. ALL operations MUST be concurrent/parallel in a single message
2. **NEVER save working files, text/mds and tests to the root folder**
3. ALWAYS organize files in appropriate subdirectories
4. **USE CLAUDE CODE'S TASK TOOL** for spawning agents concurrently, not just MCP

### ⚡ GOLDEN RULE: "1 MESSAGE = ALL RELATED OPERATIONS"

**MANDATORY PATTERNS:**
- **TodoWrite**: ALWAYS batch ALL todos in ONE call (5-10+ todos minimum)
- **Task tool (Claude Code)**: ALWAYS spawn ALL agents in ONE message with full instructions
- **File operations**: ALWAYS batch ALL reads/writes/edits in ONE message
- **Bash commands**: ALWAYS batch ALL terminal operations in ONE message
- **Memory operations**: ALWAYS batch ALL memory store/retrieve in ONE message

### 🎯 CRITICAL: Claude Code Task Tool for Agent Execution

**Claude Code's Task tool is the PRIMARY way to spawn agents:**
```javascript
// ✅ CORRECT: Use Claude Code's Task tool for parallel agent execution
[Single Message]:
  Task("Research agent", "Analyze requirements and patterns...", "researcher")
  Task("Coder agent", "Implement core features...", "coder")
  Task("Tester agent", "Create comprehensive tests...", "tester")
  Task("Reviewer agent", "Review code quality...", "reviewer")
  Task("Architect agent", "Design system architecture...", "system-architect")
```

**MCP tools are ONLY for coordination setup:**
- `mcp__claude-flow__swarm_init` - Initialize coordination topology
- `mcp__claude-flow__agent_spawn` - Define agent types for coordination
- `mcp__claude-flow__task_orchestrate` - Orchestrate high-level workflows

### 📁 File Organization Rules

**NEVER save to root folder. Use these directories:**
- `/src` - Source code files
- `/tests` - Test files
- `/docs` - Documentation and markdown files
- `/config` - Configuration files
- `/scripts` - Utility scripts
- `/examples` - Example code

### 📋 Repository Update Instructions

**CRITICAL**: Before making ANY changes to the agents folder structure, read:
- **[`.claude/REPO_UPDATE_INSTRUCTIONS.md`](.claude/REPO_UPDATE_INSTRUCTIONS.md)** - Complete guide for updating all dependent files

This document contains:
- Quick reference table of ALL files that need updates
- Checklists for different update scenarios (add/remove/move agents)
- Automation scripts available (`scripts/generate-catalogs.py`)
- Verification commands to ensure nothing is missed
- Current folder structure reference

  **IMPORTANT:** During the update from 2.7.0 > v3 of this repo, several critical lessons were learned, and detailed notes taken for future devs & agents to learn from BEFORE attempting any future updates. Please read the entire file, BEFORE updating in the future:
   https://github.com/RomanAlexanderW/all-claude-sub-agents-updated/blob/main/v2.7-to-v3-Update-Lessons-From-Self-Reflection.md

**Key automation script**:
```bash
# Regenerates all catalogs, LLM.txt, and JSON files
python3 scripts/generate-catalogs.py
```

## Project Overview

This project uses **Claude Flow v3** with SPARC (Specification, Pseudocode, Architecture, Refinement, Completion) methodology for systematic Test-Driven Development.

### 🆕 Claude Flow v3 Key Features
- **26 CLI Commands** with 140+ subcommands
- **SONA**: Self-Optimizing Neural Architecture (<0.05ms adaptation)
- **17 Hooks** + **12 Background Workers** (daemon)
- **3-Tier Model Routing**: Agent Booster (WASM) → Haiku → Sonnet/Opus
- **Hybrid Memory Backend**: SQLite + AgentDB with HNSW indexing
- **Byzantine Fault-Tolerant Consensus**: Tolerates up to 1/3 agent failures
- **150x-12500x Faster** vector search with hyperbolic embeddings

## Claude Flow v3 Commands

### Core Commands (26 Primary)
```bash
# Initialize project with v3
npx claude-flow@v3alpha init --force
npx claude-flow@v3alpha init --wizard  # Interactive setup

# Agent management (8 subcommands)
npx claude-flow@v3alpha agent spawn <type>
npx claude-flow@v3alpha agent list
npx claude-flow@v3alpha agent status <id>
npx claude-flow@v3alpha agent stop <id>
npx claude-flow@v3alpha agent metrics
npx claude-flow@v3alpha agent pool health
npx claude-flow@v3alpha agent logs <id>

# Swarm orchestration (6 subcommands)
npx claude-flow@v3alpha swarm create --topology hierarchical
npx claude-flow@v3alpha swarm status
npx claude-flow@v3alpha swarm scale --agents 8

# Memory with HNSW (11 subcommands)
npx claude-flow@v3alpha memory store <key> <value>
npx claude-flow@v3alpha memory search <query>
npx claude-flow@v3alpha memory vector-search <query>  # 150x-12500x faster
npx claude-flow@v3alpha memory status

# Hive-Mind with Byzantine consensus
npx claude-flow@v3alpha hive-mind wizard
npx claude-flow@v3alpha hive-mind spawn
npx claude-flow@v3alpha hive-mind consensus
```

### v3 Daemon & Background Workers
```bash
# 12 auto-triggered workers
npx claude-flow@v3alpha daemon start
npx claude-flow@v3alpha daemon trigger audit --context "./src"
npx claude-flow@v3alpha daemon trigger optimize
npx claude-flow@v3alpha daemon trigger testgaps
npx claude-flow@v3alpha daemon trigger securityscan
```

### v3 Migration Commands
```bash
# Safe v2 → v3 migration with rollback
npx claude-flow@v3alpha migrate status
npx claude-flow@v3alpha migrate run
npx claude-flow@v3alpha migrate verify
npx claude-flow@v3alpha migrate rollback
npx claude-flow@v3alpha migrate breaking-changes
```

## SPARC Commands (v3)

### Core Commands
- `npx claude-flow@v3alpha sparc modes` - List available modes
- `npx claude-flow@v3alpha sparc run <mode> "<task>"` - Execute specific mode
- `npx claude-flow@v3alpha sparc tdd "<feature>"` - Run complete TDD workflow
- `npx claude-flow@v3alpha sparc info <mode>` - Get mode details

### Batchtools Commands
- `npx claude-flow@v3alpha sparc batch <modes> "<task>"` - Parallel execution
- `npx claude-flow@v3alpha sparc pipeline "<task>"` - Full pipeline processing
- `npx claude-flow@v3alpha sparc concurrent <mode> "<tasks-file>"` - Multi-task processing

### Build Commands
- `npm run build` - Build project
- `npm run test` - Run tests
- `npm run lint` - Linting
- `npm run typecheck` - Type checking

## SPARC Workflow Phases

1. **Specification** - Requirements analysis (`sparc run spec-pseudocode`)
2. **Pseudocode** - Algorithm design (`sparc run spec-pseudocode`)
3. **Architecture** - System design (`sparc run architect`)
4. **Refinement** - TDD implementation (`sparc tdd`)
5. **Completion** - Integration (`sparc run integration`)

## Code Style & Best Practices

- **Modular Design**: Files under 500 lines
- **Environment Safety**: Never hardcode secrets
- **Test-First**: Write tests before implementation
- **Clean Architecture**: Separate concerns
- **Documentation**: Keep updated

## 🚀 Available Agents

### Full Agent Library (610 Agents)
See **[agents/README.md](agents/README.md)** for the complete library organized in 7 categories:
- `01-software-engineering/` (274 agents) - Frontend, Backend, DevOps, Testing, Mobile
- `02-data-and-ai/` (94 agents) - ML, Data Science, Analytics
- `03-business/` (66 agents) - Marketing, Sales, Finance, Operations
- `04-security-compliance/` (69 agents) - AppSec, Infrastructure, Compliance
- `05-predictions-forecasting/` (44 agents) - Sports, Markets, Social, Tech
- `06-personal-development/` (56 agents) - Career, Skills, Wellness
- `07-specialized-domains/` (4 agents) - Simulations, Industry-Specific

### Core Development (Built-in)
`coder`, `reviewer`, `tester`, `planner`, `researcher`

### Swarm Coordination
`hierarchical-coordinator`, `mesh-coordinator`, `adaptive-coordinator`, `collective-intelligence-coordinator`, `swarm-memory-manager`

### Consensus & Distributed (v3 Enhanced)
`byzantine-coordinator`, `raft-manager`, `gossip-coordinator`, `consensus-builder`, `crdt-synchronizer`, `quorum-manager`, `security-manager`

### Performance & Optimization
`perf-analyzer`, `performance-benchmarker`, `task-orchestrator`, `memory-coordinator`, `smart-agent`

### GitHub & Repository
`github-modes`, `pr-manager`, `code-review-swarm`, `issue-tracker`, `release-manager`, `workflow-automation`, `project-board-sync`, `repo-architect`, `multi-repo-swarm`

### SPARC Methodology
`sparc-coord`, `sparc-coder`, `specification`, `pseudocode`, `architecture`, `refinement`

### Specialized Development
`backend-dev`, `mobile-dev`, `ml-developer`, `cicd-engineer`, `api-docs`, `system-architect`, `code-analyzer`, `base-template-generator`

### Testing & Validation
`tdd-london-swarm`, `production-validator`

### Migration & Planning
`migration-planner`, `swarm-init`

## 🎯 Claude Code vs MCP Tools

### Claude Code Handles ALL EXECUTION:
- **Task tool**: Spawn and run agents concurrently for actual work
- File operations (Read, Write, Edit, MultiEdit, Glob, Grep)
- Code generation and programming
- Bash commands and system operations
- Implementation work
- Project navigation and analysis
- TodoWrite and task management
- Git operations
- Package management
- Testing and debugging

### MCP Tools ONLY COORDINATE:
- Swarm initialization (topology setup)
- Agent type definitions (coordination patterns)
- Task orchestration (high-level planning)
- Memory management
- Neural features (SONA)
- Performance tracking
- GitHub integration
- Daemon worker management (v3)
- Model routing (v3)

**KEY**: MCP coordinates the strategy, Claude Code's Task tool executes with real agents.

## 🚀 Quick Setup (v3)

```bash
# Add MCP servers (Claude Flow v3 required, others optional)
claude mcp add claude-flow -- npx claude-flow@v3alpha mcp start
claude mcp add ruv-swarm npx ruv-swarm mcp start  # Optional: Enhanced coordination
claude mcp add flow-nexus npx flow-nexus@latest mcp start  # Optional: Cloud features
claude mcp add ruvector npx ruvector mcp start  # Optional: PostgreSQL AI bridge
```

## MCP Tool Categories (v3: 140+ Tools)

### Coordination
`swarm_init`, `swarm_create`, `swarm_scale`, `agent_spawn`, `task_orchestrate`

### Agent Management (v3)
`agent_list`, `agent_status`, `agent_stop`, `agent_metrics`, `agent_pool_health`, `agent_logs`

### Monitoring
`swarm_status`, `agent_list`, `agent_metrics`, `task_status`, `task_results`

### Memory & Neural (v3 Enhanced)
`memory_usage`, `memory_vector_search`, `memory_consolidate`, `neural_status`, `neural_train`, `neural_patterns`, `neural_adapt`

### Daemon & Workers (v3 New)
`daemon_start`, `daemon_stop`, `daemon_trigger`, `daemon_schedule`, `daemon_workers`

### Model Routing (v3 New)
`route_analyze`, `route_select`, `route_metrics`, `agent_booster`

### GitHub Integration
`github_swarm`, `repo_analyze`, `pr_enhance`, `issue_triage`, `code_review`

### Security (v3 Enhanced)
`security_audit`, `security_scan`, `security_validate`, `cve_check`, `ai_defence`

### System
`benchmark_run`, `features_detect`, `swarm_monitor`

### Migration (v3 New)
`migrate_status`, `migrate_run`, `migrate_verify`, `migrate_rollback`, `migrate_breaking`

### Flow-Nexus MCP Tools (Optional Advanced Features)
Flow-Nexus extends MCP capabilities with 70+ cloud-based orchestration tools:

**Key MCP Tool Categories:**
- **Swarm & Agents**: `swarm_init`, `swarm_scale`, `agent_spawn`, `task_orchestrate`
- **Sandboxes**: `sandbox_create`, `sandbox_execute`, `sandbox_upload` (cloud execution)
- **Templates**: `template_list`, `template_deploy` (pre-built project templates)
- **Neural AI**: `neural_train`, `neural_patterns`, `seraphina_chat` (AI assistant)
- **GitHub**: `github_repo_analyze`, `github_pr_manage` (repository management)
- **Real-time**: `execution_stream_subscribe`, `realtime_subscribe` (live monitoring)
- **Storage**: `storage_upload`, `storage_list` (cloud file management)

**Authentication Required:**
- Register: `mcp__flow-nexus__user_register` or `npx flow-nexus@latest register`
- Login: `mcp__flow-nexus__user_login` or `npx flow-nexus@latest login`
- Access 70+ specialized MCP tools for advanced orchestration

## 🚀 Agent Execution Flow with Claude Code

### The Correct Pattern:

1. **Optional**: Use MCP tools to set up coordination topology
2. **REQUIRED**: Use Claude Code's Task tool to spawn agents that do actual work
3. **REQUIRED**: Each agent runs hooks for coordination
4. **REQUIRED**: Batch all operations in single messages

### Example Full-Stack Development:

```javascript
// Single message with all agent spawning via Claude Code's Task tool
[Parallel Agent Execution]:
  Task("Backend Developer", "Build REST API with Express. Use hooks for coordination.", "backend-dev")
  Task("Frontend Developer", "Create React UI. Coordinate with backend via memory.", "coder")
  Task("Database Architect", "Design PostgreSQL schema. Store schema in memory.", "code-analyzer")
  Task("Test Engineer", "Write Jest tests. Check memory for API contracts.", "tester")
  Task("DevOps Engineer", "Setup Docker and CI/CD. Document in memory.", "cicd-engineer")
  Task("Security Auditor", "Review authentication. Report findings via hooks.", "reviewer")
  
  // All todos batched together
  TodoWrite { todos: [...8-10 todos...] }
  
  // All file operations together
  Write "backend/server.js"
  Write "frontend/App.jsx"
  Write "database/schema.sql"
```

## 📋 Agent Coordination Protocol (v3)

### Every Agent Spawned via Task Tool MUST:

**1️⃣ BEFORE Work:**
```bash
npx claude-flow@v3alpha hooks pre-task --description "[task]"
npx claude-flow@v3alpha hooks session-restore --session-id "swarm-[id]"
npx claude-flow@v3alpha hooks model-select --complexity "[low|medium|high]"
```

**2️⃣ DURING Work:**
```bash
npx claude-flow@v3alpha hooks post-edit --file "[file]" --memory-key "swarm/[agent]/[step]"
npx claude-flow@v3alpha hooks notify --message "[what was done]"
npx claude-flow@v3alpha hooks pattern-detect --context "[relevant context]"
```

**3️⃣ AFTER Work:**
```bash
npx claude-flow@v3alpha hooks post-task --task-id "[task]"
npx claude-flow@v3alpha hooks consolidate --patterns true
npx claude-flow@v3alpha hooks session-end --export-metrics true
```

## 🎯 Concurrent Execution Examples

### ✅ CORRECT WORKFLOW: MCP Coordinates, Claude Code Executes (v3)

```javascript
// Step 1: MCP tools set up coordination with v3 anti-drift configuration
[Single Message - Coordination Setup]:
  mcp__claude-flow__swarm_init {
    topology: "hierarchical",  // Recommended for anti-drift
    maxAgents: 8,
    consensus: "byzantine",
    strategy: "specialized"
  }
  mcp__claude-flow__agent_spawn { type: "researcher" }
  mcp__claude-flow__agent_spawn { type: "coder" }
  mcp__claude-flow__agent_spawn { type: "tester" }

// Step 2: Claude Code Task tool spawns ACTUAL agents that do the work
[Single Message - Parallel Agent Execution]:
  // Claude Code's Task tool spawns real agents concurrently
  Task("Research agent", "Analyze API requirements and best practices. Check memory for prior decisions.", "researcher")
  Task("Coder agent", "Implement REST endpoints with authentication. Coordinate via hooks.", "coder")
  Task("Database agent", "Design and implement database schema. Store decisions in memory.", "code-analyzer")
  Task("Tester agent", "Create comprehensive test suite with 90% coverage.", "tester")
  Task("Reviewer agent", "Review code quality and security. Document findings.", "reviewer")

  // Batch ALL todos in ONE call
  TodoWrite { todos: [
    {id: "1", content: "Research API patterns", status: "in_progress", priority: "high"},
    {id: "2", content: "Design database schema", status: "in_progress", priority: "high"},
    {id: "3", content: "Implement authentication", status: "pending", priority: "high"},
    {id: "4", content: "Build REST endpoints", status: "pending", priority: "high"},
    {id: "5", content: "Write unit tests", status: "pending", priority: "medium"},
    {id: "6", content: "Integration tests", status: "pending", priority: "medium"},
    {id: "7", content: "API documentation", status: "pending", priority: "low"},
    {id: "8", content: "Performance optimization", status: "pending", priority: "low"}
  ]}

  // Parallel file operations
  Bash "mkdir -p app/{src,tests,docs,config}"
  Write "app/package.json"
  Write "app/src/server.js"
  Write "app/tests/server.test.js"
  Write "app/docs/API.md"
```

### ❌ WRONG (Multiple Messages):
```javascript
Message 1: mcp__claude-flow__swarm_init
Message 2: Task("agent 1")
Message 3: TodoWrite { todos: [single todo] }
Message 4: Write "file.js"
// This breaks parallel coordination!
```

## Performance Benefits (v3)

- **84.8% SWE-Bench solve rate**
- **30-50% token reduction** (via intelligent model routing)
- **2.8-4.4x speed improvement**
- **150x-12500x faster** vector search
- **<0.05ms** SONA adaptation time
- **<500ms** CLI cold start
- **<1ms** vector search latency
- **27+ neural models**

## v3 Hooks System (17 Hooks)

### Core Hooks (6)
- `pre-task` - Auto-assigns agents with 3-tier model routing
- `post-task` - Trains neural patterns and updates SONA
- `pre-edit` - Validates with Zod schemas, checks path traversal
- `post-edit` - Auto-formats and triggers Agent Booster transforms
- `pre-command` - Security validation with command sandboxing
- `post-command` - Updates memory and triggers pattern detection

### Session Hooks (3)
- `session-start` - Restores previous context with SONA state
- `session-end` - Generates summaries and exports metrics
- `session-restore` - Loads memory with hybrid backend

### Intelligence Routing Hooks (3)
- `model-select` - Selects optimal model tier (Booster/Haiku/Sonnet/Opus)
- `complexity-analyze` - Analyzes task complexity for routing
- `route-decision` - Routes to optimal processing tier

### Neural Learning Hooks (5)
- `pattern-detect` - Detects patterns with HNSW and hyperbolic embeddings
- `learn-trigger` - Triggers SONA learning cycle with EWC++
- `consolidate` - Consolidates patterns to prevent catastrophic forgetting

## v3 Daemon Workers (12 Auto-Triggered)

| Worker | Purpose | Auto-Schedule |
|--------|---------|---------------|
| **UltraLearn** | Deep knowledge acquisition | On-demand |
| **Optimize** | Performance tuning | After-task |
| **Consolidate** | Memory compression | Session-end |
| **Audit** | Security compliance | Periodic |
| **Map** | Structure analysis | On-demand |
| **DeepDive** | Deep investigation | On-demand |
| **Document** | Auto-documentation | Post-edit |
| **Refactor** | Code smell detection | On-demand |
| **Benchmark** | Performance measurement | On-demand |
| **TestGaps** | Test coverage gaps | Post-edit |
| **SecurityScan** | Vulnerability scanning | Periodic |
| **PatternMine** | Pattern discovery | Session-end |

## v3 Model Routing (3-Tier)

| Tier | Model | Latency | Cost | Use Case |
|------|-------|---------|------|----------|
| **Tier 1** | Agent Booster (WASM) | <1ms | $0 | Simple transforms |
| **Tier 2** | Haiku/Sonnet | 500ms-2s | $ | Medium tasks |
| **Tier 3** | Opus | 2-5s | $$$ | Complex architecture |

**WASM Transforms Available:**
- `var-to-const`, `add-types`, `add-error-handling`
- `async-await`, `add-logging`, `remove-console`

## Advanced Features (v3.0.0)

- 🚀 6 Topology Options (hierarchical, mesh, ring, star, hybrid, adaptive)
- ⚡ 150x-12500x Faster Vector Search with HNSW
- 🧠 SONA Neural Architecture (<0.05ms adaptation)
- 🤖 60+ Specialized Agents Built-in
- 📊 3-Tier Model Routing (30-50% token reduction)
- 🛡️ Byzantine Fault-Tolerant Consensus
- 💾 Hybrid Memory Backend (SQLite + AgentDB)
- 🔗 140+ MCP Tools
- 🪝 17 Hooks + 12 Background Workers
- 🔐 CVE-Hardened Security with Zod Validation
- 🔄 Safe v2→v3 Migration with Rollback

## Integration Tips

1. Start with basic swarm init
2. Scale agents gradually
3. Use memory for context
4. Monitor progress regularly
5. Train patterns from success
6. Enable hooks automation
7. Use GitHub tools first

## Support

- Documentation: https://github.com/ruvnet/claude-flow
- Issues: https://github.com/ruvnet/claude-flow/issues
- Flow-Nexus Platform: https://flow-nexus.ruv.io (registration required for cloud features)

---

Remember: **Claude Flow coordinates, Claude Code creates!**

# important-instruction-reminders
Do what has been asked; nothing more, nothing less.
NEVER create files unless they're absolutely necessary for achieving your goal.
ALWAYS prefer editing an existing file to creating a new one.
NEVER proactively create documentation files (*.md) or README files. Only create documentation files if explicitly requested by the User.
Never save working files, text/mds and tests to the root folder.
