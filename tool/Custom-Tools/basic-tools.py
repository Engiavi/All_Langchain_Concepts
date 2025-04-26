from langchain_core.tools import tool

""" to make a tool we need to follow 3 steps
1. create a function or write logic
2. add type hints
3. add tool decorator
"""
# Step 1 - create a function

def multiply(a, b):
    """Multiply two numbers"""
    return a*b

# Step 2 - add type hints

def multiply(a: int, b:int) -> int:
    """Multiply two numbers"""
    return a*b

# Step 3 - add tool decorator

@tool # this decorator plays a crucial role here, it makes the function as special function and helps to communicate with the LLMs
def multiply(a: int, b:int) -> int:
    """Multiply two numbers"""
    return a*b

result = multiply.invoke({"a":3, "b":5})# multiply function becomes tool function, hence it supports runnable. therefore it has methods like invoke

print(result)
print(multiply.name)
print(multiply.description)
print(multiply.args)
print(multiply.args_schema.model_json_schema())