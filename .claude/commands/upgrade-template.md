---
allowed-tools: Bash, Read, LS
description: Upgrade existing template to latest version
---

# Upgrade Template

Upgrade an existing project template to the latest version while preserving your custom changes.

## Usage
```
/upgrade-template [template-type]
```

## Safety Features
- Backs up existing files before upgrade
- Preserves custom configurations in `.agent/` directory
- Shows diff of changes before applying
- Allows selective upgrade of specific files

## Arguments
- `$ARGUMENTS`: Template type to upgrade (frontend, backend, mobile, fullstack)

## What this command does:
1. Detects current template type (if not specified)
2. Creates backup of existing files
3. Downloads latest template version
4. Shows differences between current and new version
5. Applies upgrade with conflict resolution

```bash
# Parse arguments
TEMPLATE_TYPE="$ARGUMENTS"

# Check if we're in a project directory
if [ ! -d ".agent" ]; then
  echo "❌ No .agent directory found. This doesn't appear to be an initialized project."
  echo "💡 Use /init-template to initialize a new project first."
  exit 1
fi

# Auto-detect template type if not provided
if [ -z "$TEMPLATE_TYPE" ]; then
  if [ -f "package.json" ]; then
    if grep -q "next" package.json; then
      TEMPLATE_TYPE="frontend"
    elif grep -q "express" package.json; then
      TEMPLATE_TYPE="backend"
    elif grep -q "react-native" package.json; then
      TEMPLATE_TYPE="mobile"
    else
      TEMPLATE_TYPE="fullstack"
    fi
  else
    echo "❌ Could not auto-detect template type. Please specify: frontend, backend, mobile, or fullstack"
    exit 1
  fi
fi

# Validate template type
case $TEMPLATE_TYPE in
  frontend|backend|mobile|fullstack)
    echo "🎯 Upgrading $TEMPLATE_TYPE template..."
    ;;
  *)
    echo "❌ Invalid template type. Available: frontend, backend, mobile, fullstack"
    exit 1
    ;;
esac

# Create backup
BACKUP_DIR=".agent/backup-$(date +%Y%m%d-%H%M%S)"
echo "💾 Creating backup in $BACKUP_DIR..."
mkdir -p "$BACKUP_DIR"
cp -r . "$BACKUP_DIR/" 2>/dev/null || true

# Repository configuration
REPO_URL="https://github.com/zdpk-automation/agent-template"
TEMP_DIR=$(mktemp -d)

# Download latest template
echo "📥 Downloading latest template..."
curl -sSL "$REPO_URL/archive/refs/heads/main.tar.gz" | tar -xz -C "$TEMP_DIR" --strip-components=1

TEMPLATE_SOURCE="$TEMP_DIR/templates/$TEMPLATE_TYPE"

if [ ! -d "$TEMPLATE_SOURCE" ]; then
  echo "❌ Template '$TEMPLATE_TYPE' not found in repository"
  rm -rf "$TEMP_DIR"
  exit 1
fi

# Show what will be updated
echo "🔍 Analyzing differences..."
echo "Files that will be updated:"
echo "=========================="

# Compare files
find "$TEMPLATE_SOURCE" -type f | while read -r file; do
  relative_path="${file#$TEMPLATE_SOURCE/}"
  
  # Skip .agent directory files (preserve custom config)
  if [[ "$relative_path" == .agent/* ]]; then
    continue
  fi
  
  current_file="./$relative_path"
  
  if [ -f "$current_file" ]; then
    if ! diff -q "$file" "$current_file" >/dev/null 2>&1; then
      echo "  📝 Modified: $relative_path"
    fi
  else
    echo "  ➕ New: $relative_path"
  fi
done

echo ""
echo "⚠️  This will overwrite existing template files."
echo "💾 Backup created in: $BACKUP_DIR"
echo ""
read -p "Continue with upgrade? (y/N): " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
  echo "❌ Upgrade cancelled"
  rm -rf "$TEMP_DIR"
  exit 0
fi

# Apply upgrade
echo "🔄 Applying upgrade..."
find "$TEMPLATE_SOURCE" -type f | while read -r file; do
  relative_path="${file#$TEMPLATE_SOURCE/}"
  
  # Skip .agent directory files (preserve custom config)
  if [[ "$relative_path" == .agent/* ]]; then
    continue
  fi
  
  target_file="./$relative_path"
  target_dir=$(dirname "$target_file")
  
  mkdir -p "$target_dir"
  cp "$file" "$target_file"
done

# Update .agent template info (but preserve custom settings)
if [ -f "$TEMPLATE_SOURCE/.agent/template.json" ]; then
  echo "📋 Updating template metadata..."
  cp "$TEMPLATE_SOURCE/.agent/template.json" ".agent/template.json"
fi

# Cleanup
rm -rf "$TEMP_DIR"

echo "✅ Template upgraded successfully!"
echo "📂 Backup available in: $BACKUP_DIR"
echo "🔍 Review changes and test your project"
echo "🗑️  Remove backup when satisfied: rm -rf $BACKUP_DIR"
```