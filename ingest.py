import os
from langchain_community.document_loaders import  PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter  # type: ignore[import]
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


DOCS_DIR = "docs"
VECTOR_DIR = "vectorstore"
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

def load_pdfs(folder):
    docs = []
    for file in os.listdir(folder):
        if file.endswith(".pdf"):
            path = os.path.join(folder, file)
            print(f"Loading: {file}")
            loader = PyMuPDFLoader(path)
            docs.extend(loader.load())
    print(f"Total pages loaded: {len(docs)}")
    return docs

def chunk_documents(docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=80,
        separators=["\n\n", "\n", " ", ""]
    )
    chunks= text_splitter.split_documents(docs)
    print(f"Total chunks created: {len(chunks)}")
    return chunks

def embed_and_store(chunks):
    print("loading embedding model(first run downloads ~80MB)")
    embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
    print("Embedding chunks into ChromaDB")
    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=VECTOR_DIR
    )
    print(f"Done. {len(chunks)} chunks embedded and stored in {VECTOR_DIR}")
    return vectordb

if __name__ == "__main__":
    print("\n === Solar Assistant - Knowledge Base Ingest ===\n")
    print("\n[1/3] Loading pdf's from docs folder")
    docs = load_pdfs(DOCS_DIR)
    print("\n[2/3] Chunking documents into smaller pieces")
    chunks = chunk_documents(docs)
    print("\n[3/3] Embedding chunks and Storing in ChromaDB")
    vectordb = embed_and_store(chunks)
    print("\n Knowledge Base ready. - Ingest complete.")