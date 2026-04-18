from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
import logging
import json

# Setup logging
logging.basicConfig(
    filename='docs/pdf.log',
    level=logging.INFO,
    encoding='utf-8',
    format='%(message)s'  # important: removes extra log clutter
)

# Load PDFs
loader = DirectoryLoader(
    path="docs",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

# docs = loader.load()
docs = loader.lazy_load()

# Collect metadata
metadata_list = [doc.metadata for doc in docs]

# Pretty print JSON to log file
pretty_json = json.dumps(metadata_list, indent=1, ensure_ascii=False)
logging.info(pretty_json)

