from flask import Flask, request
from groq import Groq
import os
from dotenv import load_dotenv

# .env 파일 로드 (있는 경우)
load_dotenv()

# Groq API 키 설정
api_key = os.getenv('GROQ_API_KEY')

SYSTEM_PROMPT = """
너는 지적이고 침착한 조언자야. 말투는 반말로 하고, 사용자에게 논리적이고 깊이 있는 생각을 던져줘.
감정을 읽되, 감정에 휘둘리지 않고, 명확하고 사실에 기반한 조언을 해. 필요하면 예시나 비유를 사용하고,
대화는 자연스럽고 인간적인 어조를 유지해. 또한 답변 언어는 기본 한국어로 해주고, 사용자가 다른 언어로 해달라고 하면 그 언어로 해줘야 해.
"""

def handler(request):
    if request.method == 'POST':
        user_input = request.form.get("user_input", "")
        
        # API 키 확인
        if not api_key or api_key in ["YOUR_GROQ_API_KEY", "your_groq_api_key_here"]:
            return "❌ API 키가 설정되지 않았습니다."
        
        try:
            client = Groq(api_key=api_key)
            
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_input}
                ],
                model="llama3-8b-8192",
                temperature=0.7,
                max_tokens=1000,
                top_p=1.0,
                stop=None,
            )
            
            response = chat_completion.choices[0].message.content
            return response.strip()
            
        except Exception as e:
            error_msg = str(e)
            if "authentication" in error_msg.lower():
                return "❌ API 키를 확인해주세요."
            elif "rate_limit" in error_msg.lower():
                return "⏰ 요청이 너무 많습니다. 잠시 후 다시 시도해주세요."
            elif "quota" in error_msg.lower():
                return "💰 월 사용량을 초과했습니다."
            else:
                return f"😅 오류가 발생했습니다: {error_msg}"
    
    return "Method not allowed"
