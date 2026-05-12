from google import genai
import os

client = genai.Client(api_key="")

for m in client.models.list():
    if "tts" in m.name.lower():
        print(m.name)