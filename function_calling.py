import openai


functions = [
    {
        "name": "return_recipe",
        "description": "Return the recipe asked",
        "parameters": {
            "type": "object",
            "properties": {
                "ingredients": {
                    "type": "string",
                    "description": "The ingredients list."
                },
                "steps": {
                    "type": "string",
                    "description": "The recipe steps."
                },
            },
            },
            "required": ["ingredients","steps"],
        }
]

recipe = 'Fish and chips'
query = f"What is the recipe for {recipe}? Return the ingredients list and steps separately."


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=[{"role": "user", "content": query}],
    functions=functions,
    function_call={'name':'return_recipe'}
)
response_message = response["choices"][0]["message"]
print(response_message)
print(response_message['function_call']['arguments'])
