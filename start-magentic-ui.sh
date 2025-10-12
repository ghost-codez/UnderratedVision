#!/bin/bash

# Magentic-UI Startup Script
# This script automatically loads your API key and starts the application

echo "🚀 Starting Magentic-UI..."

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "❌ .env file not found!"
    echo "📋 Please copy .env.example to .env and add your API key:"
    echo "   cp .env.example .env"
    echo "   # Then edit .env with your actual API key"
    exit 1
fi

# Load environment variables from .env file
export $(cat .env | grep -v '^#' | xargs)

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source .venv/bin/activate

# Start Magentic-UI
echo "🌐 Starting Magentic-UI on http://127.0.0.1:${PORT:-8081}"
echo "📖 API Documentation: http://127.0.0.1:${PORT:-8081}/docs"
echo "🛑 Press Ctrl+C to stop"
echo ""

magentic-ui --port ${PORT:-8081}
