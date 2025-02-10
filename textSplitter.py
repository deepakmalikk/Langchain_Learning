from langchain_text_splitters import RecursiveCharacterTextSplitter

mydata= ""

with open('split.txt','r') as file:
    mydata=file.read()
text_split = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=10)
splittedText= text_split.split_text(mydata)
print(splittedText)