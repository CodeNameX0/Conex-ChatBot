@echo off
echo 🤖 Conex 챗봇 - Groq API 설정 및 실행
echo ================================

echo.
echo 1단계: Python 확인...
py --version
if %errorlevel% neq 0 (
    echo ❌ Python이 설치되지 않았습니다.
    echo 📥 https://python.org 에서 Python을 다운로드하여 설치하세요.
    pause
    exit /b 1
)

echo.
echo 2단계: 필요한 패키지 설치 중...
py -m pip install -r requirements.txt

echo.
echo 3단계: API 키 확인...
if "%GROQ_API_KEY%"=="" (
    echo ❌ GROQ_API_KEY 환경 변수가 설정되지 않았습니다.
    echo.
    echo 📋 설정 방법:
    echo 1. https://console.groq.com 에서 API 키 받기
    echo 2. PowerShell에서 다음 명령 실행:
    echo    $env:GROQ_API_KEY="your_api_key_here"
    echo 3. 또는 app.py 파일에서 직접 수정
    echo.
    echo ⚠️  환경 변수 없이 app.py에서 직접 설정하셔도 됩니다.
    echo.
) else (
    echo ✅ API 키가 설정되었습니다!
)

echo.
echo 4단계: Flask 애플리케이션 시작...
echo 🌐 브라우저에서 http://localhost:5000 으로 접속하세요!
echo ⏹️  종료하려면 Ctrl+C를 누르세요.
echo.
py app.py

pause
