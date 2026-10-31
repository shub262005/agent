from langchain_core.tools import tool
from langchain_ollama import OllamaLLM


@tool
def refund():
    """handle refund requests."""
    return "refund ticket raised"


@tool
def technical_error():
    """handle techinical issues"""
    return "techincal support ticket raised"


llm = OllamaLLM(model="llama3.2", temperature=0.3)

query = input("Enter your problem : ")

if "refund" in query:
    result = refund.invoke({})
elif "error" in query or "not working" in query:
    result = technical_error.invoke({})
else:
    result = llm.invoke(
        f"""
            You are a customer support agent.

            Customer query:
            {query}

            provide a short and helpful response.
        """
    )

print("\nSupport Response : ")
print(result)
