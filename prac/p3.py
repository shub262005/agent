
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

llm = OllamaLLM(model="llama3.2",temperature=0.7)

weather = input("Enter Weather : ")
budget = int(input("Enter budget : "))

if weather =="rainy":
    activity = "indoor activity"
elif budget < 1000:
    activity = "local sight seeing"    
else :
    activity = "premium outdoor activity"
prompt = PromptTemplate.from_template(
    """ 
    You are a travel agent.
    Recommend a simple plan involving this activity:{activity} suitable for this weather{weather} & budget is {budget}.

    Give:
    1.Recommneded activity
    2.Short description
    3.Estimated Spending
    4.One useful tip

    """
)

chain = prompt | llm

result = chain.invoke({
    "activity":activity,
    "weather":weather,
    "budget":budget
})

print("+++++++++++++++++++++++++++++")
print(result)