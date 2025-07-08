## Summary / 요약
• 에이전트 템플릿 구조를 모듈화하고 CLI 친화적으로 리팩토링했습니다. (Refactored agent template structure for modularity and CLI-friendliness.)
• 레거시 스크립트를 제거하고 CLI 기반 프로젝트 설정을 위한 기반을 마련했습니다. (Removed legacy scripts and laid groundwork for CLI-based project setup.)
• 중앙 집중식 에이전트 지침 및 사용자 정의 템플릿을 도입했습니다. (Introduced centralized agent instructions and custom templates.)
• PR 템플릿 시스템 및 가이드라인을 강화하고, AI 도구 관련 문서를 업데이트했습니다. (Enhanced PR template system and guidelines, and updated AI tool documentation.)
• GitHub Actions 워크플로우 및 CLI 에이전트 도구를 추가하여 자동화된 릴리스 및 프로젝트 관리를 지원합니다. (Added GitHub Actions workflows and CLI agent tools to support automated releases and project management.)

## Problem/Motivation / 문제 및 동기

**English:**
The previous template structure was monolithic and difficult to maintain, with scattered and duplicated agent instructions. Project setup scripts were inefficient, and there was a lack of comprehensive PR guidelines. The overall development workflow lacked automation and standardization for AI tool configurations.

**한국어:**
이전 템플릿 구조는 모놀리식이었고 유지보수가 어려웠으며, 에이전트 지침이 분산되고 중복되어 있었습니다. 프로젝트 설정 스크립트는 비효율적이었고, 포괄적인 PR 가이드라인이 부족했습니다. 전반적인 개발 워크플로우는 AI 도구 구성에 대한 자동화 및 표준화가 부족했습니다.

## Solution / 해결방법

**English:**
Implemented a comprehensive template system for managing AI tool configurations, including a modular agent template structure, CLI-based setup transition, enhanced PR guidelines, and new project templates with automation tools.

**한국어:**
AI 도구 구성을 관리하기 위한 포괄적인 템플릿 시스템을 구현했습니다. 여기에는 모듈화된 에이전트 템플릿 구조, CLI 기반 설정 전환, 강화된 PR 가이드라인, 그리고 자동화 도구를 포함한 새로운 프로젝트 템플릿이 포함됩니다.

### Implementation Details / 구현 세부사항
```typescript
// 주요 구조적 변경사항은 다음과 같습니다:
// - `templates/common/AGENTS.md` 생성: 공유 에이전트 지침을 중앙 집중화합니다.
// - `custom.template.md` 도입: 각 프로젝트 템플릿에 사용자별 구성을 허용합니다.
// - 레거시 스크립트 제거: `scripts/init.sh`, `scripts/setup-pr-templates.sh`가 제거되고 CLI 도구로 대체됩니다.
// - `.gemini/settings.json` 추가: Gemini CLI 구성을 위한 설정 파일입니다.
// - `templates/backend`, `templates/frontend`, `templates/web-project` 등 새로운 프로젝트 템플릿 추가.
// - `.github/workflows`에 GitHub Actions 워크플로우 추가: 자동화된 릴리스를 지원합니다.
```

### API Changes / API 변경사항
```typescript
// 이 PR에서는 직접적인 API 변경사항(새로운 엔드포인트 또는 메서드)이 도입되지 않았습니다.
// 변경사항은 주로 구조적이며 CLI 도구 및 프로젝트 설정과 관련이 있습니다.
```

## User Experience / 사용자 경험

**English:**
Users will experience a more organized and scalable template structure, making it easier to add new templates and maintain existing ones. PR writing efficiency is improved through structured templates and clear guidelines. Project setup will transition to a more streamlined CLI-based approach, and automated releases will simplify deployment.

**한국어:**
사용자는 더 체계적이고 확장 가능한 템플릿 구조를 경험하게 될 것입니다. 새로운 템플릿을 추가하고 기존 템플릿을 유지보수하기가 더 쉬워집니다. 구조화된 템플릿과 명확한 가이드라인을 통해 PR 작성 효율성이 향상됩니다. 프로젝트 설정은 더욱 간소화된 CLI 기반 접근 방식으로 전환될 예정이며, 자동화된 릴리스는 배포를 간소화할 것입니다.

## Test Plan / 테스트 계획
- [x] 새 디렉토리 구조 및 템플릿의 수동 확인. (Manual verification of new directory structure and templates.)
- [ ] CLI 도구 및 PR 템플릿 시스템의 기능 테스트. (Functional testing of CLI tools and PR template system.)
- [ ] 제거된 스크립트의 기능이 새 CLI 도구에서 올바르게 작동하는지 확인. (Verify that the functionality of removed scripts works correctly in the new CLI tool.)
- [ ] GitHub Actions 워크플로우 테스트. (Test GitHub Actions workflows.)

## Breaking Changes / 호환성 변경
⚠️ `init.sh` 및 `setup-pr-templates.sh` 스크립트가 제거되어, 프로젝트 설정 방식이 변경되었습니다. 사용자는 이제 곧 출시될 CLI 도구에 의존해야 합니다. (The `init.sh` and `setup-pr-templates.sh` scripts have been removed, changing the project setup method. Users must now rely on the forthcoming CLI tool.)

## Key Code Changes / 핵심 코드 변경사항
```diff
--- a/scripts/init.sh
+++ /dev/null
@@ -1,20 +0,0 @@
-# Legacy script removed
```
```diff
--- a/templates/backend/AGENTS.md
+++ b/templates/backend/AGENTS.md
@@ -1,5 +1,7 @@
 # Backend Agent Instructions
 
-This is a placeholder for backend-specific agent instructions.
-You can add details about backend frameworks, database interactions, etc.
+
+This file contains instructions specific to the backend agent.
+It extends the common agent instructions found in `common/AGENTS.md`.
+
+## Backend-Specific Directives
+*   **Framework**: Node.js with Express.js
+*   **Database**: PostgreSQL (managed via Docker Compose)
+*   **Authentication**: Google OAuth (planned)
```
```typescript
// New file: .gemini/settings.json
{
  "mcpServers": {
    "github": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "GITHUB_PERSONAL_ACCESS_TOKEN",
        "ghcr.io/github/github-mcp-server"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": ""
      }
    }
  }
}
```

## Screenshots / 스크린샷
<!-- UI 변경사항: Before/After 스크린샷 -->
<!-- UI changes: Before/After screenshots -->
N/A (No direct UI changes)

## Performance Impact / 성능 영향

**English:**
Negligible performance impact. The changes are primarily structural and related to development workflow, not runtime performance of applications.

**한국어:**
성능에 미치는 영향은 미미합니다. 변경사항은 주로 구조적이며 개발 워크플로우와 관련이 있으며, 애플리케이션의 런타임 성능에는 영향을 주지 않습니다.

## Dependencies / 의존성

**English:**
No new external library dependencies are introduced at the project root level. The changes involve internal project structure and CLI tools.

**한국어:**
프로젝트 루트 수준에서 새로운 외부 라이브러리 의존성은 도입되지 않습니다. 변경사항은 내부 프로젝트 구조 및 CLI 도구와 관련이 있습니다.

## Additional Notes / 추가 정보

**English:**
This PR lays the foundation for a more standardized and automated development environment for AI tools. Future work will involve implementing the dedicated CLI tool to replace the removed scripts.

**한국어:**
이 PR은 AI 도구를 위한 보다 표준화되고 자동화된 개발 환경의 기반을 마련합니다. 향후 작업에는 제거된 스크립트를 대체할 전용 CLI 도구 구현이 포함될 것입니다.

## Checklist / 체크리스트
- [ ] 기능 요구사항 충족 확인 (Verify functional requirements are met)
- [ ] 코드 스타일 가이드 준수 (Code style guide compliance)
- [ ] 테스트 커버리지 확인 (Test coverage verified)
- [ ] 문서 업데이트 (필요한 경우) (Documentation updated (if needed))
- [ ] 보안 검토 완료 (Security review completed)
- [ ] 성능 영향 분석 (Performance impact analyzed)
- [ ] 핵심 변경사항 코드블록으로 표시 (Key changes highlighted with code blocks)
- [ ] 다국어 설명 제공 (Bilingual descriptions provided)