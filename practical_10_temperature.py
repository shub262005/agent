from langchain_ollama import OllamaLLM

# Low temperature
low = OllamaLLM(
    model="llama3.2",
    temperature=0.1
)

# High temperature
high = OllamaLLM(
    model="llama3.2",
    temperature=1.0
)

# Prompt
prompt = "Write a creative sentence about AI."

# Generate responses
low_result = low.invoke(prompt)
high_result = high.invoke(prompt)

# Display results
print("========================================")
print("       TEMPERATURE COMPARISON")
print("========================================")

print("\nLow Temperature (0.1):")
print(low_result)

print("\nHigh Temperature (1.0):")
print(high_result)