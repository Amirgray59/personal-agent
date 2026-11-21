import os 
from dotenv import load_dotenv 
from openai import OpenAI 


class LLMClient: 

    def __init__(self) : 

        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_BASE_URL"),
            timeout=60, 
            max_retries=2 
        )

        self.model = os.getenv("OPENAI_MODEL")



    def generate(self, messages: list[dict[str,str]]) -> str : 

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages, 
            temperature=.2 
        )

        content = response.choices[0].message.content

        if not content : 
            raise RuntimeError("LLM returend an empty message")


        return content 