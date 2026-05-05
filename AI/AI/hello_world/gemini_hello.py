from google import genai
import os

API_key=os.get("GOOGLE_API_KEY")
client = genai.Client(
    api_key=API_key
)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Hello My name is Piyush"
)

print(response.text)