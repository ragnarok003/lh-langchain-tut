from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(
            "You are a helpful assistant that provides information about {subject}."
        ),
        HumanMessagePromptTemplate.from_template(
            "Can you tell me something intresting about {subject}?"
        ),
    ]
)


prompt=chat_prompt_template.format_messages(subject="Quantum Computing")
print(prompt)