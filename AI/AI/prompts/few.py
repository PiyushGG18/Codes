from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
API_key=os.getenv("GOOGLE_API_KEY")

client = OpenAI(
    api_key= API_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# Few shot prompting: directly giving the instruction and few examples to the model

SYSTEM_PROMPT = """
You should answer only and only the coding related questions. Do not ans anything else. 
Your name is Alexa. If user asks anything else just answer sorry. you can tell them your name

Rule:
- Strictly follow the output in JSON format

Output format:
{{
    "code": "string" or null,
    "isCodingQuestion" boolean
}}

Examples:
Q: Can you explain the a + b whole square?
A: {{ "code": null, "isCodingQuestion": false }}

Q: Hey, write a code in python for adding two numbers.
A: {{ "code": "def add(a, b):
                return a + b", "isCodingQuestion": true }}

"""

response = client.chat.completions.create(
    model="gemini-3.1-flash-lite-preview",
    messages=[
        {"role":"system","content": SYSTEM_PROMPT},
        {"role":"user","content":"Hey myself Piyush, what is your name. Can you write a C++ code to take sum of array of size n"}
    ]
)

print(response.choices[0].message.content)

# 1. Few-shot Prompting: The model is provided with a few examples before asking it to generate a response.