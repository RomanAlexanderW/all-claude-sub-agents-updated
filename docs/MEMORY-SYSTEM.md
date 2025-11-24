# Memory System - AgentDB & ReasoningBank

## Overview

Claude Flow v2.7.0 features a **hybrid memory system** combining AgentDB vector search with ReasoningBank persistent memory.

## 🚀 AgentDB v1.3.9

### Features

- **96x-164x Faster** vector search (vs. baseline)
- **HNSW Indexing**: O(log n) search complexity
- **9 RL Algorithms**: Optimization strategies
- **Semantic Understanding**: Natural language queries
- **Automatic Schema**: Self-discovering data structures

### Performance Metrics

```
Vector Search: 96x-164x faster
Memory Search: 150x faster
Memory Footprint: 4x-32x reduction (quantization)
SWE-Bench Score: 84.8% (industry leading)
```

### Usage

```bash
# Initialize AgentDB
npx claude-flow@alpha init --force

# Vector search for patterns
npx claude-flow@alpha memory search "similar-patterns" --agentdb

# Store with semantic indexing
npx claude-flow@alpha memory store "key" "value" --semanticindexing

# View AgentDB stats
npx claude-flow@alpha memory stats --agentdb
```

## 🧠 ReasoningBank

### Purpose

Persistent memory system for agent reasoning patterns and decisions.

### Key Features

- **Pattern Storage**: Save decision-making processes
- **Semantic Search**: Find related patterns
- **Automatic Fallback**: Graceful degradation if AgentDB unavailable
- **Memory Compression**: 4x-32x reduction through quantization
- **Reflexion Learning**: Continuous improvement from patterns

### Architecture

```
ReasoningBank
├── Pattern Store (Semantic DB)
├── Decision Log (Execution history)
├── Learning Registry (Accumulated knowledge)
└── Fallback Handler (Reliability layer)
```

### Usage

```bash
# Store reasoning pattern
npx claude-flow@alpha memory store "solution-pattern" '{
  "problem": "optimization",
  "approach": "caching",
  "results": "2x speedup"
}' --reasoningbank

# Search patterns
npx claude-flow@alpha memory search "performance-optimization" --semantic

# List stored patterns
npx claude-flow@alpha memory list --patterns

# Clear old patterns
npx claude-flow@alpha memory prune --days 30
```

## 🔄 Hybrid Strategy

### Execution Flow

1. **Agent Task**: Execute agent task
2. **AgentDB Lookup**: Check vector database (fast path)
3. **Pattern Found**: Return cached result (96x-164x speedup)
4. **Not Found**: ReasoningBank lookup (fallback)
5. **Compute**: Generate new pattern if needed
6. **Store**: Save in both systems for future use

### Decision Logic

```
if pattern in AgentDB {
  return cached_result  // 96x-164x faster
} else if pattern in ReasoningBank {
  return reasoning_pattern  // fallback
} else {
  compute_new_pattern()  // fallback to computation
  store_in_agentdb()     // for future use
  store_in_reasoningbank()
}
```

## 💾 Memory Management

### Compression

ReasoningBank uses quantization to reduce memory:

- **4x Compression**: Standard mode
- **8x Compression**: Moderate mode
- **16x-32x Compression**: Maximum compression
- **Adaptive**: Automatic selection based on available memory

### Storage Locations

- **AgentDB**: Vector indices (fast search)
- **ReasoningBank**: Full patterns (semantic search)
- **Local Cache**: Recent patterns (L1 cache)
- **Disk**: Persistent backup (archival)

## 🔐 Memory Security

- **Encryption**: AES-256 for sensitive data
- **Access Control**: Agent-specific permissions
- **Audit Trail**: Complete memory access log
- **Data Retention**: Configurable deletion policies

## 📊 Monitoring

### Memory Stats

```bash
npx claude-flow@alpha memory stats
# Output:
# AgentDB size: 1.2 GB
# Vector indices: 250K patterns
# ReasoningBank size: 2.3 GB
# Compression ratio: 12x
# Hit rate: 87.3%
```

### Performance Dashboard

```bash
npx claude-flow@alpha memory dashboard
# Shows: Vector search performance, hit rates, response times
```

## 🚨 Troubleshooting

### Common Issues

1. **Memory Not Found**
   - Check AgentDB initialization
   - Verify ReasoningBank is configured
   - Check fallback handler status

2. **Slow Vector Search**
   - Rebuild indices
   - Check HNSW parameters
   - Monitor memory pressure

3. **Compression Issues**
   - Adjust compression ratio
   - Clear old patterns
   - Increase storage allocation

## 📚 Related Documentation

- [Agent System](./AGENT-SYSTEM.md)
- [MCP Tools](./MCP-TOOLS.md)
- [Installation](./INSTALLATION.md)
