from langchain_core.prompts import PromptTemplate

template = "Write a short blog post about {topic} in a {style} style."
prompt = PromptTemplate(input_variables=["topic", "style"], template=template)

print(prompt.format(topic="AI in Education",style="informative"))