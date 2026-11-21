import os 
from dotenv import load_dotenv 
from openai import OpenAI 


load_dotenv() 

api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenev("OPENAI_BASE_URL")
model = os.getenv("OPENAI_MODEL")




if not all([api_key, base_url, model]) : 
    raise RuntimeError("Missing LLM Configuration")


client = OpenAI(
    api_key=api_key,
    base_url=base_url, 
    timeout=60,
    max_retries=2
)

message = input("Enter a message: ")

response = client.responses.create(
    model=model,
    input=message
)

print(response.output_text)