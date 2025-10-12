# Quick Reference Guide

Essential commands for working with the Urban Zones - Magentic-UI project.

## 🚀 Quick Start Commands

```bash
# Clone and setup
git clone https://github.com/ghost-codez/urban-zones.git
cd urban-zones/magentic-ui
uv sync --dev

# Set API key and run
export OPENAI_API_KEY="your-key"
uv run magentic-ui --port 8081
```

## 📦 Environment Management

### Using uv (Recommended)

```bash
# Setup environment
uv sync --dev

# Run commands
uv run pytest tests/
uv run magentic-ui --port 8081
uv run python script.py

# Add dependencies
uv add package-name
uv add --dev dev-package-name
```

### Manual Virtual Environment

```bash
# Create and activate
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows

# Install and run
pip install -e .
python -m pytest tests/
python -m magentic_ui.backend.cli --port 8081
```

## 🧪 Testing Commands

```bash
# Run all tests
uv run pytest tests/ -v

# Run specific test file
uv run pytest tests/test_config.py -v

# Run with coverage
uv run pytest tests/ --cov=src --cov-report=term-missing

# Run specific test function
uv run pytest tests/test_config.py::test_yaml_deserialize -v
```

## 🔧 Development Tools

### Code Quality

```bash
# Format code
uv run ruff format src tests

# Lint code
uv run ruff check src
uv run ruff check src --fix  # Auto-fix

# Type checking
uv run mypy src
uv run pyright src
```

### Task Runner (poethepoet)

```bash
uv run poe fmt      # Format code
uv run poe lint     # Lint code
uv run poe mypy     # Type check with mypy
uv run poe pyright  # Type check with pyright
uv run poe test     # Run tests
uv run poe check    # Run all checks
```

## 🌐 Application Commands

### Running the Server

```bash
# Standard run
uv run magentic-ui --port 8081

# Without Docker (limited features)
uv run magentic-ui --run-without-docker --port 8081

# With debug mode
uv run magentic-ui --port 8081 --debug

# Custom configuration
uv run magentic-ui --port 8081 --config custom_config.yaml
```

### Alternative Entry Points

```bash
# Using module
uv run python -m magentic_ui.backend.cli --port 8081

# Using CLI script
uv run magentic-cli --port 8081
```

## 📝 Git Workflow

### Basic Commands

```bash
# Check status
git status
git diff

# Stage and commit
git add .
git commit -m "feat: add new feature"

# Push to GitHub
git push origin master

# Pull latest changes
git pull origin master
```

### Conventional Commits

```bash
git commit -m "feat: add new feature"
git commit -m "fix: resolve bug"
git commit -m "docs: update readme"
git commit -m "test: add unit tests"
git commit -m "refactor: improve code structure"
git commit -m "chore: update dependencies"
```

## 🐛 Debugging Commands

### Environment Debugging

```bash
# Check Python version and path
uv run python --version
uv run which python

# Check installed packages
uv run pip list

# Verify imports
uv run python -c "import magentic_ui; print(magentic_ui.__file__)"

# Check environment variables
uv run python -c "import os; print(os.environ.get('OPENAI_API_KEY', 'Not set'))"
```

### Application Debugging

```bash
# Run with verbose logging
uv run magentic-ui --port 8081 --verbose

# Check Docker status
docker ps
docker images

# View logs
docker logs container_name
```

## 📊 Project Information

### File Structure

```
urban-zones/
├── magentic-ui/
│   ├── src/magentic_ui/     # Main package
│   ├── tests/               # Test suite
│   ├── .venv/              # Virtual environment
│   ├── pyproject.toml      # Project config
│   └── uv.lock            # Dependency lock
├── README.md               # Main documentation
├── INSTALL.md             # Installation guide
├── DEVELOPMENT.md         # Development guide
└── QUICK_REFERENCE.md     # This file
```

### Key Files

- `pyproject.toml`: Project configuration and dependencies
- `uv.lock`: Locked dependency versions
- `pytest.ini`: Test configuration
- `.gitignore`: Git ignore rules

## 🔗 Useful URLs

- **Local App**: http://localhost:8081
- **GitHub Repo**: https://github.com/ghost-codez/urban-zones
- **Original Repo**: https://github.com/microsoft/magentic-ui
- **uv Docs**: https://docs.astral.sh/uv/

## 🆘 Troubleshooting

### Common Issues

```bash
# uv command not found
pip install uv

# Permission denied (macOS/Linux)
chmod +x .venv/bin/activate

# Docker not running
# Start Docker Desktop

# Tests failing
uv run pytest tests/ -v --tb=short

# Import errors
uv sync --dev
```

### Reset Environment

```bash
# Clean and reinstall
rm -rf .venv/
uv sync --dev

# Or with manual venv
rm -rf .venv/
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

---

**Keep this handy for quick reference!** 📌
