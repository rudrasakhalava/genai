from langchain.tools import tool

@tool
def multiply(a : int , b : int) -> int:
    """Multiply two numbers"""
    return a*b

result = multiply.invoke({"a" : 3, "b" : 4})

print(result)