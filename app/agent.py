from app.llm import LLMClient
from app.tools.registery import ToolRegistry
import json 

from typing import Any 


class Agent:

    def __init__(
        self, llm: LLMClient, 
        tools: ToolRegistry,    # give the agent tools class to check and run tools 
        max_tool_rounds: int = 5
    ):

        self.llm = llm
        self.tools = tools 
        self.max_tool_rounds = max_tool_rounds

        # also defined the tools at system prompt
        self.system_message = {
            "role": "system",
            "content": """
            You are a helpful AI assistant.

            Available tools:

            1. calculator:
            Use for arithmetic calculations.

            2. get_current_datetime:
            Use for current date and time questions.

            Never guess current date or time.
            Use the appropriate tool when needed.

            Only claim a tool was executed
            if it was actually called.
            
            Respond in the same language as the user.

            Your developer's name is Amir 
            """
        }

        self.messages = [self.system_message.copy()]

    def run(self, user_input: str) -> str:

        if not user_input.strip():
            raise ValueError("User input cannot be empty")

        
        history_length = len(self.messages)

        self.messages.append({
            "role": "user",
            "content": user_input,
        })

        try:

            tool_rounds = 0 


            while True : 

                
                # Ask LLM 
                response = self.llm.generate(
                    messages= self.messages ,
                    tools = self.tools.get_definitions()
                )



                # Save LLM response message 
                self.messages.append(
                    response.model_dump(exclude_none=True)
                )


                # Check if LLM not requested a tool (use a normal response) 
                if not response.tool_calls: 
                    answer = response.content or "" 

                    if not answer.strip() : 
                        raise RuntimeError("LLM returned an empty response")

                    return answer 

                
                # check the tool count call limit 
                if tool_rounds >= self.max_tool_rounds : 
                    raise RuntimeError("Maximum tool rounds exceeded")



                for tool_call in response.tool_calls : 

                    tool_name = tool_call.function.name 


                    tool_argument = tool_call.function.arguments     


                    result = self.tools.execute(
                        name=tool_name, 
                        arguments=tool_argument
                    )

                
                    self.messages.append({
                        "role" : "tool", 
                        "tool_call_id" : tool_call.id, 
                        "name" : tool_name , 
                        "content" : json.dumps(
                            result, 
                            ensure_ascii=False 
                        )
                    })

                tool_rounds += 1 
                




        except Exception:
            del self.messages[history_length: ]
            raise 

    def reset(self):

        self.messages = [self.system_message.copy()]