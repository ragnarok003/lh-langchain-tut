from langchain_community.document_loaders import CSVLoader
loader =CSVLoader(file_path="docs/clg_db.students.csv")

data =loader.load()

for datum in data:
    print(datum)