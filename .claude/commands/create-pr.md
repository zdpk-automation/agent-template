# Create PR Command

Create a properly formatted bilingual PR following project guidelines.

## Instructions

Create a PR with the following requirements:

### 1. Title Format / 제목 형식
- Use Korean(English) bilingual format: `feat: Add feature / 기능 추가`
- Include proper commit type (feat, fix, docs, refactor, test, chore)
- Keep title under 50 characters for the English part

### 2. Required Sections / 필수 섹션
All PRs must include these bilingual sections:
- `## Summary / 요약` - Key changes in bullet points
- `## Problem / 문제점` - What problem this solves  
- `## Solution / 해결방법` - How the problem was solved
- `## Test Plan / 테스트 계획` - How changes were verified

### 3. Bilingual Content Guidelines / 이중 언어 내용 가이드라인
- **Section headers**: Always use `## English / 한국어` format
- **Bullet points**: Use `• English description / 한국어 설명` format
- **Key changes**: Highlight important changes in both languages
- **Code blocks**: Use code blocks to show important changes

### 4. PR Validation Checks / PR 검증 확인사항
Before creating PR, validate:
- **Single Responsibility**: One complete feature or fix only
- **No Mixed Types**: Don't mix feat+docs, infrastructure+business logic, etc.
- **Size Guidelines**: Keep under 800 lines, 15 files maximum
- **Dependencies**: If adding dependencies, make it a separate PR

### 5. Process / 프로세스
1. Check current git status and uncommitted changes
2. Analyze changes for split requirements per `.agent/docs/pr-guidelines.md`
3. If changes need splitting, suggest how to split first
4. If changes are appropriate for single PR, create properly formatted PR
5. Include relevant code blocks highlighting key changes
6. Add appropriate test plan and checklist

### 6. Required Footer / 필수 푸터
Always end with:
```
🤖 Generated with [Claude Code](https://claude.ai/code)
```

## Reference Documents
- `.agent/docs/pr-guidelines.md` - Comprehensive PR guidelines
- `.agent/AGENT.md` - Project-specific PR requirements

## Examples

### Good PR Title Examples / 좋은 PR 제목 예시
```
feat: Add template management system / 템플릿 관리 시스템 추가
fix: Resolve cache update issue / 캐시 업데이트 문제 해결  
docs: Update PR guidelines with split criteria / 분할 기준이 포함된 PR 가이드라인 업데이트
```

### Bad PR Title Examples / 나쁜 PR 제목 예시
```
feat: Add CLI with all features and docs
Update stuff
Fix bug and add feature
```