# CLI 툴 개발 가이드 (CLI Tool Development Guide)

## 1. 개요 (Overview)
이 문서는 `agent-template` 저장소의 템플릿을 활용하여 새로운 프로젝트 및 다양한 콘텐츠를 생성하고 관리하는 CLI 툴의 개발 가이드입니다. 이 툴은 개발자가 표준화된 프로젝트 구조와 문서 형식을 신속하게 시작하고 유지보수할 수 있도록 돕는 것을 목표로 합니다.

## 2. 지원 언어 및 프레임워크 (Supported Languages & Frameworks)

### 언어 (Languages)
*   TypeScript (TS)
*   Python
*   Rust
*   Dart

### 프레임워크 (Frameworks)
*   **Backend**: Axum (Rust), NestJS (TS), FastAPI (Python)
*   **Frontend**: Next.js (TS), Flutter (Dart)
*   **Infrastructure**: Terraform (GCP, AWS)
*   **CLI**: Typer (Python), Clap (Rust)

### 추가 사용 사례 (Additional Use Cases)
*   Social platform scripts
*   Obsidian technical blog posts
*   Study records
*   Daily records

## 3. 기능 (Features)

### `init` (초기화)
*   **다양한 템플릿 유형 지원**: 코드 프로젝트(백엔드, 프론트엔드, 인프라, **CLI**), 스크립트, 문서(블로그, 기록) 등 다양한 유형의 템플릿을 기반으로 새 항목을 생성합니다.
*   **세분화된 템플릿 선택**: 언어, 프레임워크, 콘텐츠 유형(예: `backend/python/fastapi`, `doc/obsidian/blog-post`, `cli/python/typer`)을 조합하여 템플릿을 선택할 수 있도록 지원합니다.
*   특정 템플릿 버전을 선택할 수 있도록 지원합니다 (Git 태그 활용).
*   프로젝트/항목 이름, 경로, 작성자 등 사용자 입력을 받습니다.
*   템플릿 파일 복사 및 플레이스홀더(placeholder) 치환 기능을 포함합니다.

### `list` (목록)
*   사용 가능한 모든 템플릿 목록을 유형별(코드, 문서 등)로 표시합니다.
*   각 템플릿의 사용 가능한 버전(Git 태그)을 함께 표시할 수 있습니다.

## 4. 아키텍처 (Architecture)

```
cli/
├── main.py             # CLI 진입점 (Entry point)
├── commands/           # CLI 하위 명령 (Subcommands)
│   ├── init.py         # `init` 명령어 로직
│   └── list.py         # `list` 명령어 로직
├── core/               # 핵심 로직 (Core Logic)
│   ├── template_manager.py # 템플릿 저장소(Git)와 상호작용 (클론, 태그 조회 등)
│   └── project_generator.py # 프로젝트/콘텐츠 생성, 파일 복사, 플레이스홀더 치환
├── config.py           # CLI 설정 (예: 템플릿 저장소 URL)
└── utils.py            # 공통 유틸리티 함수
```

**주요 구성 요소 (Key Components):**
*   **CLI 프레임워크 (CLI Framework):** `Typer` (또는 `Click`) 라이브러리를 사용하여 명령줄 인자 파싱, 하위 명령 정의, 도움말 생성 등을 처리합니다.
*   **`template_manager.py`:**
    *   `agent-template` 저장소를 로컬에 클론하거나 업데이트하는 기능을 담당합니다.
    *   사용 가능한 템플릿 디렉토리(예: `templates/backend/python/fastapi`, `templates/doc/obsidian/blog-post`, `templates/cli/python/typer`)를 식별합니다.
    *   Git 태그를 사용하여 템플릿의 버전을 관리하고, 특정 버전의 템플릿을 체크아웃하는 기능을 제공합니다.
*   **`project_generator.py`:**
    *   선택된 템플릿 디렉토리의 내용을 새 프로젝트/콘텐츠 경로로 복사합니다.
    *   템플릿 내의 플레이스홀더(예: `{{project_name}}`, `{{author}}`, `{{today_date}}`)를 사용자 입력 값으로 치환합니다.
    *   `.git` 디렉토리와 같은 불필요한 파일을 복사하지 않도록 처리합니다.

## 5. 개발 지침 (Development Guidelines)

### 명확한 문서화 (Clear Documentation)
**모든 코드 변경 및 새로운 기능 개발 시에는 해당 변경사항과 관련된 문서를 명확하게 작성해야 합니다.** 이는 코드의 이해도를 높이고, 향후 유지보수 및 협업을 용이하게 합니다. 특히 CLI 툴의 사용법, 기능, 아키텍처 변경사항은 이 가이드 문서에 상세히 반영되어야 합니다.

### 코드 스타일 (Code Style)
Python PEP 8 스타일 가이드를 준수합니다.

### 테스트 (Testing)
모든 기능에 대해 적절한 단위 테스트 및 통합 테스트를 작성합니다.
