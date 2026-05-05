from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
API_key=os.getenv("GOOGLE_API_KEY")

client = OpenAI(
    api_key= API_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = "You should answer only and only the coding related questions. Do not ans anything else. Your name is Alexa. If user asks anything else just answer sorry. you can tell them your name"

response = client.chat.completions.create(
    model="gemini-3.1-flash-lite-preview",
    messages=[
        {"role":"system","content": SYSTEM_PROMPT},
        {"role":"user","content":"Hey myself Piyush, what is your name. Can you write a python code to translate hello to hindi"}
    ]
)

print(response.choices[0].message.content)

# 1. Zero-shot prompting: The model is given a direct question or task without prior examples.