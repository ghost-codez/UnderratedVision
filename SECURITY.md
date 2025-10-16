# Security Guidelines for UnderratedVision

## 🔐 API Key Management

### Never Commit API Keys

**CRITICAL**: Never commit your `.env` file or any file containing API keys to version control.

### Setup Instructions

1. **Copy the template file**:
   ```bash
   cp .env.example .env
   ```

2. **Add your API key** (local only, never commit):
   ```bash
   # Edit .env file
   OPENAI_API_KEY=sk-proj-your-actual-key-here
   ```

3. **Verify .env is ignored**:
   ```bash
   git status
   # Should NOT show .env file
   ```

### What's Protected

The `.gitignore` file protects:
- ✅ `.env` - Your environment variables
- ✅ `.env.local` - Local overrides
- ✅ `.env.development.local` - Development secrets
- ✅ `.env.production.local` - Production secrets
- ✅ All files matching `*api*key*` pattern
- ✅ All files matching `*secret*` pattern

### If You Accidentally Committed Secrets

**IMMEDIATE ACTION REQUIRED**:

1. **Revoke the compromised API key**:
   - Go to https://platform.openai.com/api-keys
   - Delete the exposed key immediately
   - Create a new API key

2. **Remove from git history** (if needed):
   ```bash
   # Use git-filter-branch or BFG Repo-Cleaner
   # See: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
   ```

3. **Update your local .env**:
   ```bash
   # Add new API key to .env
   OPENAI_API_KEY=sk-proj-your-new-key-here
   ```

---

## 🔒 Environment Variables

### Required Variables

```bash
# REQUIRED - Your OpenAI API key
OPENAI_API_KEY=sk-proj-...
```

### Optional Variables

```bash
# Application port (default: 8081)
PORT=8081

# Application host (default: 127.0.0.1)
HOST=127.0.0.1

# Logging level (default: INFO)
LOG_LEVEL=INFO

# Alternative LLM providers
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_ENDPOINT=...
OLLAMA_BASE_URL=http://localhost:11434
```

---

## 🛡️ Best Practices

### Local Development

1. **Always use `.env` for local secrets**:
   ```bash
   cp .env.example .env
   # Edit .env with your actual keys
   ```

2. **Never share your `.env` file**:
   - Don't email it
   - Don't commit it
   - Don't share it in chat/Slack

3. **Use the startup script**:
   ```bash
   ./start_underratedvision.sh
   ```

### Production Deployment

1. **Use environment variables directly**:
   ```bash
   export OPENAI_API_KEY="your-production-key"
   ./start_underratedvision.sh
   ```

2. **Use secrets management**:
   - Docker Secrets
   - Kubernetes Secrets
   - AWS Secrets Manager
   - HashiCorp Vault

3. **Never hardcode secrets** in:
   - Source code
   - Configuration files
   - Docker images
   - Git repositories

### GitHub Security

1. **Enable branch protection**:
   - Require pull request reviews
   - Require status checks to pass
   - Dismiss stale pull request approvals

2. **Use GitHub Secrets** for CI/CD:
   ```yaml
   - name: Start Application
     env:
       OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
     run: ./start_underratedvision.sh
   ```

3. **Enable secret scanning**:
   - GitHub will alert if secrets are detected
   - Automatically revoke exposed tokens

---

## 🚨 Security Checklist

Before pushing to GitHub:

- [ ] `.env` file is NOT in git status
- [ ] `.gitignore` includes `.env` and `*.env`
- [ ] No API keys in README or documentation
- [ ] No API keys in code comments
- [ ] No API keys in commit messages
- [ ] `.env.example` has placeholder values only
- [ ] All sensitive files are in `.gitignore`

---

## 📚 Additional Resources

- [GitHub: Removing Sensitive Data](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
- [OWASP: Secrets Management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
- [OpenAI: API Key Security](https://platform.openai.com/docs/guides/production-best-practices/api-key-security)

---

**Status**: ✅ Your repository is secure and ready for production!

