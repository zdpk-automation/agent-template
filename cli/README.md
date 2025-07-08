# Agent CLI

Simple bash-based template manager for AI-powered development projects.

## Installation

### Quick Install (Recommended)
```bash
curl -sSL https://github.com/zdpk-automation/agent-template/releases/latest/download/install.sh | bash
```

### Manual Install
```bash
# Download the CLI script
curl -L https://github.com/zdpk-automation/agent-template/releases/latest/download/agent-cli-1.0.0-linux.tar.gz | tar xz

# Make it executable and move to PATH
chmod +x agent
sudo mv agent /usr/local/bin/
```

## Usage

### Initialize Projects
```bash
# Frontend project (React + TypeScript)
agent init --frontend

# Backend project (Node.js + Express + TypeScript)  
agent init --backend

# Mobile project (React Native)
agent init --mobile

# Fullstack project
agent init --fullstack
```

### Upgrade Templates
```bash
# Upgrade frontend template to latest version
agent upgrade --frontend

# Upgrade backend template to latest version
agent upgrade --backend
```

### List Available Templates
```bash
agent list
```

## Features

- 🚀 **Simple**: Just a bash script, no complex dependencies
- 📦 **Template Management**: Download and manage project templates
- 🔄 **Version Control**: Each template has its own version
- 🤖 **AI Integration**: Includes AI agent configuration (separated from project code)
- ⚡ **Fast**: Direct download from GitHub releases

## Template Structure

When you run `agent init --frontend`, you get:

```
your-project/
├── src/                    # Project source code
│   ├── App.tsx
│   └── ...
├── package.json           # Project dependencies
├── tsconfig.json          # TypeScript config
├── .agent/                # AI agent configuration (isolated)
│   ├── configs/
│   │   └── claude-config.json
│   └── ...
├── AGENTS.md              # AI usage guidelines
└── ...
```

## How It Works

1. **Templates**: Stored in `templates/` directory of this repo
2. **Versions**: Managed in `config.yaml` 
3. **Downloads**: CLI downloads specific version from GitHub releases
4. **Separation**: AI agent config goes to `.agent/` directory, project code stays clean

## Version Management

Templates are versioned independently:

```yaml
# config.yaml
templates:
  frontend:
    version: "v1.2.0"
  backend:
    version: "v1.1.0"
```

When you upgrade, only the specified template gets updated.

## Development

The CLI is a single bash script (`cli/agent`) with no external dependencies except:
- `curl` or `wget` for downloads
- `tar` for extraction
- Standard Unix tools (`grep`, `sed`, etc.)

## Contributing

1. Add/modify templates in `templates/` directory
2. Update version in `config.yaml`
3. Create a git tag: `git tag v1.x.x && git push origin v1.x.x`
4. GitHub Actions will create the release automatically

## License

MIT