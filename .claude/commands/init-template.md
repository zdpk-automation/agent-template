---
allowed-tools: Bash, Read, Write, LS, Glob
description: Initialize a new project from a template
---

# Initialize Template

Initialize a new project from a template. This command downloads the latest template from the repository and sets up the project structure.

## Usage
```
/init-template [template-type] [project-name]
```

## Available Templates
- `frontend`: React/Next.js frontend template
- `backend`: Node.js/Express backend template  
- `mobile`: React Native mobile template
- `fullstack`: Full-stack application template

## What this command does:
1. Downloads the latest template from GitHub repository
2. Extracts template files to the specified project directory
3. Sets up AI agent configuration in `.agent/` directory
4. Initializes project structure with proper naming

## Template Arguments
- `$ARGUMENTS`: Will be parsed as `[template-type] [project-name]`
- If no project name provided, uses current directory name

## Example Usage
```
/init-template frontend my-react-app
/init-template backend api-server
/init-template mobile my-mobile-app
```

Please provide the template type and project name as arguments.
Arguments: $ARGUMENTS

Let me initialize the template for you:

```bash
# Parse arguments
ARGS=($ARGUMENTS)
TEMPLATE_TYPE=${ARGS[0]}
PROJECT_NAME=${ARGS[1]:-$(basename $(pwd))}

# Validate template type
case $TEMPLATE_TYPE in
  frontend|backend|mobile|fullstack)
    echo "✅ Valid template type: $TEMPLATE_TYPE"
    ;;
  *)
    echo "❌ Invalid template type. Available: frontend, backend, mobile, fullstack"
    exit 1
    ;;
esac

# Repository configuration
REPO_URL="https://github.com/zdpk-automation/agent-template"
TEMP_DIR=$(mktemp -d)

# Download and extract template
echo "📥 Downloading template from $REPO_URL..."
curl -sSL "$REPO_URL/archive/refs/heads/main.tar.gz" | tar -xz -C "$TEMP_DIR" --strip-components=1

# Check if template exists
TEMPLATE_SOURCE="$TEMP_DIR/templates/$TEMPLATE_TYPE"
if [ ! -d "$TEMPLATE_SOURCE" ]; then
  echo "❌ Template '$TEMPLATE_TYPE' not found in repository"
  rm -rf "$TEMP_DIR"
  exit 1
fi

# Create project directory if it doesn't exist
mkdir -p "$PROJECT_NAME"

# Copy template files
echo "📁 Copying template files to $PROJECT_NAME..."
find "$TEMPLATE_SOURCE" -type f | while read -r file; do
  relative_path="${file#$TEMPLATE_SOURCE/}"
  
  # Skip .agent directory files for now
  if [[ "$relative_path" == .agent/* ]]; then
    continue
  fi
  
  target_file="$PROJECT_NAME/$relative_path"
  target_dir=$(dirname "$target_file")
  
  mkdir -p "$target_dir"
  cp "$file" "$target_file"
done

# Copy AI agent configuration
if [ -d "$TEMPLATE_SOURCE/.agent" ]; then
  echo "🤖 Setting up AI agent configuration..."
  mkdir -p "$PROJECT_NAME/.agent"
  cp -r "$TEMPLATE_SOURCE/.agent"/* "$PROJECT_NAME/.agent/"
fi

# Cleanup
rm -rf "$TEMP_DIR"

echo "✅ Template '$TEMPLATE_TYPE' initialized successfully in '$PROJECT_NAME'!"
echo "📂 Project structure created with AI agent configuration"
echo "🚀 You can now start working on your project"
```