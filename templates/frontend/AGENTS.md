# Frontend Project AI Configuration

## 프로젝트 개요 / Project Overview
- **타입 / Type**: Frontend Web Application
- **주요 기술 / Tech Stack**: React, TypeScript, Vite
- **스타일링 / Styling**: CSS Modules
- **상태 관리 / State Management**: React Context / Zustand
- **테스팅 / Testing**: Jest, React Testing Library

## 개발 환경 설정 / Development Environment

### 빌드 및 개발 명령어 / Build and Development Commands
```bash
npm run dev          # 개발 서버 시작 / Start development server
npm run build        # 프로덕션 빌드 / Production build
npm run test         # 테스트 실행 / Run tests
npm run lint         # 코드 린팅 / Code linting
npm run format       # 코드 포맷팅 / Code formatting
```

### 코딩 스타일 가이드 / Coding Style Guide
- **들여쓰기 / Indentation**: 2 spaces
- **따옴표 / Quotes**: Single quotes for strings
- **세미콜론 / Semicolons**: 항상 사용 / Always use
- **네이밍 / Naming**: camelCase for variables, PascalCase for components
- **파일명 / File naming**: kebab-case for files, PascalCase for components

## AI 도구 사용 가이드 / AI Tools Usage Guide

### Claude Code 활용 / Claude Code Usage
- 컴포넌트 설계 및 구현 / Component design and implementation
- React 훅 최적화 / React hooks optimization
- 타입스크립트 타입 정의 / TypeScript type definitions
- 성능 최적화 제안 / Performance optimization suggestions

### 프로젝트 구조 / Project Structure
```
src/
├── components/     # 재사용 가능한 컴포넌트 / Reusable components
├── pages/         # 페이지 컴포넌트 / Page components
├── hooks/         # 커스텀 훅 / Custom hooks
├── utils/         # 유틸리티 함수 / Utility functions
├── types/         # 타입 정의 / Type definitions
├── styles/        # 글로벌 스타일 / Global styles
└── __tests__/     # 테스트 파일 / Test files
```

## 품질 기준 / Quality Standards
- **테스트 커버리지 / Test Coverage**: 최소 80% / Minimum 80%
- **타입스크립트 / TypeScript**: strict mode 활성화 / Strict mode enabled
- **접근성 / Accessibility**: WCAG 2.1 AA 준수 / WCAG 2.1 AA compliance
- **성능 / Performance**: Lighthouse 점수 90+ 목표 / Target Lighthouse score 90+