#!/bin/bash

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default values
PROJECT_TYPE="web"
TOOLS=()
FORCE=false

# Help function
show_help() {
    cat << EOF
Agent Template Initializer

Usage: $0 [OPTIONS]

Options:
    -t, --type TYPE         Project type (web, mobile, data) [default: web]
    -T, --tools TOOLS       Comma-separated list of tools (claude,gemini,opencode) [default: all]
    -f, --force            Force overwrite existing configurations
    -h, --help             Show this help message

Examples:
    $0 --type web --tools claude,gemini
    $0 --type data --tools opencode --force
EOF
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -t|--type)
            PROJECT_TYPE="$2"
            shift 2
            ;;
        -T|--tools)
            IFS=',' read -ra TOOLS <<< "$2"
            shift 2
            ;;
        -f|--force)
            FORCE=true
            shift
            ;;
        -h|--help)
            show_help
            exit 0
            ;;
        *)
            echo -e "${RED}Unknown option: $1${NC}"
            show_help
            exit 1
            ;;
    esac
done

# If no tools specified, use all
if [ ${#TOOLS[@]} -eq 0 ]; then
    TOOLS=("claude" "gemini" "opencode")
fi

echo -e "${BLUE}🤖 Agent Template Initializer${NC}"
echo -e "${BLUE}================================${NC}"
echo ""

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo -e "${YELLOW}⚠️  Not in a git repository. Consider running 'git init' first.${NC}"
    echo ""
fi

# Create necessary directories
echo -e "${GREEN}📁 Creating directories...${NC}"
mkdir -p .agent/{configs,scripts,docs}

# Function to setup Claude
setup_claude() {
    echo -e "${GREEN}🔧 Setting up Claude Code...${NC}"
    
    # Copy config files
    if [ ! -f ".agent/configs/claude-config.json" ] || [ "$FORCE" = true ]; then
        curl -sSL "https://raw.githubusercontent.com/zdpk-automation/agent-template/main/configs/claude/config.json" > .agent/configs/claude-config.json
        echo "  ✓ Claude config created"
    else
        echo -e "${YELLOW}  ⚠️  Claude config exists (use --force to overwrite)${NC}"
    fi
    
    if [ ! -f "AGENTS.md" ] || [ "$FORCE" = true ]; then
        curl -sSL "https://raw.githubusercontent.com/zdpk-automation/agent-template/main/configs/claude/AGENTS.md" > AGENTS.md
        echo "  ✓ AGENTS.md created"
    else
        echo -e "${YELLOW}  ⚠️  AGENTS.md exists (use --force to overwrite)${NC}"
    fi
}

# Function to setup Gemini
setup_gemini() {
    echo -e "${GREEN}🔧 Setting up Gemini CLI...${NC}"
    
    if [ ! -f ".agent/configs/gemini-config.yaml" ] || [ "$FORCE" = true ]; then
        curl -sSL "https://raw.githubusercontent.com/zdpk-automation/agent-template/main/configs/gemini/config.yaml" > .agent/configs/gemini-config.yaml
        echo "  ✓ Gemini config created"
    else
        echo -e "${YELLOW}  ⚠️  Gemini config exists (use --force to overwrite)${NC}"
    fi
}

# Function to setup OpenCode
setup_opencode() {
    echo -e "${GREEN}🔧 Setting up OpenCode...${NC}"
    
    if [ ! -f ".agent/configs/opencode-config.toml" ] || [ "$FORCE" = true ]; then
        curl -sSL "https://raw.githubusercontent.com/zdpk-automation/agent-template/main/configs/opencode/config.toml" > .agent/configs/opencode-config.toml
        echo "  ✓ OpenCode config created"
    else
        echo -e "${YELLOW}  ⚠️  OpenCode config exists (use --force to overwrite)${NC}"
    fi
}

# Setup each requested tool
for tool in "${TOOLS[@]}"; do
    case $tool in
        claude)
            setup_claude
            ;;
        gemini)
            setup_gemini
            ;;
        opencode)
            setup_opencode
            ;;
        *)
            echo -e "${RED}❌ Unknown tool: $tool${NC}"
            ;;
    esac
done

# Create environment template
if [ ! -f ".env.example" ] || [ "$FORCE" = true ]; then
    echo -e "${GREEN}📝 Creating environment template...${NC}"
    cat > .env.example << EOF
# AI Tool API Keys
ANTHROPIC_API_KEY=your_claude_api_key_here
GOOGLE_API_KEY=your_gemini_api_key_here
OPENCODE_API_KEY=your_opencode_api_key_here

# Project Configuration
PROJECT_TYPE=$PROJECT_TYPE
TOOLS=${TOOLS[*]}
EOF
    echo "  ✓ .env.example created"
fi

# Add to .gitignore
if [ -f ".gitignore" ]; then
    if ! grep -q ".agent/configs" .gitignore; then
        echo "" >> .gitignore
        echo "# Agent configurations with secrets" >> .gitignore
        echo ".agent/configs/*-config.*" >> .gitignore
        echo ".env" >> .gitignore
        echo "  ✓ Updated .gitignore"
    fi
else
    cat > .gitignore << EOF
# Agent configurations with secrets
.agent/configs/*-config.*
.env

# Dependencies
node_modules/
EOF
    echo "  ✓ Created .gitignore"
fi

echo ""
echo -e "${GREEN}✅ Setup complete!${NC}"
echo ""
echo -e "${BLUE}Next steps:${NC}"
echo "1. Copy .env.example to .env and add your API keys"
echo "2. Customize the configuration files in .agent/configs/"
echo "3. Start using your AI tools!"
echo ""
echo -e "${BLUE}Configured tools:${NC} ${TOOLS[*]}"
echo -e "${BLUE}Project type:${NC} $PROJECT_TYPE"