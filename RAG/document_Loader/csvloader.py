from langchain_community.document_loaders import CSVLoader  # type:ignore

loader = CSVLoader(file_path = "books/industry.csv")
res = loader.load()
# it basically create different objects for each row in the csv file
print(res[0].page_content)
print(res[0].metadata)