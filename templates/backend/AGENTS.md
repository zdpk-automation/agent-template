# Backend Project AI Configuration

## 프로젝트 개요 / Project Overview
- **타입 / Type**: Backend API Server
- **주요 기술 / Tech Stack**: Node.js, Express, TypeScript
- **데이터베이스 / Database**: PostgreSQL
- **인증 / Authentication**: JWT
- **테스팅 / Testing**: Jest, Supertest

## 개발 환경 설정 / Development Environment

### 빌드 및 개발 명령어 / Build and Development Commands
```bash
npm run dev          # 개발 서버 시작 / Start development server
npm run build        # 프로덕션 빌드 / Production build
npm run start        # 프로덕션 서버 시작 / Start production server
npm run test         # 테스트 실행 / Run tests
npm run lint         # 코드 린팅 / Code linting
npm run format       # 코드 포맷팅 / Code formatting
```

### API 설계 원칙 / API Design Principles
- **RESTful**: REST API 설계 원칙 준수 / Follow REST API design principles
- **버전 관리 / Versioning**: /api/v1/ 형태로 버전 관리 / Version management with /api/v1/
- **에러 처리 / Error Handling**: 일관된 에러 응답 형식 / Consistent error response format
- **보안 / Security**: Helmet, CORS, Rate limiting 적용 / Apply Helmet, CORS, Rate limiting

## AI 도구 사용 가이드 / AI Tools Usage Guide

### Claude Code 활용 / Claude Code Usage
- API 엔드포인트 설계 및 구현 / API endpoint design and implementation
- 데이터베이스 스키마 설계 / Database schema design
- 미들웨어 및 인증 로직 / Middleware and authentication logic
- 에러 처리 및 로깅 / Error handling and logging

### 프로젝트 구조 / Project Structure
```
src/
├── controllers/    # 컨트롤러 / Controllers
├── middleware/     # 미들웨어 / Middleware
├── models/         # 데이터 모델 / Data models
├── routes/         # 라우트 정의 / Route definitions
├── services/       # 비즈니스 로직 / Business logic
├── utils/          # 유틸리티 함수 / Utility functions
├── types/          # 타입 정의 / Type definitions
└── __tests__/      # 테스트 파일 / Test files
```

## 보안 고려사항 / Security Considerations
- **환경 변수 / Environment Variables**: 민감한 정보는 .env 파일로 관리 / Manage sensitive data with .env files
- **입력 검증 / Input Validation**: 모든 입력 데이터 검증 / Validate all input data
- **SQL 인젝션 방지 / SQL Injection Prevention**: 파라미터화된 쿼리 사용 / Use parameterized queries
- **HTTPS**: 프로덕션에서 HTTPS 강제 / Enforce HTTPS in production

## 품질 기준 / Quality Standards
- **테스트 커버리지 / Test Coverage**: 최소 80% / Minimum 80%
- **API 문서화 / API Documentation**: OpenAPI/Swagger 사용 / Use OpenAPI/Swagger
- **로깅 / Logging**: 구조화된 로깅 / Structured logging
- **모니터링 / Monitoring**: 헬스체크 엔드포인트 / Health check endpoints