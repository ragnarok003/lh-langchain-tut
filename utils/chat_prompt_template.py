from langchain_core.prompts import ChatPromptTemplate

chat_template=ChatPromptTemplate.from_messages([
    ("system","You are a professional blog writer. "),
    ("user","Write a blog about {topic} in {style} style. ")
])

print(chat_template.format_messages(topic="AI in Healthcare",style="friendly"))