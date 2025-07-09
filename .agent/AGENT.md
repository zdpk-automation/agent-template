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

## PR 작성 시 주의사항
- 반드시 [기여 가이드](.agent/docs/contributing.md)의 PR 작성 규칙을 따를 것
- **PR 최소 단위 원칙**: 하나의 PR은 하나의 완전한 기능만 포함할 것
- **필수 분할 기준**: 다음 경우 반드시 별도 PR로 분할
  - 서로 다른 모듈/컴포넌트 변경
  - 기능 추가 + 리팩토링 혼재  
  - 인프라 변경 + 비즈니스 로직 변경
  - 의존성 추가 + 기능 구현
- **다국어 지원 필수**: 
  - PR 제목: `feat: Add feature / 기능 추가` 형태로 병기
  - 섹션 제목: `## Summary / 요약` 형태로 병기
  - 핵심 내용: 영어 설명 후 한국어 설명 병기
- 코드 변경 시 관련 문서도 함께 업데이트
- 테스트 계획과 체크리스트를 포함할 것