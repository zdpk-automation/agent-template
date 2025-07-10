---
allowed-tools: Bash, Write, Read, LS
description: Interactive project initialization with language and framework selection
---

# Project Setup / 프로젝트 설정

Interactive project initialization with automatic environment detection and setup.

## Usage / 사용법
```
/setup
```

## What this command does / 이 명령어의 기능
1. Interactive language selection / 대화형 언어 선택
2. Framework selection based on language / 언어 기반 프레임워크 선택  
3. Automatic project structure generation / 자동 프로젝트 구조 생성
4. Configuration files setup / 설정 파일 생성
5. Git initialization / Git 초기화

```bash
#!/bin/bash

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m'

echo -e "${BLUE}🚀 Project Setup - Language & Framework Selection${NC}"
echo -e "${BLUE}===============================================${NC}"
echo ""

# Check if already in a project
if [ -f "package.json" ] || [ -f "Cargo.toml" ] || [ -f "requirements.txt" ] || [ -f "go.mod" ] || [ -f "pom.xml" ]; then
    echo -e "${YELLOW}⚠️  Warning: Existing project detected!${NC}"
    echo "Continue anyway? (y/N)"
    read -r response
    if [[ ! "$response" =~ ^[Yy]$ ]]; then
        echo "Setup cancelled."
        exit 0
    fi
    echo ""
fi

# Get project name
echo -e "${WHITE}📝 Project Name${NC}"
PROJECT_NAME=$(basename "$(pwd)")
echo -e "${CYAN}Enter project name (default: $PROJECT_NAME):${NC}"
read -r input_name
if [ -n "$input_name" ]; then
    PROJECT_NAME="$input_name"
fi
echo -e "${GREEN}✓ Project: $PROJECT_NAME${NC}"
echo ""

# Language selection
echo -e "${WHITE}🔤 Select Programming Language:${NC}"
echo -e "${CYAN}1.${NC} TypeScript/JavaScript"
echo -e "${CYAN}2.${NC} Rust" 
echo -e "${CYAN}3.${NC} Python"
echo -e "${CYAN}4.${NC} Go"
echo -e "${CYAN}5.${NC} Java"
echo ""
echo -e "${CYAN}Enter your choice (1-5):${NC}"
read -r lang_choice

case $lang_choice in
    1) LANGUAGE="typescript" ;;
    2) LANGUAGE="rust" ;;
    3) LANGUAGE="python" ;;
    4) LANGUAGE="go" ;;
    5) LANGUAGE="java" ;;
    *) 
        echo -e "${RED}❌ Invalid choice${NC}"
        exit 1
        ;;
esac

echo -e "${GREEN}✓ Language: $LANGUAGE${NC}"
echo ""

# Framework selection based on language
echo -e "${WHITE}🛠️  Select Framework:${NC}"
case $LANGUAGE in
    "typescript")
        echo -e "${CYAN}1.${NC} NestJS (Backend API)"
        echo -e "${CYAN}2.${NC} Express (Simple Backend)"
        echo -e "${CYAN}3.${NC} Next.js (Full-stack)"
        echo -e "${CYAN}4.${NC} React (Frontend)"
        echo -e "${CYAN}5.${NC} Vue.js (Frontend)"
        echo ""
        echo -e "${CYAN}Enter your choice (1-5):${NC}"
        read -r fw_choice
        case $fw_choice in
            1) FRAMEWORK="nestjs"; PROJECT_TYPE="backend" ;;
            2) FRAMEWORK="express"; PROJECT_TYPE="backend" ;;
            3) FRAMEWORK="nextjs"; PROJECT_TYPE="fullstack" ;;
            4) FRAMEWORK="react"; PROJECT_TYPE="frontend" ;;
            5) FRAMEWORK="vue"; PROJECT_TYPE="frontend" ;;
            *) echo -e "${RED}❌ Invalid choice${NC}"; exit 1 ;;
        esac
        ;;
    "rust")
        echo -e "${CYAN}1.${NC} Axum (Web Framework)"
        echo -e "${CYAN}2.${NC} Actix-web (Web Framework)"
        echo -e "${CYAN}3.${NC} Warp (Web Framework)"
        echo -e "${CYAN}4.${NC} Tauri (Desktop App)"
        echo ""
        echo -e "${CYAN}Enter your choice (1-4):${NC}"
        read -r fw_choice
        case $fw_choice in
            1) FRAMEWORK="axum"; PROJECT_TYPE="backend" ;;
            2) FRAMEWORK="actix"; PROJECT_TYPE="backend" ;;
            3) FRAMEWORK="warp"; PROJECT_TYPE="backend" ;;
            4) FRAMEWORK="tauri"; PROJECT_TYPE="desktop" ;;
            *) echo -e "${RED}❌ Invalid choice${NC}"; exit 1 ;;
        esac
        ;;
    "python")
        echo -e "${CYAN}1.${NC} FastAPI (Modern API)"
        echo -e "${CYAN}2.${NC} Django (Full Framework)"
        echo -e "${CYAN}3.${NC} Flask (Minimal Framework)"
        echo -e "${CYAN}4.${NC} Streamlit (Data Apps)"
        echo ""
        echo -e "${CYAN}Enter your choice (1-4):${NC}"
        read -r fw_choice
        case $fw_choice in
            1) FRAMEWORK="fastapi"; PROJECT_TYPE="backend" ;;
            2) FRAMEWORK="django"; PROJECT_TYPE="fullstack" ;;
            3) FRAMEWORK="flask"; PROJECT_TYPE="backend" ;;
            4) FRAMEWORK="streamlit"; PROJECT_TYPE="data" ;;
            *) echo -e "${RED}❌ Invalid choice${NC}"; exit 1 ;;
        esac
        ;;
    "go")
        echo -e "${CYAN}1.${NC} Gin (Web Framework)"
        echo -e "${CYAN}2.${NC} Echo (Web Framework)"
        echo -e "${CYAN}3.${NC} Fiber (Web Framework)"
        echo -e "${CYAN}4.${NC} Standard Library"
        echo ""
        echo -e "${CYAN}Enter your choice (1-4):${NC}"
        read -r fw_choice
        case $fw_choice in
            1) FRAMEWORK="gin"; PROJECT_TYPE="backend" ;;
            2) FRAMEWORK="echo"; PROJECT_TYPE="backend" ;;
            3) FRAMEWORK="fiber"; PROJECT_TYPE="backend" ;;
            4) FRAMEWORK="stdlib"; PROJECT_TYPE="backend" ;;
            *) echo -e "${RED}❌ Invalid choice${NC}"; exit 1 ;;
        esac
        ;;
    "java")
        echo -e "${CYAN}1.${NC} Spring Boot (Framework)"
        echo -e "${CYAN}2.${NC} Quarkus (Cloud Native)"
        echo -e "${CYAN}3.${NC} Micronaut (Microservices)"
        echo ""
        echo -e "${CYAN}Enter your choice (1-3):${NC}"
        read -r fw_choice
        case $fw_choice in
            1) FRAMEWORK="springboot"; PROJECT_TYPE="backend" ;;
            2) FRAMEWORK="quarkus"; PROJECT_TYPE="backend" ;;
            3) FRAMEWORK="micronaut"; PROJECT_TYPE="backend" ;;
            *) echo -e "${RED}❌ Invalid choice${NC}"; exit 1 ;;
        esac
        ;;
esac

STACK="$LANGUAGE-$FRAMEWORK"
echo -e "${GREEN}✓ Stack: $LANGUAGE + $FRAMEWORK ($PROJECT_TYPE)${NC}"
echo ""

# Auto-generate project based on detection
echo -e "${WHITE}⚙️  Auto-generating project structure...${NC}"

# Create base directories
mkdir -p .agent/{prd,docs}

# Language and framework specific setup
case $STACK in
    "typescript-nestjs")
        echo -e "${BLUE}🏗️  Setting up NestJS + TypeScript...${NC}"
        
        # Create directory structure
        mkdir -p src/{modules,common,config}
        mkdir -p src/modules/{auth,users,health}
        mkdir -p src/common/{decorators,filters,guards,interceptors,pipes}
        mkdir -p test/{unit,e2e}
        mkdir -p docs
        
        # Auto-generate package.json
        cat > package.json << EOF
{
  "name": "$PROJECT_NAME",
  "version": "0.1.0",
  "description": "NestJS TypeScript API",
  "scripts": {
    "build": "nest build",
    "start": "nest start",
    "start:dev": "nest start --watch",
    "start:prod": "node dist/main",
    "lint": "eslint \"{src,test}/**/*.ts\" --fix",
    "test": "jest",
    "test:watch": "jest --watch",
    "test:e2e": "jest --config ./test/jest-e2e.json"
  },
  "dependencies": {
    "@nestjs/common": "^10.0.0",
    "@nestjs/core": "^10.0.0",
    "@nestjs/platform-express": "^10.0.0",
    "@nestjs/config": "^3.0.0",
    "@nestjs/swagger": "^7.0.0",
    "reflect-metadata": "^0.1.13",
    "rxjs": "^7.8.1"
  },
  "devDependencies": {
    "@nestjs/cli": "^10.0.0",
    "@nestjs/testing": "^10.0.0",
    "@types/node": "^20.0.0",
    "@typescript-eslint/eslint-plugin": "^6.0.0",
    "@typescript-eslint/parser": "^6.0.0",
    "eslint": "^8.42.0",
    "jest": "^29.5.0",
    "typescript": "^5.1.3"
  }
}
EOF
        
        # Auto-generate main.ts
        cat > src/main.ts << EOF
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  await app.listen(3000);
  console.log('🚀 Application running on http://localhost:3000');
}
bootstrap();
EOF

        # Auto-generate app.module.ts
        cat > src/app.module.ts << EOF
import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { HealthModule } from './modules/health/health.module';

@Module({
  imports: [
    ConfigModule.forRoot({ isGlobal: true }),
    HealthModule,
  ],
})
export class AppModule {}
EOF

        # Auto-generate health module
        cat > src/modules/health/health.module.ts << EOF
import { Module } from '@nestjs/common';
import { HealthController } from './health.controller';

@Module({
  controllers: [HealthController],
})
export class HealthModule {}
EOF

        cat > src/modules/health/health.controller.ts << EOF
import { Controller, Get } from '@nestjs/common';

@Controller('health')
export class HealthController {
  @Get()
  check() {
    return {
      status: 'ok',
      timestamp: new Date().toISOString(),
      service: '$PROJECT_NAME',
    };
  }
}
EOF

        cat > tsconfig.json << EOF
{
  "compilerOptions": {
    "module": "commonjs",
    "declaration": true,
    "removeComments": true,
    "emitDecoratorMetadata": true,
    "experimentalDecorators": true,
    "allowSyntheticDefaultImports": true,
    "target": "ES2021",
    "sourceMap": true,
    "outDir": "./dist",
    "baseUrl": "./",
    "incremental": true,
    "skipLibCheck": true
  }
}
EOF

        cat > .gitignore << 'EOF'
node_modules/
dist/
.env
*.log
.DS_Store
EOF
        ;;
        
    "rust-axum")
        echo -e "${BLUE}🦀 Setting up Axum + Rust...${NC}"
        
        mkdir -p src/{handlers,models,services}
        mkdir -p tests
        
        cat > Cargo.toml << EOF
[package]
name = "$PROJECT_NAME"
version = "0.1.0"
edition = "2021"

[dependencies]
axum = "0.7"
tokio = { version = "1.0", features = ["full"] }
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
tower = "0.4"
tower-http = { version = "0.5", features = ["cors"] }
tracing = "0.1"
tracing-subscriber = "0.3"

[dev-dependencies]
hyper = { version = "1.0", features = ["full"] }
EOF

        cat > src/main.rs << EOF
use axum::{routing::get, Router, Json};
use serde::Serialize;
use std::net::SocketAddr;

#[derive(Serialize)]
struct HealthResponse {
    status: String,
    timestamp: String,
    service: String,
}

async fn health() -> Json<HealthResponse> {
    Json(HealthResponse {
        status: "ok".to_string(),
        timestamp: chrono::Utc::now().to_rfc3339(),
        service: "$PROJECT_NAME".to_string(),
    })
}

#[tokio::main]
async fn main() {
    tracing_subscriber::init();
    
    let app = Router::new().route("/health", get(health));
    
    let addr = SocketAddr::from(([127, 0, 0, 1], 3000));
    let listener = tokio::net::TcpListener::bind(addr).await.unwrap();
    
    println!("🚀 Server running on http://{}", addr);
    axum::serve(listener, app).await.unwrap();
}
EOF

        cat > .gitignore << 'EOF'
/target/
Cargo.lock
.env
*.log
.DS_Store
EOF
        ;;

    "python-fastapi")
        echo -e "${BLUE}🐍 Setting up FastAPI + Python...${NC}"
        
        mkdir -p app/{api,core,models,services}
        mkdir -p tests
        
        cat > requirements.txt << EOF
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0
python-dotenv==1.0.0
EOF

        cat > main.py << EOF
from fastapi import FastAPI
from app.api.health import router as health_router

app = FastAPI(title="$PROJECT_NAME", version="0.1.0")

app.include_router(health_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
EOF

        mkdir -p app/api
        cat > app/api/health.py << EOF
from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/health")
async def health_check():
    return {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "$PROJECT_NAME"
    }
EOF

        cat > app/__init__.py << 'EOF'
EOF

        cat > app/api/__init__.py << 'EOF'
EOF

        cat > .gitignore << 'EOF'
__pycache__/
*.pyc
.env
.venv/
venv/
.DS_Store
EOF
        ;;

    *)
        echo -e "${YELLOW}⚠️  Basic structure for $STACK${NC}"
        mkdir -p src docs
        echo "# $PROJECT_NAME" > README.md
        ;;
esac

# Create project configuration
cat > .agent/project.json << EOF
{
  "name": "$PROJECT_NAME",
  "language": "$LANGUAGE",
  "framework": "$FRAMEWORK",
  "project_type": "$PROJECT_TYPE",
  "stack": "$STACK",
  "created_at": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
  "version": "0.1.0"
}
EOF

# Create basic AGENT.md
cat > .agent/AGENT.md << EOF
# $PROJECT_NAME

**Language**: $LANGUAGE
**Framework**: $FRAMEWORK  
**Type**: $PROJECT_TYPE
**Created**: $(date +"%Y-%m-%d")

## Development Workflow

Use these Claude Code commands:

1. \`/prd create <feature>\` - Create requirements
2. \`/prd validate <feature>\` - Validate requirements  
3. \`/task plan <feature>\` - Plan development tasks
4. \`/task apply <task-id>\` - Execute tasks

## Guidelines

- Follow $FRAMEWORK best practices
- Write comprehensive tests
- Maintain clear documentation
EOF

# Initialize Git
echo -e "${WHITE}📦 Initializing Git...${NC}"
if [ ! -d ".git" ]; then
    git init
    git add .
    git commit -m "🚀 Initial setup: $LANGUAGE + $FRAMEWORK

Auto-generated project structure for $PROJECT_NAME
Stack: $STACK
Type: $PROJECT_TYPE

🤖 Generated with Claude Code /setup"
    
    echo -e "${GREEN}✓ Git initialized${NC}"
fi

# Success summary
echo ""
echo -e "${GREEN}🎉 Project Setup Complete!${NC}"
echo -e "${WHITE}========================${NC}"
echo -e "${CYAN}Project:${NC} $PROJECT_NAME"
echo -e "${CYAN}Stack:${NC} $LANGUAGE + $FRAMEWORK"
echo -e "${CYAN}Type:${NC} $PROJECT_TYPE"
echo ""
echo -e "${WHITE}🚀 Next Steps:${NC}"
echo -e "${CYAN}1.${NC} Install dependencies"
echo -e "${CYAN}2.${NC} Create your first PRD: ${YELLOW}/prd create <feature>${NC}"
echo -e "${CYAN}3.${NC} Plan tasks: ${YELLOW}/task plan <feature>${NC}"

case $LANGUAGE in
    "typescript"|"javascript")
        echo ""
        echo -e "${YELLOW}💡 Install dependencies: ${WHITE}npm install${NC}"
        ;;
    "rust")
        echo ""
        echo -e "${YELLOW}💡 Run project: ${WHITE}cargo run${NC}"
        ;;
    "python")
        echo ""
        echo -e "${YELLOW}💡 Install dependencies: ${WHITE}pip install -r requirements.txt${NC}"
        ;;
esac

echo ""
echo -e "${GREEN}Happy coding! 🚀${NC}"
```