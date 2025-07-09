# `convert` 명령어 기본 사용법 (convert Command Basic Usage)

## 개요 (Overview)

`agent-template convert` 명령어는 기존 콘텐츠를 다른 플랫폼용으로 변환하는 기능을 제공합니다.

The `agent-template convert` command provides functionality to convert existing content for different platforms.

## 기본 사용법 (Basic Usage)

### 1. 단일 플랫폼 변환 (Single Platform Conversion)

```bash
# 블로그 포스트를 Instagram용으로 변환
agent-template convert blog-post.md instagram

# YouTube 스크립트를 X/Twitter용으로 변환  
agent-template convert youtube-script.md x
```

### 2. 다중 플랫폼 변환 (Multi-Platform Conversion)

```bash
# 하나의 콘텐츠를 여러 플랫폼용으로 동시 변환
agent-template convert tech-article.md youtube,instagram,x,threads

# 쉼표로 구분된 플랫폼 목록 사용
agent-template convert content.md "youtube, instagram, x, threads"
```

### 3. 대화형 변환 (Interactive Conversion)

```bash
# 대화형 모드로 변환 옵션 선택
agent-template convert blog-post.md --interactive

# 예상 출력:
# ? 어떤 플랫폼으로 변환하시겠습니까? (Which platforms would you like to convert to?)
#   ☑ YouTube (긴 형식 비디오)
#   ☑ Instagram (시각적 콘텐츠)
#   ☐ X/Twitter (간결한 스레드)
#   ☐ Threads (대화형 긴 텍스트)
```

## 지원 플랫폼 (Supported Platforms)

### YouTube
- **용도**: 긴 형식 비디오 콘텐츠
- **특징**: 상세한 설명, 타임스탬프, 링크 포함
- **출력 형식**: `content-youtube.md`

### Instagram
- **용도**: 시각적 콘텐츠 + 짧은 텍스트
- **특징**: 해시태그, 간결한 설명, 시각적 요소 강조
- **출력 형식**: `content-instagram.md`

### X/Twitter
- **용도**: 간결한 스레드 형식
- **특징**: 280자 제한, 스레드 분할, 해시태그
- **출력 형식**: `content-x.md`

### Threads
- **용도**: 대화형 긴 텍스트
- **특징**: 연결된 포스트, 토론 유도, 커뮤니티 참여
- **출력 형식**: `content-threads.md`

## 사용 예시 (Usage Examples)

### 예시 1: 기술 블로그 포스트 변환 (Tech Blog Post Conversion)

**원본 파일**: `python-async-guide.md`

```bash
$ agent-template convert python-async-guide.md youtube,instagram,x

✅ 변환 완료! (Conversion completed!)

생성된 파일들:
- python-async-guide-youtube.md (YouTube용 긴 형식 스크립트)
- python-async-guide-instagram.md (Instagram용 시각적 포스트)
- python-async-guide-x.md (X/Twitter용 스레드)

다음 단계:
1. 각 플랫폼별 파일 검토 및 수정
2. 플랫폼 특성에 맞는 추가 최적화
3. 시각적 자료 준비 (Instagram의 경우)
```

### 예시 2: YouTube 영상을 다른 플랫폼용으로 변환 (YouTube to Other Platforms)

**원본 파일**: `react-hooks-tutorial.md`

```bash
$ agent-template convert react-hooks-tutorial.md threads --interactive

? 변환 옵션을 선택하세요: (Select conversion options:)
  ☑ 기술적 세부사항 유지 (Maintain technical details)
  ☑ 코드 예시 포함 (Include code examples)
  ☐ 초보자 친화적 언어 (Beginner-friendly language)

? 대상 독자를 선택하세요: (Select target audience:)
  > 중급 개발자 (Intermediate developers)
    초급 개발자 (Beginner developers)
    시니어 개발자 (Senior developers)

✅ Threads용 콘텐츠가 생성되었습니다!
   파일: react-hooks-tutorial-threads.md
   
변환 요약:
- 7개의 연결된 포스트로 분할
- 각 포스트는 토론을 유도하는 질문 포함
- 실용적인 코드 예시 유지
- 커뮤니티 참여 요소 추가
```

### 예시 3: 모든 플랫폼 일괄 변환 (Batch Conversion to All Platforms)

```bash
$ agent-template convert django-best-practices.md all

? 모든 플랫폼으로 변환하시겠습니까? (Convert to all platforms?) Yes

변환 진행상황:
[████████████████████████████████] 100% 완료

✅ 모든 플랫폼용 콘텐츠 생성 완료!

출력 파일들:
├── django-best-practices-youtube.md
├── django-best-practices-instagram.md  
├── django-best-practices-x.md
└── django-best-practices-threads.md

플랫폼별 최적화 요약:
- YouTube: 25분 분량 튜토리얼 스크립트 (타임스탬프 포함)
- Instagram: 10개 슬라이드 카루셀 포스트 (주요 포인트 강조)
- X: 15개 트윗 스레드 (실용적 팁 중심)
- Threads: 8개 연결 포스트 (토론 유도 질문 포함)
```

## 변환 설정 (Conversion Settings)

### 글로벌 설정 (Global Settings)

```bash
# 기본 작성자 정보 설정
agent-template config set author.name "Your Name"
agent-template config set author.handle "@yourhandle"

# 플랫폼별 기본 설정
agent-template config set platforms.youtube.duration "medium"  # short, medium, long
agent-template config set platforms.instagram.style "technical"  # casual, technical, visual
agent-template config set platforms.x.thread_length "optimal"  # short, optimal, long
```

### 파일별 설정 (File-specific Settings)

원본 파일에 메타데이터 추가:

```markdown
---
title: "Python 비동기 프로그래밍 완벽 가이드"
author: "Alice Kim"
platforms:
  youtube:
    duration: "long"
    include_timestamps: true
  instagram:
    style: "technical"
    slide_count: 10
  x:
    thread_length: "optimal"
    include_code: true
  threads:
    discussion_points: true
    audience: "intermediate"
---

# 본문 내용...
```

## 출력 파일 구조 (Output File Structure)

### YouTube 변환 예시 (YouTube Conversion Example)

```markdown
# Python 비동기 프로그래밍 완벽 가이드 - YouTube 스크립트

## 비디오 정보
- 예상 길이: 25분
- 난이도: 중급
- 타겟 독자: Python 개발자

## 타임스탬프
- 00:00 인트로 및 개요
- 02:30 동기 vs 비동기 프로그래밍
- 05:45 async/await 기본 문법
- 10:20 실습 예제 1: 웹 크롤링
- 15:30 실습 예제 2: API 호출
- 20:15 성능 최적화 팁
- 23:45 마무리 및 다음 단계

## 스크립트

### 인트로 (0:00 - 2:30)
안녕하세요! 오늘은 Python 비동기 프로그래밍에 대해 완벽하게 알아보겠습니다...

[계속...]
```

### Instagram 변환 예시 (Instagram Conversion Example)

```markdown
# Python 비동기 프로그래밍 - Instagram 포스트

## 슬라이드 1: 커버
🐍 Python 비동기 프로그래밍 완벽 가이드

#Python #AsyncProgramming #Programming #코딩 #개발자

## 슬라이드 2: 문제 정의
⚡ 왜 비동기가 필요할까?

동기 프로그래밍의 한계:
- 하나의 작업이 끝날 때까지 대기
- I/O 작업 시 CPU 낭비
- 성능 병목 현상

## 슬라이드 3: 해결책
🚀 비동기 프로그래밍의 장점

✅ 여러 작업 동시 처리
✅ I/O 대기 시간 활용
✅ 더 빠른 응답 시간
✅ 리소스 효율성 증대

[계속...]
```

## 문제 해결 (Troubleshooting)

### 일반적인 문제 (Common Issues)

1. **지원되지 않는 파일 형식**
   ```bash
   Error: 지원되지 않는 파일 형식입니다. (.docx)
   해결: Markdown (.md) 파일로 변환 후 재시도
   ```

2. **플랫폼 이름 오류**
   ```bash
   Error: 알 수 없는 플랫폼 'twitter'
   해결: 'x' 사용 (X/Twitter의 새로운 이름)
   ```

3. **메타데이터 파싱 오류**
   ```bash
   Error: YAML 메타데이터 파싱 실패
   해결: 파일 상단의 --- 구분자 확인
   ```

## 관련 명령어 (Related Commands)

- [`agent-template list`](../list/basic-usage.md) - 사용 가능한 변환 옵션 확인
- [`agent-template config`](../config/basic-usage.md) - 변환 설정 관리
- [`agent-template init`](../init/basic-usage.md) - 새 콘텐츠 프로젝트 생성