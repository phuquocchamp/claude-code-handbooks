---
name: create-commit
description: Specialized for creating well-formatted commit messages with context-aware analysis
---

# Create Commit Message

Analyze the current git changes and generate a well-structured commit message following conventional commits format.

## Instructions

You will:
1. Examine the staged and unstaged changes in the repository
2. Determine the type of change (feat, fix, refactor, docs, test, chore, perf, style)
3. Identify the scope (affected component or module)
4. Write a clear, concise commit message following conventional commits format
5. Add a detailed body and footer if necessary

## Conventional Commits Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Guidelines

- **type**: feat (new feature), fix (bug fix), refactor (code refactor), docs (documentation), test (tests), chore (maintenance), perf (performance), style (formatting)
- **scope**: Component, module, or area affected (optional, omit if not applicable)
- **subject**: Imperative mood, present tense. Be concise (50 chars max). Do not capitalize. No period at end.
- **body**: Explain what and why, not how. Wrap at 72 characters. Use bullet points for multiple changes.
- **footer**: Reference issues (Closes #123) or breaking changes (BREAKING CHANGE: description)

## Current Changes Analysis

Review the output of:
- `git status` - to see staged and unstaged files
- `git diff --staged` - to see staged changes
- `git diff` - to see unstaged changes
