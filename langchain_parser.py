from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain.llms import GooglePalm, OpenAI


ingredients = ResponseSchema(
        name="ingredients",
        description="The ingredients from recipe, as a unique string.",
    )
steps = ResponseSchema(
        name="steps",
        description="The steps to prepare the recipe, as a unique string.",
    )

output_parser = StructuredOutputParser.from_response_schemas(
    [ingredients, steps]
)

response_format = output_parser.get_format_instructions()
print(response_format)

prompt = ChatPromptTemplate.from_template("What is the recipe for {recipe}? Return the ingredients list and steps separately. \n {format_instructions}")

llm_openai = OpenAI()
llm_palm = GooglePalm()

recipe = 'Fish and chips'

formated_prompt = prompt.format(**{"recipe":recipe, "format_instructions":output_parser.get_format_instructions()})

response_palm = llm_palm(formated_prompt)
response_openai = llm_openai(formated_prompt)

print("PaLM:")
print(response_palm)
print(output_parser.parse(response_palm))

print("Open AI:")
print(response_openai)
print(output_parser.parse(response_openai))
