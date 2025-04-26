# shell is used to run shell commands
from langchain_community.tools import ShellTool

shell_tool = ShellTool()

result = shell_tool.invoke("echo 'Hello, World!'")

print(result)