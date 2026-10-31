from langchain_core.tools import tool


@tool
def multiply(a: int, b: int):
    """Multiply two numbers."""
    return a * b


a = int(input("First number: "))
b = int(input("Second number: "))


print("\nThought: Need multiplication")
print("Action: multiply")


result = multiply.invoke({
    "a": a,
    "b": b
})


print("Observation:", result)
print("Final Answer:", result)