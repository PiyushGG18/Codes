from openai import OpenAI
import os
import json
from dotenv import load_dotenv

load_dotenv()
API_key = os.getenv("GOOGLE_API_KEY")

client = OpenAI(
    api_key=API_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = """
    You're an expert AI Assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OUTPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.
    You are an AI agent that MUST operate in a strict step-by-step loop.

    Rules:
    - You MUST return ONLY ONE step at a time.
    - Never return multiple steps.
    - Never return a list.
    - Each response must be exactly ONE JSON object.
    - After each step, wait for the next input.

    Allowed steps:
    - START
    - PLAN
    - OUTPUT

    Output format (strict):
    {"step": "START" | "PLAN" | "OUTPUT", "content": "string"}

    DO NOT:
    - Return arrays
    - Return multiple PLAN steps together
    - Add explanations outside JSON

    Example:
    START: {"step": "START", "content": "Hey, Can you solve 2 + 3 * 5 / 10"}
    PLAN: {"step": "PLAN", "content": "Seems like user is interested in math problem"} 
    PLAN: {"step": "PLAN", "content": "looking at the problem, we should solve this using BODMAS method"}
    PLAN: {"step": "PLAN", "content": "Yes, the BODMAS is correct thing to be done here}
    PLAN: {"step": "PLAN", "content": "first we must multiply 3 * 5 which is 15"}
    PLAN: {"step": "PLAN", "content": "Now the new equation is 2 + 15 / 10"}
    PLAN: {"step": "PLAN", "content": "We must perform divide that is 15 / 10 = 1.5"}
    PLAN: {"step": "PLAN", "content": "Now the new equation is 2 + 1.5"}
    PLAN: {"step": "PLAN", "content": "Now finally let's perform the add 3.5"}
    PLAN: {"step": "PLAN", "content": "Great, we have solved and finally left with 3.5 as answer.}
    OUTPUT: {"step": "OUTPUT", "content": "3.5"}
"""

message_history = [
    {"role":"system", "content": SYSTEM_PROMPT},
]
print("\n\n\n\n")
user_query = input("👉 ")
message_history.append({"role":"user", "content":user_query})

while True:
    response = client.chat.completions.create (
        model="gemini-3.1-flash-lite-preview",
        response_format={"type":"json_object"},
        messages=message_history
    )

    raw_result = response.choices[0].message.content
    # print(raw_result)
    message_history.append({"role": "assistant", "content": raw_result})
    parsed_result = json.loads(raw_result)

    if parsed_result.get("step") == "START":
        print("🔥 ", parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "PLAN":
        print("🧠 ", parsed_result.get("content"))
        continue
    
    if parsed_result.get("step") == "OUTPUT":
        print("🤖 ", parsed_result.get("content"))
        break


print("\n\n\n\n")