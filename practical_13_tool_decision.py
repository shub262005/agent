from langchain_core.tools import tool
from langchain_ollama import OllamaLLM


@tool
def difficulty(experience: int):
    """Select interview difficulty based on years of experience."""
    
    if experience < 2:
        return "Easy"
    else:
        return "Advanced"


llm = OllamaLLM(
    model="llama3.2",
    temperature=0.7
)

years = int(input("Years of experience: "))

level = difficulty.invoke({
    "experience": years
})

prompt = f"""
You are an interview preparation agent.

Generate 3 interview questions.

Candidate experience: {years} years
Difficulty: {level}

For each question:
- Give the question.
- Give the correct answer.
"""

result = llm.invoke(prompt)

print("\nINTERVIEW QUESTIONS:")
print(result)