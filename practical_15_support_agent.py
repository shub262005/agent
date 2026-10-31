from langchain_core.tools import tool
from langchain_ollama import OllamaLLM


@tool
def refund():
    """Handle refund request."""
    return "Refund request registered."


@tool
def technical():
    """Handle technical issue."""
    return "Technical support ticket created."


llm = OllamaLLM(
    model="llama3.2",
    temperature=0.3
)

query = input("Customer query: ").lower()


if "refund" in query:
    result = refund.invoke({})

elif "error" in query or "not working" in query:
    result = technical.invoke({})

else:
    result = llm.invoke(f"""
You are a customer support assistant.

Customer query:
{query}

Provide a short and helpful response.
""")


print("\nSUPPORT RESPONSE:")
print(result)