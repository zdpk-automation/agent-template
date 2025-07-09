# Development History

이 문서는 Agent Template Repository의 개발 과정과 주요 변경사항을 기록합니다.

## 프로젝트 초기 설정

### 2024년 초기 개발
- 기본 프로젝트 구조 설정
- 여러 AI 도구 설정 통합 관리 컨셉 도입
- Claude Code, Gemini CLI, OpenCode 지원 계획

### PR 템플릿 시스템 구축
- 상황별 특화된 PR 템플릿 개발
- 기능개발, 버그수정, 리팩토링 등 다양한 시나리오 지원
- 팀 협업 효율성 향상을 위한 가이드라인 수립

### CLI 도구 개발
- Python 기반 CLI 도구 구현
- 프로젝트 타입별 템플릿 생성 기능
- 자동화된 초기화 스크립트 제공

## 최근 주요 개선사항

### 2024-07-09: AI 에이전트 설정 파일 구조 개선
**배경:** 프로젝트 자체 개발용 설정과 템플릿용 설정이 혼재되어 관리가 어려움

**변경사항:**
1. **통합 지침 시스템 도입**
   - `AGENT.md`: 공통 지침을 담은 중앙 파일
   - 각 도구별 설정 파일은 AGENT.md만 참조하도록 단순화

2. **파일 구조 재정리**
   ```
   Before:
   /CLAUDE.md (심볼릭 링크)
   /GEMINI.md (프로젝트 자체용)
   /templates/common/CLAUDE.md (템플릿용)
   
   After:
   /AGENT.md (프로젝트 자체용 실제 지침)
   /CLAUDE.md → /templates/common/CLAUDE.md (심볼릭 링크)
   /.gemini/GEMINI.md → /templates/common/GEMINI.md (심볼릭 링크)
   /templates/common/AGENT.md (템플릿용 실제 지침)
   /templates/common/CLAUDE.md (AGENT.md 참조만)
   /templates/common/GEMINI.md (AGENT.md 참조만)
   ```

3. **중복 제거 및 유지보수성 향상**
   - 공통 내용은 AGENT.md에서 일괄 관리
   - 각 도구별 특화 지침은 최소화
   - 템플릿과 프로젝트 설정의 명확한 분리

**효과:**
- 설정 파일 관리 복잡도 감소
- 일관된 지침 제공
- 새로운 AI 도구 추가 시 확장성 향상

## 향후 계획

### 단기 목표
- [ ] 더 많은 프로젝트 타입 템플릿 추가
- [ ] 자동화 스크립트 개선
- [ ] 사용자 경험 개선

### 장기 목표
- [ ] 웹 기반 설정 관리 도구
- [ ] 팀 단위 설정 공유 시스템
- [ ] CI/CD 통합 기능

## 버전 관리

각 주요 변경사항은 Git 태그로 관리하며, 다음 형식을 따릅니다:
- `v1.0.0`: 메이저 버전 (구조적 변경)
- `v1.1.0`: 마이너 버전 (기능 추가)
- `v1.1.1`: 패치 버전 (버그 수정)

## 기여자

이 프로젝트에 기여한 모든 개발자들에게 감사합니다.
기여 방법은 [CONTRIBUTING.md](./contributing.md)를 참고하세요.