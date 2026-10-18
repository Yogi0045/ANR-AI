import os
from dotenv import load_dotenv
from google import genai
from datetime import date

load_dotenv()


client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def extract_entries(input:str):
    today = date.today().isoformat("DD-MM-YYYY")

    prompt = f"""
    Extract every income and expense entry from the shopkeeper's message.

    Return valid JSON in this exact format:
    {{
        "entries": [
            {{
                "date": "{today}",
                "time_slot": "morning/evening/unknown",
                "type": "income/expense",
                "category": "category name",
                "amount": 0,
                "cash": 0,
                "upi": 0,
                "description": "short description"
            }}
        ]
    }}

    Rules:
    - Create a separate entry for each income or expense.
    - If the date is not mentioned, use today's date.
    - Never Invent a Date 
    - If the time slot is unclear, use "unknown".
    - If cash and UPI amounts are not mentioned separately,
    use 0 for both. Never guess.
    - If the payment method is unknown, keep cash and upi as 0.
    - Amount is the total transaction amount.
    - Do not combine separate transactions into one entry.

    Message: {input}
    """


    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents = prompt,
        config = {
            "response_mime_type": "application/json",
        })

    return response.text