from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="llama3.2",
    temperature=0.7
)

weather = input("Weather: ").lower()
budget = int(input("Budget: "))

if weather == "rain":
    activity = "indoor activities"
elif budget < 1000:
    activity = "local sightseeing"
else:
    activity = "premium outdoor activities"

prompt = f"""
You are an AI travel agent.

Recommend a simple travel plan involving {activity}.

Weather: {weather}
Budget: ₹{budget}

Give:
1. Recommended activity
2. Short explanation
3. Estimated spending
4. One useful travel tip
"""

result = llm.invoke(prompt)

print("\nTRAVEL RECOMMENDATION:")
print(result)