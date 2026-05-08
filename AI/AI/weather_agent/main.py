from openai import OpenAI
import os
import requests
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)



def main():
    user_query = input("> ")
    response = client.chat.completions.create(
        model="gemini-3.1-flash-lite-preview",
        messages=[
            {"role": "user", "content": user_query}
        ]
    )

    print(f"🤖: {response.choices[0].message.content}")


