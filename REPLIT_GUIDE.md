# 🚀 Replit으로 Conex 챗봇 배포하기 - 완전 가이드

## 왜 Replit인가요? 🤔

- ✅ **무료**: 기본 사용량은 완전 무료
- ✅ **설치 없음**: 브라우저에서 바로 실행
- ✅ **자동 배포**: 코드 변경 시 자동으로 업데이트
- ✅ **공유 쉬움**: URL로 바로 공유 가능
- ✅ **24/7 실행**: 업그레이드하면 항상 켜져 있음

## 🎯 단계별 배포 가이드

### 1단계: Groq API 키 준비 (필수!)

먼저 API 키가 없다면 받아야 합니다:

1. **Groq Console 접속**: https://console.groq.com
2. **계정 생성**: 
   - Google 계정으로 로그인 (가장 빠름)
   - 또는 이메일로 회원가입
3. **API 키 생성**:
   - 왼쪽 메뉴에서 "API Keys" 클릭
   - "Create API Key" 버튼 클릭
   - 이름: `Conex-Chatbot` (원하는 이름)
   - API 키 복사 (⚠️ 다시 볼 수 없으니 꼭 저장!)

### 2단계: Replit 계정 생성

1. **Replit 접속**: https://replit.com
2. **회원가입**: 
   - "Sign up" 클릭
   - GitHub 계정 연결 (추천) 또는 이메일 가입
3. **계정 인증**: 이메일 인증 완료

### 3단계: 프로젝트 가져오기

#### 방법 A: GitHub에서 직접 가져오기 (추천 ⭐)

1. **Import from GitHub**:
   - Replit 대시보드에서 "Import from GitHub" 클릭
   - 또는 `+` 버튼 → "Import from GitHub"

2. **레포지토리 URL 입력**:
   ```
   https://github.com/CodeNameX0/Conex-ChatBot
   ```

3. **프로젝트 설정**:
   - Title: `Conex Chatbot`
   - Description: `AI 챗봇 - Groq API 기반`
   - Private/Public 선택 (Public 추천)

4. **Import Repl** 클릭

#### 방법 B: 수동으로 만들기

1. **새 Repl 생성**:
   - `+` 버튼 클릭
   - Template: "Python" 선택
   - Title: `Conex Chatbot`

2. **파일 업로드**:
   - GitHub에서 파일들을 다운로드
   - Replit 파일 탭에서 업로드

### 4단계: 환경 변수 설정 (중요! 🔐)

1. **Secrets 탭 열기**:
   - 왼쪽 사이드바에서 "Secrets" (🔒 아이콘) 클릭

2. **API 키 추가**:
   - Key: `GROQ_API_KEY`
   - Value: 1단계에서 복사한 API 키 붙여넣기
   - "Add new secret" 클릭

### 5단계: 패키지 설치

Replit이 자동으로 `requirements.txt`를 감지하지만, 수동으로 할 수도 있습니다:

1. **Shell 탭 열기**:
   - 하단의 "Shell" 탭 클릭

2. **패키지 설치 확인**:
   ```bash
   pip install flask groq python-dotenv
   ```

### 6단계: 실행 및 테스트

1. **Run 버튼 클릭**:
   - 상단의 녹색 "Run" 버튼 클릭
   - 또는 `Ctrl + Enter`

2. **로그 확인**:
   - Console에서 다음과 같은 메시지가 나와야 함:
   ```
   * Running on all addresses (0.0.0.0)
   * Running on http://127.0.0.1:5000
   * Running on http://10.0.0.1:5000
   ```

3. **웹 미리보기**:
   - 오른쪽에 웹 미리보기 창이 자동으로 열림
   - 또는 상단의 "Open in new tab" 클릭

### 7단계: 공유 및 사용

1. **URL 복사**:
   - 브라우저 주소창에서 URL 복사
   - 형태: `https://your-repl-name.your-username.repl.co`

2. **공유**:
   - 이 URL을 친구들과 공유
   - 누구나 접속해서 챗봇 사용 가능!

## 🔧 고급 설정

### Always On 설정 (유료)

무료 계정에서는 비활성 상태가 지속되면 Repl이 잠들지만, 업그레이드하면 24/7 실행됩니다:

1. **Repl 설정**:
   - 프로젝트에서 "Settings" 클릭

2. **Always On 활성화**:
   - "Always On" 토글 활성화
   - 월 $7 정도의 비용

### 커스텀 도메인 (유료)

1. **도메인 설정**:
   - Settings → "Custom domain"
   - 원하는 도메인 입력

### 성능 최적화

1. **Boosted Repl** (유료):
   - 더 빠른 CPU와 RAM
   - 더 안정적인 실행

## 🐛 문제 해결

### 자주 발생하는 오류들

#### 1. "Port 5000 is already in use"
```bash
# Shell에서 실행:
pkill -f python
```

#### 2. "Module not found: groq"
```bash
# Shell에서 실행:
pip install groq
```

#### 3. "API key not found"
- Secrets 탭에서 `GROQ_API_KEY`가 제대로 설정되었는지 확인
- Key 이름에 오타가 없는지 확인

#### 4. "Repl keeps sleeping"
- 무료 계정의 한계입니다
- 5분간 비활성 상태면 잠듦
- 접속하면 다시 깨어남

### 디버깅 팁

1. **Console 확인**:
   - 하단 Console에서 오류 메시지 확인

2. **Logs 보기**:
   - 실행 로그에서 문제점 파악

3. **재시작**:
   - Stop 버튼 → Run 버튼으로 재시작

## 🎉 배포 완료!

축하합니다! 이제 다음이 완료되었습니다:

- ✅ **AI 챗봇이 온라인에서 실행됨**
- ✅ **URL로 누구나 접속 가능**
- ✅ **모바일에서도 완벽 작동**
- ✅ **코드 수정 시 자동 업데이트**

## 📱 사용법

1. **URL 접속**: 배포된 URL로 접속
2. **채팅 시작**: 메시지 입력창에 질문 입력
3. **AI 응답**: Groq API로 빠른 응답 받기
4. **공유**: URL을 친구들과 공유

## 💡 다음 단계

- **UI 커스터마이징**: `templates/index.html` 수정
- **프롬프트 튜닝**: `app.py`의 `SYSTEM_PROMPT` 수정
- **기능 추가**: 새로운 기능 구현
- **도메인 연결**: 커스텀 도메인 설정

## 🆘 도움이 필요하면

1. **Replit Community**: https://replit.com/community
2. **GitHub Issues**: 프로젝트 페이지에서 이슈 생성
3. **Discord**: Replit 공식 Discord 참여

---

**🎯 핵심 포인트**: Replit은 코딩 초보자도 5분 안에 AI 챗봇을 배포할 수 있는 가장 쉬운 방법입니다!
