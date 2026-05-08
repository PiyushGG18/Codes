from openai import OpenAI
import os
import json
import requests
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional

load_dotenv()
API_key = os.getenv("GOOGLE_API_KEY")

client = OpenAI(
    api_key=API_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

def run_command(cmd: str):
    result = os.system(cmd)
    return result

def get_weather(city):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"
    
    return "Something went wrong"

available_tools = {
    "get_weather": get_weather,
    "run_command": run_command,
}

SYSTEM_PROMPT = """
    You're an expert AI Assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OUTPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.
    You are an AI agent that MUST operate in a strict step-by-step loop.
    You can also call a tool if required from the list of available tools.
    For every tool call wait for the observe step which is the output from the called tool.

    The user's operating system is Windows.
    Generate Windows-compatible commands only.
    Do not use Linux/macOS commands like touch, ls, rm, mv, etc.
    Use:
    - dir instead of ls
    - del instead of rm
    - move instead of mv
    - mkdir for folder creation
    - type nul > filename for file creation

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
    - TOOL

    Output format (strict):
    {"step": "START" | "PLAN" | "OUTPUT" | "TOOL", "content": "string", "tool":"string", "input": "string"}

    Available Tools:
    - get_weather(city: str): Takes city name as an input string and returns the whether info about the city
    - run_command(cmd: str): Takes the command as string and executes the command on user's system and returns the output from that command

    DO NOT:
    - Return arrays
    - Return multiple PLAN steps together
    - Add explanations outside JSON

    Example 1:
    START: {"step": "START", "content": "Hey, Can you solve 2 + 3 * 5 / 10"}
    PLAN: {"step": "PLAN", "content": "Seems like user is interested in math problem"} 
    PLAN: {"step": "PLAN", "content": "looking at the problem, we should solve this using BODMAS method"}
    PLAN: {"step": "PLAN", "content": "Yes, the BODMAS is correct thing to be done here"}
    PLAN: {"step": "PLAN", "content": "first we must multiply 3 * 5 which is 15"}
    PLAN: {"step": "PLAN", "content": "Now the new equation is 2 + 15 / 10"}
    PLAN: {"step": "PLAN", "content": "We must perform divide that is 15 / 10 = 1.5"}
    PLAN: {"step": "PLAN", "content": "Now the new equation is 2 + 1.5"}
    PLAN: {"step": "PLAN", "content": "Now finally let's perform the add 3.5"}
    PLAN: {"step": "PLAN", "content": "Great, we have solved and finally left with 3.5 as answer."}
    OUTPUT: {"step": "OUTPUT", "content": "3.5"}

    Example 2:
    START: What is the weather of Delhi?
    PLAN: {"step": "PLAN", "content": "Seems like user is interested in getting the weather of Delhi in India"} 
    PLAN: {"step": "PLAN", "content": "Let's see if we have any avaialble tool from the list of available tools "}
    PLAN: {"step": "PLAN", "content": "Great, we have get_weather tool available for this query."}
    PLAN: {"step": "PLAN", "content": "I need to call the get_weather tool for delhi as input for city"}
    PLAN: {"step": "TOOL", "tool": "get_weather", "input": "delhi"}
    PLAN: {"step": "OBSERVE", "tool": "get_weather","input": "delhi", "output": "The temp of delhi is cloudy with 20 C"}
    PLAN: {"step": "PLAN", "content": "Great, I got the weather info about the Delhi"}
    OUTPUT: {"step": "OUTPUT", "content":"The current weather in delhi is 20 C with some cloudy sky."}
"""

class MyOutputFormat(BaseModel):
    step: str = Field(..., description="The ID of the step. Example: PLAN, OUTPUT, TOOL etc")
    content: Optional[str] = Field(None, description="The optional string content for the step")
    tool: Optional[str] = Field(None, description="The ID of the tool to call")
    input: Optional[str] = Field(None, description="The input params of the tool")

message_history = [
    {"role":"system", "content": SYSTEM_PROMPT},
]
print("\n\n\n\n")

while True:
    user_query = input("👉 ")
    message_history.append({"role":"user", "content":user_query})

    while True:
        response = client.chat.completions.parse (
            model="gemini-3.1-flash-lite-preview",
            response_format=MyOutputFormat,
            messages=message_history
        )

        raw_result = response.choices[0].message.content
        # # print(raw_result)
        message_history.append({"role": "assistant", "content": raw_result})
        parsed_result = response.choices[0].message.parsed

        if parsed_result.step == "START":
            print("🔥 ", parsed_result.content)
            continue

        if parsed_result.step == "TOOL":
            tool_to_call = parsed_result.tool
            tool_input = parsed_result.input
            print(f"🔨: {tool_to_call}({tool_input})")

            tool_response = available_tools[tool_to_call](tool_input)
            print(f"🔨: {tool_to_call}({tool_input}) = {tool_response}")
            message_history.append({"role": "developer", "content": json.dumps(
                {"step": "OBSERVE", "tool": tool_to_call, "input": tool_input, "output": tool_response}
            )})
            continue

        if parsed_result.step == "PLAN":
            print("🧠 ", parsed_result.content)
            continue
        
        if parsed_result.step == "OUTPUT":
            print("🤖 ", parsed_result.content)
            break


print("\n\n\n\n")

def create_file(filename, content):
    with open(filename, 'w') as f: f.write(content)
    return f'{filename} created.'

def read_file(filename):
    with open(filename, 'r') as f: return f.read()

def list_directory(path="."):
    import os
    return str(os.listdir(path))

def delete_file(filename):
    import os
    os.remove(filename)
    return f'{filename} deleted.'

def update_file(filename, content):
    with open(filename, 'a') as f: f.write(content)
    return f'{filename} updated.'