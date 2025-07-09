# Agent Template Repository

통합 AI 도구 설정 관리를 위한 템플릿 저장소 및 CLI 도구 개발 프로젝트입니다.

A template repository for integrated AI tool configuration management and CLI tool development project.

## 프로젝트 개요 (Project Overview)

이 프로젝트는 AI 에이전트 템플릿을 활용하여 새로운 프로젝트 및 콘텐츠를 신속하게 생성하고 관리할 수 있는 CLI 도구를 개발하는 것을 목표로 합니다.

This project aims to develop a CLI tool that enables quick creation and management of new projects and content using AI agent templates.

## 지원하는 도구들 (Supported Tools)

- **Claude Code**: Anthropic의 공식 CLI 도구
- **Gemini CLI**: Google의 Gemini AI CLI 도구  
- **Agent Template CLI**: 개발 중인 템플릿 관리 CLI 도구 (Python + Typer)

## 주요 기능 (Key Features)

### 🤖 AI 도구 통합 관리 (Integrated AI Tool Management)
- 여러 AI 도구의 설정을 한 곳에서 관리
- 프로젝트별 맞춤 설정 템플릿 제공
- 자동화된 초기화 스크립트

### 📝 템플릿 시스템 (Template System)
- 3가지 템플릿 카테고리: 개발(Development), 콘텐츠(Content), 학습(Learning)
- 프로젝트 유형별 최적화된 템플릿 제공
- 심볼릭 링크 + 캐시 방식 파일 보호 메커니즘

### 🚀 CLI 도구 (CLI Tool - In Development)
- `init`: 프로젝트 초기화
- `convert`: 콘텐츠 플랫폼 간 변환
- `list`: 템플릿 목록 조회
- `update`: 템플릿 업데이트
- `config`: 설정 관리

### 📋 콘텐츠 변환 (Content Conversion)
- YouTube, Instagram, X/Twitter, Threads 간 콘텐츠 변환
- 플랫폼별 최적화된 형식 제공
- 대화형 변환 옵션

## 디렉토리 구조 (Directory Structure)

```
agent-template/
├── .agent/                 # 프로젝트 자체 에이전트 설정
│   ├── AGENT.md           # 프로젝트 자체용 AI 에이전트 공통 지침
│   ├── docs/              # 프로젝트 문서
│   │   ├── development-history.md    # 개발 이력
│   │   ├── contributing.md          # 기여 가이드
│   │   ├── agent-config-guide.md    # AI 에이전트 설정 가이드
│   │   ├── feature-documentation-template.md  # 기능 문서화 템플릿
│   │   └── decision-records/        # 의사결정 기록
│   ├── prd/               # PRD 문서
│   │   └── 2025-07-09-cli-tool.md  # CLI 도구 PRD
│   └── gemini-cli-usage-guide.md   # Gemini CLI 사용 가이드
├── CLAUDE.md → templates/common/CLAUDE.md  # Claude Code 설정 (심볼릭 링크)
├── .gemini/
│   └── GEMINI.md → ../templates/common/GEMINI.md  # Gemini CLI 설정 (심볼릭 링크)
├── cli/                    # CLI 도구 구현 (개발 예정)
│   ├── main.py            # CLI 메인 엔트리포인트
│   ├── commands/          # 각 명령어 구현
│   │   ├── init.py        # 초기화 명령어
│   │   ├── convert.py     # 변환 명령어
│   │   ├── list.py        # 목록 명령어
│   │   ├── update.py      # 업데이트 명령어
│   │   └── config.py      # 설정 명령어
│   ├── core/              # 핵심 로직
│   │   ├── template_manager.py     # 템플릿 관리
│   │   ├── project_generator.py   # 프로젝트 생성
│   │   ├── content_converter.py   # 콘텐츠 변환
│   │   └── version_manager.py     # 버전 관리
│   └── utils/             # 유틸리티
├── templates/              # 프로젝트별 템플릿
│   ├── common/            # 공통 템플릿
│   │   ├── AGENT.md       # 템플릿용 AI 에이전트 공통 지침
│   │   ├── CLAUDE.md      # Claude Code 설정 (AGENT.md 참조만)
│   │   ├── GEMINI.md      # Gemini CLI 설정 (AGENT.md 참조만)
│   │   └── FIXED_GUIDE.md # 고정 가이드
│   ├── development/       # 개발 템플릿 (계획됨)
│   │   ├── backend/       # 백엔드 템플릿
│   │   ├── frontend/      # 프론트엔드 템플릿
│   │   └── cli/          # CLI 도구 템플릿
│   ├── content/          # 콘텐츠 템플릿 (계획됨)
│   │   ├── blog/         # 블로그 템플릿
│   │   └── social/       # 소셜 미디어 템플릿
│   └── learning/         # 학습 템플릿 (계획됨)
└── example/              # CLI 명령어 사용 예시
    ├── init/             # `init` 명령어 예시
    ├── convert/          # `convert` 명령어 예시
    ├── list/             # `list` 명령어 예시
    ├── update/           # `update` 명령어 예시
    └── config/           # `config` 명령어 예시
```

## 개발 로드맵 (Development Roadmap)

### Phase 1 (2025 Q3) - 핵심 기능 구현
- [x] PRD 작성 및 기술 설계
- [x] 의사결정 기록 및 아키텍처 문서화
- [ ] 핵심 명령어 구현 (`init`, `list`, `update`)
- [ ] 기본 템플릿 제공
- [ ] 파일 보호 메커니즘 구현

### Phase 2 (2025 Q4) - 확장 기능
- [ ] 콘텐츠 변환 기능 추가 (`convert`)
- [ ] 더 많은 템플릿 지원
- [ ] 사용자 설정 관리 (`config`)
- [ ] 테스트 및 문서화 완료

### Phase 3 (2026 Q1) - 고급 기능
- [ ] 웹 기반 템플릿 브라우저
- [ ] 커뮤니티 템플릿 공유
- [ ] 고급 커스터마이징 기능

## 빠른 시작 (Quick Start)

### 현재 사용 가능한 기능
```bash
# 현재 프로젝트에서 AI 도구 설정 참조
# Claude Code 사용 시
cat CLAUDE.md

# Gemini CLI 사용 시  
cat .gemini/GEMINI.md

# CLI 명령어 사용 예시 확인
ls example/
```

### CLI 도구 사용 (개발 예정)
```bash
# 프로젝트 초기화
agent-template init

# 템플릿 목록 조회
agent-template list

# 콘텐츠 변환
agent-template convert blog-post.md youtube,instagram

# 템플릿 업데이트
agent-template update

# 설정 관리
agent-template config
```

## 문서 (Documentation)

### 사용자 문서 (User Documentation)
- [CLI 명령어 사용 예시](example/README.md) - 각 명령어의 상세한 사용법
- [CLI 도구 PRD](.agent/prd/2025-07-09-cli-tool.md) - 제품 요구사항 문서
- [설정 가이드](.agent/docs/setup-guide.md) - 상세한 설치 및 설정 방법
- [사용 예제](.agent/docs/usage-examples.md) - 실제 사용 시나리오와 예제

### 개발자 문서 (Developer Documentation)
- [개발 이력](.agent/docs/development-history.md) - 프로젝트 발전 과정과 변경사항
- [기여 가이드](.agent/docs/contributing.md) - 프로젝트 기여 방법, 코딩 스타일, PR 과정
- [AI 에이전트 설정 가이드](.agent/docs/agent-config-guide.md) - AGENT.md 파일 작성 및 활용법
- [기능 문서화 템플릿](.agent/docs/feature-documentation-template.md) - 새 기능 문서화 표준
- [CLI 도구 개발 가이드](.agent/docs/cli-tool-guide.md) - CLI 도구 개발 가이드라인
- [Gemini CLI 사용 가이드](.agent/gemini-cli-usage-guide.md) - 대용량 코드베이스 분석 시 활용법

### 의사결정 기록 (Decision Records)
- [파일 보호 메커니즘](.agent/docs/decision-records/2025-07-09-file-protection-mechanism.md) - 파일 보호 방식 결정 과정

## 기여하기 (Contributing)

새로운 도구 지원이나 템플릿 추가는 언제든 환영합니다. [기여 가이드](.agent/docs/contributing.md)를 참고하여 기여해주세요.

Contributions for new tool support or template additions are always welcome. Please refer to the [contributing guide](.agent/docs/contributing.md) for contribution guidelines.

## 라이선스 (License)

이 프로젝트는 MIT 라이선스 하에 제공됩니다.

This project is provided under the MIT License.