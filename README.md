# Agent Template Repository

통합 AI 도구 설정 관리를 위한 템플릿 저장소입니다.

## 지원하는 도구들

- **Claude Code**: Anthropic의 공식 CLI 도구
- **Gemini CLI**: Google의 Gemini AI CLI 도구  
- **OpenCode**: 대화형 코딩 어시스턴트

## 주요 기능

### 🤖 AI 도구 통합 관리
- 여러 AI 도구의 설정을 한 곳에서 관리
- 프로젝트별 맞춤 설정 템플릿 제공
- 자동화된 초기화 스크립트

### 📝 PR 템플릿 시스템
- 상황별 특화된 PR 템플릿 (기능개발, 버그수정, 리팩토링 등)
- 일관된 PR 작성 가이드라인
- 팀 협업 효율성 향상

### 🚀 빠른 설정
- 원클릭 설치 스크립트
- 프로젝트 타입별 최적화된 설정
- 다른 프로젝트로 쉬운 이식

## 디렉토리 구조

```
agent-template/
├── .github/                # GitHub 템플릿
│   ├── pull_request_template.md      # 기본 PR 템플릿
│   └── PULL_REQUEST_TEMPLATE/        # 특화 PR 템플릿들
├── configs/                # 각 도구별 설정 템플릿
│   ├── claude/             # Claude Code 설정
│   ├── gemini/             # Gemini CLI 설정
│   └── opencode/           # OpenCode 설정
├── scripts/                # 초기화 및 관리 스크립트
│   ├── init.sh            # 통합 초기화 스크립트
│   ├── setup-pr-templates.sh  # PR 템플릿 설정 스크립트
│   ├── setup-claude.sh    # Claude 설정 스크립트
│   ├── setup-gemini.sh    # Gemini 설정 스크립트
│   └── setup-opencode.sh  # OpenCode 설정 스크립트
├── templates/              # 프로젝트별 템플릿
│   ├── pr-templates/      # PR 템플릿 모음
│   ├── web-project/       # 웹 프로젝트용 설정
│   ├── mobile-project/    # 모바일 프로젝트용 설정
│   └── data-project/      # 데이터 프로젝트용 설정
└── docs/                  # 문서
    ├── setup-guide.md     # 설정 가이드
    ├── usage-examples.md  # 사용 예제
    ├── pr-guidelines.md   # PR 작성 가이드
    └── pr-template-usage.md  # PR 템플릿 사용법
```

## 빠른 시작

### AI 도구 설정
```bash
# 새 프로젝트에서 AI 도구 설정 초기화
curl -sSL https://raw.githubusercontent.com/zdpk-automation/agent-template/main/scripts/init.sh | bash

# 또는 로컬에서
./scripts/init.sh --project-type web
```

### PR 템플릿 설정
```bash
# 기본 PR 템플릿 설치
curl -sSL https://raw.githubusercontent.com/zdpk-automation/agent-template/main/scripts/setup-pr-templates.sh | bash

# 모든 PR 템플릿 설치
curl -sSL https://raw.githubusercontent.com/zdpk-automation/agent-template/main/scripts/setup-pr-templates.sh | bash -s -- --type all
```

## 사용법

### AI 도구 설정
1. 원하는 프로젝트 디렉토리로 이동
2. 초기화 스크립트 실행
3. 필요한 도구들 선택
4. API 키 및 개인 설정 입력
5. 설정 완료

### PR 템플릿 활용
1. 프로젝트에 PR 템플릿 설치
2. PR 생성 시 적절한 템플릿 선택
3. 템플릿에 따라 정보 작성
4. 체크리스트 확인 후 제출

## 문서

- [설정 가이드](docs/setup-guide.md) - 상세한 설치 및 설정 방법
- [사용 예제](docs/usage-examples.md) - 실제 사용 시나리오와 예제
- [PR 작성 가이드](docs/pr-guidelines.md) - 효과적인 PR 작성 방법
- [PR 템플릿 사용법](docs/pr-template-usage.md) - PR 템플릿 활용 가이드

## 기여하기

새로운 도구 지원이나 템플릿 추가는 언제든 환영합니다. [PR 작성 가이드](docs/pr-guidelines.md)를 참고하여 기여해주세요.
=======
Basic template repository for AI tools configuration.
