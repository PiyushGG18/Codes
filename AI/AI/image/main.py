from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"  # note: /openai/ at the end
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",  # vision-capable model
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Generate a caption for this image in about 50 words"},
                {"type": "image_url", "image_url": {"url": "https://i.etsystatic.com/49105148/r/il/59d360/5773872391/il_1080xN.5773872391_iscw.jpg"}}
            ]
        }
    ]
)

print("Response: ", response.choices[0].message.content)