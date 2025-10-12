# Installation Guide

This guide provides detailed instructions for setting up the Urban Zones - Magentic-UI project.

## Prerequisites

Before you begin, ensure you have the following installed:

### Required Software

1. **Python 3.10+**
   - Download from [python.org](https://www.python.org/downloads/)
   - Verify installation: `python --version`

2. **Git**
   - Download from [git-scm.com](https://git-scm.com/)
   - Verify installation: `git --version`

3. **Docker Desktop**
   - Download from [docker.com](https://www.docker.com/products/docker-desktop/)
   - Verify installation: `docker --version`

4. **uv (Python Package Manager)**
   - Install via pip: `pip install uv`
   - Or via curl: `curl -LsSf https://astral.sh/uv/install.sh | sh`
   - Verify installation: `uv --version`

### API Keys

- **OpenAI API Key**: Required for AI functionality
  - Get from [OpenAI Platform](https://platform.openai.com/api-keys)

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/ghost-codez/urban-zones.git
cd urban-zones
```

### 2. Set Up Python Environment

Navigate to the magentic-ui directory and set up the environment:

```bash
cd magentic-ui
uv sync --dev
```

This will:
- Create a virtual environment in `.venv/`
- Install all production dependencies
- Install development dependencies (pytest, mypy, ruff, etc.)
- Download and set up Python 3.12.9 if needed

### 3. Configure Environment Variables

Set your OpenAI API key:

**macOS/Linux:**
```bash
export OPENAI_API_KEY="your-api-key-here"
```

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY="your-api-key-here"
```

**Windows (Command Prompt):**
```cmd
set OPENAI_API_KEY=your-api-key-here
```

### 4. Verify Installation

Run the test suite to ensure everything is working:

```bash
uv run pytest tests/ -v
```

Expected output:
```
====== test session starts ======
...
tests/test_magentic_ui_config_serialization.py::test_yaml_deserialize PASSED
tests/test_magentic_ui_config_serialization.py::test_yaml_serialize_roundtrip PASSED
tests/test_url_status_manager.py::test_url_status_manager PASSED
...
====== X passed in Y.YYs ======
```

### 5. Launch the Application

Start Magentic-UI:

```bash
uv run magentic-ui --port 8081
```

The application will be available at: http://localhost:8081

## Alternative Installation Methods

### Using Virtual Environment Manually

If you prefer not to use `uv`:

```bash
cd magentic-ui
python -m venv .venv

# Activate virtual environment
# macOS/Linux:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate

# Install dependencies
pip install -e .
pip install -e ".[eval,azure,ollama]"  # Optional extras
pip install pytest pytest-asyncio pytest-cov  # Dev dependencies

# Run tests
python -m pytest tests/ -v

# Launch application
python -m magentic_ui.backend.cli --port 8081
```

### Docker-Only Setup

For a containerized setup:

```bash
cd magentic-ui
docker-compose up -d
```

## Troubleshooting

### Common Issues

1. **Python Version Error**
   - Ensure Python 3.10+ is installed
   - Use `python --version` to check

2. **uv Command Not Found**
   - Install uv: `pip install uv`
   - Or use the curl installer

3. **Docker Issues**
   - Ensure Docker Desktop is running
   - Check with `docker ps`

4. **Permission Errors (macOS/Linux)**
   - Use `sudo` if needed for system-wide installations
   - Consider using `--user` flag with pip

5. **Virtual Environment Activation Issues**
   - **macOS/Linux**: Use `source .venv/bin/activate`
   - **Windows**: Use `.venv\Scripts\activate`

### Getting Help

If you encounter issues:

1. Check the [GitHub Issues](https://github.com/ghost-codez/urban-zones/issues)
2. Review the [original Magentic-UI documentation](https://github.com/microsoft/magentic-ui)
3. Ensure all prerequisites are properly installed

## Next Steps

After successful installation:

1. Read the main [README.md](README.md) for usage instructions
2. Explore the [development workflow](README.md#-development-workflow)
3. Check out the example notebooks in `magentic-ui/docs/tutorials/`

---

**Installation Complete!** 🎉

You're now ready to use Magentic-UI for web automation and AI-powered tasks.
