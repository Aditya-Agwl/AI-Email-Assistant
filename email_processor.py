from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))

def analyze_email(email_text):

    prompt = f"""
    Analyze the following email.

    Return ONLY valid JSON in this format:

    {{
      "category": "",
      "priority": "",
      "summary": "",
      "action_items": [],
      "suggested_reply": ""
    }}

    Categories can be:
    - job
    - meeting
    - spam
    - personal
    - work
    - finance
    - other

    Priorities can be:
    - low
    - medium
    - high

    Email:
    {email_text}
    """

    response = client.models.generate_content(contents=prompt, model="gemini-3.5-flash")

    return response.text