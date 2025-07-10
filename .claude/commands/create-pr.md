---
allowed-tools: Bash, Read, LS, Glob
description: Create a properly formatted bilingual PR following project guidelines
---

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

## Implementation

Please check current git status and create a properly formatted PR:

```bash
# Check current git status
echo "📊 Checking git status..."
git status

echo ""
echo "📋 Checking staged changes..."
git diff --cached --stat

echo ""
echo "📝 Checking uncommitted changes..."
git diff --stat

echo ""
echo "🔍 Analyzing recent commits on current branch..."
git log --oneline -5

echo ""
echo "📏 Checking if changes meet PR guidelines..."
echo "Current branch: $(git branch --show-current)"

# Get current branch name
CURRENT_BRANCH=$(git branch --show-current)

# Check if there are uncommitted changes
if [[ -n $(git status --porcelain) ]]; then
    echo "⚠️  You have uncommitted changes. Please commit them first before creating a PR."
    exit 1
fi

# Check if current branch is main
if [[ "$CURRENT_BRANCH" == "main" ]]; then
    echo "⚠️  You are on the main branch. Please create a feature branch first."
    exit 1
fi

# Get changes between current branch and main
echo ""
echo "📊 Changes since branching from main:"
git diff main...HEAD --stat

echo ""
echo "🔢 Line count analysis:"
ADDED_LINES=$(git diff main...HEAD --stat | tail -1 | grep -o '[0-9]* insertion' | cut -d' ' -f1)
DELETED_LINES=$(git diff main...HEAD --stat | tail -1 | grep -o '[0-9]* deletion' | cut -d' ' -f1)
FILES_CHANGED=$(git diff main...HEAD --name-only | wc -l)

echo "Files changed: $FILES_CHANGED"
echo "Lines added: ${ADDED_LINES:-0}"
echo "Lines deleted: ${DELETED_LINES:-0}"

# Check PR size guidelines
if [[ $FILES_CHANGED -gt 15 ]]; then
    echo "⚠️  Warning: More than 15 files changed. Consider splitting this PR."
fi

TOTAL_LINES=$((${ADDED_LINES:-0} + ${DELETED_LINES:-0}))
if [[ $TOTAL_LINES -gt 800 ]]; then
    echo "⚠️  Warning: More than 800 lines changed. Consider splitting this PR."
fi

echo ""
echo "✅ Basic PR validation complete!"
echo "💡 Please review the changes and use the 'gh pr create' command manually with proper bilingual title and description."
echo ""
echo "🏷️  Suggested PR title format:"
echo "   [type]: [English description] / [Korean description]"
echo ""
echo "📝 Required sections in PR description:"
echo "   ## Summary / 요약"
echo "   ## Problem / 문제점"
echo "   ## Solution / 해결방법"
echo "   ## Test Plan / 테스트 계획"
echo ""
echo "👨‍💻 Create PR command:"
echo "   gh pr create --title \"[your-title]\" --body \"[your-description]\""
```