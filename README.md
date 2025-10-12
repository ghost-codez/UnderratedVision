# Urban Zones - Magentic-UI Setup

This repository contains a complete setup and deployment of Microsoft's Magentic-UI, a research prototype of a human-centered web agent powered by a multi-agent system built using AutoGen.

## 🚀 Quick Start

Magentic-UI is successfully set up and running locally on port 8081.

### Prerequisites
- Python 3.10+ (tested with 3.13.7)
- Docker Desktop
- Node.js 18+ (tested with 22.17.1)

### Setup Complete ✅

The following components have been successfully configured:

1. **Environment Setup**
   - Python virtual environment in `magentic-ui/.venv`
   - All Python dependencies installed (173 packages)
   - Node.js dependencies installed via Yarn (1,704 packages)

2. **Frontend Build**
   - Gatsby frontend built and deployed
   - Static assets copied to backend UI directory

3. **Docker Environment**
   - Docker containers automatically pulled from GHCR
   - Browser automation environment ready
   - Python execution environment configured

4. **Application Launch**
   - Server running on http://localhost:8081
   - Database initialized
   - API endpoints active and healthy

## 🎯 Usage

1. **Access the Interface**: Navigate to http://localhost:8081
2. **Configure API Key**: Set your OpenAI API key in the settings
3. **Create Sessions**: Start new sessions for different tasks
4. **Interact with Agents**: Use the multi-agent system for web automation and code generation

## 🧪 Testing

Tests have been verified and are working:
- Configuration serialization: ✅
- URL status management: ✅
- MCP workbench functionality: ✅

To run tests:
```bash
cd magentic-ui
source .venv/Scripts/activate
python -m pytest tests/ -v
```

## 📁 Project Structure

```
urban-zones/
├── magentic-ui/           # Main Magentic-UI repository
│   ├── src/               # Python source code
│   ├── frontend/          # Gatsby frontend
│   ├── tests/             # Test suite
│   ├── docker/            # Docker configurations
│   └── .venv/             # Python virtual environment
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## 🔧 Technical Details

- **Backend**: FastAPI with SQLite database
- **Frontend**: Gatsby static site generator
- **Agents**: AutoGen multi-agent framework
- **Browser Automation**: Playwright in Docker containers
- **Environment**: Isolated Python virtual environment

## 🌟 Features

- Human-centered web agent interface
- Multi-agent collaboration system
- Web browsing and automation capabilities
- Code generation and execution
- Session management and persistence
- Real-time agent communication

## 📝 Notes

- This is a research prototype from Microsoft Research
- Requires OpenAI API key for full functionality
- Docker containers are automatically managed
- All dependencies are isolated in virtual environments

## 🔗 Original Repository

Based on: https://github.com/microsoft/magentic-ui

---

**Status**: ✅ Fully operational and ready for use!
