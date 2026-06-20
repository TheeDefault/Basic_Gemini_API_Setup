from google import genai
import os
from proompt import prompt

key = os.environ.get("API_KEY")

# This will now work because it uses the correct google-genai library!
client = genai.Client(api_key=key)

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt
)
print(response.text)