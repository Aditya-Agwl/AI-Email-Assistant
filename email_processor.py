from google import genai
from dotenv import load_dotenv
import os
import json
from tools import (
    schedule_meeting,
    send_priority_alert,
    archive_spam
)

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
- interview
- meeting
- finance
- promotion
- newsletter
- security
- github
- social
- personal
- work
- spam  
- other    

    Priorities can be:
    - low
    - medium
    - high

    Email:
    {email_text}
    """

    response = client.models.generate_content(contents=prompt, model="gemini-3.5-flash")

    cleaned_response = response.text.strip()

    cleaned_response = cleaned_response.replace("```json", "")
    cleaned_response = cleaned_response.replace("```", "")

    try:
        parsed_json = json.loads(cleaned_response)
        return parsed_json

    except json.JSONDecodeError:
        return {
            "error": "Invalid JSON response",
            "raw_response": response.text
        }
    
def decide_and_execute_tool(email_data):

    category = email_data.get("category")
    priority = email_data.get("priority")

    if priority == "high":
        send_priority_alert()

    if category == "meeting":
        schedule_meeting(
            date="next Tuesday",
            time="3 PM"
        )

    elif category == "spam":
        archive_spam()

    else:
        print("\n📩 No special tool triggered")