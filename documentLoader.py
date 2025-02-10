from langchain_community.document_loaders.csv_loader import CSVLoader

loader = CSVLoader(
   'myfile.pdf'
)
data = loader.load()
print(data)