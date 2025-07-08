# TEMPLATE INSTRUCTIONS (WEB PROJECT)

## 프로젝트 개요
- **타입**: 웹 애플리케이션
- **주요 기술**: React, TypeScript, Vite
- **스타일링**: CSS Modules / Styled Components
- **상태 관리**: React Context / Zustand
- **테스팅**: Jest, React Testing Library

## 개발 환경 설정

### 빌드 및 개발 명령어
```bash
npm run dev          # 개발 서버 시작
npm run build        # 프로덕션 빌드
npm run test         # 테스트 실행
npm run lint         # 코드 린팅
npm run typecheck    # 타입 체크
```

### 코딩 스타일 가이드
- **들여쓰기**: 2 spaces
- **따옴표**: Single quotes for strings
- **세미콜론**: 항상 사용
- **네이밍**: camelCase for variables, PascalCase for components
- **파일명**: kebab-case for files, PascalCase for components

## 프로젝트 구조
```
src/
├── components/     # 재사용 가능한 컴포넌트
├── pages/         # 페이지 컴포넌트
├── hooks/         # 커스텀 훅
├── utils/         # 유틸리티 함수
├── types/         # 타입 정의
├── styles/        # 글로벌 스타일
└── __tests__/     # 테스트 파일
```

## 품질 기준
- **테스트 커버리지**: 최소 80%
- **타입스크립트**: strict mode 활성화
- **접근성**: WCAG 2.1 AA 준수
- **성능**: Lighthouse 점수 90+ 목표

## 보안 고려사항
- **환경 변수**: 민감한 정보는 .env 파일로 관리
- **XSS 방지**: React의 자동 이스케이프 기능 활용
- **CSRF 방지**: 서버 측에서 토큰 기반 방어
- **의존성 관리**: `npm audit`을 통한 취약점 점검
