# Claude Code Agent Configuration

## 공통 지침 참조 (Referencing Common Guidelines)
이 문서는 `templates/common/AGENTS.md`에 명시된 공통 지침을 따릅니다.

## 프로젝트 설정

### 언어 및 프레임워크
- 주 언어: TypeScript/JavaScript
- 프레임워크: React, Next.js, Node.js
- 패키지 매니저: npm/yarn/pnpm

### 코딩 스타일
- ESLint + Prettier 사용
- 함수형 프로그래밍 선호
- TypeScript strict mode 활성화

### 테스트 전략
- 단위 테스트: Jest/Vitest
- E2E 테스트: Playwright/Cypress
- 커버리지 목표: 80% 이상

### 빌드 및 배포
- 빌드 명령어: `npm run build`
- 테스트 명령어: `npm test`
- 린트 명령어: `npm run lint`
- 타입 체크: `npm run typecheck`

## Claude 사용 가이드

### 일반적인 작업 패턴
1. 코드 분석 및 이해
2. 기능 구현
3. 테스트 작성
4. 리팩토링
5. 문서화

### 선호하는 응답 스타일
- 간결하고 실용적인 답변
- 코드 예제 포함
- 단계별 설명
- 베스트 프랙티스 제안
