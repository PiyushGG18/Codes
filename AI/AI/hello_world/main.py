import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://openrouter.ai/api/v1/chat/completions"
headers = {
      "Authorization": f"Bearer {os.environ.get('OPENROUTER_API_KEY')}",
      "Content-Type": "application/json"
  }

payload = {
"model": "openrouter/owl-alpha",
"messages": [
  {
    "role": "user",
    "content": "Hey There"
  }
]
}

response = requests.post(url,headers=headers, json=payload)
print(response.json()["choices"][0]["message"]["content"])

# The below code is when you have OpenAI API Key

# from openai import OpenAI
# from dotenv import load_dotenv

# load_dotenv()

# client = OpenAI()

# response = client.chat.completions.create(
#     model="inclusionai/ling-2.6-1t",
#     messages=[
#         {"role":"user","content":"Hey, I am Piyush! Nice to meet you"}
#     ]
# )

# print(response.choices[0].message.content)
