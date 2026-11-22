from app.tools.registery import ToolRegistry 
from app.tools.calculator import calculator
from app.tools.date_time import get_current_datetime
from app.tools.web_search import web_search
from app.tools.file_reader import read_file


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



    registry.register(

        name="web_search",

        description=(
            "Search the internet for information. "
            "Use this tool for current events, "
            "recent information, technical documentation "
            "and questions requiring external sources. "
            "Returns titles, URLs and search snippets."
        ),

        parameters={
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query"
                }
            },
            "required": ["query"],
            "additionalProperties": False
        },

        function=web_search
    )


    registry.register(

        name="read_file",

        description=(
            "Read a text file from the agent workspace. "
            "Supported formats are TXT, MD, CSV and JSON and PY. "
            "The path must be relative to the workspace directory. "
            "For example: notes.md or reports/data.csv. "
            "Use this tool when the user asks to read or inspect a file."
        ),

        parameters={
            "type": "object",

            "properties": {
                "path": {
                    "type": "string",
                    "description": (
                        "Relative file path inside workspace. "
                        "Example: notes.md"
                    )
                }
            },

            "required": ["path"],

            "additionalProperties": False
        },

        function=read_file
    )

    return registry 
