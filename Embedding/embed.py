from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model="deepseek-r1:1.5b",
)

embeed = embeddings.embed_query("hello world")
print(len(embeed))