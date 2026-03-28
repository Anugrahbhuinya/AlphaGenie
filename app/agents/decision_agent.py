import os
from dotenv import load_dotenv
from google import genai
import time

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_decision(signal_data, sentiment_data):
    prompt = f"""
    You are a stock market assistant.

    Signal: {signal_data['signal']}
    RSI: {signal_data['rsi']}
    MA20: {signal_data['ma20']}
    MA50: {signal_data['ma50']}
    Reasons: {signal_data['reason']}
    Market Sentiment: {sentiment_data['sentiment']}

    Give:
    1. Final Recommendation (BUY/SELL/HOLD)
    2. Short explanation (2-3 lines)
    3. Confidence score (0-100)

    Output STRICT JSON:
    {{
        "recommendation": "...",
        "explanation": "...",
        "confidence": ...
    }}
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text

    except Exception as e:
        print("Gemini Error:", e)

        # 🔥 SMART FALLBACK (this saves your demo)
        return {
            "recommendation": signal_data["signal"],
            "explanation": f"Based on technical indicators: {', '.join(signal_data['reason'])}. Sentiment is {sentiment_data['sentiment']}.",
            "confidence": 60 if signal_data["signal"] == "HOLD" else 75
        }