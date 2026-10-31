from langchain_ollama import OllamaLLM


llm = OllamaLLM(
    model="llama3.2",
    temperature=0.5
)


topic = input("Research topic: ")


# Agent 1: Research Agent
research = llm.invoke(
    f"""
You are a research agent.

Research the following topic and provide important points:

{topic}

Give factual and useful points that can be used in a report.
"""
)


# Agent 2: Writer Agent
summary = llm.invoke(
    f"""
You are a report writing agent.

Convert the following research notes into
a short structured report.

Research Notes:
{research}

Include:
1. Introduction
2. Main Points
3. Conclusion
"""
)


print("\nResearch Agent:")
print(research)

print("\nWriter Agent:")
print(summary)