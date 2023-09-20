import openai

recipe = 'Fish and chips'
query = f"What is the recipe for {recipe}? Return the ingredients list and steps separately."

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=[{"role": "user", "content": query}])

response_message = response["choices"][0]["message"]
print(response_message)

print(response_message['content'])
