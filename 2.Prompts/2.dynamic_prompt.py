from langchain_core.prompts import PromptTemplate

dynamic_prompt = PromptTemplate(
    template="Write a short paragraph about {topic} in a {style} style.",
    input_variables=["topic", "style"],
)

prompt_text1 = dynamic_prompt.format(topic="AI",style="humorous")
prompt_text2 = dynamic_prompt.format(topic="Block Chain",style="humorous")
print(prompt_text1)
print(prompt_text2)

