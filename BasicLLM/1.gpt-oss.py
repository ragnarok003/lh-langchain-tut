from langchain_ollama import ChatOllama

llm=ChatOllama(model="gpt-oss")

response =llm.invoke("Hello, Langchain! Explain yourself in one sentence.")
print(response.content)
