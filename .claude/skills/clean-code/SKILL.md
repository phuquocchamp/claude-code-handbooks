---
name: clean-code
description: Review changed code for code smells, identify refactoring opportunities, and suggest improvements for better maintainability
---

# Code Review & Refactoring

Review the changed code and provide actionable feedback on code quality, maintainability, and best practices.

## What to analyze:
- **Code smells**: Duplication, long methods/functions, complex conditionals, magic numbers, unclear naming
- **Design issues**: Tight coupling, violation of SOLID principles, missing abstractions
- **Maintainability**: Readability, testability, consistency with codebase patterns
- **Performance**: Unnecessary iterations, inefficient algorithms, N+1 queries
- **Best practices**: Error handling, logging, security considerations

## How to present findings:
1. Group issues by severity (critical, important, minor)
2. Explain *why* something is a problem
3. Provide specific refactoring suggestions with code examples
4. Highlight what's working well
5. Consider the tradeoffs in your suggestions

## Focus on:
- Changes that affect behavior or maintainability
- Patterns that repeat across the diff
- Issues that will compound over time
- Context-aware advice (not dogmatic rules)

Start by asking which files or sections you'd like reviewed, or analyze the current git diff if available.
