from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

# load documents
docs = SimpleDirectoryReader(input_files=['./docs1/example - exported knowledge base.csv']).load_data()
docs[0].metadata['category'] = 'customer support'

# create index
index = VectorStoreIndex.from_documents(docs)

# save index
index.storage_context.persist()

# query
query_engine = index.as_query_engine(verbose=True)
response = query_engine.query('summarize our customer support content')
print(response)