---
allowed-tools: Read, Write, WebSearch, TodoWrite, Bash
description: Create comprehensive PRD through interactive dialogue
---

# PRD Create / PRD 작성

Create a comprehensive Product Requirements Document through interactive dialogue with the user.

## Usage / 사용법
```
/prd create <feature-name>
```

## What this command does / 이 명령어의 기능
1. Interactive PRD creation process / 대화형 PRD 작성 프로세스
2. Deep requirement exploration / 요구사항 심층 탐색
3. Automatic section generation / 자동 섹션 생성
4. Technical feasibility analysis / 기술적 실현가능성 분석
5. Save to `.agent/prd/` directory / `.agent/prd/` 디렉토리에 저장

## Arguments / 인수
- `feature-name`: Name of the feature to create PRD for / PRD를 작성할 기능명

Let me create a comprehensive PRD for the feature: **$ARGUMENTS**

```bash
#!/bin/bash

FEATURE_NAME="$ARGUMENTS"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m'

if [ -z "$FEATURE_NAME" ]; then
    echo -e "${RED}❌ Error: Feature name is required${NC}"
    echo -e "${CYAN}Usage: /prd create <feature-name>${NC}"
    echo -e "${CYAN}Example: /prd create user-authentication${NC}"
    exit 1
fi

echo -e "${BLUE}📝 PRD Creation - Interactive Requirements Gathering${NC}"
echo -e "${BLUE}=================================================${NC}"
echo -e "${WHITE}Feature: $FEATURE_NAME${NC}"
echo ""

# Check if project exists
if [ ! -f ".agent/project.json" ]; then
    echo -e "${YELLOW}⚠️  No project configuration found${NC}"
    echo -e "${CYAN}Run /setup first to initialize your project${NC}"
    exit 1
fi

# Load project info
PROJECT_NAME=$(grep -o '"name": "[^"]*"' .agent/project.json | cut -d'"' -f4)
LANGUAGE=$(grep -o '"language": "[^"]*"' .agent/project.json | cut -d'"' -f4)
FRAMEWORK=$(grep -o '"framework": "[^"]*"' .agent/project.json | cut -d'"' -f4)

echo -e "${GREEN}✓ Project: $PROJECT_NAME ($LANGUAGE + $FRAMEWORK)${NC}"
echo ""

# Create PRD filename with date
PRD_DATE=$(date +"%Y-%m-%d")
PRD_FILENAME="$PRD_DATE-$FEATURE_NAME.md"
PRD_PATH=".agent/prd/$PRD_FILENAME"

# Check if PRD already exists
if [ -f "$PRD_PATH" ]; then
    echo -e "${YELLOW}⚠️  PRD already exists: $PRD_FILENAME${NC}"
    echo "Do you want to update it? (y/N)"
    read -r response
    if [[ ! "$response" =~ ^[Yy]$ ]]; then
        echo "PRD creation cancelled."
        exit 0
    fi
    echo ""
fi

echo -e "${WHITE}🎯 Starting Interactive PRD Creation Process${NC}"
echo -e "${CYAN}I'll ask you a series of questions to create a comprehensive PRD.${NC}"
echo -e "${CYAN}Please provide detailed answers to ensure thorough documentation.${NC}"
echo ""

# Initialize PRD content
PRD_CONTENT="# PRD: $FEATURE_NAME / $(echo $FEATURE_NAME | sed 's/-/ /g' | sed 's/\b\w/\U&/g')

**Project**: $PROJECT_NAME  
**Technology Stack**: $LANGUAGE + $FRAMEWORK  
**Created**: $PRD_DATE  
**Status**: Draft

"

# 1. Problem Statement
echo -e "${WHITE}1️⃣  Problem Statement / 문제 정의${NC}"
echo -e "${CYAN}What problem does this feature solve? Describe the current pain points.${NC}"
echo -e "${YELLOW}Example: Users have to manually track their progress, leading to confusion and lost data.${NC}"
echo ""
read -p "Problem: " problem_statement

PRD_CONTENT+="## Problem Statement / 문제 정의

$problem_statement

"

# 2. Target Users
echo ""
echo -e "${WHITE}2️⃣  Target Users / 대상 사용자${NC}"
echo -e "${CYAN}Who will use this feature? Describe the user personas.${NC}"
echo -e "${YELLOW}Example: Marketing managers, developers, end-users with mobile devices${NC}"
echo ""
read -p "Target Users: " target_users

PRD_CONTENT+="## Target Users / 대상 사용자

$target_users

"

# 3. Solution Overview
echo ""
echo -e "${WHITE}3️⃣  Solution Overview / 솔루션 개요${NC}"
echo -e "${CYAN}Describe the high-level solution. What will you build?${NC}"
echo -e "${YELLOW}Example: A dashboard with real-time tracking, mobile app integration, and analytics${NC}"
echo ""
read -p "Solution: " solution_overview

PRD_CONTENT+="## Solution Overview / 솔루션 개요

$solution_overview

"

# 4. User Stories
echo ""
echo -e "${WHITE}4️⃣  User Stories / 사용자 스토리${NC}"
echo -e "${CYAN}Provide 3-5 key user stories in the format: 'As a [user], I want [goal] so that [benefit]'${NC}"
echo -e "${YELLOW}Press Enter after each story, type 'done' when finished:${NC}"
echo ""

user_stories=""
story_count=1
while true; do
    read -p "Story $story_count: " story
    if [ "$story" = "done" ] || [ -z "$story" ]; then
        break
    fi
    user_stories+="$story_count. $story
"
    ((story_count++))
done

PRD_CONTENT+="## User Stories / 사용자 스토리

$user_stories
"

# 5. Functional Requirements
echo ""
echo -e "${WHITE}5️⃣  Functional Requirements / 기능 요구사항${NC}"
echo -e "${CYAN}List the specific features and capabilities. Be detailed.${NC}"
echo -e "${YELLOW}Press Enter after each requirement, type 'done' when finished:${NC}"
echo ""

functional_reqs=""
req_count=1
while true; do
    read -p "Requirement $req_count: " req
    if [ "$req" = "done" ] || [ -z "$req" ]; then
        break
    fi
    functional_reqs+="- $req
"
    ((req_count++))
done

PRD_CONTENT+="## Functional Requirements / 기능 요구사항

$functional_reqs
"

# 6. Technical Requirements
echo ""
echo -e "${WHITE}6️⃣  Technical Requirements / 기술 요구사항${NC}"
echo -e "${CYAN}What are the technical constraints, APIs, databases, third-party services needed?${NC}"
echo ""
read -p "Technical Requirements: " tech_requirements

PRD_CONTENT+="## Technical Requirements / 기술 요구사항

### Technology Stack / 기술 스택
- **Language**: $LANGUAGE
- **Framework**: $FRAMEWORK
- **Additional Requirements**: $tech_requirements

### Architecture Considerations / 아키텍처 고려사항
"

# Add framework-specific architecture notes
case "$FRAMEWORK" in
    "nestjs")
        PRD_CONTENT+="- Use NestJS modules for feature organization
- Implement DTOs with class-validator
- Use guards for authentication/authorization
- Implement proper exception filters
"
        ;;
    "axum")
        PRD_CONTENT+="- Use Axum handlers with proper error handling
- Implement middleware for cross-cutting concerns
- Use serde for JSON serialization
- Follow async/await patterns
"
        ;;
    "fastapi")
        PRD_CONTENT+="- Use FastAPI dependency injection
- Implement Pydantic models for validation
- Use async handlers where appropriate
- Implement proper OpenAPI documentation
"
        ;;
    "react")
        PRD_CONTENT+="- Use functional components with hooks
- Implement proper TypeScript interfaces
- Use React Router for navigation
- Follow component composition patterns
"
        ;;
    *)
        PRD_CONTENT+="- Follow $FRAMEWORK best practices
- Implement proper error handling
- Use appropriate design patterns
- Ensure code maintainability
"
        ;;
esac

# 7. API Specifications
echo ""
echo -e "${WHITE}7️⃣  API Specifications / API 명세${NC}"
echo -e "${CYAN}Describe the key API endpoints (if applicable). Format: METHOD /path - Description${NC}"
echo -e "${YELLOW}Example: POST /api/auth/login - User authentication endpoint${NC}"
echo -e "${YELLOW}Press Enter after each endpoint, type 'done' when finished:${NC}"
echo ""

api_specs=""
while true; do
    read -p "API Endpoint: " endpoint
    if [ "$endpoint" = "done" ] || [ -z "$endpoint" ]; then
        break
    fi
    api_specs+="- $endpoint
"
done

if [ -n "$api_specs" ]; then
    PRD_CONTENT+="
## API Specifications / API 명세

$api_specs
"
fi

# 8. Security Considerations
echo ""
echo -e "${WHITE}8️⃣  Security Considerations / 보안 고려사항${NC}"
echo -e "${CYAN}What security measures are needed? Authentication, authorization, data protection?${NC}"
echo ""
read -p "Security Requirements: " security_reqs

PRD_CONTENT+="## Security Considerations / 보안 고려사항

$security_reqs

### Framework-Specific Security / 프레임워크별 보안
"

case "$FRAMEWORK" in
    "nestjs")
        PRD_CONTENT+="- Implement JWT authentication with guards
- Use class-validator for input validation
- Apply rate limiting middleware
- Implement CORS properly
"
        ;;
    "axum")
        PRD_CONTENT+="- Use tower middleware for authentication
- Implement proper input validation
- Use secure headers middleware
- Handle CORS configuration
"
        ;;
    "fastapi")
        PRD_CONTENT+="- Use FastAPI security utilities
- Implement OAuth2 with JWT tokens
- Use Pydantic for input validation
- Apply proper CORS middleware
"
        ;;
    *)
        PRD_CONTENT+="- Implement authentication and authorization
- Validate all user inputs
- Use HTTPS in production
- Follow security best practices
"
        ;;
esac

# 9. Performance Requirements
echo ""
echo -e "${WHITE}9️⃣  Performance Requirements / 성능 요구사항${NC}"
echo -e "${CYAN}What are the performance expectations? Response times, concurrent users, etc.${NC}"
echo ""
read -p "Performance Requirements: " perf_reqs

PRD_CONTENT+="
## Performance Requirements / 성능 요구사항

$perf_reqs

"

# 10. Testing Strategy
echo ""
echo -e "${WHITE}🔟 Testing Strategy / 테스트 전략${NC}"
echo -e "${CYAN}How will this feature be tested? Unit tests, integration tests, E2E tests?${NC}"
echo ""
read -p "Testing Strategy: " testing_strategy

PRD_CONTENT+="## Testing Strategy / 테스트 전략

$testing_strategy

### Test Types / 테스트 유형
- **Unit Tests**: Individual component/function testing
- **Integration Tests**: API endpoint testing  
- **E2E Tests**: Full user workflow testing
- **Performance Tests**: Load and stress testing

"

# 11. Success Criteria
echo ""
echo -e "${WHITE}📊 Success Criteria / 성공 기준${NC}"
echo -e "${CYAN}How will you measure the success of this feature?${NC}"
echo ""
read -p "Success Criteria: " success_criteria

PRD_CONTENT+="## Success Criteria / 성공 기준

$success_criteria

"

# 12. Implementation Timeline
echo ""
echo -e "${WHITE}⏰ Implementation Timeline / 구현 일정${NC}"
echo -e "${CYAN}Estimated timeline for implementation (e.g., 2 weeks, 1 month)?${NC}"
echo ""
read -p "Timeline: " timeline

PRD_CONTENT+="## Implementation Timeline / 구현 일정

**Estimated Duration**: $timeline

### Phases / 단계
1. **Planning & Design**: Requirements finalization and technical design
2. **Core Development**: Main feature implementation  
3. **Testing & QA**: Comprehensive testing and bug fixes
4. **Documentation**: API docs and user guides
5. **Deployment**: Production deployment and monitoring

"

# 13. Dependencies and Risks
echo ""
echo -e "${WHITE}⚠️  Dependencies and Risks / 의존성 및 위험요소${NC}"
echo -e "${CYAN}What dependencies or risks should be considered?${NC}"
echo ""
read -p "Dependencies/Risks: " dependencies

PRD_CONTENT+="## Dependencies and Risks / 의존성 및 위험요소

$dependencies

"

# Add metadata
PRD_CONTENT+="---

## Metadata / 메타데이터

- **Created by**: Claude Code /prd create command
- **Last updated**: $PRD_DATE
- **Review status**: Pending validation
- **Next steps**: Run \`/prd validate $FEATURE_NAME\` to fact-check and validate

---

> 📝 **Note**: This PRD was created through interactive dialogue. Review and validate using \`/prd validate $FEATURE_NAME\` before implementation.
"

# Save PRD
echo -e "${WHITE}💾 Saving PRD...${NC}"
echo "$PRD_CONTENT" > "$PRD_PATH"

# Success message
echo ""
echo -e "${GREEN}🎉 PRD Created Successfully!${NC}"
echo -e "${WHITE}================================${NC}"
echo -e "${CYAN}Feature:${NC} $FEATURE_NAME"
echo -e "${CYAN}File:${NC} $PRD_PATH"
echo -e "${CYAN}Lines:${NC} $(wc -l < "$PRD_PATH")"
echo ""
echo -e "${WHITE}📋 PRD Contents Summary:${NC}"
echo -e "${CYAN}•${NC} Problem Statement & Target Users"
echo -e "${CYAN}•${NC} Solution Overview & User Stories"  
echo -e "${CYAN}•${NC} Functional & Technical Requirements"
echo -e "${CYAN}•${NC} API Specifications & Security"
echo -e "${CYAN}•${NC} Performance & Testing Strategy"
echo -e "${CYAN}•${NC} Success Criteria & Timeline"
echo ""
echo -e "${WHITE}🚀 Next Steps:${NC}"
echo -e "${CYAN}1.${NC} Validate PRD: ${YELLOW}/prd validate $FEATURE_NAME${NC}"
echo -e "${CYAN}2.${NC} Plan tasks: ${YELLOW}/task plan $FEATURE_NAME${NC}"
echo -e "${CYAN}3.${NC} Start development: ${YELLOW}/task apply <task-id>${NC}"
echo ""
echo -e "${GREEN}✨ PRD ready for validation and implementation!${NC}"
```