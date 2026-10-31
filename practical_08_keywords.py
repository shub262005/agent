from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

# Initialize Ollama LLM
llm = OllamaLLM(
    model="llama3.2",
    temperature=0
)

# Create prompt template
prompt = PromptTemplate.from_template(
    "Extract 5 important keywords from the following text:\n{text}"
)

# Create chain
chain = prompt | llm

# Take text from user
text = input("Enter text: ")

# Generate keywords
result = chain.invoke({
    "text": text
})

# Display result
print("\nIMPORTANT KEYWORDS:")
print(result)