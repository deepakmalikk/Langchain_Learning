from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://en.wikipedia.org/wiki/Wikipedia:Wiki_Game")

data = loader.load()
print(data)