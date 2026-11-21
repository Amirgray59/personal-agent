import os 
from dotenv import load_dotenv 
from openai import OpenAI 
from app.llm import client

load_dotenv() 

api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_BASE_URL")
model = os.getenv("OPENAI_MODEL")





message = input("Enter a message: ")

response = client.responses.create(
    model=model,
    input=message
)

print(response.output_text)

