#!/bin/bash

# UnderratedVision Startup Script
# This script properly loads environment variables and starts the application

set -e

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Load environment variables from .env file
if [ -f "$SCRIPT_DIR/.env" ]; then
    echo "📦 Loading environment variables from .env..."
    export $(cat "$SCRIPT_DIR/.env" | grep -v '^#' | grep -v '^$' | xargs)
else
    echo "⚠️  Warning: .env file not found at $SCRIPT_DIR/.env"
    echo "Please create a .env file with your OPENAI_API_KEY"
    exit 1
fi

# Verify API key is set
if [ -z "$OPENAI_API_KEY" ]; then
    echo "❌ Error: OPENAI_API_KEY is not set in .env file"
    exit 1
fi

echo "✅ API Key loaded successfully"
echo "🚀 Starting UnderratedVision..."

# Navigate to magentic-ui directory
cd "$SCRIPT_DIR/magentic-ui"

# Activate virtual environment
if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
else
    echo "❌ Error: Virtual environment not found at .venv/bin/activate"
    echo "Please run: python3 -m venv .venv && source .venv/bin/activate && pip install magentic-ui --upgrade"
    exit 1
fi

# Start the application
echo "🌐 Launching Magentic-UI on http://127.0.0.1:8081"
uv run magentic-ui --port 8081

