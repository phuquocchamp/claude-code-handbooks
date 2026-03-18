# Check Security Skill

## Purpose
Perform comprehensive security analysis on the Python project to identify vulnerabilities, insecure practices, and potential security risks.

## When to Use
Invoke this skill when:
- Adding new code or features that handle sensitive data
- Reviewing existing code for security issues
- Preparing for deployment or security audits
- User explicitly requests a security check
- Before committing changes that touch authentication, database, or API endpoints

## What It Checks

### 1. Code Vulnerabilities
- SQL injection risks in database queries
- Command injection in system calls
- Insecure deserialization
- Cross-site scripting (XSS) vulnerabilities
- Cross-site request forgery (CSRF) protection
- Hardcoded secrets and credentials

### 2. Dependency Security
- Known CVEs in installed packages
- Outdated or deprecated dependencies
- Unnecessary dependencies with security implications

### 3. Authentication & Authorization
- Weak password validation
- Missing access controls
- Insecure session management
- Token expiration and rotation

### 4. API Security
- Missing input validation
- Insufficient error handling (information disclosure)
- Weak rate limiting
- Missing CORS configuration issues
- Unsecured endpoints

### 5. Data Security
- Unencrypted sensitive data storage
- Missing data encryption in transit
- Insecure logging of sensitive data
- Database credential exposure

### 6. Configuration Security
- Exposed environment variables
- Debug mode enabled in production
- Insecure default values
- Missing security headers

## How It Works

The skill performs:
1. **Static code analysis** - Scans Python files for vulnerable patterns
2. **Dependency checking** - Examines requirements files and installed packages
3. **Configuration review** - Checks environment and config files
4. **Best practices audit** - Verifies security best practices are followed

## Output Format

For each issue found:
- **Severity**: Critical, High, Medium, Low
- **Location**: File path and line number
- **Issue**: Description of the vulnerability
- **Risk**: Potential impact
- **Recommendation**: How to fix it

## Integration with Project

For this FastAPI project:
- Checks SQLAlchemy queries for injection vulnerabilities
- Validates Pydantic schema security
- Reviews HTTP endpoint security
- Checks database connection security
- Validates error handling and logging

## Example Usage

```
User: Check the security of my project
Claude: [Runs check-security skill]
- Analyzes all Python code
- Reviews dependencies
- Checks configurations
- Reports findings with severity levels and fixes
```
