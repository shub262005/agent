from langchain_ollama import OllamaLLM


llm = OllamaLLM(
    model="llama3.2",
    temperature=0.3
)


task = input("Enter task: ")


# Supervisor Agent
expert = llm.invoke(
    f"""
You are a supervisor agent.

Choose the best specialist for the task.

Available specialists:
MATH
PYTHON
WRITING

Task:
{task}

Return only one specialist name:
MATH, PYTHON, or WRITING.
"""
).strip().upper()


# Routing
if "MATH" in expert:
    specialist = "MATH"

elif "PYTHON" in expert:
    specialist = "PYTHON"

elif "WRITING" in expert:
    specialist = "WRITING"

else:
    specialist = "WRITING"


print("\nSupervisor selected:", specialist)


# Specialized Agent
answer = llm.invoke(
    f"""
You are a {specialist} specialist.

Solve the following task:

{task}

Provide a clear and useful answer.
"""
)


print("\nSpecialist Agent:")
print(answer)