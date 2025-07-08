# Agent Template Repository

통합 AI 도구 설정 관리를 위한 템플릿 저장소입니다.

## 지원하는 도구들

- **Claude Code**: Anthropic의 공식 CLI 도구
- **Gemini CLI**: Google의 Gemini AI CLI 도구  
- **OpenCode**: 대화형 코딩 어시스턴트

## 디렉토리 구조

```
agent-template/
├── configs/                 # 각 도구별 설정 템플릿
│   ├── claude/             # Claude Code 설정
│   ├── gemini/             # Gemini CLI 설정
│   └── opencode/           # OpenCode 설정
├── scripts/                # 초기화 및 관리 스크립트
│   ├── init.sh            # 통합 초기화 스크립트
│   ├── setup-claude.sh    # Claude 설정 스크립트
│   ├── setup-gemini.sh    # Gemini 설정 스크립트
│   └── setup-opencode.sh  # OpenCode 설정 스크립트
├── templates/              # 프로젝트별 템플릿
│   ├── web-project/       # 웹 프로젝트용 설정
│   ├── mobile-project/    # 모바일 프로젝트용 설정
│   └── data-project/      # 데이터 프로젝트용 설정
└── docs/                  # 문서
    ├── setup-guide.md     # 설정 가이드
    └── usage-examples.md  # 사용 예제
```

## 빠른 시작

```bash
# 새 프로젝트에서 설정 초기화
curl -sSL https://raw.githubusercontent.com/zdpk-automation/agent-template/main/scripts/init.sh | bash

# 또는 로컬에서
./scripts/init.sh --project-type web
```

## 사용법

1. 원하는 프로젝트 디렉토리로 이동
2. 초기화 스크립트 실행
3. 필요한 도구들 선택
4. API 키 및 개인 설정 입력
5. 설정 완료

## 기여하기

새로운 도구 지원이나 템플릿 추가는 언제든 환영합니다.