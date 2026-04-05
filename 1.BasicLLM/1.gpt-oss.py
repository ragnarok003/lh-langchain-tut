from langchain_ollama import ChatOllama

llm=ChatOllama(model="gpt-oss")

response =llm.invoke("Explain Langchain in one sentence.")
print(response.content)
