from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

# load documents
documents = SimpleDirectoryReader('documents').load_data()

# create index
index = VectorStoreIndex.from_documents(documents)

# save index
index.storage_context.persist()