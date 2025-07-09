# AI 도구 설정 파일 참조 가이드

## 개요

이 문서는 각 AI 도구들이 기본적으로 참조하는 설정 파일들의 위치와 우선순위를 정리합니다. 모든 도구가 일관된 지침을 따르도록 하기 위한 통합 설정 시스템을 제공합니다.

## 각 도구별 설정 파일 위치

### 1. Claude Code (Anthropic)

#### 기본 참조 파일
```
프로젝트_루트/
├── AGENTS.md                    # 🔥 최우선 참조 파일
├── .agent/
│   ├── configs/
│   │   └── claude-config.json   # Claude 전용 설정
│   └── instructions.md          # 추가 지침
└── .clauderc                    # 선택적 설정 파일
```

#### 참조 우선순위
1. `./AGENTS.md` (프로젝트 루트)
2. `./.agent/configs/claude-config.json`
3. `./.agent/instructions.md`
4. `~/.config/claude/config.json` (글로벌)

### 2. OpenCode

#### 기본 참조 파일
```
프로젝트_루트/
├── AGENTS.md                    # 🔥 최우선 참조 파일
├── .agent/
│   ├── configs/
│   │   └── opencode-config.json # OpenCode 전용 설정
│   └── instructions.md          # 추가 지침
└── .opencode/
    └── config.yaml              # 선택적 설정
```

#### 참조 우선순위
1. `./AGENTS.md` (프로젝트 루트)
2. `./.agent/configs/opencode-config.json`
3. `./.opencode/config.yaml`
4. `~/.config/opencode/config.yaml` (글로벌)

### 3. Gemini CLI (Google)

#### 기본 참조 파일
```
프로젝트_루트/
├── AGENTS.md                    # 🔥 최우선 참조 파일
├── .agent/
│   ├── configs/
│   │   └── gemini-config.json   # Gemini 전용 설정
│   └── instructions.md          # 추가 지침
├── .gemini/
│   └── config.yaml              # Gemini 설정
└── gemini.config.js             # 선택적 JS 설정
```

#### 참조 우선순위
1. `./AGENTS.md` (프로젝트 루트)
2. `./.agent/configs/gemini-config.json`
3. `./.gemini/config.yaml`
4. `~/.config/gemini/config.yaml` (글로벌)
5. 환경 변수 `GEMINI_API_KEY`

### 4. Claude for Sheets

#### 설정 방법
- **위치**: Google Sheets 확장 프로그램 내부
- **설정 경로**: Extensions > Claude for Sheets™ > Open sidebar > ☰ > Settings
- **API 키**: 각 시트별로 개별 설정 필요
- **참조**: 시트별 독립적 설정 (프로젝트 파일 참조 불가)

## 통합 설정 시스템

### 핵심 원칙

1. **AGENTS.md 최우선**: 모든 도구는 프로젝트 루트의 `AGENTS.md`를 최우선으로 참조
2. **도구별 전용 설정**: `.agent/configs/` 디렉토리에 도구별 JSON 설정 파일
3. **계층적 설정**: 프로젝트 > 사용자 > 글로벌 순서로 설정 적용
4. **일관된 구조**: 모든 프로젝트에서 동일한 디렉토리 구조 사용

### 표준 디렉토리 구조

```
프로젝트_루트/
├── AGENTS.md                    # 🔥 모든 AI 도구의 최우선 참조 파일
├── .agent/                      # AI 도구 통합 설정 디렉토리
│   ├── configs/                 # 도구별 전용 설정
│   │   ├── claude-config.json   # Claude Code 설정
│   │   ├── opencode-config.json # OpenCode 설정
│   │   ├── gemini-config.json   # Gemini CLI 설정
│   │   └── shared-config.json   # 공통 설정
│   ├── instructions.md          # 추가 지침 및 컨텍스트
│   ├── prompts/                 # 재사용 가능한 프롬프트
│   │   ├── code-review.md
│   │   ├── documentation.md
│   │   └── testing.md
│   └── templates/               # 코드 템플릿
│       ├── component.tsx
│       ├── api-endpoint.ts
│       └── test-case.test.ts
├── docs/                        # 프로젝트 문서
│   ├── pr-guidelines.md         # PR 작성 가이드
│   ├── coding-standards.md      # 코딩 표준
│   └── ai-usage-guide.md        # AI 도구 사용 가이드
└── .gitignore                   # .agent/ 디렉토리는 추적 대상
```

## AGENTS.md 표준 템플릿

### 기본 구조

```markdown
# AI Agent Configuration

## 프로젝트 개요
- **프로젝트명**: [프로젝트 이름]
- **주요 기술**: [기술 스택]
- **프로젝트 타입**: [웹앱/모바일/API/라이브러리 등]

## 개발 환경 설정

### 언어 및 프레임워크
- 주 언어: [TypeScript/Python/Java 등]
- 프레임워크: [React/Next.js/Django 등]
- 패키지 매니저: [npm/yarn/pnpm/pip 등]

### 코딩 스타일
- 린터: [ESLint/Pylint/등]
- 포매터: [Prettier/Black/등]
- 타입 체크: [TypeScript/mypy/등]

### 테스트 전략
- 단위 테스트: [Jest/pytest/등]
- 통합 테스트: [Cypress/Playwright/등]
- 커버리지 목표: [80% 이상]

### 빌드 및 배포
- 빌드 명령어: `npm run build`
- 테스트 명령어: `npm test`
- 린트 명령어: `npm run lint`
- 타입 체크: `npm run typecheck`

## AI 도구 사용 가이드

### 일반 원칙
1. **코드 품질 우선**: 항상 코드 품질과 가독성을 최우선으로 고려
2. **테스트 작성**: 새로운 기능에는 반드시 테스트 코드 포함
3. **문서화**: 복잡한 로직은 주석과 문서로 설명
4. **보안 고려**: 보안 취약점이 없는지 항상 검토

### 코드 작성 스타일
- 함수형 프로그래밍 선호
- 명확하고 의미 있는 변수명 사용
- 단일 책임 원칙 준수
- DRY (Don't Repeat Yourself) 원칙 적용

### PR 작성 가이드
- PR 템플릿 사용 필수
- 변경사항에 대한 명확한 설명
- 테스트 계획 포함
- 스크린샷 첨부 (UI 변경 시)

## 프로젝트별 특수 지침

### [프로젝트 특화 내용]
- 특별한 아키텍처 패턴
- 도메인 특화 규칙
- 성능 요구사항
- 보안 요구사항

## 참고 문서
- [코딩 표준](./docs/coding-standards.md)
- [PR 가이드라인](./docs/pr-guidelines.md)
- [API 문서](./docs/api-documentation.md)
```

## 도구별 전용 설정 파일

### claude-config.json
```json
{
  "model": "claude-3-sonnet-20240229",
  "max_tokens": 4000,
  "temperature": 0.1,
  "system_prompt": "You are a senior software engineer following the project guidelines in AGENTS.md",
  "preferences": {
    "code_style": "functional",
    "test_framework": "jest",
    "documentation_style": "jsdoc"
  },
  "custom_instructions": [
    "Always follow the coding standards defined in AGENTS.md",
    "Include tests for new functionality",
    "Use TypeScript strict mode",
    "Follow the PR template when suggesting changes"
  ]
}
```

### opencode-config.json
```json
{
  "model": "claude-3-sonnet-20240229",
  "context_files": [
    "AGENTS.md",
    "docs/coding-standards.md",
    "docs/pr-guidelines.md"
  ],
  "auto_include_patterns": [
    "*.md",
    "package.json",
    "tsconfig.json"
  ],
  "preferences": {
    "verbose": false,
    "auto_test": true,
    "auto_lint": true
  }
}
```

### gemini-config.json
```json
{
  "model": "gemini-pro",
  "safety_settings": {
    "harassment": "block_none",
    "hate_speech": "block_none",
    "sexually_explicit": "block_none",
    "dangerous_content": "block_none"
  },
  "generation_config": {
    "temperature": 0.1,
    "top_p": 0.8,
    "top_k": 40,
    "max_output_tokens": 4000
  },
  "system_instruction": "Follow the project guidelines in AGENTS.md. You are a senior software engineer."
}
```

## 설정 동기화 스크립트

### 자동 설정 동기화
```bash
#!/bin/bash
# sync-ai-configs.sh

# AGENTS.md의 변경사항을 각 도구별 설정에 반영
./scripts/sync-claude-config.sh
./scripts/sync-opencode-config.sh  
./scripts/sync-gemini-config.sh

echo "✅ All AI tool configurations synchronized with AGENTS.md"
```

## 모범 사례

### 1. 설정 파일 관리
- **버전 관리**: 모든 설정 파일을 Git으로 추적
- **팀 공유**: 팀원 모두가 동일한 설정 사용
- **정기 업데이트**: 프로젝트 진행에 따라 설정 업데이트

### 2. 일관성 유지
- **표준 템플릿 사용**: 모든 프로젝트에서 동일한 구조
- **명명 규칙 준수**: 파일명과 디렉토리명 일관성
- **문서화**: 설정 변경 시 문서 업데이트

### 3. 보안 고려사항
- **API 키 분리**: 설정 파일에 API 키 포함 금지
- **환경 변수 사용**: 민감한 정보는 환경 변수로 관리
- **권한 관리**: 설정 파일 접근 권한 적절히 설정

## 문제 해결

### 설정이 적용되지 않는 경우
1. 파일 경로 확인
2. 파일 권한 확인
3. JSON 문법 오류 확인
4. 도구별 캐시 삭제

### 설정 충돌 해결
1. 우선순위 확인
2. 중복 설정 제거
3. 명시적 설정 사용

## 추가 리소스

- [Claude Code 공식 문서](https://docs.anthropic.com/claude/docs)
- [OpenCode 공식 문서](https://opencode.ai/docs)
- [Gemini CLI 공식 문서](https://ai.google.dev/gemini-api/docs)
- [AI 도구 비교 가이드](./ai-tools-comparison.md)