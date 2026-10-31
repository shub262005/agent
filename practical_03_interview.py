from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

# Initialize Ollama LLM
llm = OllamaLLM(
    model="llama3.2",
    temperature=0.7
)

# Create prompt template
prompt = PromptTemplate.from_template(
    """
    Generate exactly 5 interview questions on the topic: {topic}

    Number the questions from 1 to 5.
    Return only the interview questions.
    """
)

# Create LangChain
chain = prompt | llm

# Take topic from user
topic = input("Enter subject: ")

# Generate questions
result = chain.invoke({
    "topic": topic
})

# Display result
print("\n========================================")
print("       INTERVIEW QUESTIONS")
print("========================================")
print(result)