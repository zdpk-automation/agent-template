#!/bin/bash

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default values
TEMPLATE_TYPE="default"
FORCE=false

# Help function
show_help() {
    cat << EOF
PR Template Setup Script

Usage: $0 [OPTIONS]

Options:
    -t, --type TYPE         Template type (default, feature, bugfix, refactor, hotfix, docs) [default: default]
    -f, --force            Force overwrite existing template
    -h, --help             Show this help message

Examples:
    $0 --type feature
    $0 --type hotfix --force
    $0 --type default
EOF
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -t|--type)
            TEMPLATE_TYPE="$2"
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

echo -e "${BLUE}📝 PR Template Setup${NC}"
echo -e "${BLUE}===================${NC}"
echo ""

# Create .github directory if it doesn't exist
if [ ! -d ".github" ]; then
    echo -e "${GREEN}📁 Creating .github directory...${NC}"
    mkdir -p .github
fi

# Function to setup default template
setup_default_template() {
    echo -e "${GREEN}🔧 Setting up default PR template...${NC}"
    
    if [ ! -f ".github/pull_request_template.md" ] || [ "$FORCE" = true ]; then
        curl -sSL "https://raw.githubusercontent.com/zdpk-automation/agent-template/main/.github/pull_request_template.md" > .github/pull_request_template.md
        echo "  ✓ Default PR template created"
    else
        echo -e "${YELLOW}  ⚠️  Default PR template exists (use --force to overwrite)${NC}"
    fi
}

# Function to setup specific template
setup_specific_template() {
    local template_name="$1"
    echo -e "${GREEN}🔧 Setting up $template_name PR template...${NC}"
    
    if [ ! -f ".github/PULL_REQUEST_TEMPLATE/$template_name.md" ] || [ "$FORCE" = true ]; then
        mkdir -p .github/PULL_REQUEST_TEMPLATE
        curl -sSL "https://raw.githubusercontent.com/zdpk-automation/agent-template/main/templates/pr-templates/$template_name.md" > ".github/PULL_REQUEST_TEMPLATE/$template_name.md"
        echo "  ✓ $template_name PR template created"
    else
        echo -e "${YELLOW}  ⚠️  $template_name PR template exists (use --force to overwrite)${NC}"
    fi
}

# Setup templates based on type
case $TEMPLATE_TYPE in
    default)
        setup_default_template
        ;;
    feature|bugfix|refactor|hotfix|docs)
        setup_specific_template "$TEMPLATE_TYPE"
        ;;
    all)
        setup_default_template
        mkdir -p .github/PULL_REQUEST_TEMPLATE
        for template in feature bugfix refactor hotfix docs; do
            setup_specific_template "$template"
        done
        ;;
    *)
        echo -e "${RED}❌ Unknown template type: $TEMPLATE_TYPE${NC}"
        echo "Available types: default, feature, bugfix, refactor, hotfix, docs, all"
        exit 1
        ;;
esac

# Add to .gitignore if needed
if [ -f ".gitignore" ]; then
    if ! grep -q ".github/" .gitignore; then
        echo "" >> .gitignore
        echo "# GitHub templates are tracked" >> .gitignore
        echo "# .github/" >> .gitignore
    fi
fi

echo ""
echo -e "${GREEN}✅ PR template setup complete!${NC}"
echo ""
echo -e "${BLUE}Usage:${NC}"
if [ "$TEMPLATE_TYPE" = "default" ]; then
    echo "• Default template will be used for all PRs"
elif [ "$TEMPLATE_TYPE" = "all" ]; then
    echo "• Use ?template=feature.md for feature PRs"
    echo "• Use ?template=bugfix.md for bugfix PRs"
    echo "• Use ?template=refactor.md for refactor PRs"
    echo "• Use ?template=hotfix.md for hotfix PRs"
    echo "• Use ?template=docs.md for documentation PRs"
else
    echo "• Use ?template=$TEMPLATE_TYPE.md when creating PRs"
fi
echo ""
echo -e "${BLUE}Example:${NC}"
echo "https://github.com/your-org/your-repo/compare/main...feature-branch?template=$TEMPLATE_TYPE.md"