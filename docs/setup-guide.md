# 설정 가이드

## 개요

이 가이드는 Claude Code, Gemini CLI, OpenCode를 통합 관리하기 위한 설정 방법을 설명합니다.

## 사전 요구사항

### API 키 준비

1. **Claude Code (Anthropic)**
   - [Anthropic Console](https://console.anthropic.com/)에서 API 키 발급
   - 환경변수: `ANTHROPIC_API_KEY`

2. **Gemini CLI (Google)**
   - [Google AI Studio](https://makersuite.google.com/app/apikey)에서 API 키 발급
   - 환경변수: `GOOGLE_API_KEY`

3. **OpenCode**
   - [OpenCode 웹사이트](https://opencode.ai)에서 API 키 발급
   - 환경변수: `OPENCODE_API_KEY`

### 도구 설치

```bash
# Claude Code 설치
npm install -g @anthropic-ai/claude-cli

# Gemini CLI 설치
pip install google-generativeai

# OpenCode 설치
npm install -g opencode-cli
```

## 빠른 설정

### 1. 자동 초기화 (권장)

```bash
# 새 프로젝트에서
curl -sSL https://raw.githubusercontent.com/zdpk-automation/agent-template/main/scripts/init.sh | bash

# 또는 특정 도구만
curl -sSL https://raw.githubusercontent.com/zdpk-automation/agent-template/main/scripts/init.sh | bash -s -- --tools claude,gemini
```

### 2. 수동 설정

```bash
# 저장소 클론
git clone https://github.com/zdpk-automation/agent-template.git
cd agent-template

# 원하는 프로젝트로 설정 복사
cp -r configs/ /path/to/your/project/.agent/
cp scripts/init.sh /path/to/your/project/
```

## 상세 설정

### Claude Code 설정

1. **AGENTS.md 파일 생성**
   ```bash
   cp configs/claude/AGENTS.md ./AGENTS.md
   ```

2. **설정 파일 커스터마이징**
   ```json
   {
     "model": "claude-3-5-sonnet-20241022",
     "temperature": 0.1,
     "system_prompt": "프로젝트에 맞는 시스템 프롬프트"
   }
   ```

### Gemini CLI 설정

1. **설정 파일 위치**
   ```bash
   ~/.config/gemini/config.yaml
   ```

2. **프로젝트별 설정**
   ```yaml
   project_context:
     default_language: "typescript"
     framework: "react"
   ```

### OpenCode 설정

1. **설정 파일 위치**
   ```bash
   ~/.opencode/config.toml
   ```

2. **에디터 통합**
   ```toml
   [editor]
   theme = "dark"
   auto_save = true
   ```

## 환경변수 관리

### .env 파일 생성

```bash
# .env 파일 생성
cp .env.example .env

# API 키 입력
ANTHROPIC_API_KEY=your_actual_key_here
GOOGLE_API_KEY=your_actual_key_here
OPENCODE_API_KEY=your_actual_key_here
```

### 보안 고려사항

- `.env` 파일을 `.gitignore`에 추가
- API 키를 코드에 하드코딩하지 않기
- 프로덕션 환경에서는 환경변수 또는 시크릿 관리 도구 사용

## 프로젝트 타입별 설정

### 웹 프로젝트

```bash
./scripts/init.sh --type web --tools claude,opencode
```

- React/Next.js 최적화
- TypeScript 설정
- ESLint/Prettier 통합

### 모바일 프로젝트

```bash
./scripts/init.sh --type mobile --tools gemini,opencode
```

- React Native 최적화
- 플랫폼별 설정
- 네이티브 모듈 지원

### 데이터 프로젝트

```bash
./scripts/init.sh --type data --tools claude,gemini
```

- Python/Jupyter 최적화
- 데이터 분석 도구 통합
- 시각화 라이브러리 설정

## 문제 해결

### 일반적인 문제

1. **API 키 인식 안됨**
   - 환경변수 설정 확인
   - 쉘 재시작 후 재시도

2. **설정 파일 충돌**
   - `--force` 옵션으로 강제 덮어쓰기
   - 기존 설정 백업 후 재설정

3. **권한 문제**
   - 스크립트 실행 권한 확인: `chmod +x scripts/init.sh`
   - sudo 권한이 필요한 경우 확인

### 로그 및 디버깅

```bash
# 상세 로그 출력
DEBUG=1 ./scripts/init.sh

# 설정 파일 검증
./scripts/validate-config.sh
```