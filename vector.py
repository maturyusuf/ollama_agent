from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
from pypdf import PdfReader

reader = PdfReader("data/summary.pdf")
text = ""

for page in reader.pages:
    text += page.extract_text()

embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chroma_langchain_db"

add_documents = not os.path.exists(db_location)

if(add_documents):
    documents = []
    ids = []
    
for i, sentence in enumerate(text.split(".")):
    documents.append(Document(page_content=sentence,
                              id=str(i),
                              metadata={"source": "summary.pdf"}))
    ids.append(str(i))
    
vector_store = Chroma(
    collection_name="summary",
    persist_directory=db_location,
    embedding_function=embeddings,
)

if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)
    
retriever = vector_store.as_retriever(search_kwargs={"k": 1})

    

