from langchain_ollama import OllamaLLM


llm = OllamaLLM(
    model="llama3.2",
    temperature=0.3
)


task = input("Programming requirement: ")


# Agent 1: Code Generator
code = llm.invoke(
    f"""
You are a Python code generation agent.

Write Python code for the following requirement:

{task}

Return only the Python code.
"""
)


# Agent 2: Code Reviewer
review = llm.invoke(
    f"""
You are a code review agent.

Review the following Python code:

{code}

Find:
1. Syntax errors
2. Logical errors
3. Possible improvements

If there are no major errors, state that clearly.
"""
)


print("\nGENERATED CODE:")
print(code)

print("\nCRITIC:")
print(review)