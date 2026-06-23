import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFaceEndpoint, ChatHuggingFace
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

VECTOR_DIR = "vectorstore"
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL =os.getenv("LLM_MODEL")


print(LLM_MODEL)
# SYSTEM_PROMPT = """You are a Solar energy feasibility assistant for rural and semi-urban users in india. 
# Answer ONLY using the retrieved document context provided below.
# Always cite the source document for each recommendation.
# If the contect does not contain enough information to answer, say so clearly.
# Do not make up cost figures, policy names and subsidy amounts.
# End every response with : "Consult a BEE - certified solar installer for final asssessment."

# Context: 
# {context}

# """

# def load_retriever():
#     embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
#     db = Chroma(persist_directory=VECTOR_DIR, embedding_function=embeddings)
#     return db.as_retriever(search_kwargs={"k": 5})

# def load_llm():

#     return ChatOllama(model=LLM_MODEL, temperature=0.3)
#     # endpoint = HuggingFaceEndpoint(
#     #     repo_id=LLM_MODEL,
#     #     task="text-generation",
#     #     temperature=0.3,
#     #     max_new_tokens= 512,
#     #     huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
#     #     )
#     # return ChatHuggingFace(llm=endpoint)

# def format_docs(docs):
#     formatted = []
#     for d in docs:
#         source = d.metadata.get("source", "unknown")
#         formatted.append(f"Source:{source}\n{d.page_content}")
#     return "\n\n".join(formatted)

# def build_rag_chain():
#     retriever = load_retriever()
#     llm = load_llm()

#     prompt = ChatPromptTemplate.from_messages([
#         ("system", SYSTEM_PROMPT),
#         ("human", "{question}")
#     ])

#     chain = (
#         {"context" : retriever | format_docs, "question": RunnablePassthrough()}
#         | prompt
#         | llm
#         |StrOutputParser()
#     )
#     return chain

# if __name__ == "__main__":
#     print("\n === Solar energy feasibility assistant - RAG test === \n")
#     chain = build_rag_chain()

#     test_query = "I have 500 sq ft rooftop in Hyderabad, monthly bill 3200 rupees, wants to power lights and a pump."
#     print(f"Query: {test_query}\n")
#     print("Generating answer...\n")

#     answer = chain.invoke(test_query)
#     print("---- Answer ----\n")
#     print(answer)

