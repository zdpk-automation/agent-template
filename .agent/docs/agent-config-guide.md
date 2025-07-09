# AI 에이전트 설정 가이드

이 가이드는 Agent Template Repository에서 AI 에이전트 설정 파일들을 작성하고 활용하는 방법을 설명합니다.

## 설정 파일 구조 개요

### 현재 구조
```
├── AGENT.md                # 프로젝트 자체용 공통 지침
├── CLAUDE.md → templates/common/CLAUDE.md  # Claude Code 설정 (심볼릭 링크)
├── .gemini/GEMINI.md → ../templates/common/GEMINI.md  # Gemini CLI 설정 (심볼릭 링크)
└── templates/common/
    ├── AGENT.md            # 템플릿용 공통 지침
    ├── CLAUDE.md           # Claude Code 설정 (AGENT.md 참조만)
    ├── GEMINI.md           # Gemini CLI 설정 (AGENT.md 참조만)
    ├── CLAUDE.template.md  # Claude Code 지침 템플릿
    └── GEMINI.template.md  # Gemini CLI 지침 템플릿
```

### 설계 원칙
1. **중복 제거**: 공통 지침은 AGENT.md에서 일괄 관리
2. **명확한 분리**: 프로젝트 자체용과 템플릿용 설정 구분
3. **일관성**: 모든 AI 도구가 동일한 패턴을 따름
4. **확장성**: 새로운 AI 도구 추가 시 쉽게 확장 가능

## AGENT.md 작성 가이드

### 기본 구조
```markdown
# Agent Instructions

## 프로젝트 개요
[프로젝트에 대한 간단한 설명]

## 주요 디렉토리 구조
[프로젝트의 디렉토리 구조와 각 디렉토리의 역할]

## 개발 시 유의사항
[개발할 때 주의해야 할 사항들]

## 코딩 스타일
[프로젝트의 코딩 스타일과 컨벤션]

## 작업 원칙
[AI 에이전트가 따라야 할 작업 원칙들]
```

### 프로젝트 자체용 AGENT.md 작성
프로젝트 루트의 `AGENT.md`는 이 저장소 자체를 개발할 때 사용됩니다.

**포함해야 할 내용:**
- 프로젝트의 목적과 구조
- 개발 시 지켜야 할 원칙
- 파일 구조와 네이밍 컨벤션
- 특별한 요구사항이나 제약사항

### 템플릿용 AGENT.md 작성
`templates/common/AGENT.md`는 다른 프로젝트에서 복사해서 사용할 템플릿입니다.

**포함해야 할 내용:**
- 일반적인 프로젝트 구조 가이드
- 범용적인 코딩 스타일 가이드
- 플레이스홀더와 예시
- 사용자가 수정해야 할 부분에 대한 안내

## 도구별 설정 파일

### Claude Code 설정
- **파일 위치**: `CLAUDE.md` (루트), `templates/common/CLAUDE.md`
- **내용**: AGENT.md 참조만 포함
- **특화 지침**: 필요시 Claude Code 특화 지침 추가

```markdown
# Claude Code Instructions

공통 지침은 [AGENT.md](./AGENT.md)를 참조하세요.

## Claude Code 특화 지침
- TodoWrite 도구를 적극 활용하여 작업 추적
- 단계별 작업 분해 및 실행
- 파일 읽기 전에 반드시 Read 도구 사용
```

### Gemini CLI 설정
- **파일 위치**: `.gemini/GEMINI.md`
- **내용**: AGENT.md 참조만 포함
- **특화 지침**: 필요시 Gemini CLI 특화 지침 추가

```markdown
# Gemini CLI Instructions

공통 지침은 [AGENT.md](../AGENT.md)를 참조하세요.

## Gemini CLI 특화 지침
- 대화형 계획 모드 적극 활용
- 복잡한 작업 시 단계별 분해 및 실행
```

## 새로운 프로젝트에서 사용하기

### 1. 템플릿 복사
```bash
# 기본 설정 파일들 복사
cp templates/common/AGENT.md ./AGENT.md
cp templates/common/CLAUDE.md ./CLAUDE.md
mkdir -p .gemini
cp templates/common/GEMINI.md ./.gemini/GEMINI.md
```

### 2. AGENT.md 수정
복사한 `AGENT.md`를 프로젝트에 맞게 수정:
- 프로젝트 개요 작성
- 실제 디렉토리 구조 반영
- 프로젝트 특화 지침 추가

### 3. 심볼릭 링크 설정 (선택사항)
```bash
# 중앙 관리를 위한 심볼릭 링크 생성
ln -sf templates/common/CLAUDE.md CLAUDE.md
ln -sf ../templates/common/GEMINI.md .gemini/GEMINI.md
```

## 새로운 AI 도구 추가하기

### 1. 템플릿 파일 생성
```bash
# 새로운 도구용 템플릿 생성
touch templates/common/NEWTOOL.md
touch templates/common/NEWTOOL.template.md
```

### 2. 설정 파일 내용 작성
```markdown
# NewTool Instructions

공통 지침은 [AGENT.md](./AGENT.md)를 참조하세요.

## NewTool 특화 지침
- [도구별 특화 지침들]
```

### 3. 심볼릭 링크 생성
```bash
# 적절한 위치에 심볼릭 링크 생성
# (도구별 요구사항에 따라 경로 조정)
ln -s templates/common/NEWTOOL.md NEWTOOL.md
```

## 모범 사례

### DO
- 공통 지침은 AGENT.md에서 관리
- 도구별 특화 지침은 최소화
- 명확하고 구체적인 지침 작성
- 정기적인 지침 업데이트

### DON'T
- 중복된 내용을 여러 파일에 작성
- 너무 상세한 구현 사항 포함
- 프로젝트와 무관한 일반적인 내용
- 자주 변경되는 임시적인 지침

## 문제 해결

### 심볼릭 링크가 작동하지 않는 경우
```bash
# 링크 상태 확인
ls -la CLAUDE.md
ls -la .gemini/GEMINI.md

# 링크 재생성
rm CLAUDE.md
ln -s templates/common/CLAUDE.md CLAUDE.md
```

### 에이전트가 지침을 읽지 못하는 경우
1. 파일 경로가 올바른지 확인
2. 파일 권한 확인
3. 심볼릭 링크 대상 파일 존재 확인

## 기여하기

새로운 AI 도구 지원이나 설정 개선사항이 있다면:
1. 이슈 등록으로 제안 논의
2. PR 제출 시 문서 업데이트 포함
3. 기존 패턴과 일관성 유지

---

이 가이드는 프로젝트 발전에 따라 지속적으로 업데이트됩니다. 개선사항이나 질문이 있으면 언제든 이슈로 등록해주세요.