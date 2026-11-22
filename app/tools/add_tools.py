from app.tools.registery import ToolRegistry 
from app.tools.calculator import calculator
def create_tool_registry() : 

    registry = ToolRegistry() 

    registry.register(
        name = "calculator" , 

        description = (
            "Perform arithmetic calculations "
            "using two numbers. Use this tool "
            "instead of calculating mentally."
        ),

        parameters={
            "type": "object",
            "properties": {
                "a": {
                    "type": "number",
                    "description": "First number"
                },
                "b": {
                    "type": "number",
                    "description": "Second number"
                },
                "operation": {
                    "type": "string",
                    "enum": [
                        "add",
                        "subtract",
                        "multiply",
                        "divide"
                    ]
                }
            },
            "required": ["a", "b", "operation"],
            "additionalProperties": False
        },

        function = calculator
    )

    return registry 
