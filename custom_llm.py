from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.openai import OpenAI
import openai

openai.log = 'debug'

# define LLM
llm = OpenAI(model="gpt-4", temperature=0, max_tokens=1000)

# configure service context
Settings.llm = llm

# load documents
documents = SimpleDirectoryReader('documents').load_data()

# create index
index = VectorStoreIndex.from_documents(documents)

# create chatbot
chat_engine = index.as_chat_engine(verbose=True, chat_mode='react')
chat_engine.chat_repl()