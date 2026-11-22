import json 
from dataclasses import dataclass 
from typing import Any, Callable 

@dataclass 
class RegisteredTool : 

    name: str 
    description : str 
    parameters: dict[str, Any] 
    function : Callable


class ToolRegistry : # _> add a list of tools with their use to parse into the LLM  request
    def __init__(self) : 
        self._tools: dict[str, RegisteredTool] = {}


    def register(
        self, 
        name: str, 
        description: str , 
        parameters: dict[str, Any] , 
        function: Callable
    ) : 

        if name in self._tools : 
            raise ValueError(f"Tool already registered: {name}")

    

        self._tools[name] = RegisteredTool(
            name=name,
            description=description,
            parameters=parameters,
            function=function  )

    def get_definitions(self) -> list[dist] : 

        definitions = [] 

        for tool in self._tools.values() : 

            definitions.append({
                "type" : "function" , 
                "function" : {
                    "name" : tool.name, 
                    "description" : tool.description,
                    "parameters" : tool.parameters
                }
            })

        return definitions 


    # excecute the selected tool and return the response 

    def execute(self, name: str, arguments: str) -> dict : 
        tool = self._tools.get(name)

        if tool is None : 
            return {"error" : f"Unknown tool name: {name}"}

        

        try : 
            parsed_arguments = json.loads(arguments)

            if not isinstance(parsed_arguments, dict) : 
                return {"error"  : "Tool arguments must be a JSON object"}

            result = tool.function(**parsed_arguments)

            return {"success" : True, "data" : result}


        except (json.JSONDecodeError, TypeError, ValueError) as error : 

            return {
                "success" : False, 
                "error" : str(error)
            }