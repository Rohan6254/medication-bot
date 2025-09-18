
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List 
from langchain.schema import Document
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_huggingface import HuggingFaceEmbeddings




#load
def load_pdf_files(data):
    loader = DirectoryLoader(
    data,
    glob="*.pdf",
    loader_cls=PyPDFLoader
)
    documents = loader.load()
    return documents
#filter
def filter_to_minimal_docs(docs: List[Document]) -> List[Document]:
    minimal_docs: List[Document]=[]
    for doc in docs:
        src=doc.metadata.get("source")
        minimal_docs.append(
            Document(
                page_content=doc.page_content,
                metadata={"source":src}
            )
        )
    return minimal_docs
    
#chunking
def text_split(minimal_docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20,
    )
    texts_chunk= text_splitter.split_documents(minimal_docs)
    return texts_chunk

#downloade
def download_embeddings():
    
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    return embeddings
embeddings=download_embeddings()