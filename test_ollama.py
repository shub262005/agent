from langchain_ollama import OllamaLLM

Ilm = OllamaLLM(
model="llama3.2",
temperature=0.7

)

response = Ilm.invoke("Explain Artificial Intelligence in simple words.")

print(response)