from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate,HumanMessagePromptTemplate
from langchain_ollama import ChatOllama
from rich.console import Console
from rich.markdown import Markdown
console=Console()
chat_model=ChatOllama(model="gemma4")
print("Blog Post Generator")
print("Provide ideas or topics for the blog post. Type exit to finish.")

topic =input("Enter blog post topic: ")
chat_prompt_template=ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("You are a professtional blog writer. Help generate informative, engaging and will structured blog post about a {topic}."),
    HumanMessagePromptTemplate.from_template("Write a detailed blog post about {topic}.")
])

chat_history=[]
while True:
    user_input=input("Ideas or instruction or type exit: ")
    if user_input.lower()=="exit":
        print("Exiting blog post generator.")
        break

    messages=chat_prompt_template.format_messages(topic=topic)
    for prev in chat_history:
        messages.append(prev)

    messages.append(HumanMessagePromptTemplate.from_template(user_input).format_messages(user_input=user_input)[0])

    response=chat_model.invoke(messages)
    print("Blog Post Content:\n")
    console.print(Markdown(response.content))

