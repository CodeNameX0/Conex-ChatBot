# 🔐 GitHub 보안 가이드

## 📋 프로젝트를 GitHub에 안전하게 올리기

### ✅ 이미 구현된 보안 기능

1. **환경 변수 사용**: API 키를 코드에 직접 저장하지 않음
2. **.gitignore**: 민감한 파일들이 Git에 추가되지 않도록 설정
3. **.env.example**: 환경 변수 템플릿 제공
4. **python-dotenv**: .env 파일 지원

### 🚀 GitHub에 올리는 방법

#### 1단계: Git 초기화
```bash
git init
git add .
git commit -m "Initial commit: Conex Chatbot with Groq API"
```

#### 2단계: GitHub 레포지토리 생성
1. GitHub.com에서 새 레포지토리 생성
2. 레포지토리를 **Public** 또는 **Private**으로 설정

#### 3단계: 원격 레포지토리 연결
```bash
git remote add origin https://github.com/YOUR_USERNAME/conex-chatbot.git
git branch -M main
git push -u origin main
```

### 🔐 API 키 보안 관리

#### 로컬 개발환경
```bash
# 방법 1: 환경 변수 설정 (권장)
$env:GROQ_API_KEY="your_actual_api_key"

# 방법 2: .env 파일 사용
copy .env.example .env
# .env 파일을 열어서 실제 API 키 입력
```

#### 배포 환경 (Heroku, Vercel 등)
- 플랫폼의 환경 변수 설정 기능 사용
- **절대** 코드에 직접 API 키 입력 금지

### ⚠️ 보안 체크리스트

#### ✅ 해야 할 것
- [x] `.gitignore`에 `.env` 포함
- [x] 환경 변수로 API 키 관리
- [x] `.env.example` 템플릿 제공
- [x] README에 설정 방법 명시

#### ❌ 하지 말아야 할 것
- [ ] API 키를 코드에 직접 입력
- [ ] `.env` 파일을 Git에 커밋
- [ ] API 키를 파일명이나 주석에 포함
- [ ] 스크린샷에 API 키 노출

### 🔍 API 키 유출 확인 방법

#### 1. Git 히스토리 확인
```bash
git log --all --grep="api" --grep="key" --grep="token" -i
```

#### 2. 파일 내용 검색
```bash
grep -r "gsk_" .
grep -r "api.key" .
```

#### 3. GitHub Secret Scanning
- GitHub는 자동으로 API 키 유출을 감지
- 유출 시 이메일 알림 발송

### 🛠️ API 키가 유출된 경우

1. **즉시 API 키 재생성**
   - Groq Console에서 기존 키 비활성화
   - 새 API 키 생성

2. **Git 히스토리 정리**
   ```bash
   # 주의: 공동 작업 시 위험할 수 있음
   git filter-branch --force --index-filter \
   'git rm --cached --ignore-unmatch app.py' \
   --prune-empty --tag-name-filter cat -- --all
   ```

3. **새 커밋으로 수정**
   ```bash
   git add .
   git commit -m "Security: Remove exposed API keys"
   git push --force
   ```

### 📊 보안 등급

| 방법 | 보안 등급 | 설명 |
|------|-----------|------|
| 환경 변수 | 🟢 매우 안전 | 권장 방법 |
| .env 파일 | 🟡 안전 | .gitignore 필수 |
| 코드 직접 입력 | 🔴 위험 | 절대 금지 |

### 🎯 추가 보안 팁

1. **API 키 로테이션**: 정기적으로 API 키 변경
2. **권한 최소화**: 필요한 권한만 부여
3. **모니터링**: API 사용량 주기적 확인
4. **팀 공유**: .env.example 파일로 안전하게 공유

---

**💡 기억하세요**: 한 번 GitHub에 올라간 API 키는 완전히 삭제하기 어렵습니다. 처음부터 안전하게 관리하는 것이 가장 좋습니다!
