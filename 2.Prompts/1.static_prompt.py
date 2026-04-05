from langchain_core.prompts import PromptTemplate

static_prompt = PromptTemplate(
    input_variables=[], template="write a short fun fact about AI"
)
prompt_text=static_prompt.format()
print(prompt_text)