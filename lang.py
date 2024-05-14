from langchain_community.vectorstores import PathwayVectorClient
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain

client = PathwayVectorClient(host="127.0.0.1", port=8754)

query = input("Enter your query: ")
docs = client.similarity_search(query)

for i in docs:
    print(i.page_content)


# model = Ollama(model="gemma:2b")


# prompt = ChatPromptTemplate.from_template(
#     """
#     you are a helpful assistant how answers the quesiton which is give to you.if you don't know the answer you can answer based on the context povided and 
#     if you don't find the answer in the context just say that you don't know.
#     <context>
#     {context}
#     </context>
#     Question: {input}
#     """
# )


# chain = create_stuff_documents_chain(model, prompt)

# retriver = client.as_retriever()

# retrival_chain = create_retrieval_chain(retriver,chain)

# response = retrival_chain.invoke({'input': 'what is the pathway'})

# print(response)