#!/bin/bash

# UnderratedVision Repository Setup Script
# This script helps set up the new GitHub repository

echo "🚀 UnderratedVision Repository Setup"
echo "===================================="

# Check if we're in the right directory
if [ ! -f "README.md" ] || [ ! -d "extensions" ]; then
    echo "❌ Error: Please run this script from the UnderratedVision root directory"
    exit 1
fi

echo "📋 Pre-setup checklist:"
echo "1. Create new repository 'UnderratedVision' on GitHub"
echo "2. Set repository description: 'Multi-Domain AI Automation Platform'"
echo "3. Add topics: ai-automation, multi-agent-systems, business-intelligence"
echo "4. Enable Issues, Projects, Wiki, Discussions, Actions"
echo ""
read -p "Have you completed the above steps? (y/n): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Please complete the setup on GitHub first, then run this script again."
    exit 1
fi

# Get the GitHub username
read -p "Enter your GitHub username: " GITHUB_USERNAME

# Backup current git config
echo "📦 Backing up current git configuration..."
git remote -v > .git_remotes_backup.txt

# Remove current origin (if exists)
echo "🔄 Updating git remotes..."
git remote remove origin 2>/dev/null || true

# Add new origin
NEW_REPO_URL="https://github.com/${GITHUB_USERNAME}/UnderratedVision.git"
git remote add origin $NEW_REPO_URL

echo "✅ New origin set to: $NEW_REPO_URL"

# Create and switch to main branch
echo "🌿 Setting up main branch..."
git checkout -b main 2>/dev/null || git checkout main

# Stage all files
echo "📁 Staging files for commit..."
git add .

# Create initial commit
echo "💾 Creating initial commit..."
git commit -m "🚀 Initial UnderratedVision v2.0.0 release

- Multi-domain AI automation platform
- Specialized agents for business, technical, creative, healthcare domains
- Cross-domain workflow orchestration
- Enterprise-ready architecture with comprehensive documentation
- Built on Microsoft Magentic-UI v0.1.2

Features:
✅ Real estate analysis and investment evaluation
✅ Construction project coordination and management
✅ Marketing strategy and campaign optimization
✅ Medical research and healthcare compliance
✅ Multi-domain workflow orchestration
✅ Stakeholder demonstrations with ROI metrics

Transforming industries through intelligent automation."

# Create version tag
echo "🏷️ Creating version tag..."
git tag -a "underratedvision-v2.0.0-magentic-ui-v0.1.2" -m "UnderratedVision v2.0.0 - Multi-Domain AI Automation Platform

Initial release featuring:
- Multi-domain agent architecture
- Cross-industry workflow orchestration  
- Enterprise documentation and demonstrations
- Built on Microsoft Magentic-UI v0.1.2"

# Push to GitHub
echo "⬆️ Pushing to GitHub..."
echo "Repository URL: $NEW_REPO_URL"
read -p "Push to GitHub now? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    git push -u origin main
    git push origin --tags
    echo "✅ Successfully pushed to GitHub!"
    echo ""
    echo "🎉 Repository setup complete!"
    echo "📍 Your repository: https://github.com/${GITHUB_USERNAME}/UnderratedVision"
    echo ""
    echo "Next steps:"
    echo "1. Update repository description and topics on GitHub"
    echo "2. Enable branch protection rules"
    echo "3. Set up GitHub Actions workflows"
    echo "4. Create first release from the tag"
    echo "5. Share your multi-domain AI platform with the world!"
else
    echo "⏸️ Push skipped. You can push manually later with:"
    echo "   git push -u origin main"
    echo "   git push origin --tags"
fi

echo ""
echo "🔗 Quick links to set up:"
echo "- Repository settings: https://github.com/${GITHUB_USERNAME}/UnderratedVision/settings"
echo "- Create release: https://github.com/${GITHUB_USERNAME}/UnderratedVision/releases/new"
echo "- Enable discussions: https://github.com/${GITHUB_USERNAME}/UnderratedVision/settings#discussions"

echo ""
echo "🎯 UnderratedVision is ready to transform industries!"
