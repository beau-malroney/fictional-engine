from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage

documents = SimpleDirectoryReader("documents").load_data()

# bge-base embedding model
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

# ollama
Settings.llm = Ollama(model="llama3", request_timeout=120.0)

index = VectorStoreIndex.from_documents(
    documents,
)

query_engine = index.as_query_engine()
print(query_engine.query("What can you tell me about zenva?"))

# def chatMessageTest():
#     messages = [
#         ChatMessage(
#             role="system", content="You are a pirate with a colorful personality"
#         ),
#         ChatMessage(role="user", content="What is your name"),
#     ]
#     resp = llm.chat(messages)
#     print(resp)
#     return


# def test_chat():
#     resp = llm.complete("Who is Paul Graham?")
#     print(resp)
#     return

# def testStream():
#     response = llm.stream_complete("Who is Paul Graham?")
#     for r in response:
#         print(r.delta, end="")
#     return

# def testStreamChatMessage():
#     messages = [
#         ChatMessage(
#             role="system", content="You are a pirate with a colorful personality"
#         ),
#         ChatMessage(role="user", content="What is your name"),
#     ]
#     resp = llm.stream_chat(messages)
#     for r in resp:
#         print(r.delta, end="")