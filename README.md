# Urban Zones - Magentic-UI Setup

This repository contains a complete setup and deployment of Microsoft's Magentic-UI, a research prototype of a human-centered web agent powered by a multi-agent system built using AutoGen.

## 🚀 Quick Start

### Prerequisites
- Python 3.10+ (tested with 3.12.9)
- Docker Desktop
- Git
- OpenAI API key

### Installation & Setup

1. **Clone the repository**:
```bash
git clone https://github.com/ghost-codez/urban-zones.git
cd urban-zones
```

2. **Set up the Python environment**:
```bash
cd magentic-ui
uv sync --dev
```

3. **Set your OpenAI API key**:
```bash
export OPENAI_API_KEY="your-api-key-here"
```

4. **Launch Magentic-UI**:
```bash
uv run magentic-ui --port 8081
```

5. **Access the interface**: Navigate to http://localhost:8081

## 🧪 Testing

Run the test suite to verify everything is working:

```bash
cd magentic-ui

# Option 1: Using uv (recommended)
uv run pytest tests/ -v

# Option 2: Using virtual environment
source .venv/bin/activate  # macOS/Linux
python -m pytest tests/ -v
```

Test status:
- Configuration serialization: ✅
- URL status management: ✅
- MCP workbench functionality: ✅
- Playwright controller: ✅
- Agent integration: ✅

## 🛠️ Development Workflow

### Local Development

1. **Make changes** to the code
2. **Run tests** to ensure everything works:
```bash
uv run pytest tests/ -v
```
3. **Test the application** locally:
```bash
uv run magentic-ui --port 8081
```

### Environment Management

**Using uv (recommended)**:
```bash
# Install dependencies
uv sync --dev

# Run commands in the virtual environment
uv run python your_script.py
uv run pytest tests/
uv run magentic-ui

# Add new dependencies
uv add package-name
uv add --dev package-name  # for dev dependencies
```

**Manual virtual environment**:
```bash
# Activate environment (macOS/Linux)
source .venv/bin/activate

# Activate environment (Windows)
.venv\Scripts\activate

# Run commands
python -m pytest tests/
python -m magentic_ui.backend.cli

# Deactivate when done
deactivate
```

## 📤 Pushing to GitHub

1. **Stage your changes**:
```bash
git add .
```

2. **Commit with a descriptive message**:
```bash
git commit -m "feat: add new feature or fix: resolve issue"
```

3. **Push to GitHub**:
```bash
git push origin master
```

### Git Workflow Best Practices

```bash
# Check status
git status

# View changes
git diff

# Stage specific files
git add file1.py file2.py

# Commit with conventional commit format
git commit -m "type: description"
# Types: feat, fix, docs, style, refactor, test, chore

# Push to remote
git push origin master

# Pull latest changes
git pull origin master
```

## 📁 Project Structure

```
urban-zones/
├── magentic-ui/           # Main Magentic-UI repository
│   ├── src/               # Python source code
│   │   └── magentic_ui/   # Main package
│   ├── frontend/          # Gatsby frontend
│   ├── tests/             # Test suite
│   ├── docker/            # Docker configurations
│   ├── .venv/             # Python virtual environment
│   ├── pyproject.toml     # Python project configuration
│   ├── uv.lock           # Dependency lock file
│   └── pytest.ini        # Test configuration
├── .gitignore             # Git ignore rules
└── README.md              # This documentation
```

## 🔧 Technical Details

- **Package Manager**: uv (fast Python package manager)
- **Backend**: FastAPI with SQLite database
- **Frontend**: Gatsby static site generator
- **Agents**: AutoGen multi-agent framework
- **Browser Automation**: Playwright in Docker containers
- **Testing**: pytest with asyncio support
- **Environment**: Isolated Python virtual environment

## 🌟 Features

- Human-centered web agent interface
- Multi-agent collaboration system
- Web browsing and automation capabilities
- Code generation and execution
- Session management and persistence
- Real-time agent communication
- File upload and analysis
- MCP (Model Context Protocol) server integration

## 📝 Important Notes

- This is a research prototype from Microsoft Research
- Requires OpenAI API key for full functionality
- Docker containers are automatically managed
- All dependencies are isolated in virtual environments
- Use `uv` for faster dependency management
- Tests must pass before pushing to GitHub

## 🔗 References

- **Original Repository**: https://github.com/microsoft/magentic-ui
- **GitHub Repository**: https://github.com/ghost-codez/urban-zones
- **uv Documentation**: https://docs.astral.sh/uv/

---

**Status**: ✅ Fully operational and ready for development!
