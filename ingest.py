from langchain_community.document_loaders import ArxivLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.rag.pinecone_setup import get_vectorstore

loader = ArxivLoader(query="large language models", load_max_docs=10)
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=200
)

chunks = splitter.split_documents(docs)

vectorstore = get_vectorstore()
vectorstore.add_documents(chunks)

print("Ingestion complete!")