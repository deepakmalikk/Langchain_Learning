mydata= ""

with open('split.txt','r') as file:
    mydata=file.read()

# from langchain_text_splitters import RecursiveCharacterTextSplitter


# text_split = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=10)
# splittedText= text_split.split_text(mydata)
# print(splittedText)

from langchain_text_splitters import CharacterTextSplitter

splitter = CharacterTextSplitter(separator="\n\n", chunk_size=100, chunk_overlap=20)
splittedText= splitter.split_text(mydata)

print(splittedText)
