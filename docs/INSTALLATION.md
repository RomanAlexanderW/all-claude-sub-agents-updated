# Installation Guide - Claude Flow v3.0.0

## System Requirements

### Minimum Requirements

- **Node.js**: 18.0.0 or higher (LTS recommended)
- **npm**: 9.0.0 or higher
- **Memory**: 2 GB RAM minimum (4 GB+ recommended)
- **Disk**: 500 MB free space
- **OS**: Linux, macOS, or Windows

### Recommended Setup

- **Node.js**: 20.x LTS
- **npm**: 10.x
- **Memory**: 8+ GB for large swarms
- **Disk**: 2+ GB for AgentDB indices
- **OS**: Linux (Ubuntu 20.04+) for best compatibility

## Installation Steps

### 1. Install Claude Code (Required)

```bash
# Install Claude Code globally
npm install -g @anthropic-ai/claude-code

# Verify installation
claude --version
```

### 2. Install Claude Flow v3.0.0

```bash
# Using npx (recommended)
npx claude-flow@v3alpha init --force

# Or install globally
npm install -g claude-flow@v3alpha
claude-flow --version
# Should output: v3.0.0-alpha.185
```

### 3. Clone This Repository

```bash
git clone https://github.com/RomanAlexanderW/all-claude-sub-agents-updated.git
cd all-claude-sub-agents-updated

# Install dependencies
npm install
```

### 4. Initialize AgentDB

```bash
# Initialize with default settings
npx claude-flow@v3alpha init --force

# Or with custom configuration
npx claude-flow@v3alpha init --agentdb --reasoningbank --vector-search
```

## Platform-Specific Instructions

### macOS

```bash
# Using Homebrew (optional)
brew install node@20

# Then follow standard installation
npx claude-flow@v3alpha init --force
```

### Linux (Ubuntu/Debian)

```bash
# Update package manager
sudo apt-get update

# Install Node.js 18+
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

# Install Claude Flow
npx claude-flow@v3alpha init --force
```

### Windows

```powershell
# Using Chocolatey (recommended)
choco install nodejs

# Or download from https://nodejs.org/

# Then install Claude Flow
npx claude-flow@v3alpha init --force
```

### Docker

```bash
# Use provided Docker setup
docker build -t claude-flow:3.0.0 .

# Run container
docker run -it claude-flow:3.0.0 npx claude-flow@v3alpha init --force
```

## Configuration

### Verify Installation

```bash
# Check Claude Code
claude --version

# Check Claude Flow
npx claude-flow@v3alpha --version

# Run diagnostics
npx claude-flow@v3alpha diagnostics
```

### Configure AgentDB

Create `.claude/agentdb-config.json`:

```json
{
  "indexType": "hnsw",
  "vectorDimension": 1536,
  "maxElements": 100000,
  "efConstruction": 200,
  "efSearch": 100,
  "quantization": true,
  "compressionRatio": 16,
  "storage": "./agentdb-data"
}
```

### Configure ReasoningBank

Edit `.claude/settings.json`:

```json
{
  "reasoningBankSettings": {
    "enabled": true,
    "autoFallback": true,
    "memoryCompression": "quantization",
    "compressionRatio": "4x-32x",
    "storage": "./memory-data"
  }
}
```

## Troubleshooting Installation

### Issue: Node.js Version Too Old

```bash
# Check version
node --version

# Update Node.js
nvm install 20
nvm use 20

# Or via npm
npm install -g n
n stable
```

### Issue: Permission Denied

```bash
# Fix npm permissions
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
export PATH=~/.npm-global/bin:$PATH

# Add to ~/.bashrc or ~/.zshrc
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

### Issue: AgentDB Compilation Error

```bash
# Install build tools
# macOS
xcode-select --install

# Linux (Ubuntu)
sudo apt-get install build-essential python3

# Windows
npm install -g windows-build-tools
```

### Issue: Memory Issues with Large Swarms

```bash
# Increase Node.js heap size
export NODE_OPTIONS="--max-old-space-size=8192"

# Or in commands
NODE_OPTIONS="--max-old-space-size=8192" npx claude-flow@v3alpha swarm "task"
```

## Verification

```bash
# Test basic functionality
npx claude-flow@v3alpha agents list --limit 5

# Test memory system
npx claude-flow@v3alpha memory store "test-key" "test-value" --reasoningbank

# Test vector search
npx claude-flow@v3alpha memory search "test" --agentdb

# Run health check
npx claude-flow@v3alpha diagnostics --full
```

## Next Steps

1. **Read the Tutorial**: `./tutorial.md`
2. **Explore Agents**: `npx claude-flow@v3alpha agents list`
3. **Create First Swarm**: `npx claude-flow@v3alpha swarm "simple-task" --claude`
4. **Store Memories**: `npx claude-flow@v3alpha memory store key value --reasoningbank`
5. **Learn Hive-Mind**: `npx claude-flow@v3alpha hive-mind wizard`

## Support & Resources

- **Documentation**: `./docs/`
- **Agents Directory**: `./agents/`
- **Flow Strategies**: `./flowstrats.md`
- **Quick Reference**: `./agents-quickref.md`
- **Official Repo**: https://github.com/ruvnet/claude-flow

## Environment Variables

```bash
# Set custom AgentDB location
export AGENTDB_PATH="/custom/path"

# Enable debug logging
export CLAUDE_FLOW_DEBUG=true

# Set memory backend
export MEMORY_BACKEND="agentdb"  # or "reasoningbank"

# Configure performance
export MAX_WORKERS=32
export VECTOR_SEARCH_TIMEOUT=30000
```

---

**Installation Complete!** You're ready to use Claude Flow v3.0.0. Start with `npx claude-flow@v3alpha --help`
