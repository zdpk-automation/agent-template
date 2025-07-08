## Summary / 요약
- 에이전트 템플릿 구조를 모듈화하고 CLI 친화적으로 리팩토링했습니다. (Refactored the agent template structure to be more modular and CLI-friendly.)
- 전용 CLI 도구로 대체될 레거시 스크립트(`init.sh`, `setup-pr-templates.sh`)를 제거했습니다. (Removed legacy scripts (`init.sh`, `setup-pr-templates.sh`) that will be replaced by a dedicated CLI tool.)
- 중복을 줄이기 위해 공유 에이전트 지침을 위한 중앙 `common/AGENTS.md`를 도입했습니다. (Introduced a central `common/AGENTS.md` for shared agent instructions, reducing duplication.)
- 사용자별 구성을 위해 각 프로젝트 템플릿에 `custom.template.md`를 추가했습니다. (Added `custom.template.md` to each project template for user-specific configurations.)
- AI 도구 구성에 대한 문서를 업데이트하고 추가했습니다. (Updated and added documentation for AI tools configuration.)

## Problem/Motivation / 문제 및 동기
이전 템플릿 구조는 모놀리식이었고 유지보수가 어렵고 크로스 플랫폼 사용에 이상적이지 않은 쉘 스크립트를 포함했습니다. 에이전트 지침은 여러 템플릿에 걸쳐 분산되고 중복되어 공통 구성을 관리하기 어려웠습니다. (The previous template structure was monolithic and included shell scripts that were difficult to maintain and not ideal for cross-platform use. The agent instructions were scattered and duplicated across different templates, making it hard to manage common configurations.)

## Solution / 해결방법
- **CLI 우선 접근 방식 (CLI-First Approach):** 프로젝트 초기화 및 설정을 처리할 미래의 CLI 도구를 위해 쉘 스크립트를 제거했습니다. (Removed shell scripts in favor of a future CLI tool that will handle project initialization and setup.)
- **중앙 집중식 에이전트 지침 (Centralized Agent Instructions):** 모든 에이전트 유형에 적용 가능한 기본 지침을 저장하기 위해 `templates/common/AGENTS.md`를 생성했습니다. 이제 템플릿별 `AGENTS.md` 파일은 공통 파일에서 상속받아 유지보수를 간소화합니다. (Created a `templates/common/AGENTS.md` to store base instructions applicable to all agent types. Template-specific `AGENTS.md` files now inherit from the common file, simplifying maintenance.)
- **사용자별 사용자 정의 (User-Specific Customization):** 각 템플릿 디렉토리에 `custom.template.md`를 추가하여 사용자가 핵심 템플릿을 수정하지 않고도 자신만의 지침을 추가할 수 있도록 했습니다. (Added `custom.template.md` in each template directory, allowing users to add their own instructions without modifying the core templates.)
- **표준화 (Standardization):** 새로운 구조는 더 체계적이고 확장 가능하여 새로운 템플릿을 추가하고 기존 템플릿을 유지보수하기 쉽게 만듭니다. (The new structure is more organized and scalable, making it easier to add new templates and maintain existing ones.)

### Key Changes / 주요 변경사항
- **삭제됨 (Deleted):** `scripts/init.sh`, `scripts/setup-pr-templates.sh`
- **생성됨 (Created):** `templates/common/AGENTS.md`, `templates/backend/custom.template.md`, `templates/frontend/custom.template.md`, `templates/web-project/custom.template.md`, `docs/ai-tools-config-reference.md`
- **수정됨 (Modified):** `.gemini/GEMINI.md`, `templates/backend/AGENTS.md`, `templates/frontend/AGENTS.md`, `templates/web-project/AGENTS.md`

## Test Plan / 테스트 계획
- [x] 새 디렉토리 구조의 수동 확인. (Manual verification of the new directory structure.)
- [ ] 새 CLI 도구는 제거된 스크립트의 기능을 다루기 위한 자체 전용 테스트를 가질 것입니다. (The new CLI tool will have its own dedicated tests to cover the functionality of the removed scripts.)
- [ ] 기존 템플릿이 새 구조로 성공적으로 로드되고 테스트되었습니다. (Existing templates have been successfully loaded and tested with the new structure.)

## Breaking Changes / 호환성 변경
- `init.sh` 및 `setup-pr-templates.sh` 스크립트가 제거되었습니다. 사용자는 이제 프로젝트 설정을 위해 곧 출시될 CLI 도구에 의존해야 합니다. (The `init.sh` and `setup-pr-templates.sh` scripts have been removed. Users must now rely on the forthcoming CLI tool for project setup.)

## Checklist / 체크리스트
- [x] 코드 스타일 가이드 준수 (Code style guide compliance)
- [ ] 테스트 커버리지 확인 (Test coverage verified)
- [x] 문서 업데이트 (필요한 경우) (Documentation updated (if needed))
- [ ] 보안 취약점 검토 (Security review completed)
- [ ] 성능 영향 분석 (Performance impact analyzed)
- [x] 핵심 변경사항 코드블록으로 표시 (Key changes highlighted with code blocks)
