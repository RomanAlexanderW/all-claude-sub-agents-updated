#!/usr/bin/env node
/**
 * Validates all agents conform to Claude Flow v2.7.0 format
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const agentsDir = path.join(__dirname, '..', '.claude', 'agents');

const requiredFields = ['name', 'type', 'color', 'description', 'capabilities', 'priority'];
const validTypes = ['developer', 'tester', 'coordinator', 'analyzer', 'security',
                    'synchronizer', 'reviewer', 'planner', 'researcher', 'specialist',
                    'optimizer', 'manager', 'engineer', 'architect', 'documenter'];
const validPriorities = ['critical', 'high', 'medium', 'low'];

let totalAgents = 0;
let validAgents = 0;
let errors = [];

function validateAgent(filePath) {
  const content = fs.readFileSync(filePath, 'utf-8');
  const fileName = path.basename(filePath);

  // Check for YAML frontmatter
  if (!content.startsWith('---')) {
    errors.push(`${fileName}: Missing YAML frontmatter`);
    return false;
  }

  const frontmatterEnd = content.indexOf('---', 3);
  if (frontmatterEnd === -1) {
    errors.push(`${fileName}: Invalid YAML frontmatter`);
    return false;
  }

  const frontmatter = content.substring(3, frontmatterEnd);

  // Check required fields
  for (const field of requiredFields) {
    if (!frontmatter.includes(`${field}:`)) {
      errors.push(`${fileName}: Missing required field '${field}'`);
      return false;
    }
  }

  // Check valid type
  const typeMatch = frontmatter.match(/type:\s*(\w+)/);
  if (typeMatch && !validTypes.includes(typeMatch[1])) {
    errors.push(`${fileName}: Invalid type '${typeMatch[1]}'`);
    return false;
  }

  // Check valid priority
  const priorityMatch = frontmatter.match(/priority:\s*(\w+)/);
  if (priorityMatch && !validPriorities.includes(priorityMatch[1])) {
    errors.push(`${fileName}: Invalid priority '${priorityMatch[1]}'`);
    return false;
  }

  return true;
}

function walkDir(dir) {
  if (!fs.existsSync(dir)) {
    console.log(`Directory not found: ${dir} (agents not yet added)`);
    return;
  }

  const files = fs.readdirSync(dir);

  for (const file of files) {
    const filePath = path.join(dir, file);
    const stat = fs.statSync(filePath);

    if (stat.isDirectory()) {
      walkDir(filePath);
    } else if (file.endsWith('.md')) {
      totalAgents++;
      if (validateAgent(filePath)) {
        validAgents++;
      }
    }
  }
}

console.log('Validating Claude Flow v2.7.0 agents...\n');
walkDir(agentsDir);

console.log('='.repeat(50));
console.log('VALIDATION RESULTS');
console.log('='.repeat(50));
if (totalAgents > 0) {
  console.log(`Total agents: ${totalAgents}`);
  console.log(`Valid agents: ${validAgents}`);
  console.log(`Invalid agents: ${totalAgents - validAgents}`);
  console.log(`Success rate: ${((validAgents / totalAgents) * 100).toFixed(1)}%`);

  if (errors.length > 0) {
    console.log('\nErrors (first 20):');
    errors.slice(0, 20).forEach(e => console.log(`  - ${e}`));
    if (errors.length > 20) {
      console.log(`  ... and ${errors.length - 20} more`);
    }
  }
  process.exit(errors.length > 0 ? 1 : 0);
} else {
  console.log('No agents found yet. Agent directory ready for population.');
  console.log('Expected agents directory: ' + agentsDir);
  process.exit(0);
}
