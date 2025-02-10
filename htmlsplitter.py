from langchain_text_splitters import HTMLHeaderTextSplitter

mydata=""
with open('index.html','r') as file:
   mydata = file.read()
headers_to_split_on = [(
    "h1","header1"),
   
    ]

htmlsplitter=HTMLHeaderTextSplitter(headers_to_split_on,)
splittedText=htmlsplitter.split_text(mydata)
print(splittedText)