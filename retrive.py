from llama_index.retrievers.pathway import PathwayRetriever

from pathway.xpacks.llm.vector_store import VectorStoreClient

#from llama_index.readers.pathway import PathwayReader


retriever = PathwayRetriever(host="127.0.0.1", port=8754)
# results = retriever.retrieve("what is javascript")
# print(results)

from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.llms.ollama import Ollama

model = Ollama(model="gemma:2b",request_timeout=600)

query_engine = RetrieverQueryEngine.from_args(
    retriever,
    llm=model,
)
question = input("write a query:")
response = query_engine.query(str_or_query_bundle=question)
print(str(response))