# 사용 예제

## 시나리오별 활용법

### 1. 새 React 프로젝트 시작

```bash
# 프로젝트 생성
npx create-react-app my-app --template typescript
cd my-app

# Agent 설정 초기화
curl -sSL https://raw.githubusercontent.com/zdpk-automation/agent-template/main/scripts/init.sh | bash -s -- --type web

# 환경변수 설정
cp .env.example .env
# .env 파일에 API 키 입력

# Claude Code로 컴포넌트 생성
claude "Create a responsive header component with navigation"

# Gemini로 스타일링
gemini "Add Tailwind CSS styling to the header component"

# OpenCode로 테스트 작성
opencode "Write unit tests for the header component"
```

### 2. 기존 프로젝트에 AI 도구 추가

```bash
# 기존 프로젝트 디렉토리에서
cd existing-project

# 특정 도구만 설정
./scripts/init.sh --tools claude,opencode --force

# 프로젝트 컨텍스트 업데이트
# AGENTS.md 파일 수정하여 프로젝트 특성 반영
```

### 3. 팀 협업 설정

```bash
# 팀 공통 설정 저장소 생성
git clone https://github.com/zdpk-automation/agent-template.git team-ai-config
cd team-ai-config

# 팀 전용 설정 커스터마이징
# configs/ 디렉토리의 설정 파일들 수정

# 팀원들이 사용할 수 있도록 배포
git add .
git commit -m "Add team AI configuration"
git push origin main
```

## 도구별 활용 예제

### Claude Code 활용

#### 코드 리뷰 및 개선

```bash
# AGENTS.md에 코드 리뷰 가이드라인 추가
echo "## Code Review Guidelines
- Focus on performance and security
- Suggest modern JavaScript/TypeScript patterns
- Check for accessibility issues
- Recommend testing strategies" >> AGENTS.md

# Claude에게 코드 리뷰 요청
claude "Review this component for performance and accessibility issues"
```

#### 문서화 자동화

```bash
# API 문서 생성
claude "Generate comprehensive API documentation for this Express.js server"

# README 업데이트
claude "Update README.md with installation and usage instructions"
```

### Gemini CLI 활용

#### 데이터 분석

```bash
# 설정에 데이터 분석 컨텍스트 추가
cat >> .agent/configs/gemini-config.yaml << EOF
project_context:
  domain: "data_analysis"
  preferred_libraries: ["pandas", "numpy", "matplotlib"]
  output_format: "jupyter_notebook"
EOF

# 데이터 분석 요청
gemini "Analyze this CSV file and create visualizations"
```

#### 다국어 지원

```bash
# 한국어 응답 설정
gemini --language ko "이 React 컴포넌트를 다국어 지원하도록 수정해줘"
```

### OpenCode 활용

#### 실시간 코딩 세션

```bash
# 개발 서버와 함께 OpenCode 실행
npm run dev &
opencode --watch

# 실시간 코드 수정 및 피드백
```

#### 코드 품질 개선

```bash
# 설정에 품질 기준 추가
cat >> .agent/configs/opencode-config.toml << EOF
[quality_checks]
eslint = true
prettier = true
typescript = true
test_coverage = 80
EOF

# 코드 품질 개선 요청
opencode "Improve code quality and add missing tests"
```

## 워크플로우 예제

### 1. 기능 개발 워크플로우

```bash
# 1. 기능 계획 (Claude)
claude "Plan the implementation of user authentication feature"

# 2. 코드 구현 (OpenCode)
opencode "Implement JWT-based authentication with React hooks"

# 3. 스타일링 (Gemini)
gemini "Create a modern login form with CSS-in-JS"

# 4. 테스트 작성 (Claude)
claude "Write comprehensive tests for authentication flow"

# 5. 문서화 (Gemini)
gemini "Document the authentication API endpoints"
```

### 2. 버그 수정 워크플로우

```bash
# 1. 문제 분석 (Claude)
claude "Analyze this error log and identify the root cause"

# 2. 수정 구현 (OpenCode)
opencode "Fix the identified issue and add error handling"

# 3. 테스트 추가 (Gemini)
gemini "Add regression tests to prevent this bug from recurring"
```

### 3. 리팩토링 워크플로우

```bash
# 1. 코드 분석 (Claude)
claude "Analyze this legacy code and suggest refactoring strategies"

# 2. 점진적 리팩토링 (OpenCode)
opencode "Refactor this component to use modern React patterns"

# 3. 성능 최적화 (Gemini)
gemini "Optimize this code for better performance"
```

## 고급 설정 예제

### 1. 프로젝트별 커스텀 프롬프트

```json
// .agent/configs/claude-config.json
{
  "system_prompt": "You are a senior full-stack developer working on an e-commerce platform. Focus on scalability, security, and user experience. Always consider mobile-first design and accessibility.",
  "project_context": {
    "domain": "e-commerce",
    "tech_stack": ["React", "Node.js", "PostgreSQL", "Redis"],
    "priorities": ["security", "performance", "accessibility"]
  }
}
```

### 2. 팀 코딩 스타일 통합

```yaml
# .agent/configs/gemini-config.yaml
preferences:
  code_style: "airbnb"
  naming_convention: "camelCase"
  max_line_length: 100
  prefer_const: true
  semicolons: true
  trailing_commas: true

team_guidelines:
  - "Use TypeScript for all new code"
  - "Write tests for all public APIs"
  - "Follow atomic commit principles"
  - "Use conventional commit messages"
```

### 3. 자동화 스크립트 통합

```bash
#!/bin/bash
# scripts/ai-workflow.sh

# 코드 품질 체크
echo "🔍 Running code quality checks..."
npm run lint
npm run typecheck
npm test

# AI 도구로 개선 제안
echo "🤖 Getting AI suggestions..."
claude "Review recent changes and suggest improvements"
gemini "Check for potential security issues"
opencode "Optimize performance bottlenecks"

echo "✅ AI workflow complete!"
```

## 팁과 모범 사례

### 1. 효율적인 프롬프트 작성

```bash
# 좋은 예: 구체적이고 컨텍스트가 명확
claude "Refactor this React component to use TypeScript, add proper error handling, and ensure it's accessible for screen readers"

# 나쁜 예: 모호하고 컨텍스트 부족
claude "이 코드 좋게 만들어줘"
```

### 2. 설정 파일 버전 관리

```bash
# 민감한 정보 제외하고 설정 템플릿만 커밋
git add .agent/configs/*.template
git add AGENTS.md
git commit -m "Add AI tool configuration templates"
```

### 3. 성능 모니터링

```bash
# AI 도구 사용량 추적
echo "$(date): Claude API call" >> .agent/logs/usage.log

# 토큰 사용량 최적화
claude --max-tokens 1000 "Brief code review for this function"
```