from langchain_ollama import OllamaLLM


llm = OllamaLLM(
    model="llama3.2",
    temperature=0.5
)


task = input("Enter task: ")


# Planning
plan = llm.invoke(
    f"""
Create exactly 3 steps to complete the following task:

{task}

Clearly number the three steps.
"""
)


# Execution
execution = llm.invoke(
    f"""
Execute this plan conceptually.

Plan:
{plan}

Give the expected outcome of completing the plan.
"""
)


print("\nPLAN:")
print(plan)

print("\nEXECUTION:")
print(execution)