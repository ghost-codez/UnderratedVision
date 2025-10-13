# UnderratedVision Troubleshooting Guide

This guide helps resolve common issues when setting up and using UnderratedVision.

## 🚨 Common Installation Issues

### Docker Issues

**Problem**: Docker not found or permission denied
```bash
docker: command not found
# or
permission denied while trying to connect to the Docker daemon
```

**Solutions**:
```bash
# Install Docker (Ubuntu/Debian)
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
# Log out and back in

# macOS - Install Docker Desktop
# Download from https://www.docker.com/products/docker-desktop/

# Windows - Use WSL2 + Docker Desktop
# Enable WSL2 and install Docker Desktop with WSL2 integration
```

### Python Environment Issues

**Problem**: Python version conflicts
```bash
python: command not found
# or
This package requires Python >=3.10
```

**Solutions**:
```bash
# Check Python version
python3 --version

# Install Python 3.10+ (Ubuntu/Debian)
sudo apt update
sudo apt install python3.10 python3.10-venv python3.10-pip

# macOS with Homebrew
brew install python@3.10

# Windows - Download from python.org
```

**Problem**: Virtual environment activation fails
```bash
source .venv/bin/activate: No such file or directory
```

**Solutions**:
```bash
# Ensure you're in the right directory
cd UnderratedVision/magentic-ui

# Create virtual environment if missing
python3 -m venv .venv

# Windows activation
.venv\Scripts\activate

# macOS/Linux activation
source .venv/bin/activate
```

### Git Submodule Issues

**Problem**: Magentic-UI submodule not found
```bash
fatal: not a git repository: magentic-ui/.git
```

**Solutions**:
```bash
# Initialize submodules
git submodule update --init --recursive

# If still failing, re-add submodule
git submodule deinit magentic-ui
git rm magentic-ui
git submodule add https://github.com/microsoft/magentic-ui.git magentic-ui
git submodule update --init --recursive
```

## 🔧 Runtime Issues

### API Key Problems

**Problem**: OpenAI API key not working
```bash
Error: Invalid API key provided
```

**Solutions**:
```bash
# Verify API key is set
echo $OPENAI_API_KEY

# Set API key (replace with your actual key)
export OPENAI_API_KEY="sk-your-actual-key-here"

# Make permanent (add to ~/.bashrc or ~/.zshrc)
echo 'export OPENAI_API_KEY="sk-your-actual-key-here"' >> ~/.bashrc
source ~/.bashrc

# Windows PowerShell
$env:OPENAI_API_KEY="sk-your-actual-key-here"
```

### Port Conflicts

**Problem**: Port 8081 already in use
```bash
Error: Port 8081 is already in use
```

**Solutions**:
```bash
# Use different port
magentic-ui --port 8082

# Find and kill process using port 8081
lsof -ti:8081 | xargs kill -9

# Windows
netstat -ano | findstr :8081
taskkill /PID <PID> /F
```

### Extension Loading Issues

**Problem**: UnderratedVision agents not loading
```bash
ModuleNotFoundError: No module named 'agents'
```

**Solutions**:
```bash
# Ensure you're in the extensions directory
cd UnderratedVision/extensions

# Check Python path
python -c "import sys; print(sys.path)"

# Add current directory to Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# Test agent loading
python -c "from agents import agent_registry; print('✅ Success')"
```

## 🏢 Domain-Specific Issues

### Real Estate Agent Issues

**Problem**: Property data not accessible
```bash
Error: Unable to access property database
```

**Solutions**:
- Verify API keys for real estate data sources
- Check network connectivity to MLS systems
- Ensure proper authentication for property databases
- Review rate limiting and usage quotas

### Construction Agent Issues

**Problem**: Safety compliance data outdated
```bash
Warning: Safety regulations may be outdated
```

**Solutions**:
- Update safety regulation databases
- Verify compliance with local building codes
- Check for recent regulatory changes
- Refresh certification requirements

### Healthcare Agent Issues

**Problem**: HIPAA compliance warnings
```bash
Warning: Potential HIPAA compliance issue
```

**Solutions**:
- Review data handling procedures
- Ensure proper encryption for medical data
- Verify access controls and audit logging
- Update privacy protection measures

## 🔄 Performance Issues

### Slow Response Times

**Problem**: Agents taking too long to respond
```bash
Timeout: Agent response exceeded 30 seconds
```

**Solutions**:
```bash
# Increase timeout settings
export AGENT_TIMEOUT=60

# Check system resources
htop  # Linux/macOS
# Task Manager on Windows

# Optimize Docker resources
docker system prune
docker stats
```

### Memory Issues

**Problem**: Out of memory errors
```bash
MemoryError: Unable to allocate memory
```

**Solutions**:
```bash
# Check memory usage
free -h  # Linux
vm_stat  # macOS

# Increase Docker memory limits
# Docker Desktop -> Settings -> Resources -> Memory

# Process large datasets in chunks
# Implement pagination for large queries
```

## 🌐 Network Issues

### Firewall Problems

**Problem**: Cannot access web interface
```bash
Connection refused: localhost:8081
```

**Solutions**:
```bash
# Check if service is running
curl http://localhost:8081

# Verify firewall settings
sudo ufw status  # Ubuntu
# Windows Firewall settings

# Test with different network interface
magentic-ui --host 0.0.0.0 --port 8081
```

### Proxy Issues

**Problem**: Cannot connect through corporate proxy
```bash
ProxyError: Cannot connect to proxy
```

**Solutions**:
```bash
# Set proxy environment variables
export HTTP_PROXY=http://proxy.company.com:8080
export HTTPS_PROXY=http://proxy.company.com:8080
export NO_PROXY=localhost,127.0.0.1

# Configure pip for proxy
pip install --proxy http://proxy.company.com:8080 magentic-ui
```

## 🧪 Testing Issues

### Test Failures

**Problem**: Tests failing during setup
```bash
FAILED tests/test_agent_integration.py
```

**Solutions**:
```bash
# Run tests with verbose output
cd magentic-ui
uv run pytest tests/ -v -s

# Run specific test
uv run pytest tests/test_agent_integration.py -v

# Skip failing tests temporarily
uv run pytest tests/ -k "not test_failing_function"

# Update test dependencies
uv sync --dev
```

## 📞 Getting Additional Help

### Log Collection

When reporting issues, include these logs:
```bash
# System information
uname -a
python3 --version
docker --version

# Application logs
tail -f ~/.magentic-ui/logs/application.log

# Docker logs
docker logs <container_id>

# Extension logs
cd extensions
python -c "import logging; logging.basicConfig(level=logging.DEBUG)"
```

### Community Support

- **GitHub Issues**: https://github.com/ghost-codez/UnderratedVision/issues
- **GitHub Discussions**: https://github.com/ghost-codez/UnderratedVision/discussions
- **Documentation**: Check README.md and docs/ directory
- **Upstream Issues**: https://github.com/microsoft/magentic-ui/issues

### Enterprise Support

For enterprise deployments and custom domain implementations:
- Review our enterprise documentation
- Consider professional services for complex integrations
- Evaluate dedicated support options for mission-critical deployments

---

**Still having issues?** Open a GitHub issue with:
1. Your operating system and version
2. Python and Docker versions
3. Complete error messages and logs
4. Steps to reproduce the problem
5. Expected vs. actual behavior

We're here to help you succeed with UnderratedVision! 🚀
