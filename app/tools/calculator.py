import math
def calculator(
    a: int | float,
    b: int | float,
    operation: str
) -> dict:

    print("\n[ToolCall] Using calculator ...")

    if isinstance(a, bool) or not isinstance(a, (int, float)):
        raise ValueError("First operand must be a number")

    if isinstance(b, bool) or not isinstance(b, (int, float)):
        raise ValueError("Second operand must be a number")

    if not math.isfinite(a) or not math.isfinite(b):
        raise ValueError("Operands must be finite numbers")

    operations = {
        "add": lambda: a + b,
        "subtract": lambda: a - b,
        "multiply": lambda: a * b,
        "divide": lambda: a / b,
    }

    if operation not in operations:
        raise ValueError("Unsupported operation")

    if operation == "divide" and b == 0:
        raise ValueError("Division by zero is not allowed")

    result = operations[operation]()

    return {
        "a": a,
        "b": b,
        "operation": operation,
        "result": result
    }