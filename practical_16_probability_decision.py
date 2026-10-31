from langchain_ollama import OllamaLLM


symptom_probability = {
    "mild": 0.2,
    "moderate": 0.5,
    "severe": 0.9
}


severity = input("Severity (mild/moderate/severe): ").lower()

risk = symptom_probability[severity]


if risk > 0.7:
    action = "Seek professional medical attention"
else:
    action = "Monitor symptoms"


llm = OllamaLLM(
    model="llama3.2",
    temperature=0.3
)


result = llm.invoke(
    f"Explain this recommendation simply: {action}"
)


print("\nRISK PROBABILITY:", risk)
print("RECOMMENDATION:", action)
print("\nLLM EXPLANATION:")
print(result)