# 🤖 Conex 챗봇 - Groq API 가이드

## 📋 프로젝트 소개

Groq API를 사용한 고품질 AI 챗봇입니다. Groq은 매우 빠른 추론 속도를 자랑하며, 무료 티어를 제공하여 비용 부담 없이 고품질 AI 챗봇을 구현할 수 있습니다.

### ✨ 주요 특징
- 🚀 **초고속 응답**: Groq의 LPU(Language Processing Unit) 기술로 매우 빠른 응답
- 💰 **무료 사용**: 월 1만 토큰 무료 제공 (일반적인 대화 2,000~3,000회)
- 🎨 **모던 UI**: 글래스모피즘 디자인의 아름다운 인터페이스
- 📱 **반응형 디자인**: 모든 디바이스에서 완벽한 사용자 경험
- 🌐 **다국어 지원**: 한국어 최적화

## 🚀 빠른 시작

### 1단계: Groq API 키 받기

1. **Groq 콘솔 방문**: https://console.groq.com
2. **회원가입/로그인**: Google, GitHub 계정으로 간편 가입
3. **API 키 생성**: 
   - 좌측 메뉴에서 "API Keys" 클릭
   - "Create API Key" 버튼 클릭
   - 키 이름 입력 후 생성
   - 🔐 **중요**: API 키를 안전한 곳에 저장 (다시 볼 수 없음)

### 2단계: 환경 설정

#### Python 환경 확인
```bash
py --version  # Python 3.7 이상 필요 (Windows에서는 py 사용)
```

#### 필요한 패키지 설치
```bash
# Flask 및 Groq 패키지 설치 (Windows)
py -m pip install -r requirements.txt

# 또는 개별 설치
py -m pip install flask groq
```

### 3단계: API 키 설정 (보안)

#### 방법 1: 환경 변수 설정 (권장 🔐)
```bash
# Windows (PowerShell)
$env:GROQ_API_KEY="your_groq_api_key_here"

# Windows (CMD)
set GROQ_API_KEY=your_groq_api_key_here

# macOS/Linux
export GROQ_API_KEY="your_groq_api_key_here"
```

#### 방법 2: .env 파일 사용 (로컬 개발용)
```bash
# .env.example을 .env로 복사
copy .env.example .env

# .env 파일을 열어서 실제 API 키 입력
GROQ_API_KEY=your_actual_groq_api_key
```

⚠️ **중요**: `.env` 파일은 Git에 커밋되지 않습니다 (보안)

### 4단계: 애플리케이션 실행

```bash
# 현재 디렉토리로 이동
cd "c:\Users\David Jung\Desktop\Conex Chatbot"

# Flask 앱 실행 (Windows)
py app.py

# 또는 배치 파일 사용
start.bat
```

브라우저에서 `http://localhost:5000` 접속! 🎉

## 📁 프로젝트 구조

```
Conex Chatbot/
├── app.py                 # 메인 Flask 애플리케이션 (Groq API)
├── app_groq.py           # Groq API 버전
├── app_simple.py         # 규칙 기반 버전
├── app_ollama.py         # Ollama 버전
├── app_huggingface.py    # Hugging Face 버전
├── app_claude.py         # Claude API 버전
├── templates/
│   └── index.html        # 메인 웹 인터페이스
├── requirements.txt      # Python 패키지 목록
├── README.md            # 이 파일
└── README_FREE.md       # 무료 옵션 가이드
```

## 🔧 Groq API 상세 설정

### 사용 가능한 모델들

| 모델명 | 특징 | 권장 사용처 |
|--------|------|-------------|
| `llama3-8b-8192` | 빠르고 효율적 | 일반 대화, 빠른 응답 |
| `llama3-70b-8192` | 높은 품질 | 복잡한 질문, 깊이 있는 대화 |
| `mixtral-8x7b-32768` | 긴 컨텍스트 | 긴 문서 분석, 요약 |
| `gemma-7b-it` | 가벼움 | 단순한 작업 |

### 응답 품질 튜닝

`app.py`에서 다음 파라미터들을 조정할 수 있습니다:

```python
chat_completion = client.chat.completions.create(
    messages=[...],
    model="llama3-8b-8192",      # 모델 선택
    temperature=0.7,             # 창의성 (0.0-2.0)
    max_tokens=1000,             # 최대 토큰 수
    top_p=1.0,                   # 다양성 제어
    stop=None,                   # 중단 조건
)
```

#### 파라미터 설명:
- **temperature**: 
  - `0.0-0.3`: 일관되고 예측 가능한 답변
  - `0.4-0.7`: 균형잡힌 창의성 (권장)
  - `0.8-2.0`: 매우 창의적이고 다양한 답변

- **max_tokens**: 
  - 한국어 기준 토큰당 약 0.7-1글자
  - 1000 토큰 ≈ 700-1000글자

## 💰 Groq 요금 및 제한사항

### 무료 티어
- ✅ **월 1만 토큰 무료**
- ✅ **초당 30 요청**
- ✅ **분당 14,000 토큰**

### 예상 사용량
- 짧은 대화 (50토큰): **월 200회**
- 보통 대화 (150토큰): **월 66회**
- 긴 대화 (500토큰): **월 20회**

### 사용량 확인
```python
# app.py에 추가하여 토큰 사용량 확인
print(f"사용된 토큰: {chat_completion.usage.total_tokens}")
```

## 🛠️ 커스터마이징 가이드

### 시스템 프롬프트 변경

`app.py`의 `SYSTEM_PROMPT`를 수정하여 AI의 성격을 변경할 수 있습니다:

```python
# 친근한 상담사
SYSTEM_PROMPT = """
너는 따뜻하고 친근한 상담사야. 사용자의 고민을 공감하며 들어주고, 
실용적이면서도 따뜻한 조언을 해줘. 반말로 편하게 대화해.
"""

# 전문 멘토
SYSTEM_PROMPT = """
너는 경험이 풍부한 멘토야. 사용자의 문제를 분석하고 구체적인 해결책을 제시해줘.
논리적이고 체계적인 조언을 해줘.
"""

# 재미있는 친구
SYSTEM_PROMPT = """
너는 유머 감각이 있는 친구야. 재미있고 밝은 에너지로 대화하며,
사용자의 기분을 좋게 만들어줘. 이모지도 적절히 사용해줘.
"""
```

### UI 커스터마이징

`templates/index.html`에서 다음을 변경할 수 있습니다:

- **색상 테마**: CSS 그라데이션 색상 변경
- **폰트**: `font-family` 속성 수정
- **레이아웃**: 컨테이너 크기 및 배치 조정
- **애니메이션**: 호버 효과 및 전환 애니메이션

## 🔍 문제 해결

### 자주 발생하는 오류

#### 1. ImportError: No module named 'groq'
```bash
# 해결: Groq 패키지 설치
pip install groq
```

#### 2. Authentication Error
```bash
# 해결: API 키 확인
# 1. API 키가 올바른지 확인
# 2. 환경 변수가 제대로 설정되었는지 확인
echo $GROQ_API_KEY  # macOS/Linux
echo $env:GROQ_API_KEY  # Windows PowerShell
```

#### 3. Rate Limit Exceeded
```bash
# 해결: 요청 간격 조정
# app.py에 딜레이 추가
import time
time.sleep(1)  # 1초 대기
```

#### 4. 한국어 인코딩 문제
```python
# app.py 파일 상단에 추가
# -*- coding: utf-8 -*-
```

### 성능 최적화

#### 1. 모델 선택 최적화
```python
# 빠른 응답이 필요한 경우
model="llama3-8b-8192"

# 품질이 중요한 경우
model="llama3-70b-8192"
```

#### 2. 토큰 사용량 최적화
```python
# 시스템 프롬프트를 간결하게 작성
# max_tokens을 적절히 제한
max_tokens=500  # 기본값에서 줄임
```

## 🚀 배포 가이드

### GitHub Pages 알림
⚠️ **중요**: GitHub Pages는 정적 사이트만 호스팅할 수 있어서 Flask 백엔드가 작동하지 않습니다. 
실제 챗봇을 사용하려면 아래 클라우드 플랫폼 중 하나를 선택하여 배포하세요.

### 무료 클라우드 배포 옵션

#### 1. Heroku 배포 (추천 🌟)

**1단계: Heroku 계정 생성**
- https://heroku.com 에서 무료 계정 생성

**2단계: 배포 파일 준비**
```bash
# Procfile 생성
echo "web: python app.py" > Procfile

# 포트 설정을 위해 app.py 수정 필요
```

**3단계: Heroku CLI로 배포**
```bash
# Heroku CLI 설치 후
heroku login
heroku create your-chatbot-name
heroku config:set GROQ_API_KEY=your_actual_api_key
git push heroku main
```

#### 2. Replit 배포 (가장 쉬움 🎯)

**1단계: Replit에서 프로젝트 가져오기**
- https://replit.com 접속
- "Import from GitHub" 선택
- 레포지토리 URL 입력

**2단계: 환경 변수 설정**
- Secrets 탭에서 `GROQ_API_KEY` 추가

**3단계: 실행**
- Run 버튼 클릭하면 바로 배포 완료!

#### 3. Vercel 배포

**1단계: Vercel 계정 연결**
- https://vercel.com 에서 GitHub 연결

**2단계: 프로젝트 가져오기**
- GitHub 레포지토리 선택하여 자동 배포

**3단계: 환경 변수 설정**
- Settings > Environment Variables에서 `GROQ_API_KEY` 추가

#### 4. Railway 배포

**1단계: Railway 연결**
- https://railway.app 에서 GitHub 연결

**2단계: 배포**
- 프로젝트 선택하면 자동 배포

**3단계: 환경 변수**
- Variables 탭에서 `GROQ_API_KEY` 설정

### GitHub에 안전하게 올리기

#### 1단계: Git 초기화
```bash
git init
git add .
git commit -m "Initial commit: Conex Chatbot"
```

#### 2단계: GitHub 레포지토리 생성 및 푸시
```bash
git remote add origin https://github.com/YOUR_USERNAME/conex-chatbot.git
git branch -M main
git push -u origin main
```

✅ **보안이 보장됩니다**: API 키는 `.gitignore`로 제외됨

### 로컬 네트워크에서 접근

```python
# app.py 마지막 부분 수정
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
```

같은 네트워크의 다른 기기에서 `http://YOUR_IP:5000`으로 접근 가능

### 클라우드 배포 (Heroku)

1. **Procfile 생성**:
```
web: python app.py
```

2. **requirements.txt 생성**:
```
flask==2.3.3
groq==0.4.1
```

3. **환경 변수 설정**:
Heroku 대시보드에서 `GROQ_API_KEY` 설정

## 📞 지원 및 피드백

- **Groq 공식 문서**: https://console.groq.com/docs
- **GitHub Issues**: 버그 리포트 및 기능 요청
- **Discord 커뮤니티**: 실시간 도움말

## 📄 라이선스

MIT License - 자유롭게 사용, 수정, 배포 가능

---

## 🎯 다음 단계

1. ✅ Groq API 키 받기
2. ✅ 패키지 설치
3. ✅ 앱 실행
4. 🎨 UI 커스터마이징
5. 🧠 프롬프트 최적화
6. 🚀 배포

**즐거운 챗봇 개발되세요!** 🎉
