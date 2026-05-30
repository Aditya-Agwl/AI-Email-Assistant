import sqlite3
import json
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_sql(user_query):

    prompt = f"""
    You are a SQLite expert.

    Table name: emails

    Columns:
    - id
    - sender
    - subject
    - category
    - priority
    - summary

    Return ONLY valid SQL.

    User Request:
    {user_query}
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    sql_query = response.text.strip()

    sql_query = sql_query.replace("```sql", "")
    sql_query = sql_query.replace("```", "")

    return sql_query.strip()

def execute_query(sql_query):

    if not sql_query.upper().startswith("SELECT"):
        raise Exception(
            "Only SELECT queries allowed"
        )

    conn = sqlite3.connect("emails.db")

    cursor = conn.cursor()

    cursor.execute(sql_query)

    rows = cursor.fetchall()

    conn.close()

    return rows