# PR 템플릿 사용 가이드

## 개요

이 가이드는 agent-template에서 제공하는 PR 템플릿들을 효과적으로 활용하는 방법을 설명합니다.

## 제공되는 템플릿

### 1. 기본 템플릿 (Default)
- **파일**: `.github/pull_request_template.md`
- **용도**: 모든 일반적인 PR에 사용
- **특징**: 간결하면서도 필수 정보를 모두 포함

### 2. 기능 개발 템플릿 (Feature)
- **파일**: `.github/PULL_REQUEST_TEMPLATE/feature.md`
- **용도**: 새로운 기능 추가 시 사용
- **특징**: 사용자 경험, 성능 영향, 스크린샷 섹션 포함

### 3. 버그 수정 템플릿 (Bugfix)
- **파일**: `.github/PULL_REQUEST_TEMPLATE/bugfix.md`
- **용도**: 버그 수정 시 사용
- **특징**: 버그 재현 방법, 근본 원인 분석, 위험도 평가 포함

### 4. 리팩토링 템플릿 (Refactor)
- **파일**: `.github/PULL_REQUEST_TEMPLATE/refactor.md`
- **용도**: 코드 리팩토링 시 사용
- **특징**: 개선사항, 성능 비교, 동작 변경 없음 확인 포함

### 5. 핫픽스 템플릿 (Hotfix)
- **파일**: `.github/PULL_REQUEST_TEMPLATE/hotfix.md`
- **용도**: 긴급 수정 시 사용
- **특징**: 인시던트 정보, 영향도 분석, 롤백 계획 포함

### 6. 문서 템플릿 (Docs)
- **파일**: `.github/PULL_REQUEST_TEMPLATE/docs.md`
- **용도**: 문서 변경 시 사용
- **특징**: 문서 유형, 대상 독자, 검증 방법 포함

## 설치 방법

### 자동 설치 (권장)

```bash
# 기본 템플릿만 설치
curl -sSL https://raw.githubusercontent.com/zdpk-automation/agent-template/main/scripts/setup-pr-templates.sh | bash

# 특정 템플릿 설치
curl -sSL https://raw.githubusercontent.com/zdpk-automation/agent-template/main/scripts/setup-pr-templates.sh | bash -s -- --type feature

# 모든 템플릿 설치
curl -sSL https://raw.githubusercontent.com/zdpk-automation/agent-template/main/scripts/setup-pr-templates.sh | bash -s -- --type all
```

### 수동 설치

```bash
# 저장소 클론
git clone https://github.com/zdpk-automation/agent-template.git

# 기본 템플릿 복사
cp agent-template/.github/pull_request_template.md .github/

# 특정 템플릿들 복사
mkdir -p .github/PULL_REQUEST_TEMPLATE
cp agent-template/templates/pr-templates/*.md .github/PULL_REQUEST_TEMPLATE/
```

## 사용 방법

### 기본 템플릿 사용
기본 템플릿이 설치되어 있으면 PR 생성 시 자동으로 적용됩니다.

### 특정 템플릿 사용
URL 파라미터를 사용하여 특정 템플릿을 선택할 수 있습니다:

```
https://github.com/your-org/your-repo/compare/main...feature-branch?template=feature.md
```

### GitHub CLI 사용
```bash
# 기본 템플릿으로 PR 생성
gh pr create

# 특정 템플릿으로 PR 생성
gh pr create --body-file .github/PULL_REQUEST_TEMPLATE/feature.md
```

## 템플릿 커스터마이징

### 프로젝트별 수정
각 프로젝트의 특성에 맞게 템플릿을 수정할 수 있습니다:

```bash
# 기본 템플릿 수정
vim .github/pull_request_template.md

# 특정 템플릿 수정
vim .github/PULL_REQUEST_TEMPLATE/feature.md
```

### 섹션 추가/제거
프로젝트 요구사항에 따라 섹션을 추가하거나 제거할 수 있습니다:

```markdown
## Custom Section
<!-- 프로젝트 특화 섹션 -->

## Database Changes
<!-- 데이터베이스 변경사항이 있는 경우 -->
- [ ] 마이그레이션 스크립트 작성
- [ ] 백업 계획 수립
```

## 팀별 활용 예시

### 웹 프론트엔드 팀
```markdown
## Browser Compatibility
- [ ] Chrome 최신 버전
- [ ] Firefox 최신 버전
- [ ] Safari 최신 버전
- [ ] Edge 최신 버전

## Accessibility
- [ ] 스크린 리더 테스트
- [ ] 키보드 네비게이션 테스트
- [ ] 색상 대비 확인
```

### 백엔드 API 팀
```markdown
## API Changes
- [ ] API 문서 업데이트
- [ ] 버전 호환성 확인
- [ ] 성능 벤치마크 실행

## Database Impact
- [ ] 마이그레이션 필요 여부
- [ ] 인덱스 영향 분석
- [ ] 쿼리 성능 테스트
```

### 모바일 앱 팀
```markdown
## Platform Testing
- [ ] iOS 테스트 완료
- [ ] Android 테스트 완료
- [ ] 다양한 화면 크기 테스트

## App Store Guidelines
- [ ] iOS App Store 가이드라인 준수
- [ ] Google Play Store 정책 준수
```

## 자동화 통합

### GitHub Actions와 연동
```yaml
name: PR Template Validation
on:
  pull_request:
    types: [opened, edited]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Check PR Template
        run: |
          if [[ "${{ github.event.pull_request.body }}" == *"## Summary"* ]]; then
            echo "✅ PR template used correctly"
          else
            echo "❌ Please use the PR template"
            exit 1
          fi
```

### PR 체크리스트 자동 검증
```yaml
- name: Validate Checklist
  run: |
    checklist_items=$(echo "${{ github.event.pull_request.body }}" | grep -c "\- \[x\]")
    if [ $checklist_items -lt 3 ]; then
      echo "❌ Please complete at least 3 checklist items"
      exit 1
    fi
```

## 모범 사례

### 1. 템플릿 선택 가이드
- **Feature**: 새로운 기능, UI 변경, API 추가
- **Bugfix**: 버그 수정, 오류 해결
- **Refactor**: 코드 개선, 성능 최적화 (동작 변경 없음)
- **Hotfix**: 긴급 수정, 프로덕션 이슈 해결
- **Docs**: 문서 업데이트, README 수정

### 2. 작성 팁
- **구체적으로 작성**: "버그 수정" → "로그인 시 세션 만료 오류 수정"
- **체크리스트 활용**: 빠뜨리기 쉬운 작업들을 체크리스트로 관리
- **스크린샷 첨부**: UI 변경사항은 반드시 스크린샷 포함
- **테스트 계획 상세화**: 어떻게 테스트했는지 구체적으로 명시

### 3. 리뷰어를 위한 배려
- **변경 이유 설명**: 왜 이렇게 구현했는지 배경 설명
- **주의사항 명시**: 특별히 확인해야 할 부분 하이라이트
- **관련 이슈 링크**: 관련된 이슈나 PR 번호 포함

## 문제 해결

### 템플릿이 적용되지 않는 경우
1. 파일 경로 확인: `.github/pull_request_template.md`
2. 파일 권한 확인: 읽기 권한 있는지 확인
3. 브라우저 캐시 삭제 후 재시도

### 특정 템플릿 사용 시 오류
1. 파일명 확인: `feature.md`, `bugfix.md` 등
2. URL 파라미터 확인: `?template=feature.md`
3. 파일 인코딩 확인: UTF-8로 저장되어 있는지 확인

### 템플릿 업데이트
```bash
# 최신 템플릿으로 업데이트
curl -sSL https://raw.githubusercontent.com/zdpk-automation/agent-template/main/scripts/setup-pr-templates.sh | bash -s -- --type all --force
```

## 추가 리소스

- [GitHub PR 템플릿 공식 문서](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository)
- [PR 작성 가이드](./pr-guidelines.md)
- [코드 리뷰 베스트 프랙티스](./code-review-guide.md)