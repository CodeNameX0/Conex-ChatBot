from flask import Flask, request, jsonify
import os

def handler(request):
    api_key = os.getenv('GROQ_API_KEY')
    
    return jsonify({
        'api_key_set': bool(api_key and api_key not in ["YOUR_GROQ_API_KEY", "your_groq_api_key_here"]),
        'api_key_length': len(api_key) if api_key else 0,
        'environment': 'vercel' if os.getenv('VERCEL') else 'local',
        'vercel_env': os.getenv('VERCEL_ENV', 'unknown')
    })
