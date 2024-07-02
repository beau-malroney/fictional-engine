from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

# load documents
documents = SimpleDirectoryReader('documents').load_data()

# create index
index = VectorStoreIndex.from_documents(documents)

# create chatbot
chat_engine = index.as_chat_engine(verbose=True, chat_mode='react')
chat_engine.chat_repl()