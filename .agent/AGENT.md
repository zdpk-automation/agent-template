# Agent Instructions - Agent Template Repository

이 파일은 agent-template 저장소를 개발하고 관리할 때 AI 에이전트들이 참조하는 공통 지침입니다.

## 필수 참조 문서
작업 시작 전에 반드시 다음 문서들을 읽고 지침을 따라야 합니다:

- [개발 이력](.agent/docs/development-history.md) - 프로젝트 발전 과정과 변경사항
- [기여 가이드](.agent/docs/contributing.md) - 프로젝트 기여 방법, 코딩 스타일, PR 과정
- [AI 에이전트 설정 가이드](.agent/docs/agent-config-guide.md) - AGENT.md 파일 작성 및 활용법
- [기능 문서화 템플릿](.agent/docs/feature-documentation-template.md) - 새 기능 문서화 표준

## Claude 사용자 추가 참조 문서
현재 LLM이 Claude인 경우 다음 문서도 참조하세요:

- [Gemini CLI 사용 가이드](.agent/gemini-cli-usage-guide.md) - 대용량 코드베이스 분석 시 Gemini CLI 활용법

## 프로젝트 개요
이 저장소는 통합 AI 도구 설정 관리를 위한 템플릿 저장소입니다:
- 여러 AI 도구 (Claude Code, Gemini CLI, OpenCode) 설정 통합 관리
- 프로젝트별 맞춤 설정 템플릿 제공
- PR 템플릿 시스템 및 CLI 도구 구현

## 주요 디렉토리 구조
- `.agent/`: 프로젝트 자체 에이전트 설정 및 문서
- `configs/`: 각 도구별 설정 템플릿
- `templates/`: 프로젝트별 템플릿 (사용자가 복사해서 사용)
- `cli/`: CLI 도구 구현
- `templates/common/`: 공통 템플릿 파일들

## 개발 시 유의사항
- 기존 템플릿 구조와 일관성 유지
- 한국어 주석 및 문서 작성 선호
- 사용자 친화적인 설정 및 초기화 스크립트 제공
- 템플릿 파일은 `.template.md` 확장자 사용
- 프로젝트 자체 설정과 템플릿용 설정을 명확히 구분

## 코딩 스타일
- Python: PEP 8 준수, 타입 힌트 사용
- 일관된 네이밍 컨벤션 유지
- 설정 파일은 YAML, JSON, TOML 형식 지원

## 템플릿 관리
- 템플릿 파일들은 `templates/` 디렉토리에 위치
- 공통 템플릿은 `templates/common/` 에 위치
- 각 템플릿은 독립적으로 사용 가능해야 함

## 작업 원칙
- 대화형 계획 모드 활용
- 단계별 작업 분해 및 실행
- 코드 생성 시 컨텍스트 유지
- 다국어 지원 (한국어/영어) 고려
- 보안 및 모범 사례 준수

## 날짜 사용 지침 (Date Usage Guidelines)
- **항상 현재 날짜 확인**: 문서 작성 시 `date` 명령어로 실제 날짜 확인할 것
- **환경 변수 참조**: `<env>` 태그의 `Today's date` 정보 활용할 것
- **하드코딩 금지**: 날짜를 직접 입력하지 말고 시스템에서 가져올 것
- **파일명 규칙**: `YYYY-MM-DD-feature-name.md` 형식에서 날짜 부분은 실제 날짜 사용할 것
- **신뢰할 수 있는 소스**: Bash의 `date` 명령어나 환경 변수를 사용하여 정확한 날짜 확보할 것

## PRD 작성 규칙 / PRD Writing Rules
- **PRD 우선 작성 필수**: 모든 새로운 기능 개발 전에 반드시 PRD를 대화식으로 작성할 것
- **대화식 PRD 진행**: 사용자와 질문-답변 형식으로 요구사항을 구체화할 것
- **PRD 저장 위치**: 완성된 PRD는 `.agent/prd/` 디렉토리에 저장할 것
- **PRD 파일명 규칙**: `YYYY-MM-DD-feature-name.md` 형식으로 명명할 것
- **다국어 PRD 작성**: PRD 내용도 한국어(영어) 병기로 작성할 것

## PR 작성 시 주의사항
- 반드시 [기여 가이드](.agent/docs/contributing.md)의 PR 작성 규칙을 따를 것
- 코드 변경 시 관련 문서도 함께 업데이트
- 테스트 계획과 체크리스트를 포함할 것
- **다국어 지원 필수**: 모든 문서, PR 내용은 반드시 '한국어(영어)' 형태로 병기할 것
- **결과 검증 필수**: PR 생성/수정 후 반드시 실제 결과를 확인하고 정확히 보고할 것