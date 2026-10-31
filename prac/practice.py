from langchain_core.prompts import PromptTemplate
from langchain_core.tools import tool
from langchain_ollama import ChatOllama


@tool
def calculator(a: float, b: float, operation: str) -> float:
    """Perform addition,subtraction,multiplication or diviison."""
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        "Invalid operation"


llm = ChatOllama(model="llama3.2", temperature=0)
llm_with_tools = llm.bind_tools([calculator])

query = input("ask a math question (e.g., multiply,division,etc) : ")

response = llm_with_tools.invoke(query)

if response.tool_calls:
    tool_call = response.tool_calls[0]
    print("Tool Called : ", tool_call["name"])
    print("Args : ", tool_call["args"])

    result = calculator.invoke(tool_call["args"])
    print("Result : ", result)
else:
    print("no tool called: ", response.content)
