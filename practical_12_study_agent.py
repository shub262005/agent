from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="llama3.2",
    temperature=0.7
)

subject = input("Subject: ")
hours = int(input("Available hours: "))

prompt = f"""
You are an AI study planning agent.

Subject: {subject}
Available study time: {hours} hours

Break the study goal into smaller tasks.

Requirements:
1. Identify the important topics.
2. Break them into smaller tasks.
3. Assign approximate time to each task.
4. Prioritize difficult topics first.
5. Create a practical study schedule.

Give the final plan in a clear format.
"""

result = llm.invoke(prompt)

print("\nSTUDY PLAN:")
print(result)