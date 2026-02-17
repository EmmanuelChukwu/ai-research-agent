from langchain.tools import tool
import math
from typing import Union

@tool
def calculator(expression: str) -> Union[float, str]:
    """
    Evaluate mathematical expressions and perform calculations.
    Supports basic arithmetic (+, -, *, /), powers (**), and common functions (sqrt, sin, cos, log, etc).
    Example: "2 + 2", "sqrt(16)", "3 ** 2"
    """
    try:
        # Create a safe namespace with common math functions
        safe_dict = {
            'sqrt': math.sqrt,
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'log': math.log,
            'log10': math.log10,
            'exp': math.exp,
            'pi': math.pi,
            'e': math.e,
            'abs': abs,
            'round': round,
            'max': max,
            'min': min,
        }
        result = eval(expression, {"__builtins__": {}}, safe_dict)
        return f"Result: {result}"
    except Exception as e:
        return f"Error calculating expression: {str(e)}"
