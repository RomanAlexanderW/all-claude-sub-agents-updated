# MCP Tools Reference - 100+ Available Tools

## Overview

Claude Flow v3.0.0 includes **140+ MCP (Model Context Protocol) tools** for swarm orchestration, agent coordination, and automation.

## 🎯 Tool Categories

### Swarm Orchestration (25 tools)

Core tools for multi-agent coordination:

- `swarm_init` - Initialize swarm topology
- `swarm_spawn` - Create worker agents
- `swarm_monitor` - Monitor swarm execution
- `swarm_broadcast` - Message all agents
- `swarm_reduce` - Aggregate results
- `task_distribute` - Assign tasks to agents
- `task_coordinate` - Synchronize task execution
- `task_schedule` - Schedule swarm tasks
- `task_priority` - Manage task priorities
- `result_aggregate` - Combine swarm results
- `state_sync` - Synchronize agent states
- `heartbeat_monitor` - Health check agents
- `error_handle` - Error recovery
- `load_balance` - Distribute workload
- `performance_monitor` - Track swarm performance
- `metric_collect` - Gather metrics
- `alert_trigger` - Alert on conditions
- `fallback_activate` - Activate fallback strategies
- `rollback_execute` - Rollback changes
- `topology_switch` - Change swarm topology
- `queue_manage` - Manage task queues
- `throttle_control` - Control execution rate
- `resource_allocate` - Allocate resources
- `capacity_check` - Check capacity
- `scaling_trigger` - Trigger auto-scaling

### Hive-Mind Intelligence (15 tools)

Queen-led coordination tools:

- `queen_init` - Initialize queen agent
- `queen_decision` - Make coordination decisions
- `worker_assign` - Assign workers to tasks
- `worker_monitor` - Monitor workers
- `hierarchy_manage` - Manage agent hierarchy
- `knowledge_share` - Share knowledge between agents
- `consensus_build` - Build consensus decisions
- `conflict_resolve` - Resolve agent conflicts
- `leadership_transfer` - Transfer leadership
- `loyalty_check` - Verify agent loyalty
- `colony_health` - Check colony health
- `efficiency_optimize` - Optimize efficiency
- `growth_manage` - Manage colony growth
- `split_hive` - Split into new hives
- `merge_hives` - Merge multiple hives

### AgentDB Integration (20 tools)

Vector search and memory tools:

- `vector_search` - Semantic vector search
- `pattern_find` - Find similar patterns
- `embedding_generate` - Generate embeddings
- `index_rebuild` - Rebuild search indices
- `schema_infer` - Auto-infer data schema
- `memory_store` - Store in AgentDB
- `memory_retrieve` - Retrieve from AgentDB
- `memory_search` - Search memory
- `memory_delete` - Delete from memory
- `compression_apply` - Apply compression
- `quantization_adjust` - Adjust quantization
- `cache_warm` - Warm up cache
- `cache_invalidate` - Invalidate cache
- `backup_create` - Create backup
- `backup_restore` - Restore backup
- `migration_execute` - Migrate data
- `health_check` - Check AgentDB health
- `performance_tune` - Tune performance
- `stats_collect` - Collect statistics
- `monitoring_setup` - Setup monitoring

### GitHub Integration (12 tools)

Repository and workflow tools:

- `github_pr_review` - Review pull requests
- `github_workflow_trigger` - Trigger workflows
- `github_issue_create` - Create issues
- `github_branch_create` - Create branches
- `github_commit_create` - Create commits
- `github_release_publish` - Publish releases
- `github_repo_analyze` - Analyze repository
- `github_security_scan` - Security scanning
- `github_notify_users` - Notify users
- `github_webhook_setup` - Setup webhooks
- `github_action_run` - Run actions
- `github_multilrepo_sync` - Multi-repo sync

### Automation & Quality (15 tools)

Testing and validation tools:

- `test_run` - Run tests
- `test_coverage` - Analyze coverage
- `lint_check` - Run linting
- `format_apply` - Apply formatting
- `type_check` - TypeScript type checking
- `security_audit` - Security audit
- `dependency_scan` - Scan dependencies
- `performance_test` - Performance testing
- `benchmark_run` - Run benchmarks
- `quality_gate_check` - Quality checks
- `validation_execute` - Run validation
- `verification_run` - Verify implementation
- `documentation_generate` - Generate docs
- `changelog_update` - Update changelog
- `version_bump` - Bump version

### Development Helpers (13 tools)

Development workflow tools:

- `code_review` - Code review
- `pair_program` - Pair programming
- `refactor_suggest` - Refactoring suggestions
- `architecture_review` - Architecture review
- `design_pattern_apply` - Apply design patterns
- `test_generate` - Generate tests
- `mock_create` - Create mocks
- `api_document` - API documentation
- `example_generate` - Generate examples
- `migration_guide` - Migration guides
- `debugging_assist` - Debugging assistance
- `performance_profile` - Profile performance
- `optimization_suggest` - Suggest optimizations

## 📊 Tool Matrix

| Category | Tools | Purpose |
|----------|-------|---------|
| Swarm Orchestration | 25 | Multi-agent coordination |
| Hive-Mind | 15 | Queen-led intelligence |
| AgentDB | 20 | Vector search & memory |
| GitHub | 12 | Repository management |
| Automation | 15 | Testing & quality |
| Development | 13 | Code development |

## 🚀 Usage Examples

### Swarm Orchestration

```bash
# Initialize swarm
npx claude-flow@v3alpha swarm init --workers 10

# Distribute task
npx claude-flow@v3alpha swarm task-distribute "task-description"

# Monitor performance
npx claude-flow@v3alpha swarm performance-monitor --live
```

### Hive-Mind Coordination

```bash
# Activate hive-mind
npx claude-flow@v3alpha hive-mind init

# Make consensus decision
npx claude-flow@v3alpha hive-mind consensus "decision-topic"

# Monitor colony health
npx claude-flow@v3alpha hive-mind health-check
```

### AgentDB Vector Search

```bash
# Search patterns
npx claude-flow@v3alpha memory vector-search "similar-patterns"

# Store embedding
npx claude-flow@v3alpha memory embedding-generate "content"

# Rebuild indices
npx claude-flow@v3alpha memory index-rebuild
```

## 🔧 Configuration

Tools are configured in `.claude/settings.json`:

```json
{
  "mcpTools": {
    "enabled": true,
    "toolCount": 100,
    "categories": [
      "orchestration",
      "automation",
      "integration",
      "monitoring"
    ],
    "performance": {
      "timeout": 30000,
      "retries": 3,
      "cache": true
    }
  }
}
```

## 📚 Related Documentation

- [Agent System](./AGENT-SYSTEM.md)
- [Memory System](./MEMORY-SYSTEM.md)
- [Hive-Mind Intelligence](./HIVE-MIND.md)
- [Installation](./INSTALLATION.md)
