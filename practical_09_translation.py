from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

# Initialize Ollama LLM
llm = OllamaLLM(
    model="llama3.2",
    temperature=0.2
)

# Create prompt template
prompt = PromptTemplate.from_template(
    "Translate this text into {language}:\n{text}"
)

# Create chain
chain = prompt | llm

# Take input from user
text = input("Text: ")
language = input("Language: ")

# Generate translation
result = chain.invoke({
    "text": text,
    "language": language
})

# Display result
print("\nTRANSLATION:")
print(result)