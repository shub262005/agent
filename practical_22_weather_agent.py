import requests
from langchain_ollama import OllamaLLM


city = input("Enter city: ")


url = f"https://wttr.in/{city}?format=j1"

response = requests.get(url)
data = response.json()


temp = data["current_condition"][0]["temp_C"]
weather = data["current_condition"][0]["weatherDesc"][0]["value"]


llm = OllamaLLM(
    model="llama3.2",
    temperature=0.5
)


result = llm.invoke(
    f"""
You are a weather advisory agent.

City: {city}
Weather: {weather}
Temperature: {temp} C

Give simple practical advice for someone visiting this city today.
Mention suitable clothing and one useful activity suggestion.
"""
)


print("\nWeather Information:")
print("City:", city)
print("Weather:", weather)
print("Temperature:", temp, "C")

print("\nAgent Advice:")
print(result)