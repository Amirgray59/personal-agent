from app.tools.registery import ToolRegistry 
from app.tools.calculator import calculator
from app.tools.date_time import get_current_datetime


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


    registry.register(

        name="get_current_datetime",

        description=(
            "Get the current date and time "
            "for a specified IANA timezone. "
            "Use this tool when the user asks "
            "about the current date, time or day." 
            "give the timezone of Tehran by default if users didnt specifie"
        ),

        parameters={
            "type": "object",
            "properties": {
                "timezone": {
                    "type": "string",
                    "description": (
                        "IANA timezone, for example "
                        "Asia/Baku, Asia/Tehran or UTC"
                    )
                }
            },
            "required": ["timezone"],
            "additionalProperties": False
        },

        function=get_current_datetime
    )

    return registry 
