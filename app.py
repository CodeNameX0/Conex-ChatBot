from flask import Flask, render_template, request
from groq import Groq
import os
from dotenv import load_dotenv

# .env 파일 로드 (있는 경우)
load_dotenv()

app = Flask(__name__)

# Groq API 키 설정 (보안 우선순위: 환경변수 > .env 파일)
api_key = os.getenv('GROQ_API_KEY')

# API 키 유효성 검사
if not api_key or api_key == "YOUR_GROQ_API_KEY" or api_key == "your_groq_api_key_here":
    print("🚨 보안 오류: API 키가 설정되지 않았습니다!")
    print()
    print("📋 안전한 설정 방법:")
    print("1. https://console.groq.com 에서 API 키 받기")
    print("2. 환경 변수 설정:")
    print("   Windows: $env:GROQ_API_KEY='your_actual_api_key'")
    print("   Linux/Mac: export GROQ_API_KEY='your_actual_api_key'")
    print("3. 또는 .env 파일 생성:")
    print("   .env.example을 .env로 복사하고 실제 API 키 입력")
    print()
    print("⚠️  절대 코드에 직접 API 키를 입력하지 마세요!")
    exit(1)

client = Groq(api_key=api_key)

SYSTEM_PROMPT = """
너는 지적이고 침착한 조언자야. 말투는 반말로 하고, 사용자에게 논리적이고 깊이 있는 생각을 던져줘.
감정을 읽되, 감정에 휘둘리지 않고, 명확하고 사실에 기반한 조언을 해. 필요하면 예시나 비유를 사용하고,
대화는 자연스럽고 인간적인 어조를 유지해. 또한 답변 언어는 기본 한국어로 해주고, 사용자가 다른 언어로 해달라고 하면 그 언어로 해줘야 해.
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.form["user_input"]
    
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ],
            model="llama3-8b-8192",  # 빠르고 효율적인 모델
            temperature=0.7,         # 적당한 창의성
            max_tokens=1000,         # 충분한 답변 길이
            top_p=1.0,
            stop=None,
        )
        
        response = chat_completion.choices[0].message.content
        
        # 선택사항: 토큰 사용량 로깅
        print(f"토큰 사용량: {chat_completion.usage.total_tokens}")
        
        return response.strip()
        
    except Exception as e:
        error_msg = str(e)
        if "authentication" in error_msg.lower():
            return "❌ API 키를 확인해주세요. README.md의 설정 가이드를 참고하세요."
        elif "rate_limit" in error_msg.lower():
            return "⏰ 요청이 너무 많습니다. 잠시 후 다시 시도해주세요."
        elif "quota" in error_msg.lower():
            return "💰 월 사용량을 초과했습니다. 다음 달에 다시 이용해주세요."
        else:
            return f"😅 오류가 발생했습니다: {error_msg}"

if __name__ == "__main__":
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

# Vercel을 위한 WSGI 설정
# Vercel은 이 변수를 찾아서 앱을 실행합니다
handler = app
