---
allowed-tools: Bash, WebFetch
description: List available templates and their versions
---

# List Available Templates

Show all available templates from the repository with their descriptions and versions.

## Usage
```
/list-templates
```

## What this command does:
1. Fetches the latest repository information
2. Lists all available templates in the `templates/` directory
3. Shows template descriptions and available versions
4. Provides usage examples

```bash
# Repository configuration
REPO_URL="https://github.com/zdpk-automation/agent-template"
API_URL="https://api.github.com/repos/zdpk-automation/agent-template"

echo "📋 Available Templates from $REPO_URL"
echo "=================================================="
echo ""

# Get repository contents
TEMP_DIR=$(mktemp -d)
curl -sSL "$REPO_URL/archive/refs/heads/main.tar.gz" | tar -xz -C "$TEMP_DIR" --strip-components=1

TEMPLATES_DIR="$TEMP_DIR/templates"

if [ ! -d "$TEMPLATES_DIR" ]; then
  echo "❌ Templates directory not found in repository"
  rm -rf "$TEMP_DIR"
  exit 1
fi

# List templates
for template_dir in "$TEMPLATES_DIR"/*; do
  if [ -d "$template_dir" ]; then
    template_name=$(basename "$template_dir")
    
    # Skip hidden directories
    if [[ "$template_name" == .* ]]; then
      continue
    fi
    
    echo "🎯 $template_name"
    
    # Check for README or description
    if [ -f "$template_dir/README.md" ]; then
      # Extract first line of README as description
      description=$(head -n 1 "$template_dir/README.md" | sed 's/^#*\s*//')
      echo "   📝 $description"
    elif [ -f "$template_dir/package.json" ]; then
      # Extract description from package.json
      description=$(grep -o '"description":\s*"[^"]*"' "$template_dir/package.json" | sed 's/"description":\s*"\([^"]*\)"/\1/')
      if [ -n "$description" ]; then
        echo "   📝 $description"
      fi
    fi
    
    # List key files
    echo "   📁 Key files:"
    find "$template_dir" -maxdepth 2 -type f -name "*.json" -o -name "*.md" -o -name "*.ts" -o -name "*.js" | head -5 | while read -r file; do
      rel_path="${file#$template_dir/}"
      echo "      • $rel_path"
    done
    
    echo ""
  fi
done

# Get available versions (Git tags)
echo "🏷️  Available Versions:"
echo "----------------------"
git ls-remote --tags "$REPO_URL" | grep -o 'refs/tags/[^{}]*' | sed 's/refs\/tags\///' | sort -V | tail -10 | while read -r tag; do
  echo "   • $tag"
done

if ! git ls-remote --tags "$REPO_URL" | grep -q 'refs/tags/'; then
  echo "   • main (latest)"
fi

echo ""
echo "💡 Usage Examples:"
echo "   /init-template frontend my-react-app"
echo "   /init-template backend api-server"
echo "   /init-template mobile my-mobile-app"
echo "   /init-template fullstack my-fullstack-app"
echo ""
echo "🔄 To update templates cache: /update-template-cache"

# Cleanup
rm -rf "$TEMP_DIR"
```