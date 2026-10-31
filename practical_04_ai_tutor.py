from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

# Initialize Ollama LLM
llm = OllamaLLM(model="llama3.2", temperature=0.7)

# Create prompt template
prompt = PromptTemplate.from_template(
    """
    You are an AI tutor.

    Explain {topic} to a {level} student.
    Use simple and easy-to-understand language.
    Give a clear explanation with a suitable example.
    """
)

# Create LangChain
chain = prompt | llm

# Take input from user
topic = input("Topic: ")
level = input("Level (beginner/intermediate): ")

# Generate explanation
result = chain.invoke({"topic": topic, "level": level})

# Display result
print("\n========================================")
print("           AI TUTOR RESPONSE")
print("========================================")
print(result)
