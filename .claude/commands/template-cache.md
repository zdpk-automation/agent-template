---
allowed-tools: Bash, LS
description: Show template cache information and manage cache
---

# Template Cache Management

Show information about the template cache and manage cached templates.

## Usage
```
/template-cache [action]
```

## Actions
- `info` (default): Show cache information
- `clear`: Clear the cache
- `update`: Force update cache

## What this command does:
1. Shows cache location and size
2. Displays last update time
3. Lists cached templates
4. Provides cache management options

```bash
# Parse action
ACTION="${ARGUMENTS:-info}"

# Cache directory
CACHE_DIR="$HOME/.agent-template-cache"

case $ACTION in
  "info"|"")
    echo "📦 Template Cache Information"
    echo "=============================="
    echo ""
    
    if [ -d "$CACHE_DIR" ]; then
      echo "📁 Cache Location: $CACHE_DIR"
      
      # Calculate cache size
      if command -v du >/dev/null 2>&1; then
        cache_size=$(du -sh "$CACHE_DIR" 2>/dev/null | cut -f1)
        echo "💾 Cache Size: $cache_size"
      fi
      
      # Show last update
      if [ -d "$CACHE_DIR/repo" ]; then
        if [ -d "$CACHE_DIR/repo/.git" ]; then
          last_update=$(git -C "$CACHE_DIR/repo" log -1 --format=%cd --date=short 2>/dev/null)
          echo "🕒 Last Update: ${last_update:-Unknown}"
          
          # Show current branch/commit
          current_commit=$(git -C "$CACHE_DIR/repo" rev-parse --short HEAD 2>/dev/null)
          echo "🔗 Current Commit: ${current_commit:-Unknown}"
        fi
        
        # List cached templates
        echo ""
        echo "📋 Cached Templates:"
        if [ -d "$CACHE_DIR/repo/templates" ]; then
          for template_dir in "$CACHE_DIR/repo/templates"/*; do
            if [ -d "$template_dir" ]; then
              template_name=$(basename "$template_dir")
              if [[ "$template_name" != .* ]]; then
                file_count=$(find "$template_dir" -type f | wc -l)
                echo "  • $template_name ($file_count files)"
              fi
            fi
          done
        else
          echo "  ❌ No templates found in cache"
        fi
      else
        echo "❌ Cache repository not found"
      fi
      
      echo ""
      echo "🔄 Cache Actions:"
      echo "  /template-cache update  - Force update cache"
      echo "  /template-cache clear   - Clear cache"
      
    else
      echo "❌ Cache directory not found: $CACHE_DIR"
      echo "💡 Cache will be created automatically when you first use templates"
    fi
    ;;
    
  "clear")
    echo "🗑️  Clearing template cache..."
    
    if [ -d "$CACHE_DIR" ]; then
      rm -rf "$CACHE_DIR"
      echo "✅ Cache cleared successfully"
      echo "💡 Cache will be recreated automatically when needed"
    else
      echo "ℹ️  Cache directory doesn't exist, nothing to clear"
    fi
    ;;
    
  "update")
    echo "🔄 Updating template cache..."
    
    # Create cache directory if it doesn't exist
    mkdir -p "$CACHE_DIR"
    
    # Repository URL
    REPO_URL="https://github.com/zdpk-automation/agent-template.git"
    
    if [ -d "$CACHE_DIR/repo" ]; then
      echo "📥 Pulling latest changes..."
      git -C "$CACHE_DIR/repo" pull origin main
      if [ $? -eq 0 ]; then
        echo "✅ Cache updated successfully"
      else
        echo "❌ Failed to update cache"
        echo "🔄 Trying fresh clone..."
        rm -rf "$CACHE_DIR/repo"
        git clone "$REPO_URL" "$CACHE_DIR/repo"
        if [ $? -eq 0 ]; then
          echo "✅ Cache recreated successfully"
        else
          echo "❌ Failed to clone repository"
        fi
      fi
    else
      echo "📥 Cloning repository..."
      git clone "$REPO_URL" "$CACHE_DIR/repo"
      if [ $? -eq 0 ]; then
        echo "✅ Cache initialized successfully"
      else
        echo "❌ Failed to initialize cache"
      fi
    fi
    
    # Show updated cache info
    echo ""
    echo "📊 Updated Cache Information:"
    /template-cache info
    ;;
    
  *)
    echo "❌ Invalid action: $ACTION"
    echo "Available actions: info, clear, update"
    exit 1
    ;;
esac
```