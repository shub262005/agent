from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

llm = OllamaLLM(
    model="llama3.2",
    temperature=0.3
)

prompt = PromptTemplate.from_template(
    """
    Summarize the following text in exactly 1 sentences.

    Text:
    {text}
    """
)

chain = prompt | llm

text = input("Enter text: ")

result = chain.invoke({
    "text": text
})

print("\nSUMMARY:")
print(result)