from langchain.tools import tool
from app.rag.pinecone_setup import get_vectorstore

vectorstore = get_vectorstore()
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

@tool
def rag_search(query: str) -> str:
    """
    Search the internal research database for relevant information.
    """
    docs = retriever.invoke(query)
    return "\n\n".join([doc.page_content for doc in docs])