# 🚀 Magentic-UI Complete Setup Guide

## 📋 Overview

This repository contains a fully functional installation of **Microsoft Magentic-UI** - a human-centered interface powered by multi-agent systems for web automation.

## ✅ What's Included

- **Original Microsoft Magentic-UI v0.1.2** (latest official release)
- **Complete Gatsby Frontend** built from source
- **Multi-Agent System** with AutoGen framework
- **Web Automation** with Playwright + Docker
- **OpenAI Integration** ready for configuration
- **Session Management** and file processing
- **Real-time Updates** via WebSocket

## 🛠 Installation

### Prerequisites

- **Python 3.10+** (tested with 3.11.12)
- **Docker** (for web automation)
- **Node.js & Yarn** (for frontend development)
- **OpenAI API Key** (for AI functionality)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/ghost-codez/urban-zones.git
   cd urban-zones
   ```

2. **Set up Python environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install magentic-ui --upgrade
   ```

3. **Install Playwright browsers**
   ```bash
   playwright install
   ```

4. **Configure API key (One-time setup)**
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key
   # The API key will be automatically loaded from .env file
   ```

5. **Start the application**
   ```bash
   # Option 1: Use the convenient startup script
   ./start-magentic-ui.sh

   # Option 2: Manual start (loads .env automatically)
   source .venv/bin/activate && magentic-ui --port 8081
   ```

6. **Access the interface**
   - Main Application: http://127.0.0.1:8081
   - API Documentation: http://127.0.0.1:8081/docs

## 🔧 Development Setup

### Frontend Development

```bash
cd magentic-ui/frontend
yarn install
yarn start  # Development server on port 8000
```

### Building Frontend

```bash
cd magentic-ui/frontend
yarn build
# Copy built files to backend
cp -r public/* ../src/magentic_ui/backend/web/ui/
```

## 🔒 Security

- **API keys are excluded** from the repository
- **Environment variables** are properly configured
- **Sensitive data** is protected via `.gitignore`
- **Use `.env.example`** as a template for configuration

## 🚀 Features

### Multi-Agent System
- Create and manage AI agent sessions
- Collaborative workflows between multiple agents
- Real-time agent communication

### Web Automation
- Browser automation with Playwright
- Form filling and web interaction
- Screenshot and data extraction

### File Processing
- Upload and analyze documents
- Code generation and modification
- Data extraction and transformation

## 📚 Documentation

- **Official Repository**: https://github.com/microsoft/magentic-ui
- **API Reference**: Available at `/docs` endpoint
- **Troubleshooting**: See `magentic-ui/TROUBLESHOOTING.md`

## 🎯 Ready for Production

The installation is complete and tested. All components are working:

- ✅ Backend API (FastAPI)
- ✅ Frontend Interface (Gatsby/React)
- ✅ Database (SQLite with migrations)
- ✅ Docker Integration
- ✅ OpenAI Integration
- ✅ Multi-Agent Framework
- ✅ Web Automation

## 🤝 Contributing

This is a working installation of the official Microsoft Magentic-UI. For contributions to the core project, please visit the [official repository](https://github.com/microsoft/magentic-ui).

## 📄 License

This project follows the same license as the original Microsoft Magentic-UI project.
