import os 
from dotenv import load_dotenv 
from openai import OpenAI 

from app.agent import Agent 
from app.llm import LLMClient

from app.tools.registery import ToolRegistry 
from app.tools.calculator import calculator

from app.tools.add_tools import create_tool_registry 

def main() : 

    load_dotenv() 

    api_key = os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("OPENAI_BASE_URL")
    model = os.getenv("OPENAI_MODEL")

    if not all([api_key, base_url, model]) : 
        raise RuntimeError("LLM missing configuration")

    tools = create_tool_registry() 

    llm = LLMClient()
    agent = Agent(llm, tools)

    print("Personal Agent started...")
    print("Commands: /reset , /exit")

    while True : 

        user_input = input("\n>> ").strip() 

        if user_input.strip() == "/exit" : 
            print("Agent stoped")
            break 

        if user_input.strip() == "/reset" : 
            agent.reset() 
            print("Conversation history cleaned!")
            continue 


        if not user_input : 
            continue 


        try : 
            response = agent.run(user_input=user_input)
            print(f"\nAgent : {response}")


        except Exception as exc : 
            print(f"\nError : {exc}")
        


if __name__ == "__main__" : 
    main()