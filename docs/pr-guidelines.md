# Pull Request 작성 가이드

## 개요

효과적이고 이해하기 쉬운 Pull Request를 작성하기 위한 종합 가이드입니다. 이 가이드를 따르면 코드 리뷰어가 변경사항을 빠르게 이해하고 효율적으로 리뷰할 수 있습니다.

## PR 작성 원칙

### 1. 명확성 (Clarity)
- **목적이 명확해야 함**: 무엇을, 왜 변경했는지 분명히 설명
- **간결하면서도 충분한 정보 제공**: 불필요한 내용은 제외하되 필요한 정보는 누락하지 않음
- **기술적 배경이 다른 사람도 이해할 수 있도록 작성**

### 2. 구조화 (Structure)
- **일관된 템플릿 사용**: 프로젝트별 표준 템플릿 활용
- **논리적 순서**: 문제 → 해결방법 → 결과 순으로 설명
- **시각적 구분**: 섹션별로 명확히 구분

### 3. 완전성 (Completeness)
- **테스트 계획 포함**: 어떻게 검증할 것인지 명시
- **영향 범위 설명**: 변경이 미치는 영향 분석
- **후속 작업 언급**: 필요한 경우 추가 작업 계획

## PR 제목 작성법

### 형식
```
[타입] 간결한 변경사항 요약 (50자 이내)
```

### 타입 분류
- `feat`: 새로운 기능 추가
- `fix`: 버그 수정
- `docs`: 문서 변경
- `style`: 코드 포맷팅, 세미콜론 누락 등
- `refactor`: 코드 리팩토링
- `test`: 테스트 추가 또는 수정
- `chore`: 빌드 프로세스, 도구 설정 등

### 좋은 예시
```
feat: Add user authentication with JWT
fix: Resolve memory leak in data processing
docs: Update API documentation for v2.0
refactor: Simplify user service logic
```

### 나쁜 예시
```
Update stuff
Fix bug
Changes
WIP
```

## PR 본문 구조

### 필수 섹션

#### 1. Summary (요약)
```markdown
## Summary
• 핵심 변경사항을 3-5개 불릿 포인트로 요약
• 각 포인트는 구체적이고 측정 가능한 내용
• 비기술적 배경을 가진 사람도 이해할 수 있도록 작성
```

#### 2. Problem/Motivation (문제/동기)
```markdown
## Problem
현재 상황의 문제점이나 개선이 필요한 이유를 설명:
- 구체적인 문제 상황
- 사용자에게 미치는 영향
- 비즈니스적 필요성
```

#### 3. Solution (해결방법)
```markdown
## Solution
문제를 어떻게 해결했는지 설명:
- 선택한 접근 방법과 이유
- 대안들과 비교한 장단점
- 핵심 구현 내용
```

#### 4. Test Plan (테스트 계획)
```markdown
## Test Plan
변경사항을 어떻게 검증할 것인지:
- [ ] 단위 테스트 추가/수정
- [ ] 통합 테스트 실행
- [ ] 수동 테스트 시나리오
- [ ] 성능 테스트 (필요한 경우)
```

### 선택적 섹션

#### 5. Breaking Changes (호환성 변경)
```markdown
## Breaking Changes
⚠️ 기존 코드와 호환되지 않는 변경사항:
- 변경된 API 인터페이스
- 마이그레이션 가이드
- 영향받는 컴포넌트/서비스
```

#### 6. Screenshots/Demo (스크린샷/데모)
```markdown
## Screenshots
UI 변경이 있는 경우:
- Before/After 스크린샷
- 새로운 기능 데모 GIF
- 다양한 화면 크기에서의 테스트 결과
```

#### 7. Performance Impact (성능 영향)
```markdown
## Performance Impact
성능에 영향을 주는 변경사항:
- 벤치마크 결과
- 메모리 사용량 변화
- 응답 시간 개선/악화
```

#### 8. Dependencies (의존성)
```markdown
## Dependencies
새로운 의존성이나 버전 업데이트:
- 추가된 라이브러리와 선택 이유
- 업데이트된 패키지와 변경사항
- 보안 취약점 해결
```

## PR 크기 가이드

### 이상적인 PR 크기
- **라인 수**: 200-400줄 (최대 800줄)
- **파일 수**: 5-10개 파일
- **리뷰 시간**: 30분 이내

### 큰 PR을 나누는 방법
1. **기능별 분할**: 독립적인 기능은 별도 PR로
2. **단계별 분할**: 준비 → 구현 → 테스트 → 문서화
3. **파일별 분할**: 관련 없는 파일 변경은 분리

## 코드 리뷰 고려사항

### 리뷰어를 위한 배려
- **변경 이유 설명**: 코드만 보고 이해하기 어려운 부분은 주석으로 설명
- **핵심 변경사항 하이라이트**: 특히 주의 깊게 봐야 할 부분 명시
- **테스트 방법 제공**: 로컬에서 테스트할 수 있는 방법 안내

### 자가 검토 체크리스트
- [ ] 코드 스타일 가이드 준수
- [ ] 테스트 커버리지 확인
- [ ] 문서 업데이트 (필요한 경우)
- [ ] 보안 취약점 검토
- [ ] 성능 영향 분석

## 특수 상황별 가이드

### 1. 핫픽스 (Hotfix)
```markdown
## 🚨 Hotfix: [문제 요약]

### Incident
- 발생 시간: YYYY-MM-DD HH:MM
- 영향 범위: 사용자/시스템 영향도
- 긴급도: Critical/High/Medium

### Root Cause
문제의 근본 원인

### Fix
최소한의 변경으로 문제 해결

### Verification
- [ ] 프로덕션 환경에서 테스트 완료
- [ ] 모니터링 지표 정상화 확인
```

### 2. 실험적 기능 (Experimental)
```markdown
## 🧪 Experimental: [기능명]

### Hypothesis
가설과 검증하고자 하는 내용

### Implementation
실험을 위한 구현 방법

### Metrics
성공/실패를 판단할 지표

### Rollback Plan
실험 실패 시 롤백 계획
```

### 3. 리팩토링 (Refactoring)
```markdown
## ♻️ Refactor: [대상 컴포넌트/모듈]

### Current Issues
현재 코드의 문제점

### Improvements
개선된 점들:
- 가독성 향상
- 성능 개선
- 유지보수성 증대

### Behavior Changes
⚠️ 동작 변경사항 (없어야 함)
```

## 자동화 도구 활용

### GitHub Templates
`.github/pull_request_template.md` 파일로 기본 템플릿 설정

### PR 체크리스트
```markdown
## Checklist
- [ ] 코드 리뷰 완료
- [ ] 테스트 통과
- [ ] 문서 업데이트
- [ ] 보안 검토
- [ ] 성능 테스트
```

### 라벨 활용
- `breaking-change`: 호환성 변경
- `needs-documentation`: 문서 업데이트 필요
- `performance`: 성능 관련 변경
- `security`: 보안 관련 변경

## 팀별 커스터마이징

### 프로젝트 특성 반영
- **웹 프론트엔드**: 브라우저 호환성, 접근성 체크리스트
- **백엔드 API**: API 문서 업데이트, 데이터베이스 마이그레이션
- **모바일**: 플랫폼별 테스트, 앱스토어 가이드라인 준수
- **데이터**: 데이터 품질, 개인정보 보호 고려사항

### 팀 문화 반영
- **코드 리뷰 문화**: 건설적 피드백, 학습 기회 제공
- **커뮤니케이션 스타일**: 공식적/비공식적 톤앤매너
- **의사결정 프로세스**: 승인 권한, 리뷰어 지정 규칙

## 예시 템플릿

### 기본 템플릿
```markdown
## Summary
• 

## Problem


## Solution


## Test Plan
- [ ] 
- [ ] 
- [ ] 

## Checklist
- [ ] 코드 리뷰 완료
- [ ] 테스트 통과
- [ ] 문서 업데이트 (필요한 경우)
```

### 상세 템플릿
```markdown
## Summary
• 
• 
• 

## Problem/Motivation


## Solution


## Test Plan
- [ ] 단위 테스트 추가/수정
- [ ] 통합 테스트 실행
- [ ] 수동 테스트 완료
- [ ] 성능 테스트 (필요한 경우)

## Breaking Changes
⚠️ 없음 / 다음 변경사항들:


## Screenshots
<!-- UI 변경이 있는 경우 Before/After 스크린샷 -->

## Performance Impact
<!-- 성능에 영향을 주는 경우 벤치마크 결과 -->

## Dependencies
<!-- 새로운 의존성이나 버전 업데이트가 있는 경우 -->

## Additional Notes
<!-- 기타 리뷰어가 알아야 할 정보 -->

## Checklist
- [ ] 코드 스타일 가이드 준수
- [ ] 테스트 커버리지 확인
- [ ] 문서 업데이트 (필요한 경우)
- [ ] 보안 취약점 검토
- [ ] 성능 영향 분석
```