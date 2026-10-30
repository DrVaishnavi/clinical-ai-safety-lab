"""
test_keys.py - checks that both free API keys work.
Run with:  python test_keys.py

Model names change often. If a model name stops working, this script
prints the models your key CAN use, so you can copy a new name in.
"""
import os
from dotenv import load_dotenv  # reads the keys from your .env file

load_dotenv()

QUESTION = "In one sentence, what is infective endocarditis?"

# Change these two lines if a model name stops working
GEMINI_MODEL = "gemini-3.8-flash"
GROQ_MODEL = "openai/gpt-oss-120b"

# ---------- 1. Gemini (Google AI Studio) ----------
print("Testing Gemini...")
try:
    from google import genai
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    reply = client.models.generate_content(model=GEMINI_MODEL, contents=QUESTION)
    print("Gemini works:", reply.text.strip(), "\n")
except Exception as error:
    print("Gemini failed:", error, "\n")

# ---------- 2. Groq ----------
print("Testing Groq...")
try:
    from groq import Groq
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    try:
        reply = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[{"role": "user", "content": QUESTION}],
        )
        print("Groq works:", reply.choices[0].message.content.strip())
    except Exception as error:
        print("Groq model failed:", error)
        print("Models your Groq key can use:")
        for m in client.models.list().data:
            print("  -", m.id)
except Exception as error:
    print("Groq failed:", error)
