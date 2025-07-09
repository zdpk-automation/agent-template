# CLI 명령어 사용 예시 (CLI Command Usage Examples)

이 디렉토리는 Agent Template CLI 도구의 각 명령어에 대한 상세한 사용법 예시를 제공합니다.

This directory provides detailed usage examples for each command of the Agent Template CLI tool.

## 구조 (Structure)

```
example/
├── init/                    # `init` 명령어 예시 (init command examples)
│   ├── basic-usage.md      # 기본 사용법 (basic usage)
│   ├── advanced-option.md  # 고급 옵션 (advanced options)
│   └── troubleshooting.md  # 문제 해결 (troubleshooting)
├── convert/                # `convert` 명령어 예시 (convert command examples)
│   ├── basic-usage.md      # 기본 사용법 (basic usage)
│   ├── platform-specific.md # 플랫폼별 변환 (platform-specific conversion)
│   └── troubleshooting.md  # 문제 해결 (troubleshooting)
├── list/                   # `list` 명령어 예시 (list command examples)
│   ├── basic-usage.md      # 기본 사용법 (basic usage)
│   ├── filtering.md        # 필터링 옵션 (filtering options)
│   └── troubleshooting.md  # 문제 해결 (troubleshooting)
├── update/                 # `update` 명령어 예시 (update command examples)
│   ├── basic-usage.md      # 기본 사용법 (basic usage)
│   ├── version-management.md # 버전 관리 (version management)
│   └── troubleshooting.md  # 문제 해결 (troubleshooting)
└── config/                 # `config` 명령어 예시 (config command examples)
    ├── basic-usage.md      # 기본 사용법 (basic usage)
    ├── advanced-setting.md # 고급 설정 (advanced settings)
    └── troubleshooting.md  # 문제 해결 (troubleshooting)
```

## 사용 방법 (How to Use)

각 명령어별 디렉토리에서 원하는 사용 예시를 찾아보세요:

Browse the directory for each command to find the usage examples you need:

1. **기본 사용법 (Basic Usage)**: 각 명령어의 기본적인 사용 방법
2. **고급 옵션 (Advanced Options)**: 복잡한 시나리오와 고급 기능
3. **문제 해결 (Troubleshooting)**: 자주 발생하는 문제와 해결 방법

## 동기화 규칙 (Synchronization Rules)

⚠️ **중요 (Important)**: 이 예시들은 실제 CLI 코드와 동기화되어야 합니다.

- CLI 코드 변경 시 관련 예시 업데이트 필수
- 모든 예시는 실제 실행 가능해야 함
- CI/CD에서 예시 실행 테스트 수행
- `--help` 출력과 예시 문서 내용 일치 확인

⚠️ **Important**: These examples must be synchronized with the actual CLI code.

- Update related example when CLI code changes
- All examples must be executable
- Run example tests in CI/CD
- Ensure `--help` output matches example documentation

## 기여 방법 (How to Contribute)

새로운 예시 추가 시:

When adding new examples:

1. 해당 명령어 디렉토리에 적절한 파일명으로 생성
2. 실제 실행 가능한 예시 작성
3. 한국어/영어 병기 형식 사용
4. 예시 실행 후 결과 확인
5. 관련 문서와 동기화 확인

1. Create in the appropriate command directory with proper filename
2. Write actually executable examples
3. Use Korean/English bilingual format
4. Verify example execution and results
5. Check synchronization with related documentation