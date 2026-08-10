from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
API_key = os.get("GOOGLE_API_KEY")

client = OpenAI(
    api_key=API_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

response = client.chat.completions.create(
    model="gemini-3.1-flash-lite-preview",
    messages=[
        {"role":"system","content":"You are an expert in Maths and only and only ans maths related questions. That if the query is not related to maths, just say sorry and do not answer the question."},
        {"role":"user","content":"Hey, can you help me in answering what is a - b whole cube"}
    ]
)

print(response.choices[0].message.content)