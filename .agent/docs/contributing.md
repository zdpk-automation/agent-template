# 기여 가이드

Agent Template Repository에 기여해주셔서 감사합니다! 이 가이드는 프로젝트에 효과적으로 기여하는 방법을 안내합니다.

## 기여 유형

### 1. 새로운 AI 도구 지원 추가
- 새로운 AI 도구용 템플릿 생성
- 설정 파일 구조 설계
- 사용 가이드 작성

### 2. 프로젝트 템플릿 추가
- 새로운 프로젝트 유형 템플릿
- 기존 템플릿 개선
- 템플릿 문서화

### 3. CLI 도구 개선
- 새로운 명령어 추가
- 기존 기능 개선
- 버그 수정

### 4. 문서 개선
- 사용법 가이드 개선
- 예제 추가
- 오타 수정

## 기여 과정

### 1. 이슈 확인/등록
기여하기 전에 관련 이슈를 확인하거나 새로 등록해주세요.

```bash
# 이슈 템플릿 사용
- 버그 리포트: .github/ISSUE_TEMPLATE/bug_report.md
- 기능 요청: .github/ISSUE_TEMPLATE/feature_request.md
- 문서 개선: .github/ISSUE_TEMPLATE/documentation.md
```

### 2. 포크 및 브랜치 생성
```bash
# 저장소 포크 후 클론
git clone https://github.com/YOUR-USERNAME/agent-template.git
cd agent-template

# 기능 브랜치 생성
git checkout -b feature/your-feature-name
```

### 3. 개발 환경 설정
```bash
# Python 가상환경 설정
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt

# 개발 도구 설치
pip install -r requirements-dev.txt
```

### 4. 개발 및 테스트
```bash
# 코드 품질 확인
flake8 cli/
black cli/
mypy cli/

# 테스트 실행
pytest tests/

# 통합 테스트
./tests/integration/run_all.sh
```

### 5. 문서 업데이트
변경사항에 따라 관련 문서를 업데이트해주세요:
- README.md 업데이트
- 기능 문서 작성 (docs/features/ 디렉토리 사용)
- 변경사항을 docs/development-history.md에 기록

## 코딩 스타일

### Python 코드
- PEP 8 준수
- 타입 힌트 사용
- docstring 작성 (Google 스타일)

```python
def example_function(param1: str, param2: int) -> bool:
    """함수의 목적을 설명하는 docstring.
    
    Args:
        param1: 첫 번째 매개변수 설명
        param2: 두 번째 매개변수 설명
        
    Returns:
        반환값에 대한 설명
        
    Raises:
        ValueError: 발생 가능한 예외 설명
    """
    return True
```

### 마크다운 문서
- 한국어 우선, 필요시 영어 병기
- 명확한 구조와 섹션 구분
- 코드 예시와 실행 결과 포함

## 새로운 AI 도구 추가 가이드

### 1. 파일 구조 생성
```bash
# 설정 파일 생성
mkdir -p configs/newtool
touch configs/newtool/config.json

# 템플릿 파일 생성
touch templates/common/NEWTOOL.md
touch templates/common/NEWTOOL.template.md
```

### 2. 설정 파일 작성
```markdown
# NewTool Instructions

공통 지침은 [AGENT.md](./AGENT.md)를 참조하세요.

## NewTool 특화 지침
- [도구별 특화 지침들]
```

### 3. CLI 통합
```python
# cli/commands/newtool.py
import click
from cli.core.template_manager import TemplateManager

@click.command()
@click.option('--config', help='설정 파일 경로')
def init_newtool(config):
    """NewTool 설정 초기화"""
    manager = TemplateManager()
    manager.init_newtool(config)
```

### 4. 문서화
- 사용 가이드 작성
- 예제 추가
- 제한사항 및 주의사항 명시

## 프로젝트 템플릿 추가 가이드

### 1. 템플릿 디렉토리 생성
```bash
mkdir -p templates/your-project-type
cd templates/your-project-type
```

### 2. 필수 파일 생성
```bash
# 에이전트 설정 파일
touch AGENTS.md

# 프로젝트 설정 파일
touch package.json  # 또는 requirements.txt, Cargo.toml 등

# 커스텀 템플릿
touch custom.template.md
```

### 3. 템플릿 내용 작성
프로젝트 유형에 맞는 구조와 설정을 포함하세요.

## 테스트 가이드

### 단위 테스트
```bash
# 특정 모듈 테스트
pytest tests/test_template_manager.py -v

# 커버리지 확인
pytest --cov=cli tests/
```

### 통합 테스트
```bash
# CLI 명령어 테스트
./tests/integration/test_init_command.sh

# 템플릿 생성 테스트
./tests/integration/test_template_generation.sh
```

## PR 제출 가이드

### 1. PR 제목 규칙
- `feat:` 새로운 기능 추가
- `fix:` 버그 수정
- `docs:` 문서 수정
- `refactor:` 코드 리팩토링
- `test:` 테스트 추가/수정

### 2. PR 설명 템플릿
```markdown
## 변경사항 요약
- [주요 변경사항 1]
- [주요 변경사항 2]

## 테스트 계획
- [ ] 단위 테스트 통과
- [ ] 통합 테스트 통과
- [ ] 문서 업데이트 완료

## 체크리스트
- [ ] 코딩 스타일 가이드 준수
- [ ] 타입 힌트 추가
- [ ] 문서 업데이트
- [ ] 테스트 추가/수정
```

### 3. 브랜치 규칙
- `feature/` 새로운 기능
- `fix/` 버그 수정
- `docs/` 문서 수정
- `refactor/` 리팩토링

## 리뷰 과정

### 1. 자동 검사
- 코드 품질 검사 (flake8, black, mypy)
- 테스트 실행
- 문서 빌드 확인

### 2. 코드 리뷰
- 로직 검증
- 성능 고려사항 확인
- 보안 검토
- 문서화 적절성 확인

### 3. 최종 승인
- 모든 검사 통과
- 리뷰어 승인
- 충돌 해결 완료

## 릴리즈 과정

### 1. 버전 관리
- 시맨틱 버전 관리 (x.y.z)
- CHANGELOG.md 업데이트
- Git 태그 생성

### 2. 배포 준비
- 문서 최종 검토
- 예제 테스트
- 호환성 확인

## 질문과 지원

### 도움이 필요한 경우
- GitHub Issues로 질문 등록
- 디스커션 참여
- 문서 확인

### 소통 가이드
- 명확하고 구체적인 질문
- 관련 컨텍스트 제공
- 재현 가능한 예제 포함

---

이 프로젝트는 오픈소스 정신에 따라 모든 기여자를 환영합니다. 작은 개선사항부터 큰 기능 추가까지, 모든 기여가 소중합니다!

궁금한 점이 있으면 언제든 이슈로 문의해주세요.