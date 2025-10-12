# Development Guide

This guide covers development workflows, testing, and contribution guidelines for the Urban Zones - Magentic-UI project.

## Development Environment Setup

### Quick Setup

```bash
# Clone and setup
git clone https://github.com/ghost-codez/urban-zones.git
cd urban-zones/magentic-ui
uv sync --dev

# Set API key
export OPENAI_API_KEY="your-api-key-here"

# Verify setup
uv run pytest tests/ -v
```

### Development Dependencies

The project includes these development tools:

- **pytest**: Testing framework
- **pytest-asyncio**: Async testing support
- **pytest-cov**: Coverage reporting
- **mypy**: Static type checking
- **pyright**: Additional type checking
- **ruff**: Fast Python linter and formatter
- **poethepoet**: Task runner

## Development Workflow

### 1. Making Changes

```bash
# Create a new branch (optional but recommended)
git checkout -b feature/your-feature-name

# Make your changes
# Edit files in src/, tests/, etc.

# Format code
uv run ruff format src tests

# Lint code
uv run ruff check src

# Type check
uv run pyright src
```

### 2. Testing

Run tests frequently during development:

```bash
# Run all tests
uv run pytest tests/ -v

# Run specific test file
uv run pytest tests/test_specific_file.py -v

# Run with coverage
uv run pytest tests/ --cov=src --cov-report=term-missing

# Run tests matching a pattern
uv run pytest tests/ -k "test_pattern" -v
```

### 3. Using Task Runner

The project uses `poethepoet` for common tasks:

```bash
# Format code
uv run poe fmt

# Lint code
uv run poe lint

# Type check with mypy
uv run poe mypy

# Type check with pyright
uv run poe pyright

# Run full test suite
uv run poe test

# Run all checks (format, lint, type check, test)
uv run poe check
```

## Testing Guidelines

### Test Structure

```
tests/
├── test_aggregate_mcp_workbench.py    # MCP workbench tests
├── test_magentic_ui_config_serialization.py  # Config tests
├── test_mcp_agent_integration.py      # Agent integration tests
├── test_playwright_controller.py      # Browser automation tests
├── test_playwright_state.py          # State management tests
└── test_url_status_manager.py        # URL management tests
```

### Writing Tests

1. **Follow naming conventions**:
   - Test files: `test_*.py`
   - Test functions: `test_*`

2. **Use async/await for async tests**:
```python
import pytest

@pytest.mark.asyncio
async def test_async_function():
    result = await some_async_function()
    assert result is not None
```

3. **Use fixtures for setup**:
```python
@pytest.fixture
def sample_data():
    return {"key": "value"}

def test_with_fixture(sample_data):
    assert sample_data["key"] == "value"
```

### Running Specific Tests

```bash
# Run tests for a specific module
uv run pytest tests/test_url_status_manager.py -v

# Run a specific test function
uv run pytest tests/test_url_status_manager.py::test_url_status_manager -v

# Run tests with specific markers
uv run pytest -m "not npx" tests/ -v
```

## Code Quality

### Formatting and Linting

The project uses `ruff` for both formatting and linting:

```bash
# Format code
uv run ruff format src tests

# Check for lint issues
uv run ruff check src

# Fix auto-fixable lint issues
uv run ruff check src --fix
```

### Type Checking

Two type checkers are configured:

```bash
# MyPy (strict mode)
uv run mypy src

# Pyright (strict mode)
uv run pyright src
```

## Dependency Management

### Adding Dependencies

```bash
# Add production dependency
uv add package-name

# Add development dependency
uv add --dev package-name

# Add optional dependency group
uv add --optional eval package-name
```

### Updating Dependencies

```bash
# Update all dependencies
uv sync --upgrade

# Update specific package
uv add package-name@latest
```

## Local Development Server

### Running the Application

```bash
# Standard run
uv run magentic-ui --port 8081

# Run without Docker (limited functionality)
uv run magentic-ui --run-without-docker --port 8081

# Run with debug mode
uv run magentic-ui --port 8081 --debug
```

### Environment Variables

Create a `.env` file in the `magentic-ui` directory:

```env
OPENAI_API_KEY=your-api-key-here
MAGENTIC_UI_PORT=8081
MAGENTIC_UI_DEBUG=true
```

## Git Workflow

### Commit Guidelines

Use conventional commit format:

```bash
# Feature
git commit -m "feat: add new web automation feature"

# Bug fix
git commit -m "fix: resolve session persistence issue"

# Documentation
git commit -m "docs: update installation guide"

# Tests
git commit -m "test: add tests for URL manager"

# Refactor
git commit -m "refactor: improve agent communication"
```

### Before Committing

```bash
# Run all checks
uv run poe check

# Stage changes
git add .

# Commit with descriptive message
git commit -m "type: description"

# Push to GitHub
git push origin master
```

## Debugging

### Common Debug Commands

```bash
# Run with verbose output
uv run magentic-ui --port 8081 --verbose

# Check Python path and imports
uv run python -c "import magentic_ui; print(magentic_ui.__file__)"

# Verify environment
uv run python -c "import sys; print(sys.path)"
```

### IDE Setup

For VS Code, create `.vscode/settings.json`:

```json
{
    "python.defaultInterpreterPath": "./.venv/bin/python",
    "python.testing.pytestEnabled": true,
    "python.testing.pytestArgs": ["tests"],
    "python.linting.enabled": true,
    "python.formatting.provider": "none",
    "[python]": {
        "editor.defaultFormatter": "charliermarsh.ruff",
        "editor.codeActionsOnSave": {
            "source.organizeImports": true
        }
    }
}
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run all tests and checks
5. Commit with conventional format
6. Push and create a pull request

---

**Happy Coding!** 🚀
