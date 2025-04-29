from langchain_core.tools import tool
# we have to make functionality of 2 or more than 2 tools.
# then it will called as toolkit.

# building Custom tools with the help of tool decorator, wecan use another method

@tool #first tool to add two numbers
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@tool#second tool to multiply two numbers
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

class MathToolkit:
    def get_tools(self):
        return [add, multiply]
    
toolkit = MathToolkit()
tools = toolkit.get_tools()

for tool in tools:
    print(tool.name, "=>", tool.description)