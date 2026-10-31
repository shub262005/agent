from langchain_core.tools import tool
from langchain_ollama import OllamaLLM

@tool
def calculator(a: float, b: float, operation: str) -> float:
    """Perform addition, subtraction, multiplication or division."""
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        return "Invalid operation"

llm = OllamaLLM(model="llama3.2", temperature=0)

question = input("Enter first number: ")
a = float(question)

b = float(input("Enter second number: "))
operation = input("Enter operation (add/subtract/multiply/divide): ")

result = calculator.invoke({
    "a": a,
    "b": b,
    "operation": operation
})

print("Result:", result)
