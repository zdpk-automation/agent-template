# `init` 명령어 기본 사용법 (init Command Basic Usage)

## 개요 (Overview)

`agent-template init` 명령어는 새로운 프로젝트를 표준화된 템플릿으로 초기화하는 기능을 제공합니다.

The `agent-template init` command provides functionality to initialize new projects with standardized templates.

## 기본 사용법 (Basic Usage)

### 1. 대화형 초기화 (Interactive Initialization)

```bash
# 대화형 모드로 프로젝트 초기화
agent-template init

# 예상 출력:
# ? 어떤 유형의 프로젝트를 시작하시겠습니까? (What type of project would you like to start?)
#   > 개발 프로젝트 (Development)
#     콘텐츠 제작 (Content Creation)  
#     학습 프로젝트 (Learning)
```

### 2. 개발 프로젝트 초기화 (Development Project Initialization)

```bash
# 개발 프로젝트 선택 시 추가 옵션
# ? 개발 언어를 선택하세요 (Select programming language):
#   > Python
#     TypeScript
#     Rust
#     Dart

# ? 프레임워크를 선택하세요 (Select framework):
#   > FastAPI
#     Django
#     Flask
```

### 3. 프로젝트 정보 입력 (Project Information Input)

```bash
# ? 프로젝트 이름을 입력하세요 (Enter project name):
#   > my-awesome-api

# ? 작성자 이름을 입력하세요 (Enter author name):
#   > John Doe

# ? 작성자 이메일을 입력하세요 (Enter author email):
#   > john.doe@example.com
```

## 사용 예시 (Usage Examples)

### 예시 1: FastAPI 백엔드 프로젝트 (FastAPI Backend Project)

```bash
$ agent-template init
? 어떤 유형의 프로젝트를 시작하시겠습니까? 개발 프로젝트
? 개발 언어를 선택하세요: Python
? 프레임워크를 선택하세요: FastAPI
? 프로젝트 이름을 입력하세요: user-management-api
? 작성자 이름을 입력하세요: Alice Kim
? 작성자 이메일을 입력하세요: alice.kim@company.com

✅ 프로젝트 'user-management-api'가 성공적으로 생성되었습니다!
   위치: ./user-management-api/
   템플릿: development/backend/python/fastapi v2.1.0

다음 단계:
1. cd user-management-api
2. python -m venv venv
3. source venv/bin/activate
4. pip install -r requirements.txt
5. uvicorn main:app --reload
```

### 예시 2: 기술 블로그 포스트 (Tech Blog Post)

```bash
$ agent-template init
? 어떤 유형의 프로젝트를 시작하시겠습니까? 콘텐츠 제작
? 콘텐츠 유형을 선택하세요: 블로그 포스트
? 플랫폼을 선택하세요: Obsidian
? 포스트 제목을 입력하세요: "Python 비동기 프로그래밍 완벽 가이드"
? 작성자 이름을 입력하세요: Bob Lee

✅ 블로그 포스트 템플릿이 성공적으로 생성되었습니다!
   위치: ./python-async-guide/
   템플릿: content/blog/obsidian/tech-post v1.5.0

다음 단계:
1. cd python-async-guide
2. Obsidian에서 폴더 열기
3. index.md 파일 편집 시작
```

### 예시 3: CLI 도구 개발 (CLI Tool Development)

```bash
$ agent-template init
? 어떤 유형의 프로젝트를 시작하시겠습니까? 개발 프로젝트
? 개발 언어를 선택하세요: Python
? 프레임워크를 선택하세요: CLI (Typer)
? 프로젝트 이름을 입력하세요: file-organizer
? 작성자 이름을 입력하세요: Charlie Park

✅ CLI 프로젝트 'file-organizer'가 성공적으로 생성되었습니다!
   위치: ./file-organizer/
   템플릿: development/cli/python/typer v1.0.0

다음 단계:
1. cd file-organizer
2. python -m venv venv
3. source venv/bin/activate
4. pip install -e .
5. file-organizer --help
```

## 생성된 파일 구조 (Generated File Structure)

### FastAPI 프로젝트 예시 (FastAPI Project Example)

```
user-management-api/
├── .agent/
│   ├── template/
│   │   ├── AGENT.md -> ~/.agent-template-cache/templates/development/backend/python/fastapi/AGENT.md
│   │   └── README.md -> ~/.agent-template-cache/templates/development/backend/python/fastapi/README.md
│   └── template.json
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   ├── routers/
│   └── dependencies.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── pyproject.toml
```

### 템플릿 메타데이터 (Template Metadata)

생성된 `.agent/template.json` 파일 예시:

```json
{
  "version": "2.1.0",
  "template_type": "development/backend/python/fastapi",
  "created_at": "2025-07-09T10:00:00Z",
  "last_updated": "2025-07-09T10:00:00Z",
  "author": "Alice Kim",
  "author_email": "alice.kim@company.com",
  "project_name": "user-management-api",
  "protected_files": [
    ".agent/template/AGENT.md",
    ".agent/template/README.md"
  ]
}
```

## 플레이스홀더 치환 (Placeholder Substitution)

템플릿 파일에서 다음 플레이스홀더들이 자동으로 치환됩니다:

The following placeholders are automatically substituted in template files:

- `{{project_name}}` → `user-management-api`
- `{{author_name}}` → `Alice Kim`
- `{{author_email}}` → `alice.kim@company.com`
- `{{current_date}}` → `2025-07-09`
- `{{current_year}}` → `2025`
- `{{template_version}}` → `2.1.0`

## 참고사항 (Notes)

- 모든 템플릿 파일은 읽기 전용으로 보호됩니다
- 프로젝트 생성 후 `.agent/template/` 디렉토리의 파일들은 수정하지 마세요
- 템플릿 업데이트가 필요한 경우 `agent-template update` 명령어를 사용하세요

- All template files are protected as read-only
- Do not modify files in `.agent/template/` directory after project creation
- Use `agent-template update` command for template updates

## 관련 명령어 (Related Commands)

- [`agent-template list`](../list/basic-usage.md) - 사용 가능한 템플릿 확인
- [`agent-template update`](../update/basic-usage.md) - 템플릿 업데이트
- [`agent-template config`](../config/basic-usage.md) - 기본 설정 관리