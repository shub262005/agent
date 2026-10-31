from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

# Initialize the OllamaLLM model
llm = OllamaLLM(model='llama3.2',temperature=0)

# Define a function to extract important keywords from a text
def extract_keywords(text):
    # Generate a prompt to ask the model to find keywords
    prompt = PromptTemplate.from_template(
        """
        Find the 5 most important keywords in this text: {text} and just return those words'
        """
    )
    chain = prompt | llm
    # Use the model to generate a response
    response = chain.invoke({"text":text})
    return response
    # Extract the keywords from the response
    

    

# Test the function with a sample text
text = 'The new policy aims to reduce carbon emissions by 50% by 2030. The government has pledged to invest $10 billion in renewable energy projects.'
print(extract_keywords(text))