## Summary / 요약
<!-- 새로운 기능의 핵심 내용을 3-5개 불릿 포인트로 요약 -->
<!-- Summarize the new feature in 3-5 bullet points -->
• 
• 
• 

## Problem/Motivation / 문제 및 동기
<!-- 이 기능이 왜 필요한지, 어떤 사용자 문제를 해결하는지 설명 -->
<!-- Explain why this feature is needed and what user problem it solves -->

**English:**


**한국어:**


## Solution / 해결방법
<!-- 기능을 어떻게 구현했는지, 주요 설계 결정사항 설명 -->
<!-- Explain how you implemented the feature and key design decisions -->

### Implementation Details / 구현 세부사항
```typescript
// Key interfaces or types added
interface NewFeature {
  id: string;
  name: string;
  config: FeatureConfig;
}
```

### API Changes / API 변경사항
```typescript
// New endpoints or methods
export const createFeature = async (data: CreateFeatureRequest): Promise<Feature> => {
  // Implementation
};
```

## User Experience / 사용자 경험
<!-- 사용자 관점에서 어떻게 동작하는지 설명 -->
<!-- Describe how it works from the user's perspective -->


## Test Plan
- [ ] 단위 테스트 추가
- [ ] 통합 테스트 실행
- [ ] 사용자 시나리오 테스트
- [ ] 접근성 테스트 (UI 기능인 경우)
- [ ] 다양한 브라우저/디바이스 테스트 (필요한 경우)

## Screenshots/Demo
<!-- 새로운 기능의 스크린샷이나 데모 GIF 첨부 -->

## Performance Impact
<!-- 성능에 미치는 영향 분석 -->

## Breaking Changes
⚠️ 없음

## Documentation
<!-- 업데이트된 문서나 새로 작성된 문서 링크 -->

## Checklist
- [ ] 기능 요구사항 충족 확인
- [ ] 코드 스타일 가이드 준수
- [ ] 테스트 커버리지 80% 이상
- [ ] 사용자 문서 업데이트
- [ ] API 문서 업데이트 (필요한 경우)
- [ ] 보안 검토 완료